# -*- coding: utf-8 -*-
"""Fetch a list of name=url pairs with polite delay and retry."""
import sys, os, ssl, time, urllib.request, urllib.error

OWN = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(OWN, "_raw")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get(name, url, tries=3):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    })
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=60, context=ctx) as r:
                data = r.read()
                with open(os.path.join(OUT, name + ".html"), "wb") as f:
                    f.write(data)
                enc = "utf-8"
                head = data[:4000].decode("latin-1", "ignore").lower()
                if "charset=iso-8859-1" in head:
                    enc = "latin-1"
                with open(os.path.join(OUT, name + ".txt"), "w", encoding="utf-8") as f:
                    f.write(data.decode(enc, "replace"))
                print("%-32s %s %7d  %s" % (name, r.status, len(data), url))
                return True
        except urllib.error.HTTPError as e:
            print("%-32s HTTP %s  %s" % (name, e.code, url))
            return False
        except Exception as e:
            if i == tries - 1:
                print("%-32s FAIL %s (%s)" % (name, type(e).__name__, url))
                return False
            time.sleep(4)
    return False


if __name__ == "__main__":
    for a in sys.argv[1:]:
        n, _, u = a.partition("=")
        get(n, u)
        time.sleep(1.5)
