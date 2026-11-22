import glob
import io
import os

import yaml


def load(p):
    return yaml.safe_load(io.open(p, encoding='utf-8')) or {}


CASES = [
    ('enterprise', '1960'),
    ('prince-of-wales', '1945'),
    ('illustrious', '1936'),
]

for sid, yr in CASES:
    ship = load(f'data/ships/{sid}.yaml')
    cid = ship.get('class')
    cls = load(f'data/classes/{cid}.yaml') if cid else {}
    facts = (ship.get('facts') or []) + (cls.get('facts') or [])

    print(f'=== {sid} ({yr}) ===')
    for f in facts:
        if str(f.get('field') or '').startswith('identity.') or f.get('about'):
            continue
        v = f.get('valid') or {}
        a = str(v.get('from') or '')
        b = str(v.get('to') or '')
        if a.startswith(yr) or b.startswith(yr):
            print(f"  {str(f.get('field')):<34} {a} ~ {b or 'open'}")
            print(f"     value: {str(f.get('value'))[:60]}")
    print()
