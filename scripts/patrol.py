#!/usr/bin/env python3
"""Dockyard 仓库只读巡检。

检查五件事，然后（可选）把结果推一条微信提醒。

  1. 未提交改动        git status --short 非空
  2. 未推送提交        本地 HEAD 与远端 main 的 sha 不一致
  3. 根目录杂物        白名单以外的文件出现在仓库根目录
  4. 数据层校验        scripts/validate.py 的结尾汇总
  5. 推送凭据          gh auth status 是否仍然有效

安全性：本脚本**绝不**修改仓库。不 add、不 commit、不 push、不 fetch
（fetch 要写 .git，在只读权限下会失败，所以远端 sha 直接查 GitHub API）。

推送：读 `~/.dsh/secrets/maid.json` 里的服务器凭据，往 maid 服务器的
reminders.json 追加一条一次性提醒，由服务器上的 maid 服务发到微信。
凭据不在本文件里，也不在仓库里。

用法：
    python scripts/patrol.py            # 检查 + 推送
    python scripts/patrol.py --no-push  # 只检查
"""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# 联想的 PortableGit 不在 PATH 里，必须用绝对路径。换机器/联想升级目录后
# 这里要跟着改，脚本会明确报出「找不到 git」而不是假装一切正常。
GIT_CANDIDATES = [
    r"C:\ProgramData\Lenovo\AIAgent\MCPEnv\PortableGit-2.55.0.2-64-bit\cmd\git.exe",
    r"C:\Program Files\Git\cmd\git.exe",
]

# 仓库根目录允许出现的文件。之外的一律当杂物报告。
ROOT_WHITELIST = {
    ".gitattributes", ".gitignore", "LICENSE", "README.md",
    "astro.config.mjs", "package-lock.json", "package.json",
    "requirements.txt", "tsconfig.json", "wrangler.toml",
}

# 交接报告每轮都会重新生成一份、放在根目录，好让下一轮直接找到。
# 不写死具体日期（文件名带日期），用前缀匹配。
_ROSTER_PREFIXES = ("项目交接-",)


def _is_roster(name: str) -> bool:
    return any(name.startswith(p) for p in _ROSTER_PREFIXES)

SECRETS = Path.home() / ".dsh" / "secrets" / "maid.json"


def find_git() -> str | None:
    for p in GIT_CANDIDATES:
        if os.path.isfile(p):
            return p
    return None


def git(git_exe: str, *args: str) -> str:
    r = subprocess.run(
        [git_exe, "-C", str(REPO), *args],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    # 只清尾部换行，不能用 strip()：`git status --short` 的首行以空格开头
    # （" M file"），strip 掉之后按 line[3:] 取路径会吃掉文件名第一个字符。
    return r.stdout.rstrip()


def check_worktree(git_exe: str) -> list[str]:
    out = git(git_exe, "status", "--short")
    if not out:
        return []
    return [line for line in out.splitlines() if line.strip()]


def check_unpushed(git_exe: str, repo_slug: str) -> tuple[str, str]:
    """返回 (本地 sha, 远端 sha)。任何一边取不到就给空串。

    远端 sha 优先用 `git ls-remote` —— 直接问 git 服务器，不写本地 .git，
    只读权限下也能跑。GitHub 的 REST API 有 CDN 缓存，刚 push 完立刻查
    会拿到旧 sha，造成「明明推了却报未推送」的误报（2026-11-25 实测）。
    API 只作为 ls-remote 失败时的兜底。
    """
    local = git(git_exe, "rev-parse", "HEAD")
    remote = ""
    out = git(git_exe, "ls-remote", "origin", "refs/heads/main")
    if out:
        remote = out.split()[0].strip()
    if not remote:
        try:
            url = f"https://api.github.com/repos/{repo_slug}/commits/main"
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "dockyard-patrol", "Cache-Control": "no-cache"},
            )
            with urllib.request.urlopen(req, timeout=20) as resp:
                remote = json.load(resp).get("sha", "")
        except Exception:
            remote = ""
    return local, remote


def check_root_clutter() -> list[str]:
    clutter = []
    for entry in REPO.iterdir():
        if entry.name == ".git" or entry.is_dir():
            continue
        if entry.name in ROOT_WHITELIST or _is_roster(entry.name):
            continue
        clutter.append(entry.name)
    return sorted(clutter)


def check_data_layer() -> tuple[bool, str]:
    py = sys.executable
    # validate.py 的中文会按控制台编码输出，这里强推 UTF-8，否则拿到的是乱码。
    env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}
    try:
        r = subprocess.run(
            [py, str(REPO / "scripts" / "validate.py")],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
            cwd=str(REPO), env=env,
        )
    except Exception as e:  # noqa: BLE001
        return False, f"跑不起来（{e}）"
    tail = [ln.strip() for ln in (r.stdout or "").splitlines() if ln.strip()]
    summary = tail[-1] if tail else "(无输出)"
    return r.returncode == 0, summary


def check_credentials() -> tuple[bool, str]:
    """gh 凭据是否还能推送。失效时不会有任何提示，只会等到某天 push 才报错。"""
    try:
        r = subprocess.run(
            ["gh", "auth", "status"],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
            timeout=25,
        )
    except FileNotFoundError:
        return False, "⚠️ 找不到 gh（不在 PATH）"
    except Exception as e:  # noqa: BLE001
        return False, f"检查失败（{e}）"
    return r.returncode == 0, "有效" if r.returncode == 0 else "❌ 失效，需要重新 gh auth login"


