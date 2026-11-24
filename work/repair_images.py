# 修复事故：new-orleans 的图被全删，重新下载
#
# 事故原因（2026-11-25 凌晨）：
#   verify_images.py 用全局共享的 seen 哈希去重。
#   new-orleans 与其他舰（atlanta/portland/pensacola）共用若干「合影」图，
#   哈希相同时先处理者通过、后者判重复删除。
#   而 new-orleans 的文件名正则 `^([a-z\-]+?)-(\d+)-` 非贪婪，
#   把它误归到 'new' 组，又通过 startswith 补进 'new-orleans'，
#   最终整组被判重复 → 15 张全删。
#
# 教训：去重必须是「同一舰内部去重」，不能跨舰共享哈希就删 ——
# 因为一张合影确实同时属于多艘舰，删掉会让另一艘没图。
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


def to_thumb(u, width=WIDTH):
    u = (u or '').split('?')[0]
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


# 本次修复的目标：new-orleans（0 张）、nagara（6）、monaghan（5）
TARGETS = {
    'new-orleans': (['USS New Orleans (CA-32)'],
                    ['new orleans', 'new-orleans', 'neworleans']),
    'nagara': (['Nagara (ship, 1922)', 'Nagara class cruiser'], ['nagara']),
    'monaghan': (['USS Monaghan (DD-354)', 'Farragut class destroyer'], ['monaghan']),
}

ALL_NAMES = {
    'tone': ['tone'], 'chikuma': ['chikuma'], 'haruna': ['haruna'],
    'kirishima': ['kirishima'], 'hosho': ['hosho', 'hōshō', 'hosyo'],
    'nagara': ['nagara'], 'sendai': ['sendai'], 'astoria': ['astoria'],
    'portland': ['portland'], 'minneapolis': ['minneapolis'],
    'new-orleans': ['new orleans', 'new-orleans', 'neworleans'],
    'vincennes': ['vincennes'], 'northampton': ['northampton'],
    'pensacola': ['pensacola'], 'atlanta': ['atlanta'], 'hammann': ['hammann'],
    'monaghan': ['monaghan'], 'benham': ['benham'],
}

result = {}
for sid, (cats, names) in TARGETS.items():
    # 现有磁盘文件
    existing = sorted(f for f in os.listdir(OUT) if re.match(rf'^{re.escape(sid)}-\d+-', f))
    print(f'\n===== {sid}（现有 {len(existing)}）')
    items = []
    have_titles = set()
    for fn in existing:
        idx = int(re.match(rf'^{re.escape(sid)}-(\d+)-', fn).group(1))
        items.append({'fn': fn, 'idx': idx})
    next_idx = max([it['idx'] for it in items], default=0) + 1

    for cat in cats:
        if len(items) >= 12:
            break
        try:
            files = cat_files(cat)
        except Exception as e:
            print(f'   {cat}: 失败 {type(e).__name__}')
            continue
        time.sleep(1.5)
        cand = [f for f in files if f not in have_titles
                and os.path.splitext(f)[1].lower() in ('.jpg', '.jpeg', '.png')]
        if not cand:
            continue
        infos = file_infos(cand)
        for ft in cand:
            if len(items) >= 12:
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
            ctitle = ft.lower().replace('file:', '')
            blob = desc[:400].lower()

            # 主体判定：文件名命中本舰，或描述里本舰名最先出现
            ok = any(n in ctitle for n in names)
            if not ok:
                hits = []
                for osid, onames in ALL_NAMES.items():
                    for n in onames:
                        k = blob.find(n)
                        if k >= 0:
                            hits.append((k, osid))
                            break
                hits.sort()
                ok = bool(hits) and hits[0][1] == sid
            if not ok:
                continue

            urls = [to_thumb(ii.get('thumburl')), to_thumb(ii.get('url')),
                    ii.get('thumburl')]
            data = try_urls(urls)
            if not data:
                continue
            base = re.sub(r'[^A-Za-z0-9]+', '-',
                          ft.replace('File:', '').rsplit('.', 1)[0]).strip('-')[:44]
            fn = f'{sid}-{next_idx:02d}-{base}.jpg'
            with open(os.path.join(OUT, fn), 'wb') as f:
                f.write(data)
            items.append({'fn': fn, 'idx': next_idx,
                          'commons_title': ft, 'license_raw': lic, 'descr': desc,
                          'author': strip_tags(md.get('Artist', {}).get('value', ''))[:120],
                          'source_url': 'https://commons.wikimedia.org/wiki/' + ft.replace(' ', '_'),
                          'width': ii.get('width'), 'height': ii.get('height')})
            next_idx += 1
            print(f'   + {fn[:56]} ({len(data)//1024}KB)')
            time.sleep(2)
    result[sid] = items
    print(f'   → {len(items)} 张')

with io.open('work/_ship_images_repaired.yaml', 'w', encoding='utf-8', newline='\n') as f:
    yaml.safe_dump({'ships': result}, f, allow_unicode=True, sort_keys=False,
                   default_flow_style=False, indent=2, width=200)
print('\n写出 work/_ship_images_repaired.yaml')
