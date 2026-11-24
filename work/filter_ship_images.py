# 按舰名严格筛选：只保留文件名或描述里明确点名本舰的图
#
# 为什么必须这么做：Commons 的舰分类里混着大量「舰队合影」「某舰视角拍友舰」
# 之类的图，主体不是本舰。上一轮（docs/52 §3.3）就吃过这个亏：
# 8in-55-mk9 抓到了「破损舰首」、14cm 抓到岸炮。
#
# 判据（保守）：
#   文件名 或 描述前 160 字里出现本舰的任一变体名 → 保留
#   否则 → 剔除（记录原因）
import io

import yaml

VARIANTS = {
    'tone': ['tone'],
    'chikuma': ['chikuma'],
    'haruna': ['haruna'],
    'kirishima': ['kirishima'],
    'hosho': ['hōshō', 'hosho', 'hōshō', 'hosyo'],
    'nagara': ['nagara'],
    'sendai': ['sendai'],
    'astoria': ['astoria'],
    'portland': ['portland'],
    'minneapolis': ['minneapolis'],
    'new-orleans': ['new orleans', 'new-orleans'],
    'vincennes': ['vincennes'],
    'northampton': ['northampton'],
    'pensacola': ['pensacola'],
    'atlanta': ['atlanta'],
    'hammann': ['hammann', 'hammann'],
    'monaghan': ['monaghan'],
    'benham': ['benham'],
}

d = yaml.safe_load(io.open('work/_ship_images_raw.yaml', encoding='utf-8'))
kept = {}
dropped = {}

for sid, items in d['ships'].items():
    names = VARIANTS.get(sid, [sid])
    k, x = [], []
    for it in items:
        fn = str(it.get('file', '')).lower()
        desc = str(it.get('descr', '')).lower()
        blob_head = desc[:160]
        hit = any(n in fn.replace('-', ' ') or n in fn or n in blob_head for n in names)
        if hit:
            k.append(it)
        else:
            x.append((it.get('file', '').split('/')[-1], desc[:110]))
    kept[sid] = k
    dropped[sid] = x
    print(f'{sid:14} 保留 {len(k):>2} / 原 {len(items):>2}   剔除 {len(x)}')

print('\n\n===== 被剔除的（主体不是本舰）=====')
for sid, xs in dropped.items():
    if not xs:
        continue
    print(f'\n--- {sid} ({len(xs)} 张)')
    for fn, ds in xs:
        print(f'    {fn[:58]}')
        print(f'       {ds[:100]}')

with io.open('work/_ship_images_filtered.yaml', 'w', encoding='utf-8', newline='\n') as f:
    yaml.safe_dump({'ships': kept}, f, allow_unicode=True, sort_keys=False,
                   default_flow_style=False, indent=2, width=200)

print('\n\n===== 筛选后每舰张数 =====')
tot = 0
for sid, k in kept.items():
    flag = '' if 10 <= len(k) <= 15 else ('  ← 不足' if len(k) < 10 else '  ← 超')
    print(f'  {sid:14} {len(k):>2}{flag}')
    tot += len(k)
print(f'  合计 {tot}')
