import sys, os, io, yaml
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DEST = os.path.join(ROOT, "public", "img", "ships")
path = os.path.join(HERE, "img-ships-german.yaml")

doc = yaml.safe_load(open(path, encoding="utf-8"))
rows = doc["images"]
print("parsed OK, entries =", len(rows))

PARTS = set("turret barbette conning_tower funnel mast bridge superstructure hull_side hull_bottom deck aircraft_handling catapult crane propeller rudder anchor boat funnel_uptake other".split())
VIEWS = set("bow stern broadside deck overhead detail underwater other".split())
LI = {"pd", "cc0", "cc_by", "cc_by_sa", "non_commercial", "editorial_only", "unknown", "prohibited"}
FIELDS = ["id", "file", "subject", "title", "part", "view", "date", "license", "license_tier",
          "license_raw", "author", "credit", "source_url", "width", "height"]

ids, bad = [], 0
prim = {}
for r in rows:
    e = []
    for f in FIELDS:
        if f not in r:
            e.append("missing " + f)
    if r.get("subject") not in ("ship:bismarck", "ship:tirpitz"):
        e.append("bad subject " + str(r.get("subject")))
    if r.get("part") and r["part"] not in PARTS:
        e.append("bad part " + r["part"])
    if r.get("view") and r["view"] not in VIEWS:
        e.append("bad view " + r["view"])
    if r.get("license") not in LI:
        e.append("bad license " + str(r.get("license")))
    if r.get("license_tier") not in ("A", "B", "C"):
        e.append("bad tier")
    if r.get("license_tier") == "C":
        e.append("C TIER FORBIDDEN")
    if not isinstance(r.get("title"), dict) or "zh" not in r["title"] or "en" not in r["title"]:
        e.append("bad title")
    if r.get("primary"):
        prim[r["subject"]] = prim.get(r["subject"], 0) + 1
    fp = os.path.join(DEST, os.path.basename(r["file"]))
    if not os.path.exists(fp):
        e.append("FILE MISSING")
    else:
        w, h = Image.open(fp).size
        if (w, h) != (r["width"], r["height"]):
            e.append(f"PIXEL MISMATCH record {r['width']}x{r['height']} actual {w}x{h}")
    if r["id"] in ids:
        e.append("dup id")
    ids.append(r["id"])
    flag = "OK " if not e else "!! "
    if e:
        bad += 1
    print(f"{flag}{r['id']:36s} {r['subject']:14s} {str(r['date']):12s} {r['part']:14s} {r['view']:10s} {r['license_tier']} {r['license']:9s} {r['width']}x{r['height']}")
    for x in e:
        print("      ->", x)

print()
print("primary flags:", prim or "(none — 不抢已有 primary)")
print("bad entries:", bad)
bys = {}
for r in rows:
    bys.setdefault(r["subject"], []).append(r["id"])
for k, v in bys.items():
    print(k, len(v), v)
