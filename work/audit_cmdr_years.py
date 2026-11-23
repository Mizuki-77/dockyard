# 自检：正文里提到的年份是否与 life 字段冲突（防「13 岁当上校」这类硬伤）。
import glob
import io
import re

import yaml

problems = []
for p in sorted(glob.glob('data/commanders/*.yaml')):
    d = yaml.safe_load(io.open(p, encoding='utf-8'))
    cid = d.get('id')
    life = d.get('life') or {}
    born = str(life.get('born') or '')
    died = str(life.get('died') or '')
    by = int(born[:4]) if born[:4].isdigit() else None
    dy = int(died[:4]) if died[:4].isdigit() else None

    texts = []
    for pa in d.get('intro') or []:
        texts.append(('intro', pa.get('heading'), str(pa.get('text') or '')))
    for ev in d.get('timeline') or []:
        texts.append(('timeline', ev.get('date'), str(ev.get('text') or '')))

    for kind, label, t in texts:
        for m in re.finditer(r'(\d{4})\s*年', t):
            y = int(m.group(1))
            if by and y < by:
                problems.append(f'{cid} [{kind}/{label}] 提到 {y} 年，早于出生年 {by}')
            if dy and y > dy:
                problems.append(f'{cid} [{kind}/{label}] 提到 {y} 年，晚于卒年 {dy}')

    # 时间线事件日期也查一遍
    for ev in d.get('timeline') or []:
        dt = str(ev.get('date') or '')
        if dt[:4].isdigit():
            y = int(dt[:4])
            if by and y < by:
                problems.append(f'{cid} timeline 事件日期 {dt} 早于出生年 {by}')
            if dy and y > dy:
                problems.append(f'{cid} timeline 事件日期 {dt} 晚于卒年 {dy}')

print('=== 年份越界检查 ===')
if problems:
    for x in problems:
        print('  x', x)
else:
    print('  未发现')

# 军衔与年龄合理性：入海军年龄
print()
print('=== 生卒与简介首段的年份 ===')
for p in sorted(glob.glob('data/commanders/*.yaml')):
    d = yaml.safe_load(io.open(p, encoding='utf-8'))
    life = d.get('life') or {}
    intro0 = (d.get('intro') or [{}])[0]
    txt = str(intro0.get('text') or '')
    yrs = re.findall(r'(1[89]\d{2}|20\d{2})\s*年', txt)
    print(f"  {d['id']:<22} born={str(life.get('born'))[:10]:<12} "
          f"died={str(life.get('died'))[:10]:<12} 首段年份={yrs[:4]}")
