# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

p = r"D:\deepseek harness\website-warships\work\staging\tg172\ships\portland.yaml"
t = open(p, encoding="utf-8").read()

old_start = t.find("  - field: service.unit\n    value: Task Group 62.3 / 62.4")
old_end = t.find("  - field: service.unit\n    value: Task Force 16（圣克鲁斯")
assert old_start > 0 and old_end > old_start, "anchor not found"

new = """  - field: service.unit
    value: TG 61.1.2（太平洋舰队第 16 特混舰队，随企业号掩护瓜岛登陆）
    src: [danfs-portland, savo-nwc-3]
    valid: { from: 1942-08-07, to: 1942-08-09 }
    confidence: C
    note: >-
      **这一条纠正了一个很容易犯的错误：波特兰号在瓜岛登陆时不在
      TG 62.3 里，所以萨沃岛夜战没有她。**
      DANFS 只写到「Portland provided cover and support for the Marine
      landings at Tulagi and Guadalcanal, the Solomons 7 through 9 August」，
      不给编队号。编队号出自 NWC 萨沃岛分析报告第 3 章的兵力编成表：
      「(b) TG 61.2, Amphibious Force ... (3) TG 62.3 Fire Support Group LOVE /
      Quincy, Vincennes, Astoria, Hull, Dewey, Ellet, Wilson 4 DD /
      (4) TG S62.4 Fire Support Group MIKE / San Juan 1 CL (AA) /
      Monssen, Buchanan 2 DD」
      而本舰出现在上面另一个位置：「(2) TG 61.1.2 (Pacific Fleet Task Force 16) /
      Enterprise (38 VF, 36 VD, 10 VT) 1 CV / North Carolina 1 BB /
      Portland 1 CA / Atlanta 1 CL (AA) / Balch, Maury, Gwin, Benham,
      Grayson 5 DD」
      ——**她在企业号那一边，与阿斯托里亚号分属两个不同的特混群。**
      这也解释了为什么 1942-08-09 的夜战损失名单里没有她。

"""
t = t[:old_start] + new + t[old_end:]
open(p, "w", encoding="utf-8").write(t)
print("patched")
