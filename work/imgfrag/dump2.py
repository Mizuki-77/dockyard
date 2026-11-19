import sys, json, os
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from api import catfiles, search, info, api

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "d.txt")
mode = sys.argv[1]
lines = []
if mode == "cat":
    for c in sys.argv[2:]:
        try:
            f = catfiles(c, limit=400)
        except Exception as e:
            f = ["ERR " + str(e)]
        lines.append("== %s (%d)" % (c, len(f)))
        lines += ["  " + x for x in f]
elif mode == "search":
    for q in sys.argv[2:]:
        f = search(q, limit=60)
        lines.append("== %s (%d)" % (q, len(f)))
        lines += ["  " + x for x in f]
elif mode == "catpage":
    # list subcategories too
    for c in sys.argv[2:]:
        d = api({"action": "query", "list": "categorymembers", "cmtitle": c,
                 "cmlimit": "500"})
        ms = d.get("query", {}).get("categorymembers", [])
        lines.append("== %s (%d)" % (c, len(ms)))
        lines += ["  %s %s" % (m["ns"], m["title"]) for m in ms]
open(OUT, "w", encoding="utf-8").write("\n".join(lines))
print("wrote", len(lines), "lines to", OUT)
