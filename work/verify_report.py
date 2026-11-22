# 核对交接报告里的数字是否与实际一致。
import glob
import io
import os
import re

import yaml

print('=== 1. 报告声称 vs 实际 ===')

# 页面数
pages = len(glob.glob('dist/**/*.html', recursive=True))
print(f'页面数: 报告 106 / 实际 {pages}')

# 舰、级、武器、战役、行动
ships = [p for p in glob.glob('data/ships/*.yaml') if '.bak' not in p]
classes = [p for p in glob.glob('data/classes/*.yaml') if '.bak' not in p]
slices = [p for p in glob.glob('data/slices/*.yaml') if '.bak' not in p]
articles = glob.glob('data/articles/*.yaml')
wart = glob.glob('data/weapon-articles/*.yaml')
battles = [p for p in glob.glob('data/battles/*.yaml') if '.bak' not in p]
ops = [p for p in glob.glob('data/operations/*.yaml') if '.bak' not in p]
print(f'舰: 15 / {len(ships)}')
print(f'舰级: 10 / {len(classes)}')
print(f'切片: 15 / {len(slices)}')
print(f'舰艇正文: 15 / {len(articles)}')
print(f'武器正文: 64 / {len(wart)}')
print(f'战役: 3 / {len(battles)}')
print(f'行动: 2 / {len(ops)}')

# fact
total = 0
for p in classes + ships:
    d = yaml.safe_load(io.open(p, encoding='utf-8')) or {}
    total += len(d.get('facts') or [])
print(f'fact: 1803 / {total}')

# 来源、图片、字段
s = yaml.safe_load(io.open('data/sources.yaml', encoding='utf-8'))
i = yaml.safe_load(io.open('data/images.yaml', encoding='utf-8'))
f = yaml.safe_load(io.open('data/fields.yaml', encoding='utf-8'))
fs = f['fields'] if 'fields' in f else f
print(f'来源: 253 / {len(s["sources"])}')
print(f'图片记录: 451 / {len(i["images"])}')
print(f'字段: 213 / {len(fs)}')
print(f'图片文件: 471 / {len(glob.glob("public/img/**/*", recursive=True))}')

# 每舰 fact 数
print()
print('=== 2. 每舰 fact 数（报告表格用）===')
for p in sorted(ships):
    d = yaml.safe_load(io.open(p, encoding='utf-8')) or {}
    sid = os.path.basename(p)[:-5]
    print(f'  {sid:<18} {len(d.get("facts") or [])}')
