# -*- coding: utf-8 -*-
"""找出 YAML 里「行内标量含 ': '」的隐患（会破坏解析）。"""
import glob, re, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pat = re.compile(r'^(\s*-?\s*)([A-Za-z_]+)\s*:\s+([^|>\'"\s].*)$')
n = 0
for p in sorted(glob.glob(os.path.join(ROOT, '**', '*.yaml'), recursive=True)):
    rel = os.path.relpath(p, ROOT)
    for i, line in enumerate(open(p, encoding='utf-8'), 1):
        s = line.rstrip('\n')
        m = pat.match(s)
        if not m:
            continue
        val = m.group(3)
        if ': ' in val:
            n += 1
            print('%s:%d: %s' % (rel, i, s.strip()[:160]))
print('total %d' % n)
