# 最终去重：只在「同一舰内部」按哈希去重，绝不跨舰删
#
# 事故教训（2026-11-25）：上一版跨舰共享哈希去重，
# 把 new-orleans 的 15 张全删了（它们与 atlanta/portland 的合影图哈希相同）。
# 一张合影本来就同时属于多艘舰，删除会让另一艘没图。
# 正确做法：只在单舰内部去重。
import hashlib
import io
import os
import re

import yaml

OUT = 'public/img/ships'
SHIPS = ['tone', 'chikuma', 'haruna', 'kirishima', 'hosho', 'nagara', 'sendai',
         'astoria', 'portland', 'minneapolis', 'new-orleans', 'vincennes',
         'northampton', 'pensacola', 'atlanta', 'hammann', 'monaghan', 'benham']

deleted = []
final = {}

for sid in SHIPS:
    files = sorted(f for f in os.listdir(OUT) if re.match(rf'^{re.escape(sid)}-\d+-', f))
    seen = {}
    keep = []
    for fn in files:
        p = os.path.join(OUT, fn)
        h = hashlib.sha256(open(p, 'rb').read()).hexdigest()
        if h in seen:
            os.remove(p)
            deleted.append((sid, fn, f'同舰内重复于 {seen[h]}'))
            continue
        seen[h] = fn
        keep.append(fn)
    final[sid] = keep

print('单舰内去重完成：')
tot = 0
for sid in SHIPS:
    n = len(final[sid])
    tot += n
    print(f'  {sid:14} {n:>2}' + ('  ← 仍不足 10' if n < 10 else ''))
print(f'  合计 {tot}')

if deleted:
    print(f'\n删除 {len(deleted)}：')
    for sid, fn, why in deleted:
        print(f'  [{sid}] {fn[:56]} — {why}')

with io.open('work/_ship_images_final_list.yaml', 'w', encoding='utf-8', newline='\n') as f:
    yaml.safe_dump({'ships': final}, f, allow_unicode=True, sort_keys=False,
                   default_flow_style=False, indent=2, width=200)
