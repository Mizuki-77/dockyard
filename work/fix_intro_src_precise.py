# 按段落正文实际引用的来源，重配 intro 的 src
#
# 上一版按「该文件出现频率最高的来源」自动补 src，抽检发现是错的：
#   atlanta 段0 正文写「NavWeaps 的炮座表写得很清楚」，src 却只给了 danfs-atlanta —— 对不上。
# 本站立站原则是「每条都能点开看来源」，src 必须与正文实际依据一致。
#
# 做法：扫段落正文里出现的来源指代词（NavWeaps / DANFS / navypedia / combinedfleet /
#       navsource / HyperWar），映射到该篇实际登记并使用的来源 id，
#       再与段落内容做关键词核对。
import io
import os
import re
import shutil
from collections import Counter
from datetime import datetime

import yaml

STAMP = datetime.now().strftime('%Y-%m-%d')

# 正文里的指代词 → 来源 id 前缀
HINTS = {
    'navweaps': 'navweaps-',
    'danfs': 'danfs-',
    'navypedia': 'navypedia-',
    'combinedfleet': 'combinedfleet-',
    'navsource': 'navsource-',
    'hyperwar': 'hyperwar-',
    'destroyerhistory': 'destroyerhistory-',
    'ibiblio': 'hyperwar-',
}


def load(p):
    with io.open(p, encoding='utf-8') as f:
        return yaml.safe_load(f)


def dump(p, obj):
    with io.open(p, 'w', encoding='utf-8', newline='\n') as f:
        yaml.safe_dump(obj, f, allow_unicode=True, sort_keys=False,
                       default_flow_style=False, indent=2, width=200)


TARGETS = ['atlanta', 'northampton', 'pensacola', 'portland']

for sid in TARGETS:
    p = f'data/articles/{sid}.yaml'
    if not os.path.exists(p):
        continue
    d = load(p)

    # 本文件已登记并使用的全部来源
    used = set()
    for sec in (d.get('history') or []):
        for ev in (sec.get('events') or []):
            used.update(ev.get('src') or [])
    for para in (d.get('intro', {}).get('paragraphs') or []):
        used.update(para.get('src') or [])

    changed = 0
    for i, para in enumerate(d.get('intro', {}).get('paragraphs') or []):
        zh = str(para.get('text', {}).get('zh') or '')
        en = str(para.get('text', {}).get('en') or '')
        blob = (zh + ' ' + en).lower()

        # 找出正文实际提到的来源
        picked = []
        for hint, prefix in HINTS.items():
            if hint in blob:
                # 在该篇用到的来源里找匹配前缀的
                cands = [s for s in used if str(s).startswith(prefix)]
                if cands:
                    # 优先选和本舰同名的（danfs-atlanta 对 atlanta）
                    same = [c for c in cands if sid.split('-')[0] in str(c)]
                    picked.extend(same or cands[:1])

        picked = list(dict.fromkeys(picked))
        if picked and picked != (para.get('src') or []):
            old = para.get('src')
            para['src'] = picked
            changed += 1
            print(f'  [src] {sid} 段{i}: {old} → {picked}')

    if changed:
        bak = f'{p}.bak2-{STAMP}'
        if not os.path.exists(bak):
            shutil.copy2(p, bak)
        dump(p, d)
        print(f'      ↑ {p} 改了 {changed} 段')

print('\n完成')
