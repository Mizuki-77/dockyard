# 分片预检：在把 work/staging/ 合并进 data/ 之前，先把能查的都查一遍。
#
# 为什么要单独写一个而不直接用 scripts/validate.py：
#   validate.py 只认 data/ 目录。分片还在 staging 里时跑不了它。
#   等合并完再发现问题，就得回滚 + 重来。
#
# 查什么（都是 validate.py 会拦的，这里提前拦）：
#   1. YAML 能否解析
#   2. fact 的 field 是否注册、unit 是否一致、type 是否对
#   3. enum 取值是否合法
#   4. src 是否已登记（data/sources.yaml + 各组 sources-fragment.yaml）
#   5. confidence 是否非法（D 是常见错）
#   6. 带 qual_keys 的字段是否给齐 qual
#   7. article 的顶层键 / 正文模糊词
#   8. 切片日期格式
#
# 用法：python work/precheck_staging.py [组名...]
import glob
import io
import os
import re
import sys

import yaml

DATA = 'data'
STAGING = 'work/staging'

DATE_RE = re.compile(r'^\d{4}(-\d{2}(-\d{2})?)?$')
VAGUE_RE = re.compile(r'据说|有人认为|有人称|据信|或许|大概|应该是')


def load(p):
    with io.open(p, encoding='utf-8') as f:
        return yaml.safe_load(f)


class Rep:
    def __init__(self):
        self.errors = []
        self.warns = []

    def err(self, where, msg):
        self.errors.append((where, msg))

    def warn(self, where, msg):
        self.warns.append((where, msg))


