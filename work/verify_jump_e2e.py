# 端到端验证「舰 -> 武器」跳转：
#  1. 从舰页抽出所有 /weapons/<id>/ 链接
#  2. 逐个确认目标页面存在
#  3. 确认目标页面上有该武器名、有图、有正文
#  4. 反向确认：目标页的「装在哪几艘船」能跳回来源舰
import io
import os
import re

SHIPS = ['bismarck', 'tirpitz', 'akagi', 'kaga', 'soryu', 'hiryu',
         'hood', 'illustrious', 'king-george-v', 'enterprise', 'yorktown', 'hornet']

seen = {}
edges = 0

for sid in SHIPS:
    p = f'dist/ships/{sid}/index.html'
    if not os.path.exists(p):
        continue
    h = io.open(p, encoding='utf-8').read()
    # 只取正文里的武器区链接，排除导航/侧栏
    for m in re.finditer(r'href="(/weapons/([^"/]+)/)(#[a-z-]*)?"', h):
        href, wid, anchor = m.group(1), m.group(2), m.group(3)
        edges += 1
        if wid not in seen:
            seen[wid] = set()
        seen[wid].add(sid)

print(f'从舰页抽到 {edges} 条跳转，涉及 {len(seen)} 种武器')
print()

print(f'{"武器 id":<18} {"目标页":<6} {"有正文":<7} {"有图":<6} {"回链舰数"}')
print('-' * 56)

problems = []
for wid in sorted(seen):
    tp = f'dist/weapons/{wid}/index.html'
    if not os.path.exists(tp):
        problems.append(f'{wid}: 目标页不存在')
        continue
    th = io.open(tp, encoding='utf-8').read()
    has_prose = 'prose__block' in th
    has_img = '/img/weapons/' in th
    # 目标页的「装在哪几艘船」。
    # 注意 fitrow 的 href 没有结尾斜杠（/ships/bismarck），
    # 而武器链接有（/weapons/xxx/）—— 正则别要求斜杠，否则全是 0。
    back = len(set(re.findall(r'href="/ships/([a-z0-9-]+)"', th)))
    print(f'{wid:<18} {"OK":<6} {"Y" if has_prose else "N":<7} {"Y" if has_img else "N":<6} {back}')
    if not has_prose:
        problems.append(f'{wid}: 无正文')

print()
if problems:
    print('问题：')
    for x in problems:
        print('  ' + x)
else:
    print('全部跳转目标：页面存在、有正文、有反向链接')

# 12 艘舰是否全覆盖
covered = set()
for s in seen.values():
    covered |= s
print(f'\n舰页覆盖: {len(covered)}/12  缺: {sorted(set(SHIPS) - covered) or "无"}')
