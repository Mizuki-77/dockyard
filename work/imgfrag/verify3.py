import sys, os, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta
T = ['File:"Tirpitz" i Fættenfjorden (14535516382).jpg',
     'File:"Tirpitz" i Fættenfjorden (17301883111).jpg',
     'File:Bundesarchiv Bild 121-1429, Drontheim-Fjord, Schlachtschiff "Tirpitz".jpg',
     'File:German battleship Tirpitz evading torpedoes during Operation Sportpalast.jpg']
d = meta.api({"action": "query", "titles": "|".join(T), "prop": "categories|imageinfo",
              "cllimit": "max", "iiprop": "url|size|extmetadata"})
for pg in d["query"]["pages"]:
    print("=" * 70)
    print(pg["title"])
    ii = (pg.get("imageinfo") or [{}])[0]
    print("  size:", ii.get("width"), ii.get("height"))
    print("  cats:", [c["title"] for c in pg.get("categories", [])])
    em = ii.get("extmetadata") or {}
    for f in ("ImageDescription", "DateTimeOriginal", "LicenseShortName", "Artist", "Credit", "ObjectName"):
        v = (em.get(f) or {}).get("value")
        if v:
            v = re.sub(r"<[^>]+>", " ", str(v)); v = re.sub(r"\s+", " ", v)
            print("  ", f, ":", v[:300])
