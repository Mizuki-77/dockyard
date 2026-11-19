import sys, os, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DEST = os.path.join(ROOT, "public", "img", "ships")

T = ["File:Cañones del acorazado Tirpitz.jpg",
     "File:Battleship Tirptiz in Kaafjord during May 1943.JPG",
     "File:Tirpitz at Tromso fjord in November 1944.JPG"]
d = meta.api({"action": "query", "titles": "|".join(T), "prop": "categories|imageinfo",
              "cllimit": "max", "iiprop": "url|size|extmetadata", "iiurlwidth": 1280})
for pg in d["query"]["pages"]:
    print("=" * 70)
    print(pg["title"])
    print("  size:", ((pg.get("imageinfo") or [{}])[0]).get("width"), ((pg.get("imageinfo") or [{}])[0]).get("height"))
    print("  cats:", [c["title"] for c in pg.get("categories", [])])
    em = ((pg.get("imageinfo") or [{}])[0]).get("extmetadata") or {}
    for f in ("ImageDescription", "DateTimeOriginal", "LicenseShortName", "Artist", "Credit", "ObjectName"):
        v = (em.get(f) or {}).get("value")
        if v:
            v = re.sub(r"<[^>]+>", " ", str(v)); v = re.sub(r"\s+", " ", v)
            print("  ", f, ":", v[:300])

# zoom the kaafjord aerial
im = Image.open(os.path.join(DEST, "tirpitz-1943-kaafjord-aerial.jpg"))
im.resize((im.width * 3, im.height * 3), Image.LANCZOS).save(os.path.join(HERE, "z-kaafjord.jpg"), quality=92)
print("zoom", im.size)
