# 把下载好的图登记进 data/images.yaml。
#
# 关键规矩（都是踩过的）：
#   ① YAML 里中文标题含冒号必须加引号 —— 统一用单引号，内部引号翻倍；
#   ② license 只能用现成词表：pd / cc0 / cc_by / cc_by_sa；
#      license_tier 只有 A / B / C；
#   ③ 每条必须有 source_url（Commons 文件页）与 author；
#   ④ 图片记录的 subject 写 ship:<id>，file 写 /img/ships/<文件名>；
#   ⑤ 插在 images 段里，不要重排整个文件（保住既有 451 条）。
#
# 同时写一个校验：插入后重新解析 YAML，确认条数与新增数对得上。
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / 'data' / 'images.yaml'
REPORT = ROOT / 'work' / 'shipimg' / 'download_report.json'

DRY = '--dry-run' in sys.argv

report = json.load(io.open(REPORT, encoding='utf-8'))


def q(s):
    """YAML 单引号字符串。"""
    s = str(s or '').replace('\n', ' ').strip()
    return "'" + s.replace("'", "''") + "'"


def clean_artist(s):
    """Commons 的 Artist 字段本身是 HTML 片段，必须剥标签。"""
    s = str(s or '')
    s = re.sub(r'<[^>]+>', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s or 'Unknown author'


def iid_for(sid, r, n):
    base = re.sub(r'[^a-zA-Z0-9-]+', '-', r['title'].rsplit('.', 1)[0]).strip('-').lower()
    if len(base) > 44:
        base = base[:44].rstrip('-')
    return f'{sid}-{n:02d}-{base}'[:62]


blocks = []
for sid, rows in report.items():
    for i, r in enumerate(rows, 1):
        fname = r['file'].rsplit('/', 1)[-1]
        ext = fname.rsplit('.', 1)[-1].lower()
        iid = iid_for(sid, r, i)
        # zh 标题：用 note 里的事实描述太长了，取标题翻译不了的，直接用文件名基
        # 这里用「舰名 + 日期」的简洁形式，细节放进 note
        zh = r['note']
        if len(zh) > 90:
            zh = zh[:88] + '…'

        parts = [
            f'  - id: {q(iid)}',
            f'    file: {q(r["file"])}',
            f'    subject: ship:{sid}',
            '    title:',
            f'      zh: {q(zh)}',
            f'      en: {q(r["title"])}',
            f'    part: {r["part"]}',
            f'    view: {r["view"]}',
        ]
        if r.get('date'):
            d = str(r['date'])
            # date 字段收 YYYY / YYYY-MM / YYYY-MM-DD
            m = re.match(r'^(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?', d)
            if m:
                parts.append(f'    date: {m.group(0)}')
        parts += [
            f'    license: {r["license"]}',
            f'    license_tier: {r["tier"]}',
            f'    license_raw: {q(r.get("license_raw"))}',
            f'    author: {q(clean_artist(r.get("artist")))}',
            f'    source_url: {q(r.get("page"))}',
            f'    width: {r.get("w") or 0}',
            f'    height: {r.get("h") or 0}',
            '    note: ' + q(r['note']),
        ]
        if i == 1:
            parts.append('    primary: true')
        blocks.append('\n'.join(parts) + '\n')

print(f'准备插入 {len(blocks)} 条')

if DRY:
    print('\n=== dry-run，前 2 条预览 ===')
    for b in blocks[:2]:
        print(b)
    sys.exit(0)

text = io.open(IMG, encoding='utf-8').read()

# 去重：id 已存在就跳过
added, skipped = 0, 0
for b in blocks:
    iid = re.search(r"^  - id: '([^']+)'$", b, re.M).group(1)
    if f"id: '{iid}'" in text:
        skipped += 1
        continue
    # 插到 images: 段之后的第一条之前
    m = re.search(r'^images:\n', text, re.M)
    if not m:
        print('! 找不到 images: 段')
        break
    text = text[:m.end()] + b + text[m.end():]
    added += 1

io.open(IMG, 'w', encoding='utf-8', newline='\n').write(text)
print(f'插入 {added} 条，跳过重复 {skipped} 条')

import yaml  # noqa: E402
d = yaml.safe_load(io.open(IMG, encoding='utf-8'))
print(f'images.yaml 现在共 {len(d["images"])} 条')

counts = {}
for im in d['images']:
    s = str(im.get('subject') or '')
    if s.startswith('ship:'):
        counts[s[5:]] = counts.get(s[5:], 0) + 1
print('\n各舰图片数（新 10 艘）：')
for sid in report:
    print(f'  {sid:<14} {counts.get(sid, 0)}')
