# -*- coding: utf-8 -*-
"""利根级分片自检（按 SCHEMA §10）。只读 data/，不写。"""
import glob
import io
import os
import re
import sys

import yaml

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = r'D:\deepseek harness\website-warships'
STAGE = os.path.join(ROOT, 'work', 'staging', 'tone')
DATE = re.compile(r'^\d{4}(-\d{2}(-\d{2})?)?$')

reg = yaml.safe_load(io.open(os.path.join(ROOT, 'data', 'fields.yaml'), encoding='utf-8'))
fields = {f['id']: f for f in reg['fields'] if isinstance(f, dict) and 'id' in f}
units = set(reg['units'])
rejected = set(reg['rejected_units'])

# ---- 来源表：data/sources.yaml + 本分片
srcs = {}
for p in [os.path.join(ROOT, 'data', 'sources.yaml'),
          os.path.join(STAGE, 'sources-fragment.yaml')]:
    d = yaml.safe_load(io.open(p, encoding='utf-8'))
    for s in d['sources']:
        if s['id'] in srcs:
            print('!! 来源 id 重复登记:', s['id'])
        srcs[s['id']] = s

errors = []
warns = []
infos = []

# ---- 1. YAML 可解析
files = sorted(glob.glob(os.path.join(STAGE, '**', '*.yaml'), recursive=True))
docs = {}
for p in files:
    try:
        docs[p] = yaml.safe_load(io.open(p, encoding='utf-8'))
    except Exception as e:
        errors.append(('YAML 解析失败', os.path.basename(p), str(e)))
infos.append('YAML 可解析：%d 个文件' % len(docs))

# ---- 2. fact 逐条
used_srcs = set()
total = 0
for p, d in docs.items():
    rel = os.path.basename(p)
    if not d or 'facts' not in d:
        continue
    for i, f in enumerate(d['facts']):
        total += 1
        fid = f.get('field')
        where = '%s#%s[%d]' % (rel, fid or f.get('about'), i)
        if fid not in fields:
            errors.append(('字段未注册', where, str(fid)))
            continue
        spec = fields[fid]

        # src
        ss = f.get('src')
        if not ss:
            errors.append(('无 src', where, ''))
        else:
            for s in ss:
                used_srcs.add(s)
                if s not in srcs:
                    errors.append(('src 未登记', where, s))
                elif srcs[s].get('tier') == 'E':
                    errors.append(('src 是 tier E', where, s))
                elif 'data' not in (srcs[s].get('role') or []):
                    warns.append(('src role 不含 data', where, s))

        # valid
        v = f.get('valid') or {}
        if 'from' not in v:
            errors.append(('valid 缺 from', where, ''))
        for k in ('from', 'to'):
            if v.get(k) is not None and not DATE.match(str(v[k])):
                errors.append(('valid.%s 格式' % k, where, str(v[k])))

        # unit
        u = f.get('unit')
        if u in rejected:
            errors.append(('单位被拒收', where, u))
        elif spec['unit'] is not None:
            if u is None:
                errors.append(('缺 unit', where, '需要 ' + spec['unit']))
            elif u != spec['unit']:
                errors.append(('unit 不一致', where, '%s != %s' % (u, spec['unit'])))
        elif u is not None:
            warns.append(('无单位字段却写了 unit', where, u))

        # 类型
        val = f.get('value')
        t = spec['type']
        if t in ('number', 'integer') and (not isinstance(val, (int, float)) or isinstance(val, bool)):
            errors.append(('类型不是数字', where, repr(val)))
        if t == 'bool' and not isinstance(val, bool):
            errors.append(('类型不是 bool', where, repr(val)))
        if t == 'enum' and val not in (spec.get('values') or []):
            errors.append(('枚举越界', where, repr(val)))
        if t == 'date' and not DATE.match(str(val)):
            errors.append(('date 值格式', where, repr(val)))

        # qual
        if 'qual_keys' in spec:
            q = f.get('qual') or {}
            miss = set(spec['qual_keys']) - set(q)
            if miss:
                errors.append(('缺 qual', where, str(sorted(miss))))
            qv = spec.get('qual_values') or {}
            for k, vv in q.items():
                if k in qv and vv not in qv[k]:
                    errors.append(('qual 取值越界', where, '%s=%s' % (k, vv)))

        # confidence
        c = f.get('confidence')
        if c not in ('A', 'B', 'C', None):
            errors.append(('confidence 非法', where, repr(c)))
        if c is None:
            warns.append(('未写 confidence', where, ''))

# ---- 3. 顶层键
for p, d in docs.items():
    rel = os.path.basename(p)
    if not d:
        continue
    if p.endswith('classes\\tone.yaml') or p.endswith('classes/tone.yaml'):
        for k in ('id', 'name', 'facts'):
            if k not in d:
                errors.append(('舰级缺顶层键', rel, k))
        if 'open_ended_note' not in d:
            warns.append(('舰级缺 open_ended_note', rel, ''))
    if '\\ships\\' in p or '/ships/' in p:
        for k in ('id', 'name', 'class', 'facts'):
            if k not in d:
                errors.append(('单舰缺顶层键', rel, k))
    if 'sources-fragment' in p:
        for s in d.get('sources') or []:
            for k in ('id', 'title', 'url', 'type', 'tier', 'role'):
                if k not in s:
                    errors.append(('来源缺必填键', s.get('id'), k))
            if s.get('tier') not in set((yaml.safe_load(
                    io.open(os.path.join(ROOT, 'data', 'sources.yaml'),
                            encoding='utf-8')).get('tiers') or {}).keys()):
                errors.append(('来源 tier 非法', s.get('id'), s.get('tier')))

# ---- 4. 正文禁区词（本轮无 articles，仍查一遍所有 note/value）
VAGUE = re.compile(r'据说|有人认为|有人称|据信|或许|大概|应该是')
for p, d in docs.items():
    txt = io.open(p, encoding='utf-8').read()
    for m in VAGUE.finditer(txt):
        s = max(0, m.start() - 40)
        warns.append(('禁区词', os.path.basename(p), txt[s:m.end() + 20].replace('\n', ' ')))

# ---- 5. 舰级/单舰一致性
cls = docs.get(os.path.join(STAGE, 'classes', 'tone.yaml'))
for sid in ('tone', 'chikuma'):
    sp = os.path.join(STAGE, 'ships', sid + '.yaml')
    sd = docs.get(sp)
    if sd and sd.get('class') != 'tone':
        errors.append(('class 指向错误', sid, str(sd.get('class'))))

print('=' * 70)
print('fact 总数:', total)
print('引用来源:', len(used_srcs), sorted(used_srcs))
print('登记来源:', len(srcs))
print()
print('--- 错误 %d 条 ---' % len(errors))
for e in errors:
    print('  !!', ' | '.join(str(x) for x in e))
print()
print('--- 警告 %d 条 ---' % len(warns))
for w in warns:
    print('  ??', ' | '.join(str(x) for x in w))
print()
for i in infos:
    print('  ', i)
sys.exit(1 if errors else 0)
