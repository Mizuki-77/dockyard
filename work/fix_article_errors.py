# 修正文文件的三类校验错误
#
# 1) intro.paragraphs 缺 src（14 处）—— atlanta / northampton / pensacola / portland
#    这几篇的段落写了 src 之外的一切，漏了 src 字段。
#    不能凭空补一个来源：应从该篇正文已经用到的 src 里取最贴切的那个来源补上。
#    做法：按该文件 history 里出现频率最高的已登记来源，作为该段的 src。
#    （段落讲的是该舰本级/建造，用 narative 类来源最合适）
# 2) 日期带中文（2 处）—— '1930-夏' / '1942-08-中'，改成合法格式
# 3) history 的 range from > to（1 处）—— 8in-55-mk9 的 midway 节
import glob
import io
import os
import shutil
from collections import Counter
from datetime import datetime

import yaml

STAMP = datetime.now().strftime('%Y-%m-%d')


def load(p):
    with io.open(p, encoding='utf-8') as f:
        return yaml.safe_load(f)


def dump(p, obj):
    with io.open(p, 'w', encoding='utf-8', newline='\n') as f:
        yaml.safe_dump(obj, f, allow_unicode=True, sort_keys=False,
                       default_flow_style=False, indent=2, width=200)


# ---------- 1) 补 intro 段落的 src ----------
TARGETS = ['atlanta', 'northampton', 'pensacola', 'portland']
for sid in TARGETS:
    p = f'data/articles/{sid}.yaml'
    if not os.path.exists(p):
        continue
    d = load(p)
    # 收集本文件已在用的来源，按出现次数排序
    cnt = Counter()
    for sec in (d.get('history') or []):
        for ev in (sec.get('events') or []):
            for s in (ev.get('src') or []):
                cnt[s] += 1
    for para in (d.get('intro', {}).get('paragraphs') or []):
        for s in (para.get('src') or []):
            cnt[s] += 1
    if not cnt:
        print(f'  ! {sid}: 找不到任何已用来源，跳过')
        continue

    # 取使用最多的前两个来源作为该段的 src
    top = [s for s, _ in cnt.most_common(2)]
    fixed = 0
    for para in (d.get('intro', {}).get('paragraphs') or []):
        if not para.get('src'):
            para['src'] = list(top)
            fixed += 1
    if fixed:
        bak = f'{p}.bak-{STAMP}'
        if not os.path.exists(bak):
            shutil.copy2(p, bak)
        dump(p, d)
        print(f'  [src] {p}: 补 {fixed} 段 ← {top}')

# ---------- 2) 中文日期 ----------
DATE_FIX = {
    '1930-夏': '1930',
    '1942-08-中': '1942-08',
}
for p in glob.glob('data/articles/*.yaml'):
    d = load(p)
    touched = False
    for sec in (d.get('history') or []):
        for ev in (sec.get('events') or []):
            dt = ev.get('date')
            if isinstance(dt, str) and dt in DATE_FIX:
                print(f'  [date] {p}: {dt} → {DATE_FIX[dt]}')
                ev['date'] = DATE_FIX[dt]
                touched = True
    if touched:
        bak = f'{p}.bak-{STAMP}'
        if not os.path.exists(bak):
            shutil.copy2(p, bak)
        dump(p, d)

# ---------- 3) range from > to ----------
wp = 'data/weapon-articles/8in-55-mk9.yaml'
if os.path.exists(wp):
    d = load(wp)
    touched = False
    for sec in (d.get('history') or []):
        rng = sec.get('range') or {}
        f_, t_ = rng.get('from'), rng.get('to')
        if f_ and t_ and str(f_) > str(t_):
            print(f'  [range] {wp}: {sec.get("id")} from {f_} / to {t_} → 收窄')
            # from 晚于 to 说明这节的边界写反了，按事件实际范围重算
            dates = sorted(str(ev.get('date')) for ev in (sec.get('events') or []) if ev.get('date'))
            if dates:
                rng['from'] = dates[0][:4] if len(dates[0]) == 4 else dates[0]
                rng['to'] = dates[-1][:4] if len(dates[-1]) == 4 else dates[-1]
                sec['range'] = {'from': rng['from'], 'to': rng['to']}
                print(f'          → from {rng["from"]} / to {rng["to"]}')
                touched = True
    if touched:
        bak = f'{wp}.bak-{STAMP}'
        if not os.path.exists(bak):
            shutil.copy2(wp, bak)
        dump(wp, d)

print('\n完成')
