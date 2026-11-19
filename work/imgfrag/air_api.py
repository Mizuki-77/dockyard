"""Commons API helpers for the aircraft image pass (urllib + local proxy)."""
import json, os, time, urllib.request, urllib.parse

UA = "DockyardArchive/1.0 (educational; contact@example.org)"
PROXY = "http://127.0.0.1:7897"
API = "https://commons.wikimedia.org/w/api.php"
HERE = os.path.dirname(os.path.abspath(__file__))


def _opener(proxy):
    if proxy:
        h = urllib.request.ProxyHandler({"http": PROXY, "https": PROXY})
        return urllib.request.build_opener(h)
    return urllib.request.build_opener()


def api(params, proxy=True, retries=4):
    p = dict(params)
    p.setdefault("format", "json")
    p.setdefault("formatversion", "2")
    url = API + "?" + urllib.parse.urlencode(p)
    last = None
    delay = 1.5
    for _ in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with _opener(proxy).open(req, timeout=90) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            last = e
            time.sleep(delay)
            delay = min(delay * 2, 20)
    raise last


def subcats(cat):
    out, cont = [], None
    while True:
        p = {"action": "query", "list": "categorymembers", "cmtitle": cat,
             "cmtype": "subcat", "cmlimit": "500"}
        if cont:
            p["cmcontinue"] = cont
        d = api(p)
        out += [m["title"] for m in d.get("query", {}).get("categorymembers", [])]
        cont = d.get("continue", {}).get("cmcontinue")
        if not cont:
            break
    return out


def catfiles(cat, limit=2000):
    out, cont = [], None
    while len(out) < limit:
        p = {"action": "query", "list": "categorymembers", "cmtitle": cat,
             "cmtype": "file", "cmlimit": "500"}
        if cont:
            p["cmcontinue"] = cont
        d = api(p)
        out += [m["title"] for m in d.get("query", {}).get("categorymembers", [])]
        cont = d.get("continue", {}).get("cmcontinue")
        if not cont:
            break
    return out


def info(titles, width=1280):
    res = []
    for i in range(0, len(titles), 25):
        chunk = titles[i:i + 25]
        d = api({"action": "query", "titles": "|".join(chunk), "prop": "imageinfo",
                 "iiprop": "url|size|extmetadata|mime", "iiurlwidth": width})
        for pg in d.get("query", {}).get("pages", []):
            res.append({"title": pg.get("title"),
                        "info": (pg.get("imageinfo") or [None])[0]})
        time.sleep(0.6)
    return res


def short(titles, width=1280):
    """Compact records: title, license short name, usage terms, artist, credit, date, size."""
    out = []
    for rec in info(titles, width):
        ii = rec["info"]
        if not ii:
            out.append({"title": rec["title"], "err": "no imageinfo"})
            continue
        em = ii.get("extmetadata") or {}
        g = lambda k: (em.get(k) or {}).get("value")
        out.append({
            "title": rec["title"],
            "w": ii.get("width"), "h": ii.get("height"),
            "lic": g("LicenseShortName"), "terms": g("UsageTerms"),
            "artist": g("Artist"), "credit": g("Credit"),
            "date": g("DateTimeOriginal"),
            "desc": (g("ImageDescription") or "")[:400],
            "page": ii.get("descriptionurl"),
            "thumb": ii.get("thumburl"),
        })
    return out


def download(url, dest, proxy=True):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with _opener(proxy).open(req, timeout=180) as r:
        data = r.read()
    if len(data) < 3000:
        raise RuntimeError("too small: %d bytes" % len(data))
    with open(dest, "wb") as f:
        f.write(data)
    return len(data)
