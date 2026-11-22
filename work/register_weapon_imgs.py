# 登记武器图到 data/images.yaml。
import io
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / 'data' / 'images.yaml'
PICKS = ROOT / 'work' / 'weapimg' / 'weapon_picks.json'

DRY = '--dry-run' in sys.argv


def q(s):
    s = str(s or '').replace('\n', ' ').strip()
    return "'" + s.replace("'", "''") + "'"


def clean_artist(s):
    s = re.sub(r'<[^>]+>', '', str(s or ''))
    return re.sub(r'\s+', ' ', s).strip() or 'Unknown author'


picks = json.load(io.open(PICKS, encoding='utf-8'))

blocks = []
for wid, rows in picks.items():
    for n, r in enumerate(rows, 1):
        fname = r['file'].rsplit('/', 1)[-1]
        iid = f"wpn-{wid}-{n:02d}"[:60]
        zh = r['note']
        if len(zh) > 95:
            zh = zh[:93] + '…'
        parts = [
            f'  - id: {q(iid)}',
            f'    file: {q(r["file"])}',
            f'    subject: weapon:{wid}',
            '    title:',
            f'      zh: {q(zh)}',
            f'      en: {q(r["title"])}',
            f'    part: {r["part"]}',
            f'    view: {r["view"]}',
            f'    license: {r["license"]}',
            f'    license_tier: {r["tier"]}',
            f'    license_raw: {q(r.get("license_raw"))}',
            f'    author: {q(clean_artist(r.get("artist")))}',
            f'    source_url: {q(r.get("page"))}',
            f'    width: {r.get("w") or 0}',
            f'    height: {r.get("h") or 0}',
            '    note: ' + q(r['note']),
        ]
        if n == 1:
            parts.append('    primary: true')
        blocks.append('\n'.join(parts) + '\n')

print(f'准备插入 {len(blocks)} 条武器图')

if DRY:
    for b in blocks[:2]:
        print(b)
    sys.exit(0)

text = io.open(IMG, encoding='utf-8').read()
added = skipped = 0
for b in blocks:
    iid = re.search(r"^  - id: '([^']+)'$", b, re.M).group(1)
    if f"id: '{iid}'" in text:
        skipped += 1
        continue
    m = re.search(r'^images:\n', text, re.M)
    text = text[:m.end()] + b + text[m.end():]
    added += 1

io.open(IMG, 'w', encoding='utf-8', newline='\n').write(text)
print(f'插入 {added} 条，跳过 {skipped} 条')

d = yaml.safe_load(io.open(IMG, encoding='utf-8'))
print(f'images.yaml 共 {len(d["images"])} 条')

wc = {}
for im in d['images']:
    s = str(im.get('subject') or '')
    if s.startswith('weapon:'):
        wc[s[7:]] = wc.get(s[7:], 0) + 1
print('\n新武器图覆盖：')
for wid in picks:
    print(f'  {wid:<16} {wc.get(wid, 0)}')
noimg = [w for w in wc if wc[w] == 0]
print(f'\n全站有图的武器：{len(wc)} 型')
