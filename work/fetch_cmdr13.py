# 精确取 13 位入选者的完整资料：生卒、军衔、维基条目、照片、任历。
import io
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request

UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'
EN = 'https://en.wikipedia.org/w/api.php'

# 13 位入选者：有真实条目、能写出实质内容
CHOSEN = {
    'arthur-power': 'Arthur Power',
    'augustus-agar': 'Augustus Agar',
    'benjamin-martin': 'Benjamin Martin (Royal Navy officer)',
    'ernst-lindemann': 'Ernst Lindemann',
    'eugeniusz-plawski': 'Eugeniusz Pławski',
    'helmuth-brinkmann': 'Helmuth Brinkmann',
    'karl-topp': 'Karl Topp',
    'louis-hamilton': 'Louis Keppel Hamilton',
    'michael-denny': 'Michael Denny',
    'philip-vian': 'Philip Vian',
    'robert-sherbrooke': 'Robert Sherbrooke',
    'wolf-junge': 'Wolf Junge',
    'richard-taylor-white': 'Richard Taylor White',
}


def api(params, retries=5):
    params = dict(params)
    params['format'] = 'json'
    url = EN + '?' + urllib.parse.urlencode(params)
    for a in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=45) as r:
                return json.loads(r.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(15 + a * 12)
                continue
            print(f'    HTTP {e.code}')
            return {}
        except Exception:
            if a == retries - 1:
                return {}
            time.sleep(6)
    return {}


def clean(s):
    return ' '.join(re.sub(r'<[^>]+>', '', str(s or '')).split())


out = {}
for pid, title in CHOSEN.items():
    d = api({'action': 'query', 'titles': title,
             'prop': 'pageimages|extracts|description|info',
             'piprop': 'original|thumbnail', 'pithumbsize': '900',
             'exintro': 1, 'explaintext': 1, 'inprop': 'url'})
    pages = d.get('query', {}).get('pages', {})
    pg = None
    for k, v in pages.items():
        if k != '-1':
            pg = v
    if not pg:
        print(f'! {pid}: 取不到 {title}')
        continue

    # 全文：单独再取一次正文（用于写传记时核对事实）
    dfull = api({'action': 'query', 'titles': title, 'prop': 'extracts',
                 'explaintext': 1})
    fpages = dfull.get('query', {}).get('pages', {})
    full = ''
    for k, v in fpages.items():
        full = clean(v.get('extract'))[:9000]

    out[pid] = {
        'person': pg.get('title'),
        'desc': pg.get('description'),
        'image': pg.get('thumbnail', {}).get('source'),
        'original': pg.get('original', {}).get('source'),
        'intro': clean(pg.get('extract'))[:700],
        'full': full,
        'wiki_url': (pg.get('fullurl') or ''),
    }
    flag = 'IMG' if out[pid]['image'] else '   '
    print(f'{flag} {pid:<22} {pg.get("title")}')
    print(f'    {pg.get("description") or ""}')
    time.sleep(1.5)

io.open('work/cmdr13_data.json', 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=2))

print()
print(f'取到 {len(out)} / 13')
print(f'有照片 {sum(1 for v in out.values() if v["image"])}')
