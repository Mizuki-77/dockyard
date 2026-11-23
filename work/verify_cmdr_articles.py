# 核实维基条目是不是本人，并抓取可行的照片。
#
# 上一步的自动匹配误命中率很高（Louis Armstrong / Halsey 歌手 / 板球员），
# 所以这里逐个核对：取条目的摘要（extract）与描述（description），
# 人工看过的那些才放行。同时取主图与 Commons 文件页。
import io
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request

UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'
EN = 'https://en.wikipedia.org/w/api.php'

# 人工判断为「真实条目」的（上一步逐条看过）
REAL = {
    'Arthur John Power': 'Arthur Power',
    'Augustus Willington Shelton Agar': 'Augustus Agar',
    'Benjamin Charles Stanley Martin': 'Benjamin Martin (Royal Navy officer)',
    'Ernst Lindemann': 'Ernst Lindemann',
    'Eugeniusz Józef Stanisław Pławski': 'Eugeniusz Pławski',
    'Helmuth Brinkmann': 'Helmuth Brinkmann',
    'Karl Topp': 'Karl Topp',
    'Louis Henry Keppel Hamilton': 'Louis Keppel Hamilton',
    'Michael Maynard Denny': 'Michael Denny',
    'Philip Louis Vian': 'Philip Vian',
    'Robert St. Vincent Sherbrooke': 'Robert Sherbrooke',
}

# 待定：可能是本人，也可能是同名（要看过摘要才知道）
MAYBE = {
    'Hans Meyer': 'Hans Meyer',
    'Robert Weber': 'Robert Weber',
    'Richard Taylor White': 'Richard Taylor White',
    'Wolf Junge': 'Wolf Junge',
    'Edward Lyon Berthon': 'Edward Berthon',
    'Daniel de Pass': 'Eliot de Pass',
}


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


def clean(s):
    return ' '.join(re.sub(r'<[^>]+>', '', str(s or '')).split())


def lookup(title):
    d = api({'action': 'query', 'titles': title,
             'prop': 'pageimages|extracts|description',
             'piprop': 'original|thumbnail', 'pithumbsize': '900',
             'exintro': 1, 'explaintext': 1})
    pages = d.get('query', {}).get('pages', {})
    for pid, pg in pages.items():
        if pid == '-1':
            return None
        return {
            'title': pg.get('title'),
            'desc': pg.get('description'),
            'image': pg.get('thumbnail', {}).get('source'),
            'original': pg.get('original', {}).get('source'),
            'extract': clean(pg.get('extract'))[:400],
        }
    return None


print('=== 已判定为真实条目 ===')
real_out = {}
for person, title in REAL.items():
    r = lookup(title)
    if not r:
        print(f'  !  {person}: 取不到')
        continue
    real_out[person] = r
    print(f'  {"IMG" if r["image"] else "   "} {person}')
    print(f'      {r["title"]} · {r["desc"] or ""}')
    print(f'      {r["extract"][:150]}')
    time.sleep(1.3)

print()
print('=== 待定（看摘要判断是否本人） ===')
maybe_out = {}
for person, title in MAYBE.items():
    r = lookup(title)
    if not r:
        continue
    maybe_out[person] = r
    print(f'  {person}  ->  {r["title"]} · {r["desc"] or ""}')
    print(f'      {r["extract"][:170]}')
    time.sleep(1.3)

io.open('work/cmdr_verified.json', 'w', encoding='utf-8').write(
    json.dumps({'real': real_out, 'maybe': maybe_out},
               ensure_ascii=False, indent=2))
print()
print('已写 work/cmdr_verified.json')
