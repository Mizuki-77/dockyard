import glob
import io
import os
from collections import defaultdict

import yaml

d = yaml.safe_load(io.open('data/images.yaml', encoding='utf-8'))
images = d['images']

# 按 subject 分类统计
by_ship = defaultdict(list)
for im in images:
    s = str(im.get('subject') or '')
    if s.startswith('ship:'):
        by_ship[s[5:]].append(im)

ships = []
for p in sorted(glob.glob('data/ships/*.yaml')):
    if '.bak' in p:
        continue
    ships.append(os.path.basename(p)[:-5])

print(f'{"舰":<18} {"总图":<5} {"涂装":<5} {"部位种类":<8} {"视角种类":<8} {"年代跨度"}')
print('-' * 72)

tot_imgs = 0
tot_camo = 0
for sid in ships:
    ims = by_ship.get(sid, [])
    n = len(ims)
    tot_imgs += n
    # 涂装相关：part 含 hull_side / superstructure，或 note/title 提到 camo/迷彩/涂装
    camo = 0
    for im in ims:
        blob = ' '.join([
            str(im.get('title', {})),
            str(im.get('note') or ''),
            str(im.get('part') or ''),
        ]).lower()
        if any(k in blob for k in ['camo', '迷彩', '涂装', 'disruptive', 'scheme', 'paint']):
            camo += 1
    tot_camo += camo

    parts = sorted({str(i.get('part')) for i in ims if i.get('part')})
    views = sorted({str(i.get('view')) for i in ims if i.get('view')})
    dates = sorted({str(i.get('date'))[:4] for i in ims if i.get('date')})
    span = f'{dates[0]}–{dates[-1]}' if dates else '—'

    print(f'{sid:<18} {n:<5} {camo:<5} {len(parts):<8} {len(views):<8} {span}')

print()
print(f'舰艇图片总计: {tot_imgs}，其中涂装相关: {tot_camo}')
print()

# 部位种类分布
print('=== 全站舰艇图的 part 分布 ===')
pc = defaultdict(int)
for sid, ims in by_ship.items():
    for im in ims:
        pc[str(im.get('part') or '未标')] += 1
for k, v in sorted(pc.items(), key=lambda x: -x[1]):
    print(f'  {k:<24} {v}')

print()
print('=== 全站舰艇图的 view 分布 ===')
vc = defaultdict(int)
for sid, ims in by_ship.items():
    for im in ims:
        vc[str(im.get('view') or '未标')] += 1
for k, v in sorted(vc.items(), key=lambda x: -x[1]):
    print(f'  {k:<24} {v}')
