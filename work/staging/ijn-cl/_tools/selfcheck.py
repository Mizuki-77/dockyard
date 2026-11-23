# -*- coding: utf-8 -*-
"""按 SCHEMA §10 自检本组分片。Usage: python _tools/selfcheck.py"""
import os, glob, sys, re
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WS = os.path.abspath(os.path.join(ROOT, "..", "..", ".."))

fields = yaml.safe_load(open(os.path.join(WS, "data", "fields.yaml"), encoding="utf-8"))
REG = {f["id"]: f for f in fields["fields"]}
UNITS = fields["units"]

known_src = set()
for p in [os.path.join(WS, "data", "sources.yaml"),
          os.path.join(ROOT, "sources-fragment.yaml")]:
    if os.path.exists(p):
        d = yaml.safe_load(open(p, encoding="utf-8"))
        for s in d.get("sources", []):
            known_src.add(s["id"])

errors, warns = [], []


def chk(cond, msg, bucket):
    if not cond:
        bucket.append(msg)


for path in sorted(glob.glob(os.path.join(ROOT, "**", "*.yaml"), recursive=True)):
    rel = os.path.relpath(path, ROOT)
    try:
        doc = yaml.safe_load(open(path, encoding="utf-8"))
    except Exception as e:
        errors.append("%s: YAML 解析失败: %s" % (rel, e))
        continue
    if not isinstance(doc, dict):
        continue
    if "sources" in doc:
        for s in doc["sources"]:
            for k in ("id", "title", "url", "type", "tier", "role"):
                chk(k in s, "%s: source %s 缺 %s" % (rel, s.get("id"), k), errors)
            chk(s.get("tier") in list("ABCDE"),
                "%s: source %s tier=%s 非法" % (rel, s.get("id"), s.get("tier")), errors)
            for r in (s.get("role") or []):
                chk(r in ("data", "narrative", "rights", "lead", "image"),
                    "%s: source %s role=%s 非法" % (rel, s.get("id"), r), errors)
    facts = doc.get("facts") or []
    for i, f in enumerate(facts):
        tag = "%s fact[%d]" % (rel, i)
        fid = f.get("field")
        chk(fid in REG, "%s: field %r 未注册" % (tag, fid), errors)
        if fid not in REG:
            continue
        reg = REG[fid]
        # unit
        want = reg.get("unit")
        got = f.get("unit")
        if want and want != "date":
            chk(got == want, "%s: %s 单位应为 %s，实为 %r" % (tag, fid, want, got), errors)
        elif not want:
            chk(got is None, "%s: %s 不该有 unit（实为 %r）" % (tag, fid, got), errors)
        # type
        t = reg.get("type")
        v = f.get("value")
        if t == "number" and not isinstance(v, (int, float)):
            errors.append("%s: %s 应为 number，实为 %r" % (tag, fid, v))
        if t == "integer" and not isinstance(v, int):
            errors.append("%s: %s 应为 integer，实为 %r" % (tag, fid, v))
        if t == "enum":
            chk(v in (reg.get("values") or []),
                "%s: %s 值 %r 不在枚举内" % (tag, fid, v), errors)
        if t == "bool":
            chk(isinstance(v, bool), "%s: %s 应为 bool" % (tag, fid), errors)
        # src
        src = f.get("src") or []
        chk(len(src) >= 1, "%s: %s 无 src" % (tag, fid), errors)
        for s in src:
            chk(s in known_src, "%s: src %r 未登记" % (tag, s), errors)
        # confidence
        conf = f.get("confidence")
        chk(conf in ("A", "B", "C"), "%s: confidence=%r 非法" % (tag, conf), errors)
        # valid
        val = f.get("valid") or {}
        chk("from" in val, "%s: %s 缺 valid.from" % (tag, fid), errors)
        if "from" in val:
            chk(re.match(r"^\d{4}(-\d{2}(-\d{2})?)?$", str(val["from"])),
                "%s: valid.from=%r 格式错" % (tag, val["from"]), errors)
        if "to" not in val or val.get("to") is None:
            chk(bool(f.get("note")) or bool(doc.get("open_ended_note")),
                "%s: %s valid.to 留空且无 note" % (tag, fid), errors)
        # qual
        qk = reg.get("qual_keys")
        if qk:
            q = f.get("qual") or {}
            for k in qk:
                chk(k in q, "%s: %s 缺 qual.%s" % (tag, fid, k), errors)
            for k, allowed in (reg.get("qual_values") or {}).items():
                if k in q:
                    chk(q[k] in allowed,
                        "%s: %s qual.%s=%r 非法" % (tag, fid, k, q[k]), errors)
        # tier E 不能支撑 fact
        for s in src:
            sp = os.path.join(ROOT, "sources-fragment.yaml")
            if os.path.exists(sp):
                pass
    # articles
    if "intro" in doc or "history" in doc:
        for k in ("ship", "intro", "history"):
            chk(k in doc, "%s: 正文缺顶层 %s" % (rel, k), errors)
        lead = (doc.get("intro") or {}).get("lead") or {}
        chk("zh" in lead, "%s: intro.lead 缺 zh" % rel, errors)
        paras = (doc.get("intro") or {}).get("paragraphs") or []
        chk(len(paras) >= 1, "%s: intro.paragraphs 为空" % rel, errors)
        for j, p in enumerate(paras):
            chk("heading" in p and (p.get("text") or {}).get("zh") and p.get("src"),
                "%s: para[%d] 缺 heading/text.zh/src" % (rel, j), errors)
        ev_n = 0
        for sec in doc.get("history") or []:
            chk("id" in sec and (sec.get("title") or {}).get("zh") and sec.get("events"),
                "%s: history 节缺 id/title/events" % rel, errors)
            for ev in sec.get("events") or []:
                ev_n += 1
                chk(ev.get("date") and (ev.get("text") or {}).get("zh") and ev.get("src"),
                    "%s: event 缺 date/text.zh/src" % rel, errors)
        chk(ev_n >= 8, "%s: 事件数 %d < 8" % (rel, ev_n), warns)
        raw = open(path, encoding="utf-8").read()
        for bad in ("据说", "有人认为", "有人称", "据信", "或许", "大概", "应该是"):
            if bad in raw:
                errors.append("%s: 正文含禁词「%s」" % (rel, bad))
    # slices
    if "slices" in doc:
        prev_to = None
        for s in doc["slices"]:
            for k in ("code", "title", "from", "note"):
                chk(k in s, "%s: slice %s 缺 %s" % (rel, s.get("code"), k), errors)

# tier E 不得作 fact 来源
sp = os.path.join(ROOT, "sources-fragment.yaml")
frag = yaml.safe_load(open(sp, encoding="utf-8"))
tier = {s["id"]: s["tier"] for s in frag["sources"]}
for path in sorted(glob.glob(os.path.join(ROOT, "**", "*.yaml"), recursive=True)):
    if path.endswith("sources-fragment.yaml"):
        continue
    doc = yaml.safe_load(open(path, encoding="utf-8")) or {}
    if not isinstance(doc, dict):
        continue
    for i, f in enumerate(doc.get("facts") or []):
        for s in (f.get("src") or []):
            if tier.get(s) == "E":
                errors.append("%s fact[%d]: 用 tier E 来源 %r 支撑 fact"
                              % (os.path.relpath(path, ROOT), i, s))

print("=== ERRORS (%d)" % len(errors))
for e in errors:
    print("  ✗", e)
print("=== WARNINGS (%d)" % len(warns))
for w in warns:
    print("  !", w)
print("\n登记来源 %d 个；tier E %d 个" % (len(tier), sum(1 for v in tier.values() if v == "E")))
sys.exit(1 if errors else 0)
