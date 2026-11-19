import sys, os, io, re, json, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta

T = [
 "File:Battlehip Tirpitz capsized at Tromso c1944.jpg",
 "File:Tirpitz at Tromso fjord in November 1944.JPG",
 "File:Tromsö, Royal Air Force Bomber Command, 1942-1945 CL2830.jpg",
 "File:Fleet Air Arm attack the battleship Tirpitz.jpg",
 "File:Cañones del acorazado Tirpitz.jpg",
 "File:Battleship Tirptiz in Kaafjord during May 1943.JPG",
 "File:\"Tirpitz\" i Fættenfjorden (14535516382).jpg",
]

d = meta.api({"action": "query", "titles": "|".join(T), "prop": "revisions",
              "rvprop": "content", "rvslots": "main"})
for pg in d.get("query", {}).get("pages", []):
    t = pg.get("title")
    rev = (pg.get("revisions") or [{}])[0]
    txt = (rev.get("slots", {}).get("main", {}) or {}).get("*", "")
    print("====", t)
    lic = re.findall(r"\{\{\s*([A-Za-z0-9\-\.\_ ]+?)\s*[\|\}]", txt)
    print("  templates:", ", ".join(dict.fromkeys(lic))[:400])
    print("  ---- first 700 chars ----")
    print(txt[:700].replace("\n", " | "))
    time.sleep(2)
