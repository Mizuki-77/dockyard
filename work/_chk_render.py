import io
import os
import re

print('页面引用图片数（抽查）：')
for sid in ['tone', 'chikuma', 'haruna', 'hosho', 'minneapolis', 'atlanta',
            'hammann', 'benham', 'new-orleans']:
    p = f'dist/ships/{sid}/index.html'
    if not os.path.exists(p):
        print(f'  {sid:14} 页面不存在')
        continue
    t = io.open(p, encoding='utf-8').read()
    pat = re.compile(r'/img/ships/' + re.escape(sid) + r'-\d+[^"\')\s]*')
    imgs = set(pat.findall(t))
    print(f'  {sid:14} {len(imgs)} 张')
