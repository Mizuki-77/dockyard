import json, os, sys, time, urllib.parse, urllib.request

UA = ("DockyardArchive/1.0 (educational; contact: dockyard-site) "
      "python-urllib/3")
PROXY = "http://127.0.0.1:7897"
API = "https://commons.wikimedia.org/w/api.php"
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")


def _opener(proxy):
    if proxy:
        return urllib.request.build_opener(
            urllib.request.ProxyHandler({"http": PROXY, "https": PROXY}))
    return urllib.request.build_opener()


def api(params, proxy=True, retries=6):
    params = dict(params)
    params.setdefault("format", "json")
    params.setdefault("formatversion", "2")
    url = API + "?" + urllib.parse.urlencode(params)
    last = None
    for attempt in range(retries):
        for px in ([True, False] if proxy else [False]):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA})
                with _opener(px).open(req, timeout=90) as r:
                    time.sleep(1.2)
                    return json.loads(r.read().decode("utf-8"))
            except Exception as e:
                last = e
                time.sleep(3 + attempt * 4)
    raise last


def q(titles, width=1280, proxy=True):
    """imageinfo for up to 50 titles; returns dict title -> info dict."""
    out = {}
    if isinstance(titles, str):
        titles = [titles]
    for i in range(0, len(titles), 40):
        chunk = titles[i:i + 40]
        d = api({"action": "query", "titles": "|".join(chunk),
                 "prop": "imageinfo",
                 "iiprop": "url|size|extmetadata|mime|user",
                 "iiurlwidth": width}, proxy=proxy)
        for pg in d.get("query", {}).get("pages", []):
            ii = (pg.get("imageinfo") or [{}])[0]
            out[pg.get("title")] = ii
        for pg in d.get("query", {}).get("pages", []):
            pass
    return out


def cat(c, limit=500, proxy=True):
    out, cont = [], None
    while True:
        p = {"action": "query", "list": "categorymembers", "cmtitle": c,
             "cmtype": "file", "cmlimit": "500"}
        if cont:
            p["cmcontinue"] = cont
        d = api(p, proxy=proxy)
        out += [m["title"] for m in d.get("query", {}).get("categorymembers", [])]
        cont = d.get("continue", {}).get("cmcontinue")
        if not cont or len(out) >= limit:
            break
    return out


def srch(text, limit=60, proxy=True):
    out, off = [], 0
    while len(out) < limit:
        d = api({"action": "query", "list": "search", "srsearch": text,
                 "srnamespace": "6", "srlimit": "50", "sroffset": off},
                proxy=proxy)
        hits = d.get("query", {}).get("search", [])
        out += [h["title"] for h in hits]
        if "continue" not in d:
            break
        off = d["continue"]["sroffset"]
    return out[:limit]


def meta(ii):
    em = ii.get("extmetadata") or {}

    def g(k):
        v = em.get(k) or {}
        val = v.get("value")
        if isinstance(val, str):
            import re
            val = re.sub(r"<[^>]+>", "", val).strip()
        return val

    return {
        "title": None,
        "w": ii.get("width"), "h": ii.get("height"),
        "thumb_w": ii.get("thumbwidth"), "thumb_h": ii.get("thumbheight"),
        "url": ii.get("url"),
        "thumburl": ii.get("thumburl"),
        "descurl": ii.get("descriptionurl"),
        "licshort": g("LicenseShortName"),
        "usage": g("UsageTerms"),
        "licurl": g("LicenseUrl"),
        "artist": (g("Artist") or "")[:300],
        "credit": (g("Credit") or "")[:200],
        "datetime": g("DateTimeOriginal"),
        "desc": (g("ImageDescription") or "")[:600],
        "cats": (g("Categories") or "")[:200],
        "restrictions": g("Restrictions"),
        "attribution": (g("Attribution") or "")[:200],
        "copyrighted": g("Copyrighted"),
        "attributionrequired": g("AttributionRequired"),
    }
