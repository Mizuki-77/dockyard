import sys, os, io, json, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta

T = [
 'File:Tirpitz Anchored in the Alta Fjord, in northern Norway, protected by anti-torpedo nets (1943-1944). (51055432497).jpg',
 'File:Tirpitz leaving a Norwegian fjord, circa 1942. (51055380606).jpg',
 'File:Bundesarchiv Bild 183-J19316, Norwegen, Schlachtschiff, Zerstörer.jpg',
 'File:Battleship Tirptiz in Kaafjord during May 1943.JPG',
 'File:Bundesarchiv Bild 121-1429, Drontheim-Fjord, Schlachtschiff "Tirpitz".jpg',
]

def clean(s):
    if not s:
        return ""
    s = re.sub(r"<[^>]+>", " ", s)
    s = s.replace("&amp;", "&").replace("&quot;", '"').replace("&#39;", "'").replace("&nbsp;", " ")
    return re.sub(r"\s+", " ", s).strip()

for r in meta.show(T, fields=("LicenseShortName","Artist","Credit","DateTimeOriginal","ImageDescription","UsageTerms")):
    print("====", r["title"])
    print("  lic:", clean(r.get("LicenseShortName")), "|", clean(r.get("UsageTerms"))[:90])
    print("  artist:", clean(r.get("Artist"))[:120])
    print("  credit:", clean(r.get("Credit"))[:400])
    print("  date:", clean(r.get("DateTimeOriginal"))[:70])
    print("  size:", r.get("w"), "x", r.get("h"))
    print("  desc:", clean(r.get("ImageDescription"))[:500])
