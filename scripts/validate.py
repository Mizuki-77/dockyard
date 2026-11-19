#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
P0 数据校验器。

用法：
    python scripts/validate.py                 校验全部
    python scripts/validate.py --ship bismarck 只校验一个
    python scripts/validate.py --strict        警告也当错误（CI 用）
    python scripts/validate.py --json          机器可读输出

设计原则：
  1. 宁可吵，不可静默放过。任何拿不准的都进 warnings，不吞。
  2. 报错必须给出可执行的修法，不只说"错了"。
  3. 自己先跑通：造假数据测试见 scripts/selftest.py。
"""

import argparse
import io
import json
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("需要 PyYAML：pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"



class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.infos = []

    def err(self, where, msg, fix=None):
        self.errors.append({"where": where, "msg": msg, "fix": fix})

    def warn(self, where, msg, fix=None):
        self.warnings.append({"where": where, "msg": msg, "fix": fix})

    def info(self, msg):
        self.infos.append(msg)

    @property
    def ok(self):
        return not self.errors


LAST_LOAD_ERROR = {}


def load(path):
    """读 YAML。解析失败**不抛异常**——校验器自己崩了，就没法告诉用户
    是哪个文件的哪一行坏了，等于把最需要报错的情况变成黑屏。"""
    if not path.exists():
        return None
    try:
        with io.open(path, encoding="utf-8") as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        mark = getattr(e, "problem_mark", None)
        where = f"第 {mark.line + 1} 行第 {mark.column + 1} 列" if mark else "位置未知"
        LAST_LOAD_ERROR[str(path)] = f"YAML 语法错误（{where}）：{getattr(e, 'problem', e)}"
        return None
    except OSError as e:
        LAST_LOAD_ERROR[str(path)] = f"读文件失败：{e}"
        return None


# ---------------------------------------------------------------- 注册表

FIELD_REQUIRED = {"id", "label", "type", "unit", "group", "compare", "better"}
VALID_TYPES = {"number", "integer", "string", "enum", "bool", "date", "ref", "table"}
VALID_BETTER = {"higher", "lower", "context", "none"}
VALID_GROUPS = {
    "identity", "dimensions", "propulsion", "protection", "armament",
    "sensors", "aviation", "construction", "service", "appearance",
    "media", "modelling", "weapon",
}
NAMESPACE_RE = re.compile(r"^[a-z][a-z0-9_]*(\.[a-z0-9_]+)+$")


def check_fields(reg, rep):
    """字段注册表自身的一致性。"""
    fields = reg.get("fields") or []
    units = set((reg.get("units") or {}).keys())
    rejected = set((reg.get("rejected_units") or {}).keys())
    namespaces = set((reg.get("namespaces") or {}).keys())

    seen = {}
    for i, f in enumerate(fields):
        where = f"fields.yaml#{i}"
        if not isinstance(f, dict):
            rep.err(where, "字段条目不是映射", "检查缩进，每条应为 - { id: ... }")
            continue

        missing = FIELD_REQUIRED - set(f)
        if missing:
            rep.err(where, f"缺必填键 {sorted(missing)}", f"字段 {f.get('id', '?')}")
            continue

        fid = f["id"]
        where = f"fields.yaml:{fid}"

        # id 唯一
        if fid in seen:
            rep.err(where, f"id 重复，首次出现在 #{seen[fid]}", "字段 id 必须唯一")
        seen[fid] = i

        # id 形状
        if not NAMESPACE_RE.match(fid):
            rep.err(where, "id 不符合 namespace.name[.sub] 且全小写", "例：propulsion.speed.trial")

        # 命名空间已注册
        ns = fid.split(".")[0]
        if ns not in namespaces:
            rep.err(where, f"命名空间 {ns} 未在 namespaces 段登记", f"在 namespaces 段加 {ns}: ...")

        # group 合法
        if f["group"] not in VALID_GROUPS:
            rep.err(where, f"group {f['group']} 不在合法集合内", f"合法值：{sorted(VALID_GROUPS)}")

        # type 合法
        if f["type"] not in VALID_TYPES:
            rep.err(where, f"type {f['type']} 不合法", f"合法值：{sorted(VALID_TYPES)}")

        # better 合法
        if f["better"] not in VALID_BETTER:
            rep.err(where, f"better {f['better']} 不合法", f"合法值：{sorted(VALID_BETTER)}")

        # compare 必须是布尔
        if not isinstance(f["compare"], bool):
            rep.err(where, "compare 必须是 true/false，不能是字符串", "去掉引号")

        # unit：null 或已注册；不能是 rejected
        u = f["unit"]
        if u is not None:
            if u in rejected:
                rep.err(where, f"单位 {u} 在 rejected_units 里", f"改用已注册单位：{sorted(units)}")
            elif u not in units:
                rep.err(where, f"单位 {u} 未注册", f"在 units 段登记，或改用：{sorted(units)}")

        # label 双语
        lab = f["label"]
        if not isinstance(lab, dict) or not {"zh", "en"} <= set(lab):
            rep.err(where, "label 必须同时有 zh 和 en", "label: { zh: ..., en: ... }")

        # enum 必须给 values，且 values 非空
        if f["type"] == "enum":
            if not f.get("values"):
                rep.err(where, "enum 类型缺 values", "values: [a, b, c]")
            elif len(set(f["values"])) != len(f["values"]):
                rep.err(where, "values 里有重复项", "")

        # 带限定的字段必须声明 qual_keys / qual_values
        if "qual_keys" in f:
            qk, qv = f["qual_keys"], f.get("qual_values") or {}
            if set(qk) != set(qv):
                rep.err(where, "qual_keys 与 qual_values 的键集合不一致", "每个 qual_key 都要有对应取值表")

        # 非限定字段不应出现 qual_*
        if "qual_keys" not in f and "qual_values" in f:
            rep.err(where, "有 qual_values 但没有 qual_keys", "")

        # compare=true 的字段必须能比，不能是 string/table/ref
        if f["compare"] and f["type"] in {"string", "table", "ref"}:
            rep.warn(where, f"compare=true 但 type={f['type']} 不可数值比较",
                     "改为 compare: false，或把类型改成 number/integer")

        # compare=false 却给了方向性 better —— 真矛盾：既然不比，凭什么说越高越好
        # better: context 不算矛盾，它表示"可并列展示但不判优劣"（装甲厚度、GM 等）
        if not f["compare"] and f["better"] in {"higher", "lower"}:
            rep.warn(where, f"compare=false 却声明 better={f['better']}",
                     "不比就不判优劣；要么 compare 改 true，要么 better 改 context/none")

    return {f["id"]: f for f in fields if isinstance(f, dict) and "id" in f}


def check_sources(reg, rep):
    """来源登记表自身的一致性。"""
    tiers = set((reg.get("tiers") or {}).keys())
    roles = set((reg.get("roles") or {}).keys())
    sources = reg.get("sources") or []

    out = {}
    for i, s in enumerate(sources):
        where = f"sources.yaml#{i}"
        if not isinstance(s, dict):
            rep.err(where, "来源条目不是映射", "")
            continue
        sid = s.get("id")
        if not sid:
            rep.err(where, "缺 id", "")
            continue
        where = f"sources.yaml:{sid}"

        if sid in out:
            rep.err(where, "id 重复", "来源 id 必须唯一")
        out[sid] = s

        for k in ("title", "url", "type", "tier", "role"):
            if k not in s:
                rep.err(where, f"缺 {k}", "")

        if s.get("tier") not in tiers:
            rep.err(where, f"tier {s.get('tier')} 不在 tiers 段内", "")

        for r in s.get("role") or []:
            if r not in roles:
                rep.err(where, f"role {r} 不在 roles 段内", f"合法值：{sorted(roles)}")

        st = s.get("status", "ok")
        if st not in {"ok", "not_fetched", "blocked", "gone"}:
            rep.err(where, f"status {st} 不合法", "ok / not_fetched / blocked / gone")

        # 抓到了就得有日期
        if st == "ok" and not s.get("fetched"):
            rep.warn(where, "status=ok 但没有 fetched 日期", "填抓取日期 YYYY-MM-DD")

        # 没抓到却填了日期，是自欺
        if st in {"blocked", "not_fetched", "gone"} and s.get("fetched"):
            rep.err(where, f"status={st} 却填了 fetched={s['fetched']}",
                    "没抓到就别填日期，改回 status 或删掉 fetched")

        # 挡住的必须说明原因
        if st in {"blocked", "gone"} and not s.get("note"):
            rep.err(where, f"status={st} 但没写 note", "写清为什么失败，避免下次重复踩坑")

        if s.get("access") not in {"direct", "proxy", None}:
            rep.err(where, f"access {s.get('access')} 不合法", "direct / proxy")

    return out


# ---------------------------------------------------------------- 舰船数据

DATE_RE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")
SHIP_REQUIRED_FILE = {"id", "name", "facts"}
FACT_REQUIRED = {"field", "value", "src", "valid"}


def parse_date(s):
    if not isinstance(s, (str, date)):
        return None
    s = str(s)
    if not DATE_RE.match(s):
        return "shape"
    try:
        if len(s) == 4:
            return date(int(s), 1, 1)
        if len(s) == 7:
            return date(int(s[:4]), int(s[5:7]), 1)
        return date(int(s[:4]), int(s[5:7]), int(s[8:10]))
    except ValueError:
        return "invalid"


def check_narrative(path, sources, rep):
    """narrative 文件：争议并列的结构校验。

    这里的检查不是为了"字段对不对"，而是为了守住三条会让争议被
    悄悄抹平的入口：删掉某一种说法、把没署名的观点写进来、
    把主流说当成结论。
    """
    try:
        rel = path.relative_to(ROOT).as_posix()
    except ValueError:
        rel = path.as_posix()
    d = load(path)
    if d is None:
        rep.err(rel, LAST_LOAD_ERROR.get(str(path), "文件读不出来（YAML 解析失败）"), "")
        return

    if "ship" not in d:
        rep.err(rel, "缺顶层键 ship", "narrative 必须挂在具体舰上")
    items = d.get("narratives")
    if not isinstance(items, list) or not items:
        rep.err(rel, "缺 narratives 列表或为空", "")
        return

    seen = set()
    for i, n in enumerate(items):
        nid = n.get("id")
        where = f"{rel}#{nid or ('narratives[%d]' % i)}"
        if not nid:
            rep.err(where, "缺 id", "")
        elif nid in seen:
            rep.err(where, "id 重复", "")
        else:
            seen.add(nid)

        q = n.get("question")
        if not isinstance(q, dict) or not q.get("zh") or not q.get("en"):
            rep.err(where, "question 必须同时有 zh 与 en", "")

        pos = n.get("positions")
        if not isinstance(pos, list) or len(pos) < 2:
            rep.err(where, "positions 至少要有 2 种说法，"
                           "只有一种就不叫争议，应该降级成 fact", "")
            continue

        pids = set()
        for j, p in enumerate(pos):
            pw = f"{where}/{'positions[%d]' % j}"
            pid = p.get("id")
            if not pid:
                rep.err(pw, "缺 id", "")
            elif pid in pids:
                rep.err(pw, "id 重复", "")
            else:
                pids.add(pid)

            claim = p.get("claim")
            if not isinstance(claim, dict) or not claim.get("zh"):
                rep.err(pw, "claim 缺 zh", "")
            if not isinstance(claim, dict) or not claim.get("en"):
                rep.warn(pw, "claim 缺 en", "双语站点的争议陈述也应有英文")

            held = p.get("held_by")
            if not held:
                # 这是 narrative 存在的意义所在：没署名的观点不进 narrative。
                rep.err(pw, "缺 held_by（主张者）",
                        "写具体的人名/机构名，不能是'有人认为'；"
                        "真的找不到主张者，说明这条不该进 narrative")
            elif isinstance(held, list):
                vague = re.compile(r"有人认为|有人|部分人|据称|"
                                   r"\bsome\b|\bmany\b|\bscholars\b", re.I)
                bad = [h for h in held if vague.search(str(h))]
                if bad:
                    rep.err(pw, f"held_by 含模糊表述 {bad}",
                            "必须写具体主张者姓名或机构，不能写'有人认为'")

            if not p.get("evidence"):
                rep.warn(pw, "缺 evidence（为什么这么主张）", "")

            refs = p.get("source_refs") or []
            for r in refs:
                if r not in sources:
                    rep.err(pw, f"source_refs 引用了未登记来源 {r!r}", "先加进 data/sources.yaml")

        status = n.get("status")
        if status not in {"disputed", "settled", "minority"}:
            rep.err(where, f"status {status!r} 不合法", "disputed / settled / minority")

        cc = n.get("current_consensus")
        if cc is not None and cc not in pids:
            rep.err(where, f"current_consensus {cc!r} 不在 positions 的 id 里", "")

    rep.info(f"{rel}: {len(seen)} 条 narrative，"
             f"共 {sum(len(n.get('positions') or []) for n in items)} 种说法")


BATTLE_REQUIRED = {"id", "name", "date", "timeline"}

# 与 src/lib/catalog.ts 的 THEATER_ORDER 保持一致。
# 两处各写一份是刻意的：validate.py 不 import TS，页面也不该为了一个枚举去读 py。
# 改这里必须同步改那里，validate 会在 theater 越界时报错，漏同步会立刻暴露。
THEATERS = {
    "atlantic", "north_sea", "mediterranean", "indian_ocean",
    "pacific", "arctic", "baltic", "other",
}



def check_battle(path, sources, rep, ship_ids=None):
    """battle 文件：战役是「有先后顺序的事件流」，校验重点和 fact 不同。

    这里守三条：事件必须有来源、时间必须能排序、参战舰只必须真实存在
    （否则页面上会出现指向 404 的链接）。
    """
    try:
        rel = path.relative_to(ROOT).as_posix()
    except ValueError:
        rel = path.as_posix()
    d = load(path)
    if d is None:
        rep.err(rel, LAST_LOAD_ERROR.get(str(path), "文件读不出来（YAML 解析失败）"), "")
        return

    for k in sorted(BATTLE_REQUIRED):
        if k not in d:
            rep.err(rel, f"缺顶层键 {k}", "")

    bid = d.get("id")
    if bid and path.stem != bid:
        rep.warn(rel, f"文件名 {path.stem!r} 与 id {bid!r} 不一致", "按 id 命名，改目录时不至于失联")

    name = d.get("name")
    if not isinstance(name, dict) or not name.get("zh") or not name.get("en"):
        rep.err(rel, "name 必须同时有 zh 与 en", "")

    dt = d.get("date")
    if isinstance(dt, dict):
        frm = dt.get("from")
        to = dt.get("to")
        for v, lbl in ((frm, "from"), (to, "to")):
            if v is None:
                continue
            s = str(v)
            if not re.match(r"^\d{4}(-\d{2}(-\d{2})?)?$", s):
                rep.err(rel, f"date.{lbl} {s!r} 不是 YYYY / YYYY-MM / YYYY-MM-DD", "")
        if frm and to and str(frm) > str(to):
            rep.err(rel, f"date.from {frm} 晚于 date.to {to}", "")
    elif dt is None:
        rep.err(rel, "缺 date", "战役必须有日期，哪怕只到年份")

    # theater 给「海战历史」左树做第一层分组。拼错会静默落到「其他海域」，
    # 所以这里按枚举拦：宁可构建失败，也不要一场仗从树上消失。
    th = d.get("theater")
    if th is not None and th not in THEATERS:
        rep.err(rel, f"theater {th!r} 不在枚举内", f"合法值：{sorted(THEATERS)}")

    # 参战舰只必须能解析到真实舰艇文件，否则站内链接会断
    for b in d.get("belligerents") or []:
        for s in b.get("ships") or []:
            sid = s.get("ship_id")
            if sid and ship_ids is not None and sid not in ship_ids:
                rep.err(f"{rel}#ship:{sid}", f"ship_id {sid!r} 没有对应的 data/ships/{sid}.yaml",
                        "先在 ships/ 建该舰文件，或去掉 ship_id 只留名字")

    tl = d.get("timeline")
    if not isinstance(tl, list) or not tl:
        rep.err(rel, "缺 timeline 列表或为空", "")
        return

    def tkey(t):
        """两种写法都收：
            '05:52' / '05:52:30'             —— 单日战斗，只有时刻
            '05-26 20:47' / '05-26 20:47:30' —— 跨日战斗，带月-日
        跨日时把「月、日」折进秒里（月按 31 天进位），否则「23:58 之后接 01:22」
        会被判成乱序。同一文件里两种写法不许混用——混用就没法比较大小。
        """
        s = str(t)
        md = re.match(r"^(\d{1,2})-(\d{1,2})\s+(\d{1,2}):(\d{2})(?::(\d{2}))?$", s)
        if md:
            mo, day, hh, mm, ss = (int(g or 0) for g in md.groups())
            return ((mo * 31 + day) * 24 + hh) * 3600 + mm * 60 + ss
        m = re.match(r"^(\d{1,2}):(\d{2})(?::(\d{2}))?$", s)
        if not m:
            return None
        return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3) or 0)

    # 同一战役里不允许「有时带日期、有时不带」——那样排序基准不一致，比出来的顺序是假的
    with_day = sum(1 for ev in tl if re.match(r"^\d{1,2}-\d{1,2}\s", str(ev.get("time") or "")))
    if 0 < with_day < len(tl):
        rep.err(rel, f"timeline 里 {with_day}/{len(tl)} 条带日期、其余不带",
                "跨日战役全用 '05-26 20:47'，单日战役全用 '05:52'，不要混")

    prev = None
    for i, ev in enumerate(tl):
        where = f"{rel}#timeline[{i}]"
        t = ev.get("time")
        if t is None:
            rep.err(where, "缺 time", "")
        else:
            k = tkey(t)
            if k is None:
                rep.err(where, f"time {t!r} 不是 HH:MM / HH:MM:SS，或带的跨日写法 'MM-DD HH:MM'", "")
            elif prev is not None and k < prev:
                rep.warn(where, f"time {t} 早于前一条，事件流不是顺序的",
                         "战役时间轴按时间正序写，页面不排序，写乱了就是错的")
            else:
                prev = k
        txt = ev.get("text")
        if not isinstance(txt, dict) or not txt.get("zh"):
            rep.err(where, "text 缺 zh", "")
        refs = ev.get("src") or []
        if not refs:
            rep.err(where, "缺 src", "战役里的每一条事件都要能追到来源")
        for r in refs:
            if r not in sources:
                rep.err(where, f"src 引用了未登记来源 {r!r}", "先加进 data/sources.yaml")

    # 命中 / 后果 / 伤亡三段的来源同样要能追
    for sect in ("hits_received", "consequences"):
        for i, ev in enumerate(d.get(sect) or []):
            where = f"{rel}#{sect}[{i}]"
            txt = ev.get("text")
            if not isinstance(txt, dict) or not txt.get("zh"):
                rep.err(where, "text 缺 zh", "")
            refs = ev.get("src") or []
            if not refs:
                rep.err(where, "缺 src", "")
            for r in refs:
                if r not in sources:
                    rep.err(where, f"src 引用了未登记来源 {r!r}", "")

    rep.info(f"{rel}: {len(tl)} 条时间轴事件，"
             f"{len(d.get('hits_received') or [])} 条命中记录")


OPERATION_REQUIRED = {"id", "name", "date", "phases"}


def check_operation(path, sources, rep, battle_ids=None):
    """operation 文件：战役系列（一次行动里的几场战斗）。

    这一层只存「顺序」和「定位」，不存战斗细节——所以校验重点不是数值，
    而是三条会悄悄把历史讲错的东西：
      1. phase 指向的 battle 必须真实存在，否则总览页的入口会 404；
      2. phase 必须有日期，且系列整体按日期正序，顺序错了读者会读成倒果为因；
      3. 每一站都要有 summary，否则总览页只剩标题，读者点进去才知道讲什么。
    """
    try:
        rel = path.relative_to(ROOT).as_posix()
    except ValueError:
        rel = path.as_posix()
    d = load(path)
    if d is None:
        rep.err(rel, LAST_LOAD_ERROR.get(str(path), "文件读不出来（YAML 解析失败）"), "")
        return

    for k in sorted(OPERATION_REQUIRED):
        if k not in d:
            rep.err(rel, f"缺顶层键 {k}", "")

    oid = d.get("id")
    if oid and path.stem != oid:
        rep.warn(rel, f"文件名 {path.stem!r} 与 id {oid!r} 不一致", "按 id 命名")

    name = d.get("name")
    if not isinstance(name, dict) or not name.get("zh") or not name.get("en"):
        rep.err(rel, "name 必须同时有 zh 与 en", "")

    dt = d.get("date")
    if isinstance(dt, dict):
        frm, to = dt.get("from"), dt.get("to")
        for v, lbl in ((frm, "from"), (to, "to")):
            if v is None:
                continue
            s = str(v)
            if not re.match(r"^\d{4}(-\d{2}(-\d{2})?)?$", s):
                rep.err(rel, f"date.{lbl} {s!r} 不是 YYYY / YYYY-MM / YYYY-MM-DD", "")
        if frm and to and str(frm) > str(to):
            rep.err(rel, f"date.from {frm} 晚于 date.to {to}", "")
    else:
        rep.err(rel, "缺 date", "一次行动必须有起止日期")

    top_refs = d.get("src") or []
    for r in top_refs:
        if r not in sources:
            rep.err(rel, f"顶层 src 引用了未登记来源 {r!r}", "")

    phases = d.get("phases")
    if not isinstance(phases, list) or not phases:
        rep.err(rel, "缺 phases 列表或为空", "一次行动至少要有一站")
        return

    prev = None
    seen_battles = set()
    for i, ph in enumerate(phases):
        where = f"{rel}#phases[{i}]"
        lbl = ph.get("label")
        if not (isinstance(lbl, dict) and lbl.get("zh")):
            rep.err(where, "label 缺 zh", "")

        pdt = ph.get("date")
        if not isinstance(pdt, dict) or pdt.get("from") is None:
            rep.err(where, "缺 date.from", "每一站都要有日期，否则顺序无从判断")
        else:
            s = str(pdt.get("from"))
            if not re.match(r"^\d{4}(-\d{2}(-\d{2})?)?$", s):
                rep.err(where, f"date.from {s!r} 不是 YYYY / YYYY-MM / YYYY-MM-DD", "")
            elif prev is not None and s < prev:
                rep.warn(where, f"date.from {s} 早于上一站 {prev}",
                         "系列按时间正序写，页面不排序")
            else:
                prev = s

        summ = ph.get("summary")
        if not (isinstance(summ, dict) and summ.get("zh")):
            rep.err(where, "summary 缺 zh", "总览页靠它介绍这一站，光有标题读者不知道讲了什么")

        bid = ph.get("battle")
        if bid:
            if battle_ids is not None and bid not in battle_ids:
                rep.err(f"{where}#battle:{bid}",
                        f"battle {bid!r} 没有对应的 data/battles/{bid}.yaml",
                        "总览页会链到 404；先在 battles/ 建该战役，或去掉 battle 只留标题")
            if bid in seen_battles:
                rep.err(where, f"battle {bid!r} 在同一个系列里重复出现", "一站对应一场战斗")
            seen_battles.add(bid)

        for r in ph.get("src") or []:
            if r not in sources:
                rep.err(where, f"src 引用了未登记来源 {r!r}", "")

    linked = sum(1 for ph in phases if ph.get("battle"))
    rep.info(f"{rel}: {len(phases)} 站，其中 {linked} 站已建独立战史页")


def check_operation_links(battles, operations, rep):
    """战役与系列之间的双向引用必须对得上。

    单向引用是这类结构最容易长歪的地方：把某场战斗从系列里删掉，
    战役页上的「上级行动」链接还在，读者点进去发现那一站已经没有了。
    所以两个方向都要查，且必须互为镜像。
    """
    op_ids = {o.get("id") for o in operations if isinstance(o, dict)}
    battle_ids = {b.get("id") for b in battles if isinstance(b, dict)}

    # 系列 → 战斗
    declared = {}
    for o in operations:
        if not isinstance(o, dict):
            continue
        oid = o.get("id")
        for i, ph in enumerate(o.get("phases") or []):
            bid = ph.get("battle")
            if bid:
                declared[bid] = oid

    # 战斗 → 系列
    for b in battles:
        if not isinstance(b, dict):
            continue
        bid, op = b.get("id"), b.get("operation")
        if not op:
            continue
        rel = f"data/battles/{path_stem(bid)}.yaml"
        if op not in op_ids:
            rep.err(rel, f"operation {op!r} 没有对应的 data/operations/{op}.yaml", "先建系列文件")
        elif declared.get(bid) != op:
            rep.err(rel, f"写的是 operation {op!r}，但该系列的 phases 里没有本站",
                    "两边必须互为镜像，否则战役页与总览页的链接会对不上")

    # 系列声明了、但战斗文件没写反向引用
    for bid, oid in declared.items():
        if bid not in battle_ids:
            continue  # 已由 check_operation 报过
        b = next((x for x in battles if isinstance(x, dict) and x.get("id") == bid), None)
        if b is not None and b.get("operation") != oid:
            rep.warn(f"data/battles/{path_stem(bid)}.yaml",
                     f"被 {oid!r} 的 phases 引用，但本站没写 operation: {oid}",
                     "补上以后战役页顶部会出现「上级行动」的返回入口")


def path_stem(s):
    return str(s or "")


ARTICLE_REQUIRED = {"ship", "intro", "history"}
# 武器正文与舰艇正文规则完全一样，只有顶层键从 ship 换成 weapon。
# 分开定义一个集合而不是把两个键都塞进 ARTICLE_REQUIRED，
# 是为了让「舰艇正文漏了 ship」和「武器正文漏了 weapon」各自报得准。
WEAPON_ARTICLE_REQUIRED = {"weapon", "intro", "history"}

# 这些词一出现，说明作者在替读者判断谁对谁错，或者在给观点打掩护。
# 争议归争议（narrative 里明写 held_by），正文里不许出现。
VAGUE_RE = re.compile(r"据说|有人认为|有人称|据信|或许|大概|应该是")


def _bi_ok(v):
    return isinstance(v, dict) and bool(v.get("zh"))


def check_article(path, sources, rep, ship_ids=None,
                  required=None, key="ship", known_ids=None):
    """article 文件：舰艇正文（简介 + 历史）。

    和 fact 的校验目标完全不同：fact 要单位、类型、时间窗，正文要的是
    「每句话都能追到来源」和「不许在正文里下结论」。所以这里一个字都不查数值。

    舰艇正文的顶层键是 ship，武器正文是 weapon，其余规则一字不差，所以用
    required / key / known_ids 三个参数复用同一套检查，而不是复制一份。
    """
    try:
        rel = path.relative_to(ROOT).as_posix()
    except ValueError:
        rel = path.as_posix()
    d = load(path)
    if d is None:
        rep.err(rel, LAST_LOAD_ERROR.get(str(path), "文件读不出来（YAML 解析失败）"), "")
        return

    for k in sorted(required or ARTICLE_REQUIRED):
        if k not in d:
            rep.err(rel, f"缺顶层键 {k}", "")

    sid = d.get(key)
    if sid and ship_ids is not None and sid not in ship_ids:
        rep.err(rel, f"{key} {sid!r} 没有对应的 data/ships/{sid}.yaml", "")
    if sid and known_ids is not None and sid not in known_ids:
        rep.err(rel, f"{key} {sid!r} 没有任何 data/ 文件登记过这个实体",
                "about: weapon:<id> 里没有它，页面会挂空")
    if sid and path.stem != sid:
        rep.warn(rel, f"文件名 {path.stem!r} 与 {key} {sid!r} 不一致",
                 "按实体 id 命名")

    def srcs_ok(where, refs):
        if not refs:
            rep.err(where, "缺 src", "正文的每一段都要能追到来源")
            return
        for r in refs:
            if r not in sources:
                rep.err(where, f"src 引用了未登记来源 {r!r}", "")
            elif sources[r].get("tier") == "E":
                rep.err(where, f"src {r!r} 是 E 层（百科/聚合站），不能作正文来源",
                        "E 层只能找线索，换一手档案或专题站")

    def text_ok(where, txt):
        if not _bi_ok(txt):
            rep.err(where, "text 缺 zh", "")
            return
        for lang in ("zh", "en"):
            body = (txt or {}).get(lang)
            if not body:
                continue
            if VAGUE_RE.search(str(body)):
                rep.warn(where, f"{lang} 正文出现模糊归属词：{VAGUE_RE.search(str(body)).group()}",
                         "要么写明是谁说的（放 narrative 的 held_by），要么删掉")

    # ---- intro ----
    intro = d.get("intro") or {}
    lead = intro.get("lead")
    if lead is None:
        rep.err(rel, "intro 缺 lead", "至少要有开场一段话")
    elif not _bi_ok(lead):
        rep.err(f"{rel}#intro.lead", "lead 缺 zh", "")
    # lead 不强制来源：它是摘要，来源在其下的段落里

    paras = intro.get("paragraphs")
    if not isinstance(paras, list) or not paras:
        rep.err(rel, "intro.paragraphs 为空", "简介至少一段")
    else:
        for i, p in enumerate(paras):
            where = f"{rel}#intro.paragraphs[{i}]"
            if not p.get("heading"):
                rep.warn(where, "缺 heading", "正文分节要有小标题，不然一大段读不下去")
            text_ok(where, p.get("text"))
            srcs_ok(where, p.get("src"))

    # ---- history ----
    hist = d.get("history")
    if not isinstance(hist, list) or not hist:
        rep.err(rel, "history 为空", "")
    else:
        seen = set()
        n_ev = 0
        for i, sec in enumerate(hist):
            secid = sec.get("id")
            where = f"{rel}#history/{secid or ('[%d]' % i)}"
            if not secid:
                rep.err(where, "缺 id", "")
            elif secid in seen:
                rep.err(where, "id 重复", "")
            else:
                seen.add(secid)

            if not _bi_ok(sec.get("title")):
                rep.err(where, "title 缺 zh", "")

            rng = sec.get("range") or {}
            frm, to = rng.get("from"), rng.get("to")
            for v, lbl in ((frm, "from"), (to, "to")):
                if v is None:
                    continue
                if not DATE_RE.match(str(v)):
                    rep.err(f"{where}/range", f"{lbl} {v!r} 不是 YYYY / YYYY-MM / YYYY-MM-DD", "")
            if frm and to and str(frm) > str(to):
                rep.err(f"{where}/range", f"from {frm} 晚于 to {to}", "")

            if sec.get("lead"):
                text_ok(f"{where}/lead", sec.get("lead"))

            evs = sec.get("events")
            if not isinstance(evs, list) or not evs:
                rep.err(where, "events 为空", "历史分节至少要有一条事件")
                continue
            for j, ev in enumerate(evs):
                ew = f"{where}/events[{j}]"
                dt = ev.get("date")
                if dt is None:
                    rep.err(ew, "缺 date", "")
                elif not DATE_RE.match(str(dt)):
                    rep.err(ew, f"date {dt!r} 不是 YYYY / YYYY-MM / YYYY-MM-DD", "")
                text_ok(ew, ev.get("text"))
                srcs_ok(ew, ev.get("src"))
                n_ev += 1

        rep.info(f"{rel}: 简介 {len(paras or [])} 段，历史 {len(hist)} 节 {n_ev} 条事件")


def check_ship(path, fields, sources, rep, strict, reg_all=None):
    """单舰 / 舰级数据文件。"""
    try:
        rel = path.relative_to(ROOT).as_posix()
    except ValueError:
        rel = path.as_posix()
    d = load(path)
    if d is None:
        rep.err(rel, LAST_LOAD_ERROR.get(str(path), "文件读不出来（YAML 解析失败）"),
                "YAML 语法错误会让整份数据静默丢失，必须先修")
        return None

    for k in SHIP_REQUIRED_FILE:
        if k not in d:
            rep.err(rel, f"缺顶层键 {k}", "")

    facts = d.get("facts") or []
    if not facts:
        rep.warn(rel, "没有任何 fact", "")

    # 文件级「开放时间窗」声明。舰级文件里绝大多数参数的有效期都是
    # 「从设计/服役起，直到被单舰覆盖或该级全部损失」，逐条写 note 纯属噪音。
    # 允许在文件顶层写一次 open_ended_note，说明为什么大量 valid.to 为空。
    open_note = d.get("open_ended_note")
    if open_note:
        rep.info(f"{rel}: 开放时间窗声明 —— {str(open_note)[:60]}")

    # 同一 field + 同一 valid 窗口出现多条 = 分歧（合法），但要报告
    buckets = defaultdict(list)
    ok_facts = 0
    notes = {}

    for i, f in enumerate(facts):
        where = f"{rel}#fact[{i}]"
        if not isinstance(f, dict):
            rep.err(where, "fact 不是映射", "")
            continue

        fid = f.get("field")
        where = f"{rel}#{fid or '?'}[{i}]"

        missing = FACT_REQUIRED - set(f)
        if missing:
            rep.err(where, f"缺必填键 {sorted(missing)}",
                    "必填：field / value / src / valid{from,to}")
            continue

        # 1. field 必须在注册表里
        if fid not in fields:
            near = [x for x in fields if fid and fid.split(".")[0] == x.split(".")[0]][:6]
            rep.err(where, f"字段 {fid} 不在注册表里",
                    f"要么改用已注册字段（同族：{near}），要么先往 data/fields.yaml 加")
            continue
        spec = fields[fid]

        # 2. src 至少一个，且必须登记过
        srcs = f["src"]
        if isinstance(srcs, str):
            rep.err(where, "src 必须是列表，不是字符串", "src: [kbismarck-genedata]")
            srcs = []
        if not srcs:
            rep.err(where, "fact 没有来源",
                    "至少给一个 src。找不到来源就不该写这条 fact")
            continue
        for s in srcs:
            if s not in sources:
                rep.err(where, f"来源 {s} 未在 sources.yaml 登记", "先登记再引用")

        # 3. tier E 不得支撑 fact
        for s in srcs:
            src = sources.get(s) or {}
            if src.get("tier") == "E":
                rep.err(where, f"来源 {s} 是 tier E（百科），不能作 fact 的 src",
                        "顺着百科的引用找到原始出处，登记后再引")
            if "data" not in (src.get("role") or []) and src:
                rep.warn(where, f"来源 {s} 的 role 不含 data", "确认它真能支撑数据")

        # 4. valid 时间窗
        v = f["valid"]
        if not isinstance(v, dict):
            rep.err(where, "valid 必须是映射 { from, to }", "")
            continue
        if "from" not in v:
            rep.err(where, "valid 缺 from", "时间窗必填，没确定就从该状态起始日填")
        frm, to = v.get("from"), v.get("to")
        for label, val in (("from", frm), ("to", to)):
            if val is None:
                continue
            p = parse_date(val)
            if p == "shape":
                rep.err(where, f"valid.{label}={val!r} 格式不对",
                        "用 YYYY / YYYY-MM / YYYY-MM-DD")
            elif p == "invalid":
                rep.err(where, f"valid.{label}={val!r} 不是合法日期", "")
        pf, pt = parse_date(frm), parse_date(to)
        if isinstance(pf, date) and isinstance(pt, date) and pf > pt:
            rep.err(where, f"valid.from({frm}) 晚于 valid.to({to})", "调换或修正")
        if to is None and not f.get("note") and not open_note:
            rep.warn(where, "valid.to 为空（表示至今有效/未知）但没写 note",
                     "写一句为什么没有结束时间，否则以后没人知道是忘了还是就是这样")

        # 5. 单位与注册表一致
        u = f.get("unit")
        rejected = set((reg_all.get("rejected_units") or {}).keys()) if reg_all else set()
        if u in rejected:
            rep.err(where, f"单位 {u} 在 rejected_units 里，含义不唯一或非公制",
                    f"{u}：{(reg_all.get('rejected_units') or {}).get(u, '')}")
        elif spec["unit"] is not None:
            if u is None:
                rep.err(where, f"字段 {fid} 的单位是 {spec['unit']}，fact 没写 unit",
                        f"unit: {spec['unit']}")
            elif u != spec["unit"]:
                rep.err(where, f"单位 {u} 与注册表 {spec['unit']} 不一致",
                        f"存储层统一公制，换算后写 {spec['unit']}")
        elif u is not None:
            rep.warn(where, f"字段 {fid} 注册为无单位，但 fact 写了 unit={u}", "")

        # 6. 类型粗查
        val = f["value"]
        t = spec["type"]
        if t in {"number", "integer"} and not isinstance(val, (int, float)):
            rep.err(where, f"字段 {fid} 是 {t}，但 value={val!r} 不是数字",
                    "去掉引号；若原文是区间/约数，拆成两条 fact 或写进 note")
        if t in {"number", "integer"} and isinstance(val, bool):
            rep.err(where, f"字段 {fid} 是数值，但 value 是布尔", "")
        if t == "bool" and not isinstance(val, bool):
            rep.err(where, f"字段 {fid} 是 bool，value 必须是 true/false", "")
        if t == "date":
            p = parse_date(val)
            if p in {"shape", "invalid"}:
                rep.err(where, f"字段 {fid} 是 date，value={val!r} 格式不对", "YYYY / YYYY-MM / YYYY-MM-DD")
        if t == "enum":
            allowed = spec.get("values") or []
            vals = val if isinstance(val, list) else [val]
            for vv in vals:
                if vv not in allowed:
                    rep.err(where, f"{fid} 的值 {vv!r} 不在枚举内", f"合法值：{allowed}")

        # 7. 限定字段：整数字段必须给齐 qual_keys 对应的限定值
        if "qual_keys" in spec:
            quals = f.get("qual") or {}
            need = set(spec["qual_keys"])
            have = set(quals)
            if not have:
                rep.err(where, f"字段 {fid} 需要限定词 {spec['qual_keys']}，fact 没给 qual",
                        f"qual: { {k: '<取值>' for k in spec['qual_keys']} }")
            else:
                miss = need - have
                if miss:
                    rep.err(where, f"{fid} 缺限定词 {sorted(miss)}", "")
                allowed_vals = spec.get("qual_values") or {}
                for k, vv in quals.items():
                    if k in allowed_vals and vv not in allowed_vals[k]:
                        rep.err(where, f"限定词 {k}={vv!r} 不在 {allowed_vals[k]} 内", "")

        # 8. 置信度
        conf = f.get("confidence")
        if conf not in {"A", "B", "C", None}:
            hint = "A / B / C，或不填（不填=按来源层级推断）"
            if conf == "D":
                # 这条踩过四次了（akagi / enterprise / soryu 都是）。D 是**来源层级**
                # （见 sources.yaml 的 tier），不是置信度。两者容易混，因为来源是
                # D 级专题站时，直觉上会写「这个值也是 D」。
                hint = ("D 是来源 tier（A–E），不是置信度。置信度只有 A/B/C——"
                        "它说的是「这个值有多可靠」，不是「这个来源属于哪档」。"
                        f"本值若来自 D 级来源，confidence 应填 C（或留空让它按来源推断）")
            rep.err(where, f"confidence {conf!r} 不合法", hint)
        if conf is None:
            rep.warn(where, "没写 confidence", "构建时会按来源 tier 推断，但显式写更稳")

        # 8b. comparable: false —— 「这条值的口径不是该字段要求的那个，别拿去排高低」。
        #    只允许布尔；且只对 compare: true 的字段有意义（不参与对比的字段本来就不排）。
        #    依据 2026-11-18 的口径判例：胡德号 displacement.standard=42,670 是
        #    navypedia 自己标为 "normal" 的档，硬排会让它显得比实际轻。
        comp = f.get("comparable")
        if comp is not None and not isinstance(comp, bool):
            rep.err(where, f"comparable 必须是 true/false，不能是 {comp!r}", "去掉引号")
        if comp is False:
            if not spec.get("compare"):
                rep.warn(where, f"{fid} 本来就不参与对比（compare: false），comparable: false 是多余的",
                         "删掉这个键，或确认这个字段是否该改为 compare: true")
            if not f.get("note"):
                rep.err(where, "comparable: false 但没写 note",
                        "必须说明是哪一处口径对不上（来源原话），否则以后没人知道为什么被排除")

        # 9. 多来源互证：这是**期望状态**，不是问题，只记 info。
        # 原先这里报 warn（"挂了 N 个来源但没写 note"）是判错了——多源互证
        # 恰恰是本站收录数据的正向标准，逐条要求写 note 只会训练人忽略警告。
        # 真正的风险（把两个互斥的值合成一条 fact）无法从单条 fact 看出，
        # 改由下面第 10 步「同源自相矛盾」来抓，那条是可计算的。
        if len(srcs) > 1:
            notes[where] = f"多来源互证（{len(srcs)} 个来源同一值）"

        # 分桶键必须带上实体与限定词，否则不同炮位/不同部位的同一个字段
        # 会被误判成分歧（Anton 的炮塔重 与 15cm 炮塔重 不是两种说法）。
        about = f.get("about") or ""
        qual_key = json.dumps(f.get("qual") or {}, ensure_ascii=False, sort_keys=True)
        buckets[(fid, about, qual_key, frm, to)].append((i, val, srcs, f.get("note")))
        ok_facts += 1

    # 分歧汇总（合法，但要让人看见）
    disputes = []
    for (fid, about, qual_key, frm, to), items in buckets.items():
        if len(items) < 2:
            continue
        # multi: true 的字段在同时间窗内本来就允许多条并存（雷达型号、涂装、
        # 电子战套件这类「同时装了好几样」的东西）。它们不是同一指标的两种说法，
        # 判成分歧会让每艘船都凭空多出几条假争议。
        if (fields.get(fid) or {}).get("multi"):
            continue
        vals = {json.dumps(it[1], ensure_ascii=False, sort_keys=True) for it in items}
        if len(vals) > 1:
            disputes.append({
                "field": fid, "about": about, "qual": qual_key,
                "from": frm, "to": to,
                "values": sorted(vals),
                "sources": [s for it in items for s in it[2]],
                "resolved": all(it[3] for it in items),
            })
            if not all(it[3] for it in items):
                tag = fid if not about else f"{about}:{fid}"
                rep.warn(f"{rel}:{tag}",
                         f"同一时间窗有 {len(vals)} 个不同值（{', '.join(sorted(vals))}）但没写 note",
                         "每条都写 note 说明差异来源，或拆开时间窗；页面会标『存在争议』")

            # 10. 同源自相矛盾：同一时间窗里，**同一个来源**给出了两个不同值。
            # 这不是合法分歧（合法分歧是不同来源说法不同），这是记错了或者
            # 抄重了，页面会同时显示两个值且都标着同一个出处，读者无法判断。
            for a in range(len(items)):
                for b in range(a + 1, len(items)):
                    va, vb = items[a][1], items[b][1]
                    if json.dumps(va, ensure_ascii=False, sort_keys=True) == \
                       json.dumps(vb, ensure_ascii=False, sort_keys=True):
                        continue
                    shared = set(items[a][2]) & set(items[b][2])
                    if shared:
                        tag = fid if not about else f"{about}:{fid}"
                        rep.warn(f"{rel}:{tag}",
                                 f"同一来源 {', '.join(sorted(shared))} 在同一时间窗给出两个值"
                                 f"（{va!r} / {vb!r}）",
                                 "同源不能自相矛盾：要么是抄重了，要么该来源本身有前后不一，"
                                 "请在 note 里点明是哪一处")

    if ok_facts:
        multi = len(notes)
        extra = f"，其中 {multi} 条为多来源互证" if multi else ""
        rep.info(f"{rel}: {ok_facts} 条 fact，{len(disputes)} 处同日窗分歧{extra}")

    return {"file": rel, "facts": ok_facts, "disputes": disputes}


# ---------------------------------------------------------------- 主流程

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ship", help="只校验 data/ships/<name>.yaml")
    ap.add_argument("--strict", action="store_true", help="警告也当失败")
    ap.add_argument("--json", action="store_true", help="JSON 输出")
    ap.add_argument("--data", help="数据目录（默认 data/，测试时指向临时目录）")
    args = ap.parse_args()

    global DATA
    if args.data:
        DATA = Path(args.data).resolve()

    rep = Report()
    fields_reg = load(DATA / "fields.yaml")
    sources_reg = load(DATA / "sources.yaml")

    if fields_reg is None:
        rep.err("data/fields.yaml",
                LAST_LOAD_ERROR.get(str((DATA / "fields.yaml").resolve()),
                                    "文件不存在或解析失败"), "")
        fields = {}
    else:
        fields = check_fields(fields_reg, rep)
        rep.info(f"字段注册表：{len(fields)} 个字段")

    if sources_reg is None:
        rep.err("data/sources.yaml",
                LAST_LOAD_ERROR.get(str((DATA / "sources.yaml").resolve()),
                                    "文件不存在或解析失败"), "")
        sources = {}
    else:
        sources = check_sources(sources_reg, rep)
        rep.info(f"来源登记表：{len(sources)} 条来源")

    # 舰船与舰级数据
    ships = []
    targets = []
    if args.ship:
        for sub in ("ships", "classes"):
            p = DATA / sub / f"{args.ship}.yaml"
            if p.exists():
                targets.append(p)
        if not targets:
            rep.err(f"data/ships/{args.ship}.yaml", "找不到", "")
    else:
        for sub in ("ships", "classes"):
            d = DATA / sub
            if d.exists():
                targets.extend(sorted(d.glob("*.yaml")))

    for p in targets:
        r = check_ship(p, fields, sources, rep, args.strict, fields_reg)
        if r:
            ships.append(r)

    # 叙述性争议
    narr_dir = DATA / "narratives"
    narr_targets = []
    if args.ship:
        p = narr_dir / f"{args.ship}.yaml"
        if p.exists():
            narr_targets.append(p)
    elif narr_dir.exists():
        narr_targets = sorted(narr_dir.glob("*.yaml"))
    for p in narr_targets:
        check_narrative(p, sources, rep)

    # 战役：参战舰只 id 必须能解析到真实文件
    battle_dir = DATA / "battles"
    ship_dir = DATA / "ships"
    ship_ids = {q.stem for q in ship_dir.glob("*.yaml")} if ship_dir.exists() else set()
    battle_ids = {q.stem for q in battle_dir.glob("*.yaml")} if battle_dir.exists() else set()
    if battle_dir.exists():
        for p in sorted(battle_dir.glob("*.yaml")):
            check_battle(p, sources, rep, ship_ids)

    # 战役系列：phase 指向的 battle 必须存在
    op_dir = DATA / "operations"
    if op_dir.exists():
        for p in sorted(op_dir.glob("*.yaml")):
            check_operation(p, sources, rep, battle_ids)

    # 双向引用必须互为镜像
    all_battles = [load(p) for p in sorted(battle_dir.glob("*.yaml"))] if battle_dir.exists() else []
    all_ops = [load(p) for p in sorted(op_dir.glob("*.yaml"))] if op_dir.exists() else []
    check_operation_links([b for b in all_battles if b], [o for o in all_ops if o], rep)

    # 对比器覆盖度：compare: true 但全库一条 fact 都没有 = 注册表和现实脱节。
    # 2026-11-18 P3 开工时清过一轮 5 个空字段（mine.capacity / speed.cruise /
    # turning_diameter / aviation.fuel.capacity 改为 false，standard_metric 补了数据），
    # 这条检查是防止下一个人再往注册表里加「空气字段」。
    #
    # 只报 info 不报 warn：selftest 的最小测试数据只有 1 条 fact，若报 warn
    # 会把 19 个用例全部污染成「不该报警告」。info 在正常输出里照样第一屏可见。
    if not args.ship and fields:
        used = set()
        for p in targets:
            dd = load(p) or {}
            for f in dd.get("facts") or []:
                if isinstance(f, dict) and f.get("field"):
                    used.add(f["field"])
        empty = sorted(fid for fid, spec in fields.items()
                       if spec.get("compare") and fid not in used)
        if empty:
            rep.info(f"对比器：{len(empty)} 个 compare:true 字段全库无数据 —— "
                     f"{', '.join(empty)}（建议补数据，或改 compare: false）")
        else:
            rep.info(f"对比器：{sum(1 for s in fields.values() if s.get('compare'))} 个 "
                     f"compare:true 字段全部有数据")

    # 正文（简介 + 历史）
    art_dir = DATA / "articles"
    art_targets = []
    if args.ship:
        p = art_dir / f"{args.ship}.yaml"
        if p.exists():
            art_targets.append(p)
    elif art_dir.exists():
        art_targets = sorted(art_dir.glob("*.yaml"))
    for p in art_targets:
        check_article(p, sources, rep, ship_ids)

    # 武器正文（简介 + 历史）。2026-11-18 接入：
    # 之前 data/weapon-articles/ 完全不在校验范围内，等于「页面有内容但没人验」。
    # --ship 模式只校验该舰的舰艇正文，不连带武器正文（武器与舰不是一对一）。
    wdir = DATA / "weapon-articles"
    if wdir.exists() and not args.ship:
        weapon_ids = set()
        for sub in ("ships", "classes"):
            for q in sorted((DATA / sub).glob("*.yaml")):
                dd = load(q) or {}
                for f in dd.get("facts") or []:
                    a = f.get("about") or ""
                    if a.startswith("weapon:"):
                        weapon_ids.add(a.split(":", 1)[1])
        for q in sorted(wdir.glob("*.yaml")):
            check_article(q, sources, rep, None,
                          required=WEAPON_ARTICLE_REQUIRED,
                          key="weapon", known_ids=weapon_ids)

    # 输出
    if args.json:
        # default=str 是必需的：PyYAML 会把 1941-05-24 解析成 datetime.date，
        # 而分歧记录里原样带着 valid.from/to。不加这个，一旦有分歧就整份输出崩掉。
        print(json.dumps({
            "ok": rep.ok and not (args.strict and rep.warnings),
            "errors": rep.errors, "warnings": rep.warnings,
            "infos": rep.infos, "ships": ships,
        }, ensure_ascii=False, indent=2, default=str))
    else:
        for m in rep.infos:
            print(f"  {m}")
        if rep.warnings:
            print(f"\n警告 {len(rep.warnings)} 条：")
            for w in rep.warnings:
                print(f"  ! {w['where']}\n    {w['msg']}")
                if w.get("fix"):
                    print(f"    → {w['fix']}")
        if rep.errors:
            print(f"\n错误 {len(rep.errors)} 条：")
            for e in rep.errors:
                print(f"  x {e['where']}\n    {e['msg']}")
                if e.get("fix"):
                    print(f"    → {e['fix']}")
        failed = bool(rep.errors) or (args.strict and bool(rep.warnings))
        print(f"\n{'失败' if failed else '通过'}："
              f"{len(rep.errors)} 错误 / {len(rep.warnings)} 警告")

    failed = bool(rep.errors) or (args.strict and bool(rep.warnings))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
