import sys, json, io
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, "work/imgfrag")
from api import catfiles, search, info, api

mode = sys.argv[1]
out = []
if mode == "cat":
    for c in sys.argv[2:]:
        try:
            f = catfiles(c, limit=300)
        except Exception as e:
            f = ["ERR " + str(e)]
        out.append("== %s (%d)" % (c, len(f)))
        out += ["  " + x for x in f]
    print("\n".join(out))
elif mode == "search":
    for q in sys.argv[2:]:
        f = search(q, limit=60)
        out.append("== %s (%d)" % (q, len(f)))
        out += ["  " + x for x in f]
    print("\n".join(out))
