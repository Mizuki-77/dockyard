import sys, os
from pypdf import PdfReader

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_raw')
src = os.path.join(RAW, sys.argv[1])
r = PdfReader(src)
print(f'pages={len(r.pages)}')
out = []
for i, p in enumerate(r.pages):
    t = p.extract_text() or ''
    out.append(f'\n===== PAGE {i+1} =====\n' + t)
txt = '\n'.join(out)
dst = src + '.txt'
open(dst, 'w', encoding='utf-8').write(txt)
print(f'wrote {len(txt)} chars -> {dst}')
