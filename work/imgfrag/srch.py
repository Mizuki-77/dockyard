import sys, os, time, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import api

qs = [
    "Operation Catechism Tirpitz",
    "Tirpitz capsized Tromso",
    "Tirpitz wreck 1945",
    "Bismarck wreck bow 1941",
    "Bismarck 1941 stern",
    "Tirpitz camouflage 1942",
    "Tirpitz torpedo tubes",
    "Bismarck catapult Arado",
    "Tirpitz anchor fjord",
    "Bismarck machinery propeller screw",
]
for q in qs:
    try:
        f = api.search(q, 40)
    except Exception as e:
        print("ERR", q, e)
        continue
    print("== " + q)
    for x in f:
        print("   " + x.replace("File:", ""))
    time.sleep(1.5)