def main():
    # 参数默认代表「要重点检查哪些组」，但**来源与舰级登记永远全量加载**。
    # 为什么（2026-11-22 踩到）：各组之间会互相引用 —— g4 的部族级 40 多处
    # 引用 g7 登记的 navweaps-4-7in-45-mk12。只查 g4 时会报 38 条「来源未登记」，
    # 全是误报。同理，g3 建的 county 舰级会被 g3 自己的舰引用。
    only = [a for a in sys.argv[1:] if not a.startswith('-')]
    all_groups = sorted(d for d in glob.glob(os.path.join(STAGING, '*')) if os.path.isdir(d))
    groups = [g for g in all_groups if os.path.basename(g) in only] if only else all_groups

    reg = load(os.path.join(DATA, 'fields.yaml'))
    fields = {f['id']: f for f in reg['fields']}
    rejected_units = set((reg.get('rejected_units') or {}).keys())

    srcs_reg = load(os.path.join(DATA, 'sources.yaml'))
    known_sources = {s.get('id') for s in (srcs_reg.get('sources') or [])}
    tiers = {s.get('id'): s.get('tier') for s in (srcs_reg.get('sources') or [])}

    # staging 里新登记的来源也算「已知」，但记一下哪些是新的
    # —— 扫描范围是**所有组**，不是 only 指定那几个，理由见 main() 开头。
    frag_sources = {}
    for g in all_groups:
        p = os.path.join(g, 'sources-fragment.yaml')
        if not os.path.exists(p):
            continue
        frag = load(p) or {}
        for s in (frag.get('sources') or []):
            sid = s.get('id')
            if not sid:
                continue
            frag_sources[sid] = s
            if sid not in known_sources:
                known_sources.add(sid)
                tiers[sid] = s.get('tier')

    # 已存在的舰 / 级 id，用于检查 class 引用
    ship_ids = {os.path.basename(p)[:-5] for p in glob.glob(os.path.join(DATA, 'ships', '*.yaml'))
                if '.bak' not in p}
    staging_ship_ids = set()
    for g in all_groups:
        for p in glob.glob(os.path.join(g, 'ships', '*.yaml')):
            staging_ship_ids.add(os.path.basename(p)[:-5])
    all_ship_ids = ship_ids | staging_ship_ids

    rep = Rep()
    n_files = 0
    n_facts = 0

    for g in groups:
        gname = os.path.basename(g)

        # ---------- sources-fragment 自身
        sp = os.path.join(g, 'sources-fragment.yaml')
        if os.path.exists(sp):
            frag = load(sp) or {}
            for i, s in enumerate(frag.get('sources') or []):
                w = f'{gname}/sources-fragment[{i}]'
                sid = s.get('id')
                if not sid:
                    rep.err(w, '缺 id')
                    continue
                w = f'{gname}/sources:{sid}'
                for k in ('title', 'url', 'type', 'tier', 'role'):
                    if k not in s:
                        rep.err(w, f'缺 {k}')
                if s.get('tier') not in {'A', 'B', 'C', 'D', 'E'}:
                    rep.err(w, f'tier {s.get("tier")!r} 不合法')
                bad_roles = [r for r in (s.get('role') or [])
                             if r not in {'data', 'narrative', 'rights', 'lead', 'image'}]
                if bad_roles:
                    rep.err(w, f'role {bad_roles} 不合法')
                if s.get('access') not in {'direct', 'proxy', None}:
                    rep.err(w, f'access {s.get("access")!r} 不合法')
        else:
            rep.warn(gname, '没有 sources-fragment.yaml')

        # ---------- 舰 / 舰级数据
        for sub in ('classes', 'ships'):
            for p in sorted(glob.glob(os.path.join(g, sub, '*.yaml'))):
                if '.bak' in p:
                    continue
                n_files += 1
                rel = f'{gname}/{sub}/{os.path.basename(p)}'
                try:
                    d = load(p)
                except Exception as e:
                    rep.err(rel, f'YAML 解析失败：{e}')
                    continue
                if not isinstance(d, dict):
                    rep.err(rel, '顶层不是映射')
                    continue

                for k in ('id', 'name', 'facts'):
                    if k not in d:
                        rep.err(rel, f'缺顶层键 {k}')

                if sub == 'ships':
                    cid = d.get('class')
                    if not cid:
                        rep.err(rel, '单舰缺 class')
                    elif not os.path.exists(os.path.join(DATA, 'classes', f'{cid}.yaml')) \
                            and not glob.glob(os.path.join(STAGING, '*', 'classes', f'{cid}.yaml')):
                        rep.err(rel, f'class {cid!r} 没有对应的 classes/{cid}.yaml')

                if d.get('id') and p.endswith(f'{d["id"]}.yaml') is False:
                    rep.warn(rel, f'id {d["id"]!r} 与文件名不一致')

                if not (d.get('facts') or []):
                    rep.warn(rel, '没有任何 fact')

                n_facts += len(d.get('facts') or [])
                check_facts(d.get('facts') or [], f'{rel}', fields, known_sources,
                            tiers, rejected_units, rep,
                            open_ended=bool(d.get('open_ended_note')))

        # ---------- 切片
        for p in sorted(glob.glob(os.path.join(g, 'slices', '*.yaml'))):
            if '.bak' in p:
                continue
            n_files += 1
            rel = f'{gname}/slices/{os.path.basename(p)}'
            try:
                d = load(p) or {}
            except Exception as e:
                rep.err(rel, f'YAML 解析失败：{e}')
                continue
            sid = d.get('ship')
            if not sid:
                rep.err(rel, '缺 ship')
            elif sid not in all_ship_ids:
                rep.err(rel, f'ship {sid!r} 没有对应的 ships/{sid}.yaml')
            slices = d.get('slices') or []
            if not slices:
                rep.err(rel, 'slices 为空')
            prev_to = None
            for i, s in enumerate(slices):
                w = f'{rel}#{s.get("code") or i}'
                if not s.get('code'):
                    rep.err(w, '缺 code')
                if not s.get('title'):
                    rep.err(w, '缺 title')
                frm, to = s.get('from'), s.get('to')
                if frm is None:
                    rep.err(w, '缺 from')
                elif not DATE_RE.match(str(frm)):
                    rep.err(w, f'from {frm!r} 格式不对')
                if to is not None:
                    if not DATE_RE.match(str(to)):
                        rep.err(w, f'to {to!r} 格式不对')
                    elif frm and str(to) < str(frm):
                        rep.err(w, f'to({to}) 早于 from({frm})')
                if prev_to and frm and str(frm) < str(prev_to):
                    rep.warn(w, f'from({frm}) 早于上一片的 to({prev_to})，切片可能重叠')
                prev_to = to
                if not s.get('note'):
                    rep.warn(w, '缺 note（切片要说明这一片变在哪）')

        # ---------- 正文
        for sub, key in (('articles', 'ship'), ('weapon-articles', 'weapon')):
            for p in sorted(glob.glob(os.path.join(g, sub, '*.yaml'))):
                if '.bak' in p:
                    continue
                n_files += 1
                rel = f'{gname}/{sub}/{os.path.basename(p)}'
                try:
                    d = load(p) or {}
                except Exception as e:
                    rep.err(rel, f'YAML 解析失败：{e}')
                    continue
                for k in (key, 'intro', 'history'):
                    if k not in d:
                        rep.err(rel, f'缺顶层键 {k}')
                eid = d.get(key)
                if eid and key == 'ship' and eid not in all_ship_ids:
                    rep.err(rel, f'{key} {eid!r} 没有对应的 ships/{eid}.yaml')

                intro = d.get('intro') or {}
                if not (intro.get('lead') or {}).get('zh'):
                    rep.err(f'{rel}#intro.lead', '缺 zh')
                paras = intro.get('paragraphs') or []
                if not paras:
                    rep.err(rel, 'intro.paragraphs 为空')
                for i, pa in enumerate(paras):
                    w = f'{rel}#intro.paragraphs[{i}]'
                    if not pa.get('heading'):
                        rep.warn(w, '缺 heading')
                    check_text(w, pa.get('text'), rep)
                    check_srcs(w, pa.get('src'), known_sources, tiers, rep)

                hist = d.get('history') or []
                if not hist:
                    rep.err(rel, 'history 为空')
                seen = set()
                for i, sec in enumerate(hist):
                    w = f'{rel}#history[{i}]'
                    sid = sec.get('id')
                    if not sid:
                        rep.err(w, '缺 id')
                    elif sid in seen:
                        rep.err(w, 'id 重复')
                    else:
                        seen.add(sid)
                    if not (sec.get('title') or {}).get('zh'):
                        rep.err(w, 'title 缺 zh')
                    evs = sec.get('events') or []
                    if not evs:
                        rep.err(w, 'events 为空')
                    for j, ev in enumerate(evs):
                        ew = f'{w}/events[{j}]'
                        dt = ev.get('date')
                        if dt is None:
                            rep.err(ew, '缺 date')
                        elif not DATE_RE.match(str(dt)):
                            rep.err(ew, f'date {dt!r} 格式不对')
                        check_text(ew, ev.get('text'), rep)
                        check_srcs(ew, ev.get('src'), known_sources, tiers, rep)

    # ---------- 输出
    print(f'检查了 {n_files} 个文件 / {n_facts} 条 fact')
    print()
    if rep.warns:
        print(f'警告 {len(rep.warns)} 条：')
        for w, m in rep.warns:
            print(f'  ! {w}: {m}')
        print()
    if rep.errors:
        print(f'错误 {len(rep.errors)} 条：')
        for w, m in rep.errors:
            print(f'  x {w}: {m}')
        print()
    print(f'{"失败" if rep.errors else "通过"}：{len(rep.errors)} 错误 / {len(rep.warns)} 警告')
    return 1 if rep.errors else 0


