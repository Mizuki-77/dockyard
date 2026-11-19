import sys, os
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from air_api import api

TITLES = [
 "File:The Royal Navy during the Second World War A7279.jpg",
 "File:The Royal Navy during the Second World War A7977.jpg",
 "File:The Royal Navy during the Second World War A6974.jpg",
 "File:The Royal Navy during the Second World War A23036.jpg",
 "File:The Royal Navy during the Second World War A25377.jpg",
 "File:The Royal Navy during the Second World War A18270.jpg",
 "File:The Royal Navy during the Second World War A100.jpg",
 "File:The Royal Navy during the Second World War A9272.jpg",
 "File:The Royal Navy during the Second World War A6654.jpg",
 "File:The Royal Navy during the Second World War A22229.jpg",
]
for t in TITLES:
    d = api({"action": "query", "titles": t, "prop": "categories", "cllimit": "500"})
    pg = d["query"]["pages"][0]
    cats = [c["title"].replace("Category:", "") for c in pg.get("categories", [])]
    keep = [c for c in cats if any(k in c for k in
            ("194", "193", "IWM", "Imperial War", "Royal Navy", "Aircraft", "Fleet Air Arm", "Seaplane"))]
    print("### " + t)
    for c in keep:
        print("   - " + c)
    print()
