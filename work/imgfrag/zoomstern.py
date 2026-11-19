import sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
p = os.path.join(ROOT, "public", "img", "ships", "bismarck-1940-stern-portholes.jpg")
im = Image.open(p)
print(im.size)
im.resize((im.width * 2, im.height * 2), Image.LANCZOS).save(os.path.join(HERE, "zoom-stern.jpg"), quality=92)
print("ok")
