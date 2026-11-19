import sys, re, html
from pathlib import Path
def conv(p, out):
    s = Path(p).read_text(encoding="utf-8", errors="replace")
    s = re.sub(r"(?is)<(script|style|head)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</(p|div|tr|h[1-6]|li|table)>", "\n", s)
    s = re.sub(r"(?i)</t[dh]>", " | ", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\xa0]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n\n", s)
    Path(out).write_text(s.strip(), encoding="utf-8")
    print(out, len(s))
base = Path(r"D:\deepseek harness\website-warships\work\raw\hood")
for f in ["kb-dsbattle.html","hood-tl5.html","hood-tl4.html"]:
    conv(base/f, base/(f.replace(".html",".txt")))
