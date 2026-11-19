import sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DEST = os.path.join(ROOT, "public", "img", "ships")
NAMES = ["bismarck-1940-bow-anchor", "bismarck-1940-kiel-quay-bow", "bismarck-1940-stern-portholes"]
CW, CH = 640, 520
sheet = Image.new("RGB", (CW * 3, CH), (20, 20, 20))
d = ImageDraw.Draw(sheet)
for i, n in enumerate(NAMES):
    im = Image.open(os.path.join(DEST, n + ".jpg"))
    im.thumbnail((CW - 8, CH - 26))
    sheet.paste(im, (i * CW + 4, 22))
    d.text((i * CW + 6, 6), n, fill=(255, 220, 120))
out = os.path.join(HERE, "zoom-bis.jpg")
sheet.save(out, quality=90)
print(out, sheet.size)
