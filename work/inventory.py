import os, glob, sys, io, yaml
from collections import Counter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = os.getcwd()


def count_lines(p):
    with open(p, encoding='utf-8') as f:
        return sum(1 for _ in f)


print('=== src 目录 ===')
for p in sorted(glob.glob('src/**/*', recursive=True)):
    if os.path.isfile(p):
        rel = p.replace('\\', '/')
        print(f'{rel:52} {count_lines(p):5} 行 {os.path.getsize(p):7} B')

print()
print('=== data 汇总 ===')
for sub in ['ships', 'classes', 'slices', 'articles', 'weapon-articles',
            'battles', 'operations', 'narratives']:
    files = sorted(glob.glob(f'data/{sub}/*.yaml'))
    lines = sum(count_lines(p) for p in files)
    print(f'  data/{sub:18} {len(files):3} 个文件 {lines:6} 行')

for f in ['data/fields.yaml', 'data/sources.yaml', 'data/images.yaml']:
    print(f'  {f:35} {count_lines(f):6} 行 {os.path.getsize(f):8} B')

print()
print('=== fact 与实体统计 ===')
ships = {}
classes = {}
for p in sorted(glob.glob('data/ships/*.yaml')):
    d = yaml.safe_load(open(p, encoding='utf-8'))
    ships[d['id']] = len(d.get('facts') or [])
for p in sorted(glob.glob('data/classes/*.yaml')):
    d = yaml.safe_load(open(p, encoding='utf-8'))
    classes[d['id']] = len(d.get('facts') or [])
print('  ships:', ships, '合计', sum(ships.values()))
print('  classes:', classes, '合计', sum(classes.values()))

weapons = set()
for p in glob.glob('data/classes/*.yaml') + glob.glob('data/ships/*.yaml'):
    d = yaml.safe_load(open(p, encoding='utf-8'))
    for f in d.get('facts') or []:
        a = f.get('about') or ''
        if a.startswith('weapon:'):
            weapons.add(a.split(':', 1)[1])
print('  武器实体:', len(weapons))

imgs = yaml.safe_load(open('data/images.yaml', encoding='utf-8'))['images']
srcs = yaml.safe_load(open('data/sources.yaml', encoding='utf-8'))['sources']
flds = yaml.safe_load(open('data/fields.yaml', encoding='utf-8'))['fields']
print('  图片:', len(imgs), Counter(x.get('license_tier') for x in imgs))
print('  来源:', len(srcs), Counter(s.get('tier') for s in srcs))
print('  字段:', len(flds))
