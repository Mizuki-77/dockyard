import sys, os
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from air_api import subcats, catfiles

for c in ["Category:HMS Hood (51)", "Category:Fairey III", "Category:Fleet Air Arm"]:
    try:
        subs = subcats(c)
    except Exception as e:
        subs = []
    try:
        files = catfiles(c, limit=600)
    except Exception as e:
        files = []
    print("== %s | subs=%d files=%d" % (c, len(subs), len(files)))
    for s in subs[:60]:
        print("   sub: " + s)
    for f in files:
        low = f.lower()
        if any(k in low for k in ["aircraft", "seaplane", "flycatcher", "fairey", "plane", "walrus", "iiif", "iii"]):
            print("   f: " + f)
