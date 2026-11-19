import sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DEST = os.path.join(ROOT, "public", "img", "ships")

NEW = [
 "bismarck-1939-propellers.jpg", "bismarck-1940-kiel-quay-bow.jpg",
 "bismarck-1940-turret-anton.jpg", "bismarck-1940-superstructure.jpg",
 "bismarck-1940-catapult-crane.jpg", "bismarck-1940-stern-portholes.jpg",
 "tirpitz-1939-launch.jpg", "tirpitz-1942-faettenfjord.jpg",
 "tirpitz-1942-faettenfjord-aerial.jpg", "tirpitz-1942-drontheimfjord.jpg",
 "tirpitz-1944-380mm-turret.jpg", "tirpitz-1942-sportpalast.jpg",
 "tirpitz-1943-kaafjord-aerial.jpg", "tirpitz-1944-operation-tungsten.jpg",
 "tirpitz-1944-tromso.jpg", "tirpitz-1945-capsized.jpg",
 "tirpitz-1943-kaafjord-smokescreen.jpg",
]
cell_w, cell_h = 470, 350
cols = 3
rows = (len(NEW) + cols - 1) // cols
sheet = Image.new("RGB", (cols * cell_w, rows * cell_h), (20, 20, 20))
d = ImageDraw.Draw(sheet)
for i, fn in enumerate(NEW):
    im = Image.open(os.path.join(DEST, fn)).convert("RGB")
    im.thumbnail((cell_w - 10, cell_h - 30))
    x = (i % cols) * cell_w + (cell_w - im.width) // 2
    y = (i // cols) * cell_h + 26
    sheet.paste(im, (x, y))
    d.text(((i % cols) * cell_w + 6, (i // cols) * cell_h + 6), f"{i+1}. {fn[:40]}", fill=(255, 215, 70))
out = os.path.join(HERE, "verify-final.jpg")
sheet.save(out, quality=86)
print(out, sheet.size)
