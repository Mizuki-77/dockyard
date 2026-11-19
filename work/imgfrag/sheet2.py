import sys, os, glob
sys.stdout.reconfigure(encoding="utf-8")
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
files = sorted(glob.glob(os.path.join(HERE, "cand", "*.jpg")))
if len(sys.argv) > 1:
    tag = sys.argv[1]
    files = [f for f in files if os.path.basename(f).startswith(tag)]
CELL_W = 620
cols = 2
imgs = []
for f in files:
    im = Image.open(f).convert("RGB")
    r = CELL_W / im.width
    im = im.resize((CELL_W, max(1, int(im.height * r))), Image.LANCZOS)
    imgs.append((os.path.basename(f), im))
rows = (len(imgs) + cols - 1) // cols
rowh = [max(im.height for _, im in imgs[i * cols:(i + 1) * cols]) + 26 for i in range(rows)]
sheet = Image.new("RGB", (CELL_W * cols, sum(rowh)), (30, 30, 30))
d = ImageDraw.Draw(sheet)
y = 0
for r in range(rows):
    x = 0
    for name, im in imgs[r * cols:(r + 1) * cols]:
        d.text((x + 4, y + 6), name, fill=(255, 220, 120))
        sheet.paste(im, (x, y + 24))
        x += CELL_W
    y += rowh[r]
out = os.path.join(HERE, "sheet-%s.jpg" % (sys.argv[2] if len(sys.argv) > 2 else "x"))
sheet.save(out, quality=88)
print(out, sheet.size)
