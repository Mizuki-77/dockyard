import sys, os, io, time, urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, "..", "..", "public", "img", "ships"))

JOBS = [
    ("File:Battleship Bismarck burning and sinking 1941.jpg", "bismarck-1941-sinking.jpg"),
    ("File:An aerial reconnaissance photograph of Alten Fjord showing the German battleship TIRPITZ at her anchorage.jpg",
     "tirpitz-1943-altenfjord-reconnaissance.jpg"),
]

cache = meta.meta([t for t, _ in JOBS], width=1280)
opener = urllib.request.build_opener(urllib.request.ProxyHandler({"http": meta.PROXY, "https": meta.PROXY}))
for title, name in JOBS:
    ii = cache[title]
    url = ii["thumburl"]
    dst = os.path.join(OUT, name)
    ok = False
    for a in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": meta.UA})
            with opener.open(req, timeout=180) as r:
                open(dst, "wb").write(r.read())
            ok = True
            break
        except Exception as e:
            print("retry", name, str(e)[:60]); time.sleep(5)
    time.sleep(1.0)
    if ok:
        print(name, Image.open(dst).size, os.path.getsize(dst), "src", ii.get("width"), ii.get("height"))
    else:
        print("FAILED", name)
