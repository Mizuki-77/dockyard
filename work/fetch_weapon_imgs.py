# 抓 8 型武器图并登记。
#
# 45in-45-mk1 与 47in-45-mk12 在 Commons 上没有独立分类（试了三种命名都为空），
# 这两型就**不放图**，页面显示「暂无影像」。
# 用户本轮明确说了「尽力而为，不强求多图」，所以不为它们凑图。
#
# 每型只取 1-2 张：武器页的图是「让人认出这门炮长什么样」，
# 不需要图集（舰的图集才是重点）。
import io
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'img_weapon_tmp'
OUT = ROOT / 'public' / 'img' / 'weapons'
OUT.mkdir(parents=True, exist_ok=True)

UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'
API = 'https://commons.wikimedia.org/w/api.php'

CATS = {
    '8in-50-mk8': 'BL 8 inch Mk VIII naval gun',
    '6in-50-mk23': 'BL 6 inch Mk XXIII naval gun',
    '4in-45-mk16': 'QF 4 inch Mk XVI naval gun',
    'vickers-50': 'Vickers .50 machine gun',
    '3pdr-hotchkiss': 'QF 3 pounder Hotchkiss',
    'skua': 'Blackburn Skua',
    'roc': 'Blackburn Roc',
    'albacore': 'Fairey Albacore',
}

# 每型想要的张数（武器图少而精）
WANT = {w: 2 for w in CATS}
WANT['roc'] = 1          # 只有 8 张候选，留 1 张
WANT['vickers-50'] = 1

BAD_EXT = ('.ogv', '.webm', '.ogg', '.mp3', '.wav', '.pdf', '.djvu', '.svg', '.tif', '.tiff')


def api(params, retries=6):
    params = dict(params)
    params['format'] = 'json'
    url = API + '?' + urllib.parse.urlencode(params)
    for a in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=45) as r:
                return json.loads(r.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(20 + a * 15)
                continue
            return {'_err': str(e)}
        except Exception:
            if a == retries - 1:
                return {}
            time.sleep(8)
    return {}


def clean(s):
    return ' '.join(re.sub(r'<[^>]+>', '', str(s or '')).split())


def to_thumb(url, width=960):
    u = (url or '').split('?')[0]
    if not u:
        return None
    if '//thumb.wikimedia.org/' in u:
        return u
    m = re.match(
        r'^https://upload\.wikimedia\.org/wikipedia/commons/'
        r'([0-9a-f])/([0-9a-f]{2})/([^/]+)$', u)
    if not m:
        return u
    a, b, name = m.group(1), m.group(2), m.group(3)
    return (f'https://thumb.wikimedia.org/wikipedia/commons/thumb/'
            f'{a}/{b}/{name}/{width}px-{name}')


def fetch(url, retries=6):
    for a in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(10 + a * 10)
                continue
            if a == retries - 1:
                return None
            time.sleep(6)
        except Exception:
            if a == retries - 1:
                return None
            time.sleep(6)
    return None


def img_ext(d):
    if d.startswith(b'\xff\xd8'):
        return 'jpg'
    if d.startswith(b'\x89PNG'):
        return 'png'
    if d[:4] == b'RIFF' and d[8:12] == b'WEBP':
        return 'webp'
    return None


def safe(s):
    s = re.sub(r'[^a-zA-Z0-9._-]+', '-', s)
    return re.sub(r'-+', '-', s).strip('-').lower()


report = {}
for wid, cat in CATS.items():
    print(f'=== {wid} ({cat}) ===')
    d = api({'action': 'query', 'list': 'categorymembers',
             'cmtitle': 'Category:' + cat, 'cmtype': 'file', 'cmlimit': '60'})
    files = [m['title'] for m in d.get('query', {}).get('categorymembers', [])]
    files = [f for f in files if not f.lower().endswith(BAD_EXT)]
    print(f'  {len(files)} 个候选')
    if not files:
        report[wid] = []
        continue

    meta = api({'action': 'query', 'titles': '|'.join(files[:40]),
                'prop': 'imageinfo',
                'iiprop': 'url|size|extmetadata|mime', 'iiurlwidth': '960'})
    pages = meta.get('query', {}).get('pages', {})

    # 优先 PD/CC0、优先大图
    cands = []
    for pid, page in pages.items():
        ii = (page.get('imageinfo') or [{}])[0]
        if not ii.get('url'):
            continue
        if ii.get('mime') not in (None, 'image/jpeg', 'image/png'):
            continue
        em = ii.get('extmetadata') or {}
        lic = clean((em.get('LicenseShortName') or {}).get('value'))
        pd = ('Public domain' in lic) or ('CC0' in lic)
        cands.append({
            'title': clean(page.get('title')).replace('File:', ''),
            'thumb': ii.get('thumburl'),
            'w': ii.get('width'), 'h': ii.get('height'),
            'license_raw': lic, 'pd': pd,
            'artist': clean((em.get('Artist') or {}).get('value'))[:160],
            'desc': clean((em.get('ImageDescription') or {}).get('value'))[:200],
            'date': clean((em.get('DateTimeOriginal') or {}).get('value'))[:30],
            'page': ii.get('descriptionurl'),
        })
    cands.sort(key=lambda e: (not e['pd'], -(e['w'] or 0)))

    rows = []
    for c in cands:
        if len(rows) >= WANT[wid]:
            break
        url = to_thumb(c['thumb'])
        data = fetch(url)
        if not data:
            continue
        ext = img_ext(data)
        if not ext:
            print(f'    非图片丢弃 {c["title"][:40]}')
            continue
        base = safe(c['title'].rsplit('.', 1)[0])[:46]
        fname = f'{wid}-{len(rows)+1:02d}-{base}.{ext}'
        (OUT / fname).write_bytes(data)
        rows.append({**c, 'file': f'/img/weapons/{fname}'})
        print(f'    OK {len(data)//1024:>4}KB  {fname[:56]}')
        time.sleep(1.5)

    report[wid] = rows
    if not rows:
        print('    没抓到可用图')
    time.sleep(2)

io.open(ROOT / 'work' / 'weapimg' / 'weapon_picks.json', 'w', encoding='utf-8').write(
    json.dumps(report, ensure_ascii=False, indent=2)) if (ROOT / 'work' / 'weapimg').exists() else None
Path(ROOT / 'work' / 'weapimg').mkdir(parents=True, exist_ok=True)
io.open(ROOT / 'work' / 'weapimg' / 'weapon_picks.json', 'w', encoding='utf-8').write(
    json.dumps(report, ensure_ascii=False, indent=2))

print()
print('=== 汇总 ===')
for wid, rows in report.items():
    print(f'  {wid:<16} {len(rows)} 张')
print(f'总计 {sum(len(v) for v in report.values())} 张')
