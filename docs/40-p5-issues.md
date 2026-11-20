# P5 · 纠错入口与版本控制

> 2026-11-20 起 · 对应交接报告 §9.1 技术债第 1 条、§9.3 路线图 P5
> 状态：**git + GitHub 仓库已就绪；纠错入口已接在战舰详情页**；武器/战役/舰级页待接。

---

## 1. 仓库

| 项 | 值 |
|---|---|
| 地址 | **https://github.com/Mizuki-77/dockyard** |
| 可见性 | Public |
| 默认分支 | `main` |
| 首次提交 | `b5056ed` 初始化仓库：Dockyard 首次纳入版本控制 |
| 规模 | 606 文件 / 63.1 MB |
| Issues | 已开启（P5 投稿的落地处） |
| topics | warships · ww2 · naval-history · astro · yaml · digital-humanities |

### 1.1 纳入了什么

原则：**入库的是「重建站点所必需」与「可读的调研报告」**；抓下来的原始 HTML/PDF/截图是原料，留在磁盘上但不进 git。

| 范围 | 大小 | 说明 |
|---|---|---|
| `data/` | 1.7 MB | 内容主体：字段注册表 / 来源表 / 图库 / 12 舰 + 8 级 + 60 武器 + 3 战役 + 2 行动 / 切片 / 正文 |
| `public/img/` | 58.6 MB | 270 张已核过授权的图 |
| `src/` | 0.4 MB | 渲染层 |
| `scripts/` | 0.1 MB | validate / selftest / test_operation_links |
| `docs/` | 0.1 MB | 框架推导、部署、对比器、新舰方法论、中途岛进度 |
| `work/*.md` `work/*.py` | 1.5 MB | 调研报告与可复用脚本 |
| `work/raw/ktb/bs-ktb.txt` | 0.4 MB | **唯一例外**，`sources.yaml:347` 的 `local_copy` 指向它 |

### 1.2 排除了什么

`node_modules/`(346 MB) · `dist/`(64 MB) · `_tmp/`(15 MB) · `*.bak`(11 个) ·
`work/` 下的原始 PDF(52.7 MB) / HTML(34 MB) / 截图(24 MB)

⚠️ **磁盘上什么都没删。** 交接报告 §9.1 第 7 条说「`work/` 不能删」，那说的是别从磁盘删。
这些原料仍然在本地，只是没有版本控制——体积大、可再生、git 里存一份也没人看。

### 1.3 换行符策略（踩过的坑）

`.gitattributes` 里设了 `* -text`，**关闭一切 CRLF↔LF 转换**。

原因：本项目原文件的换行符本来就是混的。实测 **纯 LF 272 个 / 纯 CRLF 63 个 / 混合 12 个**。
如果开 `core.autocrlf=true`，那 63 个 CRLF 文件（不少是 `data/ships/*.yaml`）
会永远显示为 modified，每天几百条假 diff。

---

## 2. 本机的 git / gh 情况（这一节最容易被后人踩）

### 2.1 情况

| 项 | 实际状态 |
|---|---|
| 系统 git | **没装**。`where git` 空的，`C:\Program Files\Git` 不存在 |
| 实际用的 git | `C:\ProgramData\Lenovo\AIAgent\MCPEnv\PortableGit-2.55.0.2-64-bit\cmd\git.exe` |
| gh CLI | `%LOCALAPPDATA%\Programs\gh\gh.exe`（2.105.0），已加进用户 PATH |
| 代理 | **HTTP 端口 12450**（见下） |

**联想便携版是临时方案。** 它在 Lenovo AI Agent 的私有目录里，重装或升级联想软件可能被删，
且不在 PATH 上。**建议装一个独立 git**，装完把 `scripts/check_auth.ps1` 里
`$gitCandidates` 的第一项就能命中，不需要改代码。

### 2.2 代理端口 —— 交接报告写错了

交接报告 §10.3 与 §10.2 都写「代理 `http://127.0.0.1:7897`」。**实际不是。**

2026-11-20 实测：SakuraCat 现在跑的是 sing-box，监听两个口：

| 端口 | 协议 | 说明 |
|---|---|---|
| **12450** | HTTP | 给 git / gh / Invoke-WebRequest 用 |
| 12440 | SOCKS | 不能用 `-Proxy` 直接指定 |
| 7897 | — | **没开** |

**但更重要的是：直连 GitHub 就能通，不需要配代理。**
`git ls-remote`、`gh api` 在不设 `HTTPS_PROXY` 的情况下都正常。
所以仓库里**故意没有** `http.proxy` 配置 —— 配了反而会在代理关闭时全线失败（踩过）。

需要强制走代理时才临时加：
```powershell
$env:HTTPS_PROXY='http://127.0.0.1:12450'
```

### 2.3 凭据

| 项 | 值 |
|---|---|
| 存储位置 | Windows 凭据管理器（keyring） |
| 账号 | `Mizuki-77` |
| 类型 | `gho_` OAuth token（**不会自动过期**） |
| scopes | `repo` · `workflow` · `read:org` · `gist` |
| credential helper | 仓库级只留一个：`!gh auth git-credential` |

