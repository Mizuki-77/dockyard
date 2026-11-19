import sys, os, json
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from air_api import api, download

ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(ROOT, "public", "img", "weapons")

PICKS = [
    # id, commons file title
    ("swordfish-hms-victorious-bismarck-strike", "File:Swordfish on HMS Victorious before strike on Bismarck.jpg"),
    ("swordfish-hms-activity-lift-wings-folded", "File:The Royal Navy during the Second World War A18270.jpg"),
    ("fulmar-hms-victorious-wings-folded", "File:The Royal Navy during the Second World War A7977.jpg"),
    ("fulmar-hms-victorious-hangar-row", "File:The Royal Navy during the Second World War A7279.jpg"),
    ("fulmar-hms-victorious-ranged-deck", "File:The Royal Navy during the Second World War A5950.jpg"),
    ("sea-gladiator-hms-victorious-landing", "File:The Royal Navy during the Second World War A6974.jpg"),
    ("sea-gladiator-malta-faith-n5520", "File:ZZZ 003915 E Gladiator.jpg"),
    ("corsair-hms-illustrious-landing-1943", "File:A Chance-Vought Corsair landing aboard HMS ILLUSTRIOUS, December 1943. A20997.jpg"),
    ("corsair-hms-victorious-wings-folding", "File:The Royal Navy during the Second World War A23036.jpg"),
    ("corsair-hms-illustrious-hangar", "File:Corsairs in hanger on Illustrious IWM A24278.jpg"),
    ("avenger-hms-illustrious-bombing-up", "File:Avenger being armed on HMS Illustrious (87) 1944.jpg"),
    ("avenger-hms-trumpeter-catapult", "File:The Royal Navy during the Second World War A25377.jpg"),
    ("walrus-hms-prince-of-wales-catapult-deck", "File:A Supermarine Walrus amphibious aircraft being hoisted from the catapult deck of HMS PRINCE OF WALES.jpg"),
    ("walrus-hms-mauritius-catapult", "File:The Royal Navy during the Second World War A9272.jpg"),
    ("walrus-hms-rodney-catapult-hoist", "File:The Royal Navy during the Second World War A100.jpg"),
    ("seafox-hms-canton-alighting", "File:The Royal Navy during the Second World War A6654.jpg"),
    ("seafox-fitters-at-work", "File:The Royal Navy during the Second World War A22229.jpg"),
    ("arado-196-gneisenau-aboard", "File:Arado Ar 196 aboard the German battleship Gneisenau, circa in 1940 (NH 83610).jpg"),
    ("arado-196-catapult-admiral-scheer", "File:German Arado Ar 196A-3 on the catapult of a German warship, circa in 1942 (NH 71324).jpg"),
    ("flycatcher-1923", "File:Fairey Flycatcher 1923.jpg"),
    ("flycatcher-401-flight-hms-eagle", "File:Fairey Flycatcher.jpg"),
    ("fairy-iiif-hms-furious-landing", "File:HMS Furious-19.jpg"),
]

def thumb(title, width=1280):
    d = api({"action": "query", "titles": title, "prop": "imageinfo",
             "iiprop": "url|size", "iiurlwidth": width})
    pg = d["query"]["pages"][0]
    ii = pg["imageinfo"][0]
    u = ii.get("thumburl") or ii["url"]
    return u.split("?")[0], ii.get("thumbwidth"), ii.get("thumbheight")

if __name__ == "__main__":
    only = sys.argv[1:]
    for pid, title in PICKS:
        if only and pid not in only:
            continue
        try:
            u, tw, th = thumb(title)
        except Exception as e:
            print("THUMB FAIL %s: %s" % (pid, e)); continue
        dest = os.path.join(OUT, pid + ".jpg")
        try:
            n = download(u, dest)
            print("OK  %-46s %6d B  %s  %sx%s" % (pid, n, u.split("/")[-1][:40], tw, th))
        except Exception as e:
            print("DL FAIL %s: %s" % (pid, e))
