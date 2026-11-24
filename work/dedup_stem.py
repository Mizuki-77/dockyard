# 补最后一道去重：同舰内「源文件名相同」也算重复（哈希不同可能是不同尺寸）
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
    seen_stem = {}
    keep = []
    for fn in files:
        m = re.match(rf'^{re.escape(sid)}-(\d+)-(.+)$', fn)
        stem = m.group(2) if m else fn
        if stem in seen_stem:
            os.remove(os.path.join(OUT, fn))
            deleted.append((sid, fn, f'同源名重复于 {seen_stem[stem]}'))
            continue
        seen_stem[stem] = fn
        keep.append(fn)
    final[sid] = keep

print('按源文件名去重后：')
tot = 0
for sid in SHIPS:
    n = len(final[sid])
    tot += n
    print(f'  {sid:14} {n:>2}' + ('  ← 不足 10' if n < 10 else ''))
print(f'  合计 {tot}')

if deleted:
    print(f'\n删除 {len(deleted)}：')
    for sid, fn, why in deleted:
        print(f'  [{sid}] {fn[:58]}')
