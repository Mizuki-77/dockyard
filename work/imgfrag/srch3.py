import sys, os, io, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import api

for q in ['Bismarck Schlachtschiff Turm', 'Bismarck 38 cm turret', 'Tirpitz bow', 'Tirpitz Turm Anton']:
    try:
        hits = api.search(q, 30)
    except Exception as e:
        print("ERR", q, str(e)[:50]); time.sleep(6); continue
    print("== " + q)
    for h in hits:
        n = h.replace("File:", "")
        if n.lower().endswith(".pdf"):
            continue
        print("   " + n)
    time.sleep(3)
