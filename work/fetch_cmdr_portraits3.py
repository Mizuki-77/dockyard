# 补抓剩下 3 张肖像。每个都有具体失败原因，逐个处理。
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
            with urllib.request.urlopen(req, timeout=150) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            print(f'    HTTP {e.code}')
            if e.code == 429:
                time.sleep(20 + a * 20)
                continue
            if a == retries - 1:
                return None
            time.sleep(10)
        except Exception as e:
            print(f'    ERR {type(e).__name__}')
            if a == retries - 1:
                return None
            time.sleep(10)
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


# 三个人各自的正确文件名。Lindemann 那张是德国联邦档案馆的，
# 文件名里有逗号和空格，且被 pageimages 截断过 —— 直接写全名。
TARGETS = {
    'ernst-lindemann': 'Bundesarchiv Bild 101II-MN-1361-21A, Schlachtschiff Bismarck.jpg',
    'arthur-power': 'Admiral Sir Arthur Power.jpg',
    'michael-denny': 'Admiral Sir Michael Denny.jpg',
}

report = {}
for pid, fname in TARGETS.items():
    print(f'=== {pid} ===')
    title = 'File:' + fname
    d = api({'action': 'query', 'titles': title, 'prop': 'imageinfo',
             'iiprop': 'url|size|extmetadata', 'iiurlwidth': '720'})
    pages = d.get('query', {}).get('pages', {})
    ii = None
    got_title = None
    for k, pg in pages.items():
        if k != '-1':
            ii = (pg.get('imageinfo') or [{}])[0]
            got_title = pg.get('title')
    if not ii or not ii.get('url'):
        print(f'   找不到 {fname}')
        # 退一步：搜文件名关键词
        key = fname.split(',')[0].split('(')[0].strip()[:40]
        d2 = api({'action': 'query', 'list': 'search',
                  'srsearch': f'filetype:bitmap {key}', 'srnamespace': '6',
                  'srlimit': '5'})
        for h in d2.get('query', {}).get('search', []):
            print(f'      候选: {h["title"]}')
        continue

    url = (ii.get('thumburl') or ii.get('url') or '').split('?')[0]
    print(f'   url: {url[:90]}')
    blob = fetch(url)
    if not blob:
        print('   下载失败')
        continue
    ext = ext_of(blob)
    if not ext:
        print(f'   非图片 {len(blob)}B')
        continue
    fn = f'{pid}.{ext}'
    (OUT / fn).write_bytes(blob)
    em = ii.get('extmetadata') or {}
    report[pid] = {
        'file': f'/img/commanders/{fn}',
        'bytes': len(blob),
        'license': clean((em.get('LicenseShortName') or {}).get('value')),
        'artist': clean((em.get('Artist') or {}).get('value'))[:160],
        'source_url': ii.get('descriptionurl'),
        'title': got_title,
        'width': ii.get('width'),
        'height': ii.get('height'),
    }
    print(f'   OK {len(blob)//1024}KB -> {fn}')
    time.sleep(3)

# 合并进已有的 portraits 文件
p = ROOT / 'work' / 'cmdr_portraits.json'
old = json.load(io.open(p, encoding='utf-8')) if p.exists() else {}
old.update(report)
io.open(p, 'w', encoding='utf-8').write(json.dumps(old, ensure_ascii=False, indent=2))

print()
print(f'本轮补到 {len(report)} 张，累计 {len(old)} 张')
for k in sorted(old):
    print(f'  {k}')
