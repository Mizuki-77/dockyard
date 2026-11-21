import json
import time
import urllib.parse
import urllib.request

UA = 'DockyardArchive/1.0 (historical research)'
API = 'https://commons.wikimedia.org/w/api.php'


def api(params, retries=5):
    params = dict(params)
    params['format'] = 'json'
    url = API + '?' + urllib.parse.urlencode(params)
    for a in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.loads(r.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(20 + a * 15)
                continue
            raise
        except Exception:
            if a == retries - 1:
                return {}
            time.sleep(8)
    return {}


# Hood / PoW / Rodney：试多种命名
CANDS = {
    'hood': ['HMS Hood (ship, 1920)', 'Hood (ship, 1920)', 'HMS Hood (1920)',
             'HMS Hood (battlecruiser)', 'Hood class battlecruisers'],
    'prince-of-wales': ['HMS Prince of Wales (53)', 'Prince of Wales (53)',
                        'HMS Prince of Wales (ship, 1939)', 'King George V class battleships'],
    'rodney': ['HMS Rodney (29)', 'Rodney (29)', 'HMS Rodney (ship, 1925)',
               'Nelson class battleships'],
}

for sid, cands in CANDS.items():
    print(f'=== {sid} ===')
    for c in cands:
        d = api({'action': 'query', 'list': 'categorymembers', 'cmtitle': 'Category:' + c,
                 'cmtype': 'file', 'cmlimit': '100'})
        ms = d.get('query', {}).get('categorymembers', [])
        if ms:
            print(f'  ✓ {c:<40} {len(ms)} 文件')
        else:
            print(f'    {c:<40} 0')
        time.sleep(2)
