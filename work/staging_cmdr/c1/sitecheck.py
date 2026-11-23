# -*- coding: utf-8 -*-
"""拿站点自己的 check_commander 规则跑一遍 c1 的三份档案（只读，不写 data/）。"""
import glob
import importlib.util
import io
import os
import sys

import yaml

sys.stdout.reconfigure(encoding='utf-8')

spec = importlib.util.spec_from_file_location('validate', 'scripts/validate.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)

ship_ids = {os.path.basename(p)[:-5] for p in glob.glob('data/ships/*.yaml') if '.bak' not in p}
battle_ids = {os.path.basename(p)[:-5] for p in glob.glob('data/battles/*.yaml') if '.bak' not in p}

reg = yaml.safe_load(io.open('data/sources.yaml', encoding='utf-8'))
known = {s['id'] for s in reg['sources']}
frag = yaml.safe_load(io.open('work/staging_cmdr/c1/sources-fragment.yaml', encoding='utf-8'))
for s in frag['sources']:
    known.add(s['id'])

rep = v.Report()
for p in sorted(glob.glob('work/staging_cmdr/c1/commanders/*.yaml')):
    from pathlib import Path
    v.check_commander(Path(p), known, rep, ship_ids, battle_ids)

for i in rep.infos:
    print(' .', i)
for w in rep.warnings:
    print(' !', w['where'], w['msg'], w.get('fix') or '')
for e in rep.errors:
    print(' x', e['where'], e['msg'], e.get('fix') or '')
print('\n站点规则：%d 错误 / %d 警告' % (len(rep.errors), len(rep.warnings)))
