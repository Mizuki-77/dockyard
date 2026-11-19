import json, sys, os, urllib.request, urllib.parse

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
PROXY = "http://127.0.0.1:7897"
API = "https://commons.wikimedia.org/w/api.php"


def _opener(proxy):
    if proxy:
        return urllib.request.build_opener(urllib.request.ProxyHandler({"http": PROXY, "https": PROXY}))
    return urllib.request.build_opener()


def api(params, proxy=True, retries=3):
    params = dict(params)
    params.setdefault("format", "json")
    params.setdefault("formatversion", "2")
    url = API + "?" + urllib.parse.urlencode(params)
    last = None
    for _ in range(retries):
        for px in ([True, False] if proxy else [False]):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA})
                with _opener(px).open(req, timeout=90) as r:
                    return json.loads(r.read().decode("utf-8"))
            except Exception as e:
                last = e
    raise last


def catfiles(cat, limit=500):
    out, cont = [], None
    while True:
        p = {"action": "query", "list": "categorymembers", "cmtitle": cat,
             "cmtype": "file", "cmlimit": "500"}
        if cont:
            p["cmcontinue"] = cont
        d = api(p)
        out += [m["title"] for m in d.get("query", {}).get("categorymembers", [])]
        cont = d.get("continue", {}).get("cmcontinue")
        if not cont or len(out) >= limit:
            break
    return out


def info(titles, width=1280):
    res = []
    for i in range(0, len(titles), 40):
        chunk = titles[i:i + 40]
        d = api({"action": "query", "titles": "|".join(chunk), "prop": "imageinfo",
                 "iiprop": "url|size|extmetadata|mime", "iiurlwidth": width})
        for pg in d.get("query", {}).get("pages", []):
            ii = (pg.get("imageinfo") or [{}])[0]
            res.append({"title": pg.get("title"), "info": ii})
    return res


def search(q, limit=100):
    out, off = [], 0
    while len(out) < limit:
        d = api({"action": "query", "list": "search", "srsearch": q,
                 "srnamespace": "6", "srlimit": "50", "sroffset": off})
        hits = d.get("query", {}).get("search", [])
        out += [h["title"] for h in hits]
        if "continue" not in d:
            break
        off = d["continue"]["sroffset"]
    return out[:limit]


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    mode = sys.argv[1]
    if mode == "cat":
        for c in sys.argv[2:]:
            f = catfiles(c)
            print("== %s (%d)" % (c, len(f)))
            for x in f:
                print("  " + x)
    elif mode == "search":
        for q in sys.argv[2:]:
            f = search(q)
            print("== %s (%d)" % (q, len(f)))
            for x in f:
                print("  " + x)
