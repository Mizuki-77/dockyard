# 用 Commons 搜索找到正确的分类名（上一次是猜的，多数不存在）
import json
import ssl
import urllib.parse
import urllib.request

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
HDR = {'User-Agent': 'DockyardArchive/1.0 (research)'}
API = 'https://commons.wikimedia.org/w/api.php'

QUERIES = {
    '15cm-50-t41': '15.5 cm gun Japanese',
    '8cm-40-3ns': '8 cm 40 Type 3 gun Japanese',
    '5in25-mk10': '5 inch 25 caliber gun',
    '8in-55-mk9': '8 inch 55 caliber gun',
    '8in-55-mk15': '8 inch 55 Mark 15',
    '21in-mk15': 'Mark 15 torpedo US Navy',
    'a5m4': 'A5M Claude fighter',
    'b4y1': 'B4Y Jean',
    '20cm-3ns-no2': '20 cm 50 Japanese gun',
    '45in-45-mk1': '4.5 inch naval gun',
    '47in-45-mk12': '4.7 inch Mark XII',
}


def search_categories(term, limit=6):
    """在分类命名空间（14）里搜"""
    q = urllib.parse.urlencode({
        'action': 'query', 'list': 'search', 'srsearch': term,
        'srnamespace': '14', 'srlimit': str(limit), 'format': 'json',
    })
    req = urllib.request.Request(API + '?' + q, headers=HDR)
    with urllib.request.urlopen(req, timeout=30, context=ctx) as f:
        j = json.load(f)
    return [x['title'] for x in (j.get('query', {}).get('search') or [])]


def cat_count(cat):
    q = urllib.parse.urlencode({
        'action': 'query', 'list': 'categorymembers', 'cmtitle': cat,
        'cmtype': 'file', 'cmlimit': '1', 'format': 'json',
    })
    req = urllib.request.Request(API + '?' + q, headers=HDR)
    with urllib.request.urlopen(req, timeout=30, context=ctx) as f:
        j = json.load(f)
    members = j.get('query', {}).get('categorymembers') or []
    return len(members) > 0


for wid, term in QUERIES.items():
    print(f'\n=== {wid}  (搜: {term})')
    try:
        cats = search_categories(term)
    except Exception as e:
        print('   搜索失败:', type(e).__name__, str(e)[:60])
        continue
    if not cats:
        print('   无分类命中')
        continue
    for c in cats:
        try:
            has = cat_count(c)
        except Exception:
            has = False
        mark = '有图' if has else ' 空 '
        print(f'   [{mark}] {c}')
