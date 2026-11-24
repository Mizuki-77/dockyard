# 最终定稿：清掉坏图、重编号、写进 images.yaml
#
# 现存问题（2026-11-25 凌晨肉眼 + 元数据双重核对）：
#   - 编号重复：hammann-04 x2、monaghan-03 x2、monaghan-05 x2
#   - 主体错误：hammann-01/02 是列克星敦爆炸、nagara-04 是 Sentai 4、
#     monaghan-03 是 TBD 坠落、benham-09 是约克城弃舰
#
# 判据：Commons 原始文件名里必须出现本舰名（最硬的判据）。
#   描述里出现但文件名没有的，一律不留 —— 上一轮吃过「描述主舰判断」反复出错的亏。
import io
import json
import os
import re
import ssl
import time
import urllib.parse
import urllib.request

import yaml

from commons_client import api

OUT = 'public/img/ships'
PROXY = 'http://127.0.0.1:12450'
WIDTH = 1280

SHIPS = ['tone', 'chikuma', 'haruna', 'kirishima', 'hosho', 'nagara', 'sendai',
         'astoria', 'portland', 'minneapolis', 'new-orleans', 'vincennes',
         'northampton', 'pensacola', 'atlanta', 'hammann', 'monaghan', 'benham']

NAMES = {
    'tone': ['tone'], 'chikuma': ['chikuma'], 'haruna': ['haruna'],
    'kirishima': ['kirishima'], 'hosho': ['hosho', 'hōshō', 'hosyo'],
    'nagara': ['nagara'], 'sendai': ['sendai'], 'astoria': ['astoria'],
    'portland': ['portland'], 'minneapolis': ['minneapolis'],
    'new-orleans': ['new orleans', 'new-orleans', 'neworleans'],
    'vincennes': ['vincennes'], 'northampton': ['northampton'],
    'pensacola': ['pensacola'], 'atlanta': ['atlanta'], 'hammann': ['hammann'],
    'monaghan': ['monaghan'], 'benham': ['benham'],
}


def strip_tags(s):
    import html
    if not s:
        return ''
    return html.unescape(re.sub(r'<[^>]+>', '', str(s))).strip()


# 1) 从历次 yaml 收集 落盘名 → Commons 原名
title_of = {}
for src in ['work/_ship_images_raw.yaml', 'work/_ship_images_filtered.yaml',
            'work/_ship_images_final.yaml', 'work/_ship_images_v2.yaml',
            'work/_ship_images_v3.yaml', 'work/_ship_images_verified.yaml',
            'work/_ship_images_repaired.yaml']:
    if not os.path.exists(src):
        continue
    d = yaml.safe_load(io.open(src, encoding='utf-8')) or {}
    for sid, items in (d.get('ships') or {}).items():
        for it in items:
            fn = os.path.basename(str(it.get('file') or ''))
            ct = str(it.get('commons_title') or '')
            if fn and ct.startswith('File:'):
                title_of[fn] = ct

print(f'已收集 {len(title_of)} 个文件的 Commons 原名')

# 2) 逐舰处理：判定 → 删除 → 重编号
deleted = []
final = {}

for sid in SHIPS:
    files = sorted(f for f in os.listdir(OUT) if re.match(rf'^{re.escape(sid)}-\d+-', f))
    names = NAMES[sid]
    keep = []
    seen_stem = set()
    for fn in files:
        m = re.match(rf'^{re.escape(sid)}-\d+-(.+)$', fn)
        stem = m.group(1) if m else fn
        ct = title_of.get(fn, '').lower().replace('file:', '')

        # 源名重复（不同编号同一张）
        if stem in seen_stem:
            os.remove(os.path.join(OUT, fn))
            deleted.append((sid, fn, '同源名重复'))
            continue

        # 主体判据：Commons 原名含本舰名
        if ct and any(n in ct for n in names):
            seen_stem.add(stem)
            keep.append((fn, stem))
        else:
            os.remove(os.path.join(OUT, fn))
            deleted.append((sid, fn, f'原名无本舰名: {ct[:40] or "(无元数据)"}'))

    # 重编号：sid-01, sid-02 …
    renumbered = []
    for i, (old, stem) in enumerate(keep, 1):
        new = f'{sid}-{i:02d}-{stem}'
        if new != old:
            os.rename(os.path.join(OUT, old), os.path.join(OUT, new))
        renumbered.append(new)
    final[sid] = renumbered

print('\n最终计数：')
tot = 0
for sid in SHIPS:
    n = len(final[sid])
    tot += n
    print(f'  {sid:14} {n:>2}' + ('  ← 素材上限' if n < 10 else ''))
print(f'  合计 {tot}')

if deleted:
    print(f'\n删除 {len(deleted)}：')
    for sid, fn, why in deleted:
        print(f'  [{sid}] {fn[:52]} — {why}')

with io.open('work/_ship_images_done.yaml', 'w', encoding='utf-8', newline='\n') as f:
    yaml.safe_dump({'ships': final}, f, allow_unicode=True, sort_keys=False,
                   default_flow_style=False, indent=2, width=200)
print('\n写出 work/_ship_images_done.yaml')