def build_report(rows: list[str]) -> str:
    return "\n".join(rows)


def push_wechat(text: str, minutes_ahead: int = 3) -> str:
    """往 maid 服务器塞一条一次性提醒。返回一句结果说明。"""
    if not SECRETS.is_file():
        return f"⚠️ 微信未推送：缺凭据文件 {SECRETS}"
    try:
        cfg = json.loads(SECRETS.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return f"⚠️ 微信未推送：凭据读不出（{e}）"

    host = cfg.get("host", "")
    user = cfg.get("user", "root")
    password = cfg.get("password", "")
    if not (host and password):
        return "⚠️ 微信未推送：maid.json 里缺 host / password"

    try:
        import paramiko  # noqa: PLC0415
    except ImportError:
        return "⚠️ 微信未推送：本机缺 paramiko（pip install paramiko）"

    now = dt.datetime.now()
    fire_at = (now + dt.timedelta(minutes=minutes_ahead)).replace(microsecond=0)
    rid = f"dockyard-patrol-{now:%Y%m%d}"

    payload = {
        "id": rid,
        "at": fire_at.isoformat(),
        "text": text,
        "done": False,
    }
    remote_code = (
        "import json,sys\n"
        "p='/root/maid/reminders.json'\n"
        "item=json.loads(sys.stdin.read())\n"
        "d=json.load(open(p))\n"
        "d=[x for x in d if x.get('id')!=item['id']]\n"
        "d.append(item)\n"
        "json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)\n"
        "print('ok',len(d))\n"
    )
    b64 = base64.b64encode(remote_code.encode()).decode()
    stdin_blob = json.dumps(payload, ensure_ascii=False)

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(host, username=user, password=password, timeout=15)
        cmd = (
            f"python3 -c \"import base64;exec(base64.b64decode('{b64}').decode())\""
            f" <<'__ITEM__'\n{stdin_blob}\n__ITEM__"
        )
        _, out, err = client.exec_command(cmd, timeout=25)
        stdout = out.read().decode("utf-8", "replace").strip()
        stderr = err.read().decode("utf-8", "replace").strip()
        if stdout.startswith("ok"):
            return f"✅ 已排队，{fire_at:%H:%M} 由小月发到微信"
        return f"⚠️ 微信未推送：服务器返回 {stderr or stdout or '(空)'}"
    except Exception as e:  # noqa: BLE001
        return f"⚠️ 微信未推送：连不上 maid 服务器（{e}）"
    finally:
        client.close()


def main() -> int:
    # Windows 控制台默认 GBK，报告里带 emoji 会直接抛 UnicodeEncodeError。
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass

    ap = argparse.ArgumentParser()
    ap.add_argument("--no-push", action="store_true", help="只检查，不发微信")
    ap.add_argument("--repo-slug", default="Mizuki-77/dockyard")
    args = ap.parse_args()

    today = dt.datetime.now()
    rows = [f"【Dockyard 巡检 {today:%Y-%m-%d}】"]

    git_exe = find_git()
    if not git_exe:
        rows.append("git：⚠️ 找不到 PortableGit，本地三项检查跳过")
        local = remote = ""
        dirty: list[str] = []
    else:
        rows.append(f"git：{git_exe}")
        dirty = check_worktree(git_exe)
        local, remote = check_unpushed(git_exe, args.repo_slug)

    # 未提交
    if git_exe:
        if dirty:
            names = "、".join(line[3:].strip() for line in dirty[:5])
            more = f" 等 {len(dirty)} 个" if len(dirty) > 5 else f"（{len(dirty)} 个）"
            rows.append(f"未提交：{names}{more}")
        else:
            rows.append("未提交：无")

    # 未推送
    if git_exe:
        if not remote:
            rows.append("未推送：⚠️ 取不到远端 sha（检查网络）")
        elif local == remote:
            rows.append("未推送：无")
        else:
            head = git(git_exe, "log", "-1", "--oneline").strip()
            rows.append(f"未推送：本地 {local[:7]} ≠ 远端 {remote[:7]}（{head}）")

    clutter = check_root_clutter()
    rows.append(f"根目录：{'多了 ' + '、'.join(clutter) if clutter else '干净'}")

    ok, summary = check_data_layer()
    rows.append(f"数据层：{summary}" if ok else f"数据层：❌ {summary}")

    cred_ok, cred_msg = check_credentials()
    rows.append(f"凭据：{cred_msg}")

    # 结论
    problems = []
    if git_exe and dirty:
        problems.append("有未提交改动")
    if git_exe and remote and local != remote:
        problems.append("有未推送提交")
    if clutter:
        problems.append("根目录有杂物")
    if not ok:
        problems.append("数据层校验没过")
    if not cred_ok:
        problems.append("推送凭据失效")
    rows.append(f"结论：{'需要处理 —— ' + '，'.join(problems) if problems else '干净，可以不管'}")

    report = build_report(rows)

    if not args.no_push:
        # 干净的日子只发一句话，别每周报喜占屏。
        text = report if problems else (
            f"【Dockyard 巡检 {today:%Y-%m-%d}】\n干净，可以不管。\n"
            f"未提交无 · 未推送无 · 根目录干净 · 数据层通过 · 凭据有效"
        )
        rows.append("")
        rows.append(push_wechat(text))

    print(build_report(rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())
