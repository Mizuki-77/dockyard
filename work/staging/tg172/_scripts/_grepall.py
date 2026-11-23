# -*- coding: utf-8 -*-
import sys, os, re, glob
sys.path.insert(0, r"D:\deepseek harness\website-warships\work\staging\tg172")
import _tool

RAW = r"D:\deepseek harness\website-warships\work\staging\tg172\_raw"
pat = re.compile(sys.argv[1], re.I)
prefix = sys.argv[2] if len(sys.argv) > 2 else ""
for p in sorted(glob.glob(os.path.join(RAW, prefix + "*.txt"))):
    t = _tool.to_text(open(p, encoding="utf-8", errors="replace").read())
    lines = t.split("\n")
    hits = [(i, ln) for i, ln in enumerate(lines) if pat.search(ln)]
    if not hits:
        continue
    print("==== %s (%d hits)" % (os.path.basename(p), len(hits)))
    for i, ln in hits[:25]:
        print("   L%-5d %s" % (i + 1, ln.strip()[:260]))
