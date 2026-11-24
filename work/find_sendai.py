# 补查川内分类（上一条搜索返回空）
import time

from commons_client import cat_files, search_cats

for term in ['Sendai cruiser 1923', 'Japanese cruiser Sendai', 'Sendai class light cruiser']:
    print(f'=== {term}')
    try:
        cats = search_cats(term, limit=10)
    except Exception as e:
        print('  失败', type(e).__name__)
        continue
    for c in cats:
        print('   ', c)
    time.sleep(2)
    for c in cats:
        if 'Sendai' in c and c.startswith('Category:'):
            try:
                f = cat_files(c[9:], limit=300)
            except Exception:
                f = []
            imgs = [x for x in f if not x.lower().endswith(('.ogv', '.webm', '.ogg'))]
            print(f'      [{len(imgs)} 张] {c}')
            time.sleep(1.5)
