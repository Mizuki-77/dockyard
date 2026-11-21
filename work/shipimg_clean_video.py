# 清理：.ogv 视频被当成图片下载了，以及检查其他非图片文件。
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / 'work' / 'shipimg'
OUT = ROOT / 'public' / 'img' / 'ships'

picked = json.load(io.open(WORK / 'picked.json', encoding='utf-8'))

# 硬剔除：标题里带 .ogv / .webm / .ogg 的（视频）
removed = []
for sid in list(picked.keys()):
    keep = []
    for e in picked[sid]:
        t = e['title'].lower()
        if any(t.endswith(ext) or ext + ' ' in t for ext in ['.ogv', '.webm', '.ogg', '.ogm']):
            p = OUT / e['name']
            if p.exists():
                p.unlink()
            removed.append((sid, e['name']))
        else:
            keep.append(e)
    picked[sid] = keep

print('剔除视频:')
for sid, n in removed:
    print(f'  {sid:<18} {n[:60]}')

io.open(WORK / 'picked.json', 'w', encoding='utf-8').write(
    json.dumps(picked, ensure_ascii=False, indent=2))

# 同时检查磁盘上有没有非 JPEG 的扩展
print()
print('=== 磁盘上的 -extra- 文件是否都是 jpg ===')
import os
bad = [f for f in os.listdir(OUT) if '-extra-' in f and not f.lower().endswith('.jpg')]
print('非 jpg:', bad if bad else '无')

# 验证每张都是真 JPEG（读文件头）
print()
print('=== 文件头校验（FF D8 = JPEG）===')
badhdr = []
for f in os.listdir(OUT):
    if '-extra-' not in f:
        continue
    p = OUT / f
    with io.open(p, 'rb') as fh:
        head = fh.read(2)
    if head != b'\xff\xd8':
        badhdr.append((f, head))
print('非 JPEG 文件头:', len(badhdr))
for f, h in badhdr[:10]:
    print(f'  {f}  header={h}')
