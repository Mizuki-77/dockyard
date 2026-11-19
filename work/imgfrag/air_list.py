import sys, os, json
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from air_api import catfiles, short

targets = sys.argv[1:]
allrows = {}
for c in targets:
    files = catfiles(c, limit=4000)
    print("== %s files=%d" % (c, len(files)))
    rows = short(files)
    allrows[c] = rows
    for r in rows:
        if r.get("err"):
            print("  [ERR] " + r["title"]); continue
        print("  %s | %sx%s | %s | %s | %s" % (
            r["title"].replace("File:", ""), r["w"], r["h"],
            (r["lic"] or "?")[:26], (r["date"] or "")[:22],
            (r["desc"] or "").replace("\n", " ")[:150]))
    print()
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "air-dump.json"), "a", encoding="utf-8") as f:
    f.write(json.dumps(allrows, ensure_ascii=False) + "\n")
