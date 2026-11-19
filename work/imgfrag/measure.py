import sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DEST = os.path.join(ROOT, "public", "img", "ships")
for fn in sorted(os.listdir(DEST)):
    if fn.startswith(("bismarck-19", "tirpitz-19")):
        p = os.path.join(DEST, fn)
        im = Image.open(p)
        print(f"{fn:44s} {im.size[0]:5d}x{im.size[1]:<5d} {im.format} {im.mode} {os.path.getsize(p)//1024}KB")
