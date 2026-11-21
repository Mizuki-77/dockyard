# 查哪些舰详情页真的渲染了「武器配置」区。
import io
import os

print(f'{"舰":<20} {"armament 区":<12} {"武器卡片"}')
print('-' * 44)

for d in sorted(os.listdir('dist/ships')):
    p = f'dist/ships/{d}/index.html'
    if not os.path.exists(p) or not os.path.isdir(f'dist/ships/{d}'):
        continue
    h = io.open(p, encoding='utf-8').read()
    has_sec = 'id="armament"' in h
    n = h.count('class="weapon"') + h.count('class="weapon ')
    print(f'{d:<20} {"有" if has_sec else "无":<12} {n}')
