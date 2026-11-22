# 给缺少「建造期」切片的舰补一个前置切片。
# 只补那些「首个切片明显晚于最早 fact」的，且不与现有首个切片重叠。
import glob
import io
import os
import re

import yaml


def load(p):
    return yaml.safe_load(io.open(p, encoding='utf-8')) or {}


ships = {}
for p in glob.glob('data/ships/*.yaml'):
    if '.bak' in p:
        continue
    ships[os.path.basename(p)[:-5]] = load(p)

classes = {}
for p in glob.glob('data/classes/*.yaml'):
    if '.bak' in p:
        continue
    classes[os.path.basename(p)[:-5]] = load(p)

report = []
for sid, ship in ships.items():
    sp = f'data/slices/{sid}.yaml'
    if not os.path.exists(sp):
        continue
    sd = load(sp)
    sl = sd.get('slices') or []
    if not sl:
        continue

    all_facts = (ship.get('facts') or []) + \
                (classes.get(ship.get('class'), {}).get('facts') or [])
    # 建造相关 fact 的最早日期（排除 identity 与 about）
    cand = []
    for f in all_facts:
        fld = str(f.get('field') or '')
        if fld.startswith('identity.') or f.get('about'):
            continue
        if not fld.startswith('construction.'):
            continue
        a = str((f.get('valid') or {}).get('from') or '')
        if re.match(r'^\d{4}', a):
            cand.append(a)
    if not cand:
        continue

    earliest = min(cand)
    first_slice_from = str(sl[0].get('from') or '')

    # 差距超过 1 年才补
    if earliest[:4] >= first_slice_from[:4]:
        continue
    if int(first_slice_from[:4]) - int(earliest[:4]) < 1:
        continue

    report.append({
        'sid': sid,
        'earliest': earliest,
        'first': first_slice_from,
        'code': sl[0].get('code'),
    })

print('需要补建造期切片的舰：')
for r in report:
    print(f"  {r['sid']:<16} 最早 fact {r['earliest']}  首个切片 {r['first']}  ({r['code']})")

print()
print(f'共 {len(report)} 艘')
