# -*- coding: utf-8 -*-
"""HTML -> readable plain text. Usage: python totext.py <rawname>"""
import sys, os, re, html

RAW = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_raw")

def strip(p):
    s = open(p, encoding="utf-8", errors="replace").read()
    s = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", s)
    s = re.sub(r"(?is)<!--.*?-->", " ", s)
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</(p|div|tr|h[1-6]|li|table)>", "\n", s)
    s = re.sub(r"(?i)</t[dh]>", " | ", s)
    s = re.sub(r"(?i)<td[^>]*>", " | ", s)
    s = re.sub(r"(?s)<[^>]+>", "", s)
    s = html.unescape(s)
    s = s.replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s.strip()

name = sys.argv[1]
src = os.path.join(RAW, name + ".html")
out = os.path.join(RAW, name + ".txt")
t = strip(src)
open(out, "w", encoding="utf-8").write(t)
print("wrote %s (%d chars)" % (out, len(t)))
