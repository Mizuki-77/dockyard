# 六张肖像统一重抓为**原图**（不取 720px 缩略图）。
#
# 上一版尺寸问题：cropped 图的 thumburl 是按「原图宽度」算的，
# 原图本身就小（michael-denny 那张原图 221px），所以缩略图更小。
# 人物页上要当主视觉，太小会糊。
#
# 策略：先要 original，超过 1600px 宽的再降采样到 1200 并转灰度 JPEG，
# 避免把 4000px 的档案照直接塞进仓库。
from pathlib import Path

import io
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'public' / 'img' / 'commanders'
OUT.mkdir(parents=True, exist_ok=True)
UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'
COMMONS = 'https://commons.wikimedia.org/w/api.php'

EXACT = {
    'philip-vian': 'File:Philip Vian.jpg',
    'ernst-lindemann':
        'File:Bundesarchiv Bild 101II-MN-1361-21A, Schlachtschiff Bismarck, '
        'Kapitän Ernst Lindemann.jpg',
    'arthur-power': 'File:Sir Arthur John Power, March 1945.jpg',
    'arthur-power-crop': 'File:Sir Arthur John Power, March 1945 (cropped).jpg',
    'eugeniusz-plawski': 'File:Eugeniusz Pławski.jpg',
    'louis-hamilton': 'File:Louis Keppel Hamilton.jpg',
    'michael-denny':
        'File:Admiral Sir John Tovey and Members of His Staff. 4 February 1943, '
        'on Board Home Fleet Flagship HMS King George V. A14846.jpg',
}

# 若确切标题取不到，用搜索兜底
FALLBACK_Q = {
    'philip-vian': 'Philip Vian admiral portrait',
    'eugeniusz-plawski': 'Eugeniusz Pławski',
    'louis-hamilton': 'Louis Keppel Hamilton admiral',
    'arthur-power': 'Arthur John Power admiral 1945',
}


def api(params, retries=6):
    params = dict(params)
    params['format'] = 'json'
    url = COMMONS + '?' + urllib.parse.urlencode(params)
    for a in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=50) as r:
                return json.loads(r.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(20 + a * 15)
                continue
            return {}
        except Exception:
            if a == retries - 1:
                return {}
            time.sleep(8)
    return {}


def fetch(url, retries=6):
    for a in range(retries):
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': UA,
                'Referer': 'https://commons.wikimedia.org/',
            })
            with urllib.request.urlopen(req, timeout=180) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(25 + a * 20)
                continue
            if a == retries - 1:
                return None
            time.sleep(12)
        except Exception:
            if a == retries - 1:
                return None
            time.sleep(12)
    return None


def info_of(title):
    d = api({'action': 'query', 'titles': title, 'prop': 'imageinfo',
             'iiprop': 'url|size|extmetadata'})
    pages = d.get('query', {}).get('pages', {})
    for k, pg in pages.items():
        if k == '-1':
            continue
        ii = (pg.get('imageinfo') or [{}])[0]
        if ii.get('url'):
            return ii, pg.get('title')
    return None, None


def clean(s):
    return ' '.join(re.sub(r'<[^>]+>', '', str(s or '')).split())


def save_normalized(raw_bytes, dest_stem):
    """原图可能过大/是 PNG，统一转成不超过 1200px 宽的灰度 JPEG。"""
    tmp = io.BytesIO(raw_bytes)
    im = Image.open(tmp)
    im = im.convert('L') if im.mode in ('1', 'L', 'P', 'RGBA') else im.convert('RGB')
    w, h = im.size
    if max(w, h) > 1200:
        scale = 1200 / max(w, h)
        im = im.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
    out = OUT / f'{dest_stem}.jpg'
    im.save(out, 'JPEG', quality=88, optimize=True)
    return out, im.size


report = json.load(io.open(ROOT / 'work' / 'cmdr_portraits.json', encoding='utf-8'))

for pid, title in EXACT.items():
    if pid.endswith('-crop'):
        continue
    print(f'=== {pid} ===')
    ii, got = info_of(title)
    if not ii and pid in FALLBACK_Q:
        d = api({'action': 'query', 'list': 'search',
                 'srsearch': f'filetype:bitmap {FALLBACK_Q[pid]}',
                 'srnamespace': '6', 'srlimit': '5'})
        for h in d.get('query', {}).get('search', []):
            t = h['title']
            if 'cropped' in t:
                continue
            ii2, got2 = info_of(t)
            if ii2:
                ii, got = ii2, got2
                print(f'   兜底命中: {t[:70]}')
                break
    if not ii:
        print('   取不到')
        continue

    url = (ii.get('url') or '').split('?')[0]
    blob = fetch(url)
    if not blob:
        print('   下载失败')
        continue
    try:
        out, size = save_normalized(blob, pid)
    except Exception as e:
        print(f'   转码失败 {e}')
        continue

    em = ii.get('extmetadata') or {}
    report[pid] = {
        'file': f'/img/commanders/{pid}.jpg',
        'bytes': out.stat().st_size,
        'license': clean((em.get('LicenseShortName') or {}).get('value')),
        'artist': clean((em.get('Artist') or {}).get('value'))[:200],
        'source_url': ii.get('descriptionurl'),
        'title': got,
        'width': size[0],
        'height': size[1],
        'orig': f'{ii.get("width")}x{ii.get("height")}',
    }
    print(f'   OK {out.stat().st_size//1024}KB  {size[0]}x{size[1]}  (原 {ii.get("width")}x{ii.get("height")})')
    time.sleep(3)

io.open(ROOT / 'work' / 'cmdr_portraits.json', 'w', encoding='utf-8').write(
    json.dumps(report, ensure_ascii=False, indent=2))

print()
print('=== 最终 ===')
for k in sorted(report):
    v = report[k]
    print(f'  {k:<22} {v.get("width")}x{v.get("height")}  {v.get("license","")[:22]}')
