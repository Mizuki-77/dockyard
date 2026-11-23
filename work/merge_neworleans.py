# 合并两份 classes/new-orleans.yaml（tg162a 为主，tg172 补齐独有项）
#
# 为什么需要：两组各自独立建了同一个舰级文件。
#   tg162a 版 97 fact / 62 字段，覆盖 CA-32/36/44
#   tg172  版 83 fact / 58 字段，覆盖 CA-32/34/36，且带 identity.* 与武器实体
# 规则：以 tg162a 为基底；tg172 里键不重复的照收；键冲突的并列（两条都留，note 标来源）
import io
import shutil
from datetime import datetime

import yaml

A = 'work/staging/tg162a/classes/new-orleans.yaml'
B = 'work/staging/tg172/classes/new-orleans.yaml'
OUT = 'work/staging/_merged/classes/new-orleans.yaml'
STAMP = datetime.now().strftime('%Y-%m-%d')


def load(p):
    with io.open(p, encoding='utf-8') as f:
        return yaml.safe_load(f)


def dump(p, obj):
    import os
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with io.open(p, 'w', encoding='utf-8', newline='\n') as f:
        yaml.safe_dump(obj, f, allow_unicode=True, sort_keys=False,
                       default_flow_style=False, indent=2, width=200)


def fkey(f):
    """事实的同一性：归属 + 字段 + 限定词 + 时间窗。值不同算冲突，不算重复。"""
    return (
        f.get('about'),
        f.get('field'),
        str(f.get('qual')),
        str(f.get('valid')),
    )


a = load(A)
b = load(B)
fa = a.get('facts') or []
fb = b.get('facts') or []

ka = {}
for f in fa:
    ka.setdefault(fkey(f), []).append(f)

added = []
conflicts = []
for f in fb:
    k = fkey(f)
    if k not in ka:
        added.append(f)
        ka[k] = [f]
    else:
        existing = ka[k]
        # 值相同 → 重复，丢弃
        if any(str(e.get('value')) == str(f.get('value')) for e in existing):
            continue
        # 值不同 → 冲突，两条都留
        conflicts.append((f.get('field'), existing[0].get('value'), f.get('value')))

merged = dict(a)
merged['name'] = {'zh': '新奥尔良级重巡洋舰', 'en': 'New Orleans-class heavy cruiser'}
merged['class_of'] = ['new-orleans', 'minneapolis', 'vincennes', 'astoria']
merged['facts'] = fa + added

note = merged.get('open_ended_note') or ''
note += (
    f'\n\n【合并记录 {STAMP}】本文件由两个调研分片合并：'
    f'tg162a（CA-32/36/44）为主体，tg172（CA-32/34/36）补齐独有项与武器实体。'
    f'tg162a 原有 {len(fa)} 条，并入 tg172 独有 {len(added)} 条，'
    f'另 {len(conflicts)} 条键冲突按「两说并列」同时保留。'
)
merged['open_ended_note'] = note

dump(OUT, merged)

print(f'基底 {len(fa)} 条 + 并入 {len(added)} 条 = {len(merged["facts"])} 条')
print(f'冲突并列 {len(conflicts)} 条：')
for fld, va, vb in conflicts:
    print(f'   {fld}: {va}  vs  {vb}')
print(f'\n已写出 {OUT}')
