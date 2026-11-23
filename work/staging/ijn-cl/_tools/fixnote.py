# -*- coding: utf-8 -*-
"""修正：把「单行 note 内含 ': '」的值自动改成双引号包裹。"""
import glob, re, os, io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pat = re.compile(r'^(\s*)note:[ ]+([^|>\'"\s].*)$')
fixed = 0
for p in sorted(glob.glob(os.path.join(ROOT, '**', '*.yaml'), recursive=True)):
    lines = io.open(p, encoding='utf-8').read().split('\n')
    out, changed = [], False
    for line in lines:
        m = pat.match(line)
        if m and ': ' in m.group(2):
            indent, val = m.group(1), m.group(2)
            val = val.replace('\\', '\\\\').replace('"', '\\"')
            out.append('%snote: "%s"' % (indent, val))
            changed = True
            fixed += 1
        else:
            out.append(line)
    if changed:
        io.open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
        print('fixed', os.path.relpath(p, ROOT))
print('total fixed', fixed)
