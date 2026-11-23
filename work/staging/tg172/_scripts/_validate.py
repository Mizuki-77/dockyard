# -*- coding: utf-8 -*-
"""Validate tg172 shards against data/fields.yaml."""
import sys, glob, yaml

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = r"D:\deepseek harness\website-warships"
fields = yaml.safe_load(open(ROOT + r"\data\fields.yaml", encoding="utf-8"))
F = {f["id"]: f for f in fields["fields"]}
units = fields["units"]

errors = []
warns = []

for p in sorted(glob.glob(ROOT + r"\work\staging\tg172\**\*.yaml", recursive=True)):
    if p.endswith(".bak") or "sources-fragment" in p:
        continue
    d = yaml.safe_load(open(p, encoding="utf-8"))
    name = p.split("tg172\\")[-1]
    for i, f in enumerate(d.get("facts", [])):
        fid = f.get("field")
        where = "%s fact#%d %s" % (name, i, fid)
        if fid not in F:
            errors.append("%s :: field not registered" % where)
            continue
        reg = F[fid]

        # unit
        if reg.get("unit"):
            if f.get("unit") != reg["unit"]:
                errors.append("%s :: unit %r != %r" % (where, f.get("unit"), reg["unit"]))
        else:
            if "unit" in f:
                errors.append("%s :: unit given but registry unit is null" % where)

        # confidence
        if f.get("confidence") not in ("A", "B", "C", None):
            errors.append("%s :: confidence %r" % (where, f.get("confidence")))

        # qual
        if reg.get("qual_keys"):
            q = f.get("qual")
            if not q:
                errors.append("%s :: missing qual (needs %s)" % (where, reg["qual_keys"]))
            else:
                for k in reg["qual_keys"]:
                    if k not in q:
                        errors.append("%s :: qual missing key %s" % (where, k))
                for k, allowed in (reg.get("qual_values") or {}).items():
                    if k in q and q[k] not in allowed:
                        errors.append("%s :: qual %s=%r not in %s" % (where, k, q[k], allowed))
        else:
            if f.get("qual"):
                errors.append("%s :: qual given but registry has no qual_keys" % where)

        # type
        t = reg.get("type")
        v = f.get("value")
        if t == "number" and not isinstance(v, (int, float)):
            if not (isinstance(v, str) and v.strip()):
                errors.append("%s :: number expected, got %r" % (where, v))
            else:
                warns.append("%s :: number field holds string %r" % (where, v[:40]))
        if t == "integer" and not isinstance(v, int):
            errors.append("%s :: integer expected, got %r" % (where, v))
        if t == "bool" and not isinstance(v, bool):
            errors.append("%s :: bool expected, got %r" % (where, v))
        if t == "enum":
            allowed = reg.get("values") or []
            if v not in allowed:
                errors.append("%s :: enum %r not in %s" % (where, v, allowed))
        if t == "date":
            import datetime
            ok = isinstance(v, (str, int, datetime.date))
            if isinstance(v, str) and len(v) < 4:
                ok = False
            if not ok:
                errors.append("%s :: date bad %r" % (where, v))

        # valid
        val = f.get("valid") or {}
        if "from" not in val:
            errors.append("%s :: valid.from missing" % where)
        if "to" not in val and not f.get("note") and not d.get("open_ended_note"):
            errors.append("%s :: valid.to open and no note" % where)

        # src
        if not f.get("src"):
            errors.append("%s :: no src" % where)

print("ERRORS %d" % len(errors))
for e in errors:
    print("  E", e)
print("WARNS %d" % len(warns))
for w in warns:
    print("  W", w)
