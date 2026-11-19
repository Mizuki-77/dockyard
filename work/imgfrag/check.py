import sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
picks = ["0", "2", "4", "7", "14", "21"]
cell_w, cell_h = 420, 300
cols, rows = 3, 2
sheet = Image.new("RGB", (cols * cell_w, rows * cell_h), (18, 18, 18))
for i, n in enumerate(picks):
    p = os.path.join(HERE, "prev", n + ".jpg")
    im = Image.open(p).convert("RGB")
    im.thumbnail((cell_w - 8, cell_h - 8))
    x = (i % cols) * cell_w + (cell_w - im.width) // 2
    y = (i // cols) * cell_h + (cell_h - im.height) // 2
    sheet.paste(im, (x, y))
out = os.path.join(HERE, "check.jpg")
sheet.save(out, quality=88)
print(out, sheet.size)
