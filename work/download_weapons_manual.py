# 按 pick_weapons.py 的手工清单精确下载武器图。
#
# 与自动版的区别：先按文件名精确查 imageinfo，再只下那几张。
# 文件名里有特殊字符（括号、逗号、空格），必须 URL 编码正确。
import io
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, 'work')
from pick_weapons import CATS  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'public' / 'img' / 'weapons'
OUT.mkdir(parents=True, exist_ok=True)

UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'
API = 'https://commons.wikimedia.org/w/api.php'


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
for wid, spec in CATS.items():
    print(f'=== {wid} ===')
    rows = []
    titles = ['File:' + t for (t, _p, _v, _n) in spec['picks']]
    d = api({'action': 'query', 'titles': '|'.join(titles),
             'prop': 'imageinfo',
             'iiprop': 'url|size|extmetadata|mime', 'iiurlwidth': '960'})
    pages = d.get('query', {}).get('pages', {})
    by_title = {}
    for pid, page in pages.items():
        by_title[clean(page.get('title'))] = page

    for n, (title, part, view, note) in enumerate(spec['picks'], 1):
        page = by_title.get('File:' + title)
        if not page:
            # 标题可能被规范化（下划线/空格），宽松匹配一次
            for k, v in by_title.items():
                if k.replace('_', ' ').lower() == ('File:' + title).replace('_', ' ').lower():
                    page = v
                    break
        if not page or not (page.get('imageinfo') or [{}])[0].get('url'):
            print(f'  [{n}] 找不到 {title[:50]}')
            continue

        ii = page['imageinfo'][0]
        em = ii.get('extmetadata') or {}
        lic = clean((em.get('LicenseShortName') or {}).get('value'))
        pd = ('Public domain' in lic) or ('CC0' in lic)
        if 'CC BY' in lic and not pd:
            tier, lic_key = 'B', ('cc_by_sa' if 'CC BY-SA' in lic else 'cc_by')
        elif pd:
            tier, lic_key = 'A', ('pd' if 'Public domain' in lic else 'cc0')
        else:
            print(f'  [{n}] 授权 {lic!r} 不可用，跳过')
            continue

        url = to_thumb(ii.get('thumburl'))
        data = fetch(url)
        if not data:
            print(f'  [{n}] 下载失败')
            continue
        ext = img_ext(data)
        if not ext:
            print(f'  [{n}] 非图片')
            continue

        base = safe(title.rsplit('.', 1)[0])[:46]
        fname = f'{wid}-{n:02d}-{base}.{ext}'
        (OUT / fname).write_bytes(data)
        rows.append({
            'file': f'/img/weapons/{fname}',
            'title': title,
            'part': part, 'view': view, 'note': note,
            'license': lic_key, 'tier': tier, 'license_raw': lic,
            'artist': clean((em.get('Artist') or {}).get('value'))[:160],
            'page': ii.get('descriptionurl'),
            'w': ii.get('width'), 'h': ii.get('height'),
        })
        print(f'  [{n}] OK {len(data)//1024:>4}KB  {fname[:54]}')
        time.sleep(1.5)

    report[wid] = rows
    time.sleep(2)

Path(ROOT / 'work' / 'weapimg').mkdir(parents=True, exist_ok=True)
io.open(ROOT / 'work' / 'weapimg' / 'weapon_picks.json', 'w', encoding='utf-8').write(
    json.dumps(report, ensure_ascii=False, indent=2))

print()
print('=== 汇总 ===')
for wid, rows in report.items():
    print(f'  {wid:<16} {len(rows)} 张')
print(f'总计 {sum(len(v) for v in report.values())} 张')
