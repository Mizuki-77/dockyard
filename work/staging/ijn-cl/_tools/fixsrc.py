# -*- coding: utf-8 -*-
"""修正 articles/*.yaml 中 src: 被误缩进到 text: 之下的问题。

规则：event 里的 src 应与该 event 的 text: 同级；
若 src 的缩进比 text: 多 2 格，就减 2 格。
"""
import glob, re, os, io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files = sorted(glob.glob(os.path.join(ROOT, 'articles', '*.yaml')))
total = 0

for p in files:
    lines = io.open(p, encoding='utf-8').read().split('\n')
    out = []
    text_indent = None
    changed = 0
    for line in lines:
        s = line.rstrip()
        m_text = re.match(r'^(\s*)text:\s*$', s)
        if m_text:
            text_indent = len(m_text.group(1))
            out.append(line)
            continue
        m_src = re.match(r'^(\s*)src:\s*\[', s)
        if m_src and text_indent is not None:
            ind = len(m_src.group(1))
            if ind == text_indent + 2:
                out.append(' ' * text_indent + s.lstrip())
                changed += 1
                continue
        # 离开该 event/text 块
        if s.strip() and text_indent is not None:
            ind = len(s) - len(s.lstrip())
            if ind < text_indent and not s.lstrip().startswith('-'):
                text_indent = None
        out.append(line)
    if changed:
        io.open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
        print('%s: fixed %d src lines' % (os.path.relpath(p, ROOT), changed))
        total += changed
print('total', total)
