# 查每艘舰的时间轴切片现在挂的是什么图，以及那张图的 part/view。
import io
import os
import re
import yaml

ROOT = os.getcwd()
d = yaml.safe_load(io.open('data/images.yaml', encoding='utf-8'))
imgs = d['images']

by_ship = {}
for im in imgs:
    s = str(im.get('subject') or '')
    if s.startswith('ship:'):
        by_ship.setdefault(s[5:], []).append(im)

# 局部图的 part/view
LOCAL_PARTS = {'turret', 'superstructure', 'aircraft_handling', 'catapult',
               'bridge', 'propeller', 'detail'}
LOCAL_VIEWS = {'detail'}

print(f'{"舰":<18} {"片数":<5} {"挂局部图":<8} 明细')
print('-' * 78)
total_bad = 0
for sid in sorted(by_ship.keys()):
    sp = f'data/slices/{sid}.yaml'
    if not os.path.exists(sp):
        continue
    sd = yaml.safe_load(io.open(sp, encoding='utf-8')) or {}
    slices = sd.get('slices') or []
    bad = []
    for sl in slices:
        if sl.get('image'):
            continue  # 手工指定，不管
        part = str(sl.get('code'))
        # 无法在 python 里复现 sliceImages 逻辑（那是 TS），这里只统计图池构成
    # 统计该舰图池里有多少局部图
    pool = by_ship[sid]
    n_local = sum(1 for i in pool
                  if str(i.get('part')) in LOCAL_PARTS
                  or str(i.get('view')) in LOCAL_VIEWS)
    total_bad += n_local
    if n_local:
        bad.append(f'{n_local}/{len(pool)} 张是局部图')
    print(f'{sid:<18} {len(slices):<5} {"有风险" if n_local else "OK":<8} {"; ".join(bad)}')

print()
print('=== 全站舰图里的局部图统计 ===')
n_all = len([i for i in imgs if str(i.get('subject', '')).startswith('ship:')])
n_local = len([i for i in imgs
               if str(i.get('subject', '')).startswith('ship:')
               and (str(i.get('part')) in LOCAL_PARTS or str(i.get('view')) in LOCAL_VIEWS)])
print(f'舰图 {n_all} 张，其中局部图 {n_local} 张（{n_local/n_all*100:.0f}%）')
print()
print('=== part 分布 ===')
from collections import Counter
for k, v in Counter(str(i.get('part')) for i in imgs
                    if str(i.get('subject', '')).startswith('ship:')).most_common():
    print(f'  {k:<24} {v}')
print()
print('=== view 分布 ===')
for k, v in Counter(str(i.get('view')) for i in imgs
                    if str(i.get('subject', '')).startswith('ship:')).most_common():
    print(f'  {k:<24} {v}')
