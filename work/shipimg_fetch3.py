# 增量抓三艘舰的候选，合并进已有 candidates.json。
import io
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / 'work' / 'shipimg'
UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'
API = 'https://commons.wikimedia.org/w/api.php'

CATS = {
    'hood': 'HMS Hood (ship, 1920)',
    'prince-of-wales': 'HMS Prince of Wales (ship, 1941)',
    'rodney': 'HMS Rodney (ship, 1925)',
}


def api(params, retries=6):
    params = dict(params)
    params['format'] = 'json'
    url = API + '?' + urllib.parse.urlencode(params)
    for a in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.loads(r.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                w = 20 + a * 15
                print(f'    429 wait {w}s')
                time.sleep(w)
                continue
            raise
        except Exception:
            if a == retries - 1:
                return {}
            time.sleep(8)
    return {}


def clean(s):
    import re
    return ' '.join(re.sub(r'<[^>]+>', '', str(s or '')).split())


def cat_files(cat, limit=100):
    out = []
    cont = {}
    while len(out) < limit:
        p = {'action': 'query', 'list': 'categorymembers', 'cmtitle': 'Category:' + cat,
             'cmtype': 'file', 'cmlimit': '50'}
        p.update(cont)
        d = api(p)
        out += [m['title'] for m in d.get('query', {}).get('categorymembers', [])]
        if 'continue' in d:
            cont = d['continue']
            time.sleep(3)
        else:
            break
    return out[:limit]


def imageinfo(titles):
    res = {}
    for i in range(0, len(titles), 20):
        d = api({'action': 'query', 'titles': '|'.join(titles[i:i + 20]),
                 'prop': 'imageinfo',
                 'iiprop': 'url|size|extmetadata|mime', 'iiurlwidth': '1280'})
        res.update(d.get('query', {}).get('pages', {}))
        time.sleep(3)
    return res


existing = json.load(io.open(WORK / 'candidates.json', encoding='utf-8'))
print(f'已有 {sum(len(v) for v in existing.values())} 条')

for sid, cat in CATS.items():
    print(f'\n=== {sid} ({cat}) ===')
    if existing.get(sid):
        print('  已有，跳过')
        continue
    files = cat_files(cat)
    print(f'  {len(files)} 个文件')
    if not files:
        existing[sid] = []
        continue
    meta = imageinfo(files)
    entries = []
    for pid, page in meta.items():
        ii = (page.get('imageinfo') or [{}])[0]
        if not ii.get('url'):
            continue
        em = ii.get('extmetadata') or {}
        entries.append({
            'title': clean(page.get('title')).replace('File:', ''),
            'thumb': ii.get('thumburl'),
            'w': ii.get('width'), 'h': ii.get('height'),
            'mime': ii.get('mime'),
            'license': clean((em.get('LicenseShortName') or {}).get('value')),
            'artist': clean((em.get('Artist') or {}).get('value'))[:180],
            'desc': clean((em.get('ImageDescription') or {}).get('value'))[:250],
            'date': clean((em.get('DateTimeOriginal') or {}).get('value'))[:40],
            'page': ii.get('descriptionurl'),
        })
    entries.sort(key=lambda e: -(e.get('w') or 0))
    existing[sid] = entries
    pd = sum(1 for e in entries if 'Public domain' in e['license'] or 'CC0' in e['license'])
    print(f'  取到 {len(entries)} 条，PD/CC0 {pd}')
    time.sleep(4)

io.open(WORK / 'candidates.json', 'w', encoding='utf-8').write(
    json.dumps(existing, ensure_ascii=False, indent=2))
print(f'\n合并后总计 {sum(len(v) for v in existing.values())} 条')
