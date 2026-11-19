import sys, json, re, time
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import midway_api as m

raw = {}
for fn in ["_meta_mid_battle.json", "_meta_mid_ships.json",
           "_meta_mid_air.json", "_meta_mid_extra.json"]:
    for e in json.load(open(fn, encoding="utf-8")):
        raw[e["title"]] = e

titles = sorted(raw)
out = {}
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
        tmpl = re.findall(r"\{\{\s*(PD-[A-Za-z0-9\-\.]+|Cc-by[^}|]*|CC0[^}|]*)", wt, re.I)
        out[t] = sorted(set(x.strip() for x in tmpl))
    print("chunk", i, len(out)); time.sleep(3)

json.dump(out, open("_templates.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
c = Counter()
for v in out.values():
    for x in v:
        c[x] += 1
for k, v in c.most_common():
    print(v, k)
