import sys, os
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from air_api import subcats, catfiles

cats = [
    "Category:Fairey Swordfish",
    "Category:Fairey Fulmar",
    "Category:Gloster Sea Gladiator",
    "Category:Vought F4U Corsair",
    "Category:Grumman TBF Avenger",
    "Category:Supermarine Walrus",
    "Category:Fairey Seafox",
    "Category:Arado Ar 196",
    "Category:Fairey Flycatcher",
    "Category:Fairey III",
    "Category:Fairey IIIF",
]
for c in cats:
    try:
        subs = subcats(c)
    except Exception as e:
        subs = ["ERR %s" % e]
    try:
        files = catfiles(c, limit=4000)
    except Exception as e:
        files = []
    print("== %s | subs=%d files=%d" % (c, len(subs), len(files)))
    for s in subs:
        print("   sub: " + s)
