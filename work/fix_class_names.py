# 单舰级的中文名统一成「××级」。
#
# 现状：data/classes/akagi.yaml 与 kaga.yaml（这两艘是事实上的单舰级，
# 因为没有同型舰）名字写成「赤城（单舰）」「加贺（单舰）」。这在树上显示
# 时会和「俾斯麦级」「光辉级」不成体系 —— 同级层其他条目都是「××级」。
#
# 改成「赤城级」「加贺级」，与海军史的通行说法一致（赤城型航空母舰 /
# 加贺型航空母舰），也与本站其他级的写法一致。
import glob
import io
import os
import re
import sys
from datetime import datetime

import yaml

DRY = '--dry-run' in sys.argv

FIXES = {
    'akagi': {'zh': '赤城级', 'en': 'Akagi class'},
    'kaga': {'zh': '加贺级', 'en': 'Kaga class'},
}

changed = []
for cid, want in FIXES.items():
    p = f'data/classes/{cid}.yaml'
    if not os.path.exists(p):
        print(f'  ! 缺 {p}')
        continue
    text = io.open(p, encoding='utf-8').read()
    d = yaml.safe_load(text)
    old_zh = d['name']['zh']

    # 替换 name 块里的 zh 与 en 两行
    def repl_zh(m):
        return m.group(1) + want['zh']

    m_zh = re.search(r'^(name:\n(?:\s+\S+:.*\n)*?\s+zh:\s*)(.+)$', text, re.M)
    m_en = re.search(r'^(name:\n(?:\s+\S+:.*\n)*?\s+en:\s*)(.+)$', text, re.M)
    if not m_zh:
        print(f'  ! {cid}: 找不到 name.zh')
        continue

    new_text = text
    if m_en:
        new_text = new_text[:m_en.start(2)] + want['en'] + new_text[m_en.end(2):]
        # 注意：改 en 之后 zh 的偏移可能变，重算一次
        m_zh = re.search(r'^(name:\n(?:\s+\S+:.*\n)*?\s+zh:\s*)(.+)$', new_text, re.M)
    new_text = new_text[:m_zh.start(2)] + want['zh'] + new_text[m_zh.end(2):]

    if not DRY:
        bak = f'{p}.bak-{datetime.now().strftime("%Y-%m-%d")}'
        if not os.path.exists(bak):
            io.open(bak, 'w', encoding='utf-8', newline='\n').write(text)
        io.open(p, 'w', encoding='utf-8', newline='\n').write(new_text)

    changed.append((cid, old_zh, want['zh']))

print(f'改名 {len(changed)} 个舰级：')
for cid, old, new in changed:
    print(f'  {cid:<10} {old:<14} -> {new}')

if DRY:
    print('\n=== dry-run ===')
    sys.exit(0)

print('\n复验全部舰级：')
for p in sorted(glob.glob('data/classes/*.yaml')):
    if '.bak' in p:
        continue
    d = yaml.safe_load(io.open(p, encoding='utf-8'))
    print(f"  {d['id']:<14} {d['name']['zh']:<26} {d['name']['en']}")
