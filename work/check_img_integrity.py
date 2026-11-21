import io
import re
from collections import Counter

import yaml

d = yaml.safe_load(io.open('data/images.yaml', encoding='utf-8'))
imgs = d['images']

# 检查重复 id
ids = [x['id'] for x in imgs]
dup = [k for k, v in Counter(ids).items() if v > 1]
print(f'总 {len(imgs)} 条，重复 id: {len(dup)}')
for k in dup[:10]:
    print(f'  {k}')

# 检查重复 file
files = [str(x.get('file')) for x in imgs]
dupf = [k for k, v in Counter(files).items() if v > 1]
print(f'重复 file: {len(dupf)}')
for k in dupf[:10]:
    print(f'  {k}')

# 检查指向不存在文件的记录
import os
missing = []
for x in imgs:
    f = str(x.get('file') or '')
    if f.startswith('/img/'):
        p = 'public' + f
        if not os.path.exists(p):
            missing.append(f)
print(f'文件缺失: {len(missing)}')
for m in missing[:10]:
    print(f'  {m}')
