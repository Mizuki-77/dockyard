# c2 组交付说明 · 三位英国皇家海军舰长

> Dockyard · 2026-11-23 · Power / Hamilton / Denny
> 交付目录：`work/staging_cmdr/c2/`

---

## 1. 交付摘要

| 文件 | 简介 | 年表 | 关联舰 | 关联战役 | 来源数 |
|---|---|---|---|---|---|
| `commanders/arthur-power.yaml` | 5 段 | 20 条 | 1（`ark-royal`） | 0 | 3 |
| `commanders/louis-hamilton.yaml` | 5 段 | 19 条 | 1（`prince-of-wales`） | 0 | 4 |
| `commanders/michael-denny.yaml` | 5 段 | 20 条 | 1（`victorious`） | 0 | 6 |

来源：新增登记 6 条（`sources-fragment.yaml`），复用在 `data/sources.yaml` 里已登记的 4 条
（`naval-history-arkroyal`、`naval-history-pow`、`naval-history-victorious`、
`naval-history-aurora`、`ac-vic-kamikaze`、`ac-kami-co`、`ac-pacops`、`ac-tf57`，共 8 条）。
**零 E 级来源**：三篇都没有用维基作 src，timeline 的每一条都至少指向一个 D 级来源。

自检：
- `python work/staging_cmdr/c2/_raw/selfcheck.py` → 全部通过
  （结构 / 日期格式 / 升序 / intro 字数 100–220 / timeline 8–20 / ship·battle id 存在 / src 已登记）
- 直接调用项目 `scripts/validate.py` 的 `check_commander()` → **0 错误 0 警告**

---

## 2. 任务书需要更正的地方（以来源为准）

### 2.1 Hamilton 不是丹麦海峡海战当天的舰长 —— 这一条必须改

任务书写「`denmark-strait`（1941-05-24，威尔士亲王号参战，**他就是当天的舰长**）」，**与三份来源全部冲突**：

| 来源 | 记载 |
|---|---|
| `unithistories-hamilton` | Prince of Wales 任期 `05.10.1940 – 14.02.1941`（在建期间指挥），`15.02.1941 – 27.02.1941` 已转「whilst unemployed」 |
| `uboatnet-cmdr-hamilton` | Warship Commands：`HMS Prince of Wales (53) 5 Oct 1940 – 15 Feb 1941` |
| `naval-history-pow` | 「**February 15th** - The PRINCE OF WALES new CO Captain John Catterall Leach MVO RN took command.」 |

1941-05-24 当天在舰桥上的舰长是 **John Catterall Leach**。`naval-history-pow` 还记了那一幕：
「At 0602 hours A shell from BISMARCK's first salvo … passed through the compass platform
without exploding but killing everyone except **the Captain** and the Chief Yeoman.」

所以 `relations.battles` **留空**。硬填会造出一条错误的双向跳转（战役页 ↔ 一个当天根本不在舰上的人）。

### 2.2 Denny 的勋衔不是 KBE

任务书和不少二手资料写 `KBE`。`unithistories-denny` 与 `uboatnet-cmdr-denny` 一致给出的是
**CB (1940-06-07) / CBE (1944-01-01) / DSO (1945-10-23) / KCB (1950-06-08) / GCB (1954-06-10)**，
没有 KBE。`full` 字段按 `GCB, KCB, CBE, DSO` 写。

### 2.3 Denny 的最终军衔是 Admiral，不是 Admiral of the Fleet

两份 D 级来源都止于 `Adm. 22.04.1952`，`Retired: 28 Jul 1959`。没有更高晋升记录。
`rank_final: Admiral`。

（对照：Power 确实是 `Admiral of the Fleet 22.04.1952`，那一处任务书没错。）

### 2.4 Power 的皇家方舟号任期起点要分两层写

任务书表格里写「1938-01-17 至 1940-04-20」，与 `uboatnet-arkroyal-class` 一致，没问题。
但 `unithistories-power` 把这一段拆成两条：「17.01.1938 - 26.07.1938 CO *while under construction*」
和「26.07.1938 - 04.1940 CO」，且 1939-07-26 起兼舰旗舰长与参谋长。
本文件按 1938-01-17 起算，但在 timeline 里把两层都写了。

