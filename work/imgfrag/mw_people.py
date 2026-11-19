import sys, time, io
import midway_api as m

CATS = [
    "Category:Chūichi Nagumo",
    "Category:Isoroku Yamamoto",
    "Category:Raymond A. Spruance",
    "Category:Frank Jack Fletcher",
    "Category:Tamon Yamaguchi",
    "Category:Minoru Genda",
]

buf = io.StringIO()
for r in CATS:
    try:
        d = m.api({"action": "query", "list": "categorymembers", "cmtitle": r,
                   "cmlimit": "500", "cmtype": "subcat|file"})
    except Exception as e:
        buf.write("=== %s ERROR %s\n" % (r, e)); continue
    mem = d.get("query", {}).get("categorymembers", [])
    subs = [x["title"] for x in mem if x["title"].startswith("Category:")]
    files = [x["title"] for x in mem if not x["title"].startswith("Category:")]
    buf.write("=== %s : %d subcats, %d files\n" % (r, len(subs), len(files)))
    for s in subs:
        buf.write("  SUB " + s + "\n")
    for f in files:
        buf.write("  FILE " + f + "\n")
    time.sleep(2)

open("_mwpeople.txt", "w", encoding="utf-8").write(buf.getvalue())
print("ok")
