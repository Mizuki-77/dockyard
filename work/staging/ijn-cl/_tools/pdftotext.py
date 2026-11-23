# -*- coding: utf-8 -*-
"""Extract text from a PDF in _raw. Usage: python pdftotext.py <rawname>"""
import sys, os
import pymupdf

RAW = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_raw")

name = sys.argv[1]
src = os.path.join(RAW, name + ".pdf")
out = os.path.join(RAW, name + ".txt")
doc = pymupdf.open(src)
parts = []
for i, page in enumerate(doc):
    parts.append("\n===== page %d =====\n" % (i + 1))
    parts.append(page.get_text())
t = "".join(parts)
open(out, "w", encoding="utf-8").write(t)
print("wrote %s (%d pages, %d chars)" % (out, len(doc), len(t)))
