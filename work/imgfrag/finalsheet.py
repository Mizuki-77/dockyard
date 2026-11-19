import sys, os, io, yaml
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DEST = os.path.join(ROOT, "public", "img", "ships")
rows = yaml.safe_load(open(os.path.join(HERE, "img-ships-german.yaml"), encoding="utf-8"))["images"]

CW, CH, COLS = 340, 300, 5
rows_n = (len(rows) + COLS - 1) // COLS
sheet = Image.new("RGB", (CW * COLS, CH * rows_n), (26, 26, 26))
d = ImageDraw.Draw(sheet)
for i, r in enumerate(rows):
    im = Image.open(os.path.join(DEST, os.path.basename(r["file"])))
    im.thumbnail((CW - 10, CH - 34))
    x = (i % COLS) * CW + (CW - im.width) // 2
    y = (i // COLS) * CH + 4
    sheet.paste(im, (x, y))
    d.text(((i % COLS) * CW + 6, (i // COLS) * CH + CH - 28), f"{i+1}. {r['id'][:34]}", fill=(255, 220, 120))
    d.text(((i % COLS) * CW + 6, (i // COLS) * CH + CH - 15), f"{r['part']} / {r['view']} / {r['license_tier']}", fill=(160, 200, 255))
out = os.path.join(HERE, "final-check.jpg")
sheet.save(out, quality=88)
print(out, sheet.size)
