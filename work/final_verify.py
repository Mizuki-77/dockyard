import io
import os
import re

SHIPS = ['rodney', 'prince-of-wales', 'prinz-eugen']
WEAPONS = ['16in-45-mk1', '6in-50-mk22', '47in-40-mk8', '20-3cm-sk-c34']

print('=' * 66)
print('三艘新舰')
print('=' * 66)
print(f'{"舰":<18} {"图":<4} {"正文段":<7} {"历史条":<7} {"武器":<5} {"篇幅"}')
print('-' * 60)
for sid in SHIPS:
    p = f'dist/ships/{sid}/index.html'
    if not os.path.exists(p):
        print(f'{sid}: 缺失')
        continue
    h = io.open(p, encoding='utf-8').read()
    imgs = len(set(re.findall(r'src="(/img/ships/[^"]+)"', h)))
    paras = len(re.findall(r'class="prose__p"', h))
    events = len(re.findall(r'class="histev__item"', h))
    wpns = len(set(re.findall(r'href="/weapons/([^"/]+)/"', h)))
    body = re.search(r'<main.*?</main>', h, re.S)
    tl = len(re.sub(r'<[^>]+>', '', body.group(0))) if body else 0
    print(f'{sid:<18} {imgs:<4} {paras:<7} {events:<7} {wpns:<5} {tl}')

print()
print('=' * 66)
print('四型新武器')
print('=' * 66)
print(f'{"武器":<18} {"图":<4} {"正文段":<7} {"历史":<5} {"装舰数"}')
print('-' * 60)
for wid in WEAPONS:
    p = f'dist/weapons/{wid}/index.html'
    if not os.path.exists(p):
        print(f'{wid}: 缺失')
        continue
    h = io.open(p, encoding='utf-8').read()
    has_img = f'/img/weapons/{wid}-primary.jpg' in h
    paras = len(re.findall(r'class="prose__block"', h))
    hist = h.count('histsect')
    ships = len(set(re.findall(r'href="/ships/([a-z0-9-]+)"', h)))
    print(f'{wid:<18} {"Y" if has_img else "N":<4} {paras:<7} {hist:<5} {ships}')

print()
print('=' * 66)
print('战役覆盖')
print('=' * 66)
for b, total in [('denmark-strait', 4), ('last-battle', 13), ('midway', 7)]:
    p = f'dist/battles/{b}/index.html'
    if not os.path.exists(p):
        continue
    h = io.open(p, encoding='utf-8').read()
    links = sorted(set(re.findall(r'href="(/ships/[a-z0-9-]+)"', h)))
    notes = len(re.findall(r'class="side__note"', h))
    print(f'  {b:<16} 可点 {len(links)}/{total}  未收录说明 {notes} 条')
    print(f'  {"":<16} {", ".join(x.replace("/ships/","") for x in links)}')
