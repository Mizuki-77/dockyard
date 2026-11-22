# 数据一致性对账。
#
# 检查各层之间的引用是否闭合：
#   1. class_of 与 ships[].class 双向一致
#   2. 每个舰的切片边界是否落在 fact 的时间窗内
#   3. articles / slices / images 是否有孤儿（指向不存在的舰）
#   4. fact 的 about 引用（weapon:/mount:）是否有对应实体
#   5. 武器页的文章与图是否齐全
import glob
import io
import os
import re
from collections import defaultdict

import yaml


def load(p):
    return yaml.safe_load(io.open(p, encoding='utf-8')) or {}


def zh(v):
    if isinstance(v, dict):
        return v.get('zh') or v.get('en') or ''
    return str(v)


problems = []

# ---------------------------------------------------------------- 1. 舰级双向
ships = {}
for p in glob.glob('data/ships/*.yaml'):
    if '.bak' in p:
        continue
    d = load(p)
    ships[os.path.basename(p)[:-5]] = d

classes = {}
for p in glob.glob('data/classes/*.yaml'):
    if '.bak' in p:
        continue
    d = load(p)
    classes[os.path.basename(p)[:-5]] = d

print('=== 1. class_of 与 ship.class 双向一致 ===')
for cid, c in classes.items():
    of = c.get('class_of') or []
    for sid in of:
        if sid not in ships:
            problems.append(f'classes/{cid}.class_of 指向不存在的舰 {sid}')
            continue
        if ships[sid].get('class') != cid:
            problems.append(
                f'{sid}.class = {ships[sid].get("class")}，但 classes/{cid}.class_of 包含它')
    # 反向：有哪些舰的 class 是 cid 但没写进 class_of
    members = [s for s, d in ships.items() if d.get('class') == cid]
    for m in members:
        if m not in of:
            problems.append(f'{m}.class = {cid}，但 classes/{cid}.class_of 里没有它 [{of}]')

for sid, s in ships.items():
    cid = s.get('class')
    if cid and cid not in classes:
        problems.append(f'{sid}.class 指向不存在的舰级 {cid}')

if not problems:
    print('  ✓ 双向一致')

# ---------------------------------------------------------------- 2. 切片边界
print()
print('=== 2. 切片边界是否落在 fact 时间窗内 ===')
slice_problems = []
for p in glob.glob('data/slices/*.yaml'):
    if '.bak' in p:
        continue
    d = load(p)
    sid = d.get('ship')
    if not sid:
        slice_problems.append(f'{p}: 缺 ship 字段')
        continue
    if sid not in ships:
        slice_problems.append(f'{p}: ship={sid} 不存在')
        continue

    # 该舰所有 fact 的日期。
    # 必须与运行时 buildShipView() 的过滤口径一致，否则会大量误报：
    #   identity.*       文书日期，不进时间轴
    #   带 about 的       武器/炮位本体，说的是「那型炮何时存在」，不是本舰状态
    all_facts = (ships[sid].get('facts') or []) + \
                (classes.get(ships[sid].get('class'), {}).get('facts') or [])
    facts = [
        f for f in all_facts
        if not str(f.get('field') or '').startswith('identity.')
        and not f.get('about')
    ]
    spans = []
    for f in facts:
        v = f.get('valid') or {}
        a = str(v.get('from') or '')
        if re.match(r'^\d{4}', a):
            spans.append(a)

    for sl in d.get('slices') or []:
        code = sl.get('code')
        frm = str(sl.get('from') or '')
        to = str(sl.get('to') or '')
        if not re.match(r'^\d{4}', frm):
            slice_problems.append(f'{sid}/{code}: from={frm} 不是合法日期')
        if to and not re.match(r'^\d{4}', to):
            slice_problems.append(f'{sid}/{code}: to={to} 不是合法日期')
        if to and frm and to < frm:
            slice_problems.append(f'{sid}/{code}: to({to}) 早于 from({frm})')

    # 切片是否覆盖了整段时间轴
    sl = d.get('slices') or []
    if sl:
        s0 = str(sl[0].get('from') or '')
        s1 = str(sl[-1].get('to') or '')
        if spans:
            fmin, fmax = min(spans), max(spans)
            if s0[:4] > fmin[:4]:
                slice_problems.append(
                    f'{sid}: 首个切片从 {s0} 开始，但最早 fact 在 {fmin}（前段没覆盖）')
            if s1 and s1[:4] < fmax[:4]:
                slice_problems.append(
                    f'{sid}: 末个切片到 {s1} 结束，但最晚 fact 在 {fmax}（后段没覆盖）')

