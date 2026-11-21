# 第二轮剔除：替补里有几张仍不合格。
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / 'work' / 'shipimg'
OUT = ROOT / 'public' / 'img' / 'ships'

DROP2 = [
    # 纳粹旗、纪念牌 —— 不是舰照
    'bismarck-extra-fix-el-acorazado-bismarck-y-la-bandera-nazi-j.jpg',
    'bismarck-extra-fix-marineehrenmal-laboe-gedenktafel-f-r-die-jpg.jpg',
    # 珍珠港航拍 —— 主体不是本舰
    'enterprise-extra-fix-aerial-view-of-pearl-harbor-navy-yard-a.jpg',
    'yorktown-extra-fix-aerail-view-of-pearl-harbor-on-3-may-1940.jpg',
    # 与已有的 extra-3 是同一张的另一裁切
    'prince-of-wales-extra-fix-the-royal-navy-during-the-second-w.jpg',
]

picked = json.load(io.open(WORK / 'picked.json', encoding='utf-8'))

for n in DROP2:
    p = OUT / n
    if p.exists():
        p.unlink()
        print(f'删除 {n}')
    for sid in picked:
        picked[sid] = [x for x in picked[sid] if x['name'] != n]

io.open(WORK / 'picked.json', 'w', encoding='utf-8').write(
    json.dumps(picked, ensure_ascii=False, indent=2))

print()
print('=== 最终张数 ===')
tot = 0
for sid, es in picked.items():
    tot += len(es)
    print(f'  {sid:<18} {len(es)}')
print(f'总计 {tot}')
