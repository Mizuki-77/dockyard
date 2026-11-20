# 从候选里按规则选一张主图，下载 1280 宽缩略图，输出 images.yaml 片段。
#
# 选图不能只看尺寸 —— 上一轮踩过的坑必须写进代码里：
#  · a6m2 分类里有 AT-6 改装的**复制品**（desc 里写 replica / AT-6）
#  · 25mm-96 与 127cm-89 分类里混进了**昭和天皇照片**（島村信政5.jpg）
#  · 要避开 wreck（残骸）、burning（燃烧）、modern memorial（现代纪念碑）
#
# 所以：先用黑名单把垃圾剔掉，再按「本项目相关舰 + tier + 尺寸」排序。

import io
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / 'work' / 'weaponimg'
OUT = ROOT / 'public' / 'img' / 'weapons'
UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'

# 标题/描述里出现这些词就排除
BAD = [
    'replica', 'reproduction', 'AT-6', 'Texan', 'model kit', 'scale model',
    'wreck', 'wreckage', 'burning', 'fire', 'damaged', 'salvage',
    'Hirohito', 'Emperor', '島村', 'portrait', 'ceremony', 'memorial day',
    'wikipedia', 'logo', 'map', 'chart', 'diagram',
]

# 本项目收录的舰名（出现在标题/描述里说明是实战期照片，优先）
SHIPS = [
    'akagi', 'kaga', 'soryu', 'hiryu', 'enterprise', 'yorktown', 'hornet',
    'bismarck', 'tirpitz', 'hood', 'illustrious', 'king george',
]

# 每型手工指定首选：看完候选清单后钉死，避免自动规则选错。
# 值为 Commons 文件标题（不含 File: 前缀）。
PICK = {
    # 珍珠港当天零战起飞瞬间，PD。不用 Fujikawa Maru（那是沉在特鲁克泻湖的残骸）
    # 也不用 AT-6 改装的复制品（分类里有 3 张，desc 明写 replica）。
    'a6m2': '80-G-182252 (23758329140).jpg',
    'd3a1': 'Japanese planes preparing-Pearl Harbor.jpg',
    'b5n2': 'Nakajima B5N2 green.jpg',
    # 硫磺岛双联 25mm 阵地，PD。分类里混着昭和天皇照片，必须钉死。
    '25mm-96': '127-GW-304-143496 (24979023882).jpg',
    '20cm-3ns': '203-mm turret on Takao.jpg',
    # 赤城号上双联 12cm 炮组 —— 完全对题，且是本项目收录的舰。
    # 这张是「炮在舰上的使用状态」而不是炮座特写，登记时 part/view 已按实际标注。
    '12cm-10ns': 'Akagi AA gun position.jpg',
    '127cm-89': 'Type89 12.7cm AA GUN01.jpg',
    '5in38-mk12': '127mm guns aboard USS Enterprise (CV-6) during gunnery practice, 4 March 1942 (80-G-16954).jpg',
    # 大黄蜂号上正在射击的四联 1.1"，正好是本项目的舰。
    # 但原图只有 795x609，是全项目最小的主图 —— 已在 note 里注明。
    '11in75-mk1': '28 mm Flak USS Hornet (CV-8) May 1942.jpg',
    'f4f-wildcat': 'F4F VF-6 taking off from USS Enterprise (CV-6) 1942.jpg',
    'sbd-dauntless': 'Aircraft are armed on USS Enterprise (CV-6) in early 1942.jpg',
    'tbd-devastator': 'Douglas TBD-1 Devastators of VT-6 in flight, circa in 1939 (NH 77104).jpg',
}

# 12cm-10ns 只有赤城舰照可用，必须如实标注 part/view
PART_OVERRIDE = {
    '12cm-10ns': ('mount', 'deck'),
}


def clean(html):
    s = re.sub(r'<[^>]+>', '', str(html or ''))
    s = s.replace('&amp;', '&').replace('&quot;', '"').replace('&#039;', "'")
    return ' '.join(s.split())


