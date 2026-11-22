# 查 Commons 分类正名。
#
# 硬教训（docs/45）：
#   ① 绝对不要用关键词搜图，必须按 Category: 浏览；
#   ② 分类名必须查正名，各国命名规律不同。
#
# 本脚本只做一件事：给定一批候选分类名，查它在 Commons 上是否存在、
# 有多少文件。存在的才拿去做下一步。
import json
import time
import urllib.parse
import urllib.request

UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'
API = 'https://commons.wikimedia.org/w/api.php'

CANDIDATES = {
    # 英国航母
    'ark-royal': [
        'HMS Ark Royal (ship, 1938)',
        'HMS Ark Royal (91)',
        'HMS Ark Royal (ship, 1937)',
        'Ark Royal class aircraft carrier',
    ],
    'victorious': [
        'HMS Victorious (ship, 1939)',
        'HMS Victorious (R38)',
        'HMS Victorious (ship, 1941)',
    ],
    # 英国巡洋舰
    'norfolk': [
        'HMS Norfolk (ship, 1928)',
        'HMS Norfolk (78)',
        'HMS Norfolk (ship, 1930)',
        'County class cruiser',
    ],
    'dorsetshire': [
        'HMS Dorsetshire (ship, 1929)',
        'HMS Dorsetshire (40)',
        'HMS Dorsetshire',
    ],
    'sheffield': [
        'HMS Sheffield (ship, 1937)',
        'HMS Sheffield (C24)',
        'HMS Sheffield (ship, 1936)',
    ],
    # 英国驱逐舰
    'cossack': [
        'HMS Cossack (ship, 1937)',
        'HMS Cossack (F03)',
        'HMS Cossack (G03)',
        'HMS Cossack',
    ],
    'maori': [
        'HMS Maori (ship, 1937)',
        'HMS Maori (F24)',
        'HMS Maori (G24)',
        'HMS Maori',
    ],
    'zulu': [
        'HMS Zulu (ship, 1937)',
        'HMS Zulu (F18)',
        'HMS Zulu (G18)',
        'HMS Zulu',
    ],
    'sikh': [
        'HMS Sikh (ship, 1938)',
        'HMS Sikh (F82)',
        'HMS Sikh (G82)',
        'HMS Sikh',
    ],
    'piorun': [
        'ORP Piorun (ship, 1940)',
        'ORP Piorun (G65)',
        'ORP Piorun',
        'HMS Nerissa (ship, 1940)',
    ],
}


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
                w = 15 + a * 12
                print(f'      429 wait {w}s')
                time.sleep(w)
                continue
            return {'_err': str(e)}
        except Exception as e:
            if a == retries - 1:
                return {'_err': str(e)}
            time.sleep(6)
    return {}


def count(cat):
    d = api({'action': 'query', 'list': 'categorymembers',
             'cmtitle': 'Category:' + cat, 'cmtype': 'file', 'cmlimit': '500'})
    if '_err' in d:
        return None, d['_err']
    members = d.get('query', {}).get('categorymembers', [])
    if not members:
        # 可能是分类不存在
        return 0, 'empty'
    return len(members), 'ok'


results = {}
for sid, cands in CANDIDATES.items():
    print(f'=== {sid} ===')
    hits = []
    for c in cands:
        n, st = count(c)
        flag = 'OK' if n else '--'
        print(f'  [{flag}] {n if n is not None else "?" :>4}  {c}   ({st})')
        if n:
            hits.append((c, n))
        time.sleep(1.5)
    results[sid] = hits
    print()

print('=== 结论：每个实体可用的分类 ===')
for sid, hits in results.items():
    if not hits:
        print(f'  {sid}: 无可用分类')
    else:
        best = max(hits, key=lambda x: x[1])
        print(f'  {sid}: {best[0]}  ({best[1]} 文件)')

with open('work/imgcat_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print('\n已写 work/imgcat_results.json')
