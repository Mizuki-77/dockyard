import sys, os, io, yaml
sys.stdout.reconfigure(encoding="utf-8")
from PIL import Image

ROOT = r"D:\deepseek harness\website-warships"
FRAG = os.path.join(ROOT, "work", "imgfrag", "img-weapons-2.yaml")
MAIN = os.path.join(ROOT, "data", "images.yaml")
out = []
ok = True

raw = open(FRAG, encoding="utf-8").read()
frag = yaml.safe_load(raw)
out.append("YAML parse: OK (top-level keys: %s)" % list(frag.keys()))

REQ = ["id", "file", "subject", "title", "part", "view", "date", "license",
       "license_tier", "license_raw", "author", "credit", "source_url",
       "width", "height", "primary", "note"]
SUBJ = {"weapon:15in-42-mk1", "weapon:g7a-t1"}

main = yaml.safe_load(open(MAIN, encoding="utf-8"))["images"]
main_ids = {i["id"] for i in main}
out.append("data/images.yaml: %d images in registry" % len(main))

imgs = frag["images"]
out.append("fragment images: %d" % len(imgs))
seen = set()
for im in imgs:
    keys = list(im.keys())
    if keys != REQ:
        ok = False
        out.append("  [FAIL] %s field order/set mismatch: %s" % (im.get("id"), keys))
    missing = [k for k in REQ if k not in im]
    if missing:
        ok = False
        out.append("  [FAIL] %s missing fields %s" % (im.get("id"), missing))
    iid = im["id"]
    if iid in seen:
        ok = False
        out.append("  [FAIL] duplicate id inside fragment: %s" % iid)
    seen.add(iid)
    if iid in main_ids:
        ok = False
        out.append("  [FAIL] id collides with data/images.yaml: %s" % iid)
    if im["subject"] not in SUBJ:
        ok = False
        out.append("  [FAIL] bad subject: %s -> %s" % (iid, im["subject"]))
    if not isinstance(im.get("title"), dict) or set(im["title"].keys()) != {"zh", "en"}:
        ok = False
        out.append("  [FAIL] title not block mapping zh/en: %s" % iid)
    p = os.path.join(ROOT, "public", im["file"].lstrip("/").replace("/", os.sep))
    if not os.path.exists(p):
        ok = False
        out.append("  [FAIL] file missing: %s" % p)
        continue
    w, h = Image.open(p).size
    if (w, h) != (im["width"], im["height"]):
        ok = False
        out.append("  [FAIL] pixel mismatch %s: file %dx%d vs yaml %sx%s"
                   % (iid, w, h, im["width"], im["height"]))
    if im["primary"] not in (True, False):
        ok = False
        out.append("  [FAIL] primary not bool: %s" % iid)
    if im["license_tier"] == "B":
        n = im["note"]
        need = [im["author"], im["license_raw"],
                "creativecommons.org", "本站仅按站内统一宽度缩放", "未裁剪、未改作"]
        miss = [x for x in need if x not in n]
        if miss:
            ok = False
            out.append("  [FAIL] B-tier note missing %s (%s)" % (miss, iid))
    out.append("  [ok] %-38s %sx%s  tier %s  %d bytes"
               % (iid, w, h, im["license_tier"], os.path.getsize(p)))

by_subj = {}
for im in imgs:
    by_subj.setdefault(im["subject"], []).append(im["id"])
out.append("coverage: " + "; ".join("%s -> %d" % (k, len(v)) for k, v in sorted(by_subj.items())))
prim = [im["id"] for im in imgs if im["primary"]]
out.append("primary flags: %s" % prim)

out.append("")
out.append("RESULT: " + ("PASS" if ok else "FAIL"))
txt = "\n".join(out)
open(os.path.join(ROOT, "work", "imgfrag", "verify-weapons-2.txt"), "w", encoding="utf-8").write(txt)
print(txt)
