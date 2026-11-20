# 为缺图的 12 型武器按 Commons 分类抓图。
#
# 三条硬规矩（交接报告 §7.4）：
#  1. **绝对不用关键词搜索**，必须按 Category: 浏览 —— 关键词会抓到图书馆封面、
#     1904 年报纸、现代空军合影（上一轮踩过三次）。
#  2. 每张之间 sleep 2-3 秒；遇 429 等 10-20 秒重试。一次抓 10 张以上几乎必被限流。
#  3. thumbnail 宽度只允许 120/250/330/500/960/1280/1920/3840。本站习惯 1280。
#
# 只做「列候选 + 元数据」，不下载。看完候选再决定下哪些。

import io
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / 'work' / 'weaponimg'

UA = 'DockyardArchive/1.0 (historical research; contact via github.com/Mizuki-77/dockyard)'
API = 'https://commons.wikimedia.org/w/api.php'

# 12 型 -> 候选 Commons 分类（按分类浏览，不用搜索）
#
# 分类名是 2026-11-20 用 work/find_cats.py 在 Category 命名空间里实测确认的，
# 不是猜的。上一轮猜的名字（Category:Type 96 25 mm AT/AA gun 等）全部 0 结果。
CATEGORIES = {
    'a6m2': [
        'Category:Mitsubishi A6M Zero',
    ],
    'd3a1': [
        'Category:Aichi D3A',
    ],
    'b5n2': [
        'Category:Nakajima B5N',
    ],
    '25mm-96': [
        'Category:Type 96 25 mm machine gun',
        'Category:Type 96 25mm AA Gun',
    ],
    '20cm-3ns': [
        'Category:20 cm/50 3rd Year Type naval gun',
    ],
    # 12 cm 十年式没有独立 Commons 分类（实测搜不到）。
    # 退回它的独占装备舰赤城的分类，从舰上找该炮的照片 —— 这样找到的图
    # 不是「炮的特写」，而是「炮在舰上的状态」，对模型制作者其实更有用，
    # 但登记时必须如实标 part/view，不能冒充特写。
    '12cm-10ns': [
        'Category:Akagi (ship, 1927)',
    ],
    '127cm-89': [
        'Category:Type 89 12.7cm AA Gun',
    ],
    '5in38-mk12': [
        'Category:5"/38 caliber gun',
    ],
    '11in75-mk1': [
        'Category:1.1"/75 caliber gun',
        'Category:1.1 inch/75 caliber gun',
        'Category:1.1"/75 (28 mm) Mark 1',
    ],
    'f4f-wildcat': [
        'Category:Grumman F4F Wildcat',
    ],
    'sbd-dauntless': [
        'Category:Douglas SBD Dauntless',
    ],
    'tbd-devastator': [
        'Category:Douglas TBD Devastator',
    ],
}


def api(params):
    params = dict(params)
    params['format'] = 'json'
    url = API + '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = 10 + attempt * 5
                print(f'    429，等 {wait}s 重试…')
                time.sleep(wait)
                continue
            raise
        except Exception as e:
            if attempt == 3:
                raise
            print(f'    出错 {e}，重试…')
            time.sleep(3)


def list_category(cat, limit=60):
    """列分类下的文件。"""
    out = []
    cont = {}
    while True:
        p = {
            'action': 'query',
            'list': 'categorymembers',
            'cmtitle': cat,
            'cmtype': 'file',
            'cmlimit': '50',
        }
        p.update(cont)
        d = api(p)
        members = d.get('query', {}).get('categorymembers', [])
        out += [m['title'] for m in members]
        if 'continue' in d and len(out) < limit:
            cont = d['continue']
            time.sleep(2)
        else:
            break
    return out[:limit]


def imageinfo(titles):
    """批量取图片元数据（含缩略图 URL、尺寸、许可）。"""
    if not titles:
        return {}
    d = api({
        'action': 'query',
        'titles': '|'.join(titles[:20]),
        'prop': 'imageinfo',
        'iiprop': 'url|size|extmetadata|mime',
        'iiurlwidth': '1280',
    })
    return d.get('query', {}).get('pages', {})


def main():
    WORK.mkdir(parents=True, exist_ok=True)
    result = {}

    only = sys.argv[1] if len(sys.argv) > 1 else None

    for wid, cats in CATEGORIES.items():
        if only and wid != only:
            continue
        print(f'\n=== {wid} ===')
        found = []
        for cat in cats:
            try:
                files = list_category(cat)
            except Exception as e:
                print(f'  {cat}: 失败 {e}')
                continue
            print(f'  {cat}: {len(files)} 个文件')
            if files:
                found = files
                break
            time.sleep(2)

        if not found:
            print('  ✗ 没找到分类，需要换分类名')
            result[wid] = {'ok': False, 'cats_tried': cats}
            continue

        # 分批取元数据
        meta = {}
        for i in range(0, len(found), 20):
            batch = found[i:i + 20]
            try:
                meta.update(imageinfo(batch))
            except Exception as e:
                print(f'    元数据失败 {e}')
            time.sleep(3)

        entries = []
        for pid, page in meta.items():
            ii = (page.get('imageinfo') or [{}])[0]
            em = ii.get('extmetadata') or {}

            def g(k):
                return (em.get(k) or {}).get('value', '')

            entries.append({
                'title': page.get('title'),
                'thumb': ii.get('thumburl'),
                'full': ii.get('url'),
                'w': ii.get('width'),
                'h': ii.get('height'),
                'mime': ii.get('mime'),
                'license': g('LicenseShortName'),
                'artist': g('Artist'),
                'credit': g('Credit'),
                'desc': g('ImageDescription')[:200],
                'page': ii.get('descriptionurl'),
            })

        entries.sort(key=lambda e: -(e.get('w') or 0))
        result[wid] = {'ok': True, 'entries': entries}
        print(f'  取到 {len(entries)} 条元数据')

    out = WORK / 'candidates.json'
    with io.open(out, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f'\n写入 {out}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
