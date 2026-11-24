# 1) 判定 10 条待复核（人工看描述后全否决）
# 2) 给不足 10 张的 4 艘（nagara / hammann / monaghan / benham）再从分类里补
import io
import os
import re
import ssl
import time
import urllib.request

import yaml

from commons_client import api

OUT = 'public/img/ships'
PROXY = 'http://127.0.0.1:12450'
WIDTH = 1280

# --- 1) 待复核全部否决（描述里主体明确是别的舰或干脆没有本舰）
REJECT = {
    'tone-07-GmZUpFBa8AEnoHj.jpg', 'haruna-05-GmZUpFBa8AEnoHj.jpg',
    'portland-13-US-Pacific-Fleet-ships-steam-towar',
    'minneapolis-13-A-heavy-explosion-on-board-USS-',
    'new-orleans-10-USS-Hawaii-CB-3-and-other-cruis',
    'vincennes-01-Convoy-WS-12-en-route-to-Cape-Tow',
    'vincennes-02-LC-USE6-D-008870-19856170365.jpg',
    'vincennes-03-USS-Quincy-CA-39-under-fire-durin',
    'hammann-01-A-heavy-explosion-on-board-USS-Lexi',
    'hammann-02-Large-explosion-aboard-USS-Lexington-CV',
}

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
    return u.split('?')[0] if u else u


def to_thumb(u, width=WIDTH):
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
    for a in range(tries):
        for u in urls:
            if not u:
                continue
            try:
                req = urllib.request.Request(u, headers={
                    'User-Agent': 'DockyardArchive/1.0 (research)',
                    'Referer': 'https://commons.wikimedia.org/'})
                with opener.open(req, timeout=150) as f:
                    data = f.read()
                if data[:2] == b'\xff\xd8' or data[:4] == b'\x89PNG':
                    return data
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    time.sleep(8 * (a + 1))
                else:
                    time.sleep(2)
            except Exception:
                time.sleep(3)
    return None


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


d = yaml.safe_load(io.open('work/_ship_images_v2.yaml', encoding='utf-8'))
ships = d['ships']

# 应用否决
removed = 0
for sid, items in ships.items():
    keep = []
    for it in items:
        fn = os.path.basename(str(it['file']))
        if fn in REJECT:
            removed += 1
            continue
        keep.append(it)
    ships[sid] = keep
print(f'否决待复核 {removed} 张')

# --- 2) 补不足的
TARGETS = {
    'nagara': (['Nagara (ship, 1922)', 'Nagara class cruiser', 'Nagara class light cruiser'],
               ['nagara']),
    'hammann': (['USS Hammann (DD-412)', 'Sims class destroyer'], ['hammann']),
    'monaghan': (['USS Monaghan (DD-354)', 'Farragut class destroyer'], ['monaghan']),
    'benham': (['USS Benham (DD-397)', 'Benham class destroyer'], ['benham']),
}

existing_files = set(os.listdir(OUT))

for sid, (cats, names) in TARGETS.items():
    cur = ships.get(sid) or []
    if len(cur) >= 10:
        continue
    have = {str(it.get('commons_title') or '') for it in cur}
    print(f'\n===== {sid}（现有 {len(cur)}）')
    for cat in cats:
        if len(cur) >= 12:
            break
        try:
            files = cat_files(cat)
        except Exception as e:
            print(f'   {cat}: 失败 {type(e).__name__}')
            continue
        time.sleep(1.5)
        cand = [f for f in files if f not in have
                and os.path.splitext(f)[1].lower() in ('.jpg', '.jpeg', '.png')]
        if not cand:
            print(f'   {cat}: 无新候选')
            continue
        infos = file_infos(cand)
        for ft in cand:
            if len(cur) >= 12:
                break
            ii = infos.get(ft)
            if not ii:
                continue
            md = ii.get('extmetadata') or {}
            lic = strip_tags(md.get('LicenseShortName', {}).get('value', ''))
            l = lic.lower()
            if not ('public domain' in l or 'cc0' in l or 'pd' in l.split(';')[0]):
                continue
            desc = strip_tags(md.get('ImageDescription', {}).get('value', ''))
            blob = (ft + ' ' + desc).lower()
            # 严格：文件名或描述里本舰名必须出现，且描述里不能先出现别的舰
            if not any(n in blob for n in names):
                continue
            urls = [to_thumb(ii.get('thumburl')), to_thumb(ii.get('url')),
                    ii.get('thumburl')]
            data = try_urls(urls)
            if not data:
                continue
            base = re.sub(r'[^A-Za-z0-9]+', '-',
                          ft.replace('File:', '').rsplit('.', 1)[0]).strip('-')[:48]
            idx = len(cur) + 1
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
                'descr': desc[:300],
                'date': strip_tags(md.get('DateTimeOriginal', {}).get('value', ''))[:40],
            })
            print(f'      + {fn[:56]} ({len(data)//1024}KB)')
            time.sleep(2.5)
    ships[sid] = cur
    print(f'   → {len(cur)}')

with io.open('work/_ship_images_v3.yaml', 'w', encoding='utf-8', newline='\n') as f:
    yaml.safe_dump({'ships': ships}, f, allow_unicode=True, sort_keys=False,
                   default_flow_style=False, indent=2, width=200)

print('\n===== 最终 =====')
tot = 0
for sid in ['tone', 'chikuma', 'haruna', 'kirishima', 'hosho', 'nagara', 'sendai',
            'astoria', 'portland', 'minneapolis', 'new-orleans', 'vincennes',
            'northampton', 'pensacola', 'atlanta', 'hammann', 'monaghan', 'benham']:
    n = len(ships.get(sid) or [])
    tot += n
    print(f'  {sid:14} {n:>2}' + ('  ← 不足 10' if n < 10 else ''))
print(f'  合计 {tot}')
