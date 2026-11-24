# 修正筛选逻辑：必须看 Commons 原始文件名与描述，不能看落盘文件名
#
# bug：上一版给了落盘名 `tone-01-xxx.jpg`，再拿它去匹配「tone」，
# 于是每一张都命中，等于没筛。
# 正确做法：用 it['commons_title']（Commons 上的原始 File: 名）+ descr 判断。
import io

import yaml

VARIANTS = {
    'tone': ['tone'],
    'chikuma': ['chikuma'],
    'haruna': ['haruna'],
    'kirishima': ['kirishima'],
    'hosho': ['hōshō', 'hosho', 'hosyo'],
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
    'hammann': ['hammann'],
    'monaghan': ['monaghan'],
    'benham': ['benham'],
}

d = yaml.safe_load(io.open('work/_ship_images_raw.yaml', encoding='utf-8'))
kept, dropped = {}, {}

for sid, items in d['ships'].items():
    names = VARIANTS.get(sid, [sid])
    k, x = [], []
    for it in items:
        # 只看 Commons 原名与描述
        ctitle = str(it.get('commons_title') or '').lower()
        desc = str(it.get('descr') or '').lower()
        blob = ctitle + ' ' + desc[:200]
        hit = any(n in blob for n in names)
        if hit:
            k.append(it)
        else:
            x.append((ctitle.replace('file:', '')[:60], desc[:110]))
    kept[sid] = k
    dropped[sid] = x
    print(f'{sid:14} 保留 {len(k):>2} / 原 {len(items):>2}   剔除 {len(x)}')

print('\n\n===== 被剔除的（主体不是本舰）=====')
n = 0
for sid, xs in dropped.items():
    if not xs:
        continue
    print(f'\n--- {sid} ({len(xs)} 张)')
    for fn, ds in xs:
        n += 1
        print(f'    {fn}')
        print(f'       {ds[:100]}')
print(f'\n共剔除 {n} 张')

with io.open('work/_ship_images_filtered.yaml', 'w', encoding='utf-8', newline='\n') as f:
    yaml.safe_dump({'ships': kept}, f, allow_unicode=True, sort_keys=False,
                   default_flow_style=False, indent=2, width=200)

print('\n===== 筛选后 =====')
tot = 0
for sid, k in kept.items():
    flag = '' if len(k) >= 10 else '  ← 不足 10'
    print(f'  {sid:14} {len(k):>2}{flag}')
    tot += len(k)
print(f'  合计 {tot}')
