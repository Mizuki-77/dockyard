# 打印候选清单供人工挑选。
#
# 为什么要人工看：Commons 分类里混着大量不相关的图 —— 上一轮关键词搜索
# 抓到过图书馆封面、1904 年报纸、现代空军合影。即使按分类浏览，
# 分类里也可能有「同厂其他型号」「仪式照片」「残骸」。
# 选图这一步必须看标题和描述，不能只看尺寸。

import io
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
P = ROOT / 'work' / 'weaponimg' / 'candidates.json'


def clean(html):
    import re
    s = re.sub(r'<[^>]+>', '', str(html or ''))
    s = s.replace('&amp;', '&').replace('&quot;', '"').replace('&#039;', "'")
    return ' '.join(s.split())


def main():
    d = json.load(io.open(P, encoding='utf-8'))
    only = sys.argv[1] if len(sys.argv) > 1 else None
    for wid, rec in d.items():
        if only and wid != only:
            continue
        if not rec.get('ok'):
            print(f'\n########## {wid}: 无候选 ##########')
            continue
        print(f'\n{"#" * 70}')
        print(f'# {wid}  （{len(rec["entries"])} 个候选）')
        print(f'{"#" * 70}')
        for i, e in enumerate(rec['entries']):
            lic = clean(e.get('license'))
            tier = 'A' if ('Public domain' in lic or 'CC0' in lic) else ('B' if lic.startswith('CC') else '?')
            t = clean(e.get('title')).replace('File:', '')
            print(f"\n[{i:>2}] tier={tier}  {e.get('w')}x{e.get('h')}  {lic}")
            print(f"     {t[:100]}")
            desc = clean(e.get('desc'))
            if desc:
                print(f"     desc: {desc[:110]}")


if __name__ == '__main__':
    main()
