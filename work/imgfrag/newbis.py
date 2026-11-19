import sys, os, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta

T = [
 'File:Battleship Bismarck burning and sinking 1941.jpg',
 'File:Battleship Bismarck under fire and burning 1941.jpg',
 'File:Bundesarchiv Bild 146-1984-055-14, Schlachtschiff Bismarck, nach Seegefecht.jpg',
 'File:Bundesarchiv Bild 146-1989-012-03, Schlachtschiff Bismarck in der Ostsee.jpg',
 'File:The Royal Navy during the Second World War A4301.jpg',
 'File:The Royal Navy during the Second World War A4386.jpg',
 'File:The Royal Navy during the Second World War A9798.jpg',
 "File:Battleship Bismarck's port side 15 cm gun.jpeg",
 'File:Bundesarchiv Bild 193-13-3-12, Schlachtschiff Bismarck.jpg',
 'File:Bundesarchiv Bild 193-13-3-13, Schlachtschiff Bismarck.jpg',
 'File:Bundesarchiv Bild 193-13-3-14, Schlachtschiff Bismarck.jpg',
 'File:Bundesarchiv Bild 193-13-5-09, Schlachtschiff Bismarck.jpg',
 'File:Bundesarchiv Bild 193-03-2-10, Schlachtschiff Bismarck.jpg',
 'File:Bundesarchiv Bild 193-03-6-05A, Schlachtschiff Bismarck.jpg',
 'File:Bundesarchiv Bild 193-04-2-10A, Schlachtschiff Bismarck.jpg',
 'File:Bundesarchiv Bild 193-04-2-12A, Schlachtschiff Bismarck.jpg',
 'File:Bundesarchiv Bild 193-04-5-25A, Schlachtschiff Bismarck.jpg',
 'File:Bundesarchiv Bild 193-06-7-16, Schlachtschiff Bismarck.jpg',
 'File:Bundesarchiv Bild 193-13-4-33, Schlachtschiff Bismarck.jpg',
 'File:Bundesarchiv Bild 193-13-6-35, Schlachtschiff Bismarck.jpg',
 'File:Bundesarchiv Bild 193-30-5-31A, Schlachtschiff Bismarck.jpg',
 'File:Bundesarchiv Bild 193-30-5-34A, Schlachtschiff Bismarck.jpg',
 'File:Bundesarchiv Bild 193-01-7-08A, Schlachtschiff Bismarck.jpg',
]
d = meta.api({"action": "query", "titles": "|".join(T), "prop": "categories|imageinfo",
              "cllimit": "max", "iiprop": "url|size|extmetadata"})
for pg in sorted(d["query"]["pages"], key=lambda p: p["title"]):
    print("=" * 70)
    print(pg["title"])
    ii = (pg.get("imageinfo") or [{}])[0]
    print("  size:", ii.get("width"), ii.get("height"))
    print("  lic:", ((ii.get("extmetadata") or {}).get("LicenseShortName") or {}).get("value"))
    print("  cats:", [c["title"].replace("Category:", "") for c in pg.get("categories", [])][:8])
    em = ii.get("extmetadata") or {}
    for f in ("ImageDescription", "DateTimeOriginal", "Artist", "Credit"):
        v = (em.get(f) or {}).get("value")
        if v:
            v = re.sub(r"<[^>]+>", " ", str(v)); v = re.sub(r"\s+", " ", v)
            print("  ", f, ":", v[:220])
