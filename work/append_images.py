# 把新图追加进 data/images.yaml。
#
# 不用文本拼接：images.yaml 有 5000+ 行，手工编辑容易破坏缩进。
# 这里用 PyYAML 读 → 追加 → 用同样的风格写回。
# 但 PyYAML 的 dump 会重排整个文件（注释全丢、行宽变化），
# 对这个项目是灾难 —— 所以改成「只动文件尾部」：
# 找到 images: 最后一个条目结束的位置，直接在后面插入新条目文本。

import io
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / 'data' / 'images.yaml'
FRAG = ROOT / 'work' / 'weaponimg' / 'images_fragment.yaml'


def main():
    text = io.open(IMG, encoding='utf-8').read()
    frag = io.open(FRAG, encoding='utf-8').read()

    lines = text.split('\n')

    # 找到 images: 这一行，以及它后面最后一个非空、且缩进 >= 4 的行（即最后一条的结尾）
    start = None
    for i, ln in enumerate(lines):
        if ln.strip() == 'images:':
            start = i
            break
    if start is None:
        print('找不到 images: 行')
        return 1

    # 从 start 往下，找到第一个顶层键（非空且不以空格开头）
    end = None
    for i in range(start + 1, len(lines)):
        ln = lines[i]
        if ln and not ln.startswith(' '):
            end = i
            break
    if end is None:
        end = len(lines)

    # 回退到最后一个非空行之后
    insert_at = end
    while insert_at > start + 1 and not lines[insert_at - 1].strip():
        insert_at -= 1

    print(f'images: 在第 {start+1} 行，区间结束于第 {insert_at} 行')

    before = lines[:insert_at]
    after = lines[insert_at:]

    new_lines = before + [''] + frag.rstrip('\n').split('\n') + after
    out = '\n'.join(new_lines)

    io.open(IMG, 'w', encoding='utf-8', newline='\n').write(out)
    print(f'原 {len(lines)} 行 → 现 {len(new_lines)} 行')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
