import sys, os, glob
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from PIL import Image

ROOT = r"D:\deepseek harness\website-warships"
OUT = os.path.join(ROOT, "public", "img", "weapons")
for p in sorted(glob.glob(os.path.join(OUT, "*.jpg"))):
    n = os.path.basename(p)
    if not any(k in n for k in ["swordfish", "fulmar", "sea-gladiator", "corsair", "avenger",
                                "walrus", "seafox", "arado-196", "flycatcher", "fairy-iiif"]):
        continue
    with Image.open(p) as im:
        print("%-46s %5dx%-5d %s %8d B" % (n, im.width, im.height, im.format, os.path.getsize(p)))
