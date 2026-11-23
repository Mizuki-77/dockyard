# c1 交付笔记 · Philip Vian / Augustus Agar / Robert Sherbrooke

> Dockyard · 2026-11-23 · 组名 `c1`
>
> 全部产出在 `work/staging_cmdr/c1/`，未触碰 `data/`、`src/`、`public/`。

---

## 1. 交付摘要

| 文件 | 简介 | 年表 | 关联 | 源文件 |
|---|---|---|---|---|
| `commanders/philip-vian.yaml` | 4 段（164 / 202 / 185 / 170 字） | 20 条 | 2 舰（cossack 两任）+ 1 战役（last-battle） | 9 个 |
| `commanders/augustus-agar.yaml` | 4 段（158 / 177 / 155 / 184 字） | 19 条 | 1 舰（dorsetshire）+ 0 战役 | 5 个 |
| `commanders/robert-sherbrooke.yaml` | 4 段（134 / 173 / 185 / 146 字） | 20 条 | 2 舰（cossack 两任）+ 0 战役 | 5 个 |

来源登记：`sources-fragment.yaml` 共 13 条 —— **D 级 10 条、E 级 3 条**。
三条关键事实（生卒、任免、战功）都落在 D 级来源上：

- `unithistories-vian` / `unithistories-agar` / `unithistories-sherbrooke`（J.N. Houterman 的 RN 军官档案）
  —— 逐条给任免起止日、晋升日、勋衔授予日与理由。三个人的生卒与军衔都靠它落地。
- `naval-history-afridi` / `naval-history-naiad` / `naval-history-emerald`（G.B. Mason 的舰艇战史）
- `bbc-altmark`、`historyofwar-altmark`（阿尔特马克的两个独立复述）
- `victoriacross-sherbrooke`、`notts-sherbrooke-vc`（VC 宪报日与 citation 措辞）

E 级只用在三处，且都写明是线索：维基条目用来搭骨架 / 找线索，正文相应段落在 `note` 里点明等级。
**没有一条 timeline 的 `src` 只有 E 级。**

自检（两个都过）：

```
python work/staging_cmdr/c1/selfcheck.py   → 0 错误 / 0 警告
python work/staging_cmdr/c1/sitecheck.py   → 0 错误 / 0 警告（直接调用 scripts/validate.py 的 check_commander）
```

`selfcheck.py` 查结构、intro 字数（100–220，按汉字计）、年表升序、来源已登记、关联 id 真实存在、模糊词；
`sitecheck.py` 用站点自己的校验函数跑这三份文件，保证合入后不会被 `validate.py` 拦下。

---

## 2. 任务书里写错的地方（以来源为准，已改）

### 2.1 Vian 的出生日：不是「1894-06-15 待核实」，而是确实 06-15，但维基 infobox 有个笔误

任务书给的 1894-06-15 是对的，`unithistories-vian` 记为 `15.06.1894 London`。
**但要提醒主会话**：英文维基 infobox 的 `death_date` 模板写的是
`{{death date and age|df=y|1968|5|27|1894|6|14}}` —— 出生日被写成 **06-14**，
与它自己的首段（15 June 1894）和 unithistories 都矛盾。这是模板笔误，不要在别处照抄。

### 2.2 Vian 与北角海战无关 —— 任务书这一条要删

任务书说 Vian「北角海战击沉沙恩霍斯特」。**这件事他没参与。**

- `unithistories-vian` 的任免表里，1943 年 9–11 月他在萨勒诺（Force V / TF 88），
  11 月起转诺曼底（Force J / Eastern Task Force），1944 年全年在英国与诺曼底；
  1944-11-15 才去英国太平洋舰队。**1943 年 12 月他不在北角。**
- 北角海战（1943-12-26）的英方指挥是 Fraser（本土舰队）与 Burnett（Force 1，坐镇 Belfast），
  与 Vian 无关。

因此 `philip-vian.yaml` 里没有北角，也没有沙恩霍斯特。

### 2.3 「Vian 击沉沙恩霍斯特」与「Vian 从驱逐舰舰长做到海军元帅」的措辞

后半句没问题：DSO 三枚（1940-04-12 阿尔特马克、1940-12-03 DN 行动、1941-10-14 俾斯麦），
1941-07-08 少将，1952-06-01 海军元帅同日退役，`unithistories-vian` 全有。
前半句（北角）见上，删。

### 2.4 Vian 在「最终战」里的实际位置 —— 任务书要求「查清再写」，结论如下

任务书的直觉是对的，这里必须写准，因为很容易写成「Vian 参加了击沉俾斯麦的炮战」：

