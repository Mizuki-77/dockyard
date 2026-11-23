# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

p = r"D:\deepseek harness\website-warships\work\staging\tg172\sources-fragment.yaml"
t = open(p, encoding="utf-8").read()

old = """      用来核对「萨沃岛当晚各水面群编成」这一件事。本文件实际只用它一句：
      「(3) TG 62.3 Fire Support Group LOVE / Quincy, Vincennes, Astoria,
       Hull, Dewey, Ellet, Wilson 4 DD / (4) TG S62.4 Fire Support Group MIKE」
      ——**TG 62.4 的舰名在这一页没有展开**，所以波特兰号当晚属哪一群
      仍然未获取（不能因为两舰在中途岛同属 17.2 就推定它们在萨沃岛也同群）。
      口径提示：该报告是战后（1950）海军战争学院的分析著作，
      属权威二次文献记 C，不是一手战报；本章其余内容（航空搜索、日军编成）
      与本组两舰无直接关系，未使用。"""

new = """      **它是本组唯一给出「1942-08 瓜岛登陆时波特兰号到底在哪一群」的来源。**
      该页兵力编成表原文（节选）：
      「(b) TG 61.2, Amphibious Force (TF 62 plus SW Pac TF 44)
       (1) TG 62.1, Transport Group XRAY ...
       (2) TG 62.2, Transport Group YOKE ...
       (3) TG 62.3 Fire Support Group LOVE
       Quincy, Vincennes, Astoria, Hull, Dewey, Ellet, Wilson 4 DD
       (4) TG S62.4 Fire Support Group MIKE
       San Juan 1 CL (AA) / Monssen, Buchanan 2 DD」
      而在它上面的另一段：
      「(2) TG 61.1.2 (Pacific Fleet Task Force 16)
       Enterprise (38 VF, 36 VD, 10 VT) 1 CV
       North Carolina 1 BB / Portland 1 CA / Atlanta 1 CL (AA)
       Balch, Maury, Gwin, Benham, Grayson 5 DD」
      ——**波特兰号在 TG 61.1.2（企业号群），不在 TG 62.3，所以萨沃岛夜战里
      没有她。** 这条推翻了「两舰中途岛同属 17.2，所以瓜岛也在一起」的想当然。
      口径提示：该报告是战后（1950）海军战争学院的分析著作，
      属权威二次文献记 C，不是一手战报；本章其余内容（航空搜索、日军编成）
      与本组两舰无直接关系，未使用。"""

assert old in t, "anchor not found"
t = t.replace(old, new, 1)
open(p, "w", encoding="utf-8").write(t)
print("patched")
