import sys, os, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meta
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DEST = os.path.join(ROOT, "public", "img", "ships")
for fn in ["bismarck-1940-bow-anchor.jpg", "bismarck-1940-hull-plate-rivets.jpg"]:
    im = Image.open(os.path.join(DEST, fn))
    print(fn, im.size, os.path.getsize(os.path.join(DEST, fn)) // 1024, "KB")

def clean(s):
    if not s: return ""
    s = re.sub(r"<[^>]+>", " ", s)
    s = s.replace("&amp;", "&")
    return re.sub(r"\s+", " ", s).strip()

T = ["File:Bundesarchiv Bild 193-02-6-17, Schlachtschiff Bismarck.jpg",
     "File:Bundesarchiv Bild 193-08-3-22, Schlachtschiff Bismarck.jpg",
     "File:Bundesarchiv Bild 193-05-2-07A, Schlachtschiff Bismarck.jpg",
     "File:Bundesarchiv Bild 193-03-1-06, Schlachtschiff Bismarck.jpg",
     "File:Bundesarchiv Bild 193-04-4-16A, Schlachtschiff Bismarck.jpg",
     "File:Bundesarchiv Bild 193-04-4-19A, Schlachtschiff Bismarck.jpg",
     "File:Bundesarchiv Bild 193-B30-5-32, Schlachtschiff Bismarck, Schrauben.jpg",
     "File:Bundesarchiv DVM 10 Bild-23-63-40, Schlachtschiff \"Tirpitz\", Stapellauf.jpg"]
for r in meta.show(T, fields=("LicenseShortName", "Artist", "DateTimeOriginal")):
    print(r["title"][:70], "|", clean(r.get("LicenseShortName")), "|", clean(r.get("Artist"))[:40], "|", clean(r.get("DateTimeOriginal"))[:40])