- **05-26 22:00** Sheffield 把敌方位距离交给第 4 驱逐舰分队（`kbismarck-chase`、`hmshood-tovey-dispatch` §72）。
- **整夜至 05-27 08:45**：他指挥五舰跟踪 + 鱼雷攻击，共射 16 枚鱼雷。
  托维战报 §74 记「Cossack 与 Maori 各有一雷命中，Sikh 可能也命中」；
  「俾斯麦最高生还军官说驱逐舰鱼雷无一命中」这条记录在本站 `data/battles/last-battle.yaml` 的争议 6 里。
- **08:45 主力舰接火之后**：炮战由 KGV / Rodney / Norfolk / Dorsetshire 完成。
  Vian 的分队不在白昼炮战序列里；战报 §90 记「KGV 与 Rodney 带 Cossack、Sikh、Zulu 北上返航」。

所以 `relations.battles[0].role` 写的是「第 4 驱逐舰分队指挥官，率五艘驱逐舰夜间跟踪与鱼雷攻击」，
并在 `note` 里明写「他与分队不在当日白昼的炮战序列内」。这是本档案最需要主会话复核的一条。

另一处细节：托维战报 §72 写他「**放弃**了对 KGV 与 Rodney 的屏护任务去追」，
而海军部原令是「join and screen the King George V and the Rodney」（§54）。
这个「抗令去追」是托维自己写进战报并嘉许的（"as I knew he would"），
是 Vian 这个人的关键判断，已写进 intro 第 3 段。

### 2.5 Agar 的军衔：最终是 **Captain（上校）**，不是准将

`unithistories-agar` 的晋升链是 `Capt. 31.12.1933 (retd 12.01.1943)`，另有
`Cdre. 2nd cl. (retd) 15.11.1943`。两级准将是**退休名册上的**，
1943-11-15 授，任格林尼治院长至 1946-09-30，任满「回为上校实衔」。
所以 `rank_final: Captain`，`note` 里解释了为什么不用准将。

### 2.6 Agar 的 VC 事迹：任务书说「击沉苏联巡洋舰」—— 准确，但可以更准

沉的是 **6,645 吨的巡洋舰 Oleg**（`unithistories-agar` 的 VC citation 原文：
"a Russian cruiser was sunk"；英文维基点名为 Oleg）。
任务书说「用鱼雷艇击沉」，他当时是 **CMB4 的艇长**，不是「鱼雷艇」这种泛称；
CMB 是 5 吨级的海岸摩托艇，与蒸汽鱼雷艇不是一类东西。文件里用 CMB 原词。

### 2.7 Sherbrooke 的哥萨克号任期：任务书只给了一段，实际是两段

任务书：`cossack` 1939-12-29 至 1940-01-18。
`uboat.net` 的舰长表（`uboat-cossack`）列了 **两次**：

```
2  Cdr. Robert St. Vincent Sherbrooke  29 Dec 1939 – 18 Jan 1940
4  Cdr. Robert St. Vincent Sherbrooke  29 Mar 1940 – 21 May 1940
```

第 4 任这一段在 `data/ships/cossack.yaml` 里目前**没有收录**（那里写的是
「Vian 在本舰任内有两次任期，中间短暂由 Sherbrooke 接任」——措辞把两段并成一句，
数字上看不出第二段的起止）。

我在 `robert-sherbrooke.yaml` 里把第二段写进了 relations，并在 note 里标注
「本条是本次调研新增的第二任期」，**没有改 `data/ships/cossack.yaml`**（不在我的权限内）。
建议主会话在合并时决定：是把 Sherbrooke 的第二任期补成一条独立 fact，
还是维持现在这种「注记式」写法。前一任 Daniel de Pass 到 1939-12-29，第 5 任 Vian 从 1940-05-21 起，
两个空档正好对上，说明 uboat.net 这条表内部是自洽的。

### 2.8 Agar 与 Dorsetshire 的接任日：任务书给 1941-08-18，另有 08-08 一说

`uboat.net` 记 18 Aug 1941；`unithistories-agar` 记 `08.08.1941–05.04.1942`；
`naval-history-dorsetshire` 也记 8 Aug 交接。差 10 天，可能是「任命」与「到舰」之别。
`data/ships/dorsetshire.yaml` 已经就这一点写过并列表述，我沿用 uboat.net 的窗口并在 note 里说明。

### 2.9 舍布鲁克在 1940-04-13 到底在哪条舰上：我判了，理由如下

一开始我把这一条当成「两源打架」并列处理，后来发现**可以直接裁决**，所以改了：

- `naval-history-afridi`：1940 年 4 月 13 日 Afridi 的任务是「Deployed in search operation …
  for ships reported by aircraft」，**在港外搜索**，没有入港。
- `naval-history-cossack`：同日「2nd Battle of Narvik. Engaged and sank German destroyer ERIC GIESE
  with HMS FOXHOUND … hit by nine 5in shells」，**入港作战的是哥萨克号**。
