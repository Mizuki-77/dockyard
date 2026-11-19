import sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta, time

for cat in ("Category:Tirpitz (ship, 1941)", "Category:Fættenfjorden", "Category:Operation Catechism"):
    d = meta.api({"action": "query", "list": "categorymembers", "cmtitle": cat,
                  "cmtype": "file", "cmlimit": "500"})
    mem = [m["title"] for m in d.get("query", {}).get("categorymembers", [])]
    print("=" * 60)
    print(cat, len(mem))
    for m in mem:
        print("   ", m)
    time.sleep(1.5)
