# 从 899 条候选里筛选，每舰挑一批质量好的，下载。
#
# 用户的明确要求：「大部分时候侧舷图就够用了，也别太多了，筛选一些」。
#
# 筛选规则：
# 1. 硬排除：不是本舰（同名别舰/现代舰）、模型、徽章、地图、邮票、残骸内部、
#    水兵生活照（甲板洗地之类）、明显无关
# 2. 优先 PD/CC0（本站 A 档，可归档）
# 3. 优先「整舰可见」的构图（broadside / 航行中 / 锚泊全景）
# 4. 尺寸 >= 800 宽（模型玩家要能看清结构）
# 5. 每舰上限 12 张（用户说别太多）
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

# 每舰上限
LIMIT = 12

# 硬排除关键词（标题+描述里出现就丢）
BAD = [
    'badge', 'crest', 'coat of arms', 'emblem', 'shield',
    'map', 'chart', 'diagram', 'plan', 'drawing',
    'stamp', 'postal', 'coin', 'medal', 'banknote',
    'model', 'kit', 'diorama', 'painting', 'artwork', 'illustration',
    'poster', 'propaganda', 'cartoon', 'comic',
    'wreck', 'wreckage', 'debris', 'salvage', 'underwater',
    'grave', 'memorial', 'plaque', 'monument', 'museum ship',
    'launch ceremony', 'christening', 'commissioning ceremony',
    'crew', 'sailor', 'seaman', 'payday', 'scrubbing', 'washing',
    'sleeping', 'cooking', 'galley', 'mess', 'church service',
    'interview', 'portrait', 'group photo', 'posing',
    'port', 'harbour', 'harbor',  # 过多锚泊照，先排除（下面会作为备选放宽）
    'logo', 'flag', 'ensign',
    'space shuttle', 'starship', 'fictional',
    'R09', 'CVN-65', 'CV-10', 'CV-11',  # 同名现代舰
    '(1902)', '(1911)', '(1896)', '(1891)', '(1765)', '(1794)', '(1904)',
]

# 强优先：整舰构图
GOOD_VIEW = ['broadside', 'underway', 'at sea', 'steaming', 'aerial', 'overhead',
             'starboard', 'port side', 'port bow', 'starboard bow',
             'full view', 'in the firth', 'at anchor']

# 每舰排除的同名别舰
EXCLUDE_SHIP = {
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


def clean(s):
    return ' '.join(re.sub(r'<[^>]+>', '', str(s or '')).split())


def is_bad(entry):
    blob = (entry['title'] + ' ' + entry.get('desc', '')).lower()
    for w in BAD:
        if w.lower() in blob:
            return w
    return None


def ship_excluded(sid, entry):
    blob = (entry['title'] + ' ' + entry.get('desc', '')).lower()
    for w in EXCLUDE_SHIP.get(sid, []):
        if w.lower() in blob:
            return w
    return None


def score(entry):
    blob = (entry['title'] + ' ' + entry.get('desc', '')).lower()
    lic = entry.get('license', '')
    s = 0

    if 'Public domain' in lic:
        s += 100
    elif 'CC0' in lic:
        s += 95
    elif lic.startswith('CC'):
        s += 40
    else:
        s += 5

    for v in GOOD_VIEW:
        if v in blob:
            s += 25
            break

    w = entry.get('w') or 0
    if w >= 3000:
        s += 30
    elif w >= 2000:
        s += 25
    elif w >= 1200:
        s += 18
    elif w >= 800:
        s += 10
    else:
        s -= 50  # 太小，模型玩家用不上

    # 说明里提到舰名加一点（确认是本舰）
    if any(x in blob for x in ['bismarck', 'tirpitz', 'akagi', 'kaga', 'soryu',
                                'hiryu', 'hood', 'illustrious', 'enterprise',
                                'yorktown', 'hornet', 'rodney', 'prince of wales',
                                'prinz eugen', 'king george']):
        s += 10

    return s


def download(url, dest):
    try:
        url = url.replace('upload.wikimedia.org', 'thumb.wikimedia.org')
    except Exception:
        pass
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
                w = 20 + a * 15
                print(f'      429 wait {w}s')
                time.sleep(w)
                continue
            return False
        except Exception:
            time.sleep(5)
    return False


def slug(s):
    s = re.sub(r'[^a-zA-Z0-9]+', '-', s).strip('-').lower()
    return s[:44]


def main():
    cand = json.load(io.open(WORK / 'candidates.json', encoding='utf-8'))
    OUT.mkdir(parents=True, exist_ok=True)
    picked_all = {}

    for sid, entries in cand.items():
        print(f'\n=== {sid} ({len(entries)} 候选) ===')
        pool = []
        for e in entries:
            b = is_bad(e)
            if b:
                continue
            x = ship_excluded(sid, e)
            if x:
                continue
            if (e.get('w') or 0) < 800:
                continue
            pool.append(e)

        pool.sort(key=score, reverse=True)
        chosen = pool[:LIMIT]
        print(f'  筛后 {len(pool)} 条，取前 {len(chosen)}')

        got = []
        for i, e in enumerate(chosen):
            name = f'{sid}-extra-{i+1}-{slug(e["title"])}.jpg'
            dest = OUT / name
            if dest.exists():
                print(f'    [{i+1}] 已存在 {name}')
                got.append((e, name))
                continue
            ok = download(e.get('thumb'), dest)
            print(f'    [{i+1}] {"OK" if ok else "失败"} {name}')
            if ok:
                got.append((e, name))
            time.sleep(3)

        picked_all[sid] = [
            {
                'name': n,
                'title': e['title'],
                'license': e['license'],
                'artist': e['artist'],
                'desc': e.get('desc', ''),
                'date': e.get('date', ''),
                'page': e.get('page'),
                'w': e.get('w'), 'h': e.get('h'),
            }
            for e, n in got
        ]

    io.open(WORK / 'picked.json', 'w', encoding='utf-8').write(
        json.dumps(picked_all, ensure_ascii=False, indent=2))
    total = sum(len(v) for v in picked_all.values())
    print(f'\n下载完成 {total} 张')


if __name__ == '__main__':
    main()
