# -*- coding: utf-8 -*-
"""c1 自检：结构、字数、时间升序、来源登记、关联 id 真实性。"""
import glob
import io
import os
import re
import sys

import yaml

sys.stdout.reconfigure(encoding='utf-8')

DATE_RE = re.compile(r'^\d{4}(-\d{2}(-\d{2})?)?$')
VAGUE = re.compile(r'据说|有人认为|有人称|据信|或许|大概|应该是')

SHIP_IDS = {os.path.basename(p)[:-5] for p in glob.glob('data/ships/*.yaml') if '.bak' not in p}
BATTLE_IDS = {os.path.basename(p)[:-5] for p in glob.glob('data/battles/*.yaml') if '.bak' not in p}
reg = yaml.safe_load(io.open('data/sources.yaml', encoding='utf-8'))
KNOWN = {s['id'] for s in reg['sources']}
frag = yaml.safe_load(io.open('work/staging_cmdr/c1/sources-fragment.yaml', encoding='utf-8'))
for s in frag['sources']:
    KNOWN.add(s['id'])

errs, warns, infos = [], [], []


def cn_len(s):
    """按汉字计数的近似字数：中文按 1，连续的拉丁/数字串按 1 组计。"""
    s = re.sub(r'\s+', '', s)
    latin = re.findall(r'[A-Za-z0-9\-\.\'’]+', s)
    n_latin_chars = sum(len(x) for x in latin)
    return len(s) - n_latin_chars + len(latin)


for p in sorted(glob.glob('work/staging_cmdr/c1/commanders/*.yaml')):
    d = yaml.safe_load(io.open(p, encoding='utf-8'))
    name = os.path.basename(p)
    if d.get('id') != name[:-5]:
        errs.append('%s: id 与文件名不一致' % name)

    life = d.get('life') or {}
    for k in ('born', 'died'):
        v = life.get(k)
        if v and not DATE_RE.match(str(v)):
            errs.append('%s: life.%s 格式不对 %r' % (name, k, v))

    intro = d.get('intro') or []
    if not (3 <= len(intro) <= 5):
        errs.append('%s: intro 段数 %d 不在 3-5' % (name, len(intro)))
    for i, pa in enumerate(intro):
        n = cn_len(pa['text'])
        infos.append('%s intro[%d] %-14s %3d 字' % (name, i, pa['heading'], n))
        if not (100 <= n <= 220):
            errs.append('%s: intro[%d] 字数 %d 不在 100-220' % (name, i, n))
        m = VAGUE.search(pa['text'])
        if m:
            errs.append('%s: intro[%d] 出现模糊词「%s」' % (name, i, m.group()))

    tl = d.get('timeline') or []
    if not (8 <= len(tl) <= 20):
        errs.append('%s: timeline %d 条不在 8-20' % (name, len(tl)))
    prev = None
    for i, ev in enumerate(tl):
        dt = str(ev.get('date'))
        if not DATE_RE.match(dt):
            errs.append('%s: timeline[%d] date %r 格式不对' % (name, i, dt))
        if prev and dt < prev:
            errs.append('%s: timeline[%d] %s 早于上一条 %s' % (name, i, dt, prev))
        prev = dt
        if not ev.get('src'):
            errs.append('%s: timeline[%d] 缺 src' % (name, i))
        for s in ev.get('src') or []:
            if s not in KNOWN:
                errs.append('%s: timeline[%d] src %r 未登记' % (name, i, s))
        m = VAGUE.search(str(ev.get('text')))
        if m:
            errs.append('%s: timeline[%d] 出现模糊词「%s」' % (name, i, m.group()))

    rel = d.get('relations') or {}
    for t in rel.get('ships') or []:
        if t['ship'] not in SHIP_IDS:
            errs.append('%s: ship %r 不存在' % (name, t['ship']))
        for k in ('from', 'to'):
            if t.get(k) and not DATE_RE.match(str(t[k])):
                errs.append('%s: relation %s 格式不对' % (name, k))
        if t.get('from') and t.get('to') and str(t['from']) > str(t['to']):
            errs.append('%s: relation from 晚于 to' % name)
    for b in rel.get('battles') or []:
        if b['battle'] not in BATTLE_IDS:
            errs.append('%s: battle %r 不存在' % (name, b['battle']))

    for s in d.get('src') or []:
        if s not in KNOWN:
            errs.append('%s: 顶层 src %r 未登记' % (name, s))

    infos.append('%s: intro %d 段 / timeline %d 条 / 关联 %d 舰 %d 战役' % (
        name, len(intro), len(tl),
        len(rel.get('ships') or []), len(rel.get('battles') or [])))

for s in frag['sources']:
    for k in ('title', 'url', 'type', 'tier', 'role'):
        if k not in s:
            errs.append('sources-fragment: %s 缺 %s' % (s.get('id'), k))
    if s.get('tier') not in ('A', 'B', 'C', 'D', 'E'):
        errs.append('sources-fragment: %s tier 不对' % s.get('id'))
    for r in s.get('role') or []:
        if r not in ('data', 'narrative', 'rights', 'lead', 'image'):
            errs.append('sources-fragment: %s role %r 不合法' % (s.get('id'), r))

for m in infos:
    print(' .', m)
for m in warns:
    print(' !', m)
for m in errs:
    print(' x', m)
print('\n%d 错误 / %d 警告' % (len(errs), len(warns)))
