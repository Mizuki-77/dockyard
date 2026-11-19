#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
校验器的自测。校验器自己不被验证，就不配拦别人的数据。

做法：每例造一个最小的坏数据目录，跑 validate.py，断言它真的报了对应的错。
"能跑通"不算数，"能拦住"才算数。

    python scripts/selftest.py
"""

import io
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VALIDATE = ROOT / "scripts" / "validate.py"

MIN_FIELDS = """
version: 1
units:
  t: { zh: 公吨, en: tonne, kind: mass }
  m: { zh: 米, en: metre, kind: length }
rejected_units:
  mt: 用 t
namespaces:
  displacement: 排水量
  dimensions: 尺度
  weapon: 武器
groups:
  - { id: dimensions, label: { zh: 尺寸, en: Dimensions }, order: 1 }
fields:
  - { id: displacement.standard, label: { zh: 标准排水量, en: Standard displacement }, type: number, unit: t, group: dimensions, compare: true, better: none }
  - { id: dimensions.length.oa,  label: { zh: 全长, en: Length overall }, type: number, unit: m, group: dimensions, compare: true, better: none }
  - { id: dimensions.ship_type, label: { zh: 舰种, en: Ship type }, type: enum, unit: null, group: dimensions, compare: false, better: none, values: [battleship, cruiser] }
  - { id: weapon.range.max, label: { zh: 最大射程, en: Max range }, type: number, unit: m, group: dimensions, compare: true, better: higher }
"""

MIN_SOURCES = """
version: 1
tiers:
  A: { label: { zh: 一手, en: Primary }, desc: x }
  D: { label: { zh: 专题站, en: Specialist }, desc: x }
  E: { label: { zh: 百科, en: Encyclopedia }, desc: x }
roles:
  data: 可作数据来源
  lead: 仅作线索
sources:
  - { id: good, title: Good Source, url: "https://example.org/a", type: website, tier: D, role: [data], access: direct, fetched: 2026-11-17 }
  - { id: wiki, title: Some Wiki, url: "https://example.org/b", type: encyclopedia, tier: E, role: [lead], access: direct, fetched: 2026-11-17 }
