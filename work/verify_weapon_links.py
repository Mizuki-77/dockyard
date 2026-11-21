# 验证「舰 -> 武器」跳转全部可用。
#
# 光看有没有生成 <a> 不够：href 拼错时 build 不报错、页面照样生成，
# 点进去才 404。所以这里把每个 href 提出来，逐个确认目标页面真的存在。
import io
import os
import re

SHIPS = ['bismarck', 'tirpitz', 'akagi', 'kaga', 'soryu', 'hiryu',
         'hood', 'illustrious', 'king-george-v', 'enterprise', 'yorktown', 'hornet']
CLASSES = ['bismarck', 'tirpitz', 'akagi', 'kaga', 'soryu', 'illustrious',
           'king-george-v', 'yorktown', 'admiral']

total_links = 0
broken = []
no_link_pages = []

print(f'{"页面":<28} {"武器链接":<8} {"炮位链接":<8} {"死链"}')
print('-' * 62)

for kind, ids, base in [('ships', SHIPS, 'dist/ships'), ('classes', CLASSES, 'dist/classes')]:
    for sid in ids:
        p = f'{base}/{sid}/index.html'
        if not os.path.exists(p):
            continue
        h = io.open(p, encoding='utf-8').read()

        wlinks = re.findall(r'href="(/weapons/[^"#]+)(#[^"]*)?"', h)
        weapon_hrefs = [a for a, b in wlinks]
        mount_hrefs = [a + b for a, b in wlinks if b]

        bad = []
        for href in set(weapon_hrefs):
            target = 'dist' + href.rstrip('/') + '/index.html'
            if not os.path.exists(target):
                bad.append(href)

        n_weapon = len(set(weapon_hrefs))
        total_links += n_weapon
        if n_weapon == 0:
            no_link_pages.append(f'{kind}/{sid}')
        if bad:
            broken.extend([(kind, sid, b) for b in bad])

        flag = 'OK' if not bad else f'{len(bad)} 死链'
        print(f'{kind}/{sid:<20} {n_weapon:<8} {len(set(mount_hrefs)):<8} {flag}')

print()
print(f'武器链接总计: {total_links}')
if broken:
    print('死链:')
    for k, s, b in broken:
        print(f'  {k}/{s} -> {b}')
else:
    print('无死链')

if no_link_pages:
    print(f'没有武器链接的页面: {no_link_pages}')
