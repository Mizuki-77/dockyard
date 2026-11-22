# 找「数组/对象被直接渲染」的隐患。
#
# 2026-11-22 修正版：初版误报太多，把数字类型的 sources 也报了。
# 现在按已知的类型来源做白名单：
#   stats() 返回的 s.sources / s.facts 等都是数字（.length 的结果）
#   tree.ts 的 leaf.sources 也是数字
#   sources={...} 形式的 <Xxx     是传给组件的 props，不是渲染
import glob
import io
import re

# 已知是数字的字段名（stats() 与 tree.ts 的产物）
NUMERIC_FIELDS = {'s.sources', 's.facts', 's.ships', 's.classes',
                  's.narratives', 's.fields',
                  'w.sources', 'x.sources', 'n.sources'}

# 真正会导致 [object Object] 的模式：数组字段名直接放进 {} 且没有 .length/.map/.join
ARRAY_FIELDS = ['designations', 'categories', 'classIds', 'shipIds',
                'mounts', 'windows', 'pairs', 'alts', 'positions']

found = 0
for p in glob.glob('src/**/*.astro', recursive=True):
    lines = io.open(p, encoding='utf-8').read().split('\n')
    for i, line in enumerate(lines, 1):
        # 跳过组件 props（形如 xxx={yyy} 而非 >{yyy}<）
        for fld in ARRAY_FIELDS:
            pat = r'>\{[a-zA-Z_][\w.]*\.' + fld + r'\}<'
            if re.search(pat, line):
                print(f'{p}:{i}  [数组 .{fld} 直接渲染]')
                print(f'    {line.strip()[:100]}')
                found += 1

        # 数组与数字比较
        for fld in ARRAY_FIELDS + ['src', 'facts']:
            pat = r'\.' + fld + r'\s*[><]=?\s*\d'
            if re.search(pat, line):
                print(f'{p}:{i}  [数组 .{fld} 与数字比较，永远为假]')
                print(f'    {line.strip()[:100]}')
                found += 1

print()
if found == 0:
    print('✓ 未发现数组被直接渲染的隐患')
else:
    print(f'共 {found} 处需要人工确认')
