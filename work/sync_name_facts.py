# 把 identity.name_zh 这条 fact 的值同步成文件顶层的 name.zh。
#
# 为什么需要单独一步：normalize_ship_names.py 只改了 `name: { zh: ... }`
# 那一行（页面标题、树上显示用它），但 fact 里还有一条
# `field: identity.name_zh`（详情页「身份」区、以及可能被 fact 驱动的
# 地方用它）。两者不一致的话，同一个页面上会出现两个中文名。
#
# validate.py 不查这个（它没有「fact 值必须与顶层 name 一致」的规则），
# 所以只能靠这一步。以后改动舰名时，两步都要跑。
import glob
import io
import os
import sys
from datetime import datetime

import yaml

DRY = '--dry-run' in sys.argv

fixed = []
for p in sorted(glob.glob('data/ships/*.yaml')):
    if '.bak' in p:
        continue
    text = io.open(p, encoding='utf-8').read()
    d = yaml.safe_load(text)
    sid = d.get('id')
    nz = (d.get('name') or {}).get('zh')
    if not sid or not nz:
        continue

    old_fact = None
    for f in d.get('facts') or []:
        if f.get('field') == 'identity.name_zh' and f.get('value') != nz:
            old_fact = f.get('value')
            break
    if old_fact is None:
        continue

    # 只替换 identity.name_zh 那一条的 value 行。
    # 块形如：
    #   - field: identity.name_zh
    #     value: 赤城
    # 用正则定位「field: identity.name_zh」后紧跟的 value 行。
    pat = r'(- field: identity\.name_zh\n(?:[ \t]+\S+:.*\n)*?[ \t]+value: )(.+?)(\n)'
    m = None
    for mm in __import__('re').finditer(pat, text):
        m = mm
        break
    if not m:
        print(f'  ! {sid}: 找到不一致但正则没匹配上，跳过')
        continue

    new_text = text[:m.start(2)] + nz + text[m.end(2):]

    if not DRY:
        bak = f'{p}.bak-{datetime.now().strftime("%Y-%m-%d")}'
        if not os.path.exists(bak):
            io.open(bak, 'w', encoding='utf-8', newline='\n').write(text)
        io.open(p, 'w', encoding='utf-8', newline='\n').write(new_text)

    fixed.append((sid, old_fact, nz))

print(f'同步 identity.name_zh {len(fixed)} 条：')
for sid, old, new in fixed:
    print(f'  {sid:<18} {old:<14} -> {new}')

if DRY:
    print('\n=== dry-run ===')
    sys.exit(0)

print('\n复验：')
bad = []
for p in sorted(glob.glob('data/ships/*.yaml')):
    if '.bak' in p:
        continue
    d = yaml.safe_load(io.open(p, encoding='utf-8'))
    nz = (d.get('name') or {}).get('zh')
    for f in d.get('facts') or []:
        if f.get('field') == 'identity.name_zh' and f.get('value') != nz:
            bad.append((d['id'], nz, f.get('value')))
print('  全部一致' if not bad else f'  仍有不一致：{bad}')
