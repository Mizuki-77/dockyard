import sys, os, io, time, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import api

for q in ["Tirpitz anti-torpedo net Alta fjord", "Tirpitz X craft damage 1943", "Tirpitz Kaa fjord 1944 camouflage net"]:
    try:
        hits = api.search(q, 25)
    except Exception as e:
        print("ERR", q, str(e)[:60])
        time.sleep(8)
        continue
    print("== " + q)
    for h in hits:
        print("   " + h.replace("File:", ""))
    time.sleep(3)
