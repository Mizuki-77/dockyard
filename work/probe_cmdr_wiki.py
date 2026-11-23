# 换一条路找照片：先查英文维基有没有这个人的条目，
# 有条目就取页面主图（pageimages）—— 那些图都在 Commons 上。
#
# 为什么这比直接搜 Commons 好：
#   Commons 的搜索是全文检索，人名带军衔、缩写、中间名时匹配不上；
#   维基条目是**人为挂上去的**，编者为人物条目挑的就是肖像照，
#   命中率远高于全文搜。
import io
import json
import time
import urllib.error
import urllib.parse
import urllib.request

UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'
EN = 'https://en.wikipedia.org/w/api.php'

data = json.load(io.open('work/cmdr_rows.json', encoding='utf-8'))
people = data['people']


def api(params, retries=5):
    params = dict(params)
    params['format'] = 'json'
    url = EN + '?' + urllib.parse.urlencode(params)
    for a in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.loads(r.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(15 + a * 12)
                continue
            return {}
        except Exception:
            if a == retries - 1:
                return {}
            time.sleep(6)
    return {}


out = {}
for key, p in sorted(people.items()):
    name = p['name']
    # 第一步：搜条目
    d = api({'action': 'query', 'list': 'search', 'srsearch': name,
             'srlimit': '3'})
    hits = d.get('query', {}).get('search', [])
    if not hits:
        out[name] = {'article': None, 'image': None}
        print(f'  -  {name:<42} 无条目')
        time.sleep(1.2)
        continue

    title = hits[0]['title']
    # 第二步：取该页主图
    d2 = api({'action': 'query', 'titles': title,
              'prop': 'pageimages', 'piprop': 'original|thumbnail',
              'pithumbsize': '800'})
    pages = d2.get('query', {}).get('pages', {})
    img = None
    orig = None
    for pid, pg in pages.items():
        img = pg.get('thumbnail', {}).get('source')
        orig = pg.get('original', {}).get('source')
    out[name] = {'article': title, 'image': img, 'original': orig}
    flag = 'IMG' if img else '   '
    print(f'  {flag} {name:<42} {title[:52]}')
    time.sleep(1.2)

io.open('work/cmdr_wiki.json', 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=2))

withart = sum(1 for v in out.values() if v['article'])
withimg = sum(1 for v in out.values() if v['image'])
print()
print(f'有维基条目：{withart} / {len(out)}')
print(f'有条目且有主图：{withimg} / {len(out)}')
