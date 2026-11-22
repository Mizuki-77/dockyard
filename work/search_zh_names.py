# 用维基搜索 API 补查没直接命中的舰名。
import json
import time
import urllib.parse
import urllib.request

QUERIES = {
    'king-george-v': '英王乔治五世号 战列舰',
    'prince-of-wales': '威尔士亲王号 战列舰',
    'illustrious': '光辉号 航空母舰',
    'sheffield': '谢菲尔德号 轻巡洋舰',
    'norfolk': '诺福克号 重巡洋舰',
    'cossack': '哥萨克号 驱逐舰',
    'maori': '毛利人号 驱逐舰',
    'zulu': '祖鲁人号 驱逐舰',
    'sikh': '锡克人号 驱逐舰',
    'bismarck': '俾斯麦号 战舰',
    'tirpitz': '提尔皮茨号 战列舰',
    'prinz-eugen': '欧根亲王号 重巡洋舰',
    'piorun': '闪电号 驱逐舰 波兰',
}


def search(q, retries=4):
    url = 'https://zh.wikipedia.org/w/api.php?' + urllib.parse.urlencode({
        'action': 'query', 'list': 'search', 'srsearch': q,
        'format': 'json', 'srlimit': 4, 'srprop': 'snippet',
    })
    req = urllib.request.Request(url, headers={
        'User-Agent': 'DockyardNameCheck/1.0 (contact: dockyard local tool)'})
    last = None
    for attempt in range(retries):
        try:
            d = json.loads(urllib.request.urlopen(req, timeout=25).read().decode('utf-8'))
            return [r['title'] for r in d.get('query', {}).get('search', [])]
        except Exception as e:
            last = e
            time.sleep(3 * (attempt + 1))
    return [f'ERR {last}']


for sid, q in QUERIES.items():
    hits = search(q)
    print(f'{sid:<18} {q}')
    for h in hits:
        print(f'                   - {h}')
    print()
    time.sleep(2.0)
