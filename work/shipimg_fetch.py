# 批量抓 15 艘舰的候选图元数据（分类浏览，不用关键词搜索）。
# 每舰取前 N 个文件，先看盘子，再筛选。
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

# 2026-11-22 实测确认的正名
CATS = {
    'akagi': 'Akagi (ship, 1927)',
    'bismarck': 'Bismarck (ship, 1939)',
    'enterprise': 'USS Enterprise (CV-6)',
    'hiryu': 'Hiryū (ship, 1939)',
    'hornet': 'USS Hornet (CV-8)',
    'illustrious': 'HMS Illustrious (87)',
    'kaga': 'Kaga (ship, 1928)',
    'king-george-v': 'HMS King George V (41)',
    'prinz-eugen': 'Prinz Eugen (ship, 1938)',
    'soryu': 'Sōryū (ship, 1937)',
    'tirpitz': 'Tirpitz (ship, 1941)',
    'yorktown': 'USS Yorktown (CV-5)',
    # 这三艘待确认，先用最可能的
    'hood': 'HMS Hood (ship, 1920)',
    'prince-of-wales': 'HMS Prince of Wales (ship, 1941)',
    'rodney': 'HMS Rodney (ship, 1925)',
}


def api(params, retries=5):
    params = dict(params)
    params['format'] = 'json'
    url = API + '?' + urllib.parse.urlencode(params)
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.loads(r.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = 20 + attempt * 15
                print(f'    429, wait {wait}s')
                time.sleep(wait)
                continue
            raise
        except Exception:
            if attempt == retries - 1:
                return {}
            time.sleep(8)
    return {}


def cat_files(cat, limit=80):
    out = []
    cont = {}
    while len(out) < limit:
        p = {'action': 'query', 'list': 'categorymembers', 'cmtitle': 'Category:' + cat,
             'cmtype': 'file', 'cmlimit': '50'}
        p.update(cont)
        d = api(p)
        ms = d.get('query', {}).get('categorymembers', [])
        out += [m['title'] for m in ms]
        if 'continue' in d:
            cont = d['continue']
            time.sleep(3)
        else:
            break
    return out[:limit]


def imageinfo(titles):
    res = {}
    for i in range(0, len(titles), 20):
        batch = titles[i:i + 20]
        d = api({'action': 'query', 'titles': '|'.join(batch),
                 'prop': 'imageinfo',
                 'iiprop': 'url|size|extmetadata|mime', 'iiurlwidth': '1280'})
        res.update(d.get('query', {}).get('pages', {}))
        time.sleep(3)
    return res


def clean(s):
    import re
    return ' '.join(re.sub(r'<[^>]+>', '', str(s or '')).split())


def main():
    WORK.mkdir(parents=True, exist_ok=True)
    out = {}

    for sid, cat in CATS.items():
        print(f'\n=== {sid} ({cat}) ===')
        files = cat_files(cat)
        print(f'  分类返回 {len(files)} 个文件')
        if not files:
            out[sid] = []
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
                'w': ii.get('width'),
                'h': ii.get('height'),
                'mime': ii.get('mime'),
                'license': clean((em.get('LicenseShortName') or {}).get('value')),
                'artist': clean((em.get('Artist') or {}).get('value'))[:180],
                'desc': clean((em.get('ImageDescription') or {}).get('value'))[:250],
                'date': clean((em.get('DateTimeOriginal') or {}).get('value'))[:40],
                'page': ii.get('descriptionurl'),
            })
        entries.sort(key=lambda e: -(e.get('w') or 0))
        out[sid] = entries
        lic_pd = sum(1 for e in entries if 'Public domain' in e['license'] or 'CC0' in e['license'])
        print(f'  取到 {len(entries)} 条，其中 PD/CC0 {lic_pd}')
        time.sleep(4)

    io.open(WORK / 'candidates.json', 'w', encoding='utf-8').write(
        json.dumps(out, ensure_ascii=False, indent=2))
    print(f'\n写入 {WORK / "candidates.json"}')
    print(f'总计 {sum(len(v) for v in out.values())} 条')


if __name__ == '__main__':
    main()