"""


def fact(**kw):
    base = {
        "field": "displacement.standard",
        "value": 41700,
        "unit": "t",
        "src": ["good"],
        "valid": {"from": "1940-08-24", "to": "1941-05-27"},
        "confidence": "B",
        "note": "ok",
    }
    base.update(kw)
    return base


CASES = [
    # (名字, fact 内容, 期望命中的错误关键词)
    ("正常 fact 应当通过", fact(), None),
    ("缺来源", {k: v for k, v in fact().items() if k != "src"}, "缺必填键"),
    ("src 为空列表", fact(src=[]), "没有来源"),
    ("来源未登记", fact(src=["nope"]), "未在 sources.yaml 登记"),
    ("tier E 当来源", fact(src=["wiki"]), "tier E"),
    ("缺 valid", {k: v for k, v in fact().items() if k != "valid"}, "缺必填键"),
    ("valid 缺 from", fact(valid={"to": "1941-05-27"}), "valid 缺 from"),
    ("日期格式错", fact(valid={"from": "Aug 1940", "to": "1941-05-27"}), "格式不对"),
    ("起止颠倒", fact(valid={"from": "1941-05-27", "to": "1940-08-24"}), "晚于"),
    ("单位不一致", fact(unit="kg"), "不一致"),
    ("缺单位", fact(unit=None), "没写 unit"),
    ("用了拒收单位", fact(unit="mt"), "rejected_units"),
    ("值是字符串", fact(value="41700"), "不是数字"),
    ("字段未注册", fact(field="displacement.fake"), "不在注册表里"),
    ("枚举值非法", fact(field="dimensions.ship_type", value="warship", unit=None), "不在枚举内"),
    ("枚举值合法", fact(field="dimensions.ship_type", value="battleship", unit=None), None),
    ("bool 当数值", fact(value=True), "布尔"),
    ("置信度非法", fact(confidence="X"), "confidence"),
    # comparable: false 是「口径对不上，别拿去排高低」的标记。
    # 只允许布尔；标了必须写 note（否则以后没人知道为什么被排除）；
    # 对本来就不参与对比的字段标它没有意义。
    ("comparable 非布尔", fact(comparable="false"), "comparable 必须是 true/false"),
    ("comparable false 但没写 note",
     {k: v for k, v in fact(comparable=False).items() if k != "note"},
     "comparable: false 但没写 note"),
    ("comparable false 用在 compare:false 字段上",
     fact(field="dimensions.ship_type", value="battleship", unit=None, comparable=False),
     "WARN:comparable: false 是多余的"),
    ("两条同窗不同值（应为警告）", None, "WARN:同一时间窗"),
    ("同源自相矛盾（应为警告）", None, "WARN:同一来源"),
    ("不同炮位同字段不算分歧", None, None),
]


def build(tmp, facts, extra_bad_sources=None):
    d = Path(tmp)
    (d / "ships").mkdir(parents=True, exist_ok=True)
    (d / "fields.yaml").write_text(MIN_FIELDS, encoding="utf-8")
    src = MIN_SOURCES
    if extra_bad_sources:
        src = src.replace("  - { id: wiki", extra_bad_sources + "\n  - { id: wiki")
    (d / "sources.yaml").write_text(src, encoding="utf-8")
    doc = {"id": "test", "name": "Test Ship", "facts": facts}
    import yaml
    (d / "ships" / "test.yaml").write_text(
        yaml.safe_dump(doc, allow_unicode=True, sort_keys=False), encoding="utf-8")


def run(tmp):
    p = subprocess.run(
        [sys.executable, str(VALIDATE), "--data", tmp, "--json"],
        capture_output=True, text=True, encoding="utf-8",
        env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"},
    )
    try:
        return json.loads(p.stdout)
    except json.JSONDecodeError:
        print("!! validate.py 没有输出合法 JSON：")
        print(p.stdout[:2000])
        print(p.stderr[:2000])
        raise


def main():
    fails = []
    for name, one, expect in CASES:
        tmp = tempfile.mkdtemp()
        try:
            if name.startswith("两条"):
                facts = [fact(), fact(value=43978, note=None)]
            elif name.startswith("同源"):
                # 同一个来源在同一时间窗给出两个值：不是合法分歧，是抄重了
                facts = [fact(), fact(value=43978)]
            elif name.startswith("不同炮位"):
                # 不同实体（about）的同一个字段，值本来就不同，不该判成分歧
                facts = [fact(field="weapon.range.max", value=35550, unit="m",
                              about="weapon:a"),
                         fact(field="weapon.range.max", value=23000, unit="m",
                              about="weapon:b")]
            else:
                facts = [one]
            build(tmp, facts)
            out = run(tmp)
            blob = json.dumps(out["errors"], ensure_ascii=False)
            wblob = json.dumps(out["warnings"], ensure_ascii=False)

            if expect is None:
                if out["errors"]:
                    fails.append(f"× {name}：不该报错，实际 {blob}")
                elif out["warnings"]:
                    fails.append(f"× {name}：不该报警告，实际 {wblob}")
                else:
                    print(f"√ {name}")
            elif expect.startswith("WARN:"):
                key = expect[5:]
                if key not in wblob:
                    fails.append(f"× {name}：期望警告含 {key!r}，实际警告 {wblob}")
                else:
                    print(f"√ {name}")
            else:
                if expect not in blob:
                    fails.append(f"× {name}：期望错误含 {expect!r}，实际 {blob}")
                else:
                    print(f"√ {name}")
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    # 注册表自身的坏数据
    tmp = tempfile.mkdtemp()
    try:
        (Path(tmp) / "ships").mkdir()
        (Path(tmp) / "fields.yaml").write_text(
            MIN_FIELDS.replace("unit: t, group: dimensions, compare: true",
                               "unit: mt, group: dimensions, compare: true", 1),
            encoding="utf-8")
        (Path(tmp) / "sources.yaml").write_text(MIN_SOURCES, encoding="utf-8")
        out = run(tmp)
        blob = json.dumps(out["errors"], ensure_ascii=False)
        if "rejected_units" not in blob:
            fails.append(f"× 注册表用了拒收单位：没拦住，{blob}")
        else:
            print("√ 注册表用了拒收单位")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    # 没抓到却填了抓取日期
    tmp = tempfile.mkdtemp()
    try:
        (Path(tmp) / "ships").mkdir()
        (Path(tmp) / "fields.yaml").write_text(MIN_FIELDS, encoding="utf-8")
        (Path(tmp) / "sources.yaml").write_text(
            MIN_SOURCES.replace(
                "role: [data], access: direct, fetched: 2026-11-17 }",
                "role: [data], access: direct, fetched: 2026-11-17, status: blocked, note: 被挡了 }"),
            encoding="utf-8")
        out = run(tmp)
        blob = json.dumps(out["errors"], ensure_ascii=False)
        if "却填了 fetched" not in blob:
            fails.append(f"× blocked 却填 fetched：没拦住，{blob}")
        else:
            print("√ blocked 却填 fetched")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    # narrative 层：最容易被悄悄抹平的是"只剩一种说法"
    NARR_GOOD = """
