import json, sys, os, time, urllib.request, urllib.parse

UA = ("DockyardImageBot/1.0 (https://dockyard.example; contact@example.org) "
      "python-urllib/3.14")
PROXY = "http://127.0.0.1:7897"
API = "https://commons.wikimedia.org/w/api.php"
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "meta-cache.json")


def _opener(proxy):
    if proxy:
        return urllib.request.build_opener(urllib.request.ProxyHandler({"http": PROXY, "https": PROXY}))
    return urllib.request.build_opener()


def api(params, proxy=True, retries=6):
    params = dict(params)
    params.setdefault("format", "json")
    params.setdefault("formatversion", "2")
    url = API + "?" + urllib.parse.urlencode(params)
    last = None
    delay = 2.0
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with _opener(proxy).open(req, timeout=90) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            last = e
            time.sleep(delay)
            delay = min(delay * 2, 30)
    raise last


def load_cache():
    if os.path.exists(CACHE):
        with open(CACHE, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_cache(c):
    with open(CACHE, "w", encoding="utf-8") as f:
        json.dump(c, f, ensure_ascii=False, indent=1)


def meta(titles, width=1280):
    cache = load_cache()
    todo = [t for t in titles if t not in cache]
    for i in range(0, len(todo), 25):
        chunk = todo[i:i + 25]
        d = api({"action": "query", "titles": "|".join(chunk), "prop": "imageinfo",
                 "iiprop": "url|size|extmetadata|mime", "iiurlwidth": width})
        norm = {}
        for n in d.get("query", {}).get("normalized", []):
            norm[n["to"]] = n["from"]
        got = set()
        for pg in d.get("query", {}).get("pages", []):
            t = pg.get("title")
            ii = (pg.get("imageinfo") or [None])[0]
            cache[t] = ii
            got.add(t)
        for t in chunk:
            tt = t
            if tt not in cache and tt.replace("_", " ") in cache:
                continue
            if tt not in cache:
                cache[tt] = None
        save_cache(cache)
        time.sleep(1.2)
    return cache


def show(titles, fields=("LicenseShortName", "Artist", "Credit", "DateTimeOriginal", "ImageDescription", "UsageTerms")):
    cache = meta(titles)
    out = []
    for t in titles:
        ii = cache.get(t)
        rec = {"title": t}
        if not ii:
            rec["err"] = "missing"
            out.append(rec)
            continue
        rec["w"] = ii.get("width")
        rec["h"] = ii.get("height")
        rec["thumb"] = ii.get("thumburl")
        rec["page"] = ii.get("descriptionurl")
        em = ii.get("extmetadata") or {}
        for f in fields:
            v = (em.get(f) or {}).get("value")
            if v:
                rec[f] = v
        out.append(rec)
    return out


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    titles = [l.strip() for l in open(sys.argv[1], encoding="utf-8") if l.strip()]
    res = show(titles)
    print(json.dumps(res, ensure_ascii=False, indent=1))
