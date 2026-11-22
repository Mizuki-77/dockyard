import yaml, glob, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
VAGUE = re.compile(r"据说|有人认为|有人称|据信|或许|大概|应该是")
DATE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")
srcs = set()
for p in ['data/sources.yaml'] + glob.glob('work/staging/g7-weapons/sources-fragment.yaml'):
    d = yaml.safe_load(open(p, encoding='utf-8'))
    for s in d['sources']:
        srcs.add((s['id'], s.get('tier')))
srcmap = {i: t for i, t in srcs}
for p in sorted(glob.glob('work/staging/g7-weapons/weapon-articles/*.yaml')):
    d = yaml.safe_load(open(p, encoding='utf-8'))
    assert 'weapon' in d and 'intro' in d and 'history' in d, p
    wid = d['weapon']
    assert p.split('\\')[-1].split('/')[-1][:-5] == wid, (p, wid)
    npar = len(d['intro']['paragraphs'])
    nev = sum(len(s['events']) for s in d['history'])
    nsec = len(d['history'])
    bad = []
    for i, para in enumerate(d['intro']['paragraphs']):
        for r in para.get('src') or []:
            if r not in srcmap: bad.append(('para%d'%i, r, 'unregistered'))
            elif srcmap[r] == 'E': bad.append(('para%d'%i, r, 'tierE'))
        for lang in ('zh', 'en'):
            t = (para.get('text') or {}).get(lang)
            if t and VAGUE.search(str(t)): bad.append(('para%d'%i, lang, VAGUE.search(str(t)).group()))
    for sec in d['history']:
        for k in ('from', 'to'):
            v = (sec.get('range') or {}).get(k)
            if v is not None and not DATE.match(str(v)): bad.append((sec['id'], k, 'datefmt'))
        if sec.get('lead'):
            for lang in ('zh','en'):
                t = sec['lead'].get(lang)
                if t and VAGUE.search(str(t)): bad.append((sec['id'],'lead-'+lang,VAGUE.search(str(t)).group()))
        for j, ev in enumerate(sec['events']):
            if not DATE.match(str(ev['date'])): bad.append((sec['id'], j, 'datefmt'))
            if not (ev.get('src')): bad.append((sec['id'], j, 'nosrc'))
            for r in ev.get('src') or []:
                if r not in srcmap: bad.append((sec['id'], j, r+' unregistered'))
                elif srcmap[r] == 'E': bad.append((sec['id'], j, r+' tierE'))
            for lang in ('zh','en'):
                t = (ev.get('text') or {}).get(lang)
                if t and VAGUE.search(str(t)): bad.append((sec['id'], j, lang+' '+VAGUE.search(str(t)).group()))
    print(f"{wid}: intro {npar} 段 / history {nsec} 节 {nev} 事件 / 问题 {len(bad)}")
    for b in bad: print("   !", b)
