# -*- coding: utf-8 -*-
"""Fetch raw pages for tg172 research. Usage: python _fetch.py [name=url ...]"""
import sys, os, json, ssl, urllib.request, urllib.error

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_raw")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

TARGETS = [
    ("navweaps-8in55-mk9", "https://www.navweaps.com/Weapons/WNUS_8-55_mk9.php"),
    ("navweaps-5in25-mk10", "https://www.navweaps.com/Weapons/WNUS_5-25_mk10.php"),
    ("navweaps-11in75", "https://www.navweaps.com/Weapons/WNUS_1-1-75.php"),
    ("navweaps-20mm", "https://www.navweaps.com/Weapons/WNUS_20mm_AA.php"),
    ("navweaps-us-index", "https://www.navweaps.com/Weapons/index_weapons.php"),
    ("navweaps-radar-us", "https://www.navweaps.com/Weapons/WN_Radar.php"),
    ("ibiblio-ca-index", "https://www.ibiblio.org/hyperwar/USN/ships/ships-ca.html"),
    ("ibiblio-danfs-index", "https://www.ibiblio.org/hyperwar/USN/ships/"),
    ("navsource-astoria", "http://www.navsource.org/archives/04/034/04034.htm"),
    ("navsource-portland", "http://www.navsource.org/archives/04/033/04033.htm"),
    ("navypedia-neworleans", "https://www.navypedia.org/ships/usa/us_cr_new_orleans.htm"),
    ("navypedia-portland", "https://www.navypedia.org/ships/usa/us_cr_portland.htm"),
    ("navypedia-usa-index", "https://www.navypedia.org/ships/usa/usa_cr.htm"),
]


def fetch(name, url):
    path = os.path.join(OUT, name + ".html")
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    })
    try:
        with urllib.request.urlopen(req, timeout=45, context=ctx) as r:
            data = r.read()
            code = r.status
    except urllib.error.HTTPError as e:
        print("%-24s HTTP %s  %s" % (name, e.code, url))
        return None
    except Exception as e:
        print("%-24s FAIL %s  (%s)" % (name, e, url))
        return None
    with open(path, "wb") as f:
        f.write(data)
    # try decode guess
    enc = "utf-8"
    head = data[:4000].decode("latin-1", "ignore").lower()
    if "charset=shift_jis" in head or "charset=shift-jis" in head:
        enc = "shift_jis"
    elif "charset=euc-jp" in head:
        enc = "euc-jp"
    elif "charset=iso-8859-1" in head:
        enc = "latin-1"
    txt = data.decode(enc, "replace")
    with open(os.path.join(OUT, name + ".txt"), "w", encoding="utf-8") as f:
        f.write(txt)
    print("%-24s %s  %7d bytes  %s" % (name, code, len(data), url))
    return txt


if __name__ == "__main__":
    if len(sys.argv) > 1:
        todo = []
        for a in sys.argv[1:]:
            n, _, u = a.partition("=")
            todo.append((n, u))
    else:
        todo = TARGETS
    for n, u in todo:
        fetch(n, u)
