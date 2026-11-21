import json
import time
import urllib.parse
import urllib.request

UA = 'DockyardArchive/1.0 (historical research)'
API = 'https://commons.wikimedia.org/w/api.php'


def api(params):
    params = dict(params)
    params['format'] = 'json'
    url = API + '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    return json.loads(urllib.request.urlopen(req, timeout=30).read().decode('utf-8'))


CANDS = [
    'HMS Prince of Wales (1941)',
    'HMS Prince of Wales (53)',
    'HMS Rodney (1925)',
    'HMS Rodney (29)',
    'HMS Hood (51)',
    'HMS Hood (1920)',
]

for c in CANDS:
    # 先看这个分类存不存在、有多少文件
    d = api({'action': 'query', 'list': 'categorymembers', 'cmtitle': 'Category:' + c,
             'cmlimit': '5'})
    ms = d.get('query', {}).get('categorymembers', [])
    print(f'{c:<32} 成员 {len(ms)}')
    for m in ms[:3]:
        print(f'    {m["title"]}')
    time.sleep(2)

print()
print('=== 直接搜文件 ===')
for q in ['Prince of Wales 1941 battleship', 'Rodney battleship 1941', 'HMS Hood battlecruiser']:
    d = api({'action': 'query', 'list': 'search', 'srsearch': q, 'srnamespace': '6', 'srlimit': '5'})
    print(f'--- {q} ---')
    for h in d.get('query', {}).get('search', []):
        print(f'   {h["title"]}')
    time.sleep(2)
