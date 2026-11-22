# -*- coding: utf-8 -*-
"""g8-weapons2 自检：按 scripts/validate.py 的 check_article 规则跑一遍。

只读 data/sources.yaml 与 data/classes|ships/*.yaml，不改任何东西。
"""
import glob
import io
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.chdir(ROOT)

DATE_RE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")
VAGUE_RE = re.compile(r"据说|有人认为|有人称|据信|或许|大概|应该是")

srcs = {s["id"]: s for s in yaml.safe_load(open("data/sources.yaml", encoding="utf-8"))["sources"]}
frag = yaml.safe_load(open("work/staging/g8-weapons2/sources-fragment.yaml", encoding="utf-8"))
for s in frag["sources"]:
    for k in ("id", "title", "url", "type", "tier", "role"):
        if not s.get(k):
            print("FRAG 缺必填键", s.get("id"), k)
    if s["id"] in srcs:
        print("FRAG 重复登记（data/sources.yaml 已有）:", s["id"])
    srcs[s["id"]] = s
print("来源池:", len(srcs), "（新增", len(frag["sources"]), "条）")

known = set()
for sub in ("classes", "ships"):
    for p in glob.glob(f"data/{sub}/*.yaml"):
        d = yaml.safe_load(open(p, encoding="utf-8")) or {}
        for f in d.get("facts") or []:
            a = str(f.get("about") or "")
            if a.startswith("weapon:"):
                known.add(a.split(":", 1)[1])

errs, warns, infos = [], [], []
for p in sorted(glob.glob("work/staging/g8-weapons2/weapon-articles/*.yaml")):
    rel = p.replace("\\", "/")
    d = yaml.safe_load(open(p, encoding="utf-8")) or {}

    for k in ("weapon", "intro", "history"):
        if k not in d:
            errs.append(f"{rel} 缺顶层键 {k}")
    wid = d.get("weapon")
    if wid not in known:
        errs.append(f"{rel} weapon {wid!r} 没有任何 data/ 文件登记过这个实体")
    if os.path.basename(p)[:-5] != wid:
        warns.append(f"{rel} 文件名与 weapon {wid!r} 不一致")
    if str(d.get("updated")) != "2026-11-22":
        warns.append(f"{rel} updated 不是 2026-11-22")

    def chk(where, txt, need_src=True, src=None):
        if not isinstance(txt, dict) or not txt.get("zh"):
            errs.append(f"{where} text 缺 zh")
            return
        for lang in ("zh", "en"):
            body = txt.get(lang) or ""
            m = VAGUE_RE.search(str(body))
            if m:
                warns.append(f"{where} {lang} 出现模糊词 {m.group()!r}")
        if need_src:
            if not src:
                errs.append(f"{where} 缺 src")
            for r in src or []:
                if r not in srcs:
                    errs.append(f"{where} src 未登记 {r!r}")
                elif srcs[r].get("tier") == "E":
                    errs.append(f"{where} src {r!r} 是 E 层")

    intro = d.get("intro") or {}
    if not isinstance(intro.get("lead"), dict) or not intro.get("lead", {}).get("zh"):
        errs.append(f"{rel}#intro.lead 缺 zh")
    paras = intro.get("paragraphs") or []
    if not paras:
        errs.append(f"{rel}#intro.paragraphs 为空")
    for i, para in enumerate(paras):
        w = f"{rel}#intro.paragraphs[{i}]"
        if not para.get("heading"):
            warns.append(f"{w} 缺 heading")
        chk(w, para.get("text"), src=para.get("src"))

    n_ev, seen = 0, set()
    for i, sec in enumerate(d.get("history") or []):
        sid = sec.get("id")
        w = f"{rel}#history/{sid or i}"
        if not sid:
            errs.append(f"{w} 缺 id")
        elif sid in seen:
            errs.append(f"{w} id 重复")
        seen.add(sid)
        if not isinstance(sec.get("title"), dict) or not sec.get("title", {}).get("zh"):
            errs.append(f"{w} title 缺 zh")
        rng = sec.get("range") or {}
        for lbl in ("from", "to"):
            v = rng.get(lbl)
            if v is None:
                continue
            if not DATE_RE.match(str(v)):
                errs.append(f"{w}/range {lbl} {v!r} 格式不对")
        if rng.get("from") and rng.get("to") and str(rng["from"]) > str(rng["to"]):
            errs.append(f"{w}/range from 晚于 to")
        if sec.get("lead"):
            chk(f"{w}/lead", sec.get("lead"), need_src=False)
        evs = sec.get("events") or []
        if not evs:
            errs.append(f"{w} events 为空")
        for j, ev in enumerate(evs):
            ew = f"{w}/events[{j}]"
            dt = ev.get("date")
            if dt is None:
                errs.append(f"{ew} 缺 date")
            elif not DATE_RE.match(str(dt)):
                errs.append(f"{ew} date {dt!r} 格式不对")
            chk(ew, ev.get("text"), src=ev.get("src"))
            n_ev += 1
    infos.append(f"{rel}: intro {len(paras)} 段，history {len(d.get('history') or [])} 节 {n_ev} 条事件")

for l in infos:
    print("  ", l)
print()
for l in warns:
    print("WARN", l)
for l in errs:
    print("ERR ", l)
print()
print(f"errors={len(errs)} warnings={len(warns)}")
sys.exit(1 if errs else 0)