⚠️ **踩过的坑：联想便携版的系统级 `credential.helper=helper-selector` 会弹窗**
（`CredentialHelperSelector`，选项是 `<no helper>` / `wincred` / `manager`）。
推送**不受影响**（弹窗前就已经推完了），但每次都要点一下很烦。

已经这样处理：仓库级 `credential.helper` 只保留 gh 那一个。系统级那份没动过
（那是联想的，改了会影响其他项目）。实测 `git fetch` 不再弹窗。

---

## 3. 凭据失效风险的处理

### 3.1 真实风险是什么

**不是「到期」。** `gho_` token 是长期的，不手动 revoke 就一直有效。
`gh auth status` 和 `hosts.yml` 里都没有过期时间字段。

**真实风险是失效**：重装系统 / 清空 Windows 凭据管理器 / 换机器 / 手动 revoke。
失效的那一刻**没有任何提示**，只会等到某天 push 时才报错——而那时你可能已经改了几十个文件。

### 3.2 两道保险

**第一道：本机自检脚本**

```powershell
powershell -ExecutionPolicy Bypass -File scripts\check_auth.ps1
```

查 6 项：git 可用 / gh 可用 / 登录态 / 远端可达 / 本地仓库状态 / validate.py。
分 `[ OK ]` / `[WARN]` / `[FAIL]` 三级，`[FAIL]` 会给出修复命令，以 exit code 表示结果。

> 脚本里有一处必须注意：`$OutputEncoding` 和 `[Console]::OutputEncoding` 都设成 UTF-8。
> 否则 Python 的 UTF-8 stdout 被按 GBK 解，中文全变乱码。

**第二道：每周自动跑**

| 项 | 值 |
|---|---|
| 名称 | Dockyard · 每周凭据与数据健康自检 |
| 时间 | 每周一 09:00（Asia/Shanghai） |
| 模式 | 每次新开会话；只读权限 |
| ID | `automation_dc62b0af-b048-4302-820c-a3baf7a95e8d` |

它的输出分两类：**阻塞项**（凭据掉了 / git 找不到 / validate 不过）
与**非阻塞**（网络不通、有未提交文件）。凭据掉了会直接给修复命令。

管理：设置里关掉，或让我改。

**第三道：GitHub 侧的 workflow**

`.github/workflows/health.yml` 每周一 01:00 UTC 跑 `validate.py` + `selftest.py`。
这一道**不查本机凭据**（GitHub 的服务器上看不到你的电脑），查的是数据层本身有没有坏。
它和本机自检互补：本机挂了它照跑，数据坏了它在网页上有红叉。

### 3.3 凭据真的掉了怎么办

```powershell
gh auth login --web --scopes repo,workflow
```

会给你一个一次性码（形如 `XXXX-XXXX`），去 https://github.com/login/device 输入。

**踩过的坑**：这个码 **15 分钟就过期**，而且必须当场操作。前两次都因为没及时输而超时。
浏览器里 `Authorize` 按钮点不动的典型原因是**窗口太窄，按钮被挤到可视区外**——
按 `Ctrl` + `-` 缩到 80% 就能点。

---

## 4. 纠错入口（P5 主体）

### 4.1 做了什么

`docs/00-framework.md` §6.1 的设计：

```
读者发现错误
  → 点数据点旁的 ⚠ 标记
  → 自动带出：舰船 id、字段 id、当前值、当前来源、页面 URL
  → 跳转 GitHub Issue（模板预填）
  → 审核：采纳 → 改 YAML 并关单；驳回 → 说明理由留档
```

**核心不是「有个反馈入口」，是「每个数据点都有自己的入口」。**
全站一个「联系我们」会让人写「你们俾斯麦的数据好像有点问题」；
带上字段和当前值，他写的是「NavWeaps 那页是 35,550 m，你们写的是 36,520」——
后者能直接变成一条新的 fact。

### 4.2 涉及的文件

| 文件 | 作用 |
|---|---|
| `src/lib/site.ts` | **新建**。`REPO_URL` 常量 + `issueUrl()` 拼 URL |
| `src/components/ReportIssue.astro` | **新建**。⚠ 按钮，纯 `<a>`，无 JS |
| `src/pages/ships/[id].astro` | 详细参数区每行接一个按钮 |
| `.github/ISSUE_TEMPLATE/correction.yml` | issue 表单模板 |
| `src/pages/help.astro` | 状态说明从「还在做」改成「已覆盖战舰页」 |

### 4.3 三个非显然的决定

**① 用 `<a>` 不用 JS。**
静态站无后端，GitHub issue 本身就是存储与审核队列。用链接的好处：中键能新开标签、
能右键复制、禁用 JS 也能用、不占首屏 JS 预算。

**② issue form 会忽略 URL 里的 `body` 参数。**
这是实测出来的。`correction.yml` 是 issue **form**（带 `body:` 字段列表），
它只认「和表单字段 id 同名」的查询参数（`entity` / `page` / `claim`），
传一大段 markdown 到 `body` 会被静默丢弃。
若哪天换回 markdown 模板（`.md`），则要改回 `body` 参数。
**这条写进 `src/lib/site.ts` 的注释了，别再踩。**

