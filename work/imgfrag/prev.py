import sys, os, io, json, urllib.request, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import meta

UA = meta.UA
PROXY = meta.PROXY
PREV = os.path.join(HERE, "prev")
os.makedirs(PREV, exist_ok=True)

LIST = [l.strip() for l in open(os.path.join(HERE, "prevlist.txt"), encoding="utf-8") if l.strip()]


def fetch(url, proxy=True, retries=4):
    last = None
    for _ in range(retries):
        try:
            op = urllib.request.build_opener(urllib.request.ProxyHandler({"http": PROXY, "https": PROXY})) if proxy else urllib.request.build_opener()
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Referer": "https://commons.wikimedia.org/"})
            with op.open(req, timeout=120) as r:
                return r.read()
        except Exception as e:
            last = e
            time.sleep(3)
    raise last


cache = meta.load_cache()
todo = [t for t in LIST if t not in cache]
if todo:
    meta.meta(todo, width=500)

cache = meta.load_cache()
idx = {}
for i, t in enumerate(LIST):
    ii = cache.get(t)
    if not ii:
        print("MISS", t)
        continue
    u = ii.get("thumburl") or ii.get("url")
    p = os.path.join(PREV, "%02d.jpg" % i)
    if os.path.exists(p) and os.path.getsize(p) > 1000:
        idx[i] = t
        continue
    try:
        b = fetch(u)
        open(p, "wb").write(b)
        idx[i] = t
        print("OK %02d %s %d" % (i, t.replace("File:", ""), len(b)))
    except Exception as e:
        print("FAIL %02d %s %s" % (i, t, str(e)[:80]))
    time.sleep(0.6)

json.dump(idx, open(os.path.join(HERE, "prev-index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
