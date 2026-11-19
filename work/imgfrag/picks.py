import sys, os, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta

PICKS = {
    # Bismarck
    "File:Bundesarchiv Bild 193-B30-5-32, Schlachtschiff Bismarck, Schrauben.jpg": "bismarck-propellers-1939",
    "File:Bundesarchiv Bild 193-30-5-31A, Schlachtschiff Bismarck.jpg": "bismarck-stern-rudder-1939",
    "File:Early Bismarck.jpg": "bismarck-unfinished-1940",
    "File:Bundesarchiv Bild 101II-MN-1396-04, Kiel, Schlachtschiff Bismarck am Kai.jpg": "bismarck-kiel-bow-1940",
    "File:Bundesarchiv Bild 193-03-1-06, Schlachtschiff Bismarck.jpg": "bismarck-bridge-1940",
    "File:Bundesarchiv Bild 193-04-4-19A, Schlachtschiff Bismarck.jpg": "bismarck-stern-1940",
    # Tirpitz
    "File:Bundesarchiv DVM 10 Bild-23-63-40, Schlachtschiff \"Tirpitz\", Stapellauf.jpg": "tirpitz-launch-1939",
    "File:Battleship Tirpitz off Kiel Sept 1941.jpg": "tirpitz-kiel-1941",
    "File:\"Tirpitz\" i Fættenfjorden (14535516382).jpg": "tirpitz-faettenfjord-1942",
    "File:\"Tirpitz\" i Fættenfjorden (17301883111).jpg": "tirpitz-faettenfjord-aerial-1942",
    "File:Tirpitz Anchored in the Alta Fjord, in northern Norway, protected by anti-torpedo nets (1943-1944). (51055432497).jpg": "tirpitz-antitorpedo-nets-1943",
    "File:Cañones del acorazado Tirpitz.jpg": "tirpitz-380mm-turret",
    "File:Tirpitz Crewmen on board the battleship, while she was moored in a Norwegian fjord, circa 1942-44. One of the ship's 380mm (15) gun turrets is trained abeam, and several camouflage floats are in the distance. (51055366666).jpg": "tirpitz-turret-abeam-1943",
    "File:Fleet Air Arm attack the battleship Tirpitz.jpg": "tirpitz-air-attack-1944",
    "File:Tirpitz at Tromso fjord in November 1944.JPG": "tirpitz-tromso-1944",
    "File:Battlehip Tirpitz capsized at Tromso c1944.jpg": "tirpitz-capsized-1944",
    "File:German battleship Tirpitz partly covered by a smokescreen at Kaafjord A22634.jpg": "tirpitz-smokescreen-kaafjord",
}

titles = list(PICKS)
res = meta.show(titles, fields=("LicenseShortName", "License", "Artist", "Credit",
                                "DateTimeOriginal", "ImageDescription", "UsageTerms", "Attribution"))
out = []
for r in res:
    key = PICKS.get(r["title"])
    r["key"] = key
    out.append(r)
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "picks-meta.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

import re
def clean(s):
    if not s:
        return ""
    s = re.sub(r"<[^>]+>", " ", s)
    s = s.replace("&amp;", "&").replace("&quot;", '"').replace("&#39;", "'").replace("&nbsp;", " ")
    return re.sub(r"\s+", " ", s).strip()

for r in out:
    print("----", r["key"], "|", r["title"])
    print("   lic:", clean(r.get("LicenseShortName")), "| usage:", clean(r.get("UsageTerms"))[:80])
    print("   artist:", clean(r.get("Artist"))[:150])
    print("   credit:", clean(r.get("Credit"))[:150])
    print("   date:", clean(r.get("DateTimeOriginal"))[:80])
    print("   size:", r.get("w"), "x", r.get("h"))
    print("   desc:", clean(r.get("ImageDescription"))[:200])
