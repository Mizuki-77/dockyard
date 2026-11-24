# 严格清洗：去重 + 剔除主体不是本舰的图
#
# 已发现的问题（2026-11-25 凌晨人工核查）：
#   1. 同一张图被存成两个文件名 —— hammann-04 出现两次、monaghan-03/05 各两次
#   2. 分类里混进别的舰 —— tone-01 实为夕立号、tone-04 为古鹰/衣笠、
#      hammann-01/02 是列克星敦号爆炸、monaghan-03 是 TBD 坠落、nagara-04 是 Sentai 4
#
# 判据（严格版）：
#   主体判据 = Commons 原始文件名里出现本舰名（最可靠，因为上传者通常按主体命名）
#   若仅描述里出现 → 人工复核名单，不自动通过
import hashlib
import io
import os
import re

import yaml

OUT = 'public/img/ships'
SHIPS = ['tone', 'chikuma', 'haruna', 'kirishima', 'hosho', 'nagara', 'sendai',
         'astoria', 'portland', 'minneapolis', 'new-orleans', 'vincennes',
         'northampton', 'pensacola', 'atlanta', 'hammann', 'monaghan', 'benham']

NAMES = {
    'tone': ['tone'],
    'chikuma': ['chikuma'],
    'haruna': ['haruna'],
    'kirishima': ['kirishima'],
    'hosho': ['hosho', 'hōshō', 'hosyo'],
    'nagara': ['nagara'],
    'sendai': ['sendai'],
    'astoria': ['astoria'],
    'portland': ['portland'],
    'minneapolis': ['minneapolis'],
    'new-orleans': ['new orleans', 'new-orleans', 'neworleans'],
    'vincennes': ['vincennes'],
    'northampton': ['northampton'],
    'pensacola': ['pensacola'],
    'atlanta': ['atlanta'],
    'hammann': ['hammann'],
    'monaghan': ['monaghan'],
    'benham': ['benham'],
}

d = yaml.safe_load(io.open('work/_ship_images_final.yaml', encoding='utf-8'))['ships']

# 全库按哈希去重（同一张图只留第一次出现的）
seen_hash = {}
final = {}
dropped = []

for sid in SHIPS:
    items = d.get(sid) or []
    keep = []
    for it in items:
        path = os.path.join('public', str(it['file']).lstrip('/'))
        if not os.path.exists(path):
            dropped.append((sid, os.path.basename(str(it['file'])), '文件不存在'))
            continue
        raw = open(path, 'rb').read()
        h = hashlib.sha256(raw).hexdigest()

        # 去重
        if h in seen_hash:
            dropped.append((sid, os.path.basename(str(it['file'])),
                            f'与 {seen_hash[h]} 重复'))
            continue

        # 主体判据：只看 Commons 原始文件名
        ctitle = str(it.get('commons_title') or '').lower().replace('file:', '')
        names = NAMES[sid]
        if not any(n in ctitle for n in names):
            dropped.append((sid, os.path.basename(str(it['file'])),
                            f'文件名无本舰名: {ctitle[:44]}'))
            continue

        seen_hash[h] = os.path.basename(str(it['file']))
        keep.append(it)
    final[sid] = keep

print('清洗结果：')
tot = 0
for sid in SHIPS:
    n = len(final[sid])
    tot += n
    print(f'  {sid:14} {n:>2}' + ('  ← 不足 10' if n < 10 else ''))
print(f'  合计 {tot}')

print(f'\n剔除 {len(dropped)} 张：')
for sid, fn, why in dropped:
    print(f'  [{sid}] {fn[:50]}  — {why}')

with io.open('work/_ship_images_clean.yaml', 'w', encoding='utf-8', newline='\n') as f:
    yaml.safe_dump({'ships': final}, f, allow_unicode=True, sort_keys=False,
                   default_flow_style=False, indent=2, width=200)
print('\n写出 work/_ship_images_clean.yaml')
