"""Dry-run validator for the g6-piorun staging slice.

Reuses scripts/validate.py's checks by staging the fragment into a temp
copy of data/ — but simpler and safer: we just replicate the field/unit/
type/enum/src/valid checks for the three data files, and the article/
slice checks per SCHEMA.
"""
import sys, re, datetime, glob, os
import yaml

ROOT = os.path.abspath('.')
STG = 'work/staging/g6-piorun'
DATA = 'data'

fields_reg = yaml.safe_load(open(os.path.join(DATA, 'fields.yaml'), encoding='utf-8'))
FIELDS = {f['id']: f for f in fields_reg['fields']}

sources_data = yaml.safe_load(open(os.path.join(DATA, 'sources.yaml'), encoding='utf-8'))
sources = {s['id']: s for s in sources_data['sources']}
frag = yaml.safe_load(open(os.path.join(STG, 'sources-fragment.yaml'), encoding='utf-8'))
for s in frag['sources']:
    if s['id'] in sources:
        print('WARN duplicate source id already in data/sources.yaml:', s['id'])
    sources[s['id']] = s
print('sources loaded: data=%d frag=%d total=%d' % (len(sources_data['sources']), len(frag['sources']), len(sources)))

DATE_RE = re.compile(r'^\d{4}(-\d{2}(-\d{2})?)?$')
errors, warns = [], []


def err(w, m):
    errors.append((w, m))


def warn(w, m):
    warns.append((w, m))


def parse_date(v):
    if v is None:
        return None
    s = str(v)
    if not DATE_RE.match(s):
        return 'shape'
    try:
        parts = s.split('-')
        return datetime.date(int(parts[0]), int(parts[1]) if len(parts) > 1 else 1,
                             int(parts[2]) if len(parts) > 2 else 1)
    except Exception:
        return 'invalid'


def check_ship_file(path):
    d = yaml.safe_load(open(path, encoding='utf-8'))
    if d is None:
        err(path, 'YAML failed to parse')
        return
    for k in ('id', 'name', 'facts'):
        if k not in d:
            err(path, 'missing top-level key %s' % k)
    open_note = d.get('open_ended_note')
    facts = d.get('facts') or []
    print('\n== %s : %d facts' % (path, len(facts)))
    seen = {}
    for i, f in enumerate(facts):
        where = '%s#%s[%d]' % (path, f.get('field', '?'), i)
        for k in ('field', 'value', 'src', 'valid'):
            if k not in f:
                err(where, 'missing required key %s' % k)
        fid = f.get('field')
        if fid not in FIELDS:
            err(where, 'field %r not registered' % fid)
            continue
        spec = FIELDS[fid]
        # src
        srcs = f.get('src')
        if not isinstance(srcs, list) or not srcs:
            err(where, 'src must be a non-empty list')
            srcs = []
        for s in srcs:
            if s not in sources:
                err(where, 'source %r not registered' % s)
            elif sources[s].get('tier') == 'E':
                err(where, 'source %r is tier E' % s)
            elif 'data' not in (sources[s].get('role') or []):
                warn(where, 'source %r role lacks data' % s)
        # valid
        v = f.get('valid')
        if not isinstance(v, dict):
            err(where, 'valid must be a mapping')
            continue
        if 'from' not in v:
            err(where, 'valid missing from')
        frm, to = v.get('from'), v.get('to')
        for lbl, val in (('from', frm), ('to', to)):
            if val is None:
                continue
            p = parse_date(val)
            if p in ('shape', 'invalid'):
                err(where, 'valid.%s=%r bad date' % (lbl, val))
        pf, pt = parse_date(frm), parse_date(to)
        if isinstance(pf, datetime.date) and isinstance(pt, datetime.date) and pf > pt:
            err(where, 'valid.from > valid.to')
        if to is None and not f.get('note') and not open_note:
            warn(where, 'valid.to empty and no note')
        # unit
        u = f.get('unit')
        if spec['unit'] is not None:
            if u is None:
                err(where, 'field %s needs unit %s' % (fid, spec['unit']))
            elif u != spec['unit']:
                err(where, 'unit %r != registry %r' % (u, spec['unit']))
        elif u is not None:
            warn(where, 'field %s has no unit but fact sets %r' % (fid, u))
        # type
        val = f['value']
        t = spec['type']
        if t in ('number', 'integer') and not isinstance(val, (int, float)):
            err(where, 'field %s is %s but value %r not numeric' % (fid, t, val))
        if t == 'bool' and not isinstance(val, bool):
            err(where, 'field %s is bool' % fid)
        if t == 'date':
            p = parse_date(val)
            if p in ('shape', 'invalid'):
                err(where, 'date field %s value %r bad' % (fid, val))
        if t == 'enum':
            allowed = spec.get('values') or []
            for vv in (val if isinstance(val, list) else [val]):
                if vv not in allowed:
                    err(where, '%s value %r not in enum' % (fid, vv))
        # qual
        if 'qual_keys' in spec:
            quals = f.get('qual') or {}
            need = set(spec['qual_keys'])
            have = set(quals)
            if not have:
                err(where, 'field %s needs qual %s' % (fid, spec['qual_keys']))
            else:
                miss = need - have
                if miss:
                    err(where, '%s missing qual %s' % (fid, sorted(miss)))
                av = spec.get('qual_values') or {}
                for k, vv in quals.items():
                    if k in av and vv not in av[k]:
                        err(where, 'qual %s=%r not allowed' % (k, vv))
        # confidence
        conf = f.get('confidence')
        if conf not in ('A', 'B', 'C', None):
            err(where, 'confidence %r invalid' % conf)
        if conf is None:
            warn(where, 'no confidence')
        comp = f.get('comparable')
        if comp is not None and not isinstance(comp, bool):
            err(where, 'comparable must be bool')
        seen.setdefault((fid, f.get('about', '')), 0)
        seen[(fid, f.get('about', ''))] += 1
    # duplicate values in same window = dispute report only
    return d


