import sys, os, json
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wapi

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "d.txt")
mode = sys.argv[1]
lines = []
try:
    if mode == "catpage":
        for c in sys.argv[2:]:
            d = wapi.api({"action": "query", "list": "categorymembers",
                          "cmtitle": c, "cmlimit": "500"})
            ms = d.get("query", {}).get("categorymembers", [])
            lines.append("== %s (%d)" % (c, len(ms)))
            lines += ["  ns%s %s" % (m["ns"], m["title"]) for m in ms]
    elif mode == "cat":
        for c in sys.argv[2:]:
            f = wapi.cat(c, limit=400)
            lines.append("== %s (%d)" % (c, len(f)))
            lines += ["  " + x for x in f]
    elif mode == "search":
        for t in sys.argv[2:]:
            f = wapi.srch(t, limit=50)
            lines.append("== %s (%d)" % (t, len(f)))
            lines += ["  " + x for x in f]
except Exception as e:
    lines.append("ERROR " + repr(e))
open(OUT, "w", encoding="utf-8").write("\n".join(lines))
print("ok", len(lines))
