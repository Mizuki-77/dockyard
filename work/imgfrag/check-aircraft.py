"""校验 work/imgfrag/img-aircraft.yaml —— 结构、文件存在、像素、subject、id 撞车。"""
import sys, os, re, json
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import yaml
from PIL import Image

ROOT = r"D:\deepseek harness\website-warships"
FRAG = os.path.join(ROOT, "work", "imgfrag", "img-aircraft.yaml")
MAIN = os.path.join(ROOT, "data", "images.yaml")

ALLOWED_SUBJECTS = {
    "swordfish", "fulmar", "sea-gladiator", "corsair", "avenger",
    "walrus", "seafox", "arado-196", "flycatcher", "fairy-iiif",
}
FIELDS = ["id", "file", "subject", "title", "part", "view", "date", "license",
          "license_tier", "license_raw", "author", "credit", "source_url",
          "width", "height", "primary", "note"]
THUMB_WIDTHS = {120, 250, 330, 500, 960, 1280, 1920, 3840}

fails, warns, ok = [], [], []


def fail(m):
    fails.append(m)


def warn(m):
    warns.append(m)


# ---------------------------------------------------------------- 1. 解析
with open(FRAG, encoding="utf-8") as f:
    raw = f.read()
try:
    doc = yaml.safe_load(raw)
    ok.append("YAML 可解析（safe_load 成功）")
except Exception as e:
    fail("YAML 解析失败：%s" % e)
    doc = None

if not isinstance(doc, dict):
    fail("顶层不是映射")
elif list(doc.keys()) != ["images"]:
    fail("顶层键应为 ['images']，实际 %r" % list(doc.keys()))
else:
    ok.append("顶层键唯一且为 images")

items = (doc or {}).get("images") or []
ok.append("条目数：%d" % len(items))

# 标题必须是块式：文本上不允许出现流式 `title: {`
stream = [i + 1 for i, ln in enumerate(raw.splitlines())
          if re.match(r"^\s*title:\s*[\{\[]", ln)]
if stream:
    fail("发现流式 title 映射，行号 %s" % stream)
else:
    ok.append("title 全部为块式（无 title: { ... } 流式写法）")

# ---------------------------------------------------------------- 2. data/images.yaml 现有 id
with open(MAIN, encoding="utf-8") as f:
    main_txt = f.read()
main_ids = set(re.findall(r"^\s*-\s*id:\s*(\S+)\s*$", main_txt, re.M))
main_urls = set(re.findall(r"source_url:\s*\"?([^\s\"']+)", main_txt))
ok.append("data/images.yaml 现有 id 数：%d" % len(main_ids))

frag_ids, frag_urls = set(), set()
seen_files = {}

