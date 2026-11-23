# 用搜到的**确切完整文件名**重抓。上一版失败是因为我把文件名猜短了。
import io
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'public' / 'img' / 'commanders'
OUT.mkdir(parents=True, exist_ok=True)
UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'
COMMONS = 'https://commons.wikimedia.org/w/api.php'

# 确切标题（从上一版的搜索结果里抄的，一字不改）
EXACT = {
    'ernst-lindemann':
        'File:Bundesarchiv Bild 101II-MN-1361-21A, Schlachtschiff Bismarck, '
        'Kapitän Ernst Lindemann.jpg',
    'arthur-power':
        'File:Sir Arthur John Power, March 1945 (cropped).jpg',
    'michael-denny':
        'File:Admiral Sir John Tovey and Members of His Staff. 4 February 1943, '
        'on Board Home Fleet Flagship HMS King George V. A14846 (cropped).jpg',
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
            print(f'    api HTTP {e.code}')
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
            print(f'    HTTP {e.code}')
            if e.code == 429:
                time.sleep(25 + a * 20)
                continue
            if a == retries - 1:
                return None
            time.sleep(12)
        except Exception as e:
            print(f'    ERR {type(e).__name__}')
            if a == retries - 1:
                return None
            time.sleep(12)
    return None


def ext_of(d):
    if d.startswith(b'\xff\xd8'):
        return 'jpg'
    if d.startswith(b'\x89PNG'):
        return 'png'
    if d[:4] == b'RIFF' and d[8:12] == b'WEBP':
        return 'webp'
    return None


def clean(s):
    return ' '.join(re.sub(r'<[^>]+>', '', str(s or '')).split())


report = {}
for pid, title in EXACT.items():
    print(f'=== {pid} ===')
    d = api({'action': 'query', 'titles': title, 'prop': 'imageinfo',
             'iiprop': 'url|size|extmetadata', 'iiurlwidth': '720'})
    pages = d.get('query', {}).get('pages', {})
    ii, got = None, None
    for k, pg in pages.items():
        if k != '-1':
            ii = (pg.get('imageinfo') or [{}])[0]
            got = pg.get('title')
    if not ii or not ii.get('url'):
        print('   仍然找不到，检查标题')
        continue

    # 这是 cropped 图，尺寸可能已经不大；先试 thumb，失败再试原图
    cands = []
    if ii.get('thumburl'):
        cands.append(('thumb', ii['thumburl'].split('?')[0]))
    if ii.get('url'):
        cands.append(('orig', ii['url'].split('?')[0]))

    blob = None
    used = None
    for kind, u in cands:
        print(f'   试 {kind}: {u[:80]}')
        blob = fetch(u)
        if blob and ext_of(blob):
            used = kind
            break
        blob = None
        time.sleep(3)

    if not blob:
        print('   两种都失败')
        continue

    ext = ext_of(blob)
    fn = f'{pid}.{ext}'
    (OUT / fn).write_bytes(blob)
    em = ii.get('extmetadata') or {}
    report[pid] = {
        'file': f'/img/commanders/{fn}',
        'bytes': len(blob),
        'license': clean((em.get('LicenseShortName') or {}).get('value')),
        'artist': clean((em.get('Artist') or {}).get('value'))[:160],
        'source_url': ii.get('descriptionurl'),
        'title': got,
        'width': ii.get('width'),
        'height': ii.get('height'),
        'via': used,
    }
    print(f'   OK {len(blob)//1024}KB [{used}] -> {fn}')
    time.sleep(4)

p = ROOT / 'work' / 'cmdr_portraits.json'
old = json.load(io.open(p, encoding='utf-8')) if p.exists() else {}
old.update(report)
io.open(p, 'w', encoding='utf-8').write(json.dumps(old, ensure_ascii=False, indent=2))

print()
print(f'本轮补到 {len(report)} 张，累计 {len(old)} 张')
for k in sorted(old):
    print(f'  {k:<24} {old[k].get("license","?")[:20]}')
