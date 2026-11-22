import glob, io, os, sys, re
import yaml

ROOT = r'D:\deepseek harness\website-warships'
STG = os.path.join(ROOT, 'work', 'staging', 'g1-victorious')

fields = {f['id']: f for f in yaml.safe_load(open(os.path.join(ROOT, 'data', 'fields.yaml'), encoding='utf-8'))['fields']}
srcs = {s['id']: s for s in yaml.safe_load(open(os.path.join(ROOT, 'data', 'sources.yaml'), encoding='utf-8'))['sources']}

# 新来源分片
frag = yaml.safe_load(open(os.path.join(STG, 'sources-fragment.yaml'), encoding='utf-8'))
new_srcs = {s['id']: s for s in frag['sources']}
all_srcs = dict(srcs)
all_srcs.update(new_srcs)

DATE_RE = re.compile(r'^\d{4}(-\d{2}(-\d{2})?)?$')
REQUIRED = {'field', 'value', 'src', 'valid'}
errors = []
warns = []


def err(m):
    errors.append(m)


def warn(m):
    warns.append(m)


# ---- sources fragment 自身
for s in frag['sources']:
    for k in ('id', 'title', 'url', 'type', 'tier', 'role'):
        if k not in s:
            err(f'sources#{s.get("id")}: 缺 {k}')
    if s.get('tier') not in {'A', 'B', 'C', 'D', 'E'}:
        err(f'sources:{s["id"]}: tier 非法 {s.get("tier")}')
    for r in (s.get('role') or []):
        if r not in {'data', 'narrative', 'rights', 'lead', 'image'}:
            err(f'sources:{s["id"]}: role 非法 {r}')
    if s['id'] in srcs:
        err(f'sources:{s["id"]}: 已在 data/sources.yaml 登记，重复')

# ---- ships
p = os.path.join(STG, 'ships', 'victorious.yaml')
ship = yaml.safe_load(open(p, encoding='utf-8'))
for k in ('id', 'name', 'class', 'facts'):
    if k not in ship:
        err(f'ships: 缺顶层键 {k}')
facts = ship['facts']
n = 0
for i, f in enumerate(facts):
    where = f"ships#{i}:{f.get('field')}"
    miss = REQUIRED - set(f)
    if miss:
        err(f'{where}: 缺 {sorted(miss)}')
        continue
    fid = f['field']
    if fid not in fields:
        err(f'{where}: 字段未注册')
        continue
    spec = fields[fid]
    s = f['src']
    if isinstance(s, str):
        err(f'{where}: src 是字符串')
        s = []
    if not s:
        err(f'{where}: 无 src')
    for x in s:
        if x not in all_srcs:
            err(f'{where}: 来源 {x} 未登记')
        elif all_srcs[x].get('tier') == 'E':
            err(f'{where}: 来源 {x} 是 tier E')
        elif 'data' not in (all_srcs[x].get('role') or []):
            warn(f'{where}: 来源 {x} role 不含 data')
    v = f['valid']
    if not isinstance(v, dict) or 'from' not in v:
        err(f'{where}: valid 缺 from')
    else:
        for lbl in ('from', 'to'):
            val = v.get(lbl)
            if val is None:
                continue
            if not DATE_RE.match(str(val)):
                err(f'{where}: valid.{lbl}={val!r} 格式错')
        if v.get('to') and str(v['from']) > str(v['to']):
            err(f'{where}: from 晚于 to')
        if v.get('to') is None and not f.get('note') and not ship.get('open_ended_note'):
            warn(f'{where}: to 空且无 note')
    u = f.get('unit')
    if spec['unit'] is not None:
        if u is None:
            err(f'{where}: 缺 unit {spec["unit"]}')
        elif u != spec['unit']:
            err(f'{where}: unit {u} != {spec["unit"]}')
    elif u is not None:
        warn(f'{where}: 无单位字段写了 unit={u}')
    val = f['value']
    t = spec['type']
    if t in ('number', 'integer') and (isinstance(val, bool) or not isinstance(val, (int, float))):
        err(f'{where}: type {t} 但 value={val!r}')
    if t == 'bool' and not isinstance(val, bool):
        err(f'{where}: bool 字段 value 非布尔')
    if t == 'date' and not DATE_RE.match(str(val)):
        err(f'{where}: date 字段 value={val!r} 格式错')
    if t == 'enum':
        for vv in (val if isinstance(val, list) else [val]):
            if vv not in (spec.get('values') or []):
                err(f'{where}: 枚举值 {vv!r} 非法')
    if 'qual_keys' in spec:
        q = f.get('qual') or {}
        miss_q = set(spec['qual_keys']) - set(q)
        if not q:
            err(f'{where}: 缺 qual')
        elif miss_q:
            err(f'{where}: qual 缺 {sorted(miss_q)}')
        else:
            allowed = spec.get('qual_values') or {}
            for k, vv in q.items():
                if k in allowed and vv not in allowed[k]:
                    err(f'{where}: qual {k}={vv!r} 非法')
    elif f.get('qual'):
        err(f'{where}: 非限定字段写了 qual')
    c = f.get('confidence')
    if c not in ('A', 'B', 'C', None):
        err(f'{where}: confidence {c!r} 非法')
    if c is None:
        warn(f'{where}: 无 confidence')
    n += 1

