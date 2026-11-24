# 诊断：为什么所有分类都返回空
# 先用一个必定存在的分类验证 API 通路，再逐步排查
import json
import ssl
import urllib.parse
import urllib.request

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
HDR = {'User-Agent': 'DockyardArchive/1.0 (research)'}
API = 'https://commons.wikimedia.org/w/api.php'


def call(params):
    url = API + '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=HDR)
    with urllib.request.urlopen(req, timeout=40, context=ctx) as f:
        return json.load(f)


print('=== 1. 用一个必然存在的大分类验证通路 ===')
j = call({'action': 'query', 'list': 'categorymembers',
          'cmtitle': 'Category:Ships', 'cmtype': 'file',
          'cmlimit': '5', 'format': 'json'})
print('  query 键:', list(j.keys()))
print('  categorymembers:', len(j.get('query', {}).get('categorymembers') or []))
print('  原始片段:', json.dumps(j, ensure_ascii=False)[:400])

print('\n=== 2. 试一个已知存在的舰分类（上一轮抓过的）===')
for cat in ['Category:Yokosuka B4Y', 'Category:Mitsubishi A5M']:
    j = call({'action': 'query', 'list': 'categorymembers',
              'cmtitle': cat, 'cmtype': 'file', 'cmlimit': '5', 'format': 'json'})
    n = len(j.get('query', {}).get('categorymembers') or [])
    print(f'  {cat}: {n} 个文件')

print('\n=== 3. 查分类是否存在（titles 方式）===')
for cat in ['Category:Tone (ship, 1937)', 'Category:Japanese cruiser Tone']:
    j = call({'action': 'query', 'titles': cat, 'format': 'json'})
    pages = j.get('query', {}).get('pages') or {}
    for k, v in pages.items():
        print(f'  {cat}: missing={("missing" in v)} title={v.get("title")}')

print('\n=== 4. 搜索真实分类名 ===')
j = call({'action': 'query', 'list': 'search', 'srsearch': 'Tone cruiser',
          'srnamespace': '14', 'srlimit': '8', 'format': 'json'})
for x in (j.get('query', {}).get('search') or []):
    print('  ', x['title'])
