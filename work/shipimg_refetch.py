# 重新下载：从候选池直接挑，带文件头校验，失败就换下一个。
# 上一轮的教训：下载后必须校验 b'\xff\xd8'，否则会把 HTML 错误页当图片存下来。
import io
import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / 'work' / 'shipimg'
OUT = ROOT / 'public' / 'img' / 'ships'
UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'

TARGET = 12  # 每舰目标张数

cand = json.load(io.open(WORK / 'candidates.json', encoding='utf-8'))

# 已有的（之前下好的、校验过的）保留，从候选里跳过
existing_files = set(f for f in __import__('os').listdir(OUT) if '-extra-' in f)

BAD = [
    'badge', 'crest', 'coat of arms', 'emblem',
    'map', 'chart', 'diagram', 'drawing', 'plan',
    'stamp', 'postal', 'coin', 'medal', 'banknote',
    'model', 'kit', 'diorama', 'painting', 'artwork', 'illustration',
    'poster', 'propaganda', 'cartoon', 'comic',
    'wreck', 'wreckage', 'debris', 'salvage', 'underwater',
    'grave', 'memorial', 'plaque', 'monument', 'museum ship',
    'crew', 'sailor', 'seaman', 'payday', 'scrubbing', 'washing',
    'sleeping', 'cooking', 'galley', 'mess', 'church service',
    'interview', 'portrait', 'group photo', 'posing',
    'logo', 'flag', 'ensign',
    'space shuttle', 'starship', 'fictional',
    'churchill', 'hitler', 'lexington', 'texas', 'jacob', 'piorun',
    'restoration', 'original scan', 'partial', 'bayonne', 'reserve ships',
    'signal flying', 'survivors', 'explosion', 'sinking', 'cemetery',
    'ceremony', 'launching', 'christening',
]

EXCLUDE = {
    'hood': ['1891', '1893'],
    'prince-of-wales': ['R09', '1902', '1765', '1794', '1904'],
    'rodney': ['1833', '1888', '1901'],
    'illustrious': ['R06', '1896', '1803', '1789'],
    'king-george-v': ['1911'],
    'tirpitz': ['1921'],
    'enterprise': ['CVN-65', 'shuttle', 'Slagharen'],
    'hornet': ['CV-12', 'CVS-12', 'museum'],
    'yorktown': ['CV-10', 'CVS-10', 'PG-1'],
}

GOOD = ['broadside', 'underway', 'at sea', 'steaming', 'aerial', 'overhead',
        'starboard', 'port side', 'full view', 'at anchor']


def blob_of(e):
    return (e['title'] + ' ' + (e.get('desc') or '')).lower()


def ok_entry(sid, e):
    b = blob_of(e)
    for w in BAD:
        if w in b:
            return False
    for w in EXCLUDE.get(sid, []):
        if w.lower() in b:
            return False
    if (e.get('w') or 0) < 800:
        return False
    t = e['title'].lower()
    if any(x in t for x in ['.ogv', '.webm', '.ogg', '.pdf', '.tif', '.tiff']):
        return False
    return True


def score(e):
    b = blob_of(e)
    lic = e.get('license', '')
    s = 0
    if 'Public domain' in lic:
        s += 100
    elif 'CC0' in lic:
        s += 95
    elif lic.startswith('CC'):
        s += 45
    else:
        s += 5
    for v in GOOD:
        if v in b:
            s += 25
            break
    w = e.get('w') or 0
    s += 30 if w >= 3000 else 25 if w >= 2000 else 18 if w >= 1200 else 10
    return s


def fetch(url, dest):
    """下载并严格校验是 JPEG。"""
    if not url:
        return False
    for a in range(6):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=90) as r:
                data = r.read()
            if len(data) < 5000:
                return False
            if data[:2] != b'\xff\xd8':
                return False
            io.open(dest, 'wb').write(data)
            return True
        except urllib.error.HTTPError as ex:
            if ex.code == 429:
                time.sleep(30 + a * 20)
                continue
            return False
        except Exception:
            time.sleep(8)
    return False


import re


def slug(s):
    return re.sub(r'[^a-zA-Z0-9]+', '-', s).strip('-').lower()[:44]


result = {}
total = 0
for sid, entries in cand.items():
    have = [f for f in existing_files if f.startswith(sid + '-extra-')]
    need = TARGET - len(have)
    print(f'\n=== {sid}  已有 {len(have)}，需补 {need} ===')
    if need <= 0:
        result[sid] = have
        continue

    pool = [e for e in entries if ok_entry(sid, e)]
    pool.sort(key=score, reverse=True)

    got = list(have)
    idx = 0
    for e in pool:
        if len(got) >= TARGET:
            break
        idx += 1
        name = f'{sid}-extra-r{idx}-{slug(e["title"])}.jpg'
        dest = OUT / name
        if dest.exists():
            got.append(name)
            continue
        if fetch(e.get('thumb'), dest):
            got.append(name)
            print(f'  OK {name[:58]}')
            time.sleep(3)
        else:
            print(f'  跳过 {e["title"][:50]}')

    result[sid] = got
    total += len(got)

io.open(WORK / 'final_imgs.json', 'w', encoding='utf-8').write(
    json.dumps(result, ensure_ascii=False, indent=2))
print(f'\n完成，共 {total} 张')
