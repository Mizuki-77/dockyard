"""把 navweaps 纯文本里的 Description 段落与关键日期字段摘成一份 digest，便于一次读完。"""
import io
import pathlib
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

FILES = sys.argv[1:]
LIMIT = 4200

for f in FILES:
    p = pathlib.Path(f)
    if not p.exists():
        print("MISSING", f)
        continue
    s = p.read_text(encoding="utf-8", errors="replace")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    print("=" * 30, p.name)
    cands = [m.start() for m in re.finditer(r"Description", s)]
    if cands:
        i = max(cands, key=lambda k: len(s[k:].split("Gun Characteristics")[0]))
        print(s[i : i + LIMIT])
    for k in ("Ship Class Used On", "Date Of Design", "Date In Service"):
        j = s.find(k)
        if j >= 0:
            seg = s[j : j + 220].replace("\n", " / ")
            print("[F]", seg)
    print()
