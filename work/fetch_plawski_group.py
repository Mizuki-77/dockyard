# 抓 Pławski 的合影，并用官方描述里的方位做标注。
#
# 官方描述原文：
#   "On board the Polish destroyer ORP Piorun (Thunderbolt), formerly HMS Nerissa,
#    officers off watch get a little warmth and comfort round the wardroom fire ...
#    The Captain, Eugeniusz Pławski, is farthest from the camera, ne[xt to ...]"
# 也就是说他是画面里离镜头最远的那个。这类「合影 + 官方点名方位」
# 正是用户说的「合影也行，标注就好」。
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
UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'
API = 'https://commons.wikimedia.org/w/api.php'

TARGET = 'File:The Polish Navy during the Second World War A2491.jpg'


def api(params, retries=5):
    params = dict(params)
    params['format'] = 'json'
    url = API + '?' + urllib.parse.urlencode(params)
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


def fetch(url, retries=5):
    for a in range(retries):
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': UA,
                'Referer': 'https://commons.wikimedia.org/',
            })
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(20 + a * 15)
                continue
            if a == retries - 1:
                return None
            time.sleep(10)
        except Exception:
            if a == retries - 1:
                return None
            time.sleep(10)
    return None


def clean(s):
    return ' '.join(re.sub(r'<[^>]+>', '', str(s or '')).split())


d = api({'action': 'query', 'titles': TARGET, 'prop': 'imageinfo',
         'iiprop': 'url|size|extmetadata'})
pages = d.get('query', {}).get('pages', {})
ii = None
for k, pg in pages.items():
    if k != '-1':
        ii = (pg.get('imageinfo') or [{}])[0]
if not ii:
    raise SystemExit('取不到 imageinfo')

url = (ii.get('url') or '').split('?')[0]
print('downloading', url[:90])
blob = fetch(url)
if not blob:
    raise SystemExit('下载失败')

im = Image.open(io.BytesIO(blob))
im = im.convert('L') if im.mode in ('1', 'L', 'P', 'RGBA', 'LA') else im.convert('RGB')
w, h = im.size
if max(w, h) > 1200:
    s = 1200 / max(w, h)
    im = im.resize((int(w * s), int(h * s)), Image.LANCZOS)
out = OUT / 'eugeniusz-plawski.jpg'
im.save(out, 'JPEG', quality=90, optimize=True)

em = ii.get('extmetadata') or {}
desc = clean((em.get('ImageDescription') or {}).get('value'))

rep_path = ROOT / 'work' / 'cmdr_portraits.json'
rep = json.load(io.open(rep_path, encoding='utf-8')) if rep_path.exists() else {}
rep['eugeniusz-plawski'] = {
    'file': '/img/commanders/eugeniusz-plawski.jpg',
    'bytes': out.stat().st_size,
    'license': clean((em.get('LicenseShortName') or {}).get('value')),
    'artist': clean((em.get('Artist') or {}).get('value'))[:200],
    'source_url': ii.get('descriptionurl'),
    'commons_file': TARGET.replace('File:', ''),
    'width': im.size[0],
    'height': im.size[1],
    # 合影标注：画面里哪个是他
    'group_shot': True,
    'where_zh': '画面中离镜头最远的那一位（后排、门左侧）',
    'desc_official': desc[:420],
}
io.open(rep_path, 'w', encoding='utf-8').write(
    json.dumps(rep, ensure_ascii=False, indent=2))

print(f'OK {out.stat().st_size//1024}KB {im.size[0]}x{im.size[1]}')
print('官方描述：', desc[:260])
