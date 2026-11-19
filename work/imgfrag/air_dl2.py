import sys, os
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from air_api import api, download

ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(ROOT, "public", "img", "weapons")

TITLE = ("File:Corsair fighters and Fairey Barracuda torpedo bombers ranged on the flight deck of "
         "HMS FORMIDABLE off Norway in July 1944.jpg")
d = api({"action": "query", "titles": TITLE, "prop": "imageinfo",
         "iiprop": "url|size", "iiurlwidth": 1280})
ii = d["query"]["pages"][0]["imageinfo"][0]
u = (ii.get("thumburl") or ii["url"]).split("?")[0]
dest = os.path.join(OUT, "corsair-hms-formidable-ranged-deck.jpg")
n = download(u, dest)
print("OK", n, ii.get("thumbwidth"), ii.get("thumbheight"))
