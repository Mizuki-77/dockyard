import sys, os, io, json, time, urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, "..", "..", "public", "img", "ships"))

TITLES = [
    "File:Battleship Bismarck burning and sinking 1941.jpg",
    "File:An aerial reconnaissance photograph of Alten Fjord showing the German battleship TIRPITZ at her anchorage.jpg",
]
# cache 只按标题存，之前用 500 抓过，必须清掉再按 1280 重取
cache = meta.load_cache()
for t in TITLES:
    cache.pop(t, None)
meta.save_cache(cache)

d = meta.api({"action": "query", "titles": "|".join(TITLES), "prop": "imageinfo",
              "iiprop": "url|size|extmetadata", "iiurlwidth": 1280})
names = {
 "File:Battleship Bismarck burning and sinking 1941.jpg": "bismarck-1941-sinking.jpg",
 "File:An aerial reconnaissance photograph of Alten Fjord showing the German battleship TIRPITZ at her anchorage.jpg":
     "tirpitz-1943-altenfjord-reconnaissance.jpg",
}
opener = urllib.request.build_opener(urllib.request.ProxyHandler({"http": meta.PROXY, "https": meta.PROXY}))
for pg in d["query"]["pages"]:
    t = pg["title"]
    ii = pg["imageinfo"][0]
    name = names[t]
    dst = os.path.join(OUT, name)
    for a in range(4):
        try:
            req = urllib.request.Request(ii["thumburl"], headers={"User-Agent": meta.UA})
            with opener.open(req, timeout=180) as r:
                open(dst, "wb").write(r.read())
            break
        except Exception as e:
            print("retry", name, str(e)[:60]); time.sleep(5)
    time.sleep(1.0)
    print(name, Image.open(dst).size, os.path.getsize(dst), "| origin", ii["width"], ii["height"])
    print("   thumb:", ii["thumburl"][:120])