def check_text(where, txt, rep):
    if not isinstance(txt, dict) or not txt.get('zh'):
        rep.err(where, 'text 缺 zh')
        return
    for lang in ('zh', 'en'):
        body = txt.get(lang)
        if not body:
            continue
        m = VAGUE_RE.search(str(body))
        if m:
            rep.warn(where, f'{lang} 正文出现模糊归属词「{m.group()}」')


def check_srcs(where, refs, known_sources, tiers, rep):
    if not refs:
        rep.err(where, '缺 src')
        return
    if isinstance(refs, str):
        rep.err(where, 'src 必须是列表不是字符串')
        return
    for r in refs:
        if r not in known_sources:
            rep.err(where, f'src {r!r} 未登记')
        elif tiers.get(r) == 'E':
            rep.err(where, f'src {r!r} 是 tier E（百科），不能作依据')


def check_facts(facts, rel, fields, known_sources, tiers, rejected_units, rep,
                open_ended=False):
    for i, f in enumerate(facts):
        if not isinstance(f, dict):
            rep.err(f'{rel}#fact[{i}]', '不是映射')
            continue
        fid = f.get('field')
        w = f'{rel}#{fid or "?"}[{i}]'

        missing = {'field', 'value', 'src', 'valid'} - set(f)
        if missing:
            rep.err(w, f'缺必填键 {sorted(missing)}')
            continue

        if fid not in fields:
            near = [x for x in fields if x.split('.')[0] == str(fid).split('.')[0]][:5]
            rep.err(w, f'字段 {fid!r} 不在注册表里（同族：{near}）')
            continue
        spec = fields[fid]

        srcs = f.get('src')
        if isinstance(srcs, str):
            rep.err(w, 'src 必须是列表')
            srcs = []
        if not srcs:
            rep.err(w, '没有来源')
            continue
        for s in srcs:
            if s not in known_sources:
                rep.err(w, f'来源 {s!r} 未登记')
            elif tiers.get(s) == 'E':
                rep.err(w, f'来源 {s!r} 是 tier E，不能作 fact 来源')

        v = f.get('valid')
        if not isinstance(v, dict):
            rep.err(w, 'valid 必须是映射')
            continue
        if 'from' not in v:
            rep.err(w, 'valid 缺 from')
        for lbl in ('from', 'to'):
            val = v.get(lbl)
            if val is None:
                continue
            if not DATE_RE.match(str(val)):
                rep.err(w, f'valid.{lbl}={val!r} 格式不对')

        # 单位
        u = f.get('unit')
        if u in rejected_units:
            rep.err(w, f'单位 {u!r} 在 rejected_units 里')
        elif spec.get('unit') is not None:
            if u is None:
                rep.err(w, f'字段需要 unit: {spec["unit"]}，没给')
            elif u != spec['unit']:
                rep.err(w, f'unit {u!r} 与注册表 {spec["unit"]!r} 不一致')
        elif u is not None:
            rep.warn(w, f'字段注册为无单位，但写了 unit={u!r}')

        # 类型
        val = f.get('value')
        t = spec.get('type')
        if t in ('number', 'integer'):
            if isinstance(val, bool) or not isinstance(val, (int, float)):
                rep.err(w, f'字段是 {t}，但 value={val!r} 不是数字')
        if t == 'bool' and not isinstance(val, bool):
            rep.err(w, f'字段是 bool，value 必须 true/false')
        if t == 'date' and not DATE_RE.match(str(val)):
            rep.err(w, f'字段是 date，value={val!r} 格式不对')
        if t == 'enum':
            allowed = spec.get('values') or []
            vals = val if isinstance(val, list) else [val]
            for vv in vals:
                if vv not in allowed:
                    rep.err(w, f'{fid} 的值 {vv!r} 不在枚举内')

        # qual
        if 'qual_keys' in spec:
            quals = f.get('qual') or {}
            need = set(spec['qual_keys'])
            have = set(quals)
            if not have:
                rep.err(w, f'需要 qual {spec["qual_keys"]}，没给')
            else:
                miss = need - have
                if miss:
                    rep.err(w, f'缺限定词 {sorted(miss)}')
                allowed_vals = spec.get('qual_values') or {}
                for k, vv in quals.items():
                    if k in allowed_vals and vv not in allowed_vals[k]:
                        rep.err(w, f'限定词 {k}={vv!r} 不在 {allowed_vals[k]} 内')

        # confidence
        conf = f.get('confidence')
        if conf not in {'A', 'B', 'C', None}:
            hint = '（D 是来源层级不是置信度，用 A/B/C）' if conf == 'D' else ''
            rep.err(w, f'confidence {conf!r} 不合法{hint}')
        elif conf is None:
            rep.warn(w, '没写 confidence')

        # valid.to 空要 note —— 但文件顶层写了 open_ended_note 就是合法声明，
        # 与 validate.py 的口径一致（那里也是 `not f.get("note") and not open_note`）。
        if v.get('to') is None and not f.get('note') and not open_ended:
            rep.warn(w, 'valid.to 为空且没 note（文件也没有 open_ended_note）')


if __name__ == '__main__':
    sys.exit(main())
