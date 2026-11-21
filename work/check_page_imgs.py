import io
import os
import re

SHIPS = ['akagi', 'bismarck', 'enterprise', 'hiryu', 'hornet', 'illustrious',
         'kaga', 'king-george-v', 'prince-of-wales', 'prinz-eugen', 'rodney',
         'soryu', 'tirpitz', 'yorktown']

print(f'{"舰":<18} {"页面图数":<10} {"图集区":<8}')
print('-' * 40)
total = 0
for sid in SHIPS:
    p = f'dist/ships/{sid}/index.html'
    if not os.path.exists(p):
        print(f'{sid:<18} 缺失')
        continue
    h = io.open(p, encoding='utf-8').read()
    imgs = set(re.findall(r'src="(/img/ships/[^"]+)"', h))
    n = len(imgs)
    total += n
    has_gallery = 'id="gallery"' in h
    print(f'{sid:<18} {n:<10} {"Y" if has_gallery else "N"}')
print(f'\n页面图总数 {total}')
