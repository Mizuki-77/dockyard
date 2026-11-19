# -*- coding: utf-8 -*-
"""模拟在时刻 T 做五舰对比，看 compare:true 字段的真实命中率。"""
from pathlib import Path
import datetime as dt
import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def load(p):
    with open(p, encoding="utf-8") as f:
        return yaml.safe_load(f)


reg = load(DATA / "fields.yaml")
compare_fields = [f for f in reg["fields"] if f.get("compare") and (f.get("applies_to") or ["class", "ship"]) == ["class", "ship"]]

ships = {p.stem: load(p) for p in sorted((DATA / "ships").glob("*.yaml"))}
classes = {p.stem: load(p) for p in sorted((DATA / "classes").glob("*.yaml"))}


def norm(v):
    if v is None:
        return None
    if isinstance(v, dt.date):
        return v.isoformat()
    s = str(v).strip()
    import re
    m = re.match(r"^(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?", s)
    if not m:
        return None
    y, mo, d = m.group(1), m.group(2) or "01", m.group(3) or "01"
    return f"{y}-{mo}-{d}"


def num(v, edge="start"):
    s = norm(v)
    if not s:
        return 9_999_999_999 if edge == "end" else 0
    y, m, d = s.split("-")
    return int(y) * 10000 + int(m) * 100 + int(d)


def pool(sid):
    s = ships[sid]
    own = [(f, "ship") for f in (s.get("facts") or [])]
    inh = [(f, "class") for f in (classes[s["class"]].get("facts") or [])] if s.get("class") in classes else []
    return own + inh


def at(sid, field, T):
    t = num(T)
    hits = []
    for f, origin in pool(sid):
        if f.get("field") != field or f.get("about"):
            continue
        a = num(f.get("valid", {}).get("from"), "start")
        b = num((f.get("valid") or {}).get("to"), "end")
        if a <= t <= b:
            hits.append((f, origin))
    ship = [h for h in hits if h[1] == "ship"]
    return ship if ship else hits


for T in ["1941-03-01", "1941-05-01", "1941-05-24", "1942-06-01"]:
    print("=" * 20, "T =", T)
    n_ok = 0
    for f in compare_fields:
        vals = {}
        for sid in ships:
            h = at(sid, f["id"], T)
            vals[sid] = h[0][0].get("value") if h else None
        got = sum(1 for v in vals.values() if v is not None)
        if got:
            n_ok += 1
            mark = "OK " if got == 5 else "   "
            print(f" {mark} {f['id']:34s} {got}/5  " + "  ".join(f"{k[:6]}={v}" for k, v in vals.items()))
    print(f"  -> 有值的字段 {n_ok}/{len(compare_fields)}，五舰齐全的 {sum(1 for f in compare_fields if all(at(s, f['id'], T) for s in ships))}")
    print()
