import sys, os, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta

HERE = os.path.dirname(os.path.abspath(__file__))
idx = json.load(open(os.path.join(HERE, "prevnew.json"), encoding="utf-8"))
want = ["12", "13", "15", "16", "17"]
rows = meta.show([idx[k] for k in want], fields=("LicenseShortName", "Artist", "Credit",
                                                 "DateTimeOriginal", "ImageDescription", "UsageTerms"))
for k, r in zip(want, rows):
    print("#" + k, r["title"], r["w"], "x", r["h"])
    print("   page:", r["page"])
    for f in ("LicenseShortName", "Artist", "Credit", "DateTimeOriginal", "ImageDescription", "UsageTerms"):
        print("   ", f, "=", r.get(f, ""))
    print()
