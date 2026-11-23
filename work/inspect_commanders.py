import glob
import io

import yaml

rows = []
for p in sorted(glob.glob('data/commanders/*.yaml')):
    d = yaml.safe_load(io.open(p, encoding='utf-8'))
    rows.append((d.get('id'), d.get('rank_final'), d.get('rank_at_post'),
                 len(d.get('intro') or []), len(d.get('timeline') or []),
                 len((d.get('relations') or {}).get('ships') or []),
                 len((d.get('relations') or {}).get('battles') or [])))

print(f'{"id":<22}{"final":<26}{"at_post":<22}{"intro":>6}{"tl":>4}{"ship":>6}{"btl":>5}')
print('-' * 95)
for r in rows:
    print(f'{str(r[0]):<22}{str(r[1]):<26}{str(r[2]):<22}{r[3]:>6}{r[4]:>4}{r[5]:>6}{r[6]:>5}')

print()
print(f'共 {len(rows)} 人')
print(f'缺 rank_at_post: {[r[0] for r in rows if not r[2]]}')
