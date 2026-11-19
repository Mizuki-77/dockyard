import sys, os, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta

HERE = os.path.dirname(os.path.abspath(__file__))
idx = json.load(open(os.path.join(HERE, "prevnew.json"), encoding="utf-8"))
t = idx["14"]
print("TITLE:", t)
rows = meta.show([t], fields=("LicenseShortName", "Artist", "Credit", "DateTimeOriginal",
                              "ImageDescription", "UsageTerms", "AttributionRequired"))
for r in rows:
    print("w,h:", r["w"], r["h"], "| page:", r["page"])
    for k, v in r.items():
        if k in ("title", "w", "h", "thumb", "page"):
            continue
        print("  ", k, "=", v)
