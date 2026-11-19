import sys, re, os
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"D:\deepseek harness\website-warships\work\raw\yorktown-hornet-tech.md"
lines = open(p, encoding="utf-8").read().split("\n")

# 1) table column consistency per block
blocks, cur = [], []
for i, l in enumerate(lines):
    if l.strip().startswith("|"):
        cur.append((i + 1, l))
    else:
        if cur: blocks.append(cur); cur = []
if cur: blocks.append(cur)

print("TABLE BLOCKS:", len(blocks))
badblocks = 0
for b in blocks:
    counts = {}
    for ln, l in b:
        c = l.count("|")
        counts.setdefault(c, []).append(ln)
    if len(counts) > 1:
        badblocks += 1
        print("  MISMATCH block starting line %d:" % b[0][0])
        for c, lns in sorted(counts.items()):
            print("    pipes=%d rows: %s" % (c, lns[:8]))
print("BLOCKS WITH MISMATCH:", badblocks)

# 2) section presence
need = ["§0","§1","§2","§3","§4","§5","§6","§7","§8","§9","§10","§11","§12","§13","§14","§15","§16","§17"]
missing = [s for s in need if ("## " + s) not in open(p, encoding="utf-8").read()]
print("MISSING SECTIONS:", missing if missing else "none")

# 3) 未获取 counts
txt = open(p, encoding="utf-8").read()
print("未获取:", txt.count("未获取"))
print("未获取≠0 statement:", "「未获取」≠「0」" in txt)

# 4) source ids in 14.1 all used inline?
defined = set(re.findall(r"\| \*\*(S\d{1,2})\*\* \|", txt))
inline = set(re.findall(r"\bS(\d{1,2})\b", txt))
inline = {"S" + x for x in inline}
print("DEFINED:", sorted(defined, key=lambda s: int(s[1:])))
print("DEFINED BUT NEVER CITED:",
      sorted([d for d in defined if len(re.findall(r"\b" + d + r"\b", txt)) <= 1],
             key=lambda s: int(s[1:])))
