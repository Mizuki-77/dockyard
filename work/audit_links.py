# 全站链接与锚点体检。
#
# 查四类问题：
#   1. 内部链接指向不存在的页面
#   2. 锚点（#xxx）在目标页里不存在
#   3. 站内图片文件缺失
#   4. 外链是否为空 / 非法
import io
import os
import re
from collections import defaultdict

ROOT = '.'
DIST = 'dist'

# 收集所有生成的页面
pages = {}
for dirpath, _, files in os.walk(DIST):
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(dirpath, f)
            rel = p[len(DIST):].replace('\\', '/')
            if rel.endswith('/index.html'):
                rel = rel[:-len('index.html')]
            pages[rel] = p

print(f'共 {len(pages)} 个页面')

# 每个页面的锚点集合
anchors = {}
for rel, p in pages.items():
    h = io.open(p, encoding='utf-8').read()
    ids = set(re.findall(r'\bid="([^"]+)"', h))
    anchors[rel] = ids

def norm(href):
    """把 href 归一成页面 key。"""
    href = href.split('?')[0]
    if not href.startswith('/'):
        return None
    frag = None
    if '#' in href:
        href, frag = href.split('#', 1)
    if not href.endswith('/'):
        # /ships/bismarck -> /ships/bismarck/
        if href and not href.endswith('.html') and '.' not in href.split('/')[-1]:
            href += '/'
    return href, frag

broken_page = defaultdict(set)
broken_anchor = defaultdict(set)
broken_img = defaultdict(set)
bad_href = defaultdict(set)

for rel, p in pages.items():
    h = io.open(p, encoding='utf-8').read()

    # 内部链接
    for m in re.finditer(r'href="([^"]*)"', h):
        raw = m.group(1)
        if not raw or raw.startswith(('http://', 'https://', 'mailto:', 'javascript:')):
            continue
        if raw.startswith('#'):
            # 同页锚点
            frag = raw[1:]
            if frag and frag not in anchors.get(rel, set()):
                broken_anchor[rel].add(raw)
            continue
        r = norm(raw)
        if not r:
            continue
        target, frag = r
        if target not in pages:
            # 可能是目录/静态资源，排除
            if not target.endswith('/'):
                continue
            broken_page[rel].add(target)
            continue
        if frag and frag not in anchors.get(target, set()):
            broken_anchor[rel].add(f'{target}#{frag}')

    # 图片
    for m in re.finditer(r'src="(/img/[^"]+)"', h):
        f = m.group(1)
        if not os.path.exists(ROOT + '/public' + f):
            broken_img[rel].add(f)

print()
print('=' * 70)
print(f'1) 指向不存在页面的内部链接: {sum(len(v) for v in broken_page.values())} 处')
for rel, s in sorted(broken_page.items()):
    print(f'   {rel}  ->  {sorted(s)[:5]}')

print()
print('=' * 70)
print(f'2) 锚点不存在: {sum(len(v) for v in broken_anchor.values())} 处')
for rel, s in sorted(broken_anchor.items()):
    print(f'   {rel}')
    for x in sorted(s)[:6]:
        print(f'      {x}')

print()
print('=' * 70)
print(f'3) 图片文件缺失: {sum(len(v) for v in broken_img.values())} 处')
for rel, s in sorted(broken_img.items()):
    print(f'   {rel}  ->  {sorted(s)[:5]}')

print()
print('=' * 70)
print('4) 空 href 或 #:')
empty = 0
for rel, p in pages.items():
    h = io.open(p, encoding='utf-8').read()
    for m in re.finditer(r'href="(#?)"', h):
        empty += 1
        if empty <= 5:
            print(f'   {rel}  href="{m.group(1)}"')
print(f'   共 {empty} 处')
