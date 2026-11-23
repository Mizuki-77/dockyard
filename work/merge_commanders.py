# 合并指挥官分片到 data/commanders/，并做入库前预检。
#
# 预检规则与 scripts/validate.py 的 check_commander 对齐，但提前在
# staging 阶段跑 —— 免得合并完才发现 relations 指向不存在的舰。
import glob
import io
import os
import re
import shutil
import sys

import yaml

STAGING = 'work/staging_cmdr'
DATA = 'data/commanders'

DATE_RE = re.compile(r'^\d{4}(-\d{2}(-\d{2})?)?$')
VAGUE_RE = re.compile(r'据说|有人认为|有人称|据信|或许|大概|应该是')


def load(p):
    return yaml.safe_load(io.open(p, encoding='utf-8') or '')


def main():
    dry = '--dry-run' in sys.argv
    groups = sorted(d for d in glob.glob(os.path.join(STAGING, '*'))
                    if os.path.isdir(d) and not d.endswith('data'))

    ship_ids = {os.path.basename(p)[:-5]
                for p in glob.glob('data/ships/*.yaml') if '.bak' not in p}
    battle_ids = {os.path.basename(p)[:-5]
                  for p in glob.glob('data/battles/*.yaml') if '.bak' not in p}

    reg = yaml.safe_load(io.open('data/sources.yaml', encoding='utf-8'))
    known_src = {s.get('id') for s in reg.get('sources') or []}
    tiers = {s.get('id'): s.get('tier') for s in reg.get('sources') or []}

    # staging 里新登记的来源也算已知
    new_src = []
    for g in groups:
        p = os.path.join(g, 'sources-fragment.yaml')
        if not os.path.exists(p):
            continue
        frag = yaml.safe_load(io.open(p, encoding='utf-8')) or {}
        for s in frag.get('sources') or []:
            sid = s.get('id')
            if sid and sid not in known_src:
                known_src.add(sid)
                tiers[sid] = s.get('tier')
                new_src.append(s)

    errors, warns = [], []
    plan = []

    for g in groups:
        gname = os.path.basename(g)
        for p in sorted(glob.glob(os.path.join(g, 'commanders', '*.yaml'))):
            if '.bak' in p:
                continue
            rel = f'{gname}/{os.path.basename(p)}'
            try:
                d = yaml.safe_load(io.open(p, encoding='utf-8'))
            except Exception as e:
                errors.append(f'{rel}: YAML 解析失败 {e}')
                continue
            if not isinstance(d, dict):
                errors.append(f'{rel}: 顶层不是映射')
                continue

            for k in ('id', 'name'):
                if k not in d:
                    errors.append(f'{rel}: 缺顶层键 {k}')

            cid = d.get('id')
            if cid and os.path.basename(p)[:-5] != cid:
                errors.append(f'{rel}: 文件名与 id={cid} 不一致')

            nm = d.get('name') or {}
            for k in ('zh', 'en'):
                if not nm.get(k):
                    errors.append(f'{rel}: name 缺 {k}')

            life = d.get('life') or {}
            for k in ('born', 'died'):
                v = life.get(k)
                if v and not DATE_RE.match(str(v)):
                    errors.append(f'{rel}: life.{k}={v!r} 格式不对')

            for i, pa in enumerate(d.get('intro') or []):
                w = f'{rel}#intro[{i}]'
                if not pa.get('heading'):
                    warns.append(f'{w}: 缺 heading')
                txt = str(pa.get('text') or '')
                if not txt:
                    errors.append(f'{w}: 缺 text')
                m = VAGUE_RE.search(txt)
                if m:
                    warns.append(f'{w}: 模糊词「{m.group()}」')

            tl = d.get('timeline') or []
            if not tl:
                warns.append(f'{rel}: 没有 timeline（人物页会缺年表）')
            prev = None
            for i, ev in enumerate(tl):
                w = f'{rel}#timeline[{i}]'
                dt = ev.get('date')
                if dt is None:
                    errors.append(f'{w}: 缺 date')
                elif not DATE_RE.match(str(dt)):
                    errors.append(f'{w}: date={dt!r} 格式不对')
                else:
                    if prev and str(dt) < str(prev):
                        warns.append(f'{w}: 日期 {dt} 早于上一条 {prev}')
                    prev = dt
                if not ev.get('text'):
                    errors.append(f'{w}: 缺 text')
                sr = ev.get('src')
                if not sr:
                    errors.append(f'{w}: 缺 src')
                elif isinstance(sr, str):
                    errors.append(f'{w}: src 必须是列表')
                else:
                    for s in sr:
                        if s not in known_src:
                            errors.append(f'{w}: 来源 {s!r} 未登记')
                m = VAGUE_RE.search(str(ev.get('text') or ''))
                if m:
                    warns.append(f'{w}: 模糊词「{m.group()}」')

            rel_ = d.get('relations') or {}
            for i, t in enumerate(rel_.get('ships') or []):
                w = f'{rel}#relations.ships[{i}]'
                sid = t.get('ship')
                if not sid:
                    errors.append(f'{w}: 缺 ship')
                elif sid not in ship_ids:
                    errors.append(f'{w}: ship {sid!r} 不存在于 data/ships/')
                if not t.get('role'):
                    warns.append(f'{w}: 缺 role')
                for k in ('from', 'to'):
                    v = t.get(k)
                    if v and not DATE_RE.match(str(v)):
                        errors.append(f'{w}: {k}={v!r} 格式不对')

            for i, b in enumerate(rel_.get('battles') or []):
                w = f'{rel}#relations.battles[{i}]'
                bid = b.get('battle')
                if not bid:
                    errors.append(f'{w}: 缺 battle')
                elif bid not in battle_ids:
                    errors.append(f'{w}: battle {bid!r} 不存在于 data/battles/')
                if not b.get('role'):
                    warns.append(f'{w}: 缺 role')

            for s in d.get('src') or []:
                if s not in known_src:
                    errors.append(f'{rel}#src: 来源 {s!r} 未登记')

            plan.append((p, os.path.join(DATA, os.path.basename(p))))

    print(f'分组 {len(groups)} 个，指挥官文件 {len(plan)} 个，新来源 {len(new_src)} 条')
    print()
    for src, dst in plan:
        mark = '覆盖' if os.path.exists(dst) else '新建'
        print(f'  [{mark}] {dst}')
    print()

    if warns:
        print(f'警告 {len(warns)} 条：')
        for w in warns:
            print(f'  ! {w}')
        print()
    if errors:
        print(f'错误 {len(errors)} 条：')
        for e in errors:
            print(f'  x {e}')
        print()
    print(f'{"失败" if errors else "通过"}：{len(errors)} 错误 / {len(warns)} 警告')

    if errors or dry:
        return 1 if errors else 0

    # 真合并
    os.makedirs(DATA, exist_ok=True)
    for src, dst in plan:
        if os.path.exists(dst):
            shutil.copy2(dst, dst + '.bak-merge')
        shutil.copy2(src, dst)
    print(f'已写入 {len(plan)} 个指挥官文件')

    if new_src:
        reg['sources'].extend(new_src)
        io.open('data/sources.yaml', 'w', encoding='utf-8', newline='\n').write(
            yaml.safe_dump(reg, allow_unicode=True, sort_keys=False,
                           default_flow_style=False, indent=2, width=200))
        print(f'已追加 {len(new_src)} 条来源')
    return 0


if __name__ == '__main__':
    sys.exit(main())
