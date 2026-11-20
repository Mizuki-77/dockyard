# 盘点武器的三个维度：有 fact / 有正文 / 有图
#
# 武器没有独立定义块 —— 它是靠 fact 上的 `about: weapon:<id>` 拼出来的。
# 所以「武器是否存在」= 有没有任何 fact 指向它。

import io
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'data'

WEAPON_RE = re.compile(r'^weapon:(.+)$')


def load(p):
    with io.open(p, encoding='utf-8') as f:
        return yaml.safe_load(f)


def main():
    # 1. 从所有 fact 里收集 weapon id
    weapons = {}
    files = []
    for sub in ('classes', 'ships'):
        files += [p for p in sorted((DATA / sub).glob('*.yaml')) if not p.name.endswith('.bak')]
    for p in files:
        doc = load(p)
        if not doc:
            continue
        for f in doc.get('facts') or []:
            m = WEAPON_RE.match(str(f.get('about') or ''))
            if not m:
                continue
            wid = m.group(1)
            rec = weapons.setdefault(wid, {'facts': 0, 'owners': set(), 'fields': set()})
            rec['facts'] += 1
            rec['owners'].add(p.stem)
            rec['fields'].add(f.get('field'))

    # 2. 正文
    arts = {p.stem for p in (DATA / 'weapon-articles').glob('*.yaml')}

    # 3. 图
    #    注意键名是 subject，不是 about —— 拿 about 去对会全军覆没（踩过）。
    imgs = {}
    ip = DATA / 'images.yaml'
    if ip.exists():
        doc = load(ip) or {}
        for im in doc.get('images') or []:
            subj = str(im.get('subject') or '')
            m = WEAPON_RE.match(subj)
            if m:
                imgs.setdefault(m.group(1), []).append(im.get('id'))

    total = len(weapons)
    has_art = sum(1 for k in weapons if k in arts)
    has_img = sum(1 for k in weapons if k in imgs)

    print(f"武器实体总数：{total}")
    print(f"  有 fact   ：{total}")
    print(f"  有正文    ：{has_art}")
    print(f"  有图      ：{has_img}")
    print()

    def show(title, ids):
        print("=" * 80)
        print(f"{title}（{len(ids)} 型）")
        print("=" * 80)
        if not ids:
            print("  （无）")
        for wid in ids:
            r = weapons[wid]
            print(f"  {wid:<26} fact={r['facts']:<4} 归属={','.join(sorted(r['owners']))[:38]}")
        print()

    no_art = sorted(w for w in weapons if w not in arts)
    no_img = sorted(w for w in weapons if w not in imgs)
    neither = sorted(w for w in weapons if w not in arts and w not in imgs)

    show("【没正文的】", no_art)
    show("【没图的】", no_img)
    show("【既没正文也没图】最该补", neither)

    orphan = sorted(arts - set(weapons))
    if orphan:
        print("=" * 80)
        print(f"【孤儿正文】（{len(orphan)} 型）有 .yaml 但没有任何 fact 指向它")
        print("=" * 80)
        for o in orphan:
            print(f"  {o}")
        print()

    # 顺带：完全没有 weapon.* fact 的正文也可能存在，列出来对照
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
