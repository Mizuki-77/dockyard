# 正确追加图片条目：每条用 yaml.safe_dump 单独生成，再拼接
#
# 教训：手写 YAML 文本拼接极易出错（引号未配对、换行破坏结构），
# 上一版把 author 里带换行的字段写坏了，还连带破坏了后续条目。
# 正确做法：每条 dict 用 safe_dump 生成干净片段，缩进后再插入。
import io
import shutil
from datetime import datetime

import yaml

STAMP = datetime.now().strftime('%Y-%m-%d')
IMGS = 'data/images.yaml'
CLEAN = 'data/images.yaml.bak-2026-11-25'   # 534 条、未污染

base_text = io.open(CLEAN, encoding='utf-8').read()
base = yaml.safe_load(base_text)
assert len(base['images']) == 534, f'备份条目数异常: {len(base["images"])}'
assert 'PRELOAD' in base_text, '备份缺 PRELOAD 标记'
print(f'从 {CLEAN} 恢复：{len(base["images"])} 条')

apply = yaml.safe_load(io.open('work/_ship_images_apply.yaml', encoding='utf-8'))['ships']

SHIP_ZH = {
    'tone': '利根号', 'chikuma': '筑摩号', 'haruna': '榛名号', 'kirishima': '雾岛号',
    'hosho': '凤翔号', 'nagara': '长良号', 'sendai': '川内号', 'astoria': '阿斯托里亚号',
    'portland': '波特兰号', 'minneapolis': '明尼阿波利斯号', 'new-orleans': '新奥尔良号',
    'vincennes': '文森斯号', 'northampton': '北安普敦号', 'pensacola': '彭萨科拉号',
    'atlanta': '亚特兰大号', 'hammann': '哈曼号', 'monaghan': '莫纳汉号',
    'benham': '本汉号',
}


def clean_str(s, limit=300):
    """压成单行纯文本，去掉会破坏 YAML 的字符"""
    if not s:
        return ''
    s = str(s).replace('\r', ' ').replace('\n', ' ').replace('\t', ' ')
    s = ' '.join(s.split())
    return s[:limit]


blocks = []
count = 0
for sid, items in apply.items():
    zh = SHIP_ZH.get(sid, sid)
    for i, it in enumerate(items, 1):
        entry = {
            'id': f'{sid}-{i:02d}',
            'file': it['file'],
            'subject': f'ship:{sid}',
            'title': {'zh': f'{zh}（第 {i} 张）',
                      'en': clean_str(str(it.get('commons_title', '')).replace('File:', ''), 90)},
            'license': 'pd',
            'license_tier': 'A',
            'license_raw': clean_str(it.get('license_raw') or 'Public domain', 80),
            'author': clean_str(it.get('author'), 100),
            'source_url': it.get('source_url') or '',
            'width': it.get('width'),
            'height': it.get('height'),
        }
        if i == 1:
            entry['primary'] = True
        desc = clean_str(it.get('descr'), 300)
        if desc:
            entry['note'] = desc
        # 单条 dump，indent 让后续手工加两格缩进
        frag = yaml.safe_dump([entry], allow_unicode=True, sort_keys=False,
                              default_flow_style=False, indent=2, width=200)
        frag_lines = ['  ' + ln if ln.strip() else ln for ln in frag.rstrip('\n').split('\n')]
        blocks.append('\n'.join(frag_lines))
        count += 1

header = ('\n  # ===== 2026-11-25 新增：中途岛扩编 18 艘舰的配图 =====\n'
          '  # 全部 A 档（PD/CC0）。按 Commons Category 浏览抓取。\n'
          '  # 每舰第一张 primary。已剔除舰队合影、友舰视角、同级的其他舰。\n')

new_text = base_text.rstrip('\n') + '\n' + header + '\n' + '\n\n'.join(blocks) + '\n'

# 严格校验
d = yaml.safe_load(new_text)
assert len(d['images']) == 534 + count, f'条目数不符: {len(d["images"])}'
# 每条都必须能取到关键字段
for im in d['images'][-count:]:
    assert im.get('file') and im.get('subject'), f'条目不完整: {im}'
print(f'校验通过：追加 {count} 条，总数 {len(d["images"])}')

shutil.copy2(IMGS, f'{IMGS}.bak2-{STAMP}')
with io.open(IMGS, 'w', encoding='utf-8', newline='\n') as f:
    f.write(new_text)
print(f'已写入 {IMGS}；PRELOAD 保留: {"PRELOAD" in new_text}')
