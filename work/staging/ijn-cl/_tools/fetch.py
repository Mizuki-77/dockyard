# -*- coding: utf-8 -*-
"""Fetch raw pages into _raw/ with UA + charset detection. Usage: python fetch.py <outname> <url>"""
import sys, os, re, urllib.request, gzip, time

RAW = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_raw")

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")


def fetch(url, timeout=60):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,ja;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "close",
    })
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read()
        enc = r.headers.get("Content-Encoding", "")
        if "gzip" in enc:
            data = gzip.decompress(data)
        return r.status, r.headers.get("Content-Type", ""), data


def charset_from(raw_bytes, http_ctype):
    m = re.search(r"charset=([\w\-]+)", http_ctype or "", re.I)
    if m:
        return m.group(1).lower()
    head = raw_bytes[:4096].decode("ascii", "ignore")
    m = re.search(r'charset=["\']?([\w\-]+)', head, re.I)
    if m:
        return m.group(1).lower()
    return None


def guess_decode(b, cs):
    cands = []
    if cs:
        if cs in ("shift_jis", "sjis", "x-sjis", "cp932", "windows-31j"):
            cands = ["cp932", "shift_jis"]
        elif cs in ("euc-jp", "euc_jp"):
            cands = ["euc_jp"]
        else:
            cands = [cs]
    cands += ["utf-8", "cp932", "euc_jp", "cp1252", "latin-1"]
    for c in cands:
        try:
            return b.decode(c), c
        except (UnicodeDecodeError, LookupError):
            continue
    return b.decode("latin-1", "replace"), "latin-1"


if __name__ == "__main__":
    name, url = sys.argv[1], sys.argv[2]
    t0 = time.time()
    try:
        status, ctype, data = fetch(url)
    except Exception as e:
        print("FAIL %s -> %s: %s" % (name, url, e))
        sys.exit(2)
    ext = ".pdf" if ("pdf" in ctype.lower() or url.lower().endswith(".pdf")) else ".html"
    out = os.path.join(RAW, name + ext)
    if ext == ".pdf":
        open(out, "wb").write(data)
        print("OK   %-32s %s %8d bytes %.1fs  (pdf)" % (name, status, len(data), time.time() - t0))
        sys.exit(0)
    txt, used = guess_decode(data, charset_from(data, ctype))
    open(out, "w", encoding="utf-8").write(
        "<!-- decoded with %s ; fetched %s -->\n" % (used, url) + txt)
    t = re.search(r"(?is)<title>(.*?)</title>", txt)
    title = re.sub(r"\s+", " ", t.group(1)).strip()[:90] if t else ""
    print("OK   %-32s %s %6d bytes %.1fs enc=%s title=%s" % (name, status, len(data), time.time() - t0, used, title))