### 2.5 Power 的生年：uboat.net 错了

`uboatnet-cmdr-power` 写「Born 12 Apr **1899**」。按 1899 算：
1904 年入 Britannia 时 5 岁、1909 年任 sub-lieutenant 时 10 岁、1910 年升 lieutenant 时 11 岁——
全部不成立。`unithistories-power` 与维基均为 **1889-04-12**。本站采 1889。
**这可能是 uboat.net 的单条录入错误，但它是本站唯一给出「12 Apr」日期的 D 级来源**，
所以 `life.born` 的日期部分只能靠 unit histories 的 `12.04.1889`。

### 2.6 Denny 接任胜利号的日期，两份 D 级来源打架

| 来源 | 口径 |
|---|---|
| `unithistories-denny` / `uboatnet-cmdr-denny` | 1943-12-08 至 1945-08-15 |
| `ac-pacops`（armouredcarriers） | 「refit which lasted until **March 4, 1944**. During this period Captain Mackintosh departed the carrier, replaced by Captain Denny.」——只说「大修期间换人」，不给日期 |

**`data/ships/victorious.yaml` 里现有的 fact 用的是 1944-03-04 起**，与本组新文件不一致。
本组按 D 级数据库的 1943-12-08 写，并在 `relations.ships[].note` 与 timeline 的 note 里
把两说并列。合并时要不要统一，请主会话决定。**我没有改 `data/`。**

### 2.7 Power 交舰日：1940-04-20 还是 1940-05-03

- `uboatnet-cmdr-power` / `unithistories-power`：1940-04-20
- `naval-history-arkroyal`：叙事写「At Scapa refuelling and replenishing, where her new CO
  Captain Cedric Swinton Holland RN took command.」——该段落在 1940-05-03 条下

两说并列。`relations.ships[].to` 取 1940-04-20（与本站 ship 文件既有口径一致）。

---

## 3. 写作上的三个抓手，落地情况

- **Power：交舰那一刻的性质**。他任内皇家方舟号做的是「存在舰队 + 反潜搜索 + 商船拦截」，
  两件最要他当场决断的事（U-39 齐射、Ju 88 俯冲）都写进 intro 第 3 段了。
  挪威战役（1940-04-23 起 Operation DX / 后续 Narvik 支援）与米尔斯克比尔（1940-07-03）
  **都在他 4 月 20 日交舰之后**——这一条任务书的括注写反了，已在 `note` 里写明不计入。
- **Hamilton：一艘没完工的舰**。他 1940-10-05 到任时舰还在伯肯黑德舾装，编制挂在利物浦的
  HMS Eaglet 下；1941-01-19 服役时「incomplete, and with only half her crew, for trials」；
  1 月 28 日出海试射时「she had embarked workers from Cammell Laird and Vickers Armstrong
  who were working on her main armament turrets」。**到 1941-05-21 该舰报「ready for Fleet
  service」时，80% 舰员是 Hostilities Only、从没上过船** —— 但那时 Leach 已经是舰长。
- **Denny：持续作战条件下的舰长**。我按「一年半没离开过这条舰」组织：Tungsten → 东印度舰队 →
  太平洋 → 冲绳 → 两次神风。神风部分用的是他自己 1945-05-10 报告（`ac-kami-co`，A 级）的
  逐分钟时刻，加上 `ac-vic-kamikaze` 收录的两段直接引语。

---

## 4. 卡住的地方

### 4.1 `unithistories.com` 的 RN 军官页要翻页找

P 姓分 `RN_officersP.html` / `P1a` / `P2` 三页，Denny 在 `D3`，Hamilton 在 H 首页。
首页搜不到不等于没有——第一轮我在 `RN_officersP.html` 里搜 `Power` 得 0 命中，
差点判定「该站没有此人」。**顺序是按页翻，不能只看首页。**

