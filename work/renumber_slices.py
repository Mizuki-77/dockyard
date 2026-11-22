# 切片 code 顺延：在首位插入一片后，把后续 code 全部 +1。
#
# 为什么不用「V0a / V0b」：
#   code 是给页面排序用的（见 Slice 接口），且用户看时间轴时读的是 code。
#   出现两个 V1 比重新编号更糟 —— 排序会不稳定。
#
# 用法：python work/renumber_slices.py data/slices/victorious.yaml
#       python work/renumber_slices.py data/slices/victorious.yaml --dry-run
import io
import re
import sys
from datetime import datetime

import yaml

path = [a for a in sys.argv[1:] if not a.startswith('-')][0]
dry = '--dry-run' in sys.argv

with io.open(path, encoding='utf-8') as f:
    text = f.read()

d = yaml.safe_load(text)
slices = d['slices']
codes = [s['code'] for s in slices]

# 找出重复的 code，按出现顺序保留第一个、后续顺延
seen = set()
mapping = []   # (old_code, new_code, index)
prefix = re.match(r'^([A-Za-z]+)', codes[0]).group(1)

counter = 0
for i, s in enumerate(slices):
    old = s['code']
    new = f'{prefix}{counter}'
    mapping.append((old, new, i, s['from'], s.get('to')))
    counter += 1

print('将重编号为：')
for old, new, i, frm, to in mapping:
    flag = '' if old == new else '  <- 改动'
    print(f'  [{i}] {old:<4} -> {new:<4}  {frm} .. {to}{flag}')

if dry:
    print('\n=== dry-run ===')
    sys.exit(0)

# 文本层面替换，保住注释与排版（yaml.safe_dump 会把注释全冲掉）
lines = text.splitlines(keepends=True)
out = []
idx = -1
for line in lines:
    m = re.match(r'^(\s*)- code: (\S+)\s*$', line)
    if m:
        idx += 1
        if idx < len(mapping):
            out.append(f'{m.group(1)}- code: {mapping[idx][1]}\n')
            continue
    out.append(line)

bak = f'{path}.bak-{datetime.now().strftime("%Y-%m-%d")}'
with io.open(bak, 'w', encoding='utf-8', newline='\n') as f:
    f.write(text)

with io.open(path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(''.join(out))

# 复验
d2 = yaml.safe_load(io.open(path, encoding='utf-8').read())
codes2 = [s['code'] for s in d2['slices']]
print(f'\n复验：{len(codes2)} 片，code 唯一 = {len(set(codes2)) == len(codes2)}')
print('  ' + ' '.join(codes2))
