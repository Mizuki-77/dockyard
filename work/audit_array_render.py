# 找「数组/对象被直接渲染成大括号表达式」的隐患。
# 典型模式：{xxx.sources} / {xxx.href} 这种在 JSX 里直接插数组或对象。
import glob
import io
import re

PATTERNS = [
    (r'\{[a-zA-Z_][\w.]*\.sources\}', '数组直接渲染（应为 .length）'),
    (r'\{[a-zA-Z_][\w.]*\.designations\}', '数组直接渲染'),
    (r'\{[a-zA-Z_][\w.]*\.categories\}', '数组直接渲染'),
    (r'\{[a-zA-Z_][\w.]*\.classIds\}', '数组直接渲染'),
    (r'\{[a-zA-Z_][\w.]*\.shipIds\}', '数组直接渲染'),
    (r'\{[a-zA-Z_][\w.]*\.facts\}', '数组直接渲染'),
    (r'\{[a-zA-Z_][\w.]*\.mounts\}', '数组直接渲染'),
    (r'\{[a-zA-Z_][\w.]*\.windows\}', '数组直接渲染'),
    (r'\{[a-zA-Z_][\w.]*\.src\}', '数组直接渲染'),
    (r'\{\s*[a-zA-Z_][\w.]*\s*>\s*\d+\s*\}', '数组与数字比较（永远 false）'),
]

found = 0
for p in glob.glob('src/**/*.astro', recursive=True):
    lines = io.open(p, encoding='utf-8').read().split('\n')
    for i, line in enumerate(lines, 1):
        for pat, desc in PATTERNS:
            for m in re.finditer(pat, line):
                # 排除 .length / .map / .join 等合法用法
                seg = m.group(0)
                if '.length' in seg:
                    continue
                print(f'{p}:{i}  [{desc}]')
                print(f'    {line.strip()[:100]}')
                found += 1

print()
print(f'共 {found} 处可疑')
