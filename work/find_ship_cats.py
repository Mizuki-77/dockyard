# 用搜索确定 18 艘新舰的真实 Commons 分类名与图片数
# 上一轮我猜的下水年全错（利根 1938 而非 1937），所以必须搜而不是猜
import time

from commons_client import cat_files, search_cats

# 舰 id → 搜索词
QUERIES = {
    'tone': 'Tone class cruiser Japanese',
    'chikuma': 'Chikuma cruiser Japanese',
    'haruna': 'Haruna battleship Japanese',
    'kirishima': 'Kirishima battleship Japanese',
    'hosho': 'Hosho aircraft carrier Japanese',
    'nagara': 'Nagara class cruiser',
    'sendai': 'Sendai class cruiser',
    'astoria': 'USS Astoria CA-34',
    'portland': 'USS Portland CA-33',
    'minneapolis': 'USS Minneapolis CA-36',
    'new-orleans': 'USS New Orleans CA-32',
    'vincennes': 'USS Vincennes CA-44',
    'northampton': 'USS Northampton CA-26',
    'pensacola': 'USS Pensacola CA-24',
    'atlanta': 'USS Atlanta CL-51',
    'hammann': 'USS Hammann DD-412',
    'monaghan': 'USS Monaghan DD-354',
    'benham': 'USS Benham DD-397',
}

results = {}
for sid, term in QUERIES.items():
    print(f'\n=== {sid}  (搜: {term})')
    try:
        cats = search_cats(term, limit=8)
    except Exception as e:
        print('   搜索失败', type(e).__name__)
        continue
    time.sleep(2)
    best = None
    for c in cats:
        if not c.startswith('Category:'):
            continue
        name = c[9:]
        # 排除明显的非本舰分类（舰级页、同名旧舰）
        try:
            files = cat_files(name, limit=500)
        except Exception:
            files = []
        time.sleep(1.5)
        imgs = [f for f in files if not f.lower().endswith(('.ogv', '.webm', '.ogg'))]
        tag = '' if imgs else ' 空'
        print(f'     {len(imgs):>4} 张  {name}{tag}')
        if imgs and (best is None or len(imgs) > best[1]):
            best = (name, len(imgs))
    if best:
        results[sid] = best
        print(f'   → 选 {best[0]}（{best[1]} 张）')

print('\n\n===== 汇总 =====')
tot = 0
for sid, (cat, n) in results.items():
    print(f'  {sid:14} {cat:34} {n:>4}')
    tot += n
print(f'  合计素材 {tot} 张，18 舰 × 10-15 张 = 180-270 张目标')
