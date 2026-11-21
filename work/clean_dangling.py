# 清理 images.yaml 里指向不存在文件的记录。
# 注意：tirpitz-1942-faettenfjord-aerial 是**原本就缺的**（不是我删的），
# 这一条要单独看 —— 它可能是历史遗留问题，需要报告而不是静默删除。
import io
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / 'data' / 'images.yaml'

text = io.open(IMG, encoding='utf-8').read()

# 找出所有 block：从 "  - id:" 到下一个 "  - id:" 之前
blocks = re.split(r'(?=^  - id: )', text, flags=re.M)

kept = []
removed = []
preexisting_missing = []

for b in blocks:
    m = re.match(r'^  - id: (\S+)', b)
    if not m:
        kept.append(b)
        continue
    iid = m.group(1)
    fm = re.search(r'^    file: (\S+)', b, re.M)
    if not fm:
        kept.append(b)
        continue
    f = fm.group(1)
    if not f.startswith('/img/'):
        kept.append(b)
        continue
    p = ROOT / 'public' / f.lstrip('/')
    if p.exists():
        kept.append(b)
    else:
        if '-extra-' in f:
            removed.append((iid, f))
        else:
            # 原本就缺的，不删，报告
            preexisting_missing.append((iid, f))
            kept.append(b)

out = ''.join(kept)
io.open(IMG, 'w', encoding='utf-8', newline='\n').write(out)

print(f'删除悬空记录 {len(removed)} 条')
print()
print('=== 原本就缺文件的记录（保留，需报告）===')
for iid, f in preexisting_missing:
    print(f'  {iid}')
    print(f'    {f}')

import yaml
d = yaml.safe_load(io.open(IMG, encoding='utf-8'))
print()
print('图片总数:', len(d['images']))
