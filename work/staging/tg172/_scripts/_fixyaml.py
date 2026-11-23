# -*- coding: utf-8 -*-
"""Fix multi-line plain scalars: 'note: xxx' continued on next lines -> block scalar."""
import sys, re, glob, io

for p in sys.argv[1:]:
    src = open(p, encoding="utf-8").read().split("\n")
    out = []
    i = 0
    changed = 0
    while i < len(src):
        line = src[i]
        m = re.match(r"^(\s*)(note|value|title|text): (.+)$", line)
        if m and not m.group(3).startswith((">", "|", "'", '"')):
            indent = m.group(1)
            # collect continuation lines that are indented deeper than indent
            j = i + 1
            cont = []
            while j < len(src):
                nxt = src[j]
                if nxt.strip() == "":
                    break
                m2 = re.match(r"^(\s*)\S", nxt)
                if not m2 or len(m2.group(1)) <= len(indent):
                    break
                cont.append(nxt.strip())
                j += 1
            if cont:
                # rebuild as block scalar
                body = [m.group(3)] + cont
                out.append("%s%s: >-" % (indent, m.group(2)))
                for b in body:
                    out.append(indent + "  " + b)
                changed += 1
                i = j
                continue
        out.append(line)
        i += 1
    open(p, "w", encoding="utf-8").write("\n".join(out))
    print("fixed %d in %s" % (changed, p))
