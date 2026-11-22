import io
import re

h = io.open('dist/index.html', encoding='utf-8').read()

print('=== 新侧栏是否渲染 ===')
for k in ['sitemap', '舰艇', '战役', '按类别浏览']:
    print(f'  {k}: {"有" if k in h else "缺"}')

print()
print('=== 舰艇清单（按国家）===')
groups = re.findall(r'class="smgroup__nation">([^<]+)<.*?class="smgroup__list">(.*?)</ul>',
                    h, re.S)
for name, body in groups:
    links = re.findall(r'class="smlink"[^>]*>([^<]+)<', body)
    print(f'  {name}: {", ".join(links)}')

print()
print('=== 战役与进度 ===')
rows = re.findall(r'class="smlink smlink--row"[^>]*><span>([^<]+)</span><span[^>]*>(\d+/\d+)</span>', h)
for name, prog in rows:
    print(f'  {name}: {prog}')

print()
print('=== 横切入口 ===')
cuts = re.findall(r'class="smcut__label">([^<]+)</span><span class="smcut__n">(\d+)<', h)
for name, n in cuts:
    print(f'  {name}: {n}')
rows2 = re.findall(r'class="smrowlink"[^>]*>\s*([^<]+?)\s*(?:<span class="smrowlink__n">(\d+)</span>)?\s*(?:型)?\s*→', h)
for r in rows2:
    print(f'  链接: {r}')

print()
print('=== 旧 SideNav 是否已移除 ===')
print(f'  sidenav 出现次数: {h.count("sidenav")}')
print(f'  旧 navItems 残留: {"有" if "快捷导航" in h else "无"}')
