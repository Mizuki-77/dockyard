# 用正名盘点 15 舰的素材总量，并与现有登记数对比出缺口。
import io
import json
import time
import urllib.parse
import urllib.request

import yaml

UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'
API = 'https://commons.wikimedia.org/w/api.php'

CATS = {
    'akagi': 'Akagi (ship, 1927)',
    'bismarck': 'Bismarck (ship, 1939)',
    'enterprise': 'USS Enterprise (CV-6)',
    'hiryu': 'Hiryū (ship, 1939)',
    'hood': 'HMS Hood (51)',
    'hornet': 'USS Hornet (CV-8)',
    'illustrious': 'HMS Illustrious (87)',
    'kaga': 'Kaga (ship, 1928)',
    'king-george-v': 'HMS King George V (41)',
    'prince-of-wales': 'HMS Prince of Wales (1941)',
    'prinz-eugen': 'Prinz Eugen (ship, 1938)',
    'rodney': 'HMS Rodney (1925)',
    'soryu': 'Sōryū (ship, 1937)',
    'tirpitz': 'Tirpitz (ship, 1941)',
    'yorktown': 'USS Yorktown (CV-5)',
}


def api(params):
    params = dict(params)
    params['format'] = 'json'
    url = API + '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(15)
                continue
            raise
        except Exception:
            if attempt == 2:
                return {}
            time.sleep(3)
    return {}


def count(cat):
    d = api({'action': 'query', 'list': 'categorymembers', 'cmtitle': 'Category:' + cat,
             'cmtype': 'file', 'cmlimit': '500'})
    return len(d.get('query', {}).get('categorymembers', []))


d = yaml.safe_load(io.open('data/images.yaml', encoding='utf-8'))
have = {}
for im in d['images']:
    s = str(im.get('subject') or '')
    if s.startswith('ship:'):
        have[s[5:]] = have.get(s[5:], 0) + 1

print(f'{"舰":<18} {"现有":<6} {"Commons 可用":<12} {"缺口"}')
print('-' * 52)
total_have = 0
total_avail = 0
for sid, cat in CATS.items():
    n = count(cat)
    h = have.get(sid, 0)
    total_have += h
    total_avail += n
    print(f'{sid:<18} {h:<6} {n:<12} {max(0, n - h)}')
    time.sleep(1.5)

print()
print(f'现有 {total_have} 张 / 素材池 {total_avail} 张')
print(f'若每舰再补 10 张，需要新增约 {15 * 10 - total_have} 张')
