# 用 Commons 的 prefixsearch 找舰船分类正名（比全文搜精准）。
import json
import time
import urllib.parse
import urllib.request

UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'
API = 'https://commons.wikimedia.org/w/api.php'

# 每舰给几个前缀猜测
GUESS = {
    'enterprise': ['Enterprise (CV-6)', 'USS Enterprise (CV-6)', 'Enterprise (ship, 1938)'],
    'hiryu': ['Hiryū', 'Hiryū (ship, 1939)', 'Hiryu'],
    'hood': ['Hood (ship, 1918)', 'HMS Hood', 'Hood (battlecruiser)'],
    'hornet': ['Hornet (CV-8)', 'USS Hornet (CV-8)', 'Hornet (ship, 1940)'],
    'illustrious': ['Illustrious (87)', 'Illustrious (ship, 1939)', 'HMS Illustrious'],
    'king-george-v': ['King George V (41)', 'King George V (ship, 1939)', 'HMS King George V'],
    'prince-of-wales': ['Prince of Wales (53)', 'Prince of Wales (ship, 1939)', 'HMS Prince of Wales'],
    'rodney': ['Rodney (29)', 'Rodney (ship, 1925)', 'HMS Rodney'],
    'soryu': ['Sōryū', 'Sōryū (ship, 1937)', 'Soryu'],
    'tirpitz': ['Tirpitz', 'Tirpitz (ship, 1939)', 'Tirpitz (battleship)'],
    'yorktown': ['Yorktown (CV-5)', 'USS Yorktown (CV-5)', 'Yorktown (ship, 1936)'],
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


for sid, guesses in GUESS.items():
    print(f'=== {sid} ===')
    best = None
    for g in guesses:
        n = count(g)
        if n:
            print(f'  {g:<40} {n} 文件  ✓')
            if not best or n > best[1]:
                best = (g, n)
        else:
            print(f'  {g:<40} 0')
        time.sleep(1.5)
    if not best:
        # prefixsearch
        d = api({'action': 'query', 'list': 'allpages', 'apnamespace': '14',
                 'apprefix': guesses[0].split('(')[0].strip(), 'aplimit': '10'})
        print('  prefixsearch:')
        for p in d.get('query', {}).get('allpages', []):
            print(f'    {p["title"]}')
    print()
