# 负向测试：确认 check_operation_links 真能抓到双向引用不一致。
# 做法是临时改坏数据 → 跑校验器 → 断言报出对应错 → 复原。
# 注意必须用 Python 读写（PowerShell 的 Set-Content 会破坏 YAML 缩进/编码）。
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BATTLE = ROOT / "data" / "battles" / "denmark-strait.yaml"
OP = ROOT / "data" / "operations" / "rheinubung.yaml"


def run():
    env = {"PYTHONIOENCODING": "utf-8", "PATH": __import__("os").environ["PATH"]}
    r = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate.py"), "--json"],
        capture_output=True, text=True, encoding="utf-8", cwd=str(ROOT), env=env,
    )
    import json
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        print("校验器输出不是 JSON：", r.stdout[:400], r.stderr[:400])
        return {"errors": [], "warnings": []}


def expect(label, errors, warnings, needle):
    hits = [e for e in errors + warnings if needle in str(e)]
    status = "OK  " if hits else "FAIL"
    print(f"{status} {label}")
    if not hits:
        print(f"     期望含 {needle!r}，实际：")
        for e in (errors + warnings)[:6]:
            print("       -", str(e)[:140])
    return bool(hits)


ok = True
shutil.copy2(BATTLE, BATTLE.with_suffix(".yaml.bak"))
shutil.copy2(OP, OP.with_suffix(".yaml.bak"))
try:
    # 用例 1：战斗文件写了不存在的系列 id
    txt = BATTLE.read_text(encoding="utf-8").replace(
        "operation: rheinubung", "operation: nonexistent-op"
    )
    BATTLE.write_text(txt, encoding="utf-8")
    d = run()
    ok &= expect("战斗引用不存在的系列 → 报错", d["errors"], d["warnings"], "nonexistent-op")

    # 复原
    shutil.copy2(BATTLE.with_suffix(".yaml.bak"), BATTLE)

    # 用例 2：系列里删掉 battle 指向，但战斗文件仍写 operation
    # 注意 battle 与列表短横线在同一行（"  - battle: denmark-strait"），
    # 所以要把 "- " 也替换掉，否则会留下一个孤立的 "  - " 导致 YAML 解析失败。
    txt = OP.read_text(encoding="utf-8").replace(
        "  - battle: denmark-strait\n    label:", "  - label:"
    )
    OP.write_text(txt, encoding="utf-8")
    d = run()
    ok &= expect("系列不再收录、战斗仍反向引用 → 报错", d["errors"], d["warnings"], "phases 里没有")

    # 复原
    shutil.copy2(OP.with_suffix(".yaml.bak"), OP)

    # 用例 3：phase 指向不存在的战斗
    txt = OP.read_text(encoding="utf-8").replace(
        "battle: denmark-strait", "battle: ghost-battle"
    )
    OP.write_text(txt, encoding="utf-8")
    d = run()
    ok &= expect("phase 指向不存在的战役 → 报错", d["errors"], d["warnings"], "ghost-battle")

    # 复原
    shutil.copy2(OP.with_suffix(".yaml.bak"), OP)

    # 收尾：确认复原后是干净的
    d = run()
    clean = not d["errors"] and not d["warnings"]
    print(("OK  " if clean else "FAIL") + " 复原后应无错误无警告")
    ok &= clean
finally:
    for p in (BATTLE, OP):
        bak = p.with_suffix(".yaml.bak")
        if bak.exists():
            shutil.copy2(bak, p)
            bak.unlink()

print()
print("全部通过" if ok else "有用例失败")
sys.exit(0 if ok else 1)
