# 为四型新武器按 Commons 分类抓候选元数据。
# 遵守 §7.4 三条硬规矩；分类名先查正名再抓。

import io
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / 'work' / 'weaponimg2'
UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'
API = 'https://commons.wikimedia.org/w/api.php'

TARGETS = {
    '16in-45-mk1': [
        'Category:BL 16 inch Mk I naval gun',
        'Category:16 inch/45 caliber gun',
        'Category:HMS Rodney (29)',
    ],
    '6in-50-mk22': [
        'Category:BL 6 inch Mk XXII naval gun',
        'Category:6 inch/50 caliber gun',
    ],
    '47in-40-mk8': [
        'Category:QF 4.7 inch Mk VIII naval gun',
        'Category:4.7 inch/40 caliber gun',
    ],
    '20-3cm-sk-c34': [
        'Category:20.3 cm SK C/34',
        'Category:20.3 cm naval guns',
        'Category:Admiral Hipper class cruiser',
        'Category:Prinz Eugen (ship, 1938)',
    ],
}


def api(params):
    params = dict(params)
    params['format'] = 'json'
    url = API + '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(12)
                continue
            raise
        except Exception:
            if attempt == 2:
                raise
            time.sleep(3)
    return {}


def search_cat(q):
    d = api({'action': 'query', 'list': 'search', 'srsearch': q,
             'srnamespace': '14', 'srlimit': '5'})
    return [h['title'] for h in d.get('query', {}).get('search', [])]


def cat_files(cat, limit=40):
    d = api({'action': 'query', 'list': 'categorymembers', 'cmtitle': cat,
             'cmtype': 'file', 'cmlimit': '40'})
    return [m['title'] for m in d.get('query', {}).get('categorymembers', [])][:limit]


def imageinfo(titles):
    if not titles:
        return {}
    d = api({'action': 'query', 'titles': '|'.join(titles[:20]),
             'prop': 'imageinfo',
             'iiprop': 'url|size|extmetadata|mime', 'iiurlwidth': '1280'})
    return d.get('query', {}).get('pages', {})


def main():
    WORK.mkdir(parents=True, exist_ok=True)
    result = {}

    print('=== 先查分类正名 ===')
    for wid, cats in TARGETS.items():
        print(f'--- {wid} ---')
        for c in cats:
            files = cat_files(c)
            print(f'  {c}: {len(files)} 文件')
            if files:
                break
            time.sleep(2)
        else:
            # 全失败，搜一下
            print('  全失败，搜正名：')
            key = wid.replace('-', ' ')
            for hit in search_cat(key)[:3]:
                print(f'    候选分类: {hit}')
            continue

        meta = imageinfo(files)
        entries = []
        for pid, page in meta.items():
            ii = (page.get('imageinfo') or [{}])[0]
            em = ii.get('extmetadata') or {}

            def g(k):
                v = (em.get(k) or {}).get('value', '')
                import re
                return ' '.join(re.sub(r'<[^>]+>', '', str(v)).split())

            entries.append({
                'title': page.get('title'),
                'thumb': ii.get('thumburl'),
                'full': ii.get('url'),
                'w': ii.get('width'),
                'h': ii.get('height'),
                'license': g('LicenseShortName'),
                'artist': g('Artist')[:200],
                'desc': g('ImageDescription')[:200],
                'page': ii.get('descriptionurl'),
            })
        entries.sort(key=lambda e: -(e.get('w') or 0))
        result[wid] = entries
        print(f'  取到 {len(entries)} 条')
        time.sleep(3)

    io.open(WORK / 'candidates.json', 'w', encoding='utf-8').write(
        json.dumps(result, ensure_ascii=False, indent=2))
    print(f'\n写入 {WORK / "candidates.json"}')


if __name__ == '__main__':
    main()
