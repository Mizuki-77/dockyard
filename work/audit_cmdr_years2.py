# 自检：正文年份 vs 生卒年。
#
# 第一版规则太粗（任何年份早于出生年/晚于卒年都报错），实测 4 条全是误报：
#   · Lindemann：1942-01-06 遗孀代领追授勋章 —— 死后发生的事，正常
#   · Pławski：2004-06-16 骨灰迁葬波兰 —— 死后发生的事，正常
#   · White：祖宅「1699 年起的宅子」 —— 说的是建筑，不是人
#
# 所以规则改成：只有在**主语是本人**且**不是死亡/追授/迁葬语境**时才报。
# 判据用关键词窗口：该年份前后 40 字内出现这些词就跳过。
EXEMPT = [
    '追授', '遗孀', '代领', '葬', '骨灰', '墓地', '公墓', '纪念碑', '纪念',
    '宅', '城堡', '建于', '年起', '成立', '下水', '开工', '服役', '建造',
    '舰', '炮', '型号', '级',
]

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
        texts.append(('timeline', str(ev.get('date')), str(ev.get('text') or '')))

    for kind, label, t in texts:
        for m in re.finditer(r'(\d{4})\s*年', t):
            y = int(m.group(1))
            bad = (by and y < by) or (dy and y > dy)
            if not bad:
                continue
            # 看窗口里有没有豁免词
            win = t[max(0, m.start() - 45): m.end() + 45]
            if any(k in win for k in EXEMPT):
                continue
            problems.append(f'{cid} [{kind}/{label}] {y} 年 | …{win.strip()[:70]}…')

print('=== 年份越界（已排除追授/迁葬/建筑等语境）===')
if problems:
    for x in problems:
        print('  x', x)
else:
    print('  未发现真实越界')

# 年龄合理性：入海军年龄
print()
print('=== 入役年龄检查（海军军官通常 13-15 岁入达特茅斯）===')
for p in sorted(glob.glob('data/commanders/*.yaml')):
    d = yaml.safe_load(io.open(p, encoding='utf-8'))
    life = d.get('life') or {}
    born = str(life.get('born') or '')
    if not born[:4].isdigit():
        continue
    by = int(born[:4])
    full = ' '.join(str(pa.get('text') or '') for pa in d.get('intro') or [])
    m = re.search(r'(\d{4})\s*年[^。]{0,12}(入海军|入达特茅斯|入奥斯本|入不列颠尼亚|入海军学院)', full)
    if m:
        age = int(m.group(1)) - by
        flag = 'OK' if 12 <= age <= 16 else '?? 可疑'
        print(f"  {d['id']:<22} 入役 {m.group(1)} 年, 当时 {age} 岁  {flag}")
