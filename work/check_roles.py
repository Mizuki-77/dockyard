import glob
import yaml

CAT_TO_ROLE = {
    'naval_gun': 'secondary_battery',
    'coastal_gun': 'other',
    'anti_aircraft_gun': 'anti_aircraft',
    'torpedo': 'torpedo',
    'depth_charge': 'other',
    'mine': 'other',
    'rocket': 'rocket',
    'radar': 'radar',
    'fire_control': 'fire_control',
    'aircraft': 'aircraft',
    'other': 'other',
}

# 从 catalog.ts 提取已登记项
import re
ts = open('src/lib/catalog.ts', encoding='utf-8').read()
block = ts.split('const ROLE_BY_WEAPON')[1].split('};')[0]
registered = dict(re.findall(r"'([^']+)':\s*'([a-z_]+)'", block))

info = {}
for p in glob.glob('data/ships/*.yaml') + glob.glob('data/classes/*.yaml'):
    if '.bak' in p:
        continue
    d = yaml.safe_load(open(p, encoding='utf-8')) or {}
    for f in d.get('facts') or []:
        a = str(f.get('about') or '')
        if not a.startswith('weapon:'):
            continue
        wid = a[7:]
        rec = info.setdefault(wid, {'cat': None, 'desig': None, 'where': []})
        if f.get('field') == 'weapon.category':
            rec['cat'] = f.get('value')
        if f.get('field') == 'weapon.designation':
            rec['desig'] = f.get('value')
        rec['where'].append(p.split('/')[-1].replace('.yaml', ''))

print(f'{"weapon id":<26} {"category":<20} {"role(now)":<20} 显式登记?  designation')
print('-' * 120)
missing = []
for wid in sorted(info):
    rec = info[wid]
    role = registered.get(wid) or CAT_TO_ROLE.get(rec['cat'], 'other')
    explicit = 'YES' if wid in registered else ''
    if wid not in registered:
        missing.append((wid, rec['cat'], role, (rec['desig'] or '')[:40]))
    print(f'{wid:<26} {str(rec["cat"]):<20} {role:<20} {explicit:<9} {str(rec["desig"])[:45]}')

print()
print('未显式登记、靠 category 退化的：', len(missing))
for m in missing:
    print('  -', m[0], '| cat =', m[1], '| 退化为', m[2], '|', m[3])
