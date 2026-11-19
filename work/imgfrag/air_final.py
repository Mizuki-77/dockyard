import sys, os, json, re, html
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from air_api import info

TITLES = [
 "File:Swordfish on HMS Victorious before strike on Bismarck.jpg",
 "File:The Royal Navy during the Second World War A18270.jpg",
 "File:The Royal Navy during the Second World War A7977.jpg",
 "File:The Royal Navy during the Second World War A7279.jpg",
 "File:The Royal Navy during the Second World War A6974.jpg",
 "File:ZZZ 003915 E Gladiator.jpg",
 "File:A Chance-Vought Corsair landing aboard HMS ILLUSTRIOUS, December 1943. A20997.jpg",
 "File:The Royal Navy during the Second World War A23036.jpg",
 "File:Avenger being armed on HMS Illustrious (87) 1944.jpg",
 "File:The Royal Navy during the Second World War A25377.jpg",
 "File:The Royal Navy during the Second World War A100.jpg",
 "File:The Royal Navy during the Second World War A9272.jpg",
 "File:The Royal Navy during the Second World War A6654.jpg",
 "File:The Royal Navy during the Second World War A22229.jpg",
 "File:Arado Ar 196 aboard the German battleship Gneisenau, circa in 1940 (NH 83610).jpg",
 "File:German Arado Ar 196A-3 on the catapult of a German warship, circa in 1942 (NH 71324).jpg",
 "File:Fairey Flycatcher 1923.jpg",
 "File:Fairey Flycatcher.jpg",
 "File:HMS Furious-19.jpg",
]

def clean(s):
    if not s:
        return ""
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()

rows = []
for rec in info(TITLES, width=1280):
    ii = rec["info"]
    em = (ii or {}).get("extmetadata") or {}
    g = lambda k: clean((em.get(k) or {}).get("value"))
    rows.append({
        "title": rec["title"],
        "w": (ii or {}).get("width"), "h": (ii or {}).get("height"),
        "lic": g("LicenseShortName"), "terms": g("UsageTerms"),
        "artist": g("Artist"), "credit": g("Credit"),
        "date": g("DateTimeOriginal"), "desc": g("ImageDescription"),
        "page": (ii or {}).get("descriptionurl"),
    })
out = os.path.join(HERE, "final-meta.json")
json.dump(rows, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("wrote", out, len(rows))
