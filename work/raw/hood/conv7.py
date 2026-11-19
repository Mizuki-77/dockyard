import re, html
from pathlib import Path
base = Path(r"D:\deepseek harness\website-warships\work\raw\hood")
def conv(name):
    s = base.joinpath(name).read_text(encoding="utf-8", errors="replace")
    s = re.sub(r"(?is)<(script|style|head)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</(p|div|tr|h[1-6]|li|table|blockquote)>", "\n", s)
    s = re.sub(r"(?i)</t[dh]>", " | ", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\xa0]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n\n", s)
    out = base.joinpath(name.replace(".htm",".txt"))
    out.write_text(s.strip(), encoding="utf-8")
    print(name, "->", len(s))
for n in ["of-116_to59.htm","of-116_61to88.htm","of-116_89to144.htm","of-116_Hood.htm"]:
    conv(n)
