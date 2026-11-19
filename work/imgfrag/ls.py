import sys, os, io, json, re, html
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta

SHORT = [
    # bismarck
    "File:Bundesarchiv Bild 193-B30-5-32, Schlachtschiff Bismarck, Schrauben.jpg",
    "File:Bundesarchiv Bild 193-36-3-18A, Schlachtschiff Bismarck, Antriebswelle.jpg",
    "File:Bundesarchiv Bild 101II-MN-1396-04, Kiel, Schlachtschiff Bismarck am Kai.jpg",
    "File:Bundesarchiv Bild 101II-MW-5562-29A, Schlachtschiff Bismarck, Bau.jpg",
    "File:Bundesarchiv Bild 193-05-3-37, Schlachtschiff Bismarck.jpg",
    "File:Bundesarchiv Bild 193-13-4-32, Schlachtschiff Bismarck.jpg",
    "File:Bundesarchiv Bild 193-13-6-34, Schlachtschiff Bismarck.jpg",
    "File:Bundesarchiv Bild 193-04-3-03, Schlachtschiff Bismarck.jpg",
    "File:Bundesarchiv Bild 193-06-7-20, Schlachtschiff Bismarck.jpg",
    "File:Bundesarchiv Bild 193-08-3-22, Schlachtschiff Bismarck.jpg",
    "File:Bundesarchiv Bild 193-03-5-18, Schlachtschiff Bismarck.jpg",
    "File:Bundesarchiv Bild 146-1968-015-25, Schlachtschiff Bismarck, Seegefecht.jpg",
    "File:El acorazado Bismarck y la bandera nazi.jpg",
    "File:Early Bismarck.jpg",
    "File:The Royal Navy during the Second World War A4386.jpg",
    "File:The Royal Navy during the Second World War A9798.jpg",
    "File:Rodney firing on Bismarck.png",
    # tirpitz
    "File:Battleship Tirpitz off Kiel Sept 1941.jpg",
    "File:Tirpitz trials 1941 h59668.jpg",
    "File:Tirpitz1940.jpg",
    "File:Bundesarchiv Bild 121-1429, Drontheim-Fjord, Schlachtschiff \"Tirpitz\".jpg",
    "File:Bundesarchiv Bild 183-J19316, Norwegen, Schlachtschiff, Zerstörer.jpg",
    "File:Bundesarchiv DVM 10 Bild-23-63-40, Schlachtschiff \"Tirpitz\", Stapellauf.jpg",
    "File:\"Tirpitz\" i Fættenfjorden (14535516382).jpg",
    "File:\"Tirpitz\" i Fættenfjorden (17301883111).jpg",
    "File:Cañones del acorazado Tirpitz.jpg",
    "File:German battleship Tirpitz partly covered by a smokescreen at Kaafjord A22634.jpg",
    "File:German battleship Tirpitz evading torpedoes during Operation Sportpalast.jpg",
    "File:Fleet Air Arm attack the battleship Tirpitz.jpg",
    "File:Battlehip Tirpitz capsized at Tromso c1944.jpg",
    "File:Tromsö, Royal Air Force Bomber Command, 1942-1945 CL2830.jpg",
    "File:Tirpitz at Tromso fjord in November 1944.JPG",
    "File:Dramatic End of the Tirpitz C4775.jpg",
    "File:Tirpitz Norway h71318.jpg",
    "File:Tirpitz-1.jpg",
]


def clean(s):
    if not s:
        return ""
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"QS:P571,.*", "", s)
    return re.sub(r"\s+", " ", s).strip()


res = meta.show(SHORT, fields=("LicenseShortName", "License", "UsageTerms", "Artist", "Credit",
                               "DateTimeOriginal", "ImageDescription", "Attribution", "ObjectName"))
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "short-meta.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

for r in res:
    print("=== " + r["title"].replace("File:", ""))
    print("  size=%sx%s" % (r.get("w"), r.get("h")))
    print("  lic=%s" % clean(r.get("LicenseShortName")))
    print("  licRaw=%s" % clean(r.get("License"))[:160])
    print("  usage=%s" % clean(r.get("UsageTerms"))[:100])
    print("  artist=%s" % clean(r.get("Artist"))[:90])
    print("  credit=%s" % clean(r.get("Credit"))[:120])
    print("  attr=%s" % clean(r.get("Attribution"))[:90])
    print("  date=%s" % clean(r.get("DateTimeOriginal"))[:50])
