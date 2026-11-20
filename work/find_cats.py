# 查正确的 Commons 分类名。
#
# 上一轮 weaponimg_fetch.py 有 3 型没找到分类（25mm-96 / 12cm-10ns / 127cm-89）。
# 分类名拼错就空手而归，所以先搜分类命名空间确认。

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
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(12)
                continue
            raise
    return {}


QUERIES = [
    'Type 96 25 mm',
    '25 mm Type 96',
    'Type 89 12.7 cm',
    '12.7 cm Type 89',
    '10th Year Type',
    '12 cm 10th Year',
    '3rd Year Type 20 cm',
    '20 cm 3rd Year',
]

for q in QUERIES:
    d = api({
        'action': 'query',
        'list': 'search',
        'srsearch': q,
        'srnamespace': '14',  # Category 命名空间
        'srlimit': '8',
    })
    hits = d.get('query', {}).get('search', [])
    print(f'\n=== 搜分类「{q}」===')
    if not hits:
        print('  无结果')
    for h in hits:
        print(f"  {h['title']}")
    time.sleep(2)
