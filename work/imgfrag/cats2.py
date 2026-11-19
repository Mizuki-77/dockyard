import sys, os, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta

T = [
    "File:Bundesarchiv Bild 193-04-4-19A, Schlachtschiff Bismarck.jpg",
    "File:Bundesarchiv Bild 193-04-4-20A, Schlachtschiff Bismarck.jpg",
]
d = meta.api({"action": "query", "titles": "|".join(T), "prop": "categories|imageinfo",
              "cllimit": "max", "iiprop": "url|size|extmetadata|mime", "iiurlwidth": 1280})
for pg in d["query"]["pages"]:
    print("=" * 70)
    print(pg["title"])
    print("  cats:", [c["title"] for c in pg.get("categories", [])])
    ii = (pg.get("imageinfo") or [{}])[0]
    print("  size:", ii.get("width"), ii.get("height"))
    em = ii.get("extmetadata") or {}
    for f in ("ImageDescription", "DateTimeOriginal", "LicenseShortName", "Artist"):
        v = (em.get(f) or {}).get("value")
        if v:
            import re
            v = re.sub(r"<[^>]+>", " ", str(v)); v = re.sub(r"\s+", " ", v)
            print("  ", f, ":", v[:200])
