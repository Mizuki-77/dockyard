import sys, os, io, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import api

for q in ['Bismarck Tarnanstrich', 'Bismarck Ostsee 1941', 'Bismarck wreck', 'Bismarck Bug Anker']:
    try:
        hits = api.search(q, 40)
    except Exception as e:
        print("ERR", q, str(e)[:60]); time.sleep(8); continue
    print("== " + q)
    for h in hits:
        n = h.replace("File:", "")
        if n.lower().endswith((".pdf", ".djvu", ".svg")):
            continue
        print("   " + n)
    time.sleep(3)
