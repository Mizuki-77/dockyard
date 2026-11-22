# 抓 10 艘新舰的图片候选（只抓元数据，不下载图）。
#
# 分类正名已由 find_new_cats.py 查实（2026-11-22）。规律与 docs/45 记的
# 「HMS <名> (ship, <下水年>)」不同 —— 这批英国舰在 Commons 上用的是
# **舷号**形式：HMS Cossack (F03)、HMS Sheffield (C24)、HMS Ark Royal (91)。
# 只有波兰舰沿用 (ship, 1940)。已更新 docs/45。
import io
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / 'work' / 'shipimg'
WORK.mkdir(parents=True, exist_ok=True)
UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'
API = 'https://commons.wikimedia.org/w/api.php'

CATS = {
    'ark-royal': 'HMS Ark Royal (91)',
    'victorious': 'HMS Victorious (R38)',
    'norfolk': 'HMS Norfolk (78)',
    'dorsetshire': 'HMS Dorsetshire (40)',
    'sheffield': 'HMS Sheffield (C24)',
    'cossack': 'HMS Cossack (F03)',
    'maori': 'HMS Maori (F24)',
    'zulu': 'HMS Zulu (F18)',
    'sikh': 'HMS Sikh (F82)',
    'piorun': 'ORP Piorun (ship, 1940)',
}


def api(params, retries=8):
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
                w = 20 + a * 20
                print(f'      429 wait {w}s')
                time.sleep(w)
                continue
            print(f'      HTTP {e.code}')
            raise
        except Exception:
            if a == retries - 1:
                return {}
            time.sleep(10)
    return {}


def clean(s):
    return ' '.join(re.sub(r'<[^>]+>', '', str(s or '')).split())


def cat_files(cat, limit=200):
    out = []
    cont = {}
    while len(out) < limit:
        p = {'action': 'query', 'list': 'categorymembers', 'cmtitle': 'Category:' + cat,
             'cmtype': 'file', 'cmlimit': '50'}
        p.update(cont)
        d = api(p)
        out += [m['title'] for m in d.get('query', {}).get('categorymembers', [])]
        if 'continue' in d:
            cont = d['continue']
            time.sleep(3)
        else:
            break
    return out[:limit]


def imageinfo(titles):
    res = {}
    for i in range(0, len(titles), 20):
        d = api({'action': 'query', 'titles': '|'.join(titles[i:i + 20]),
                 'prop': 'imageinfo',
                 'iiprop': 'url|size|extmetadata|mime', 'iiurlwidth': '1280'})
        res.update(d.get('query', {}).get('pages', {}))
        time.sleep(3)
    return res


# 视频/音频扩展名必须排除（docs/45 的坑之一）
BAD_EXT = ('.ogv', '.webm', '.ogg', '.mp3', '.wav', '.pdf', '.djvu', '.svg', '.tif', '.tiff')

out = {}
for sid, cat in CATS.items():
    print(f'=== {sid} ({cat}) ===')
    files = cat_files(cat)
    files = [f for f in files if not f.lower().endswith(BAD_EXT)]
    print(f'  {len(files)} 个图片文件（已排除视频/PDF/SVG）')
    if not files:
        out[sid] = []
        continue
    meta = imageinfo(files)
    entries = []
    for pid, page in meta.items():
        ii = (page.get('imageinfo') or [{}])[0]
        if not ii.get('url'):
            continue
        if ii.get('mime') not in (None, 'image/jpeg', 'image/png'):
            continue
        em = ii.get('extmetadata') or {}
        entries.append({
            'title': clean(page.get('title')).replace('File:', ''),
            'thumb': ii.get('thumburl'),
            'w': ii.get('width'), 'h': ii.get('height'),
            'mime': ii.get('mime'),
            'license': clean((em.get('LicenseShortName') or {}).get('value')),
            'artist': clean((em.get('Artist') or {}).get('value'))[:180],
            'desc': clean((em.get('ImageDescription') or {}).get('value'))[:300],
            'date': clean((em.get('DateTimeOriginal') or {}).get('value'))[:40],
            'page': ii.get('descriptionurl'),
        })
    entries.sort(key=lambda e: -(e.get('w') or 0))
    out[sid] = entries
    pd = sum(1 for e in entries if 'Public domain' in e['license'] or 'CC0' in e['license'])
    print(f'  取到 {len(entries)} 条，PD/CC0 {pd}')
    time.sleep(4)

path = WORK / 'candidates_new10.json'
io.open(path, 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=2))
print(f'\n已写 {path}')
print('各组候选数：')
for sid, es in out.items():
    print(f'  {sid:<16} {len(es)}')
