# -*- coding: utf-8 -*-
"""Helpers to inspect _raw pages. Usage: python _tool.py links <page> [regex]
       python _tool.py text <page> [startre] [endre]
       python _tool.py grep <page> <regex> [-C n]
"""
import sys, os, re, html

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_raw")


def path_of(name):
    p = os.path.join(RAW, name)
    if not os.path.exists(p):
        p = os.path.join(RAW, name + ".txt")
    return p


def load(name):
    return open(path_of(name), encoding="utf-8", errors="replace").read()


def to_text(t):
    t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", t)
    t = re.sub(r"(?is)<br\s*/?>", "\n", t)
    t = re.sub(r"(?is)</(p|div|tr|h[1-6]|li|table)>", "\n", t)
    t = re.sub(r"(?is)</t[dh]>", " | ", t)
    t = re.sub(r"(?s)<[^>]+>", "", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t.strip()


def cmd_links(name, pat=None):
    t = load(name)
    rx = re.compile(pat, re.I) if pat else None
    for m in re.finditer(r'(?is)<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', t):
        href, label = m.group(1), to_text(m.group(2))
        if rx and not rx.search(href + " " + label):
            continue
        print("%s | %s" % (href, label[:120]))


def cmd_text(name, start=None, end=None):
    txt = to_text(load(name))
    if start:
        i = txt.find(start)
        if i < 0:
            print("[[start not found: %s]]" % start)
            i = 0
        txt = txt[i:]
    if end:
        j = txt.find(end)
        if j > 0:
            txt = txt[:j]
    print(txt)


def cmd_grep(name, pat, ctx=0):
    txt = to_text(load(name))
    lines = txt.split("\n")
    rx = re.compile(pat, re.I)
    hits = 0
    for i, ln in enumerate(lines):
        if rx.search(ln):
            hits += 1
            lo, hi = max(0, i - ctx), min(len(lines), i + ctx + 1)
            print("--- L%d ---" % (i + 1))
            for k in range(lo, hi):
                print(lines[k])
    print("[[%d hits]]" % hits)


if __name__ == "__main__":
    c = sys.argv[1]
    if c == "links":
        cmd_links(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
    elif c == "text":
        cmd_text(sys.argv[2],
                 sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] else None,
                 sys.argv[4] if len(sys.argv) > 4 and sys.argv[4] else None)
    elif c == "grep":
        cmd_grep(sys.argv[2], sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 0)
