# 实测：36 位指挥官在 Commons 上有没有照片。
#
# 这一步行不行决定了整个功能的样子 —— 如果只有 5 个人有照片，
# 就不该给每人建一页放个大空框。
#
# 查法（不用关键词搜，那会混进同名的人）：
#   ① 先用 Commons 搜索 API 搜人名 + 限定文件命名空间
#   ② 再核一遍：文件名或描述里要出现军衔/舰名/年代之一，否则算误命中
import io
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request

UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'
API = 'https://commons.wikimedia.org/w/api.php'

data = json.load(io.open('work/cmdr_rows.json', encoding='utf-8'))
people = data['people']

# 给每个人补一点检索上下文，压掉同名误命中
HINT = {
    'A. J. L. Phillips': 'Norfolk cruiser captain',
    'Arthur John Power': 'Ark Royal captain admiral',
    'Augustus Willington Shelton Agar': 'Dorsetshire captain VC',
    'B. B. Schofield': 'King George V battleship captain',
    'Benjamin Charles Stanley Martin': 'Dorsetshire captain',
    'D. G. Clark': 'King George V commander',
    'Daniel de Pass': 'Cossack destroyer captain',
    'David Edmund Cole-Hamilton': 'Sikh destroyer',
    'Edward Lyon Berthon': 'Cossack captain',
    'Ernst Lindemann': 'Bismarck captain',
    'Eugeniusz Józef Stanisław Pławski': 'Piorun Polish navy commander',
    'Godfrey Noel Brewer': 'Maori destroyer captain',
    'Graham Henry Stokes': 'Sikh destroyer captain',
    'H. C. Bovell': 'Victorious captain',
    'H. Dalrymple-Smith': 'King George V captain',
    'Hans Meyer': 'Tirpitz captain',
    'Harold Thomas Armstrong': 'Maori destroyer',
    'Harry Robert Graham': 'Zulu destroyer captain',
    'Helmuth Brinkmann': 'Prinz Eugen admiral',
    'Henry Kitson': 'Rodney captain',
    'John Agnew Giffard': 'Sikh destroyer',
    'John Stuart Crawford': 'Zulu destroyer',
    'Karl Topp': 'Tirpitz captain',
    'L. D. Mackintosh': 'Victorious captain',
    'Louis Henry Keppel Hamilton': 'Prince of Wales captain',
    'Michael Maynard Denny': 'Victorious captain',
    'P. J. Mack': 'King George V captain',
    'Philip Louis Vian': 'admiral Cossack',
    'Rafe Edward Courage': 'Maori destroyer',
    'Richard Taylor White': 'Zulu destroyer',
    'Robert St. Vincent Sherbrooke': 'Cossack captain admiral',
    'Robert Weber': 'Tirpitz',
    'St. John Aldrich Micklethwait': 'Sikh destroyer captain',
    'T. E. Halsey': 'King George V captain',
    'W. R. Patterson': 'King George V captain',
    'Wolf Junge': 'Tirpitz captain',
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


def surname(name):
    # 取最后一个词作姓（西式姓名）
    parts = [p for p in re.split(r'[\s\.]+', name) if p]
    return parts[-1] if parts else name


out = {}
for i, (key, p) in enumerate(sorted(people.items()), 1):
    name = p['name']
    hint = HINT.get(name, '')
    q = f'{name} {hint}'.strip()
    d = api({'action': 'query', 'list': 'search',
             'srsearch': f'filetype:bitmap {q}', 'srnamespace': '6', 'srlimit': '8'})
    hits = d.get('query', {}).get('search', [])
    titles = [h['title'] for h in hits]

    # 粗筛：文件名里要有姓，或描述片段里有姓/舰名
    sn = surname(name)
    good = []
    for t in titles:
        tl = t.lower()
        if sn.lower() in tl:
            good.append(t)
    # 有 hint 里的舰名也算
    if not good and hint:
        for t in titles:
            if any(w.lower() in t.lower() for w in hint.split() if len(w) > 4):
                good.append(t)

    out[name] = {'query': q, 'hits': titles[:8], 'picked': good[:3],
                 'has': bool(good)}
    flag = 'YES' if good else '  -'
    print(f'[{flag}] {name}')
    for g in good[:2]:
        print(f'       {g}')
    time.sleep(1.6)

io.open('work/cmdr_photos.json', 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=2))

n = sum(1 for v in out.values() if v['has'])
print()
print(f'有照片候选：{n} / {len(out)}')
print(f'无照片：{len(out) - n}')
for k, v in out.items():
    if not v['has']:
        print(f'  - {k}')
