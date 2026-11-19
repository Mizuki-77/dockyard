import sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
picks = ["14", "74", "21", "02"]
cell_w, cell_h = 760, 540
cols, rows = 2, 2
sheet = Image.new("RGB", (cols * cell_w, rows * cell_h), (20, 20, 20))
d = ImageDraw.Draw(sheet)
for i, n in enumerate(picks):
    im = Image.open(os.path.join(HERE, "prev", n + ".jpg")).convert("RGB")
    im.thumbnail((cell_w - 10, cell_h - 26))
    x = (i % cols) * cell_w + (cell_w - im.width) // 2
    y = (i // cols) * cell_h + 22
    sheet.paste(im, (x, y))
    d.text(((i % cols) * cell_w + 8, (i // cols) * cell_h + 5), "#" + n, fill=(255, 215, 70))
out = os.path.join(HERE, "check-detail.jpg")
sheet.save(out, quality=90)
print(out, sheet.size)
