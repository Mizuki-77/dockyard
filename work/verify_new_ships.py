import io
import os
import re

SHIPS = ['rodney', 'prince-of-wales', 'prinz-eugen']

print(f'{"舰":<18} {"页":<4} {"图":<4} {"简介段":<6} {"历史条":<6} {"字数":<7} {"武器":<5} {"报错":<5}')
print('-' * 70)

for sid in SHIPS:
    p = f'dist/ships/{sid}/index.html'
    if not os.path.exists(p):
        print(f'{sid:<18} 页面缺失')
        continue
    h = io.open(p, encoding='utf-8').read()

    has_img = bool(re.search(r'<img[^>]+src="/img/ships/', h))
    paras = len(re.findall(r'class="prose__block"', h))
    events = len(re.findall(r'class="histev__item"', h))
    weapons = len(re.findall(r'href="/weapons/[^"]+"', h))
    rept = len(re.findall(r'class="rept', h))

    body = re.search(r'<main.*?</main>', h, re.S)
    text_len = len(re.sub(r'<[^>]+>', '', body.group(0))) if body else 0

    print(f'{sid:<18} {"Y":<4} {"Y" if has_img else "N":<4} {paras:<6} {events:<6} {text_len:<7} {weapons:<5} {rept:<5}')

print()
# 战役页是否挂上了
print('=== 战役页的舰船链接 ===')
for b in ['denmark-strait', 'last-battle']:
    p = f'dist/battles/{b}/index.html'
    if not os.path.exists(p):
        continue
    h = io.open(p, encoding='utf-8').read()
    links = sorted(set(re.findall(r'href="(/ships/[a-z-]+)"', h)))
    notes = len(re.findall(r'class="side__note"', h))
    print(f'  {b:<16} 可点 {len(links)} 艘: {", ".join(x.replace("/ships/","") for x in links)}')
    print(f'  {"":<16} 未收录说明 {notes} 条')
