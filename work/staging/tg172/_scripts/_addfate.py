# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

AST = """

  # ============================================================ 结局判定（叙述）
  - field: service.fate_category
    value: >-
      1942-08-09 萨沃岛海战中被日军巡洋舰炮火击沉。破坏链是：中弹后机库内
      三架飞机与甲板上的艇起火 -> 火势引燃 5 英寸与 1.1 英寸弹药提升通道
      -> 前部 5 英寸弹药库在 1130 前后爆炸，把舷侧炸穿到水线以下
      -> 进水使左倾由 10 度增至 15 度 -> 1215 向左翻覆、尾部下坐沉没。
      这条链的每一环都出自 BuShips 战损报告 No.29 的原文。
    src: [nhhc-wdr29, danfs-astoria]
    valid: { from: 1942-08-09 }
    confidence: A
    note: >-
      战损报告原文（依次）：「the deck beneath grew hot」；
      「The fire by now had reached the lower 5" and 1.1" hoists as frequent
      explosions were heard below decks」；
      「a heavy explosion took place on the port side in way of the forward 5"
      magazines. The ship listed about 15° to port.」
      结论段：「In ASTORIA the initial heel was caused by the flooding of port
      side compartments due to the explosion of the 5" magazine.」
      **注意这不是「被鱼雷击沉」**：报告在 Quincy 与 Vincennes 两节都提到
      疑似鱼雷命中，在 Astoria 一节没有提；DANFS 也把 Astoria 的死因写作
      炮火与随之而来的火灾进水。这与 construction.fate_type 记的
      sunk_by_enemy 不冲突（fate_type 只分「被敌方击沉」这一类）。
"""

POR = """

  # ============================================================ 结局判定（叙述）
  - field: service.fate_category
    value: >-
      战后退役封存（1946-07-12 费城退役），1959-03-01 除籍，
      1959-10-06 出售给 Union Mineral and Alloys Corp. 拆解。无战斗损失。
    src: [danfs-portland]
    valid: { from: 1959-10-06 }
    confidence: B
    note: >-
      DANFS 原句：「she decommissioned at Philadelphia 12 July 1946 and was
      maintained in reserve status until struck from the Navy List 1 March 1959.
      The cruiser was sold to Union Mineral and Alloys Corp., New York, N.Y.
      6 October 1959 and scrapped.」
      三个节点：1946-07-12 退役 / 1959-03-01 除籍 / 1959-10-06 出售。
      与 construction.fate_date 的 1959-10-06 一致。
      **实际拆解完成日期未获取**（无来源给出拆完的时间）。
"""

for p, block in ((r"D:\deepseek harness\website-warships\work\staging\tg172\ships\astoria.yaml", AST),
                 (r"D:\deepseek harness\website-warships\work\staging\tg172\ships\portland.yaml", POR)):
    t = open(p, encoding="utf-8").read().rstrip("\n")
    open(p, "w", encoding="utf-8").write(t + "\n" + block)
    print("appended", p)
