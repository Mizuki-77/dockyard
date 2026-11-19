# -*- coding: utf-8 -*-
"""从 5 艘船的数据里实测归纳：字段命中率、来源复用率、每舰工作量。"""
import io
from pathlib import Path
from collections import Counter, defaultdict

import yaml

ROOT = Path(r"D:\deepseek harness\website-warships")
DATA = ROOT / "data"

S = {}
for p in (DATA / "ships").glob("*.yaml"):
    S[p.stem] = yaml.safe_load(io.open(p, encoding="utf-8"))
C = {}
for p in (DATA / "classes").glob("*.yaml"):
    C[p.stem] = yaml.safe_load(io.open(p, encoding="utf-8"))

reg = yaml.safe_load(io.open(DATA / "fields.yaml", encoding="utf-8"))
fields = {f["id"]: f for f in reg["fields"]}

src = yaml.safe_load(io.open(DATA / "sources.yaml", encoding="utf-8"))
S2 = {s["id"]: s for s in src["sources"]}

out = io.open(ROOT / "work" / "_method.txt", "w", encoding="utf-8")
w = out.write

# ---------- 1. 每舰的 fact 数与字段覆盖面 ----------
w("===== 1. 每舰数据量 =====\n")
w("%-16s %8s %8s %8s %8s %8s\n" % ("ship", "own", "class", "字段数", "来源数", "slices"))
for sid in sorted(S):
    s = S[sid]
    own = s.get("facts") or []
    cid = s.get("class")
    cl = (C.get(cid, {}).get("facts") or []) if cid else []
    fl = {f["field"] for f in own if f.get("field")}
    sr = set()
    for f in own:
        for x in (f.get("src") or []):
            sr.add(x)
    sl = yaml.safe_load(io.open(DATA / "slices" / (sid + ".yaml"), encoding="utf-8")) \
        if (DATA / "slices" / (sid + ".yaml")).exists() else {}
    w("%-16s %8d %8d %8d %8d %8d\n"
      % (sid, len(own), len(cl), len(fl), len(sr), len(sl.get("slices") or [])))

# ---------- 2. 舰级 vs 单舰的分工 ----------
w("\n===== 2. 舰级继承省了多少 =====\n")
w("%-16s %-14s %8s %8s %6s\n" % ("ship", "class", "单舰fact", "舰级fact", "复用比"))
for sid in sorted(S):
    s = S[sid]
    cid = s.get("class") or "-"
    own = len(s.get("facts") or [])
    cl = len((C.get(cid, {}).get("facts") or [])) if cid in C else 0
    ratio = ("%.1fx" % (own / cl)) if cl else "-"
    w("%-16s %-14s %8d %8d %6s\n" % (sid, cid, own, cl, ratio))

# ---------- 3. 来源复用 ----------
w("\n===== 3. 来源被几艘船用到 =====\n")
use = defaultdict(set)
for sid in S:
    pool = list(S[sid].get("facts") or [])
    cid = S[sid].get("class")
    if cid in C:
        pool += list(C[cid].get("facts") or [])
    for f in pool:
        for x in (f.get("src") or []):
            use[x].add(sid)
multi = [(k, v) for k, v in use.items() if len(v) >= 2]
w("总来源被引用: %d 个\n" % len(use))
w("被 2 艘以上船共用的: %d 个（%.0f%%）\n"
  % (len(multi), 100.0 * len(multi) / max(1, len(use))))
w("\n被 3 艘以上船共用的来源（说明这几站是主力）：\n")
for k, v in sorted(use.items(), key=lambda kv: -len(kv[1])):
    if len(v) >= 3:
        tier = S2.get(k, {}).get("tier", "?")
        w("  %-32s %d 艘  tier=%s\n" % (k, len(v), tier))

# ---------- 4. 各领域字段的覆盖：哪些是"必填套路" ----------
w("\n===== 4. 按 group 看覆盖率（5 舰里几艘有这个字段）=====\n")
byg = defaultdict(Counter)
for sid in S:
    pool = list(S[sid].get("facts") or [])
    cid = S[sid].get("class")
    if cid in C:
        pool += list(C[cid].get("facts") or [])
    seen = set()
    for f in pool:
        if f.get("about"):
            continue
        fl = f.get("field")
        if fl in fields:
            seen.add(fl)
    for fl in seen:
        byg[fields[fl]["group"]][fl] += 1

for g in sorted(byg, key=lambda x: -sum(byg[x].values())):
    tot = sum(byg[g].values())
    w("\n[%s] 字段命中 %d 次\n" % (g, tot))
    rows = sorted(byg[g].items(), key=lambda kv: -kv[1])
    full = [k for k, v in rows if v == 5]
    if full:
        w("  5/5 全覆盖（%d 个）：%s\n" % (len(full), ", ".join(full[:12])))

out.close()
print("ok")
