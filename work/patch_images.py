# 修正 images.yaml 里两条记录：25mm-96（换正确的图）与 11in75-mk1（补上原本失败的那张）。
#
# 25mm-96 上一轮自动选中了「加贺着陆作业」——分类污染，那不是 25mm 炮。
# 11in75 上一轮 429 失败，改用 thumb.wikimedia.org 域下载成功。

import io
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / 'data' / 'images.yaml'

NEW = {
    '25mm-96-primary': {
        'width': 1280,
        'height': 907,
        'title_zh': '九六式二十五粍高角机铳（北京军事博物馆藏）',
        'title_en': 'Type 96 25 mm gun at the Beijing Military Museum',
        'part': 'mount',
        'view': 'three_quarter',
        'date': '1940s',
        'author': 'Max Smith',
        'credit': 'Max Smith / Wikimedia Commons',
        'source_url': 'https://commons.wikimedia.org/wiki/File:Type_96_Japanese_25_mm_gun_-_Beijing_Museum.jpg',
        'note': (
            '北京军事博物馆藏九六式二十五粍高角机铳。这一型通常以三连装或单装炮座出现，'
            '本图所见为单装形态。它在二战中被公认是同期最差的舰载高炮之一：'
            '15 发弹匣需频繁更换、射速低、炮口焰大、瞄准具跟不上目标速度，'
            '但日本海军因产能与组织惯性一直未换装。'
        ),
    },
    '11in75-mk1-primary': {
        'width': 500,
        'height': 383,
        'title_zh': '大黄蜂号上的四联 1.1"/75 高炮正在射击',
        'title_en': 'Quad 1.1"/75 mount firing aboard USS Hornet (CV-8)',
        'part': 'mount',
        'view': 'three_quarter',
        'date': '1942-05',
        'author': 'U.S. Navy',
        'credit': 'U.S. Navy / NHHC',
        'source_url': 'https://commons.wikimedia.org/wiki/File:28_mm_Flak_USS_Hornet_(CV-8)_May_1942.jpg',
        'note': (
            '1942 年 5 月，大黄蜂号（CV-8）上的四联 28 mm（1.1"/75）Mk 1 高炮正在射击，'
            '与本项目收录的大黄蜂号直接对应。**这是全站分辨率最低的一张主图（原图仅 795×609）**，'
            '找不到更高分辨率的该型在舰上使用的照片。'
        ),
    },
}


def patch_block(text, img_id, data):
    """在 images.yaml 里定位 id 对应的条目块，替换其中若干字段。"""
    # 条目从 "  - id: <img_id>" 开始，到下一个 "  - id:" 或文件末尾
    pat = re.compile(r'(^  - id: ' + re.escape(img_id) + r'\n)(.*?)(?=^  - id: |\Z)', re.S | re.M)
    m = pat.search(text)
    if not m:
        print(f'  ✗ 找不到 {img_id}')
        return text

    head, body = m.group(1), m.group(2)

    def set_field(body, key, value):
        # 已有该键就替换整行（含可能的多行内容），没有就追加
        kp = re.compile(r'^    ' + re.escape(key) + r':.*?(?=^    \S|\Z)', re.S | re.M)
        line = f'    {key}: {value}\n'
        if kp.search(body):
            return kp.sub(line, body, count=1)
        return body + line

    # title 是两行结构
    title_block = f"    title:\n      zh: {data['title_zh']}\n      en: '{data['title_en']}'\n"
    tp = re.compile(r'^    title:.*?(?=^    \S|\Z)', re.S | re.M)
    if tp.search(body):
        body = tp.sub(title_block, body, count=1)
    else:
        body = title_block + body

    for k in ('part', 'view', 'date', 'author', 'credit', 'source_url', 'width', 'height', 'note'):
        v = data[k]
        if k in ('note',):
            # note 可能很长，用折叠块
            body = set_field(body, k, '>-\n      ' + v)
        elif k in ('source_url',):
            body = set_field(body, k, f'"{v}"')
        elif k in ('author', 'credit'):
            body = set_field(body, k, f"'{v}'")
        else:
            body = set_field(body, k, v)

    print(f'  ✓ {img_id} 已更新')
    return text[:m.start()] + head + body + text[m.end():]


def main():
    text = io.open(IMG, encoding='utf-8').read()
    for img_id, data in NEW.items():
        text = patch_block(text, img_id, data)
    io.open(IMG, 'w', encoding='utf-8', newline='\n').write(text)
    print('写入完成')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
