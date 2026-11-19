import sys, os, io, json, re, time, urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DEST = os.path.join(ROOT, "public", "img", "ships")

TITLES = [
 "File:Bundesarchiv Bild 193-B30-5-32, Schlachtschiff Bismarck, Schrauben.jpg",
 "File:Bundesarchiv Bild 101II-MN-1396-04, Kiel, Schlachtschiff Bismarck am Kai.jpg",
 "File:Bundesarchiv Bild 193-05-2-07A, Schlachtschiff Bismarck.jpg",
 "File:Bundesarchiv Bild 193-03-1-06, Schlachtschiff Bismarck.jpg",
 "File:Bundesarchiv Bild 193-04-4-16A, Schlachtschiff Bismarck.jpg",
 "File:Bundesarchiv Bild 193-04-4-19A, Schlachtschiff Bismarck.jpg",
 "File:Bundesarchiv DVM 10 Bild-23-63-40, Schlachtschiff \"Tirpitz\", Stapellauf.jpg",
 "File:\"Tirpitz\" i Fættenfjorden (14535516382).jpg",
 "File:\"Tirpitz\" i Fættenfjorden (17301883111).jpg",
 "File:Bundesarchiv Bild 121-1429, Drontheim-Fjord, Schlachtschiff \"Tirpitz\".jpg",
 "File:Cañones del acorazado Tirpitz.jpg",
 "File:German battleship Tirpitz evading torpedoes during Operation Sportpalast.jpg",
 "File:Battleship Tirptiz in Kaafjord during May 1943.JPG",
 "File:Fleet Air Arm attack the battleship Tirpitz.jpg",
 "File:Tirpitz at Tromso fjord in November 1944.JPG",
 "File:Battlehip Tirpitz capsized at Tromso c1944.jpg",
 "File:German battleship Tirpitz partly covered by a smokescreen at Kaafjord A22634.jpg",
]

FILES = {
 "bismarck-1939-propellers.jpg": TITLES[0],
 "bismarck-1940-kiel-quay-bow.jpg": TITLES[1],
 "bismarck-1940-turret-anton.jpg": TITLES[2],
 "bismarck-1940-superstructure.jpg": TITLES[3],
 "bismarck-1940-catapult-crane.jpg": TITLES[4],
 "bismarck-1940-stern-portholes.jpg": TITLES[5],
 "tirpitz-1939-launch.jpg": TITLES[6],
 "tirpitz-1942-faettenfjord.jpg": TITLES[7],
 "tirpitz-1942-faettenfjord-aerial.jpg": TITLES[8],
 "tirpitz-1942-drontheimfjord.jpg": TITLES[9],
 "tirpitz-1944-380mm-turret.jpg": TITLES[10],
 "tirpitz-1942-sportpalast.jpg": TITLES[11],
 "tirpitz-1943-kaafjord-aerial.jpg": TITLES[12],
 "tirpitz-1944-operation-tungsten.jpg": TITLES[13],
 "tirpitz-1944-tromso.jpg": TITLES[14],
 "tirpitz-1945-capsized.jpg": TITLES[15],
 "tirpitz-1943-kaafjord-smokescreen.jpg": TITLES[16],
}

cache = meta.meta(TITLES, width=1280)
opener = urllib.request.build_opener(urllib.request.ProxyHandler({"http": meta.PROXY, "https": meta.PROXY}))

ok = 0
for fn, t in FILES.items():
    ii = cache.get(t)
    if not ii:
        print("MISS", fn); continue
    url = ii.get("thumburl")
    dst = os.path.join(DEST, fn)
    if os.path.exists(dst) and os.path.getsize(dst) > 20000:
        print("exists", fn); ok += 1; continue
    done = False
    for a in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": meta.UA})
            with opener.open(req, timeout=180) as r:
                data = r.read()
            with open(dst, "wb") as f:
                f.write(data)
            print("ok", fn, len(data), "src", ii.get("width"), ii.get("height"), "url_w", 1280)
            done = True
            break
        except Exception as e:
            print("retry", fn, str(e)[:50]); time.sleep(4 + a * 3)
    if done:
        ok += 1
    time.sleep(1.2)
print("done", ok, "/", len(FILES))