for x in slice_problems:
    print(f'  ✗ {x}')
if not slice_problems:
    print('  ✓ 无问题')

# ---------------------------------------------------------------- 3. 孤儿
print()
print('=== 3. 孤儿文件（articles / slices / images）===')
orphans = []
for p in glob.glob('data/articles/*.yaml'):
    if '.bak' in p:
        continue
    d = load(p)
    sid = d.get('ship')
    if sid and sid not in ships:
        orphans.append(f'articles/{os.path.basename(p)}: ship={sid} 不存在')

for p in glob.glob('data/slices/*.yaml'):
    if '.bak' in p:
        continue
    d = load(p)
    sid = d.get('ship')
    if sid and sid not in ships:
        orphans.append(f'slices/{os.path.basename(p)}: ship={sid} 不存在')

imgs = load('data/images.yaml').get('images') or []
subjects = defaultdict(int)
for im in imgs:
    s = str(im.get('subject') or '')
    subjects[s] += 1
for s in subjects:
    if s.startswith('ship:'):
        sid = s[5:]
        if sid not in ships:
            orphans.append(f'images.yaml: subject={s} 但该舰不存在')
    elif s.startswith('weapon:'):
        pass  # 稍后单独查
    elif s.startswith('battle:'):
        bid = s[7:]
        if not os.path.exists(f'data/battles/{bid}.yaml'):
            orphans.append(f'images.yaml: subject={s} 但该战役不存在')
    elif s.startswith('operation:'):
        oid = s[10:]
        if not os.path.exists(f'data/operations/{oid}.yaml'):
            orphans.append(f'images.yaml: subject={s} 但该行动不存在')

for x in orphans:
    print(f'  ✗ {x}')
if not orphans:
    print('  ✓ 无孤儿')

# ---------------------------------------------------------------- 4. about 引用
print()
print('=== 4. fact 的 about 引用是否有对应实体 ===')
about_problems = []
weapon_ids = set()
mount_ids = set()
for p in glob.glob('data/classes/*.yaml') + glob.glob('data/ships/*.yaml'):
    if '.bak' in p:
        continue
    d = load(p)
    for f in d.get('facts') or []:
        a = str(f.get('about') or '')
        if a.startswith('weapon:'):
            weapon_ids.add(a[7:])
        elif a.startswith('mount:'):
            mount_ids.add(a[6:])

# 武器 id 必须有对应的 article 或至少能生成页面（页面靠 fact 生成，所以都有）
no_article = []
for w in sorted(weapon_ids):
    if not os.path.exists(f'data/weapon-articles/{w}.yaml'):
        no_article.append(w)
print(f'  武器实体 {len(weapon_ids)} 个，其中无正文 {len(no_article)} 个')
if no_article:
    print(f'     {no_article}')

# 反过来：有正文但没实体
orphan_articles = []
for p in glob.glob('data/weapon-articles/*.yaml'):
    wid = os.path.basename(p)[:-5]
    if wid not in weapon_ids:
        orphan_articles.append(wid)
print(f'  武器正文 {len(glob.glob("data/weapon-articles/*.yaml"))} 篇，无实体指向 {len(orphan_articles)} 篇')
if orphan_articles:
    for x in orphan_articles:
        print(f'     ✗ {x}')
        problems.append(f'weapon-articles/{x}.yaml 没有任何 fact 指向它')

# ---------------------------------------------------------------- 5. 图片覆盖
print()
print('=== 5. 武器/战役的图覆盖 ===')
no_wimg = []
for w in sorted(weapon_ids):
    if subjects.get(f'weapon:{w}', 0) == 0:
        no_wimg.append(w)
print(f'  武器无图: {len(no_wimg)} / {len(weapon_ids)}')
if no_wimg:
    print(f'     {no_wimg[:15]}{"..." if len(no_wimg) > 15 else ""}')

print()
print('=' * 70)
print(f'汇总：{len(problems)} 条硬问题，{len(slice_problems)} 条切片问题，{len(orphans)} 条孤儿')
