import glob

import yaml

print('=== 舰级名（舰级不带「号」，这是对的：级名不是单舰名） ===')
for p in sorted(glob.glob('data/classes/*.yaml')):
    if '.bak' in p:
        continue
    d = yaml.safe_load(open(p, encoding='utf-8'))
    print(f"  {d['id']:<14} {d['name']['zh']}")
