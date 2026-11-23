import io

import yaml

print('=== cossack 现有 commander facts ===')
d = yaml.safe_load(io.open('data/ships/cossack.yaml', encoding='utf-8'))
for f in d.get('facts') or []:
    if f.get('field') != 'service.commander':
        continue
    v = f.get('valid') or {}
    print(f"  {v.get('from')} -> {v.get('to')}  {str(f.get('value'))[:64]}")

print()
print('=== c1 的 sherbrooke relations ===')
s = yaml.safe_load(io.open('work/staging_cmdr/c1/commanders/robert-sherbrooke.yaml', encoding='utf-8'))
for t in (s.get('relations') or {}).get('ships') or []:
    print(f"  {t.get('ship')} {t.get('from')} -> {t.get('to')} | {t.get('role')}")
    if t.get('note'):
        print(f"      note: {str(t.get('note'))[:140]}")

print()
print('=== c1 的 agar rank ===')
a = yaml.safe_load(io.open('work/staging_cmdr/c1/commanders/augustus-agar.yaml', encoding='utf-8'))
print('  rank_final:', a.get('rank_final'))
print('  rank_at_post:', a.get('rank_at_post'))
