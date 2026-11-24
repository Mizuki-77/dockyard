# 终局校验：以 Commons 现查的元数据为准，逐张判断主体，删掉不合格文件
#
# 为什么重做：之前多轮脚本各自判断，标准不一致，还混进了坏图
# （hammann-10/12 又是列克星敦爆炸照）。
# 现在唯一权威来源 = 现场向 Commons 查每个文件的 ImageDescription，
# 判断「描述里第一个出现的舰名是不是本舰」。
import hashlib
import io
import os
import re

import yaml

from commons_client import api

OUT = 'public/img/ships'
BATCH = 10

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


def strip_tags(s):
    import html
    if not s:
        return ''
    return html.unescape(re.sub(r'<[^>]+>', '', str(s))).strip()


# 1) 收集磁盘上每个文件的 Commons 原名（来自历次 yaml，取最全的一版）
title_of = {}
for src in ['work/_ship_images_raw.yaml', 'work/_ship_images_filtered.yaml',
            'work/_ship_images_final.yaml', 'work/_ship_images_v2.yaml',
            'work/_ship_images_v3.yaml']:
    if not os.path.exists(src):
        continue
    d = yaml.safe_load(io.open(src, encoding='utf-8')) or {}
    for sid, items in (d.get('ships') or {}).items():
        for it in items:
            fn = os.path.basename(str(it.get('file') or ''))
            ct = str(it.get('commons_title') or '')
            if fn and ct.startswith('File:'):
                title_of[fn] = ct

# 2) 磁盘实际文件
disk = {}
for fn in os.listdir(OUT):
    m = re.match(r'^([a-z\-]+?)-(\d+)-', fn)
    if not m:
        continue
    sid = m.group(1)
    if sid not in SHIPS:
        # new-orleans 的连字符 id
        continue
    disk.setdefault(sid, []).append(fn)

# 补 new-orleans（文件名前缀含连字符，单独处理）
for fn in os.listdir(OUT):
    if fn.startswith('new-orleans-'):
        disk.setdefault('new-orleans', []).append(fn)

print('磁盘文件数：')
for sid in SHIPS:
    print(f'  {sid:14} {len(disk.get(sid) or [])}')

# 3) 批量查描述
need = [title_of[f] for f in title_of if f in set(sum(disk.values(), []))]
print(f'\n待查描述 {len(need)} 个文件')

desc_of = {}
for i in range(0, len(need), BATCH):
    chunk = need[i:i + BATCH]
    j = api({'action': 'query', 'titles': '|'.join(chunk),
             'prop': 'imageinfo', 'iiprop': 'extmetadata',
             'format': 'json'})
    for _, p in (j.get('query', {}).get('pages') or {}).items():
        ii = (p.get('imageinfo') or [None])[0]
        md = (ii or {}).get('extmetadata') or {}
        desc_of[p.get('title')] = strip_tags(md.get('ImageDescription', {}).get('value', ''))
    print(f'  {i + len(chunk)}/{len(need)}')
    import time
    time.sleep(1.5)

# 4) 判定
keep, reject, no_meta = {}, [], []
seen = {}
for sid in SHIPS:
    names = ALL_NAMES[sid]
    k = []
    for fn in sorted(disk.get(sid) or []):
        path = os.path.join(OUT, fn)
        h = hashlib.sha256(open(path, 'rb').read()).hexdigest()
        if h in seen:
            reject.append((sid, fn, f'重复于 {seen[h]}'))
            continue
        ct = title_of.get(fn, '')
        desc = desc_of.get(ct, '') if ct else ''
        if not ct:
            no_meta.append((sid, fn))
            # 无元数据不敢留
            reject.append((sid, fn, '无 Commons 元数据，无法核实主体'))
            continue
        ctitle = ct.lower().replace('file:', '')
        blob = desc[:400].lower()
        if any(n in ctitle for n in names):
            seen[h] = fn
            k.append((fn, ct, desc))
            continue
        hits = []
        for osid, onames in ALL_NAMES.items():
            for n in onames:
                idx = blob.find(n)
                if idx >= 0:
                    hits.append((idx, osid))
                    break
        if hits:
            hits.sort()
            if hits[0][1] == sid:
                seen[h] = fn
                k.append((fn, ct, desc))
            else:
                reject.append((sid, fn, f'描述主舰是 {hits[0][1]}'))
        else:
            reject.append((sid, fn, '文件名与描述均无舰名'))
    keep[sid] = k

print('\n===== 判定结果 =====')
tot = 0
for sid in SHIPS:
    n = len(keep[sid])
    tot += n
    print(f'  {sid:14} {n:>2}' + ('  ← 不足 10' if n < 10 else ''))
print(f'  合计 {tot}')

print(f'\n剔除 {len(reject)}：')
for sid, fn, why in reject:
    print(f'  [{sid}] {fn[:56]} — {why}')

# 5) 删掉不合格文件
deleted = 0
for sid, fn, why in reject:
    p = os.path.join(OUT, fn)
    if os.path.exists(p):
        os.remove(p)
        deleted += 1
print(f'\n已删除 {deleted} 个不合格文件')

with io.open('work/_ship_images_verified.yaml', 'w', encoding='utf-8', newline='\n') as f:
    out = {}
    for sid in SHIPS:
        out[sid] = [{'file': f'/img/ships/{fn}', 'subject': f'ship:{sid}',
                     'commons_title': ct, 'descr': ds[:300]}
                    for fn, ct, ds in keep[sid]]
    yaml.safe_dump({'ships': out, 'rejected': [{'ship': s, 'file': f, 'why': w}
                                               for s, f, w in reject]},
                   f, allow_unicode=True, sort_keys=False,
                   default_flow_style=False, indent=2, width=200)
print('写出 work/_ship_images_verified.yaml')
