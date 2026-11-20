# 本机凭据与工具链自检
#
# 为什么要这个脚本：
#   推送依赖 `gh` 的 OAuth token，它存在 Windows 凭据管理器里。
#   token 本身不会过期，但可能因为重装系统 / 清空凭据管理器 / 换机器而消失，
#   而消失的那一刻没有任何提示 —— 只会等到下次 push 才发现。
#
# 用法（PowerShell）：
#   powershell -ExecutionPolicy Bypass -File scripts\check_auth.ps1
#
# 想让它每周自动跑一次，见 docs\40-p5-issues.md 末尾的「定时自检」一节。

$ErrorActionPreference = 'Continue'

# validate.py 输出是 UTF-8，但 PowerShell 默认按 GBK 解 Python 的 stdout，
# 结果中文全成乱码。强制两边都用 UTF-8。
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$env:PYTHONIOENCODING = 'utf-8'

$ok = $true
$notes = @()

Write-Host "=== Dockyard · 凭据与工具链自检 ===" -ForegroundColor Cyan
Write-Host ""

# ---------------------------------------------------------------- 1. git
$gitCandidates = @(
    'git',
    "$env:LOCALAPPDATA\Programs\Git\cmd\git.exe",
    'C:\Program Files\Git\cmd\git.exe',
    'C:\ProgramData\Lenovo\AIAgent\MCPEnv\PortableGit-2.55.0.2-64-bit\cmd\git.exe'
)

$git = $null
foreach ($c in $gitCandidates) {
    try {
        $v = & $c --version 2>$null
        if ($LASTEXITCODE -eq 0 -and $v -match 'git version') {
            $git = $c
            Write-Host "[ OK ] git          $v" -ForegroundColor Green
            if ($c -ne 'git') {
                $notes += "git 不在 PATH 上，当前用的是 $c"
            }
            break
        }
    } catch { }
}

if (-not $git) {
    Write-Host "[FAIL] git          找不到可用的 git" -ForegroundColor Red
    $ok = $false
}

# ---------------------------------------------------------------- 2. gh
$ghCandidates = @(
    'gh',
    "$env:LOCALAPPDATA\Programs\gh\gh.exe"
)

$gh = $null
foreach ($c in $ghCandidates) {
    try {
        $v = & $c --version 2>$null | Select-Object -First 1
        if ($LASTEXITCODE -eq 0 -and $v -match 'gh version') {
            $gh = $c
            Write-Host "[ OK ] gh           $v" -ForegroundColor Green
            break
        }
    } catch { }
}

if (-not $gh) {
    Write-Host "[FAIL] gh           未安装或不在 PATH 上" -ForegroundColor Red
    Write-Host "                    修复：从 https://github.com/cli/cli/releases 下载后解压到 %LOCALAPPDATA%\Programs\gh" -ForegroundColor Yellow
    $ok = $false
}

# ---------------------------------------------------------------- 3. 登录态
if ($gh) {
    $status = & $gh auth status 2>&1 | Out-String
    if ($LASTEXITCODE -eq 0 -and $status -match 'Logged in to github.com') {
        $user = ($status | Select-String -Pattern 'account (\S+)').Matches.Groups[1].Value
        Write-Host "[ OK ] 登录态       已登录为 $user" -ForegroundColor Green
    } else {
        Write-Host "[FAIL] 登录态       凭据失效或未登录" -ForegroundColor Red
        Write-Host "                    修复：gh auth login --web --scopes repo,workflow" -ForegroundColor Yellow
        $ok = $false
    }
}

# ---------------------------------------------------------------- 4. 远端可达
if ($gh -and $ok) {
    $reach = & $gh api repos/Mizuki-77/dockyard --jq '.full_name' 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[ OK ] 远端仓库      $reach 可达" -ForegroundColor Green
    } else {
        Write-Host "[WARN] 远端仓库      访问失败（可能是网络/代理问题，不是凭据问题）" -ForegroundColor Yellow
        $notes += "远端不可达，检查网络或代理"
    }
}

# ---------------------------------------------------------------- 5. 本地仓库状态
if ($git) {
    Push-Location (Split-Path $PSScriptRoot -Parent)
    try {
        $branch = & $git rev-parse --abbrev-ref HEAD 2>$null
        $dirty = & $git status --porcelain 2>$null
        if ($dirty) {
            $n = ($dirty | Measure-Object).Count
            Write-Host "[WARN] 本地仓库      $n 个文件未提交" -ForegroundColor Yellow
        } else {
            Write-Host "[ OK ] 本地仓库      分支 $branch 干净" -ForegroundColor Green
        }

        $remote = & $git remote get-url origin 2>$null
        if ($remote) {
            Write-Host "[ OK ] remote        $remote" -ForegroundColor Green
        }
    } finally {
        Pop-Location
    }
}

# ---------------------------------------------------------------- 6. 数据层
Write-Host ""
Write-Host "=== 数据层校验 ===" -ForegroundColor Cyan
Push-Location (Split-Path $PSScriptRoot -Parent)
try {
    $out = python scripts/validate.py 2>&1 | Out-String
    if ($out -match '0 错误' -or $LASTEXITCODE -eq 0) {
        Write-Host "[ OK ] validate      $($out.Trim().Split("`n")[-1])" -ForegroundColor Green
    } else {
        Write-Host "[FAIL] validate      数据层校验未通过" -ForegroundColor Red
        $ok = $false
    }
} finally {
    Pop-Location
}

# ---------------------------------------------------------------- 汇总
Write-Host ""
if ($ok) {
    Write-Host "结论：一切正常，可以正常推送。" -ForegroundColor Green
} else {
    Write-Host "结论：有项目需要处理，见上面的 [FAIL] 行。" -ForegroundColor Red
}

if ($notes.Count -gt 0) {
    Write-Host ""
    Write-Host "备注：" -ForegroundColor Gray
    foreach ($n in $notes) { Write-Host "  · $n" -ForegroundColor Gray }
}

exit $(if ($ok) { 0 } else { 1 })
