# 重新应用被 merge 覆盖掉的切片修复。
#
# 背景：merge_staging.py 是「全量覆盖」语义 —— 第二次跑（合并 g8）时，
# 把 g5/g3/g1 的 slices 原始分片又拷了一遍，冲掉了主会话在 data/ 上
# 手工做的三处修复（ark-royal 加 P7、dorsetshire 加 P0、victorious 加 V0）。
# 这是脚本设计缺陷，已记在文件末尾。本脚本把那三处改回来，幂等。
import io
import re
import sys
from datetime import datetime

import yaml

DRY = '--dry-run' in sys.argv


def load(p):
    return yaml.safe_load(io.open(p, encoding='utf-8'))


def dump_text(p, text):
    if not DRY:
        bak = f'{p}.bak-{datetime.now().strftime("%Y-%m-%d")}'
        import os
        if not os.path.exists(bak):
            io.open(bak, 'w', encoding='utf-8', newline='\n').write(
                io.open(p, encoding='utf-8').read())
        io.open(p, 'w', encoding='utf-8', newline='\n').write(text)


# ---------------------------------------------------------------- ark-royal
ARK_P7 = """
  - code: P7
    title: 沉没之后：调查与制度性后果（1942 起）
    from: 1941-11-15
    to: 1942-12-31
    note: >-
      **这一片里已经没有「舰」了，只有它的后果 —— 但必须留着。**

      事后调查认定损管处置与人员训练不足是沉没的重要成因，并据此修改了
      全部新造舰的电力与损管设计。这条调查结论的生效日期是 1942-01，
      比沉没晚两个月；若不设这一片，时间轴会停在 1941-11-14，
      「一艘舰的死改变了整个舰队的设计」这件事就没地方放。

      这是本站切片的一个刻意设定：**切片描述的是这艘舰的状态，但当它的死
      成为后续事件的起点时，那个后果也属于它的历史。** 同类先例见
      data/slices/rodney.yaml 的战后拆解片（note 里写了它对后续设计的影响）。

      本片显示「该时期无影像」是**对的** —— 船已经没了，不该有图。
      这不是配图缺失，不要来补图。
"""


def fix_ark_royal():
    p = 'data/slices/ark-royal.yaml'
    d = load(p)
    if any(s['code'] == 'P7' for s in d['slices']):
        print('ark-royal: P7 已存在，跳过')
        return
    text = io.open(p, encoding='utf-8').read().rstrip('\n') + '\n' + ARK_P7
    dump_text(p, text)
    print('ark-royal: 已补 P7（沉没之后）')


# ------------------------------------------------------------- dorsetshire
DOR_P0 = """  - code: P0
    title: 设计定案与订购（1925-1926）
    from: 1926-12-03
    to: 1927-09-20
    note: >-
      **这一片里还没有「本舰」，只有它的订购文书。**

      1926-12-03 列入建造计划。本舰属郡级 Norfolk 子级，设计基于
      1925 年海军计划下的 Kent 子级改进（提高干舷、加厚弹药库防护）。
      切片起点取这条 fact 的日期，而不是开工日，是照
      data/slices/illustrious.yaml 的 P0 先例办的 —— 否则时间轴最左端
      会有一段拖出去却是空白的区间。

"""


def fix_dorsetshire():
    p = 'data/slices/dorsetshire.yaml'
    d = load(p)
    first = d['slices'][0]
    if first['from'] == '1926-12-03':
        print('dorsetshire: P0 已修好，跳过')
        return
    text = io.open(p, encoding='utf-8').read()
    # 在 "slices:\n" 之后插入新片
    m = re.search(r'^slices:\n', text, re.M)
    text = text[:m.end()] + DOR_P0 + text[m.end():]
    dump_text(p, text)
    print('dorsetshire: 已补 P0（设计定案与订购）')


# -------------------------------------------------------------- victorious
VIC_V0 = """  - code: V0
    title: 设计定案与订购（1936-1937）
    from: 1936-07-08
    to: 1937-01-12
    note: >-
      **这一片里还没有「本舰」，只有它所属这一级的设计定案。**

      1936-07-08 光辉级的参谋要求（Staff Requirements）定稿：标准排水量被
      1936 年伦敦会议限定在 23,000 ts，飞行甲板要求「as large an area as
      possible」，机库侧壁 4.5 in C 装甲，载机 36 架。本舰后来的一切取舍
      都从这份文件出发，所以时间轴必须从这一天开始，而不是从它下单那天。

      这一片的数据来自舰级文件（data/classes/illustrious.yaml）而非本舰文件：
      本级三艘共用同一份参谋要求。切片起点与 fact 时间窗对齐，是照
      data/slices/illustrious.yaml 的 P0 先例办的。

"""


def fix_victorious():
    p = 'data/slices/victorious.yaml'
    d = load(p)
    if d['slices'][0]['from'] == '1936-07-08':
        print('victorious: V0 已修好，跳过')
        return
    text = io.open(p, encoding='utf-8').read()
    m = re.search(r'^slices:\n', text, re.M)
    text = text[:m.end()] + VIC_V0 + text[m.end():]
    dump_text(p, text)
    print('victorious: 已补 V0（设计定案）')


fix_ark_royal()
fix_dorsetshire()
fix_victorious()

# 重编号（用现成的脚本，它自己会留 bak）
print()
print('接下来跑重编号：')
print('  python work/renumber_slices.py data/slices/victorious.yaml')
print('  python work/renumber_slices.py data/slices/dorsetshire.yaml')
