# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ADD = '''
  - id: navweaps-8in55-mk12-15
    title: 'USA 8"/55 (20.3 cm) Marks 12 and 15 — NavWeaps'
    url: https://www.navweaps.com/Weapons/WNUS_8-55_mk12-15.php
    type: website
    tier: C
    role: [data]
    operator: NavWeaps（Tony DiGiulian 编）
    lang: en
    access: direct
    fetched: 2026-11-23
    license: all_rights_reserved
    note: >
      **用来证明「阿斯托里亚与波特兰的主炮从没装过 Mk 12/15」这一否定命题。**
      关键原句（三句连读才能得出这个结论）：
      「Mark 12: Tuscaloosa (CA-37) sub-class, Wichita (CA-45) and
       Baltimore (CA-68)」
      「Mark 15: All other Baltimore class and Oregon City (CA-122) class」
      「Minneapolis (CA-36) was regunned with Mark 15 Mod 1 in 1945」
      另注「The Tuscaloosa sub-class consisted of Tuscaloosa (CA-37),
      San Francisco (CA-38), Quincy (CA-39) and Vincennes (CA-44).」
      ——即 Mk 12/15 的装舰名单里，新奥尔良级只有 CA-37/38/39/44 这四艘，
      CA-32/34/36 一艘都不在其中；CA-36 明尼阿波利斯是 1945 年单独换装的，
      而 CA-34 阿斯托里亚 1942-08 已沉没。
      因此「中途岛时两舰主炮是 Mk 9 系列」有正面（navweaps-8in55-mk9）与
      反面（本条）双重依据。
      口径提示：本页只给炮本身（含药室 79.6 dm3、初速与 Mk 9 系列同表另列），
      炮座数据在 navweaps-8in55-mk9 那一页。
'''

p = r"D:\deepseek harness\website-warships\work\staging\tg172\sources-fragment.yaml"
t = open(p, encoding="utf-8").read().rstrip("\n")
open(p, "w", encoding="utf-8").write(t + "\n" + ADD)
print("ok")
