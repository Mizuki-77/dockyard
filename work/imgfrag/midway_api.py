import json, sys, time, os, urllib.request, urllib.parse, urllib.error

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
API = "https://commons.wikimedia.org/w/api.php"
OPENER = urllib.request.build_opener()   # 直连，不走代理


def api(params, retries=6):
    params = dict(params)
    params.setdefault("format", "json")
    params.setdefault("formatversion", "2")
    url = API + "?" + urllib.parse.urlencode(params)
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with OPENER.open(req, timeout=90) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            last = e
            if e.code == 429:
                time.sleep(12 + attempt * 6)
                continue
            time.sleep(3)
        except Exception as e:
            last = e
            time.sleep(3)
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
        time.sleep(2)
    return out


def search(q, limit=60):
    out, off = [], 0
    while len(out) < limit:
        d = api({"action": "query", "list": "search", "srsearch": q,
                 "srnamespace": "6", "srlimit": "50", "sroffset": off})
        out += [h["title"] for h in d.get("query", {}).get("search", [])]
        if "continue" not in d:
            break
        off = d["continue"].get("sroffset", 0)
        time.sleep(2)
    return out[:limit]


def info(titles, width=1280):
    res = []
    for i in range(0, len(titles), 25):
        chunk = titles[i:i + 25]
        d = api({"action": "query", "titles": "|".join(chunk), "prop": "imageinfo",
                 "iiprop": "url|size|extmetadata|mime", "iiurlwidth": width})
        for pg in d.get("query", {}).get("pages", []):
            ii = (pg.get("imageinfo") or [{}])[0]
            em = ii.get("extmetadata", {}) or {}
            res.append({
                "title": pg.get("title"),
                "url": ii.get("url"),
                "width": ii.get("width"),
                "height": ii.get("height"),
                "mime": ii.get("mime"),
                "desc_url": ii.get("descriptionurl"),
                "license": (em.get("LicenseShortName") or {}).get("value"),
                "license_url": (em.get("LicenseUrl") or {}).get("value"),
                "date": (em.get("DateTimeOriginal") or {}).get("value"),
                "desc": (em.get("ImageDescription") or {}).get("value"),
                "artist": (em.get("Artist") or {}).get("value"),
                "credit": (em.get("Credit") or {}).get("value"),
                "cats": (em.get("Categories") or {}).get("value"),
                "restrictions": (em.get("Restrictions") or {}).get("value"),
            })
        time.sleep(2)
    return res


def save(name, obj):
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), name)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    print("saved", p, len(obj) if hasattr(obj, "__len__") else "")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    mode = sys.argv[1]
    if mode == "cat":
        allf = []
        for c in sys.argv[2:]:
            f = catfiles(c)
            print("== %s (%d)" % (c, len(f)))
            for x in f:
                print("  " + x)
            allf += f
    elif mode == "search":
        for q in sys.argv[2:]:
            f = search(q)
            print("== %s (%d)" % (q, len(f)))
            for x in f:
                print("  " + x)
