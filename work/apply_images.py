# 应用判定结果：重新下载被判「留」的文件，写入正确编号
#
# 为什么重新下载：前面几版误删了不少合规文件（80-G-* 编号照、
# new-orleans 整组）。原始抓取表里保留了每张图的 Commons 原名，重下即可复原，
# 不必再从分类里重挑。
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


def try_urls(urls, tries=4):
    for a in range(tries):
        for u in urls:
            if not u:
                continue
            try:
                req = urllib.request.Request(u, headers={
                    'User-Agent': 'DockyardArchive/1.0 (research)',
                    'Referer': 'https://commons.wikimedia.org/'})
                with opener.open(req, timeout=180) as f:
                    data = f.read()
                if data[:2] == b'\xff\xd8' or data[:4] == b'\x89PNG':
                    return data
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    time.sleep(10 * (a + 1))
                else:
                    time.sleep(3)
            except Exception:
                time.sleep(4)
    return None


def file_infos(titles, batch=5):
    out = {}
    for i in range(0, len(titles), batch):
        j = api({'action': 'query', 'titles': '|'.join(titles[i:i + batch]),
                 'prop': 'imageinfo', 'iiprop': 'url|size|extmetadata',
                 'iiurlwidth': str(WIDTH), 'format': 'json'})
        for _, p in (j.get('query', {}).get('pages') or {}).items():
            ii = (p.get('imageinfo') or [None])[0]
            if ii:
                out[p.get('title')] = ii
        time.sleep(2)
    return out


dec = yaml.safe_load(io.open('work/_ship_images_decision.yaml', encoding='utf-8'))['ships']

# 先清空这 18 舰的现存文件（重新编号，保证干净）
SHIPS = list(dec.keys())
for sid in SHIPS:
    for fn in os.listdir(OUT):
        if re.match(rf'^{re.escape(sid)}-\d+-', fn):
            os.remove(os.path.join(OUT, fn))
print('已清空 18 舰的旧文件，开始重下')

result = {}
for sid in SHIPS:
    items = dec.get(sid) or []
    titles = [str(it['commons_title']) for it in items if it.get('commons_title')]
    print(f'\n===== {sid}（{len(titles)} 张）')
    infos = file_infos(titles) if titles else {}
    got = []
    for n, it in enumerate(items, 1):
        ct = str(it.get('commons_title') or '')
        if not ct:
            continue
        ii = infos.get(ct)
        if not ii:
            print(f'    {n:>2} 无 imageinfo: {ct[:50]}')
            continue
        md = ii.get('extmetadata') or {}
        lic = strip_tags(md.get('LicenseShortName', {}).get('value', ''))
        urls = [to_thumb(ii.get('thumburl')), to_thumb(ii.get('url')), ii.get('thumburl')]
        data = try_urls(urls)
        if not data:
            print(f'    {n:>2} 下载失败: {ct[:50]}')
            continue
        base = re.sub(r'[^A-Za-z0-9]+', '-',
                      ct.replace('File:', '').rsplit('.', 1)[0]).strip('-')[:44]
        fn = f'{sid}-{len(got) + 1:02d}-{base}.jpg'
        with open(os.path.join(OUT, fn), 'wb') as f:
            f.write(data)
        got.append({
            'file': f'/img/ships/{fn}',
            'subject': f'ship:{sid}',
            'commons_title': ct,
            'license': 'pd' if ('public domain' in lic.lower() or 'cc0' in lic.lower()) else 'cc',
            'license_tier': 'A',
            'license_raw': lic,
            'author': strip_tags(md.get('Artist', {}).get('value', ''))[:120],
            'credit': strip_tags(md.get('Credit', {}).get('value', ''))[:120],
            'source_url': 'https://commons.wikimedia.org/wiki/' + ct.replace(' ', '_'),
            'width': ii.get('width'),
            'height': ii.get('height'),
            'descr': strip_tags(md.get('ImageDescription', {}).get('value', ''))[:400],
            'date': strip_tags(md.get('DateTimeOriginal', {}).get('value', ''))[:40],
        })
        print(f'    [{len(got):>2}] {fn[:56]} ({len(data)//1024}KB)')
        time.sleep(2)
    result[sid] = got
    print(f'   → {len(got)} 张')

with io.open('work/_ship_images_apply.yaml', 'w', encoding='utf-8', newline='\n') as f:
    yaml.safe_dump({'ships': result}, f, allow_unicode=True, sort_keys=False,
                   default_flow_style=False, indent=2, width=200)

print('\n===== 最终 =====')
tot = 0
for sid in SHIPS:
    n = len(result[sid])
    tot += n
    print(f'  {sid:14} {n:>2}' + ('  ← 素材上限' if n < 10 else ''))
print(f'  合计 {tot}')
