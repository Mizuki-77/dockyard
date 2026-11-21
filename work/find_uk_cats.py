# 英舰分类命名规律：Category:HMS <名> (<舷号>)
import json
import time
import urllib.parse
import urllib.request

UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'
API = 'https://commons.wikimedia.org/w/api.php'

GUESS = {
    'hood': ['HMS Hood (51)', 'HMS Hood (1918)', 'Hood (51)'],
    'illustrious': ['HMS Illustrious (87)', 'Illustrious (87)'],
    'king-george-v': ['HMS King George V (41)', 'King George V (41)'],
    'prince-of-wales': ['HMS Prince of Wales (53)', 'Prince of Wales (53)'],
    'rodney': ['HMS Rodney (29)', 'Rodney (29)'],
    'tirpitz': ['Tirpitz (ship, 1941)', 'German battleship Tirpitz', 'Tirpitz (Battleship)'],
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
    for g in guesses:
        n = count(g)
        if n:
            print(f'  ✓ {g:<44} {n} 文件')
        time.sleep(1.5)
    # 无论如何都列一下 allpages 前缀
    base = guesses[0].split('(')[0].strip()
    d = api({'action': 'query', 'list': 'allpages', 'apnamespace': '14',
             'apprefix': base, 'aplimit': '8'})
    pages = [p['title'] for p in d.get('query', {}).get('allpages', [])]
    if pages:
        print('  同前缀分类:')
        for p in pages:
            print(f'    {p}')
    print()
