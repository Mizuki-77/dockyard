import sys, os, io, json, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
c = json.load(open(os.path.join(HERE, "meta-cache.json"), encoding="utf-8"))
for k in c:
    if "Cañones" in k or "acorazado" in k:
        ii = c[k]
        em = (ii or {}).get("extmetadata") or {}
        print(k, ii.get("width"), ii.get("height"))
        for f in ("LicenseShortName", "Artist", "Credit", "ImageDescription"):
            print("  ", f, "=", re.sub(r"<[^>]+>", " ", (em.get(f) or {}).get("value", ""))[:300])
