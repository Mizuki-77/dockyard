# -*- coding: utf-8 -*-
"""清洗 data/images.yaml 里 author 字段夹带的 HTML。

Commons 的 extmetadata Artist 本来就是 HTML 片段，我当时原样写进去了。
按源清洗比在渲染层补丁更好——数据本身就该是干净的。
"""
import html
import io
import re
from pathlib import Path

ROOT = Path(r"D:\deepseek harness\website-warships")
P = ROOT / "data" / "images.yaml"


def clean(s):
    if not s:
        return s
    t = re.sub(r"<[^>]*>", " ", s)
    t = html.unescape(t)
    t = re.sub(r"\s+", " ", t).strip()
    half = len(t) // 2
    if len(t) % 2 == 1 and t[:half] == t[half + 1:]:
        t = t[:half]
    elif len(t) % 2 == 0 and t[:half] == t[half:]:
        t = t[:half]
    return t


raw = io.open(P, encoding="utf-8").read()
lines = raw.split("\n")
out = []
n = 0
for ln in lines:
    m = re.match(r"^    author: (.+)$", ln)
    if not m:
        out.append(ln)
        continue
    val = m.group(1).strip()
    # 去掉外层引号再看
    quoted = val.startswith('"') and val.endswith('"')
    inner = val[1:-1] if quoted else val
    if "<" in inner or "&" in inner:
        newv = clean(inner)
        n += 1
        # 需要时加引号
        if any(c in newv for c in (":", "#", "'", '"')) or newv.startswith(("[", "{", "-", "?")):
            out.append('    author: "%s"' % newv.replace('"', '\\"'))
        else:
            out.append("    author: %s" % newv)
    else:
        out.append(ln)

io.open(P, "w", encoding="utf-8").write("\n".join(out))
print("清洗 %d 条 author" % n)
