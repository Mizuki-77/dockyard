import io

import yaml

s = yaml.safe_load(io.open('data/sources.yaml', encoding='utf-8'))
i = yaml.safe_load(io.open('data/images.yaml', encoding='utf-8'))
f = yaml.safe_load(io.open('data/fields.yaml', encoding='utf-8'))
fs = f['fields'] if 'fields' in f else f

print(f'来源: {len(s["sources"])}')
print(f'图片记录: {len(i["images"])}')
print(f'字段: {len(fs)}')

# 层级分布
from collections import Counter
tiers = Counter(x.get('tier') for x in s['sources'])
print(f'来源层级: {dict(tiers)}')

# 图片按 subject 类型
kinds = Counter(str(x.get('subject', '')).split(':')[0] for x in i['images'])
print(f'图片来源: {dict(kinds)}')

# fact 总数
import glob
total = 0
for p in glob.glob('data/classes/*.yaml') + glob.glob('data/ships/*.yaml'):
    if '.bak' in p:
        continue
    d = yaml.safe_load(io.open(p, encoding='utf-8')) or {}
    total += len(d.get('facts') or [])
print(f'fact 总数: {total}')
