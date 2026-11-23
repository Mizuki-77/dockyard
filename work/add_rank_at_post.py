# 给每位指挥官补 rank_at_post（担任所录舰职时的军衔）。
#
# 依据：data/ships/*.yaml 里 service.commander 那条 fact 的前缀军衔，
# 那是「他在这艘舰上时的实际军衔」，比 rank_final（最终军衔）更贴合
# 「战舰指挥官」这个栏目的语义。
#
# 不逐个手改 YAML，而是脚本插入：13 个文件、字段位置固定（name 之后）。
import glob
import io
import re

import yaml

# 从原始 fact 里读出每人当舰长时的军衔
AT_POST = {}
for p in glob.glob('data/ships/*.yaml'):
    if '.bak' in p:
        continue
    d = yaml.safe_load(io.open(p, encoding='utf-8')) or {}
    for f in d.get('facts') or []:
        if f.get('field') != 'service.commander':
            continue
        v = str(f.get('value') or '')
        m = re.match(
            r'^(Kapitän zur See|Kpt\.z\.S\.|Korvettenkapitän|K\.Kpt\.|'
            r'kmdr por\.|kmdr ppor\.|kmdr|'
            r'Captain|Capt\.|Commander|Cdr\.|Lieutenant|Lt\.)\s*\.?\s*(.+)$', v)
        if not m:
            continue
        rank, rest = m.group(1).rstrip('.'), m.group(2)
        rest = rest.split('（')[0].split('(')[0].strip()
        rest = re.sub(r'(,\s*(?:[A-Z]{2,4}\*?|[A-Z][a-z]{1,3}\*?)\s*)+$', '', rest).strip(' ,')
        AT_POST[rest.lower()] = rank

print(f'从舰文件读到 {len(AT_POST)} 个人名对应的当职军衔')
for k, v in sorted(AT_POST.items()):
    print(f'  {v:<22} {k}')

print()

# 13 位入选者的人工对照：档案 id → 匹配用的姓名（档案件里的 name.en）
MATCH = {
    'augustus-agar': 'Augustus Willington Shelton Agar',
    'philip-vian': 'Philip Louis Vian',
    'robert-sherbrooke': 'Robert St. Vincent Sherbrooke',
    'ernst-lindemann': 'Ernst Lindemann',
    'helmuth-brinkmann': 'Helmuth Brinkmann',
    'karl-topp': 'Karl Topp',
    'benjamin-martin': 'Benjamin Charles Stanley Martin',
    'eugeniusz-plawski': 'Eugeniusz Józef Stanisław Pławski',
    'richard-taylor-white': 'Richard Taylor White',
    'wolf-junge': 'Wolf Junge',
    'arthur-power': 'Arthur John Power',
    'louis-hamilton': 'Louis Henry Keppel Hamilton',
    'michael-denny': 'Michael Maynard Denny',
}

# 少数人的当职军衔在舰文件里写法不同，人工兜底
MANUAL = {
    'arthur-power': 'Captain',
    'louis-hamilton': 'Captain',
    'michael-denny': 'Captain',
}

changed = 0
for p in sorted(glob.glob('work/staging_cmdr/c*/commanders/*.yaml')):
    text = io.open(p, encoding='utf-8').read()
    d = yaml.safe_load(text)
    cid = d.get('id')
    if not cid or cid not in MATCH:
        continue
    if d.get('rank_at_post'):
        continue

    # 找当职军衔
    rank = MANUAL.get(cid)
    if not rank:
        target = MATCH[cid].lower()
        # 先精确匹配，再退到「姓相同」
        if target in AT_POST:
            rank = AT_POST[target]
        else:
            surname = target.split()[-1]
            for k, v in AT_POST.items():
                if k.split()[-1] == surname:
                    rank = v
                    break
    if not rank:
        print(f'  ! {cid}: 查不到当职军衔，跳过')
        continue

    # 插到 rank_final 那行之后；没有 rank_final 就插到 name 块之后
    if re.search(r'^rank_final:.*$', text, re.M):
        text = re.sub(
            r'^(rank_final:.*)$',
            lambda m: f"{m.group(1)}\nrank_at_post: '{rank}'",
            text, count=1, flags=re.M)
    else:
        text = re.sub(
            r'^(name:\n(?:[ \t]+\S+:.*\n)+)',
            lambda m: f"{m.group(1)}rank_at_post: '{rank}'\n",
            text, count=1, flags=re.M)

    io.open(p, 'w', encoding='utf-8', newline='\n').write(text)
    changed += 1
    print(f'  + {cid:<22} rank_at_post = {rank}')

print()
print(f'已补 {changed} 个文件')
