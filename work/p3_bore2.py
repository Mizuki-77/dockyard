# -*- coding: utf-8 -*-
"""列出所有 weapon.bore 的实际值（含 about 归属）。"""
import io
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
out = []

for sub in ("classes", "ships"):
    for p in sorted((DATA / sub).glob("*.yaml")):
        doc = yaml.safe_load(open(p, encoding="utf-8"))
        for f in doc.get("facts") or []:
            if f.get("field") == "weapon.bore":
                out.append((p.stem, f.get("about"), f.get("value"), f.get("unit")))
        for w in doc.get("weapons") or []:
            for f in w.get("facts") or []:
                if f.get("field") == "weapon.bore":
                    out.append((p.stem, w.get("id"), f.get("value"), f.get("unit")))

lines = [f"{o[0]:16s} {str(o[1]):40s} {o[2]} {o[3]}" for o in out]
vals = sorted({o[2] for o in out if isinstance(o[2], (int, float))})
lines.append("")
lines.append("取值集合: " + str(vals))
lines.append("unit 集合: " + str(sorted({str(o[3]) for o in out})))
lines.append("条数: " + str(len(out)))
io.open(ROOT / "work" / "_p3_bore.txt", "w", encoding="utf-8").write("\n".join(lines))
print("done", len(out))
