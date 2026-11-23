# 重试失败的那批：upload.wikimedia.org 持续 429 → 改 thumb.wikimedia.org
# 交接报告 §7.2 第 3 条：
#   upload.wikimedia.org 对本站持续 429，凡是 upload 直链要改写成
#   thumb/.../thumb/1/10/NAME.jpg/960px-NAME.jpg（路径里必须保留 /thumb/）
import html
import io
import json
import os
import re
import ssl
import time
import urllib.parse
import urllib.request

import yaml

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
HDR = {'User-Agent': 'DockyardArchive/1.0 (research; low-rate)'}
API = 'https://commons.wikimedia.org/w/api.php'
OUTDIR = 'public/img/weapons'

PLAN = {
    '14cm-50-3ns': 'Category:14 cm/50 3rd Year Type naval gun',
    '36cm-45-t41': 'Category:41 cm/45 3rd Year Type naval gun',
    '8cm-40-3ns': 'Category:Type 3 8cm AA Gun',
    '15cm-50-t41': 'Category:15.5 cm/60 3rd Year Type',
    '8in-55-mk9': 'Category:8"/55 caliber gun',
    '21in-mk15': 'Category:Mark 15 torpedo',
}


def api(params, tries=5):
    url = API + '?' + urllib.parse.urlencode(params)
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=HDR)
            with urllib.request.urlopen(req, timeout=45, context=ctx) as f:
                return json.load(f)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(5 * (i + 1))
                continue
            raise
    return {}


def strip_tags(s):
    if not s:
        return ''
    return html.unescape(re.sub(r'<[^>]+>', '', str(s))).strip()


def rewrite_to_thumb(url):
    """upload.wikimedia.org/.../d/df/NAME.jpg
       → thumb.wikimedia.org/.../thumb/d/df/NAME.jpg/960px-NAME.jpg"""
    if '/thumb/' in url:
        return url
    m = re.match(r'https?://upload\.wikimedia\.org(/wikipedia/commons)/(.)/(..)/([^/]+)$', url)
    if not m:
        return url
    base, h1, h2, fname = m.groups()
    name_no_ext = fname.rsplit('.', 1)[0]
    return (f'https://thumb.wikimedia.org{base}/thumb/{h1}/{h2}/{fname}/'
            f'960px-{name_no_ext}.jpg')


def cat_files(cat, limit=12):
    j = api({'action': 'query', 'list': 'categorymembers', 'cmtitle': cat,
             'cmtype': 'file', 'cmlimit': str(limit), 'format': 'json'})
    return [m['title'] for m in (j.get('query', {}).get('categorymembers') or [])]


def file_info(title):
    j = api({'action': 'query', 'titles': title, 'prop': 'imageinfo',
             'iiprop': 'url|size|extmetadata', 'format': 'json'})
    pages = j.get('query', {}).get('pages') or {}
    for _, p in pages.items():
        ii = (p.get('imageinfo') or [None])[0]
        if ii:
            return ii
    return None


def is_free(ii):
    md = ii.get('extmetadata') or {}
    lic = strip_tags(md.get('LicenseShortName', {}).get('value', '')).lower()
    return any(k in lic for k in ('public domain', 'pd', 'cc0'))


os.makedirs(OUTDIR, exist_ok=True)
entries = []

for wid, cat in PLAN.items():
    print(f'\n--- {wid}')
    try:
        files = cat_files(cat)
    except Exception as e:
        print(f'    分类失败 {type(e).__name__}')
        continue
    time.sleep(2)

    for ft in files:
        if ft.lower().endswith(('.ogv', '.webm', '.ogg')):
            continue
        ext = os.path.splitext(ft)[1].lower()
        if ext not in ('.jpg', '.jpeg', '.png'):
            continue
        try:
            ii = file_info(ft)
        except Exception:
            continue
        time.sleep(1.5)
        if not ii or not is_free(ii):
            continue

        orig = ii.get('url') or ''
        cands = []
        if ii.get('thumburl'):
            cands.append(ii['thumburl'])
        if orig:
            cands.append(rewrite_to_thumb(orig))
            cands.append(orig)

        got = None
        for u in cands:
            try:
                req = urllib.request.Request(u, headers=HDR)
                with urllib.request.urlopen(req, timeout=60, context=ctx) as f:
                    data = f.read()
                if data[:2] == b'\xff\xd8' or data[:4] == b'\x89PNG':
                    got = (u, data)
                    break
            except Exception:
                time.sleep(2)
                continue

        if not got:
            print(f'    {ft[:50]} 所有 URL 都拿不到')
            continue

        fn = f'{wid}{ext}'
        with open(os.path.join(OUTDIR, fn), 'wb') as f:
            f.write(got[1])

        md = ii.get('extmetadata') or {}
        entries.append({
            'id': f'weapon-{wid}-main',
            'file': f'/img/weapons/{fn}',
            'subject': f'weapon:{wid}',
            'title': {'zh': f'{wid} 实物照',
                      'en': strip_tags(md.get('ObjectName', {}).get('value', '')) or ft},
            'license': 'pd',
            'license_tier': 'A',
            'license_raw': strip_tags(md.get('LicenseShortName', {}).get('value', '')),
            'author': strip_tags(md.get('Artist', {}).get('value', ''))[:120],
            'credit': strip_tags(md.get('Credit', {}).get('value', ''))[:120],
            'source_url': 'https://commons.wikimedia.org/wiki/' + urllib.parse.quote(ft.replace(' ', '_')),
            'width': ii.get('width'),
            'height': ii.get('height'),
            'primary': True,
        })
        print(f'    ✓ {fn} ({len(got[1])} bytes) {ft}')
        time.sleep(2)
        break

print(f'\n补到 {len(entries)} 张')
if entries:
    with io.open('work/_weapon_images_fragment2.yaml', 'w', encoding='utf-8', newline='\n') as f:
        yaml.safe_dump({'images': entries}, f, allow_unicode=True,
                       sort_keys=False, default_flow_style=False, indent=2, width=200)
    print('分片: work/_weapon_images_fragment2.yaml')
