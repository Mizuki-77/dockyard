import glob
import io
import os

ORPHANS = [
    'yamato-1945-explosion.jpg',
    'yamato-1941-trials-sukumo.jpg',
    'yamato-1945-under-attack.jpg',
    'yamato-1944-samar.jpg',
    'iowa-1944-broadside.jpg',
    'missouri-1945-pacific.jpg',
]

print('精确检查这 6 个文件名是否被任何页面引用：')
for f in ORPHANS:
    hits = []
    for p in glob.glob('dist/**/*.html', recursive=True):
        h = io.open(p, encoding='utf-8').read()
        if f'"/img/ships/{f}"' in h:
            hits.append(p)
    mark = '✓ 未引用' if not hits else f'✗ 被 {len(hits)} 个页面引用: {hits[:3]}'
    print(f'  {f:<38} {mark}')
