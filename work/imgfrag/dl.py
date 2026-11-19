import sys, os, json, time, urllib.request
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import wapi
from PIL import Image

PROXY = "http://127.0.0.1:7897"
UA = "DockyardArchive/1.0 (educational)"
OUT = os.path.join(HERE, "cand")
os.makedirs(OUT, exist_ok=True)

titles = json.load(open(sys.argv[1], encoding="utf-8"))
tag = sys.argv[2]
res = wapi.q(titles, width=1280)
report = []
for i, t in enumerate(titles):
    ii = res.get(t) or {}
    url = ii.get("thumburl") or ii.get("url")
    if not url:
        report.append("%-2d %s -> NO URL" % (i, t))
        continue
    dest = os.path.join(OUT, "%s-%02d.jpg" % (tag, i))
    ok = False
    for attempt in range(5):
        try:
            op = urllib.request.build_opener(
                urllib.request.ProxyHandler({"http": PROXY, "https": PROXY}))
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with op.open(req, timeout=120) as r:
                data = r.read()
            open(dest, "wb").write(data)
            w, h = Image.open(dest).size
            report.append("%-2d %-8s %sx%s  %s" % (i, "%dKB" % (len(data) // 1024), w, h, t))
            ok = True
            break
        except Exception as e:
            time.sleep(5 + attempt * 6)
            last = e
    if not ok:
        report.append("%-2d FAIL %r %s" % (i, last, t))
    time.sleep(1.5)
open(os.path.join(HERE, "dl.txt"), "w", encoding="utf-8").write("\n".join(report))
print("\n".join(report))
