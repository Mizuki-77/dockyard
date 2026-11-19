import sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta

T = [
    "File:Bundesarchiv Bild 193-04-4-19A, Schlachtschiff Bismarck.jpg",
    "File:Bundesarchiv Bild 193-02-6-17, Schlachtschiff Bismarck.jpg",
    "File:Bundesarchiv Bild 193-03-1-06, Schlachtschiff Bismarck.jpg",
    "File:Bundesarchiv Bild 193-B30-5-32, Schlachtschiff Bismarck, Schrauben.jpg",
]
import re
for r in meta.show(T, fields=("ImageDescription", "DateTimeOriginal", "LicenseShortName", "Artist", "Credit", "UsageTerms")):
    print("=" * 70)
    print(r["title"])
    for k in ("DateTimeOriginal", "LicenseShortName", "Artist", "Credit", "UsageTerms", "ImageDescription"):
        v = r.get(k)
        if v:
            v = re.sub(r"<[^>]+>", " ", str(v))
            v = re.sub(r"\s+", " ", v)
            print("  ", k, ":", v[:260])
