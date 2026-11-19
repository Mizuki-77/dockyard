# -*- coding: utf-8 -*-
"""给现有两场战斗的事件流标 major（关键节点）。

规则：每场标 5–7 条，覆盖「开始 → 转折 → 结束」的骨架。
刻意不按时间间隔均匀抽稀——那样会砍掉转折点、留下无关紧要的相邻条。
"""
import io
import re
from pathlib import Path

ROOT = Path(r"D:\deepseek harness\website-warships")

# 用「时刻字符串 → 是否 major」映射，比按索引标稳（索引会随编辑漂移）
PLAN = {
    "denmark-strait": {
        "05:37",  # 德舰目视发现英舰
        "05:52",  # 胡德开火（且打错了船）
        "05:55",  # 俾斯麦开火
        "06:00",  # 第五次齐射击中胡德
        "06:01",  # 胡德断成两截沉没——整场战斗的结局
        "06:09",  # 德舰最后一轮齐射，战斗结束
    },
    "last-battle": {
        "05-26 10:30",  # 首次发现电报——追击开始
        "05-26 19:15",  # 皇家方舟第二波起飞
        "05-26 21:05",  # 艉部中雷
        "05-26 21:15",  # 舰已不可操纵——决定性损伤
        "05-26 21:40",  # Lütjens 最后一电
        "05-27 08:00",  # 最后的战斗开始（若存在）
        "05-27 10:39",  # 俾斯麦沉没（若存在）
    },
}


def mark(path, want):
    s = io.open(path, encoding="utf-8").read()
    orig = s
    n = 0

    # 处理两种写法：
    #   缩进 2 空格（last-battle 风格）：- time: 05-26 03:00
    #   缩进 2 空格带引号（denmark-strait 风格）：- time: '05:30'
    pat = re.compile(r"(\n(\s*)- time: '?([^'\n]+)'?\n)(\2  (?:text|major):)")

    def repl(m):
        nonlocal n
        head, ind, t, tail = m.group(1), m.group(2), m.group(3).strip(), m.group(4)
        if t in want and "major:" not in tail:
            n += 1
            return head + ind + "  major: true\n" + tail
        return m.group(0)

    s = pat.sub(repl, s)
    if s != orig:
        io.open(path, "w", encoding="utf-8").write(s)
    total = len(re.findall(r"\n\s*- time:", s))
    return n, total


for fid, want in PLAN.items():
    p = ROOT / "data" / "battles" / (fid + ".yaml")
    n, total = mark(p, want)
    print("%-16s 标了 %d 条 major / 共 %d 条事件" % (fid, n, total))
