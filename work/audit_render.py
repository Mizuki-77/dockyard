# 页面渲染体检：找渲染层的脏数据。
#
# 检查每页 HTML 里有没有：
#   NaN / undefined / null / [object Object] / Infinity
#   以及空区块（有 section 标题但正文为空）
import glob
import io
import re
from collections import defaultdict

BAD_TOKENS = ['undefined', 'NaN', '[object Object]', 'Infinity', 'null,']

hits = defaultdict(list)
empty_sections = defaultdict(list)

for p in glob.glob('dist/**/*.html', recursive=True):
    h = io.open(p, encoding='utf-8').read()
    # 去掉 <script> / <style> 内容再查（脚本里的 undefined 是正常的）
    body = re.sub(r'<script[\s\S]*?</script>', '', h)
    body = re.sub(r'<style[\s\S]*?</style>', '', body)

    for tok in BAD_TOKENS:
        for m in re.finditer(re.escape(tok), body):
            # 取上下文
            s = max(0, m.start() - 40)
            ctx = body[s:m.end() + 40].replace('\n', ' ')
            hits[p].append((tok, ctx))

print('=' * 72)
print('1) 渲染出的脏数据')
total = 0
for p, items in sorted(hits.items()):
    total += len(items)
    print(f'\n  {p}')
    seen = set()
    for tok, ctx in items[:3]:
        key = (tok, ctx[:60])
        if key in seen:
            continue
        seen.add(key)
        print(f'    [{tok}] ...{ctx}...')
if total == 0:
    print('  ✓ 无')

print()
print('=' * 72)
print('2) 空区块（section 有标题但没内容）')
# 简化判断：<section ...> 后紧跟 </section>，或中间只有空白/标题
for p in glob.glob('dist/**/*.html', recursive=True):
    h = io.open(p, encoding='utf-8').read()
    for m in re.finditer(r'<section[^>]*>(.*?)</section>', h, re.S):
        inner = m.group(1)
        # 去掉标题结构后还剩多少可见文字
        text = re.sub(r'<[^>]+>', '', inner)
        text = re.sub(r'\s+', '', text)
        if len(text) < 6:
            empty_sections[p].append(text[:20])

cnt = sum(len(v) for v in empty_sections.values())
for p, items in sorted(empty_sections.items()):
    print(f'  {p}: {len(items)} 个空 section')
if cnt == 0:
    print('  ✓ 无')

print()
print('=' * 72)
print('3) 页面标题与描述')
missing_title = []
for p in glob.glob('dist/**/*.html', recursive=True):
    h = io.open(p, encoding='utf-8').read()
    m = re.search(r'<title>([^<]*)</title>', h)
    if not m or not m.group(1).strip():
        missing_title.append(p)
print(f'  缺 title: {len(missing_title)}')
for x in missing_title[:5]:
    print(f'    {x}')

print()
print('=' * 72)
print('4) h1 数量（每页应恰好 1 个）')
multi_h1 = []
no_h1 = []
for p in glob.glob('dist/**/*.html', recursive=True):
    h = io.open(p, encoding='utf-8').read()
    n = len(re.findall(r'<h1[\s>]', h))
    if n == 0:
        no_h1.append(p)
    elif n > 1:
        multi_h1.append((p, n))
print(f'  0 个 h1: {len(no_h1)}')
for x in no_h1[:8]:
    print(f'    {x}')
print(f'  多个 h1: {len(multi_h1)}')
for x, n in multi_h1[:8]:
    print(f'    {x}  ({n} 个)')

print()
print('=' * 72)
print(f'汇总：脏数据 {total} 处，空区块 {cnt} 个，缺 title {len(missing_title)}，'
      f'缺 h1 {len(no_h1)}，多 h1 {len(multi_h1)}')
