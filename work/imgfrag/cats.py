import sys, os, io, json, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import api

T = [
 "File:German battleship Tirpitz evading torpedoes during Operation Sportpalast.jpg",
 "File:Battleship Tirptiz in Kaafjord during May 1943.JPG",
 "File:Fleet Air Arm attack the battleship Tirpitz.jpg",
 "File:Tirpitz at Tromso fjord in November 1944.JPG",
 "File:Battlehip Tirpitz capsized at Tromso c1944.jpg",
 "File:German battleship Tirpitz partly covered by a smokescreen at Kaafjord A22634.jpg",
 "File:Cañones del acorazado Tirpitz.jpg",
 "File:Bundesarchiv Bild 193-05-3-37, Schlachtschiff Bismarck.jpg",
]
for t in T:
    try:
        d = api.api({"action": "query", "titles": t, "prop": "categories", "cllimit": "50"})
        cats = []
        for pg in d.get("query", {}).get("pages", []):
            cats = [c["title"].replace("Category:", "") for c in pg.get("categories", [])]
        print("==", t[:70])
        print("   ", " | ".join(cats)[:400])
    except Exception as e:
        print("ERR", t[:40], str(e)[:60])
    time.sleep(2)
