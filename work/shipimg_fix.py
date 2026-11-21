# 剔除人工核对后不合格的图，并从候选池里替补。
import io
import json
import re
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / 'work' / 'shipimg'
OUT = ROOT / 'public' / 'img' / 'ships'
UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'

# 明确要剔除的（人工核对结果）
DROP = {
    'yorktown': ['yorktown-extra-7-large-explosion-aboard-uss-lexington-cv-2-8-.jpg',
                 'yorktown-extra-12-uss-yorktown-cv-5-uss-texas-bb-35-uss-jacob-.jpg'],
    'hood': ['hood-extra-9-hms-hood-51-march-17-1924-jpg.jpg',
             'hood-extra-10-hms-hood-51-march-17-1924-png.jpg',
             'hood-extra-11-hms-hood-51-march-17-1924-original-scan-tif.jpg',
             'hood-extra-12-hms-hood-51-march-17-1924-partial-restoratio.jpg'],
    'prince-of-wales': ['prince-of-wales-extra-6-winston-churchill-during-the-second-world-wa.jpg',
                        'prince-of-wales-extra-10-the-royal-navy-during-the-second-world-war-a.jpg'],
    'enterprise': ['enterprise-extra-4-bayonne-naval-supply-depot-with-uss-e.jpg',
                   'enterprise-extra-11-u-s-navy-reserve-ships-at-the-bayonn.jpg',
                   'enterprise-extra-12-u-s-navy-reserve-ships-at-the-bayonn.jpg'],
    'bismarck': ['bismarck-extra-11-adolf-hitler-och-andra-naziledare-h-ls.jpg',
                 'bismarck-extra-12-the-polish-institute-and-sikorski-muse.jpg'],
    'prinz-eugen': ['prinz-eugen-extra-1-uss-prinz-eugen-ix-300-at-sea-during.jpg'],
}

# 替补：从候选里按优先级重新挑，避开已选的标题
picked = json.load(io.open(WORK / 'picked.json', encoding='utf-8'))
cand = json.load(io.open(WORK / 'candidates.json', encoding='utf-8'))


def clean(s):
    return ' '.join(re.sub(r'<[^>]+>', '', str(s or '')).split())


def slug(s):
    s = re.sub(r'[^a-zA-Z0-9]+', '-', s).strip('-').lower()
    return s[:44]


def download(url, dest):
    url = url.replace('upload.wikimedia.org', 'thumb.wikimedia.org')
    for a in range(5):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            if len(data) < 3000:
                return False
            io.open(dest, 'wb').write(data)
            return True
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(20 + a * 15)
                continue
            return False
        except Exception:
            time.sleep(5)
    return False


# 更严的排除（用于替补）
STRICT_BAD = [
    'churchill', 'hitler', 'lexington', 'texas', 'jacob', 'piorun',
    'restoration', 'original scan', 'partial', 'bayonne', 'reserve ships',
    'signal flying', 'badge', 'crest', 'stamp', 'medal', 'map', 'chart',
    'drawing', 'model', 'diorama', 'painting', 'wreck', 'underwater',
    'survivors', 'explosion', 'sinking', 'cemetery', 'memorial',
    'crew', 'sailor', 'payday', 'ceremony', 'launching',
]


def strict_bad(e):
    blob = (e['title'] + ' ' + e.get('desc', '')).lower()
    for w in STRICT_BAD:
        if w in blob:
            return w
    return None


def score(e):
    blob = (e['title'] + ' ' + e.get('desc', '')).lower()
    lic = e.get('license', '')
    s = 0
    if 'Public domain' in lic:
        s += 100
    elif 'CC0' in lic:
        s += 95
    elif lic.startswith('CC'):
        s += 40
    for v in ['broadside', 'underway', 'at sea', 'steaming', 'aerial',
              'overhead', 'starboard', 'port side', 'full view', 'at anchor']:
        if v in blob:
            s += 25
            break
    w = e.get('w') or 0
    if w >= 3000:
        s += 30
    elif w >= 2000:
        s += 25
    elif w >= 1200:
        s += 18
    elif w >= 800:
        s += 10
    else:
        s -= 50
    return s


print('=== 剔除 ===')
for sid, names in DROP.items():
    for n in names:
        p = OUT / n
        if p.exists():
            p.unlink()
            print(f'  删除 {n[:60]}')
        # 从 picked 里去掉
        picked[sid] = [x for x in picked[sid] if x['name'] != n]

print()
print('=== 补选 ===')
for sid, names in DROP.items():
    need = len(names)
    used_titles = {x['title'] for x in picked.get(sid, [])}
    pool = []
    for e in cand.get(sid, []):
        if e['title'] in used_titles:
            continue
        if (e.get('w') or 0) < 800:
            continue
        if strict_bad(e):
            continue
        pool.append(e)
    pool.sort(key=score, reverse=True)

    for e in pool[:need]:
        n = f'{sid}-extra-fix-{slug(e["title"])}.jpg'
        dest = OUT / n
        ok = download(e.get('thumb'), dest)
        print(f'  {sid}: {"OK" if ok else "失败"} {n[:60]}')
        if ok:
            picked.setdefault(sid, []).append({
                'name': n,
                'title': e['title'],
                'license': e['license'],
                'artist': e['artist'],
                'desc': e.get('desc', ''),
                'date': e.get('date', ''),
                'page': e.get('page'),
                'w': e.get('w'), 'h': e.get('h'),
            })
        time.sleep(3)

io.open(WORK / 'picked.json', 'w', encoding='utf-8').write(
    json.dumps(picked, ensure_ascii=False, indent=2))

print()
print('=== 最终每舰张数 ===')
for sid, entries in picked.items():
    print(f'  {sid:<18} {len(entries)}')
