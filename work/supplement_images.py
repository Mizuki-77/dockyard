# 给数量不足的 5 艘补图：重试失败项 + 查子分类
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

SHORT = {
    'nagara': ['Nagara (ship, 1922)', 'Nagara class cruiser'],
    'sendai': ['Sendai (ship, 1924)', 'Sendai class cruiser'],
    'vincennes': ['USS Vincennes (CA-44)', 'New Orleans class cruiser'],
    'hammann': ['USS Hammann (DD-412)', 'Sims class destroyer'],
    'monaghan': ['USS Monaghan (DD-354)', 'Farragut class destroyer'],
}


def strip_tags(s):
    import html
    if not s:
        return ''
    return html.unescape(re.sub(r'<[^>]+>', '', str(s))).strip()


def cat_files(cat, limit=500):
    j = api({'action': 'query', 'list': 'categorymembers',
             'cmtitle': 'Category:' + cat, 'cmtype': 'file',
             'cmlimit': str(limit), 'format': 'json'})
    return [m['title'] for m in (j.get('query', {}).get('categorymembers') or [])]


def file_infos(titles, batch=20):
    out = {}
    for i in range(0, len(titles), batch):
        j = api({'action': 'query', 'titles': '|'.join(titles[i:i + batch]),
                 'prop': 'imageinfo', 'iiprop': 'url|size|extmetadata',
                 'iiurlwidth': str(WIDTH), 'format': 'json'})
        for _, p in (j.get('query', {}).get('pages') or {}).items():
            ii = (p.get('imageinfo') or [None])[0]
            if ii:
                out[p.get('title')] = ii
        time.sleep(1.2)
    return out


def rewrite_thumb(url):
    if '/thumb/' in url:
        return url
    m = re.match(r'https?://upload\.wikimedia\.org(/wikipedia/commons)/(.)/(..)/([^/]+)$', url)
    if not m:
        return url
    base, h1, h2, fname = m.groups()
    stem = fname.rsplit('.', 1)[0]
    return f'https://thumb.wikimedia.org{base}/thumb/{h1}/{h2}/{fname}/{WIDTH}px-{stem}.jpg'


def fetch_bytes(urls, tries=2):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler({'http': PROXY, 'https': PROXY}),
        urllib.request.HTTPSHandler(context=ctx))
    for attempt in range(tries):
        for u in urls:
            try:
                req = urllib.request.Request(u, headers={'User-Agent': 'DockyardArchive/1.0'})
                with opener.open(req, timeout=120) as f:
                    data = f.read()
                if data[:2] == b'\xff\xd8' or data[:4] == b'\x89PNG':
                    return data
            except Exception:
                time.sleep(3)
        time.sleep(4)
    return None


VARIANTS = {
    'nagara': ['nagara'],
    'sendai': ['sendai'],
    'vincennes': ['vincennes'],
    'hammann': ['hammann'],
    'monaghan': ['monaghan'],
}

prev = yaml.safe_load(io.open('work/_ship_images_filtered.yaml', encoding='utf-8'))['ships']
# 已下过的 Commons 原名
have = {}
for sid, items in prev.items():
    have[sid] = {str(it.get('commons_title') or '') for it in items}

# 已有的落盘文件
existing_files = set(os.listdir(OUT))

added = {}
for sid, cats in SHORT.items():
    cur = len(prev.get(sid) or [])
    if cur >= 10:
        continue
    print(f'\n===== {sid}（现有 {cur}）')
    new_items = []
    for cat in cats:
        try:
            files = cat_files(cat)
        except Exception as e:
            print(f'   {cat}: 失败 {type(e).__name__}')
            continue
        time.sleep(1.5)
        cand = [f for f in files
                if not f.lower().endswith(('.ogv', '.webm', '.ogg'))
                and os.path.splitext(f)[1].lower() in ('.jpg', '.jpeg', '.png')
                and f not in have[sid]]
        if not cand:
            print(f'   {cat}: 无新候选（{len(files)} 个文件）')
            continue
        print(f'   {cat}: 新候选 {len(cand)}')
        infos = file_infos(cand)
        time.sleep(1.5)
        names = VARIANTS[sid]
        for ft in cand:
            if cur + len(new_items) >= 15:
                break
            ii = infos.get(ft)
            if not ii:
                continue
            md = ii.get('extmetadata') or {}
            lic = strip_tags(md.get('LicenseShortName', {}).get('value', ''))
            l = lic.lower()
            if not ('public domain' in l or 'cc0' in l or 'pd' in l.split(';')[0]):
                continue
            blob = (ft + ' ' + strip_tags(md.get('ImageDescription', {}).get('value', ''))[:200]).lower()
            if not any(n in blob for n in names):
                continue
            urls = []
            if ii.get('thumburl'):
                urls.append(ii['thumburl'])
            if ii.get('url'):
                urls.append(rewrite_thumb(ii['url']))
            data = fetch_bytes(urls)
            if not data:
                print(f'      拿不到 {ft[:56]}')
                continue
            base = re.sub(r'[^A-Za-z0-9]+', '-', ft.replace('File:', '').rsplit('.', 1)[0]).strip('-')[:48]
            idx = cur + len(new_items) + 1
            fn = f'{sid}-{idx:02d}-{base}.jpg'
            if fn in existing_files:
                continue
            with open(os.path.join(OUT, fn), 'wb') as f:
                f.write(data)
            existing_files.add(fn)
            new_items.append({
                'file': f'/img/ships/{fn}',
                'subject': f'ship:{sid}',
                'commons_title': ft,
                'license_raw': lic,
                'author': strip_tags(md.get('Artist', {}).get('value', ''))[:120],
                'credit': strip_tags(md.get('Credit', {}).get('value', ''))[:120],
                'source_url': 'https://commons.wikimedia.org/wiki/' + ft.replace(' ', '_'),
                'width': ii.get('width'),
                'height': ii.get('height'),
                'descr': strip_tags(md.get('ImageDescription', {}).get('value', ''))[:300],
                'date': strip_tags(md.get('DateTimeOriginal', {}).get('value', ''))[:40],
            })
            print(f'      + {fn} ({len(data)//1024}KB)')
            time.sleep(2)
    added[sid] = new_items
    print(f'   → 补 {len(new_items)} 张，总 {cur + len(new_items)}')

# 合并回去
for sid, items in added.items():
    if items:
        prev[sid] = (prev.get(sid) or []) + items

with io.open('work/_ship_images_filtered.yaml', 'w', encoding='utf-8', newline='\n') as f:
    yaml.safe_dump({'ships': prev}, f, allow_unicode=True, sort_keys=False,
                   default_flow_style=False, indent=2, width=200)

print('\n===== 补图后 =====')
tot = 0
for sid, items in prev.items():
    n = len(items)
    tot += n
    print(f'  {sid:14} {n:>2}' + ('  ← 仍不足' if n < 10 else ''))
print(f'  合计 {tot}')
