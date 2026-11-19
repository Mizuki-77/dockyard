import sys, time, io
import midway_api as m

buf = io.StringIO()

def w(s):
    buf.write(s + "\n")

CATS = [
    "Category:Battle of Midway",
    "Category:Battle of Midway (Japanese forces)",
    "Category:Battle of Midway (US forces)",
    "Category:Battle of Midway (US forces on Midway)",
    "Category:People of the Battle of Midway",
    "Category:Japanese military personnel of the Battle of Midway",
]

for r in CATS:
    d = m.api({"action": "query", "list": "categorymembers", "cmtitle": r,
               "cmlimit": "500", "cmtype": "subcat|file"})
    mem = d.get("query", {}).get("categorymembers", [])
    subs = [x["title"] for x in mem if x["title"].startswith("Category:")]
    files = [x["title"] for x in mem if not x["title"].startswith("Category:")]
    w("=== %s : %d subcats, %d files" % (r, len(subs), len(files)))
    for s in subs:
        w("  SUB " + s)
    for f in files:
        w("  FILE " + f)
    time.sleep(2)

with open("_mwcats.txt", "w", encoding="utf-8") as f:
    f.write(buf.getvalue())
print("ok", len(buf.getvalue()))