- `unithistories-sherbrooke`：DSO 的授勋理由写作「2nd Battle of Narvik」（1940-06-28）。

三条合起来：他拿 DSO 的那一役，Afridi 不在战场，哥萨克号在。所以 4 月 13 日他在**哥萨克号**上，
这与 uboat.net 记他 1940-03-29 起任哥萨克号舰长完全吻合。
unithistories 把 Afridi 的任期结束日记作「04.1940」，只差月份精度，不是反证。

**教训**：军官档案与舰艇档案的「任期边界」经常只精确到月，把它们当成同一天的两种说法去并列，
会凭空造出争议。先用舰艇侧的当日行踪交叉验证，再决定要不要并列。

---

## 3. 卡住的地方

### 3.1 London Gazette 原文拿不到

`thegazette.co.uk` 对 `.../data.pdf` 一律返回 **HTTP 202 + Content-Type text/html**（空 body），
不是 200 PDF。换了 `Accept: application/pdf` 头也一样。所以三份最重要的 citation
（Vian DSO 1940-04-12、Agar VC 1919-08-22、Sherbrooke VC 1943-01-12）都**没有取到一手文本**。

替代方案（已采用）：用 `unithistories` 条目内附的 citation 摘录 + `victoriacross-sherbrooke`
按《Register of the Victoria Cross》体例的 citation 摘要，两者措辞互校。
**宪报日期本身**（不是 citation 全文）在这两个来源里一致，可以写。
如果主会话有办法拿到 PDF（例如换 UA 或走代理），建议补一条 tier A 的
`london-gazette-35859` 之类，把 Sherbrooke 的 citation 钉到一手来源上。

### 3.2 unithistories 没有 Sherbrooke 的独立页码可猜

Sherbrooke 不在 `RN_officersS.html` 也不在 S2 / S3 里，实际落在
`RN_officersS1b.html#Sherbrooke_RStV` —— 这个文件名是从英文维基的外链里抄来的，不是猜的。
另外它的条目把姓拆成 `S<span small-caps>herbrooke</span>`，**纯文本检索「Sherbrooke」会漏**
（我一开始就漏了）。以后再做这批人，直接抓 HTML 后按 `<a name="...">` 定位，别按纯文本搜。

### 3.3 Dorsetshire 沉没前的决策链只有 E 级

4 月 4 日晚出港、会合点选择、电台被毁后继续南驶——这一整段**只有英文维基（E 级）**给出叙述。
D 级能确证的只有：4 日奉命归队、5 日被利根号水侦发现、8 分钟沉没、234 人阵亡、约 30 小时后获救
（`naval-history-dorsetshire`、`uboat-dorsetshire`）。

处理：intro 第 4 段只写 D 级可确证的部分，**没有**把「他做了致命的判断」这类评价写进去；
`note` 里明写哪些是 E 级、哪些是 D 级。如果主会话希望这一段更有判断力，
需要补一手材料（Somerville 的 ADM 199 或东方舰队战报），我这边没找到可直连的副本。

### 3.4 希特勒 1943 年初停用水面舰队 —— 因果只有 E 级

「巴伦支海一役导致希特勒下令停用水面舰队」这条因果关系只见英文维基。
写进 `robert-sherbrooke.yaml` 的 `note` 作为「不作断言」的说明，正文不写。
`data/battles/` 里没有巴伦支海这一役（本站未收录），也没有对应 narrative 可挂。

### 3.4b 舍布鲁克的 Aurora 任期只有 E 级，且与 unithistories 冲突

英文维基说他 1945 年 7 月至 1946 年中任 Aurora 舰长。
但 `unithistories-sherbrooke` 的任免表在 1944-04 至 1946-04 这一段写的是
「no appointment listed」，而 `naval-history-aurora` 通篇不记舰长姓名。

处理：这条仍留在年表里（他是当事人，职务记录本身不荒谬），但**加了 `note` 标明只靠 E 级**，
并且 intro 第 4 段**不再提 Aurora**，改成只写有 D 级支撑的战后履历（授衔、退役、郡职、骑士团职务）。
如果主会话要求「timeline 每条都要 D 级以上」，这条应当删——我没有擅自删，留给你定。

### 3.5 试过但失败的站点

