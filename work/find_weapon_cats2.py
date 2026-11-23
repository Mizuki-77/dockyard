# 继续找剩余武器的 Commons 分类（上一轮被 429 限流）
# 交接报告 §7.2 第 3 条：Commons 对本站持续限流，必须放慢并重试。
import json
import ssl
import time
import urllib.parse
import urllib.request

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
HDR = {'User-Agent': 'DockyardArchive/1.0 (research; low-rate)'}
API = 'https://commons.wikimedia.org/w/api.php'

QUERIES = {
    '8in-55-mk9': '8 inch 55 caliber naval gun',
    '8in-55-mk15': 'heavy cruiser main gun 8 inch',
    '21in-mk15': 'Mark 15 torpedo',
    'a5m4': 'Mitsubishi A5M',
    'b4y1': 'Yokosuka B4Y',
    '20cm-3ns-no2': '20 cm 50 caliber Japanese naval gun',
    '45in-45-mk1': 'QF 4.5 inch',
    '47in-45-mk12': 'QF 4.7 inch',
}


def api(params, tries=4):
    q = urllib.parse.urlencode(params)
    url = API + '?' + q
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=HDR)
            with urllib.request.urlopen(req, timeout=40, context=ctx) as f:
                return json.load(f)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = 5 * (i + 1)
                print(f'      429，等 {wait}s 重试...')
                time.sleep(wait)
                continue
            raise
    return {}


def search_categories(term, limit=6):
    j = api({'action': 'query', 'list': 'search', 'srsearch': term,
             'srnamespace': '14', 'srlimit': str(limit), 'format': 'json'})
    return [x['title'] for x in (j.get('query', {}).get('search') or [])]


def cat_has_files(cat):
    j = api({'action': 'query', 'list': 'categorymembers', 'cmtitle': cat,
             'cmtype': 'file', 'cmlimit': '1', 'format': 'json'})
    return len(j.get('query', {}).get('categorymembers') or []) > 0


results = {}
for wid, term in QUERIES.items():
    print(f'\n=== {wid}  (搜: {term})')
    try:
        cats = search_categories(term)
    except Exception as e:
        print('   搜索失败:', type(e).__name__, str(e)[:60])
        continue
    time.sleep(2)
    if not cats:
        print('   无分类命中')
        continue
    good = []
    for c in cats:
        try:
            has = cat_has_files(c)
        except Exception:
            has = False
        mark = '有图' if has else ' 空 '
        print(f'   [{mark}] {c}')
        if has:
            good.append(c)
        time.sleep(1.5)
    if good:
        results[wid] = good[0]

print('\n\n===== 可用分类汇总 =====')
for k, v in results.items():
    print(f'  {k:16} → {v}')