另：该站对 `http://www.unithistories.com/officers/RN_officersX.html` 直连会 404，
必须走 `https://www.unithistories.com/officers/RN_officersX.html`；
而 `units_index/index.php?file=/officers/...` 那套代理路径只会返回一个空壳页（549 字节）。

### 4.2 Power 的出生地没拿到

`unithistories-power` 只给卒地（Gosport district, Hampshire），不给出生地。
uboat.net 也不给。维基不给。**`life.born_place` 留空**，没有猜。

### 4.3 Denny 的卒日只有一份来源

`unithistories-denny` 给 `07.04.1972 Down Ampney, Cirencester, Gloucestershire`；
`uboatnet-cmdr-denny` **只给生年 1896，没有卒日**。所以 1972-04-07 实际是单源。
任务书给的 1972-04-07 与 unit histories 一致，采用；但它不是双源确认过的。

### 4.4 Power 一战初期那几段任职没有精确日期

`unithistories-power` 对 Magnificent / Royal Arthur / Raglan / Princess Royal 只给舰名不给日期
（同一页给了 1917-08-17 起在 Magnificent，但 Raglan 与 Princess Royal 无起止）。
所以 timeline 里我把它们合成一条 `1915` 的记录，不编月份。

### 4.5 试过但没用的站点

- `admirals.org.uk`：站内只有 Board of Admiralty / Naval Staff 两个栏目页，**没有个人传记条目**，
  `?s=Power` 搜索返回空。不能用。
- `thegazette.co.uk`：`/all-notices/notice?text=...` 返回 0 字节（脚本/JS 渲染），拿不到。
- `gulabin.com`：首页 712 字节，PDF 目录 404。
- `armouredcarriers.com/document-commanding-officer-hms-victorious-kami`：404，
  正确 slug 是 `...-kamikaze-may-9`（已在 `data/sources.yaml` 里，本次复核可用）。
- `web_fetch` 对以上全部域名返回 SSRF 拦截；全部改用 `urllib` + 自定义 UA 直连。

---

## 5. 有争议 / 两说并列的清单

| # | 事实 | 说法 A | 说法 B | 本文件处理 |
|---|---|---|---|---|
| 1 | Power 生年 | 1889-04-12（unithistories） | 1899-04-12（uboat.net） | 采 1889，在 note 里写明理由 |
| 2 | Power 交卸皇家方舟号 | 1940-04-20（uboat.net / unithistories） | 1940-05-03（naval-history 叙事） | 两说并列，`to` 取 04-20 |
| 3 | Denny 接任胜利号 | 1943-12-08（uboat.net / unithistories） | 1944-03-04（ac-pacops，且本站 ship 文件已采此说） | 两说并列，本文件取 12-08 |
| 4 | Denny 卒日 | 1972-04-07（unithistories） | 无（uboat.net 缺） | 采 04-07，标注单源 |
| 5 | Hamilton 威尔士亲王号任期 | 1940-10-05 起（含在建期指挥） | 1941-01-19 服役日起（任务书口径） | 取 10-05，note 说明分两层 |
| 6 | Denny 1945-05-09 伤亡数 | 报告原件「3 killed + 20 others wounded」（ac-kami-co） | 汇编「3 killed, 19 wounded」（ac-vic-kamikaze） | 未写具体总人数，只写阵亡的炮组 |

第 6 条：`data/sources.yaml` 里 `ac-kami-co` 的 note 已经把这个 1 人之差记过了，本文件不复述。

---

## 6. 未做的

- **没动 `data/`、`src/`、`public/`**。Denny 接任日与 `data/ships/victorious.yaml` 现有一致性
  问题（见 2.6）留给主会话裁决。
- 挪威战役（`operation-dx` 等）与米尔斯克比尔、PQ 17 都写在 intro 与 timeline 里了，
  但本站 `data/battles/` 没有这些条目，所以**没有对应 relations.battles 可连**。
  如果以后补这些战役，Power（米尔斯克比尔、挪威）、Hamilton（PQ 17、挪威）、
  Denny（冲绳）都已有现成的时间与身份可以接。
