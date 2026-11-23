import glob
import io

import yaml

have = {}
for p in glob.glob('data/ships/*.yaml'):
    if '.bak' in p:
        continue
    d = yaml.safe_load(io.open(p, encoding='utf-8'))
    have[d['id']] = d['name']['zh']

print(f'现有 {len(have)} 艘：')
for k, v in sorted(have.items()):
    print(f'  {k:<18} {v}')
print()

CANDS = {
    '日本（中途岛参战）': [
        '加贺', '赤城', '苍龙', '飞龙',
        '榛名', '雾岛', '利根', '筑摩', '长良', '川内',
        '凤翔', '隼鹰', '龙骧', '神通', '阿武隈',
    ],
    '美国（中途岛参战）': [
        '企业', '约克城', '大黄蜂',
        '波特兰', '亚特兰大', '明尼阿波利斯', '北安普敦', '彭萨科拉',
        '新奥尔良', '文森斯', '阿斯托里亚', '檀香山', '盐湖城',
        '哈曼', '莫纳汉', '本汉',
    ],
}

names = list(have.values())
for nation, lst in CANDS.items():
    print(f'-- {nation}')
    for n in lst:
        hit = [v for v in names if n in v]
        mark = ('已收录: ' + hit[0]) if hit else '未收录'
        print(f'   {n:<12} {mark}')
    print()
