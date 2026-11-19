# -*- coding: utf-8 -*-
"""三个问题：
1. 五舰同时在世的日期交集
2. 对比器索引的 JSON 体积估算
3. 同 field 里口径混用的嫌疑（note 自述不是该口径）
"""
from pathlib import Path
import datetime as dt
import json
import re
import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def load(p):
    with open(p, encoding="utf-8") as f:
        return yaml.safe_load(f)


reg = load(DATA / "fields.yaml")
cmp_fields = [f["id"] for f in reg["fields"]
              if f.get("compare") and (f.get("applies_to") or ["class", "ship"]) == ["class", "ship"]]
ships = {p.stem: load(p) for p in sorted((DATA / "ships").glob("*.yaml"))}
classes = {p.stem: load(p) for p in sorted((DATA / "classes").glob("*.yaml"))}


def norm(v):
    if v is None:
        return None
    if isinstance(v, dt.date):
        return v.isoformat()
    m = re.match(r"^(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?", str(v).strip())
    if not m:
        return None
    return f"{m.group(1)}-{m.group(2) or '01'}-{m.group(3) or '01'}"


def pool(sid):
    s = ships[sid]
    own = [(f, "ship") for f in (s.get("facts") or [])]
    inh = [(f, "class") for f in (classes[s["class"]].get("facts") or [])] if s.get("class") in classes else []
    return own + inh


print("=== 1. 在世区间 ===")
span = {}
for sid in ships:
    comm = fate = None
    for f, _ in pool(sid):
        if f.get("field") == "construction.commissioned":
            comm = norm(f["value"])
        if f.get("field") == "construction.fate_date":
            fate = norm(f["value"])
    span[sid] = (comm, fate or "9999-12-31")
    print(f"{sid:16s} {comm} .. {fate}")
lo = max(v[0] for v in span.values())
hi = min(v[1] for v in span.values())
print(f"--> 五舰同时在世的交集: {lo} .. {hi}")

print()
print("=== 2. 索引体积估算 ===")
idx = {}
for sid in ships:
    fields = {}
    for f, origin in pool(sid):
        if f.get("field") in cmp_fields and not f.get("about"):
            fields.setdefault(f["field"], []).append({
                "from": norm((f.get("valid") or {}).get("from")),
                "to": norm((f.get("valid") or {}).get("to")),
                "value": f.get("value"),
                "unit": f.get("unit"),
                "conf": f.get("confidence"),
                "src": f.get("src") or [],
                "note": (f.get("note") or "")[:120],
            })
    idx[sid] = fields
blob = json.dumps(idx, ensure_ascii=False, default=str)
print("字段数只有 compare:true 时:", len(blob), "bytes ≈", round(len(blob.encode()) / 1024, 1), "KB")
n_win = sum(len(v) for s in idx.values() for v in s.values())
print("窗口条目总数:", n_win)
for sid in idx:
    print("  ", sid, "字段", len(idx[sid]), "窗口", sum(len(v) for v in idx[sid].values()))

print()
print("=== 3. 口径自述可疑（note 里出现「不是标准/不是满载/非条约」等） ===")
pat = re.compile(r"不是标准|不是满载|非条约|非.{0,6}口径|不同口径|口径不同|不可混用|不等于|并非同一")
for sid in ships:
    for f, origin in pool(sid):
        if f.get("field") in cmp_fields and pat.search(f.get("note") or ""):
            print(f"{sid:14s} {f['field']:32s} = {f.get('value')} {f.get('unit') or ''}")
            print("     note:", (f.get("note") or "").replace("\n", " ")[:150])
