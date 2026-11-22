# 把 last-battle.yaml 里 10 条只有名字的参战舰补上 ship_id，并删掉过时的 note。
#
# 为什么要脚本而不是手改：
#   这 10 条在 belligerents 里是交错分布的，手改容易把 YAML 缩进弄乱；
#   而且改完要能验证「13/13 都有 ship_id」。
#
# 保留什么：
#   - role（角色描述）原样保留 —— 里面的「5-26 已脱离、不在战场」这类
#     限定语是史实更正，不能删。
#   - note 全部删除：它写的是「本站尚未收录该舰单页」，入库后就过时了。
#
# 用法：
#   python work/patch_battle_participants.py --dry-run
#   python work/patch_battle_participants.py
import io
import os
import re
import sys
from datetime import datetime

import yaml

BATTLE = 'data/battles/last-battle.yaml'

# 舰名 → ship id。id 必须与 data/ships/<id>.yaml 一致。
SHIP_ID_BY_NAME = {
    'HMS Norfolk': 'norfolk',
    'HMS Dorsetshire': 'dorsetshire',
    'HMS Sheffield': 'sheffield',
    'HMS Ark Royal': 'ark-royal',
    'HMS Victorious': 'victorious',
    'HMS Cossack': 'cossack',
    'HMS Maori': 'maori',
    'HMS Zulu': 'zulu',
    'HMS Sikh': 'sikh',
    'ORP Piorun': 'piorun',
}


def main():
    dry = '--dry-run' in sys.argv

    with io.open(BATTLE, encoding='utf-8') as f:
        text = f.read()

    d = yaml.safe_load(text)

    # 1. 先在内存里改，确认 13/13 都能对上
    total = 0
    patched = 0
    unresolved = []
    for b in d.get('belligerents') or []:
        for s in b.get('ships') or []:
            total += 1
            name = s.get('name')
            if s.get('ship_id'):
                patched += 1
                continue
            sid = SHIP_ID_BY_NAME.get(name)
            if not sid:
                unresolved.append(name)
                continue
            if not os.path.exists(f'data/ships/{sid}.yaml') and \
               not os.path.exists(f'work/staging/g1-victorious/ships/{sid}.yaml') and \
               not any(os.path.exists(f'work/staging/{g}/ships/{sid}.yaml')
                       for g in os.listdir('work/staging')
                       if os.path.isdir(f'work/staging/{g}') and g != 'SCHEMA.md'):
                unresolved.append(f'{name} (id={sid} 但缺 ships/{sid}.yaml)')
                continue
            patched += 1

    print(f'参战条目 {total} 条，能解析到 ship_id 的 {patched} 条')
    if unresolved:
        print('未解析：')
        for u in unresolved:
            print(f'  - {u}')
        print('\n先把缺的单舰文件补上，再跑本脚本。')
        return 1

    if dry:
        print('=== dry-run：13/13 全部可解析，可以真改 ===')
        return 0

    # 2. 文本层面逐条改：给每个缺 ship_id 的块插入 ship_id、删掉 note 行。
    #    不用 yaml.safe_dump 重写整份文件 —— 那会把 923 行的注释和排版全部冲掉。
    lines = text.splitlines(keepends=True)
    out = []
    i = 0
    changed_names = []
    while i < len(lines):
        line = lines[i]
        m = re.match(r'^(\s*)- name: (.+?)\s*$', line)
        if not m:
            out.append(line)
            i += 1
            continue

        indent, name = m.group(1), m.group(2).strip()
        out.append(line)
        i += 1

        # 收集这个条目的后续行（缩进比 name 深，或同一缩进的键）
        block = []
        while i < len(lines):
            nxt = lines[i]
            if re.match(r'^\s*- name: ', nxt):
                break
            if nxt.strip() and not nxt.startswith(indent + '  ') and not nxt.startswith(indent + '-'):
                # 退回到 belligerents 这一层了
                break
            block.append(nxt)
            i += 1

        has_ship_id = any(re.match(r'^\s*ship_id:', b) for b in block)
        if has_ship_id:
            out.extend(block)
            continue

        sid = SHIP_ID_BY_NAME.get(name)
        if not sid:
            out.extend(block)
            continue

        # 删掉 note 行（可能跨多行）
        new_block = []
        skipping_note = False
        for b in block:
            if re.match(r'^\s*note:', b):
                skipping_note = True
                continue
            if skipping_note:
                # note 的续行：缩进更深、且不是新的 key
                if re.match(r'^\s+[^\s].*$', b) and not re.match(r'^\s*(ship_id|role|name):', b):
                    # 判断是否仍是 note 的续行：note: 后的行如果缩进比 note 深
                    if len(b) - len(b.lstrip()) > len(indent) + 4:
                        continue
                skipping_note = False
            new_block.append(b)

        # 在 name 之后插 ship_id
        out.append(f'{indent}  ship_id: {sid}\n')
        out.extend(new_block)
        changed_names.append(name)

    if not changed_names:
        print('没有需要改的条目（可能已经跑过了）')
        return 0

    bak = f'{BATTLE}.bak-{datetime.now().strftime("%Y-%m-%d")}'
    if not os.path.exists(bak):
        with io.open(bak, 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)

    with io.open(BATTLE, 'w', encoding='utf-8', newline='\n') as f:
        f.write(''.join(out))

    print(f'已补 ship_id 的舰：{len(changed_names)} 条')
    for n in changed_names:
        print(f'  + {n}')

    # 3. 复验
    with io.open(BATTLE, encoding='utf-8') as f:
        d2 = yaml.safe_load(f)
    tot = 0
    ok = 0
    for b in d2.get('belligerents') or []:
        for s in b.get('ships') or []:
            tot += 1
            if s.get('ship_id'):
                ok += 1
    print(f'\n复验：参战 {tot} 条，带 ship_id {ok} 条')
    return 0 if ok == tot else 1


if __name__ == '__main__':
    sys.exit(main())
