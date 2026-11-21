# 慢速补图：每张间隔 6-8 秒，遇 429 长等。支持断点续跑。
# 目标：每舰补到 10 张（用户说「别太多」，10-12 张够用）。
import io
import json
import os
import re
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / 'work' / 'shipimg'
OUT = ROOT / 'public' / 'img' / 'ships'
UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'
TARGET = 10

cand = json.load(io.open(WORK / 'candidates.json', encoding='utf-8'))

BAD = [
    'badge', 'crest', 'coat of arms', 'emblem', 'map', 'chart', 'diagram',
    'drawing', 'stamp', 'postal', 'coin', 'medal', 'banknote', 'model',
    'kit', 'diorama', 'painting', 'artwork', 'illustration', 'poster',
    'propaganda', 'cartoon', 'comic', 'wreck', 'wreckage', 'debris',
    'salvage', 'underwater', 'grave', 'memorial', 'plaque', 'monument',
    'museum ship', 'crew', 'sailor', 'seaman', 'payday', 'scrubbing',
    'washing', 'sleeping', 'cooking', 'galley', 'mess', 'church service',
    'interview', 'portrait', 'group photo', 'posing', 'logo', 'flag',
    'ensign', 'space shuttle', 'starship', 'fictional', 'churchill',
    'hitler', 'lexington', 'texas', 'jacob', 'piorun', 'restoration',
    'original scan', 'partial', 'bayonne', 'reserve ships', 'signal flying',
    'survivors', 'explosion', 'sinking', 'cemetery', 'ceremony', 'launching',
    'christening', 'pearl harbor navy yard', 'aerial view of pearl harbor',
]
EXCLUDE = {
    'hood': ['1891', '1893'], 'prince-of-wales': ['R09', '1902', '1765', '1794', '1904'],
    'rodney': ['1833', '1888', '1901'], 'illustrious': ['R06', '1896', '1803', '1789'],
    'king-george-v': ['1911'], 'tirpitz': ['1921'],
    'enterprise': ['CVN-65', 'shuttle', 'Slagharen'],
    'hornet': ['CV-12', 'CVS-12', 'museum'], 'yorktown': ['CV-10', 'CVS-10', 'PG-1'],
}
GOOD = ['broadside', 'underway', 'at sea', 'steaming', 'aerial', 'overhead',
        'starboard', 'port side', 'full view', 'at anchor']


def blob(e):
    return (e['title'] + ' ' + (e.get('desc') or '')).lower()


def ok(sid, e):
    b = blob(e)
    if any(w in b for w in BAD):
        return False
    if any(w.lower() in b for w in EXCLUDE.get(sid, [])):
        return False
    if (e.get('w') or 0) < 800:
        return False
    t = e['title'].lower()
    if any(x in t for x in ['.ogv', '.webm', '.ogg', '.pdf', '.tif', '.tiff']):
        return False
    return True


def score(e):
    b = blob(e)
    lic = e.get('license', '')
    s = (100 if 'Public domain' in lic else 95 if 'CC0' in lic
         else 45 if lic.startswith('CC') else 5)
    if any(v in b for v in GOOD):
        s += 25
    w = e.get('w') or 0
    s += 30 if w >= 3000 else 25 if w >= 2000 else 18 if w >= 1200 else 10
    return s


def fetch(url, dest):
    if not url:
        return False
    for a in range(4):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=90) as r:
                data = r.read()
            if len(data) > 5000 and data[:2] == b'\xff\xd8':
                io.open(dest, 'wb').write(data)
                return True
            return False
        except urllib.error.HTTPError as ex:
            if ex.code == 429:
                time.sleep(45 + a * 30)
                continue
            return False
        except Exception:
            time.sleep(12)
    return False


def slug(s):
    return re.sub(r'[^a-zA-Z0-9]+', '-', s).strip('-').lower()[:40]


existing = [f for f in os.listdir(OUT) if '-extra-' in f]
state = {}
for sid, entries in cand.items():
    state[sid] = [f for f in existing if f.startswith(sid + '-extra-')]

done = 0
for sid, entries in cand.items():
    have = state[sid]
    need = TARGET - len(have)
    if need <= 0:
        print(f'{sid}: 已有 {len(have)}，跳过')
        continue
    print(f'\n{sid}: 有 {len(have)}，补 {need}')
    pool = sorted([e for e in entries if ok(sid, e)], key=score, reverse=True)

    idx = 0
    for e in pool:
        if len(state[sid]) >= TARGET:
            break
        idx += 1
        name = f'{sid}-extra-s{idx}-{slug(e["title"])}.jpg'
        dest = OUT / name
        if dest.exists():
            state[sid].append(name)
            continue
        if fetch(e.get('thumb'), dest):
            state[sid].append(name)
            done += 1
            print(f'  OK {name[:56]}')
        time.sleep(7)

io.open(WORK / 'state.json', 'w', encoding='utf-8').write(
    json.dumps({k: v for k, v in state.items()}, ensure_ascii=False, indent=2))

print(f'\n本次补 {done} 张')
print('=== 每舰 ===')
for sid, fs in state.items():
    print(f'  {sid:<18} {len(fs)}')
