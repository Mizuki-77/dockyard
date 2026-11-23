# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = r"D:\deepseek harness\website-warships\work\staging\tg172"

# --- astoria: 1942-06 配置那条 armament.mount.summary，补否定证据 ---
p = ROOT + r"\ships\astoria.yaml"
t = open(p, encoding="utf-8").read()
old = """    src: [navypedia-neworleans, ussastoria-org]
    valid: { from: 1942-06-14, to: 1942-08-09 }
    confidence: C
    note: >-
      navypedia 改装表原句「mid-1942, all: - 8 x 1 - 12.7/90; + 6 x 1 - 20/70
      Mk 4, SC, Mk 3 radars」——**「all」指全级**，本舰的时间窗按
      「1942-06-14 改装完成」起算。"""
new = """    src: [navypedia-neworleans, ussastoria-org, navweaps-8in55-mk12-15]
    valid: { from: 1942-06-14, to: 1942-08-09 }
    confidence: C
    note: >-
      navypedia 改装表原句「mid-1942, all: - 8 x 1 - 12.7/90; + 6 x 1 - 20/70
      Mk 4, SC, Mk 3 radars」——**「all」指全级**，本舰的时间窗按
      「1942-06-14 改装完成」起算。
      **主炮仍是 Mk 9 系列，这一点有反面证据**：navweaps 的 8"/55 Mk 12/15
      页把装舰对象写成「Mark 12: Tuscaloosa (CA-37) sub-class, Wichita (CA-45)
      and Baltimore (CA-68)」并注明「The Tuscaloosa sub-class consisted of
      Tuscaloosa (CA-37), San Francisco (CA-38), Quincy (CA-39) and
      Vincennes (CA-44)」——**CA-32/34/36 一艘都不在这份名单里**。
      所以本舰从建成到沉没，主炮一直是 Mk 9 系列。"""
assert old in t, "astoria anchor not found"
t = t.replace(old, new, 1)
open(p, "w", encoding="utf-8").write(t)
print("astoria patched")

# --- portland: 1942 初配置那条 ---
p = ROOT + r"\ships\portland.yaml"
t = open(p, encoding="utf-8").read()
old = """    src: [navypedia-portland, navalenc-portland]
    valid: { from: 1942-02-01, to: 1943-05-01 }
    confidence: C
    note: >-
      navypedia 原句「early 1942, both: - 8 x 1 -12.7/90; + 4 x 4 - 28/75 Mk 1,
      12 x 1 - 20/70 Mk 4, SC, Mk 3, Mk 4 radars」。"""
new = """    src: [navypedia-portland, navalenc-portland, navweaps-8in55-mk12-15]
    valid: { from: 1942-02-01, to: 1943-05-01 }
    confidence: C
    note: >-
      navypedia 原句「early 1942, both: - 8 x 1 -12.7/90; + 4 x 4 - 28/75 Mk 1,
      12 x 1 - 20/70 Mk 4, SC, Mk 3, Mk 4 radars」。
      **主炮仍是 Mk 9 系列**：navweaps 的 8"/55 Mk 12/15 页装舰名单里
      （Tuscaloosa 子级 CA-37/38/39/44、Wichita、Baltimore、Oregon City）
      **没有 CA-33**，故中途岛当天本舰主炮必为 Mk 9 系列。"""
assert old in t, "portland anchor not found"
t = t.replace(old, new, 1)
open(p, "w", encoding="utf-8").write(t)
print("portland patched")
