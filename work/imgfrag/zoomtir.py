import sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DEST = os.path.join(ROOT, "public", "img", "ships")
for n, s in (("tirpitz-1942-faettenfjord-aerial", 2), ("tirpitz-1942-sportpalast", 2),
             ("tirpitz-1942-faettenfjord", 2), ("tirpitz-1942-drontheimfjord", 2)):
    im = Image.open(os.path.join(DEST, n + ".jpg"))
    im.resize((im.width * s, im.height * s), Image.LANCZOS).save(os.path.join(HERE, "z-" + n + ".jpg"), quality=92)
    print(n, im.size)
