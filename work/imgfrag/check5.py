import sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
picks = ["01", "09", "11", "12", "13", "22", "33", "35"]
cell_w, cell_h = 520, 400
cols = 3
rows = (len(picks) + cols - 1) // cols
sheet = Image.new("RGB", (cols * cell_w, rows * cell_h), (20, 20, 20))
d = ImageDraw.Draw(sheet)
for i, n in enumerate(picks):
    p = os.path.join(HERE, "prev", n + ".jpg")
    if not os.path.exists(p):
        d.text(((i % cols) * cell_w + 8, (i // cols) * cell_h + 6), "#" + n + " MISSING", fill=(255, 80, 80))
        continue
    im = Image.open(p).convert("RGB")
    im.thumbnail((cell_w - 10, cell_h - 26))
    x = (i % cols) * cell_w + (cell_w - im.width) // 2
    y = (i // cols) * cell_h + 22
    sheet.paste(im, (x, y))
    d.text(((i % cols) * cell_w + 8, (i // cols) * cell_h + 5), "#" + n, fill=(255, 215, 70))
out = os.path.join(HERE, "check-extra.jpg")
sheet.save(out, quality=88)
print(out, sheet.size)
