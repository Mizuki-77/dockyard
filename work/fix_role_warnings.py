# 修 65 个警告：来源的 role 与实际用法不符
#
# 情况：
#   navypedia-portland  role=['lead']，note 写「本组未用它支撑任何 fact」
#                       —— 但 data/classes/portland.yaml 与 ships/portland.yaml
#                       实际有 61 条 fact 引它。note 是 11-23 抓取时的临时说法，已过时。
#   danfs-atlanta-brief role=['narrative']，但被用来支撑 3 条 fact（伤亡等数据）。
#
# 处理：按实际用法补 role: data。不删 fact、不压制警告 —— 警告说的是事实，改来源描述。
import io
import shutil
from datetime import datetime

import yaml

STAMP = datetime.now().strftime('%Y-%m-%d')
P = 'data/sources.yaml'

FIX = {
    'navypedia-portland': {
        'role': ['data', 'lead'],
        'note': (
            '波特兰级（波特兰/印第安纳波利斯）逐舰技术数据与改装记录。'
            '2026-11-24 补：本级与 CA-34/36 组同属新奥尔良级谱系的对照参照，'
            'classes/portland.yaml 与 ships/portland.yaml 的多条主尺度、动力、'
            '武备 fact 直接引自本页，故 role 由 lead 补为 data。'
        ),
    },
    'danfs-atlanta-brief': {
        'role': ['data', 'narrative'],
        'note': (
            '与 cl51.html 同源但内容不同的另一份 DANFS 短稿。'
            '两处独家信息：①中途岛期间「in the screen for Enterprise and Hornet, '
            'but these ships did not come under attack」；②伤亡 172 死 79 伤。'
            '长稿无伤亡数，故伤亡类 fact 只引本页，role 需含 data。'
        ),
    },
}


def load(p):
    with io.open(p, encoding='utf-8') as f:
        return yaml.safe_load(f)


def dump(p, obj):
    with io.open(p, 'w', encoding='utf-8', newline='\n') as f:
        yaml.safe_dump(obj, f, allow_unicode=True, sort_keys=False,
                       default_flow_style=False, indent=2, width=200)


d = load(P)
hit = 0
for s in d['sources']:
    sid = s.get('id')
    if sid in FIX:
        patch = FIX[sid]
        old = s.get('role')
        s['role'] = patch['role']
        s['note'] = patch['note']
        hit += 1
        print(f'  {sid}: role {old} → {s["role"]}')

d['updated'] = STAMP
shutil.copy2(P, f'{P}.bak3-{STAMP}')
dump(P, d)
print(f'\n修了 {hit} 条来源')
