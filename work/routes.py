import glob, sys, io, os
from collections import Counter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

routes = []
for p in sorted(glob.glob('dist/**/index.html', recursive=True)):
    rel = p.replace('\\', '/').replace('dist/', '').replace('/index.html', '')
    routes.append('/' + (rel if rel else ''))
print(len(routes), 'pages')

groups = Counter()
for r in routes:
    seg = r.strip('/').split('/')[0] or '(root)'
    groups[seg] += 1
for k, v in sorted(groups.items()):
    print(f'  /{k:12} {v}')

print()
print('=== 全部路由 ===')
for r in routes:
    print(' ', r)
