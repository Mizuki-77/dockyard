"""按 URL 列表抓 navweaps 页面并存进 work/navweaps/（.php 原文 + .txt 纯文本）。

用法：python work/navweaps/fetch.py <url> [<url> ...]
国内必须走 127.0.0.1:7897 代理。
"""
import html
import pathlib
import re
import sys
import urllib.request

PROXY = "http://127.0.0.1:7897"
OUT = pathlib.Path(__file__).parent


def strip_html(s: str) -> str:
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</(p|div|tr|li|h[1-6]|table)>", "\n", s)
    s = re.sub(r"(?i)</t[dh]>", " | ", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\u00a0]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s.strip()


def main(urls):
    op = urllib.request.build_opener(
        urllib.request.ProxyHandler({"http": PROXY, "https": PROXY})
    )
    for u in urls:
        name = u.rsplit("/", 1)[-1]
        try:
            req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
            raw = op.open(req, timeout=60).read()
        except Exception as e:  # noqa: BLE001
            print("FAIL", type(e).__name__, e, u)
            continue
        txt = raw.decode("utf-8", "replace")
        (OUT / name).write_text(txt, encoding="utf-8")
        plain = strip_html(txt)
        (OUT / (name.rsplit(".", 1)[0] + ".txt")).write_text(plain, encoding="utf-8")
        print("OK", len(raw), len(plain), name)


if __name__ == "__main__":
    main(sys.argv[1:])
