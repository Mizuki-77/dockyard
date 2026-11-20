# 生成 images.yaml 的追加片段。
#
# 每条必须写清：file / subject / title / part / view / date / license +
# license_tier / license_raw / author / credit / source_url / width / height /
# primary / note。少一项页面上的授权信息就是空白的。

import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / 'work' / 'weaponimg'

picked = json.load(io.open(WORK / 'picked.json', encoding='utf-8'))

# 每型的中文标题与部位/视角/日期 —— 这些必须人工定，脚本猜不出
META = {
    'a6m2': {
        'title': ('零式舰战二一型自珍珠港起飞', 'A6M2 Model 21 taking off during the Pearl Harbor attack'),
        'part': 'aircraft', 'view': 'three_quarter', 'date': '1941-12-07',
        'note': '1941 年 12 月 7 日珍珠港攻击中，一架垂尾编号 A1-108 的零式舰战正在起飞（NHHC 80-G-182252）。',
    },
    'd3a1': {
        'title': ('九九式舰爆一一型在航母甲板上准备起飞', 'D3A1 Type 99 carrier bombers preparing to take off'),
        'part': 'aircraft', 'view': 'three_quarter', 'date': '1941-1942',
        'note': '甲板上列队的九九式舰爆。Commons 未标注具体日期与舰名，故 date 记为 1941-1942 区间。',
    },
    'b5n2': {
        'title': ('九七式舰攻一二型（战后被美军缴获试飞）', 'Captured B5N2 tested by the U.S. Navy'),
        'part': 'aircraft', 'view': 'side', 'date': '1945',
        'note': '战后被美军缴获、由海军航空试验中心（Patuxent River）试飞的 B5N2。涂装为美方测试用，不是原日军涂装。',
    },
    '25mm-96': {
        'title': ('九六式二十五粍高角机铳双联装阵地', 'Twin 25 mm Type 96 anti-aircraft mount'),
        'part': 'mount', 'view': 'detail', 'date': '1945-02-1945-03',
        'note': '硫磺岛战役期间的 25 mm 双联装阵地（USMC 127-GW-304-143496）。',
    },
    '20cm-3ns': {
        'title': ('高雄号前部 20 cm 主炮塔', 'Forward 20 cm turrets of the heavy cruiser Takao'),
        'part': 'turret', 'view': 'three_quarter', 'date': '1930s',
        'note': '高雄号前部一号、二号主炮塔与舰桥。20 cm/50 三年式 No.1 是条约时代日本重巡的标准主炮。',
    },
    '12cm-10ns': {
        'title': ('赤城号上的双联 12 cm 高角炮组', 'Twin 12 cm AA gun crew aboard Akagi'),
        'part': 'mount', 'view': 'detail', 'date': '1941-1942',
        'note': '赤城号上操作双联 120 mm 高角炮的炮组。**这是炮在舰上的使用状态，不是炮座特写** —— 12 cm 十年式在 Commons 没有独立分类，只能从赤城舰照中选取。赤城是全程未换装该炮的舰，因此这张对应该型。',
    },
    '127cm-89': {
        'title': ('八九式 12.7 cm 高角炮（驱逐舰梨号所装）', 'Type 89 12.7 cm AA gun from the destroyer Nashi'),
        'part': 'mount', 'view': 'three_quarter', 'date': '1945',
        'note': '原装于驱逐舰梨号（Nashi）的八九式 12.7 cm 高角炮，现地展示状态。',
    },
    '5in38-mk12': {
        'title': ('企业号 5"/38 双联装炮塔对空射击训练', '5"/38 mounts of USS Enterprise during gunnery practice'),
        'part': 'turret', 'view': 'three_quarter', 'date': '1942-03-04',
        'note': '1942 年 3 月 4 日，企业号（CV-6）的 5"/38 双联装炮塔在对模拟鱼雷攻击的靶机射击（NHHC 80-G-16954）。与本项目收录的企业号直接对应。',
    },
    'f4f-wildcat': {
        'title': ('企业号 VF-6 的 F4F-4 起飞', 'F4F-4 of VF-6 taking off from USS Enterprise'),
        'part': 'aircraft', 'view': 'three_quarter', 'date': '1942',
        'note': '1942 年，企业号（CV-6）第 6 战斗机中队（VF-6）的一架 F4F-4 起飞。与本项目收录的企业号直接对应。',
    },
    'sbd-dauntless': {
        'title': ('企业号飞行甲板上为 SBD 挂弹', 'Arming SBDs on the flight deck of USS Enterprise'),
        'part': 'aircraft', 'view': 'detail', 'date': '1942',
        'note': '1942 年初企业号（CV-6）飞行甲板上，弹药吊车正把炸弹送上甲板为 SBD 挂载。',
    },
    'tbd-devastator': {
        'title': ('VT-6 的 TBD-1 编队飞行', 'TBD-1 Devastators of VT-6 in flight'),
        'part': 'aircraft', 'view': 'three_quarter', 'date': '1939',
        'note': '约 1939 年，企业号（CV-6）第 6 鱼雷机中队（VT-6）的 TBD-1 编队飞行（NHHC NH 77104）。',
    },
}

ORDER = ['a6m2', 'd3a1', 'b5n2', '25mm-96', '20cm-3ns', '12cm-10ns',
         '127cm-89', '5in38-mk12', 'f4f-wildcat', 'sbd-dauntless', 'tbd-devastator']

lines = []
for wid in ORDER:
    rec = picked.get(wid)
    if not rec or not rec.get('ok'):
        print(f'跳过 {wid}（无图）')
        continue
    m = META[wid]
    zh, en = m['title']
    lic_raw = rec['license']
    # Commons 的 Artist 字段本身是 HTML 片段，必须剥标签（踩过的坑）
    author = rec.get('author') or 'Unknown author'
    credit = rec.get('credit') or ''

    # YAML 引号处理：标题里可能含空格、逗号、双引号（如 5"/38），
    # 一律用单引号包裹，内部单引号转义成两个。
    def q(s):
        s = str(s or '').replace("'", "''")
        return f"'{s}'"

    en_escaped = q(en)
    author_q = q(author)
    credit_q = q(credit)

    lines.append(f"""  - id: {wid}-primary
    file: {rec['file']}
    subject: weapon:{wid}
    title:
      zh: {zh}
      en: {en_escaped}
    part: {m['part']}
    view: {m['view']}
    date: {m['date']}
    license: {'pd' if rec['tier'] == 'A' else 'cc'}
    license_tier: {rec['tier']}
    license_raw: "{lic_raw}"
    author: {author_q}
    credit: {credit_q}
    source_url: "{rec.get('page') or ''}"
    width: {rec['w']}
    height: {rec['h']}
    primary: true
    note: {m['note']}
""")

out = WORK / 'images_fragment.yaml'
with io.open(out, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print(f'写入 {out}，共 {len(lines)} 条')
