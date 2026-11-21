# 四型武器的选图与下载。全部人工钉死，不靠自动规则。
import io
import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / 'work' / 'weaponimg2'
OUT = ROOT / 'public' / 'img' / 'weapons'
UA = 'DockyardArchive/1.0 (historical research; github.com/Mizuki-77/dockyard)'

PICK = {
    # 纳尔逊号炮术试射时 16 英寸齐射 —— 完全对题，且是本项目收录的级
    '16in-45-mk1': 'HMS Nelson during gunnery trials.jpg',
    # 罗德尼号的双联 6 英寸炮塔，2325x1772 是这批里最高清的一张
    '6in-50-mk22': 'HMS Rodney 6 inch gun turrets IWM A 95.jpg',
    # 罗德尼号 4.7 英寸高炮实弹射击
    '47in-40-mk8': 'HMS Rodney 4.7-inch AA gun firing 1940 IWM A 85.jpg',
    # 欧根亲王号（Prinz Eugen class 实为 Admiral Hipper 级识别照），
    # 该型没有独立武器分类，只能从舰照取 —— 登记时如实标注
    '20-3cm-sk-c34': 'Lot-2275-66 (26254695173).jpg',
}

META = {
    '16in-45-mk1': {
        'zh': '纳尔逊号 16 英寸主炮齐射',
        'en': 'HMS Nelson firing her 16-inch guns',
        'part': 'turret', 'view': 'three_quarter', 'date': '1920s-1930s',
        'note': '纳尔逊号在炮术试射与演习中齐射 16 英寸主炮。三座三联全前置的形制在这张图上看得最清楚。',
    },
    '6in-50-mk22': {
        'zh': '罗德尼号双联 6 英寸副炮塔',
        'en': 'Twin 6-inch gun turrets of HMS Rodney',
        'part': 'turret', 'view': 'detail', 'date': '1940s',
        'note': '罗德尼号双联 6"/50 Mark XXII 副炮塔，舰员正在给防破片护板擦油。注意这是 Mark XXII，不是巡洋舰用的 Mark XXIII。',
    },
    '47in-40-mk8': {
        'zh': '罗德尼号 4.7 英寸高炮实弹射击',
        'en': '4.7-inch AA gun firing aboard HMS Rodney',
        'part': 'mount', 'view': 'three_quarter', 'date': '1940',
        'note': '罗德尼号 4.7"/40 Mark VIII 高炮实弹射击训练。**该型在 1941-05-27 的最终战里全程未开火** —— 这张图拍的是训练，不是那场战斗。',
    },
    '20-3cm-sk-c34': {
        'zh': '欧根亲王号（20.3 cm 主炮所在的重巡）',
        'en': 'German heavy cruiser Prinz Eugen',
        'part': 'turret', 'view': 'side', 'date': '1940s',
        'note': '欧根亲王号。20.3 cm SK C/34 是希佩尔海军上将级的主炮；该型在 Commons 没有独立的武器分类，只能从舰照中取，**这是舰照而不是炮座特写**。',
    },
}


def clean(s):
    import re
    return ' '.join(re.sub(r'<[^>]+>', '', str(s or '')).split())


def download(url, dest):
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            with io.open(dest, 'wb') as f:
                f.write(data)
            return len(data)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = 15 + attempt * 10
                print(f'    429，等 {wait}s')
                time.sleep(wait)
                continue
            raise
    raise RuntimeError('下载失败')


def main():
    cand = json.load(io.open(WORK / 'candidates.json', encoding='utf-8'))
    OUT.mkdir(parents=True, exist_ok=True)
    picked = {}

    for wid, want in PICK.items():
        print(f'\n=== {wid} ===')
        entry = None
        for e in cand.get(wid, []):
            if clean(e.get('title')).replace('File:', '').strip() == want:
                entry = e
                break
        if not entry:
            print(f'  ✗ 未匹配：{want}')
            continue

        thumb = entry.get('thumb')
        # 用 thumb.wikimedia.org（upload 域会 429，实测过）
        if thumb:
            thumb = thumb.replace('upload.wikimedia.org', 'thumb.wikimedia.org')
        dest = OUT / f'{wid}-primary.jpg'
        try:
            size = download(thumb, dest)
            print(f'  OK {size // 1024} KB -> {dest.name}')
        except Exception as ex:
            print(f'  下载失败 {ex}')
            continue

        try:
            from PIL import Image
            with Image.open(dest) as im:
                rw, rh = im.size
        except Exception:
            rw, rh = entry.get('w'), entry.get('h')

        lic = clean(entry.get('license'))
        picked[wid] = {
            'file': f'/img/weapons/{dest.name}',
            'commons_title': clean(entry.get('title')),
            'page': entry.get('page'),
            'w': rw, 'h': rh,
            'license': lic,
            'tier': 'A' if ('Public domain' in lic or 'CC0' in lic) else 'B',
            'author': clean(entry.get('artist'))[:200],
            'meta': META[wid],
        }
        time.sleep(4)

    io.open(WORK / 'picked.json', 'w', encoding='utf-8').write(
        json.dumps(picked, ensure_ascii=False, indent=2))
    print(f'\n成功 {len(picked)}/4')


if __name__ == '__main__':
    main()
