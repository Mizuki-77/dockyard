import sys, json, time
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import midway_api as m

files = ["_meta_mid_battle.json", "_meta_mid_ships.json",
         "_meta_mid_air.json", "_meta_mid_extra.json"]
titles, seen = [], set()
for fn in files:
    for e in json.load(open(fn, encoding="utf-8")):
        t = e.get("title")
        if t and t not in seen:
            seen.add(t); titles.append(t)

res = {}
CH = 20
for i in range(0, len(titles), CH):
    chunk = titles[i:i + CH]
    d = m.api({"action": "query", "titles": "|".join(chunk), "prop": "imageinfo",
               "iiprop": "url|size|extmetadata|mime"})
    for pg in d.get("query", {}).get("pages", []):
        ii = (pg.get("imageinfo") or [{}])[0]
        em = ii.get("extmetadata", {}) or {}
        def g(k):
            v = em.get(k) or {}
            return v.get("value")
        res[pg.get("title")] = {
            "license_short": g("LicenseShortName"),
            "license": g("License"),
            "usage": g("UsageTerms"),
            "attr_req": g("AttributionRequired"),
            "copyrighted": g("Copyrighted"),
            "restrictions": g("Restrictions"),
        }
    print("chunk", i, "->", len(res))
    time.sleep(4)

json.dump(res, open("_licenses.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

from collections import Counter
c = Counter((v or {}).get("license") for v in res.values())
print(c)
