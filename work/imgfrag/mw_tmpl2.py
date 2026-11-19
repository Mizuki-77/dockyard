import sys, json, re, time
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import midway_api as m

raw = {}
for fn in ["_meta_mid_battle.json", "_meta_mid_ships.json",
           "_meta_mid_air.json", "_meta_mid_extra.json"]:
    for e in json.load(open(fn, encoding="utf-8")):
        raw[e["title"]] = e

titles = sorted(raw)
extra = {}
CH = 12
for i in range(0, len(titles), CH):
    chunk = titles[i:i + CH]
    d = m.api({"action": "query", "titles": "|".join(chunk), "prop": "revisions",
               "rvprop": "content", "rvslots": "main"})
    for pg in d.get("query", {}).get("pages", []):
        t = pg.get("title")
        try:
            wt = pg["revisions"][0]["slots"]["main"]["content"]
        except Exception:
            wt = ""
        lic = re.search(r"license\s*=\s*([A-Za-z0-9\-\.]+)", wt)
        nhhc = re.search(r"\{\{\s*NHHC\s*\|\s*([^|]+)", wt)
        extra[t] = {
            "license_param": lic.group(1) if lic else "",
            "nhhc_id": nhhc.group(1).strip() if nhhc else "",
        }
    time.sleep(3)

json.dump(extra, open("_extra_lic.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
n = sum(1 for v in extra.values() if v["license_param"])
print("with license param:", n, "of", len(extra))
for t, v in list(extra.items())[:5]:
    print(t[:60], v)
