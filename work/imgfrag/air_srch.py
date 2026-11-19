import sys, os
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from air_api import api

queries = [
    'insource:"Flycatcher" insource:"Hood"',
    'insource:"Fairey IIIF" insource:"Hood"',
    'insource:"Swordfish" insource:"Illustrious"',
    'flycatcher Hood',
    'Fairey IIIF Hood',
    'Arado 196 Tirpitz',
    'Arado Ar 196 Scharnhorst',
    'Seafox catapult',
]
for q in queries:
    try:
        d = api({"action": "query", "list": "search", "srsearch": q,
                 "srnamespace": "6", "srlimit": "25"})
        hits = d.get("query", {}).get("search", [])
    except Exception as e:
        print("== %s ERR %s" % (q, e)); continue
    print("== %s (%d)" % (q, len(hits)))
    for h in hits:
        print("   " + h["title"])