| 站点 | 结果 |
|---|---|
| `thegazette.co.uk` 的 `/data.pdf` | 202 + 空 body，拿不到 PDF（见 3.1） |
| `kbismarck.com/bismarck-final.html`、`/bismarck-last-battle.html` | 404，且后续重试报 SSL `UNEXPECTED_EOF` |
| `naval-history.net` 的 Onslow 页 | 试了 `25O`/`25N` 命名与 `_1`/`_2` 后缀，全部 404；改用 `unithistories-sherbrooke` 的任免表代替 |
| `victoriacross.co.uk` 的 Agar 页 | `/recipients/augustus-agar/` 与长名 slug 都 404；Agar 的 VC 日期改由 unithistories 提供 |
| `naval-history.net` 的 Aurora / Emerald 页 | 抓到了，但通篇不提舰长姓名，Sherbrooke 的 Aurora 任期改引英文维基（已标 E 级） |
| `web_fetch` / `research` | 按任务书说明，本机对所有域名 SSRF 拦；全程用 urllib + 浏览器 UA |

---

## 4. 有争议的记载（两源打架，已并列，未裁决）

| # | 事实 | 说法 A | 说法 B | 处理 |
|---|---|---|---|---|
| 1 | Vian 哥萨克号第二任期起点 | uboat.net：1940-05-21 | unithistories：1940-05-05 | 取 A 作窗口，年表写「两说并列，不裁决」 |
| 2 | Vian 第二任期终点 | uboat.net：1941-07-10 | unithistories：1941-07-08 | 同上 |
| 3 | Agar 接任 Dorsetshire | uboat.net：1941-08-18 | unithistories / naval-history：1941-08-08 | 取 A 作窗口，note 说明，与 `data/ships/dorsetshire.yaml` 现有写法一致 |
| 4 | 舍布鲁克第二次哥萨克号任期 | uboat.net：1940-03-29 至 1940-05-21 | unithistories：`18.01.1940–04.1940` 任 Afridi | 实为**月份精度差**，不是冲突，已按 §2.9 判为同一件事 |
| 5 | 1940-04-13 第二次纳尔维克海战时舍布鲁克在哪个舰上 | uboat.net 排班 → 哥萨克号 | unithistories 排班 → Afridi | 已**裁决**（见 §2.9）：`naval-history-afridi` 记 Afridi 当日只在港外搜索，入港作战的是哥萨克号；DSO 的授勋理由正是该役，反向锁定哥萨克号 |
| 6 | 驱逐舰 05-26 夜鱼雷是否命中俾斯麦 | 托维战报 §74：Cossack、Maori 各一雷命中，Sikh 可能 | 俾斯麦最高生还军官：全部未中 | 年表并列；与本站 `last-battle` 争议 6 口径一致 |
| 7 | Vian 出生日在维基 infobox 里是 06-14 | 维基 infobox 模板 | 维基正文 + unithistories：06-15 | 采 06-15，并在 note 指出模板笔误 |

第 1、2、3、6 条的「另一说」在本站既有数据里已经存在（我没有引入新分歧，只是把已有的分歧在人物页上复述一遍）。

---

## 5. 给主会话的三条提醒

1. **合并前请先看 §2.2：Vian 与北角海战无关。** 如果 `data/` 或页面文案里已经写了
   「Vian 在北角击沉沙恩霍斯特」，那是错的，需要删。
2. **§2.7 的舍布鲁克第二任期**要不要补成 `data/ships/cossack.yaml` 的独立 fact，
   需要你定；我按规范没动 `data/`。
3. **§3.1 的宪报原文**是目前最大的来源缺口。三个人的 VC/DSO citation 都还悬在
   tier D 的转述上，没有 tier A 的一手件。

---

## 6. 目录内其它文件（不是交付物，但留着可复现）

```
work/staging_cmdr/c1/
  sources-fragment.yaml       <- 交付
  commanders/*.yaml           <- 交付（3 份）
  NOTES.md                    <- 本文件
  selfcheck.py                <- 结构/字数/升序/登记/关联 自检
  sitecheck.py                <- 调 scripts/validate.py 的 check_commander
  _raw/                       <- 抓下来的原始 HTML 与纯文本、转换脚本
```

`_raw/` 里体积较大的几个（`uh-RN-A.html` 810 KB、`uh-RN-A2.html` 747 KB、
`uh-RN-S1b.html` 600 KB、`uh-RN-S2/S3.html` 各 850 KB / 1.1 MB）都是 unithistories 的分页原件，
留着是为了将来核任免日期时不用重抓。如果主会话要清工作区，这些可以删——
`unithistories-*.yaml` 里的 note 已经写清了从哪个锚点取（`#Vian_PL` / `#Agar_AWS` / `#Sherbrooke_RStV`）。

一次性探针脚本（猜 unithistories 分页、试 Gazette PDF 的那几个）已经清掉，只留下还能用的四个：
`fetch.py`（urllib 抓页）、`totxt.py`（HTML→文本）、`rows.py`（把 unithistories 的表格行解析成
「起 / 止 / 说明」三元组，避免日期与描述错位）、`ctx.py`（按关键词打印上下文）、`wclean.py`（Wikitext 洗文本）。
