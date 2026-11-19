import sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
picks = ["70", "71", "72", "73", "74", "75"]
cell_w, cell_h = 520, 400
cols, rows = 2, 3
sheet = Image.new("RGB", (cols * cell_w, rows * cell_h), (20, 20, 20))
d = ImageDraw.Draw(sheet)
for i, n in enumerate(picks):
    p = os.path.join(HERE, "prev", n + ".jpg")
    im = Image.open(p).convert("RGB")
    im.thumbnail((cell_w - 10, cell_h - 30))
    x = (i % cols) * cell_w + (cell_w - im.width) // 2
    y = (i // cols) * cell_h + 24
    sheet.paste(im, (x, y))
    d.text(((i % cols) * cell_w + 8, (i // cols) * cell_h + 6), "#" + n, fill=(255, 220, 80))
out = os.path.join(HERE, "check-turret.jpg")
sheet.save(out, quality=90)
print(out, sheet.size)
