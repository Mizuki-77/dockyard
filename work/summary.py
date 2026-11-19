# -*- coding: utf-8 -*-
"""汇总全站数据规模，用于写交接报告。"""
import io
from pathlib import Path

import yaml

ROOT = Path(r"D:\deepseek harness\website-warships")
D = ROOT / "data"
out = []

out.append("=== 战斗 ===")
for p in sorted((D / "battles").glob("*.yaml")):
    d = yaml.safe_load(io.open(p, encoding="utf-8"))
    out.append("%-18s theater=%-10s timeline=%-3d hits=%-3d conseq=%-3d losses=%d" % (
        p.stem, d.get("theater") or "-",
        len(d.get("timeline") or []),
        len(d.get("hits_received") or []),
        len(d.get("consequences") or []),
        len(d.get("losses") or [])))

out.append("")
out.append("=== 行动 ===")
for p in sorted((D / "operations").glob("*.yaml")):
    d = yaml.safe_load(io.open(p, encoding="utf-8"))
    out.append("%-18s phases=%d" % (p.stem, len(d.get("phases") or [])))

out.append("")
out.append("=== 切片 ===")
for p in sorted((D / "slices").glob("*.yaml")):
    d = yaml.safe_load(io.open(p, encoding="utf-8"))
    sl = d.get("slices") or []
    out.append("%-18s %d 片  %s" % (p.stem, len(sl), [x["code"] for x in sl]))

out.append("")
out.append("=== 正文 ===")
out.append("舰艇正文: %d 篇" % len(list((D / "articles").glob("*.yaml"))))
out.append("武器正文: %d 篇" % len(list((D / "weapon-articles").glob("*.yaml"))))

out.append("")
out.append("=== 每舰 fact / 武器数 ===")
rows = []
for p in sorted((D / "ships").glob("*.yaml")):
    s = yaml.safe_load(io.open(p, encoding="utf-8"))
    fl = s.get("facts") or []
    w = len({f.get("about") for f in fl if (f.get("about") or "").startswith("weapon:")})
    rows.append((p.stem, len(fl), w, s.get("class")))
for r in sorted(rows, key=lambda x: -x[1]):
    out.append("%-16s fact=%-4d weapon=%-2d class=%s" % r)

out.append("")
out.append("=== 舰级 ===")
for p in sorted((D / "classes").glob("*.yaml")):
    c = yaml.safe_load(io.open(p, encoding="utf-8"))
    out.append("%-16s fact=%-4d class_of=%s" % (
        p.stem, len(c.get("facts") or []), c.get("class_of")))

io.open(ROOT / "work" / "_summary.txt", "w", encoding="utf-8").write("\n".join(out))
print("ok")