**③ 桌面上默认隐藏 ⚠，hover 才浮现。**
1703 条 fact 如果每个都常驻一个警告图标，整页会像一堆报错。
用 `@media (hover: hover) and (pointer: fine)` 只对鼠标设备隐藏；
触屏没有 hover，保持常显（`opacity: .55`）。

### 4.4 验证结果

```
build: 97 页通过
akagi 页: 69 个纠错链接（详细参数区全部字段）
链接参数实测:
  template=correction.yml
  title=[纠错] 赤城 · 建造计划
  entity=赤城（akagi）
  page=https://archive.dockyard.workers.dev/ships/akagi/
  claim=站点当前显示：八八舰队计划（八四舰队计划起案）
        字段：建造计划（identity.building_program）
        当前来源：japanese-warship-akagi

        我认为正确的是：
```

### 4.5 覆盖范围（已全站覆盖）

| 页面 | 状态 | 入口数（实测） |
|---|---|---|
| `/ships/[id]` 详细参数 | ✅ | akagi 页 69 处 |
| `/weapons/[id]` 参数（按来源分块） | ✅ | 每型 13–24 处 |
| `/classes/[id]` 舰级参数 + 武备 | ✅ | bismarck 级 135 处 |
| `/battles/[id]` 事件流 / 命中记录 / 伤亡 | ✅ | midway 页 103 处 |
| `/compare` 对比器每一格 | ✅ | 20 行 × 2 舰 = 38 处 |

**战役页是特殊的一类。** 它的数据单位不是 fact，而是「事件 / 命中 / 伤亡」这些自由文本，
没有 `field`。所以 `issueUrl()` 加了 `itemLabel` 参数——
有无 `field` 走两条路径，预填正文里一个写「字段：X（id）」，一个写「条目：X」。

**对比器需要单独处理。** 它的 `<tbody>` 全是客户端 `innerHTML` 拼的，
用不了 `<ReportIssue>` 组件，所以在 `compare.astro` 的脚本里手拼了一份
`reportHref()`。**改 `site.ts` 的 `issueUrl()` 时，这里必须同步改**（两处逻辑要一致）。

对比器的样式必须写 `:global(.cmp-rept)`——这是老坑：动态 DOM 上不带
`data-astro-cid-xxx`，普通选择器一条都命中不了（详见 `docs/20-p3-compare.md` 的坑 1）。

### 4.6 对比器怎么验证的

对比器不能靠数构建产物判断（表格在 JS 里拼，产物只有代码没有结果）。
`work/verify_compare_rept.cjs` 用最小 DOM stub 把页面脚本真跑一遍，然后断言
`tbody.innerHTML` 里的链接与参数：

```
数据行数：20
纠错链接数：38
第一个链接：俾斯麦 · 标准排水量（displacement.standard），当前 43,978 t
PASS
```

跑法：`node work\verify_compare_rept.cjs`

---

## 5. 未做的事

- **issue 的自动分类与看板**（现在只有 `correction` 一个 label）
- **交接报告 §10.3 的代理端口** 需要改成 12450（本文档 §2.2 已记录正确值，
  但报告的正文还没动——下次改报告时一并修）
- **`docs/10-deploy.md` 的部署流程**（本次 deploy 后应复核一遍，见 §7）

---

## 6. 常用命令

```powershell
# 自检
powershell -ExecutionPolicy Bypass -File scripts\check_auth.ps1

# 日常提交（注意 git 可能不在 PATH 上）
git status
git add -A
git commit -m "说明"
git push

# 数据层校验
python scripts/validate.py
python scripts/selftest.py

# 构建 + 部署
cmd /c "npm.cmd run build"
cmd /c "npx.cmd wrangler deploy"

# 对比器纠错链接的渲染验证（动态 DOM，不能靠数产物）
node work\verify_compare_rept.cjs

# 凭据掉了
gh auth login --web --scopes repo,workflow
```

## 7. 部署记录

| 日期 | 版本 ID | 内容 |
|---|---|---|
| 2026-11-20 | `c71d0aea-6f4b-48a8-ad15-7ebf17b0a5b6` | P5 纠错入口全站上线 |

部署命令 `npx wrangler deploy`（不是 `npm run deploy`，后者会重新 build，
本次已经 build 过）。上传 193 个文件、耗时约 15 秒。

线上逐页验证：

| 页面 | HTTP | 纠错入口数 |
|---|---|---|
| `/ships/akagi/` | 200 | 69 |
| `/weapons/10_5cm-sk-c33/` | 200 | 13 |
| `/classes/bismarck/` | 200 | 135 |
| `/battles/midway/` | 200 | 103 |
| `/compare/` | 200 | 38（运行时生成） |

> `wrangler` 在 PowerShell 里会以 exit code 1 结束但输出 Success——
> 那是 PowerShell 把 stderr 当错误处理，不是部署失败。看「Success! Uploaded」
> 与「Current Version ID」两行即可。
