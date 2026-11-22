# 针对「切片覆盖但图池没有对应年代」的舰，专门补早期整舰图。
# 目标：欧根亲王、加贺、赤城、光辉（1955-57）。
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

cand = json.load(io.open(WORK / 'candidates.json', encoding='utf-8'))

# 各舰需要的年代窗口
NEED = {
    'prinz-eugen': ['1938', '1940', '1941', '1942', '1943', '1944'],
    'kaga': ['1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935'],
    'akagi': ['1927', '1928', '1930', '1932', '1934', '1936', '1938'],
    'illustrious': ['1955', '1956', '1957'],
}

LOCAL = ['turret', 'superstructure', 'bridge', 'propeller', 'catapult',
         'aircraft_handling', 'weapon', 'radar', 'detail']

BAD = [
    'badge', 'crest', 'map', 'chart', 'diagram', 'drawing', 'stamp', 'medal',
    'model', 'diorama', 'painting', 'artwork', 'poster', 'propaganda',
    'wreck', 'underwater', 'grave', 'memorial', 'crew', 'sailor', 'payday',
    'churchill', 'hitler', 'portrait', 'survivors', 'explosion', 'sinking',
    'ceremony', 'launching', 'christening', 'restoration', 'scan',
]


def blob(e):
    return (e['title'] + ' ' + (e.get('desc') or '')).lower()


def year_of(e):
    for src in (e.get('date', ''), e.get('title', ''), e.get('desc', '')):
        m = re.search(r'(19[2-5]\d)', str(src))
        if m:
            return m.group(1)
    return None


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
                time.sleep(40 + a * 30)
                continue
            return False
        except Exception:
            time.sleep(10)
    return False


def slug(s):
    return re.sub(r'[^a-zA-Z0-9]+', '-', s).strip('-').lower()[:40]


# 已有图片记录，避免重复
import yaml
d = yaml.safe_load(io.open('data/images.yaml', encoding='utf-8'))
existing_titles = {str(x.get('title', {}).get('en', '')) for x in d['images']}

added = []
for sid, years in NEED.items():
    print(f'\n=== {sid} 需要 {years[0]}-{years[-1]} ===')
    entries = cand.get(sid, [])
    # 候选里该舰的条目，且年代落在需要的范围
    pool = []
    for e in entries:
        b = blob(e)
        if any(w in b for w in BAD):
            continue
        if any(w in b for w in LOCAL):
            continue
        y = year_of(e)
        if y not in years:
            continue
        if e['title'] in existing_titles:
            continue
        if (e.get('w') or 0) < 700:
            continue
        t = e['title'].lower()
        if any(x in t for x in ['.ogv', '.webm', '.tif', '.tiff', '.pdf']):
            continue
        pool.append((y, e))

    pool.sort(key=lambda x: -(x[1].get('w') or 0))
    print(f'  可用 {len(pool)} 条')

    n = 0
    for y, e in pool:
        if n >= 4:
            break
        name = f'{sid}-early-{y}-{slug(e["title"])}.jpg'
        dest = OUT / name
        if dest.exists():
            continue
        if fetch(e.get('thumb'), dest):
            added.append((sid, name, y, e))
            n += 1
            print(f'    OK {y}  {name[:56]}')
        time.sleep(6)

print(f'\n新增 {len(added)} 张')
io.open(WORK / 'early_added.json', 'w', encoding='utf-8').write(
    json.dumps([{'sid': s, 'name': n, 'year': y, 'title': e['title'],
                 'license': e.get('license'), 'artist': e.get('artist'),
                 'desc': e.get('desc'), 'date': e.get('date'),
                 'page': e.get('page'), 'w': e.get('w'), 'h': e.get('h')}
                for s, n, y, e in added], ensure_ascii=False, indent=2))
