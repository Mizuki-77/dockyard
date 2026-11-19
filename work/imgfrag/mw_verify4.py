import sys, json, time, urllib.request, urllib.error, urllib.parse

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


OP = urllib.request.build_opener(NoRedirect)

files = ["_meta_mid_battle.json", "_meta_mid_ships.json",
         "_meta_mid_air.json", "_meta_mid_extra.json"]
rows, seen = [], set()
for fn in files:
    for e in json.load(open(fn, encoding="utf-8")):
        t = e.get("title")
        if not t or t in seen:
            continue
        seen.add(t)
        rows.append(e)

out = open("_verify2.log", "w", encoding="utf-8")
res = {}
for i, e in enumerate(rows, 1):
    fname = e["title"][5:]
    u = "https://commons.wikimedia.org/wiki/Special:Redirect/file/" + urllib.parse.quote(fname.replace(" ", "_"))
    code, loc = None, None
    for attempt in range(4):
        try:
            r = OP.open(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=30)
            code = r.status
            break
        except urllib.error.HTTPError as ex:
            code = ex.code
            loc = ex.headers.get("Location")
            if ex.code in (429, 503):
                time.sleep(10); continue
            break
        except Exception:
            time.sleep(3)
    exists = code in (301, 302) and loc
    res[fname] = {"title": e["title"], "filename": fname,
                  "redirect": loc, "exists": bool(exists), "code": code}
    out.write("%s %s %s\n" % ("OK  " if exists else "MISS", code, fname[:80]))
    out.flush()
    time.sleep(0.25)

out.write("\ntotal %d exist %d\n" % (len(res), sum(1 for v in res.values() if v["exists"])))
out.close()
json.dump(res, open("_verify2.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("done", len(res), sum(1 for v in res.values() if v["exists"]))