# ---------------------------------------------------------------- 3. 逐条
for n, it in enumerate(items, 1):
    tag = "第 %d 条 (%s)" % (n, it.get("id", "?") if isinstance(it, dict) else "非映射")
    if not isinstance(it, dict):
        fail(tag + " 不是映射"); continue

    missing = [k for k in FIELDS if k not in it]
    extra = [k for k in it if k not in FIELDS]
    if missing:
        fail(tag + " 缺字段 %s" % missing)
    if extra:
        fail(tag + " 多出字段 %s" % extra)
    if it.get("id") in FIELDS or not isinstance(it.get("id"), str):
        fail(tag + " id 类型异常")

    # id 撞车
    iid = it.get("id")
    if iid in main_ids:
        fail(tag + " id 与 data/images.yaml 现有条目撞车")
    if iid in frag_ids:
        fail(tag + " id 在本分片内重复")
    frag_ids.add(iid)

    # subject
    sub = it.get("subject")
    m = re.fullmatch(r"weapon:([a-z0-9_-]+)", str(sub))
    if not m:
        fail(tag + " subject 不是 weapon:<id> 形式：%r" % sub)
    elif m.group(1) not in ALLOWED_SUBJECTS:
        fail(tag + " subject 的 id 不在 10 个型号清单内：%s" % m.group(1))

    # file 路径 + 存在 + 像素
    rel = it.get("file")
    if not isinstance(rel, str) or not rel.startswith("/img/weapons/"):
        fail(tag + " file 不是 /img/weapons/... ：%r" % rel); continue
    if not os.path.basename(rel).lower().startswith(m.group(1) if m else "?"):
        warn(tag + " 文件名前缀与 subject id 不一致：%s" % rel)
    if rel in seen_files:
        fail(tag + " file 与第 %d 条重复：%s" % (seen_files[rel], rel))
    seen_files[rel] = n

    abs_p = os.path.join(ROOT, "public", rel.lstrip("/").replace("/", os.sep))
    if not os.path.isfile(abs_p):
        fail(tag + " file 不存在于磁盘：%s" % abs_p); continue
    with Image.open(abs_p) as im:
        aw, ah = im.size
    if it.get("width") != aw or it.get("height") != ah:
        fail(tag + " 像素不符：记录 %sx%s，实测 %sx%s" % (it.get("width"), it.get("height"), aw, ah))

    # 缩略宽度必须在允许档位内（本站习惯 1280，源图小于 1280 时用原尺寸）
    if aw not in THUMB_WIDTHS and aw >= 120:
        warn(tag + " 宽度 %d px 不在缩略档位表内（源图小于 1280 时属正常）" % aw)

    # source_url 撞车
    u = it.get("source_url")
    if not isinstance(u, str) or not u.startswith("https://commons.wikimedia.org/wiki/File:"):
        fail(tag + " source_url 不是 Commons 文件页：%r" % u)
    if u in main_urls:
        fail(tag + " source_url 与 data/images.yaml 已有条目重复：%s" % u)
    if u in frag_urls:
        fail(tag + " source_url 在本分片内重复：%s" % u)
    frag_urls.add(u)

    # 授权
    tier = it.get("license_tier")
    lic = it.get("license")
    if tier not in ("A", "B", "C"):
        fail(tag + " license_tier 非 A/B/C：%r" % tier)
    if tier == "C":
        fail(tag + " 是 C 档（只能外链），不应进归档分片")
    if tier == "A" and lic not in ("pd", "cc0"):
        fail(tag + " A 档但 license=%r（应为 pd / cc0）" % lic)
    if tier == "B":
        if lic not in ("cc_by", "cc_by_sa"):
            fail(tag + " B 档但 license=%r" % lic)
        note = it.get("note") or ""
        for need in ("CC BY", "http", "1280 px", "未裁剪"):
            if need not in note and not (need == "1280 px" and str(aw) + " px" in note):
                fail(tag + " B 档 note 缺要素 %r" % need)

    # title 双语
    t = it.get("title")
    if not isinstance(t, dict) or not t.get("zh") or not t.get("en"):
        fail(tag + " title 缺 zh 或 en")
    if isinstance(t, dict) and set(t.keys()) - {"zh", "en"}:
        warn(tag + " title 有多余键 %s" % (set(t.keys()) - {"zh", "en"}))

    # date 形态
    d = str(it.get("date") or "")
    if not re.fullmatch(r"\d{4}(-\d{2})?(-\d{2})?(-\d{4}(-\d{2})?(-\d{2})?)?", d):
        fail(tag + " date 形态异常：%r" % d)

    if not isinstance(it.get("primary"), bool):
        fail(tag + " primary 不是布尔")

# ---------------------------------------------------------------- 4. 每型号覆盖
by_sub = {}
for it in items:
    by_sub.setdefault(it.get("subject"), []).append(it)
print("---- 每型号覆盖 ----")
for s in sorted(ALLOWED_SUBJECTS):
    lst = by_sub.get("weapon:" + s, [])
    prim = [x["id"] for x in lst if x.get("primary")]
    print("  %-14s %d 条  主图 %s" % (s, len(lst), prim or "无"))
    if not lst:
        fail("型号 %s 没有配图" % s)
    if len(lst) > 2:
        fail("型号 %s 超过 2 条（上限 2）" % s)
    if len([x for x in lst if x.get("primary")]) != 1:
        fail("型号 %s 的 primary 标记数应为 1，实际 %d" % (s, len(prim)))

print()
print("---- 汇总 ----")
for m in ok:
    print("  OK   " + m)
for m in warns:
    print("  WARN " + m)
for m in fails:
    print("  FAIL " + m)
print()
print("结果：%d 条记录，OK %d，WARN %d，FAIL %d" % (len(items), len(ok), len(warns), len(fails)))
print("PASS" if not fails else "NOT PASS")
