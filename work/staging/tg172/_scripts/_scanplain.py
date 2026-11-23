# -*- coding: utf-8 -*-
"""Find plain-scalar note/value lines whose content contains ': ' (illegal plain scalar)."""
import sys, re

for p in sys.argv[1:]:
    for n, line in enumerate(open(p, encoding="utf-8"), 1):
        m = re.match(r"^(\s*)(note|value|title|text): (.+)$", line.rstrip("\n"))
        if not m:
            continue
        body = m.group(3)
        if body.startswith((">", "|")):
            continue
        # find ': ' or ' #' inside body
        if re.search(r":(\s|$)", body) or " #" in body:
            print("%s:%d: %s" % (p, n, line.rstrip()[:160]))
