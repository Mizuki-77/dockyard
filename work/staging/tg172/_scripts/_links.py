# -*- coding: utf-8 -*-
import sys, re
sys.path.insert(0, r"D:\deepseek harness\website-warships\work\staging\tg172")
import _tool

for name in ("wayback-navsource-astoria", "wayback-navsource-portland"):
    t = _tool.load(name)
    print("====", name)
    for m in re.finditer(r'href="([^"]+)"[^>]*>(.*?)</a>', t, re.I | re.S):
        href, label = m.group(1), _tool.to_text(m.group(2))
        blob = (href + " " + label).lower()
        if any(k in blob for k in ("history.navy", "ibiblio", "hazegray", "ussastoria", "hyperwar", "damage")):
            print(href, "|", label[:100])
