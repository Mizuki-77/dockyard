import sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
picks = ["34", "0", "32", "2", "70", "14", "74",
         "47", "40", "48", "49", "45", "58", "50", "56", "53", "54", "51"]
cell_w, cell_h = 460, 330
cols = 3
rows = (len(picks) + cols - 1) // cols
sheet = Image.new("RGB", (cols * cell_w, rows * cell_h), (20, 20, 20))
d = ImageDraw.Draw(sheet)
for i, n in enumerate(picks):
    p = os.path.join(HERE, "prev", n.zfill(2) + ".jpg")
    im = Image.open(p).convert("RGB")
    im.thumbnail((cell_w - 10, cell_h - 26))
    x = (i % cols) * cell_w + (cell_w - im.width) // 2
    y = (i // cols) * cell_h + 22
    sheet.paste(im, (x, y))
    d.text(((i % cols) * cell_w + 8, (i // cols) * cell_h + 5), "#" + n, fill=(255, 215, 70))
out = os.path.join(HERE, "check-final.jpg")
sheet.save(out, quality=88)
print(out, sheet.size)
