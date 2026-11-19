import sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DEST = os.path.join(ROOT, "public", "img", "ships")
for n in ("bismarck-1940-bow-anchor", "bismarck-1940-superstructure", "bismarck-1940-unfinished"):
    im = Image.open(os.path.join(DEST, n + ".jpg"))
    im.resize((im.width * 2, im.height * 2), Image.LANCZOS).save(os.path.join(HERE, "z-" + n + ".jpg"), quality=92)
    print(n, im.size)
