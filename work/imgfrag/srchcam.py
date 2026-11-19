import sys, os, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta

for q in ("Bismarck Baltic camouflage stripes 1941",
          "Bismarck Gotenhafen camouflage",
          "Schlachtschiff Bismarck Tarnanstrich"):
    try:
        d = meta.api({"action": "query", "list": "search", "srsearch": q,
                      "srnamespace": "6", "srlimit": "12"})
        print("=" * 60)
        print(q)
        for r in d.get("query", {}).get("search", []):
            print("   ", r["title"])
    except Exception as e:
        print(q, "ERR", e)
