# -*- coding: utf-8 -*-
"""看得出「哪些来源是主力」+ 每舰的来源清单。"""
import io
from pathlib import Path
from collections import defaultdict

import yaml

ROOT = Path(r"D:\deepseek harness\website-warships")
DATA = ROOT / "data"

S = {p.stem: yaml.safe_load(io.open(p, encoding="utf-8"))
     for p in (DATA / "ships").glob("*.yaml")}
C = {p.stem: yaml.safe_load(io.open(p, encoding="utf-8"))
     for p in (DATA / "classes").glob("*.yaml")}
src = yaml.safe_load(io.open(DATA / "sources.yaml", encoding="utf-8"))
S2 = {s["id"]: s for s in src["sources"]}

out = io.open(ROOT / "work" / "_src2.txt", "w", encoding="utf-8")
w = out.write

use = defaultdict(set)
for sid in S:
    pool = list(S[sid].get("facts") or [])
    cid = S[sid].get("class")
    if cid in C:
        pool += list(C[cid].get("facts") or [])
    for f in pool:
        for x in (f.get("src") or []):
            use[x].add(sid)

w("===== 来源被几艘船用到（降序）=====\n")
for k, v in sorted(use.items(), key=lambda kv: (-len(kv[1]), kv[0])):
    s = S2.get(k, {})
    w("  %-34s %d 艘  tier=%s  %s\n"
      % (k, len(v), s.get("tier", "?"), (s.get("title") or "")[:42]))

w("\n===== 每舰用的来源清单 =====\n")
for sid in sorted(S):
    pool = list(S[sid].get("facts") or [])
    cid = S[sid].get("class")
    if cid in C:
        pool += list(C[cid].get("facts") or [])
    sr = sorted({x for f in pool for x in (f.get("src") or [])})
    w("\n[%s] %d 个来源\n" % (sid, len(sr)))
    for x in sr:
        s = S2.get(x, {})
        w("   %-32s tier=%s\n" % (x, s.get("tier", "?")))

# 域名聚合：看主力站点
w("\n===== 按域名聚合（哪些站是真正的主力）=====\n")
from urllib.parse import urlparse
dom = defaultdict(set)
for k in use:
    u = S2.get(k, {}).get("url") or ""
    h = urlparse(u).netloc.replace("www.", "")
    if h:
        dom[h].add(k)
for h, ks in sorted(dom.items(), key=lambda kv: -len(kv[1])):
    w("  %-32s %d 个来源\n" % (h, len(ks)))

out.close()
print("ok")
