# 只接受**维基条目主图**（pageimages original），不接受搜索结果兜底。
#
# 为什么收紧（2026-11-23 踩到）：
#   上一版用「搜文件名 → 取第一个结果」兜底，结果抓回两张合影：
#     arthur-power  → 日本投降时的三人合影（他是右边白衣者）
#     louis-hamilton → 国王接见舰队将官的多人合影
#   这类图放在人物页头像是错的 —— 读者看不出哪个是他。
#
# 规矩：**人物页头像必须是「这张图就是给他拍的」**。
#   维基编者挂条目主图时做的就是这个判断，所以只用 pageimages。
#   没有主图的人就诚实显示「暂无照片」。
#
# 另外：Power 和 Hamilton 的原主图（cropped）其实是对的，
# 之前被我自己的「去 cropped」规则排除了 —— cropped 通常正是从合影里
# 裁出来的单人照，恰恰是我们要的。这条规则反了。
from pathlib import Path

import io
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'public' / 'img' / 'commanders'
OUT.mkdir(parents=True, exist_ok=True)
UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'
EN = 'https://en.wikipedia.org/w/api.php'

# 每人对应的维基条目（已核实是本人）
ARTICLE = {
    'philip-vian': 'Philip Vian',
    'ernst-lindemann': 'Ernst Lindemann',
    'arthur-power': 'Arthur Power',
    'eugeniusz-plawski': 'Eugeniusz Pławski',
    'louis-hamilton': 'Louis Keppel Hamilton',
    'michael-denny': 'Michael Denny',
}


def api(params, retries=6):
    params = dict(params)
    params['format'] = 'json'
    url = EN + '?' + urllib.parse.urlencode(params)
    for a in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=50) as r:
                return json.loads(r.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(20 + a * 15)
                continue
            return {}
        except Exception:
            if a == retries - 1:
                return {}
            time.sleep(8)
    return {}


def fetch(url, retries=6):
    for a in range(retries):
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': UA,
                'Referer': 'https://en.wikipedia.org/',
            })
            with urllib.request.urlopen(req, timeout=180) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(25 + a * 20)
                continue
            if a == retries - 1:
                return None
            time.sleep(12)
        except Exception:
            if a == retries - 1:
                return None
            time.sleep(12)
    return None


def clean(s):
    return ' '.join(re.sub(r'<[^>]+>', '', str(s or '')).split())


def save(raw, stem):
    im = Image.open(io.BytesIO(raw))
    if im.mode in ('1', 'L', 'P', 'RGBA', 'LA'):
        im = im.convert('L')
    else:
        im = im.convert('RGB')
    w, h = im.size
    if max(w, h) > 1200:
        s = 1200 / max(w, h)
        im = im.resize((int(w * s), int(h * s)), Image.LANCZOS)
    out = OUT / f'{stem}.jpg'
    im.save(out, 'JPEG', quality=88, optimize=True)
    return out, im.size


report = {}
for pid, art in ARTICLE.items():
    print(f'=== {pid} ({art}) ===')
    d = api({'action': 'query', 'titles': art,
             'prop': 'pageimages', 'piprop': 'original|name'})
    pages = d.get('query', {}).get('pages', {})
    orig, fname = None, None
    for k, pg in pages.items():
        if k == '-1':
            continue
        orig = pg.get('original', {}).get('source')
        fname = pg.get('pageimage')
    if not orig:
        print('   条目没有主图')
        continue

    blob = fetch(orig.split('?')[0])
    if not blob:
        # 原图挂了退回 Commons 的 720 缩略图
        if fname:
            alt = (f'https://commons.wikimedia.org/w/index.php?title='
                   f'Special:Redirect/file/{urllib.parse.quote(fname)}&width=900')
            blob = fetch(alt)
    if not blob:
        print('   下载失败')
        continue

    try:
        out, size = save(blob, pid)
    except Exception as e:
        print(f'   转码失败 {e}')
        continue

    # 取该文件的许可信息
    lic, artist, durl = '', '', ''
    if fname:
        d2 = api({'action': 'query', 'titles': f'File:{fname}',
                  'prop': 'imageinfo', 'iiprop': 'extmetadata|url'})
        for k, pg in d2.get('query', {}).get('pages', {}).items():
            if k == '-1':
                continue
            ii = (pg.get('imageinfo') or [{}])[0]
            em = ii.get('extmetadata') or {}
            lic = clean((em.get('LicenseShortName') or {}).get('value'))
            artist = clean((em.get('Artist') or {}).get('value'))[:200]
            durl = ii.get('descriptionurl') or ''

    report[pid] = {
        'file': f'/img/commanders/{pid}.jpg',
        'bytes': out.stat().st_size,
        'license': lic,
        'artist': artist,
        'source_url': durl,
        'commons_file': fname,
        'width': size[0],
        'height': size[1],
    }
    print(f'   OK {out.stat().st_size//1024}KB {size[0]}x{size[1]}  {lic[:24]}')
    time.sleep(3)

io.open(ROOT / 'work' / 'cmdr_portraits.json', 'w', encoding='utf-8').write(
    json.dumps(report, ensure_ascii=False, indent=2))

print()
print('=== 最终 ===')
for k in sorted(report):
    v = report[k]
    print(f'  {k:<22} {v["width"]}x{v["height"]:<5} {v["license"][:24]}')
