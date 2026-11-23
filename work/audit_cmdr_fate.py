import glob
import io

import yaml

print('=== commander fact 里带「沉没 / 阵亡 / 死」的记录 ===')
for p in sorted(glob.glob('data/ships/*.yaml')):
    if '.bak' in p:
        continue
    d = yaml.safe_load(io.open(p, encoding='utf-8')) or {}
    sid = d.get('id')
    for f in d.get('facts') or []:
        if f.get('field') != 'service.commander':
            continue
        v = str(f.get('value') or '')
        note = str(f.get('note') or '')
        if any(k in v + note for k in ('沉没', '阵亡', '死亡', '战死')):
            print(f'  {sid:<16} {v[:80]}')
            if note:
                print(f'{"":<20} note: {note[:110]}')
