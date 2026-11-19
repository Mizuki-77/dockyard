import re, html, sys
from pathlib import Path
def conv(p):
    s = Path(p).read_text(encoding="utf-8", errors="replace")
    s = re.sub(r"(?is)<(script|style|head)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</(p|div|tr|h[1-6]|li|table|blockquote)>", "\n", s)
    s = re.sub(r"(?i)</t[dh]>", " | ", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\xa0]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n\n", s)
    return s
for n in ["guardian-2001","bbc-2001"]:
    t = conv(str(Path(r"D:\deepseek harness\website-warships\work\raw\hood")/(n+".html")))
    Path(r"D:\deepseek harness\website-warships\work\raw\hood", n+".txt").write_text(t, encoding="utf-8")
    print(n, len(t))
