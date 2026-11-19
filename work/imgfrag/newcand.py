import sys, os, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta

T = [
 'File:Lot-2275-14 (26820659176).jpg',
 'File:Lot-2275-59 (26585865410).jpg',
 'File:Lot-2275-60 (26254455253).jpg',
 'File:Lot-2275-61 (26585863110).jpg',
 'File:A German Tug towing camouflage float into position to protect the German battleship Tirpitz, at Fættenfjord , Norway 1942. (50050504201).jpg',
 'File:Tirpitz (AWM SUK14095).jpg',
 'File:Acorazado Tirpitz camuflado en Noruega.jpg',
 'File:An aerial reconnaissance photograph of Alten Fjord showing the German battleship TIRPITZ at her anchorage.jpg',
 'File:German Battleship Tirpitz.jpg',
 'File:Tirpitz (1941-1944) Camouflaged at her moorings at Alta fjord , Norway, during World War II (50050816347).jpg',
 'File:Willie Tait on the wreck of Tirpitz.jpg',
 'File:Bulkhead from the German battleship Tirpitz at RAF Museum Hendon in November 2011.jpg',
 'File:Tirpitz-2 b.jpg',
 'File:Tirpitz shell 01.jpg',
]
d = meta.api({"action": "query", "titles": "|".join(T), "prop": "categories|imageinfo",
              "cllimit": "max", "iiprop": "url|size|extmetadata"})
for pg in d["query"]["pages"]:
    print("=" * 70)
    print(pg["title"])
    ii = (pg.get("imageinfo") or [{}])[0]
    print("  size:", ii.get("width"), ii.get("height"))
    print("  cats:", [c["title"].replace("Category:", "") for c in pg.get("categories", [])])
    em = ii.get("extmetadata") or {}
    for f in ("ImageDescription", "DateTimeOriginal", "LicenseShortName", "Artist", "Credit"):
        v = (em.get(f) or {}).get("value")
        if v:
            v = re.sub(r"<[^>]+>", " ", str(v)); v = re.sub(r"\s+", " ", v)
            print("  ", f, ":", v[:280])
