import sys, os, io, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta

for cat in ("Category:Bismarck (ship, 1939)", "Category:Operation Rheinübung", "Category:Last battle of the battleship Bismarck"):
    try:
        d = meta.api({"action": "query", "list": "categorymembers", "cmtitle": cat,
                      "cmtype": "file", "cmlimit": "500"})
        mem = [m["title"] for m in d.get("query", {}).get("categorymembers", [])]
        print("=" * 60)
        print(cat, len(mem))
        for m in mem:
            print("   ", m)
    except Exception as e:
        print(cat, "ERR", e)
    time.sleep(1.5)
