import sys, os, io, time, json, urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta

HERE = os.path.dirname(os.path.abspath(__file__))
UA = meta.UA
PROXY = meta.PROXY
opener = urllib.request.build_opener(urllib.request.ProxyHandler({"http": PROXY, "https": PROXY}))

EXTRA = {
 "70": "File:Bundesarchiv Bild 193-05-2-07A, Schlachtschiff Bismarck.jpg",
 "71": "File:Bundesarchiv Bild 193-01-4-25, Schlachtschiff Bismarck.jpg",
 "72": "File:Bundesarchiv Bild 193-02-4-39, Schlachtschiff Bismarck.jpg",
 "73": "File:Bundesarchiv Bild 193-19-1-26, Schlachtschiff Bismarck.jpg",
 "74": "File:Bundesarchiv Bild 193-04-4-16A, Schlachtschiff Bismarck.jpg",
 "75": "File:Bundesarchiv Bild 193-05-3-37, Schlachtschiff Bismarck.jpg",
}
cache = meta.meta(list(EXTRA.values()), width=700)
idx = json.load(open(os.path.join(HERE, "prev-index.json"), encoding="utf-8"))
for k, t in EXTRA.items():
    ii = cache.get(t)
    if not ii:
        print("MISS", t); continue
    idx[k] = t
    url = ii.get("thumburl")
    dst = os.path.join(HERE, "prev", k + ".jpg")
    if os.path.exists(dst):
        print("skip", k); continue
    for a in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with opener.open(req, timeout=120) as r, open(dst, "wb") as f:
                f.write(r.read())
            print("ok", k, t[:60])
            break
        except Exception as e:
            print("retry", k, str(e)[:40]); time.sleep(5)
    time.sleep(1.5)

json.dump(idx, open(os.path.join(HERE, "prev-index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
