# 把 work/staging/ 下的分片合并进 data/
#
# 设计要点：
#   - 只碰 staging 里真实存在的文件，缺了不算错（各组产出不等）
#   - sources 分片是「追加」：先查 data/sources.yaml 里有没有同 id，有就跳过
#   - 写入前一律留 .bak（用户规矩：覆盖已有文件前留 .bak）
#   - 幂等：同一条命令跑两次结果一样
#
# 用法：
#   python work/merge_staging.py --dry-run      # 只看会写什么
#   python work/merge_staging.py               # 真写
import glob
import io
import os
import shutil
import sys
from datetime import datetime

import yaml

STAGING = 'work/staging'
DATA = 'data'
STAMP = datetime.now().strftime('%Y-%m-%d')


def load(p):
    with io.open(p, encoding='utf-8') as f:
        return yaml.safe_load(f)


def dump(p, obj):
    """按项目的 YAML 风格写：中文不转义、保持 key 顺序、缩进 2。"""
    with io.open(p, 'w', encoding='utf-8', newline='\n') as f:
        yaml.safe_dump(
            obj, f,
            allow_unicode=True,
            sort_keys=False,
            default_flow_style=False,
            indent=2,
            width=200,
        )


def bak(path):
    if os.path.exists(path):
        target = f'{path}.bak-{STAMP}'
        if not os.path.exists(target):
            shutil.copy2(path, target)


def main():
    dry = '--dry-run' in sys.argv
    groups = sorted(d for d in glob.glob(os.path.join(STAGING, '*')) if os.path.isdir(d))

    plan = []   # (kind, src, dst)

    for g in groups:
        for sub in ('classes', 'ships', 'slices', 'articles', 'weapon-articles'):
            for p in sorted(glob.glob(os.path.join(g, sub, '*.yaml'))):
                if '.bak' in p:
                    continue
                plan.append((sub, p, os.path.join(DATA, sub, os.path.basename(p))))

    # ---- 来源分片：合并成一个追加操作
    src_fragments = []
    for g in groups:
        p = os.path.join(g, 'sources-fragment.yaml')
        if os.path.exists(p):
            src_fragments.append(p)

    print(f'分组 {len(groups)} 个，待合并数据文件 {len(plan)} 个，来源分片 {len(src_fragments)} 个')
    print()

    # 2026-11-22 修：默认**跳过已存在的目标文件**，不再无条件覆盖。
    #
    # 为什么（踩过）：第一次合并（7 组）之后，主会话在 data/ 上手工修了
    # 三处切片（ark-royal 加 P7、dorsetshire 加 P0、victorious 加 V0），
    # 然后为了合并第 8 组（g8）又跑了一次本脚本 —— 它把 g1/g3/g5 的原始
    # 分片原样又拷了一遍，三处修复当场被冲掉，audit_data 重新报出三条
    # 同样的切片问题。staging 分片是「初稿」，data/ 才是「已审定的稿」，
    # 后者不该被前者覆盖。
    #
    # 要强制重写某个文件，加 --force。
    force = '--force' in sys.argv

    skipped = []
    filtered = []
    for sub, src, dst in plan:
        if os.path.exists(dst) and not force:
            skipped.append(dst)
            continue
        filtered.append((sub, src, dst))
    plan = filtered

    for sub, src, dst in plan:
        mark = '覆盖' if os.path.exists(dst) else '新建'
        print(f'  [{mark}] {dst}')
    if skipped:
        print(f'\n  跳过已存在的目标 {len(skipped)} 个（data/ 已有审定版本；要重写加 --force）：')
        for s in skipped:
            print(f'       = {s}')
    print()

    # ---- 来源
    src_reg_path = os.path.join(DATA, 'sources.yaml')
    src_reg = load(src_reg_path)
    existing = {s.get('id') for s in (src_reg.get('sources') or [])}
    new_sources = []
    dup_sources = []
    for p in src_fragments:
        frag = load(p) or {}
        for s in (frag.get('sources') or []):
            sid = s.get('id')
            if not sid:
                print(f'  ! {p} 里有来源缺 id，跳过：{str(s)[:80]}')
                continue
            if sid in existing:
                dup_sources.append(sid)
                continue
            existing.add(sid)
            new_sources.append(s)

    print(f'新登记来源 {len(new_sources)} 条；已存在而跳过 {len(dup_sources)} 条')
    if dup_sources:
        print(f'  跳过：{", ".join(sorted(set(dup_sources)))}')
    print()

    if dry:
        print('=== dry-run，没有写任何文件 ===')
        if new_sources:
            print('将要追加的来源：')
            for s in new_sources:
                print(f'  + {s["id"]}  [{s.get("tier")}]  {str(s.get("title"))[:60]}')
        return

    # ---- 真写
    if new_sources:
        bak(src_reg_path)
        src_reg.setdefault('sources', []).extend(new_sources)
        src_reg['updated'] = STAMP
        dump(src_reg_path, src_reg)
        print(f'已把 {len(new_sources)} 条来源追加进 {src_reg_path}')

    for sub, src, dst in plan:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        bak(dst)
        shutil.copy2(src, dst)
    print(f'已合并 {len(plan)} 个数据文件')

    print()
    print('下一步：')
    print('  python scripts/validate.py')
    print('  python scripts/selftest.py')
    print('  python work/audit_data.py')


if __name__ == '__main__':
    main()
