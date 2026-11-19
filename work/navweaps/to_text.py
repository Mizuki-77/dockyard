import sys, re, html, pathlib

def strip(p):
    s = pathlib.Path(p).read_text(encoding='utf-8', errors='replace')
    s = re.sub(r'(?is)<(script|style).*?</\1>', ' ', s)
    s = re.sub(r'(?i)<br\s*/?>', '\n', s)
    s = re.sub(r'(?i)</(p|div|tr|li|h[1-6]|table)>', '\n', s)
    s = re.sub(r'(?i)</t[dh]>', ' | ', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s)
    s = re.sub(r'[ \t\u00a0]+', ' ', s)
    s = re.sub(r'\n\s*\n+', '\n', s)
    return s.strip()

for p in sys.argv[1:]:
    out = pathlib.Path(p).with_suffix('.txt')
    out.write_text(strip(p), encoding='utf-8')
    print(out, len(strip(p)))
