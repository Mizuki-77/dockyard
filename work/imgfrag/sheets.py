import sys, os, io, json, textwrap
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
PREV = os.path.join(HERE, "prev")
idx = {int(k): v for k, v in json.load(open(os.path.join(HERE, "prev-index.json"), encoding="utf-8")).items()}

CELL = 400
PAD = 14
LABEL = 40
COLS = 4


def short(t):
    t = t.replace("File:", "").replace(".jpg", "").replace(".JPG", "")
    t = t.replace("Bundesarchiv Bild ", "BA ")
    t = t.replace("Schlachtschiff Bismarck", "Bismarck")
    t = t.replace(", Schlachtschiff Bismarck", "")
    return t


def sheet(keys, out):
    rows = (len(keys) + COLS - 1) // COLS
    W = COLS * (CELL + PAD) + PAD
    H = rows * (CELL + PAD + LABEL) + PAD
    canvas = Image.new("RGB", (W, H), (20, 20, 20))
    d = ImageDraw.Draw(canvas)
    for n, k in enumerate(keys):
        p = os.path.join(PREV, "%02d.jpg" % k)
        im = Image.open(p)
        iw, ih = im.size
        im = im.convert("RGB")
        im.thumbnail((CELL, CELL))
        x = PAD + (n % COLS) * (CELL + PAD)
        y = PAD + (n // COLS) * (CELL + PAD + LABEL)
        canvas.paste(im, (x, y))
        lines = textwrap.wrap("#%d %s" % (k, short(idx[k])), 46)[:2]
        for li, ln in enumerate(lines):
            d.text((x + 3, y + CELL + 3 + li * 11), ln, fill=(255, 225, 120))
    canvas.save(out, quality=88)
    print(out, canvas.size, len(keys))


ks = sorted(idx)
for i in range(0, len(ks), 16):
    sheet(ks[i:i + 16], os.path.join(HERE, "named-%d.jpg" % (i // 16 + 1)))
