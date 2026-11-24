# 平衡判据定稿版
#
# 前两版都过偏：
#   只看文件名 → 国家档案馆编号照片（80-G-55260 之类）被误删，而它们是本舰正照
#   只看描述   → 「某舰视角拍友舰」「舰队合影」混进来
#
# 本版（最接近人工判断）：
#   ① Commons 原名含本舰名 → 通过
#   ② 否则看描述里「第一个出现的舰名」是不是本舰 → 是则通过
#      （描述第一句通常就是「USS X (CA-Y) ...」的主体说明）
#   ③ 都没有 → 进人工复核（默认不留）
#
# 另：必须先从原始抓取记录重建，因为上一版把文件删了。
import io
import os
import re

import yaml

OUT = 'public/img/ships'
SHIPS = ['tone', 'chikuma', 'haruna', 'kirishima', 'hosho', 'nagara', 'sendai',
         'astoria', 'portland', 'minneapolis', 'new-orleans', 'vincennes',
         'northampton', 'pensacola', 'atlanta', 'hammann', 'monaghan', 'benham']

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

# 从最早的原始抓取表重建（那版没删过东西）
src = io.open('work/_ship_images_raw.yaml', encoding='utf-8').read()
raw = yaml.safe_load(src)['ships']

print('从 _ship_images_raw.yaml 重建（原始抓取记录，未删过文件）')
for sid in SHIPS:
    print(f'  {sid:14} {len(raw.get(sid) or []):>2}')

# 逐舰判定（只判断，不删文件；先出清单供人工确认）
decision = {}
for sid in SHIPS:
    names = ALL_NAMES[sid]
    keep, why_drop = [], []
    for it in raw.get(sid) or []:
        ct = str(it.get('commons_title') or '').lower().replace('file:', '')
        desc = str(it.get('descr') or '')
        blob = desc[:400].lower()

        ok = any(n in ct for n in names)
        reason = '名称命中' if ok else ''
        if not ok:
            hits = []
            for osid, onames in ALL_NAMES.items():
                for n in onames:
                    k = blob.find(n)
                    if k >= 0:
                        hits.append((k, osid))
                        break
            hits.sort()
            if hits and hits[0][1] == sid:
                ok = True
                reason = '描述主舰'
            elif hits:
                why_drop.append((it, f'描述主舰是 {hits[0][1]}'))
            else:
                why_drop.append((it, '无舰名'))
        if ok:
            it2 = dict(it)
            it2['_reason'] = reason
            keep.append(it2)
    decision[sid] = (keep, why_drop)

print('\n判定结果（编号不变，仅判断）：')
tot = 0
for sid in SHIPS:
    k, d = decision[sid]
    tot += len(k)
    print(f'  {sid:14} 留 {len(k):>2}  弃 {len(d):>2}')
print(f'  合计留 {tot}')

with io.open('work/_ship_images_decision.yaml', 'w', encoding='utf-8', newline='\n') as f:
    yaml.safe_dump({'ships': {sid: decision[sid][0] for sid in SHIPS},
                    'dropped': {sid: [{'file': x.get('file'), 'why': w}
                                      for x, w in decision[sid][1]] for sid in SHIPS}},
                   f, allow_unicode=True, sort_keys=False,
                   default_flow_style=False, indent=2, width=200)
print('\n写出 work/_ship_images_decision.yaml')