# ---- slices
sl = yaml.safe_load(open(os.path.join(STG, 'slices', 'victorious.yaml'), encoding='utf-8'))
if sl.get('ship') != 'victorious':
    err('slices: ship 不是 victorious')
codes = []
for i, s in enumerate(sl['slices']):
    for k in ('code', 'title', 'from', 'note'):
        if k not in s:
            err(f'slices#{i}: 缺 {k}')
    codes.append(s['code'])
    for lbl in ('from', 'to'):
        v = s.get(lbl)
        if v is not None and not DATE_RE.match(str(v)):
            err(f'slices#{s.get("code")}: {lbl} 格式错 {v!r}')
    if s.get('to') and str(s['from']) > str(s['to']):
        err(f'slices#{s["code"]}: from 晚于 to')
if len(set(codes)) != len(codes):
    err('slices: code 重复')

# ---- article
a = yaml.safe_load(open(os.path.join(STG, 'articles', 'victorious.yaml'), encoding='utf-8'))
for k in ('ship', 'intro', 'history'):
    if k not in a:
        err(f'articles: 缺 {k}')
VAGUE = re.compile(r'据说|有人认为|有人称|据信|或许|大概|应该是')


def s_ok(where, refs):
    if not refs:
        err(f'{where}: 缺 src')
        return
    for r in refs:
        if r not in all_srcs:
            err(f'{where}: src {r} 未登记')
        elif all_srcs[r].get('tier') == 'E':
            err(f'{where}: src {r} 是 tier E')


def t_ok(where, txt):
    if not isinstance(txt, dict) or 'zh' not in txt:
        err(f'{where}: text 缺 zh')
        return
    for lang in ('zh', 'en'):
        b = txt.get(lang)
        if b and VAGUE.search(str(b)):
            warn(f'{where}: {lang} 出现模糊词 {VAGUE.search(str(b)).group()}')


lead = a['intro'].get('lead') or {}
if 'zh' not in lead:
    err('articles: intro.lead 缺 zh')
for i, p in enumerate(a['intro']['paragraphs']):
    w = f'articles#intro[{i}]'
    if not p.get('heading'):
        warn(f'{w}: 缺 heading')
    t_ok(w, p.get('text'))
    s_ok(w, p.get('src'))
nev = 0
for sec in a['history']:
    w = f'articles#hist/{sec.get("id")}'
    if 'zh' not in (sec.get('title') or {}):
        err(f'{w}: title 缺 zh')
    for lbl in ('from', 'to'):
        v = (sec.get('range') or {}).get(lbl)
        if v is not None and not DATE_RE.match(str(v)):
            err(f'{w}: range.{lbl} {v!r} 格式错')
    evs = sec.get('events') or []
    if not evs:
        err(f'{w}: events 空')
    for j, e in enumerate(evs):
        ew = f'{w}/ev[{j}]'
        if not e.get('date') or not DATE_RE.match(str(e['date'])):
            err(f'{ew}: date {e.get("date")!r} 格式错')
        t_ok(ew, e.get('text'))
        s_ok(ew, e.get('src'))
        nev += 1

print('=== 自检结果 ===')
print(f'ships fact 条数: {n}')
print(f'slices 片数: {len(sl["slices"])} -> {", ".join(codes)}')
print(f'article 简介段数: {len(a["intro"]["paragraphs"])}, 历史 {len(a["history"])} 节 {nev} 条事件')
print(f'新登记来源: {len(frag["sources"])}')
print(f'errors: {len(errors)}  warnings: {len(warns)}')
for e in errors:
    print('  E ' + e)
for w in warns:
    print('  W ' + w)
