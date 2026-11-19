import sys, os, io, time, urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DEST = os.path.join(ROOT, "public", "img", "ships")

FILES = {
 "bismarck-1940-bow-anchor.jpg": "File:Bundesarchiv Bild 193-02-6-17, Schlachtschiff Bismarck.jpg",
 "bismarck-1940-hull-plate-rivets.jpg": "File:Bundesarchiv Bild 193-08-3-22, Schlachtschiff Bismarck.jpg",
}

cache = meta.meta(list(FILES.values()), width=1280)
opener = urllib.request.build_opener(urllib.request.ProxyHandler({"http": meta.PROXY, "https": meta.PROXY}))
for fn, t in FILES.items():
    ii = cache.get(t)
    if not ii:
        print("MISS", fn); continue
    print("srcsize", ii.get("width"), ii.get("height"), "thumb", ii.get("thumburl")[:110])
    for a in range(5):
        try:
            req = urllib.request.Request(ii["thumburl"], headers={"User-Agent": meta.UA})
            with opener.open(req, timeout=180) as r:
                data = r.read()
            with open(os.path.join(DEST, fn), "wb") as f:
                f.write(data)
            print("ok", fn, len(data))
            break
        except Exception as e:
            print("retry", fn, str(e)[:50]); time.sleep(4 + a * 3)
    time.sleep(1.5)
