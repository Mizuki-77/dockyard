import glob
import io
import os

import yaml


def name_of(d):
    n = d.get('name')
    if isinstance(n, dict):
        return n.get('zh') or n.get('en') or '?'
    return str(n)


print('=== 现有 12 舰 ===')
for p in sorted(glob.glob('data/ships/*.yaml')):
    if '.bak' in p:
        continue
    d = yaml.safe_load(io.open(p, encoding='utf-8')) or {}
    sid = os.path.basename(p)[:-5]
    facts = len(d.get('facts') or [])
    print(f'  {sid:<16} {name_of(d):<14} class={str(d.get("class")):<16} fact={facts}')

print()
print('=== 现有 8 舰级 ===')
for p in sorted(glob.glob('data/classes/*.yaml')):
    if '.bak' in p:
        continue
    d = yaml.safe_load(io.open(p, encoding='utf-8')) or {}
    cid = os.path.basename(p)[:-5]
    of = d.get('class_of') or []
    print(f'  {cid:<16} {name_of(d):<14} class_of={of}')

print()
print('=== 战役里出现过的舰（未入库的）===')
known = set()
for p in glob.glob('data/ships/*.yaml'):
    if '.bak' in p:
        continue
    known.add(os.path.basename(p)[:-5])

for p in sorted(glob.glob('data/battles/*.yaml')):
    if '.bak' in p:
        continue
    d = yaml.safe_load(io.open(p, encoding='utf-8')) or {}
    print(f'--- {os.path.basename(p)[:-5]} ---')
    for side in d.get('belligerents') or []:
        label = side.get('name')
        if isinstance(label, dict):
            label = label.get('zh')
        for s in side.get('ships') or []:
            sid = s.get('ship_id') or ''
            sname = s.get('name')
            if isinstance(sname, dict):
                sname = sname.get('zh')
            mark = '已入库' if sid in known else '  缺  '
            print(f'    {mark} {str(sid):<18} {sname}')
