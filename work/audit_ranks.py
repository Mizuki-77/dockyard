import glob
import io

import yaml

print('=== summary 提到「将官/元帅」，检查 rank_final 是否够格 ===')
ADMIRAL_WORDS = ('将官', '元帅', '中将', '少将', '上将')
for p in sorted(glob.glob('data/commanders/*.yaml')):
    d = yaml.safe_load(io.open(p, encoding='utf-8'))
    s = str(d.get('summary_zh') or '')
    rf = str(d.get('rank_final') or '')
    if not any(w in s for w in ADMIRAL_WORDS):
        continue
    flag = 'OK'
    if '将' in s and not any(w in rf for w in ('Admiral', 'Vizeadmiral', 'Admiral')):
        flag = '?? 摘要说将官但 rank_final 不是'
    if '元帅' in s and 'Admiral of the Fleet' not in rf:
        flag = '?? 摘要说元帅但 rank_final 不符'
    print(f"  {d['id']:<22} {rf:<30} {flag}")
    print(f"     {s}")

print()
print('=== 全部 13 人的 rank_final / rank_at_post ===')
for p in sorted(glob.glob('data/commanders/*.yaml')):
    d = yaml.safe_load(io.open(p, encoding='utf-8'))
    print(f"  {d['id']:<22} final={str(d.get('rank_final')):<28} at_post={d.get('rank_at_post')}")
