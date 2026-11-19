import sys, os
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from air_api import subcats, catfiles, api

for c in sys.argv[1:]:
    try:
        subs = subcats(c)
    except Exception as e:
        subs = []
    try:
        files = catfiles(c, limit=400)
    except Exception as e:
        files = []
    print("== %s | subs=%d files=%d" % (c, len(subs), len(files)))
    for s in subs:
        print("   sub: " + s)
    for f in files[:80]:
        print("   f: " + f)
