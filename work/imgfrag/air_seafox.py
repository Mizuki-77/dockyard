import sys, os
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from air_api import api

for q in ['Seafox', 'insource:"Seafox"', 'Fairey Seafox Ajax', 'Seafox floatplane']:
    try:
        d = api({"action": "query", "list": "search", "srsearch": q,
                 "srnamespace": "6", "srlimit": "30"})
        hits = d.get("query", {}).get("search", [])
    except Exception as e:
        print("== %s ERR %s" % (q, e)); continue
    print("== %s (%d)" % (q, len(hits)))
    for h in hits:
        print("   " + h["title"])
