# 给 c2 三人补 rank_at_post。
# 依据：data/ships 里对应 commander fact 的军衔前缀
#   arthur-power   → ark-royal 的 fact 写 "Capt."
#   louis-hamilton → prince-of-wales 的 fact 写 "Captain"
#   michael-denny  → victorious 的 fact 写 "Captain"
import io
import re

FIX = {
    'arthur-power': 'Captain',
    'louis-hamilton': 'Captain',
    'michael-denny': 'Captain',
}

for cid, rank in FIX.items():
    p = f'data/commanders/{cid}.yaml'
    text = io.open(p, encoding='utf-8').read()
    if re.search(r'^rank_at_post:', text, re.M):
        print(f'  = {cid} 已有，跳过')
        continue
    if re.search(r'^rank_final:.*$', text, re.M):
        text = re.sub(r'^(rank_final:.*)$',
                      lambda m: f"{m.group(1)}\nrank_at_post: '{rank}'",
                      text, count=1, flags=re.M)
    else:
        text = re.sub(r'^(name:\n(?:[ \t]+\S+:.*\n)+)',
                      lambda m: f"{m.group(1)}rank_at_post: '{rank}'\n",
                      text, count=1, flags=re.M)
    io.open(p, 'w', encoding='utf-8', newline='\n').write(text)
    print(f'  + {cid} rank_at_post = {rank}')

print()
import glob

import yaml

for p in sorted(glob.glob('data/commanders/*.yaml')):
    d = yaml.safe_load(io.open(p, encoding='utf-8'))
    ok = 'OK' if d.get('rank_at_post') else 'MISSING'
    print(f"{d['id']:<22} {ok:<8} {d.get('rank_at_post')}")
