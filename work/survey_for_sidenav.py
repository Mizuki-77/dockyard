import glob
import io
import os

import yaml


def zh(v):
    if isinstance(v, dict):
        return v.get('zh') or v.get('en') or ''
    return str(v)


print('=== 15 艘舰，按国家分组 ===')
ships = []
for p in sorted(glob.glob('data/ships/*.yaml')):
    if '.bak' in p:
        continue
    d = yaml.safe_load(io.open(p, encoding='utf-8')) or {}
    sid = os.path.basename(p)[:-5]
    facts = d.get('facts') or []
    nat = ''
    typ = ''
    for f in facts:
        if f.get('field') == 'identity.nation' and not nat:
            nat = str(f.get('value'))
        if f.get('field') == 'identity.ship_type' and not typ:
            typ = str(f.get('value'))
    ships.append((sid, zh(d.get('name')), nat, typ))

for nat in sorted({s[2] for s in ships}):
    group = [s for s in ships if s[2] == nat]
    print(f'\n{nat} ({len(group)})')
    for sid, name, n, t in group:
        print(f'  {name:<14} {t:<16} {sid}')

print()
print('=== 3 场战役 ===')
for p in sorted(glob.glob('data/battles/*.yaml')):
    if '.bak' in p:
        continue
    d = yaml.safe_load(io.open(p, encoding='utf-8')) or {}
    bid = os.path.basename(p)[:-5]
    n = 0
    linked = 0
    for side in d.get('belligerents') or []:
        for s in side.get('ships') or []:
            n += 1
            if s.get('ship_id'):
                linked += 1
    print(f'  {zh(d.get("name")):<14} {bid:<16} 参战 {n} 艘，可点 {linked}')

print()
print('=== 2 个行动 ===')
for p in sorted(glob.glob('data/operations/*.yaml')):
    if '.bak' in p:
        continue
    d = yaml.safe_load(io.open(p, encoding='utf-8')) or {}
    print(f'  {zh(d.get("name")):<14} {os.path.basename(p)[:-5]}')

print()
print('=== 60 型武器的类别分布 ===')
from collections import Counter
cats = Counter()
for p in glob.glob('data/classes/*.yaml') + glob.glob('data/ships/*.yaml'):
    if '.bak' in p:
        continue
    d = yaml.safe_load(io.open(p, encoding='utf-8')) or {}
    for f in d.get('facts') or []:
        if f.get('field') == 'weapon.category':
            cats[str(f.get('value'))] += 1
print(f'  武器类别（按 fact 出现次数）: {dict(cats)}')
