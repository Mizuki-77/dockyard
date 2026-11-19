import sys, os, io, time, json, urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, "prev")
os.makedirs(P, exist_ok=True)

T = [
 "File:Battleship Bismarck burning and sinking 1941.jpg",
 "File:The Royal Navy during the Second World War A4386.jpg",
 "File:The Royal Navy during the Second World War A9798.jpg",
 "File:Bundesarchiv Bild 193-13-3-12, Schlachtschiff Bismarck.jpg",
 "File:Bundesarchiv Bild 193-13-3-13, Schlachtschiff Bismarck.jpg",
 "File:Bundesarchiv Bild 193-13-3-14, Schlachtschiff Bismarck.jpg",
 "File:Bundesarchiv Bild 193-13-5-09, Schlachtschiff Bismarck.jpg",
 "File:Bundesarchiv Bild 193-13-4-33, Schlachtschiff Bismarck.jpg",
 "File:Bundesarchiv Bild 193-03-5-18, Schlachtschiff Bismarck.jpg",
 "File:Bundesarchiv Bild 193-06-7-16, Schlachtschiff Bismarck.jpg",
 "File:Bundesarchiv Bild 193-03-2-10, Schlachtschiff Bismarck.jpg",
 "File:Duits slagschip 'de Bismarck ' genoemd naar de kanselier Otto von Bismarck, SFA022801174.jpg",
 "File:Battleship Tirpitz off Kiel Sept 1941.jpg",
 "File:An aerial reconnaissance photograph of Alten Fjord showing the German battleship TIRPITZ at her anchorage.jpg",
 "File:A German Tug towing camouflage float into position to protect the German battleship Tirpitz, at Fættenfjord , Norway 1942. (50050504201).jpg",
 "File:Tirpitz (1941-1944) Camouflaged at her moorings at Alta fjord , Norway, during World War II (50050816347).jpg",
 "File:Tirpitz Norway h71318.jpg",
 "File:Tirpitz trials 1941 h59668.jpg",
]
cache = meta.meta(T, width=500)
idx = {}
opener = urllib.request.build_opener(urllib.request.ProxyHandler({"http": meta.PROXY, "https": meta.PROXY}))
for i, t in enumerate(T):
    ii = cache.get(t)
    if not ii:
        print("MISS", t); continue
    url = ii["thumburl"]
    fn = os.path.join(P, f"n{i:02d}.jpg")
    if not os.path.exists(fn):
        for a in range(4):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": meta.UA})
                with opener.open(req, timeout=120) as r:
                    open(fn, "wb").write(r.read())
                break
            except Exception as e:
                print("retry", i, str(e)[:50]); time.sleep(4)
        time.sleep(0.8)
    idx[i] = t
    print(i, t, Image.open(fn).size if os.path.exists(fn) else "FAIL")
json.dump(idx, open(os.path.join(HERE, "prevnew.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
