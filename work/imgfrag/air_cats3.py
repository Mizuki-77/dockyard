import sys, os
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from air_api import api

TITLES = [
 "File:The Royal Navy during the Second World War A7279.jpg",
 "File:The Royal Navy during the Second World War A7977.jpg",
 "File:The Royal Navy during the Second World War A6974.jpg",
 "File:The Royal Navy during the Second World War A23036.jpg",
 "File:The Royal Navy during the Second World War A18270.jpg",
 "File:The Royal Navy during the Second World War A100.jpg",
 "File:The Royal Navy during the Second World War A9272.jpg",
 "File:The Royal Navy during the Second World War A6654.jpg",
 "File:The Royal Navy during the Second World War A22229.jpg",
 "File:The Royal Navy during the Second World War A25377.jpg",
 "File:Arado Ar 196 aboard the German battleship Gneisenau, circa in 1940 (NH 83610).jpg",
 "File:German Arado Ar 196A-3 on the catapult of a German warship, circa in 1942 (NH 71324).jpg",
 "File:Fairey Flycatcher 1923.jpg",
 "File:Fairey Flycatcher.jpg",
 "File:HMS Furious-19.jpg",
 "File:ZZZ 003915 E Gladiator.jpg",
 "File:Swordfish on HMS Victorious before strike on Bismarck.jpg",
 "File:Avenger being armed on HMS Illustrious (87) 1944.jpg",
 "File:A Supermarine Walrus amphibious aircraft being hoisted from the catapult deck of HMS PRINCE OF WALES.jpg",
 "File:Corsair fighters and Fairey Barracuda torpedo bombers ranged on the flight deck of HMS FORMIDABLE off Norway in July 1944.jpg",
]
for t in TITLES:
    d = api({"action": "query", "titles": t, "prop": "categories", "cllimit": "500"})
    pg = d["query"]["pages"][0]
    cats = sorted(c["title"].replace("Category:", "") for c in pg.get("categories", []))
    print("### " + t)
    if not cats:
        print("   (no categories)")
    for c in cats:
        print("   - " + c)
    print()
