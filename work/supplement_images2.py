# 修正下载失败的根因：URL 带了 utm 查询参数，且指向 upload 域（持续 429）
#
# 交接报告 §7.2 第 3 条：upload.wikimedia.org 对本站持续 429，
# 必须改写成 thumb.wikimedia.org/.../thumb/d/df/NAME.jpg/960px-NAME.jpg，
# 且路径里必须保留 /thumb/。
#
# 本轮 API 返回的 url 还带了 ?utm_source=… 查询串，也要剥掉，否则拼出来的路径不合法。
import io
import os
import re
import ssl
import time
import urllib.request

import yaml

from commons_client import api

OUT = 'public/img/ships'
WIDTH = 1280
PROXY = 'http://127.0.0.1:12450'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
opener = urllib.request.build_opener(
    urllib.request.ProxyHandler({'http': PROXY, 'https': PROXY}),
    urllib.request.HTTPSHandler(context=ctx))


def strip_tags(s):
    import html
    if not s:
        return ''
    return html.unescape(re.sub(r'<[^>]+>', '', str(s))).strip()


def clean(u):
    """剥掉查询串"""
    return u.split('?')[0] if u else u


def to_thumb(u, width=WIDTH):
    """upload.wikimedia.org/wikipedia/commons/d/df/N.jpg
       → thumb.wikimedia.org/wikipedia/commons/thumb/d/df/N.jpg/1280px-N.jpg"""
    u = clean(u)
    if not u:
        return None
    if '/thumb/' in u:
        return u
    m = re.match(r'https?://upload\.wikimedia\.org(/wikipedia/commons)/(.)/(..)/([^/]+)$', u)
    if not m:
        return None
    base, h1, h2, fname = m.groups()
    stem = fname.rsplit('.', 1)[0]
    return f'https://thumb.wikimedia.org{base}/thumb/{h1}/{h2}/{fname}/{width}px-{stem}.jpg'


def try_urls(urls, tries=3):
    for attempt in range(tries):
        for u in urls:
            if not u:
                continue
            try:
                req = urllib.request.Request(u, headers={
                    'User-Agent': 'DockyardArchive/1.0 (research; contact via site)',
                    'Referer': 'https://commons.wikimedia.org/'})
                with opener.open(req, timeout=150) as f:
                    data = f.read()
                if data[:2] == b'\xff\xd8' or data[:4] == b'\x89PNG':
                    return data, u
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    time.sleep(8 * (attempt + 1))
                else:
                    time.sleep(2)
            except Exception:
                time.sleep(3)
    return None, None


def cat_files(cat, limit=500):
    j = api({'action': 'query', 'list': 'categorymembers',
             'cmtitle': 'Category:' + cat, 'cmtype': 'file',
             'cmlimit': str(limit), 'format': 'json'})
    return [m['title'] for m in (j.get('query', {}).get('categorymembers') or [])]


def file_infos(titles, batch=10):
    out = {}
    for i in range(0, len(titles), batch):
        j = api({'action': 'query', 'titles': '|'.join(titles[i:i + batch]),
                 'prop': 'imageinfo', 'iiprop': 'url|size|extmetadata',
                 'iiurlwidth': str(WIDTH), 'format': 'json'})
        for _, p in (j.get('query', {}).get('pages') or {}).items():
            ii = (p.get('imageinfo') or [None])[0]
            if ii:
                out[p.get('title')] = ii
        time.sleep(1.5)
    return out


TARGETS = {
    'nagara': (['Nagara (ship, 1922)', 'Nagara class cruiser'], ['nagara']),
    'sendai': (['Sendai (ship, 1924)', 'Sendai class cruiser'], ['sendai']),
    'vincennes': (['USS Vincennes (CA-44)'], ['vincennes']),
    'hammann': (['USS Hammann (DD-412)'], ['hammann']),
    'monaghan': (['USS Monaghan (DD-354)'], ['monaghan']),
}

prev = yaml.safe_load(io.open('work/_ship_images_filtered.yaml', encoding='utf-8'))['ships']
existing_files = set(os.listdir(OUT))

for sid, (cats, names) in TARGETS.items():
    cur = prev.get(sid) or []
    if len(cur) >= 10:
        continue
    have = {str(it.get('commons_title') or '') for it in cur}
    print(f'\n===== {sid}（现有 {len(cur)}）')
    gained = 0
    for cat in cats:
        if len(cur) + gained >= 15:
            break
        try:
            files = cat_files(cat)
        except Exception as e:
            print(f'   {cat}: 失败 {type(e).__name__}')
            continue
        time.sleep(1.5)
        cand = [f for f in files
                if f not in have
                and os.path.splitext(f)[1].lower() in ('.jpg', '.jpeg', '.png')]
        if not cand:
            continue
        infos = file_infos(cand)
        for ft in cand:
            if len(cur) + gained >= 15:
                break
            ii = infos.get(ft)
            if not ii:
                continue
            md = ii.get('extmetadata') or {}
            lic = strip_tags(md.get('LicenseShortName', {}).get('value', ''))
            l = lic.lower()
            if not ('public domain' in l or 'cc0' in l or 'pd' in l.split(';')[0]):
                continue
            blob = (ft + ' ' + strip_tags(md.get('ImageDescription', {}).get('value', ''))[:250]).lower()
            if not any(n in blob for n in names):
                continue
            urls = [to_thumb(ii.get('thumburl')), to_thumb(ii.get('url')),
                    ii.get('thumburl'), ii.get('url')]
            data, _ = try_urls(urls)
            if not data:
                print(f'      拿不到 {ft[:56]}')
                continue
            base = re.sub(r'[^A-Za-z0-9]+', '-', ft.replace('File:', '').rsplit('.', 1)[0]).strip('-')[:48]
            idx = len(cur) + gained + 1
            fn = f'{sid}-{idx:02d}-{base}.jpg'
            if fn in existing_files:
                continue
            with open(os.path.join(OUT, fn), 'wb') as f:
                f.write(data)
            existing_files.add(fn)
            cur.append({
                'file': f'/img/ships/{fn}', 'subject': f'ship:{sid}',
                'commons_title': ft, 'license_raw': lic,
                'author': strip_tags(md.get('Artist', {}).get('value', ''))[:120],
                'credit': strip_tags(md.get('Credit', {}).get('value', ''))[:120],
                'source_url': 'https://commons.wikimedia.org/wiki/' + ft.replace(' ', '_'),
                'width': ii.get('width'), 'height': ii.get('height'),
                'descr': strip_tags(md.get('ImageDescription', {}).get('value', ''))[:300],
                'date': strip_tags(md.get('DateTimeOriginal', {}).get('value', ''))[:40],
            })
            gained += 1
            print(f'      + {fn} ({len(data)//1024}KB)')
            time.sleep(2.5)
    prev[sid] = cur
    print(f'   → {len(cur)} 张')

with io.open('work/_ship_images_filtered.yaml', 'w', encoding='utf-8', newline='\n') as f:
    yaml.safe_dump({'ships': prev}, f, allow_unicode=True, sort_keys=False,
                   default_flow_style=False, indent=2, width=200)

print('\n===== 最终 =====')
tot = 0
for sid, items in prev.items():
    n = len(items)
    tot += n
    print(f'  {sid:14} {n:>2}' + ('  ← 仍不足' if n < 10 else ''))
print(f'  合计 {tot}')
