import io, os, re, sys, glob
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
D = r"D:\deepseek harness\website-warships\work\raw\enterprise"
DOC = r"D:\deepseek harness\website-warships\work\raw\enterprise-tech.md"

TRANS = str.maketrans({
    "\u201c": '"', "\u201d": '"', "\u2019": "'", "\u2018": "'",
    "\u2014": "-", "\u2013": "-", "\u00d7": "x", "\u00b7": " ",
    "\u2026": "...", "\u00a0": " ",
})

def norm(s):
    s = s.translate(TRANS)
    s = s.replace("*", "")
    s = re.sub(r"\|", " ", s)
    s = re.sub(r"[\[\]]", "", s)          # wiki footnote brackets
    s = re.sub(r"\s+", " ", s).strip()
    return s

corpus = []
for p in glob.glob(os.path.join(D, "*.txt")):
    corpus.append(norm(io.open(p, encoding="utf-8", errors="replace").read()))
big = " ".join(corpus)

def find(part):
    p2 = norm(part).replace('"', "")
    cand = big.replace('"', "")
    if p2 in cand:
        return True
    p3 = re.sub(r"[\.,;:]+$", "", p2)
    return p3 in cand

doc = io.open(DOC, encoding="utf-8").read()
quotes = re.findall(r"\u300c([^\u300d]{12,})\u300d", doc)
miss, checked = [], 0
for q in quotes:
    if not re.search(r"[A-Za-z]{3}", q):
        continue
    # split on declared separators: ellipsis, arrow, middle dot, slash-join, plus-join
    parts = re.split(r"\s*(?:\.\.\.|\u2026|\u25b6|\u00b7|\s/\s|\s\+\s)\s*", q)
    for part in parts:
        part = part.strip()
        if len(part) < 10 or not re.search(r"[A-Za-z]{3}", part):
            continue
        checked += 1
        if not find(part):
            miss.append(part[:130])
print("quotes=%d checked_parts=%d UNVERIFIED=%d" % (len(quotes), checked, len(miss)))
for m in miss:
    print("  UNVERIFIED:", m)
