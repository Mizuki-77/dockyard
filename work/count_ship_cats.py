# 查 15 艘舰在 Commons 上的分类里有多少可用素材。
# 只查数量与分类名，不下图 —— 先看盘子有多大。
import json
import time
import urllib.parse
import urllib.request

UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'
API = 'https://commons.wikimedia.org/w/api.php'

SHIPS = {
    'akagi': ['Category:Akagi (ship, 1927)'],
    'bismarck': ['Category:Bismarck (ship, 1939)'],
    'enterprise': ['Category:Enterprise (CV-6)'],
    'hiryu': ['Category:Hiryū (ship, 1937)'],
    'hood': ['Category:Hood (ship, 1918)'],
    'hornet': ['Category:Hornet (CV-8)'],
    'illustrious': ['Category:Illustrious (ship, 1939)'],
    'kaga': ['Category:Kaga (ship, 1928)'],
    'king-george-v': ['Category:King George V (ship, 1939)'],
    'prince-of-wales': ['Category:Prince of Wales (ship, 1939)'],
    'prinz-eugen': ['Category:Prinz Eugen (ship, 1938)'],
    'rodney': ['Category:Rodney (ship, 1925)'],
    'soryu': ['Category:Sōryū (ship, 1935)'],
    'tirpitz': ['Category:Tirpitz (ship, 1939)'],
    'yorktown': ['Category:Yorktown (CV-5)'],
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


def count_cat(cat):
    d = api({'action': 'query', 'list': 'categorymembers', 'cmtitle': cat,
             'cmtype': 'file', 'cmlimit': '500'})
    return len(d.get('query', {}).get('categorymembers', []))


print(f'{"舰":<18} {"分类":<38} {"文件数"}')
print('-' * 70)
for sid, cats in SHIPS.items():
    for c in cats:
        try:
            n = count_cat(c)
        except Exception as e:
            n = f'ERR'
        mark = '' if n and isinstance(n, int) and n > 0 else '  ← 分类名可能错'
        print(f'{sid:<18} {c:<38} {n}{mark}')
        if not n or not isinstance(n, int):
            # 搜正名
            d = api({'action': 'query', 'list': 'search', 'srsearch': sid.replace('-', ' '),
                     'srnamespace': '14', 'srlimit': '3'})
            for h in d.get('query', {}).get('search', []):
                print(f'{"":<18}   候选: {h["title"]}')
        time.sleep(2)