ship: test
narratives:
  - id: t-why
    question: { zh: "为什么？", en: Why }
    positions:
      - id: a
        claim: { zh: "甲说", en: "claim a" }
        held_by: [Someone Real]
        evidence: because
        source_refs: [good]
      - id: b
        claim: { zh: "乙说", en: "claim b" }
        held_by: [Another Person]
        evidence: because too
        source_refs: [good]
    status: disputed
    current_consensus: a
"""

    narr_cases = [
        ("narrative 正常应通过", NARR_GOOD, None),
        ("narrative 只剩一种说法",
         NARR_GOOD.replace("""      - id: b
        claim: { zh: "乙说", en: "claim b" }
        held_by: [Another Person]
        evidence: because too
        source_refs: [good]
""", ""), "至少要有 2 种说法"),
        ("narrative 主张者写'有人认为'",
         NARR_GOOD.replace("[Another Person]", "[有人认为]"), "模糊表述"),
        ("narrative 缺 held_by",
         NARR_GOOD.replace("        held_by: [Another Person]\n", ""), "缺 held_by"),
        ("narrative 引用未登记来源",
         NARR_GOOD.replace("source_refs: [good]\n    status", "source_refs: [ghost]\n    status"),
         "未登记来源"),
        ("narrative 的 current_consensus 指向不存在的说法",
         NARR_GOOD.replace("current_consensus: a", "current_consensus: zzz"),
         "不在 positions 的 id 里"),
    ]

    for name, body, expect in narr_cases:
        tmp = tempfile.mkdtemp()
        try:
            d = Path(tmp)
            (d / "ships").mkdir()
            (d / "narratives").mkdir()
            (d / "fields.yaml").write_text(MIN_FIELDS, encoding="utf-8")
            (d / "sources.yaml").write_text(MIN_SOURCES, encoding="utf-8")
            (d / "narratives" / "test.yaml").write_text(body, encoding="utf-8")
            out = run(tmp)
            blob = json.dumps(out["errors"], ensure_ascii=False)
            wblob = json.dumps(out["warnings"], ensure_ascii=False)
            if expect is None:
                if out["errors"] or out["warnings"]:
                    fails.append(f"× {name}：不该报问题，实际 {blob} {wblob}")
                else:
                    print(f"√ {name}")
            elif expect not in blob:
                fails.append(f"× {name}：期望错误含 {expect!r}，实际 {blob}")
            else:
                print(f"√ {name}")
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    print()
    if fails:
        print(f"自测失败 {len(fails)} 例：")
        for x in fails:
            print(" ", x)
        return 1
    print(f"自测全过（{len(CASES) + 2 + len(narr_cases)} 例）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
