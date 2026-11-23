# 用 API 重新取每个人的正确 portrait 缩略图 URL，再下载。
#
# 上一版失败原因：cmdr13_data.json 里的 image 字段是 pageimages 的
# thumbnail（本身就是 upload.wikimedia.org 的直链），我按「commons/1/ab/Name」
# 的规则硬改成 thumb 路径 —— 但那些图可能不在 commons 下，或者文件名里
# 有 pageimages 特有的变形，改出来的路径不合法 → HTTP 400。
#
# 正确做法：重新问 API 要 iiurlwidth 的 thumburl（它会给出完整的 /thumb/ 路径），
# 只剥查询串。
import io
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'public' / 'img' / 'commanders'
OUT.mkdir(parents=True, exist_ok=True)

UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'
COMMONS = 'https://commons.wikimedia.org/w/api.php'

data = json.load(io.open(ROOT / 'work' / 'cmdr13_data.json', encoding='utf-8'))


def api(params, retries=5):
    params = dict(params)
    params['format'] = 'json'
    url = COMMONS + '?' + urllib.parse.urlencode(params)
    for a in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=45) as r:
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


def fetch(url, retries=5):
    for a in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(12 + a * 12)
                continue
            print(f'      HTTP {e.code} {url[:70]}')
            if a == retries - 1:
                return None
            time.sleep(6)
        except Exception:
            if a == retries - 1:
                return None
            time.sleep(6)
    return None


def ext_of(d):
    if d.startswith(b'\xff\xd8'):
        return 'jpg'
    if d.startswith(b'\x89PNG'):
        return 'png'
    if d[:4] == b'RIFF' and d[8:12] == b'WEBP':
        return 'webp'
    return None


def file_title_from_url(u):
    """从 upload 直链里抠出文件名，转成 File: 标题。"""
    name = u.split('?')[0].rsplit('/', 1)[-1]
    name = urllib.parse.unquote(name)
    # pageimages 会给 200px 之类的变形名，去掉前缀再还原
    m = re.match(r'^\d+px-(.+)$', name)
    if m:
        name = m.group(1)
    return 'File:' + name


report = {}
for pid, v in sorted(data.items()):
    img = v.get('image')
    if not img:
        print(f'  -  {pid}: 无照片')
        continue

    title = file_title_from_url(img)
    d = api({'action': 'query', 'titles': title, 'prop': 'imageinfo',
             'iiprop': 'url|size|extmetadata', 'iiurlwidth': '720'})
    pages = d.get('query', {}).get('pages', {})
    ii = None
    for k, pg in pages.items():
        if k != '-1':
            ii = (pg.get('imageinfo') or [{}])[0]
    if not ii or not ii.get('url'):
        print(f'  !  {pid}: API 没给 imageinfo（{title[:50]}）')
        continue

    # 优先用 API 给的 thumburl（带完整 /thumb/ 路径），没有才用原图
    url = (ii.get('thumburl') or ii.get('url') or '').split('?')[0]
    if not url:
        print(f'  !  {pid}: 无 URL')
        continue

    blob = fetch(url)
    if not blob:
        print(f'  !  {pid}: 下载失败')
        continue
    ext = ext_of(blob)
    if not ext:
        print(f'  !  {pid}: 非图片（{len(blob)}B）')
        continue

    fname = f'{pid}.{ext}'
    (OUT / fname).write_bytes(blob)
    em = ii.get('extmetadata') or {}
    lic = re.sub(r'<[^>]+>', '', str((em.get('LicenseShortName') or {}).get('value') or ''))
    artist = re.sub(r'<[^>]+>', '', str((em.get('Artist') or {}).get('value') or ''))
    report[pid] = {
        'file': f'/img/commanders/{fname}',
        'bytes': len(blob),
        'license': lic.strip(),
        'artist': ' '.join(artist.split())[:160],
        'source_url': ii.get('descriptionurl') or v.get('wiki_url'),
        'width': ii.get('width'),
        'height': ii.get('height'),
    }
    print(f'  OK {len(blob)//1024:>4}KB  {fname:<28} {lic.strip()[:24]}')
    time.sleep(2)

io.open(ROOT / 'work' / 'cmdr_portraits.json', 'w', encoding='utf-8').write(
    json.dumps(report, ensure_ascii=False, indent=2))

print()
print(f'成功 {len(report)} 张 / 应有 6 张')
