import glob
import re

import yaml


def load(p):
    return yaml.safe_load(open(p, encoding='utf-8')) or {}


for sid in ['ark-royal', 'dorsetshire', 'victorious']:
    s = load(f'data/ships/{sid}.yaml')
    cid = s.get('class')
    c = load(f'data/classes/{cid}.yaml') if cid else {}
    facts = [f for f in (s.get('facts') or []) + (c.get('facts') or [])
             if not str(f.get('field') or '').startswith('identity.') and not f.get('about')]
    spans = []
    for f in facts:
        v = f.get('valid') or {}
        a = str(v.get('from') or '')
        b = str(v.get('to') or '')
        if re.match(r'^\d{4}', a):
            spans.append((a, b, f['field']))
    spans.sort()
    print(f'== {sid} 最早 3 条 / 最晚 3 条（不含 identity / about）')
    for x in spans[:3]:
        print(f'    {x[0]} -> {x[1] or "(open)"}  {x[2]}')
    print('    ...')
    for x in spans[-3:]:
        print(f'    {x[0]} -> {x[1] or "(open)"}  {x[2]}')
    print()
