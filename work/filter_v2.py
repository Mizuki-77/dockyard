# 按「描述」判断主体，而不是只看文件名
#
# 上一版只认文件名 → 把大量国家档案馆编号照片（80-G-55260 之类）全剔了，
# 那些照片的描述里明写 "USS Minneapolis (CA-36)"，其实是本舰正照。
#
# 本版判据（更接近人工判断）：
#   1. Commons 文件名 含本舰名 → 通过
#   2. 否则看描述（ImageDescription）：描述里第一个出现的舰名是本舰 → 通过
#      若是别的舰名先出现 → 剔除（说明本舰只是配角或背景）
#   3. 都没有舰名 → 进「待人工复核」名单
import hashlib
import io
import os
import re

import yaml

SHIPS = ['tone', 'chikuma', 'haruna', 'kirishima', 'hosho', 'nagara', 'sendai',
         'astoria', 'portland', 'minneapolis', 'new-orleans', 'vincennes',
         'northampton', 'pensacola', 'atlanta', 'hammann', 'monaghan', 'benham']

# 全部可能出现的舰名（用于判断「描述里先提到谁」）
ALL_NAMES = {
    'tone': ['tone'], 'chikuma': ['chikuma'], 'haruna': ['haruna'],
    'kirishima': ['kirishima'], 'hosho': ['hosho', 'hōshō', 'hosyo'],
    'nagara': ['nagara'], 'sendai': ['sendai'], 'astoria': ['astoria'],
    'portland': ['portland'], 'minneapolis': ['minneapolis'],
    'new-orleans': ['new orleans', 'new-orleans', 'neworleans'],
    'vincennes': ['vincennes'], 'northampton': ['northampton'],
    'pensacola': ['pensacola'], 'atlanta': ['atlanta'], 'hammann': ['hammann'],
    'monaghan': ['monaghan'], 'benham': ['benham'],
}

d = yaml.safe_load(io.open('work/_ship_images_final.yaml', encoding='utf-8'))['ships']

seen_hash = {}
final, review, dropped = {}, [], []

for sid in SHIPS:
    names = ALL_NAMES[sid]
    keep = []
    for it in d.get(sid) or []:
        path = os.path.join('public', str(it['file']).lstrip('/'))
        if not os.path.exists(path):
            dropped.append((sid, os.path.basename(str(it['file'])), '文件不存在'))
            continue
        h = hashlib.sha256(open(path, 'rb').read()).hexdigest()
        if h in seen_hash:
            dropped.append((sid, os.path.basename(str(it['file'])),
                            f'重复于 {seen_hash[h]}'))
            continue

        ctitle = str(it.get('commons_title') or '').lower().replace('file:', '')
        desc = str(it.get('descr') or '').lower()
        blob = desc[:400]

        # 1. 文件名直接命中
        if any(n in ctitle for n in names):
            seen_hash[h] = os.path.basename(str(it['file']))
            keep.append(it)
            continue

        # 2. 描述里找「第一个出现的舰名」
        hits = []
        for other_sid, other_names in ALL_NAMES.items():
            for n in other_names:
                idx = blob.find(n)
                if idx >= 0:
                    hits.append((idx, other_sid))
                    break
        if hits:
            hits.sort()
            first_sid = hits[0][1]
            if first_sid == sid:
                seen_hash[h] = os.path.basename(str(it['file']))
                keep.append(it)
            else:
                dropped.append((sid, os.path.basename(str(it['file'])),
                                f'描述主舰是 {first_sid}'))
            continue

        # 3. 都没有 → 待复核
        if blob.strip():
            review.append((sid, it))
        else:
            dropped.append((sid, os.path.basename(str(it['file'])), '文件名与描述都无舰名'))
    final[sid] = keep

print('通过：')
tot = 0
for sid in SHIPS:
    n = len(final[sid])
    tot += n
    print(f'  {sid:14} {n:>2}' + ('  ← 不足 10' if n < 10 else ''))
print(f'  合计 {tot}')

print(f'\n剔除 {len(dropped)}：')
for sid, fn, why in dropped:
    print(f'  [{sid}] {fn[:46]} — {why}')

print(f'\n待人工复核 {len(review)}：')
for sid, it in review:
    print(f'  [{sid}] {os.path.basename(str(it["file"]))[:46]}')
    print(f'        描述: {str(it.get("descr") or "")[:110]}')

with io.open('work/_ship_images_v2.yaml', 'w', encoding='utf-8', newline='\n') as f:
    yaml.safe_dump({'ships': final,
                    'review': [{'ship': s, 'item': i} for s, i in review]},
                   f, allow_unicode=True, sort_keys=False,
                   default_flow_style=False, indent=2, width=200)
print('\n写出 work/_ship_images_v2.yaml')
