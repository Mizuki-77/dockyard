import sys, os, io, time, urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DEST = os.path.join(ROOT, "public", "img", "ships")

T = "File:Early Bismarck.jpg"
cache = meta.meta([T], width=1280)
ii = cache[T]
print("src", ii.get("width"), ii.get("height"), ii.get("thumburl")[:120])
opener = urllib.request.build_opener(urllib.request.ProxyHandler({"http": meta.PROXY, "https": meta.PROXY}))
for a in range(5):
    try:
        req = urllib.request.Request(ii["thumburl"], headers={"User-Agent": meta.UA})
        with opener.open(req, timeout=180) as r:
            data = r.read()
        open(os.path.join(DEST, "bismarck-1940-unfinished.jpg"), "wb").write(data)
        print("ok", len(data))
        break
    except Exception as e:
        print("retry", str(e)[:60]); time.sleep(5)
from PIL import Image
print(Image.open(os.path.join(DEST, "bismarck-1940-unfinished.jpg")).size)
