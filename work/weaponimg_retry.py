# 单独补下 11in75-mk1 的主图（上一轮 429 失败），并核验所有已下载图。

import io
import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / 'work' / 'weaponimg'
OUT = ROOT / 'public' / 'img' / 'weapons'
UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'

TARGET = '28 mm Flak USS Hornet (CV-8) May 1942.jpg'


def main():
    cand = json.load(io.open(WORK / 'candidates.json', encoding='utf-8'))
    picked = json.load(io.open(WORK / 'picked.json', encoding='utf-8'))

    rec = cand['11in75-mk1']
    entry = None
    for e in rec['entries']:
        if e['title'].replace('File:', '').strip() == TARGET:
            entry = e
            break

    if not entry:
        print('找不到目标条目')
        return 1

    thumb = entry.get('thumb')
    print(f'缩略图 URL: {thumb}')
    dest = OUT / '11in75-mk1-primary.jpg'

    # 原图只有 795x609，1280 宽会被放大，改用 960 档
    alt = thumb.replace('/1280px-', '/960px-') if thumb else None
    print(f'候选 URL: {alt}')

    ok = False
    for url in [alt, thumb, entry.get('full')]:
        if not url:
            continue
        for attempt in range(5):
            try:
                req = urllib.request.Request(url, headers={'User-Agent': UA})
                with urllib.request.urlopen(req, timeout=60) as r:
                    data = r.read()
                with io.open(dest, 'wb') as f:
                    f.write(data)
                print(f'成功 {len(data)//1024} KB from {url[-60:]}')
                ok = True
                break
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    wait = 20 + attempt * 10
                    print(f'  429，等 {wait}s')
                    time.sleep(wait)
                    continue
                print(f'  HTTP {e.code}')
                break
            except Exception as ex:
                print(f'  {ex}')
                break
        if ok:
            break
        time.sleep(5)

    if not ok:
        print('仍然失败')
        return 1

    # 读实际尺寸
    try:
        from PIL import Image
        with Image.open(dest) as im:
            w, h = im.size
    except Exception:
        w, h = 0, 0

    picked['11in75-mk1'] = {
        'ok': True,
        'file': '/img/weapons/11in75-mk1-primary.jpg',
        'commons_title': 'File:' + TARGET,
        'page': entry.get('page'),
        'w': w,
        'h': h,
        'license': 'Public domain',
        'tier': 'A',
        'author': '',
        'credit': '',
        'desc': 'A quad 28 mm (1.1"/75 cal) Mk 1 anti-aircraft gun firing on the U.S. aircraft carrier USS Hornet (CV-8) in May 1942.',
        'part_view': None,
    }
    with io.open(WORK / 'picked.json', 'w', encoding='utf-8') as f:
        json.dump(picked, f, ensure_ascii=False, indent=2)
    print(f'记录尺寸 {w}x{h}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