def check_article(path):
    d = yaml.safe_load(open(path, encoding='utf-8'))
    for k in ('ship', 'intro', 'history'):
        if k not in d:
            err(path, 'article missing %s' % k)
    intro = d.get('intro') or {}
    lead = intro.get('lead')
    if lead is None:
        err(path, 'intro missing lead')
    elif 'zh' not in lead:
        err(path, 'lead missing zh')
    paras = intro.get('paragraphs')
    if not isinstance(paras, list) or not paras:
        err(path, 'intro.paragraphs empty')
    else:
        for i, p in enumerate(paras):
            w = '%s#para[%d]' % (path, i)
            if not p.get('heading'):
                warn(w, 'no heading')
            txt = p.get('text') or {}
            if 'zh' not in txt:
                err(w, 'text missing zh')
            refs = p.get('src')
            if not refs:
                err(w, 'no src')
            else:
                for r in refs:
                    if r not in sources:
                        err(w, 'src %r unregistered' % r)
                    elif sources[r].get('tier') == 'E':
                        err(w, 'src %r is tier E' % r)
    VAGUE = re.compile(r'据说|有人认为|有人称|据信|或许|大概|应该是')
    n_ev = 0
    for sec in d.get('history') or []:
        if not sec.get('id'):
            err(path, 'history section missing id')
        if 'zh' not in (sec.get('title') or {}):
            err(path, 'history section title missing zh')
        evs = sec.get('events') or []
        if not evs:
            err(path, 'history section has no events')
        for j, ev in enumerate(evs):
            w = '%s#%s/ev[%d]' % (path, sec.get('id'), j)
            if not ev.get('date'):
                err(w, 'event missing date')
            elif not DATE_RE.match(str(ev.get('date'))):
                err(w, 'event date %r bad' % ev.get('date'))
            if 'zh' not in (ev.get('text') or {}):
                err(w, 'event text missing zh')
            refs = ev.get('src') or []
            if not refs:
                err(w, 'event missing src')
            for r in refs:
                if r not in sources:
                    err(w, 'src %r unregistered' % r)
                elif sources[r].get('tier') == 'E':
                    err(w, 'src %r is tier E' % r)
            n_ev += 1
    # vague wording scan across whole file
    raw = open(path, encoding='utf-8').read()
    for m in set(VAGUE.findall(raw)):
        warn(path, 'vague wording %r in article' % m)
    print('article: %d paras, %d sections, %d events' % (len(paras or []), len(d.get('history') or []), n_ev))


def check_slices(path):
    d = yaml.safe_load(open(path, encoding='utf-8'))
    if 'ship' not in d or 'slices' not in d:
        err(path, 'slices file missing ship/slices')
    codes = []
    prev_to = None
    for s in d['slices']:
        w = '%s#%s' % (path, s.get('code'))
        for k in ('code', 'title', 'from'):
            if k not in s:
                err(w, 'slice missing %s' % k)
        if not DATE_RE.match(str(s.get('from'))):
            err(w, 'from %r bad' % s.get('from'))
        if s.get('to') and not DATE_RE.match(str(s.get('to'))):
            err(w, 'to %r bad' % s.get('to'))
        if not s.get('note'):
            warn(w, 'slice has no note')
        codes.append(s.get('code'))
    print('slices: %d %s' % (len(codes), codes))


for p in ['classes/n-class.yaml', 'ships/piorun.yaml']:
    check_ship_file(os.path.join(STG, p))
check_article(os.path.join(STG, 'articles', 'piorun.yaml'))
check_slices(os.path.join(STG, 'slices', 'piorun.yaml'))

print('\n--- errors %d ---' % len(errors))
for w, m in errors:
    print('  X', w, '::', m)
print('--- warnings %d ---' % len(warns))
for w, m in warns:
    print('  !', w, '::', m)