def bad(entry):
    text = (clean(entry.get('title')) + ' ' + clean(entry.get('desc'))).lower()
    for w in BAD:
        if w.lower() in text:
            return w
    return None


def score(entry):
    text = (clean(entry.get('title')) + ' ' + clean(entry.get('desc'))).lower()
    lic = clean(entry.get('license'))
    s = 0
    if 'Public domain' in lic:
        s += 100
    elif 'CC0' in lic:
        s += 95
    elif lic.startswith('CC'):
        s += 50
    for sh in SHIPS:
        if sh in text:
            s += 30
            break
    w = entry.get('w') or 0
    if w >= 2000:
        s += 20
    elif w >= 1200:
        s += 15
    elif w >= 800:
        s += 8
    return s


def download(url, dest):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            with io.open(dest, 'wb') as f:
                f.write(data)
            return len(data)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = 10 + attempt * 5
                print(f'    429，等 {wait}s')
                time.sleep(wait)
                continue
            raise
    raise RuntimeError('下载失败')


def main():
    cand = json.load(io.open(WORK / 'candidates.json', encoding='utf-8'))
    OUT.mkdir(parents=True, exist_ok=True)

    result = {}
    for wid, rec in cand.items():
        print(f'\n=== {wid} ===')
        if not rec.get('ok'):
            print('  无候选，跳过')
            result[wid] = {'ok': False}
            continue

        entries = rec['entries']
        pinned = PICK.get(wid)

        chosen = None
        if pinned:
            for e in entries:
                if clean(e.get('title')).replace('File:', '').strip() == pinned:
                    chosen = e
                    break
            if not chosen:
                print(f'  ⚠ 钉死的标题未匹配：{pinned}')
                print(f'     候选里有相近的：{[clean(x.get("title"))[:60] for x in entries[:3]]}')

        if not chosen:
            pool = [e for e in entries if not bad(e)]
            if not pool:
                print('  全部被黑名单滤掉')
                result[wid] = {'ok': False}
                continue
            pool.sort(key=score, reverse=True)
            chosen = pool[0]
            print(f'  自动选：{clean(chosen.get("title"))[:70]}')

        why = bad(chosen)
        if why:
            print(f'  ⚠ 选中的含黑名单词「{why}」，仍按钉死处理')

        thumb = chosen.get('thumb')
        if not thumb:
            print('  无缩略图 URL')
            result[wid] = {'ok': False}
            continue

        dest = OUT / f'{wid}-primary.jpg'
        try:
            size = download(thumb, dest)
            print(f'  下载 {size // 1024} KB → {dest.name}')
        except Exception as ex:
            print(f'  下载失败 {ex}')
            result[wid] = {'ok': False}
            continue

        lic = clean(chosen.get('license'))
        tier = 'A' if ('Public domain' in lic or 'CC0' in lic) else 'B'

        # 取实际下载图的尺寸
        try:
            from PIL import Image
            with Image.open(dest) as im:
                real_w, real_h = im.size
        except Exception:
            real_w, real_h = 1280, 0

        result[wid] = {
            'ok': True,
            'file': f'/img/weapons/{dest.name}',
            'commons_title': clean(chosen.get('title')),
            'page': chosen.get('page'),
            'w': real_w,
            'h': real_h,
            'license': lic,
            'tier': tier,
            'author': clean(chosen.get('artist'))[:300],
            'credit': clean(chosen.get('credit'))[:200],
            'desc': clean(chosen.get('desc'))[:300],
            'part_view': PART_OVERRIDE.get(wid),
        }
        time.sleep(3)

    with io.open(WORK / 'picked.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f'\n写入 {WORK / "picked.json"}')

    ok = sum(1 for v in result.values() if v.get('ok'))
    print(f'成功 {ok}/{len(result)}')


if __name__ == '__main__':
    raise SystemExit(main())
