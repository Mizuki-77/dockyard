import sys, os, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, "prev")
idx = json.load(open(os.path.join(HERE, "prevnew.json"), encoding="utf-8"))
keys = sorted(idx, key=lambda k: int(k))
CW, CH, COLS = 420, 360, 4
rows = (len(keys) + COLS - 1) // COLS
sheet = Image.new("RGB", (CW * COLS, CH * rows), (24, 24, 24))
d = ImageDraw.Draw(sheet)
for n, k in enumerate(keys):
    fn = os.path.join(P, f"n{int(k):02d}.jpg")
    im = Image.open(fn)
    im.thumbnail((CW - 10, CH - 40))
    x = (n % COLS) * CW + (CW - im.width) // 2
    y = (n // COLS) * CH + 26
    sheet.paste(im, (x, y))
    d.text(((n % COLS) * CW + 6, (n // COLS) * CH + 4), f"#{k} {idx[k][5:40]}", fill=(255, 210, 110))
    d.text(((n % COLS) * CW + 6, (n // COLS) * CH + CH - 12), idx[k][40:95], fill=(150, 195, 255))
sheet.save(os.path.join(HERE, "sheet-new.jpg"), quality=88)
print("ok", sheet.size, len(keys))
