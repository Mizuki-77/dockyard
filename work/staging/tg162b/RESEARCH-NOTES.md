# 调研底稿 — TG 16.2 三巡洋舰（北安普敦 CA-26 / 彭萨科拉 CA-24 / 亚特兰大 CL-51）

> tg162b 组 · 2026-11-23
> 产出目录：`work/staging/tg162b/`
> 按 SCHEMA §9 规矩：每条结论带**英文原句 + URL**。

---

## 0. 本轮取证环境（合并时必读）

**`web_fetch` / `research` 未使用**（本机 SSRF 拦截，SCHEMA §9.1 已述）。

改用 Python urllib + UA 直连，**但两个关键站点在本机的 TLS 握手被重置**：

| 站点 | 症状 | 解决办法 |
|---|---|---|
| `history.navy.mil`（DANFS 正本） | `SSL: UNEXPECTED_EOF_WHILE_READING`，Python urllib 与 curl/schannel 全失败 | 改走 `web.archive.org` 2021 快照 |
| `navsource.org` | 同上（https 与 http 均被重置） | 改走 `navsource.net`（同站另一域名，直连可通） |

**因此 `danfs-northampton` / `danfs-pensacola` 两条来源的 `access` 记 `proxy`**，
其余全部 `direct`。主会话合并时若发现 access 语义不符，改这两条即可。

可直连的站点（本轮实测）：`navypedia.org`、`navweaps.com`、`ibiblio.org/hyperwar`、
`navsource.net`、`midway1942.com`、`web.archive.org`（有 429 限流，需间隔重试）。

### 0.1 一条容易踩的坑：DANFS 的 URL 编号

- **彭萨科拉是 `pensacola-iii`，不是 `pensacola-ii`**。
  我第一轮抓 `pensacola-ii` 拿回来的是 1918-1925 年那艘运煤船（ScStr）的船史。
- 北安普敦是 `northampton-ii`（第一艘同名舰保留了原名，故序列上只算一艘）。
- 亚特兰大在 Wayback 上取不到 `atlanta-ii`（404/429），
  改用 ibiblio 的 HyperWar 转录 `danfs_atlanta`（正文与 DANFS 单行本一致）。

---

## 1. 三处「任务书陈述 vs 来源」的核对结果

任务书里的史实陈述全部当「待核实」处理。逐条结论：

### 1.1 ✅ 成立：三舰 1942-06 都属 TG 16.2（RA Kinkaid）

> "Task Group 16.2 (TG 16.2) / Cruiser Group / Rear Adm. Thomas C. Kinkaid, USN /
> Commander Cruiser Division 6 (ComCruDiv 6) / USS New Orleans (CA-32) /
> USS Minneapolis (CA-36) / USS Vincennes (CA-44) / USS Northampton (CA-26) /
> USS Pensacola (CA-24) ... USS Atlanta (CL-51)"
> — https://www.ibiblio.org/hyperwar/PTO/TideTurns/Midway/Midway-OOB.html

交叉源 NavWeaps 逐舰带 Notes：
> "USS Northampton (CA-26) ... Notes: Escorting Enterprise."
> "USS Pensacola (CA-24) ... Notes: Escorting Enterprise; joined TF-17."
> "USS Atlanta (CL-51) ... Notes: Escorting Hornet."
> — https://www.navweaps.com/index_oob/OOB_WWII_Pacific/OOB_WWII_Midway.php

### 1.2 ❌ 任务书错：北安普敦不是 TG 16.2 旗舰，旗舰是明尼阿波利斯

**任务书写「注意：它不是 TG 16.2 旗舰（旗舰是明尼阿波利斯）」——这一条任务书是对的，
但它同时提到「我此前写错过」，所以这里给出一手证据把结论钉死：**

> "TASK ORGANIZATION: Task Force 16, Rear Admiral R.A. Spruance in ENTERPRISE
> Task Group 16.2, **Rear Admiral T.O. Kinkaid in MINNEAPOLIS**, NORTHAMPTON,
> PENSACOLA, ATLANTA, NEW ORLEANS, VINCENNES"
> — USS Enterprise (CV-6) War Diary, June 1942
> https://midway1942.com/docs/usn_doc_21.shtml

**「in MINNEAPOLIS」是美军战报里标旗舰的标准写法**（舰名紧跟在司令名之后）。
这是本轮最硬的一条证据，因为它是一手战报的转录。

另需注意 Kinkaid 的职务写法：**ComCruDiv 6（第 6 巡洋舰分队司令）**，
不是「第 6 巡洋舰队」——`docs/51` §4 已记录过这个用词错误，本轮再次确认。

### 1.3 ⚠️ 任务书需修正：「亚特兰大在中途岛大显身手」不成立

任务书说「亚特兰大护卫大黄蜂」——**编队归属成立**，但补充一个容易写错的细节：

> "During the crucial 4-6 June 1942 Battle of Midway Atlanta was in the screen for
> Enterprise and Hornet, **but these ships did not come under attack**."
> — DANFS 简史页 https://www.ibiblio.org/hyperwar/USN/ships/dafs/CL/cl51-history.html

**中途岛时本舰一炮未发。** DANFS 长稿更明确：
> "Atlanta emerged from her baptism in fire unscathed and confident"
> ——这句说的是 1942-08-24 东所罗门群岛海战，不是中途岛。
> 长稿原文："this was the first opportunity the crew has had to actively join the
> enemy in battle."（引副舰长 Campbell D. Emery）
> — https://www.ibiblio.org/hyperwar/USN/ships/dafs/CL/cl51.html

任务书里「亚特兰大护卫大黄蜂」这半句成立，但若正文写成「在中途岛作战」就是错的。

---

## 2. 各舰核实要点（任务书点名要查的项）

### 2.1 亚特兰大 1942-06 是否已服役？—— 已服役，服役满 162 天

> "commissioned at the New York navy Yard on 24 December 1941;
> Capt. Samuel P. Jenkins in command"
> — https://www.ibiblio.org/hyperwar/USN/ships/dafs/CL/cl51.html

四源一致（DANFS 长稿 / DANFS 简史页 / navypedia / NavSource）。
**服役到中途岛出港之间的时间线**（全部出自 DANFS 长稿）：
1942-03-13 前试航结束 → 03-31 判定 "ready for distant service" →
04-05 离纽约 → 04-08 抵 Cristobal → 04-23 抵珍珠港 →
05-10 出港 → **05-16 加入 TF 16** → 05-26 回珍珠港 → 05-28 随 TF 16 出港。

### 2.2 亚特兰大主炮几座？—— 8 座双联，16 门

> "Twin Enclosed Base Ring Mounts ... St. Louis (4), **Atlanta (8)**, Oakland (6)
> and Juneau (ii) (6): **Mark 29**"
> — https://www.navweaps.com/Weapons/WNUS_5-38_mk12.php

navypedia 独立印证："Armament CL51, 52: **8 x 2** - 127/38 Mk 12"。
**8 座 × 2 管 = 16 门**。DANFS 题头 "16 5"" 说的是门数，不是座数。

**这是本轮最容易出错的一个数**：把它当 8 门会低估一半火力，
当 16 座会高估一倍。

### 2.3 亚特兰大防空炮 —— 3 座四联 1.1"/75，1942 年初加到 4 座

> "Armament CL51, 52: 8 x 2 - 127/38 Mk 12, **3 x 4 - 28/75 Mk 1**,
> 2 x 4 - 533 TT, 2 DCR"
> "early 1942, Atlanta, Juneau: **+ 1 x 4 - 28/75 Mk 1**"
> — https://www.navypedia.org/ships/usa/us_cr_atlanta.htm

**20 mm 有分歧，未写 fact**，见 §6。

### 2.4 亚特兰大有鱼雷管 —— 2 座四联，Mark 15

> "Ship Class Used On: Destroyers and **Atlanta (CL-51) Class Cruisers**"
> （Mark 15 条下）
> — https://www.navweaps.com/Weapons/WTUS_WWII.php

navypedia "2 x 4 - 533 TT"，DANFS 题头 "8 21" tt."，NavSource "8 x 21" tt."。
**四源一致 8 管 / 2 座**。鱼雷型号只有 NavWeaps 给（Mark 15），故新建了
`weapon:21in-mk15` 实体。

### 2.5 彭萨科拉主炮布置 —— 2 座三联 + 2 座双联，共 10 门

**任务书问「几座？两座三联+两座双联？待核实」——答案：是，两源独立印证。**

> "Twin Mounts ... **Pensacola (2)**"
> "Triple Mounts **Pensacola (2)**, Northampton (3) and Indianapolis (3)"
> — https://www.navweaps.com/Weapons/WNUS_8-55_mk9.php

> "Armament **2 x 3** - 203/55 ..., **2 x 2** - 203/55 ..."
> — https://www.navypedia.org/ships/usa/us_cr_pensacola.htm

布置方式的解释（navypedia 独家）：
> "As a result cruisers had rather unusual arrangement of main turrets:
> **end twin turrets and superfiring triple ones.**"

即：**双联在首尾两端（低位），三联背负在它们上面**。
这是美国条约重巡里独一份的布置。

### 2.6 彭萨科拉十字路口核试 —— 是，两次爆炸都存活

> "She stood out of Pearl Harbor 20 May and reached Bikini the 29th to serve as
> a target ship. **She survived the tests of 1 July and 25 July 1946.**"
> — DANFS https://www.history.navy.mil/research/histories/ship-histories/danfs/p/pensacola-iii.html

NavSource 逐条列了两次：
> "**Survived atomic aerial burst on 1 JUL 1946** /
> **Survived atomic subsurface burst on 25 JUL 1946** /
> Decommissioned 26 AUG 1946 /
> Fate: **Sunk as target on 10 NOV 1948 off the coast of Washington.**"
> — https://navsource.net/archives/04/024/04024.htm

### 2.7 北安普敦级有鱼雷管 —— 只对 1931 年以前成立

**任务书说「北安普敦级有鱼雷管，这是与后来级的关键差别」——需要加时间限定。**

> "1931, all: **- 2 x 3 - 533 TT**"
> — https://www.navypedia.org/ships/usa/us_cr_northampton.htm

NavSource 一张 1930 年代初照片的图注是旁证：
> "USS Northampton (CA 26) underway during the early 1930s,
> **prior to the removal of her torpedo tubes.**"
> — https://navsource.net/archives/04/026/04026.htm

**结论：建成时 2 座三联 6 管，1931 年全拆。1942 年中途岛时本舰鱼雷管为 0。**
「有鱼雷管」这个特征与后来的新奥尔良级确实不同（后者从未装），
但北安普敦级自己也只带了 1 年多。

### 2.8 北安普敦塔萨法隆加 —— 1942-12-01 沉没，被亲潮号两条鱼雷

> "Close to the end of the engagement, Northampton was struck by two torpedoes,
> which tore a huge hole in her port side ... Three hours later, as she began to
> sink stern first, she had to be abandoned."
> — DANFS https://www.history.navy.mil/research/histories/ship-histories/danfs/n/northampton-ii.html

> "Sunk by two torpedoes from the Japanese destroyer **Oyashio** during the
> Battle of Tassafaronga off Guadalcanal on **01 DEC 1942**."
> — https://navsource.net/archives/04/026/04026.htm

**日期口径说明**：战斗始于 1942-11-30 深夜（午夜前 40 分钟），
弃舰与沉没在次日，故 fate_date 取 1942-12-01。
HyperWar 舰级页的写法与之一致："on 30 Nov 42 ... and sank the following day."

### 2.9 彭萨科拉塔萨法隆加 —— 中 1 条鱼雷，重伤存活

> "Pensacola turned left to prevent collision with two damaged American ships ahead
> of her. Silhouetted by the burning American cruisers, she came in the Japanese
> line of fire. **One of 18 torpedoes launched by Japanese destroyers hit her below
> the mainmast on the portside.** Her engine room flooded, three gun turrets went
> out of commission, and her oil tanks ruptured to make a soaked torch of her mast."
> — DANFS https://www.history.navy.mil/research/histories/ship-histories/danfs/p/pensacola-iii.html

**伤亡有明确数字**（本轮唯一给出数字的一场）：
> "Her dead numbered **7 officers and 118 men**. One officer and **67 men were injured**."
> 同页。即 125 死、68 伤。

与北安普敦的对比：彭萨科拉中 1 条存活，北安普敦中 2 条沉没。同一条战列线，
相邻位置，结局相反——这是塔萨法隆加最值得写的一处。

---

## 3. 已完成 / 未完成

### 3.0 本轮补到的五项关键数据（第二轮抓取）

第一轮收尾时标「未获取」的项里有五项在第二轮补齐，来源是两份 ONI 战斗叙事：

| 补到的数据 | 值 | 来源原句 |
|---|---|---|
| **北安普敦生还数** | 773（57 军官 + 716 士兵） | "rescuing all **57 officers and 716 men**" |
| **北安普敦塔萨法隆加舰长** | Capt. Willard A. Kitts, III | "Northampton, Capt. Willard A. Kitts, 111"（原文 "III" 转录成 111） |
| **彭萨科拉中雷时刻与故障清单** | 2339 中雷；turret III 失效、两台陀螺震坏 | "At 2339 without warning a torpedo struck the port side aft, outside the fuel tank forward of turret III" |
| **亚特兰大中弹明细** | 日舰 13 发 5.5 in + 12 发 5 in；友军 19 发 8 in | "thirteen 5.5-inch hits and some 3-inch ... and twelve 5-inch from the destroyers" |
| **亚特兰大 TG 62.4 阶段** | 11-11 至 11-12 掩护三艘运输船，斯科特坐舰 | "One light cruiser (antiaircraft): Atlanta (FF), Capt. Samuel P. Jenkins" |

来源：
- https://www.ibiblio.org/hyperwar/USN/USN-CN-Tassafaronga/index.html（ONI, *The Battle of Tassafaronga*）
- https://www.ibiblio.org/hyperwar/USN/USN-CN-Guadalcanal/USN-CN-Guadalcanal-1.html（ONI, *The Battle of Guadalcanal*）

**一处必须记的更正（我原先写错、本轮自行发现）：**
北安普敦号在塔萨法隆加时的舰长**不是**中途岛时的 Capt. William Dwight Chandler，
而是 **Capt. Willard A. Kitts, III**。第一轮我写的是「塔萨法隆加时是否仍为 Chandler，
来源未给，故不写入」——现在有了答案，已在 `ships/northampton.yaml` 里改成两条独立的
`service.commander` fact。**任务书没有提到这一点，属本轮自行核实。**

**另一处需要说明的口径问题：** ONI 的塔萨法隆加叙事把参战编队称作
**"Task Force WILLIAM"**（按司令姓氏的保密代号），全文**没有出现过 "TF 67"**。
「TF 67」这个番号只有 DANFS 的彭萨科拉页给。两处不矛盾，但主会话若见到
WILLIAM 这个叫法不要当成另一支编队。

### 3.1 已完成（可合并）

| 文件 | 内容 | fact 数 |
|---|---|---|
| `classes/northampton.yaml` | 舰级：主尺度/动力/装甲 11 条/武备/5 座炮位/`weapon:8in-55-mk9`（全 22 条） | 见自检 |
| `classes/pensacola.yaml` | 舰级：同上 + `weapon:5in25-mk10`（全 19 条）/6 座炮位 | |
| `classes/atlanta.yaml` | 舰级：同上 + `weapon:21in-mk15`（全 5 条）/4 座炮位 | |
| `ships/northampton.yaml` | 单舰：建造/编制/战历/结局 | |
| `ships/pensacola.yaml` | 单舰：建造/编制/战历/十字路口/结局 | |
| `ships/atlanta.yaml` | 单舰：建造/编制/战历/沉没过程/伤亡 | |
| `sources-fragment.yaml` | 17 条新来源 | |

**自检结果（SCHEMA §10）：305 条 fact，79 个字段，0 个问题。**
自检脚本在 `_raw/selfcheck.py`，主会话可直接复跑：
```
python work/staging/tg162b/_raw/selfcheck.py
```
它检查：字段注册、unit 一致性、qual 完整性、枚举合法性、
confidence ∈ {A,B,C}、src 是否全部登记、valid.from 存在性。

### 3.2 未完成（按 SCHEMA 要求，卡住就不写）

| 项 | 状态 | 原因 |
|---|---|---|
| **三舰 35 个骨架字段的 `protection.armor.weight` / `underwater.depth`** | 未获取 | 五个来源（navypedia / DANFS / NavSource / NavWeaps / HyperWar）**全都没有给装甲总重和水下防护纵深**。不推算。 |
| **北安普敦 / 彭萨科拉的 `propulsion.fuel.capacity`** | 未获取 | navypedia 只给区间："Fuel, toil **1417 - 2108**"（北安普敦）、"**1411 - 2116**"（彭萨科拉），**两个数分别对应什么状态来源未说明**。取任一都是推断。<br>第二轮试了 ONI 识别手册（`ref/ONI/` 路径全部 404）与 ibiblio 的舰级页，都没有这个数。<br>对比：亚特兰大给的是单值 "Fuel, toil 1360"，所以那一级填了。 |
| **北安普敦的 `service.casualties`** | 未获取 | 第二轮补到了生还数（773），但**没有全舰编制数**，无法由「编制 − 生还」倒推。<br>ONI 全文那个 "19 officers and 398 enlisted men" 是 **TF WILLIAM 四艘被击中巡洋舰的合计**（含明尼阿波利斯、新奥尔良、彭萨科拉），**不能拆到北安普敦名下**。<br>DANFS 本舰条目只给定性描述 "loss of life was surprisingly light"。 |
| **三舰的 `service.fate_authority`** | 未获取 | 五个来源都只叙述结局过程，不提判定机构。整条不写。 |
| **彭萨科拉 / 亚特兰大的 `service.survivors`** | 未获取 | 两舰都有伤亡数（彭萨科拉 125、亚特兰大 172）但**无编制数/生还数**。倒推属推算，不做。 |
| **三舰中途岛时期的舰载机型号** | 未获取 | navypedia 给的机型清单是**建成态**（北安普敦 "OL, O2U, O3U"；彭萨科拉 "OL, O2U"），套到 1942 年属推断。DANFS 与 NavSource 都不给中途岛时的机型。<br>**唯一例外**：HyperWar 美军序列里有一条机队记载——"Ship Units, Cruiser Scouting Squadron 5 (VCS-5) and Cruiser Scouting Squadron 6 (VCS-6) / **20 Curtiss SOC/Naval Aircraft Factory SON (Seagull)**"——但这是 TG 16.2 **整个巡洋舰群**的合计机数，**不能拆到单舰头上**。 |
| **北安普敦的 `armament.aa_40mm.count`** | 未获取（不写 0） | navypedia 逐舰改装表里 Northampton 一行没有任何 40 mm 条目，同级 Chester/Louisville/Augusta 都有。但「表里没有」≠「装 0 门」，是推断，故留空。 |
| **亚特兰大的 `armament.aa_20mm.count`** | 有分歧，不写 | 见 §6。 |
| **亚特兰大的 `service.complement.officers`** | 未获取 | 四处来源都只给编制总数，不给军官/士兵分列。 |
| **单舰 `slices/` 与 `articles/`** | **本轮未产出** | 任务书的输出清单里没有这两项（只列了 classes / ships / sources / notes）。若主会话需要，切片边界可按本文件 §5 的战历节点直接切。 |

### 3.3 关于「装甲总重」为什么补不到

这一项值得单独说明，因为它是三舰共缺的最大一块（6 个 fact 位）。本轮试过：

| 来源 | 是否给装甲总重 |
|---|---|
| navypedia 三个级页 | ❌ 只给逐部位厚度，无总重、无占比 |
| DANFS 三个条目 | ❌ 题头只有 dp./l./b./dr./s./cpl./a. 七项 |
| NavSource 三个页 | ❌ 题头有装甲厚度（"3 3/4" Belt, 2 1/2 Turrets, 1" Deck"），但无总重 |
| NavWeaps 炮页 | ❌ 不涉舰体防护 |
| HyperWar 舰级页 | ❌ 只给厚度 |
| ONI 战斗叙事 | ❌ 不涉 |

**NavSource 的装甲行还提供了一个 navypedia 没有的换算口径**，
值得记下来供主会话判断：
- 北安普敦："Armor, **3 3/4" Belt, 2 1/2 Turrets, 1" Deck, 1 1/4 Conning Tower**"
  → 95 mm 带 / 64 mm 炮塔 / 25 mm 甲板 / 32 mm 指挥塔
- 彭萨科拉："Armor, **4" Belt, 2 1/2 Turrets, 1" Deck, 1 1/4 Conning Tower**"
  → 102 mm 带 / 64 mm 炮塔 / 25 mm 甲板 / 32 mm 指挥塔
- 亚特兰大："Armor, **3 3/4" Belt, 1 1/4 Turrets, 1 1/4" Deck, 2 1/2" Conning Tower**"
  → 95 mm 带 / 32 mm 炮塔 / 32 mm 甲板 / 63 mm 指挥塔

**这三行与 navypedia 的逐部位厚度基本吻合**（英制取整），
是本轮用来交叉验证装甲数字的第三源。
**注意彭萨科拉那条 "4" Belt"**：4 in = 101.6 mm ≈ 102 mm，
对应 navypedia 的「弹药库段 102 mm」——NavSource 只写了最厚的那个数，
**没有区分机舱段 64 mm**。这是「单一装甲带数值」与「分段装甲带」的口径差别，
不是数据冲突，主会话不要当成两源打架。

---

## 4. 装甲数字的拆法（避免主会话误读）

navypedia 用「甲: A - B」这种双值写法，**本文件一律按 navypedia 自己的正文拆开**，
没有取平均、没有取上限当唯一值。

| 项目 | 北安普敦级 | 彭萨科拉级 | 亚特兰大级 |
|---|---|---|---|
| 装甲带（机舱段） | **76** | **64** | 95（+16 mm STS） |
| 装甲带（弹药库段） | **95** | **102** | 前 28 / 后 95-46 |
| 装甲甲板（机舱） | 25 | 25 | 32 |
| 装甲甲板（弹药库） | 51 | 45 | — |
| 炮座环 | 38 | **19** | — |
| 炮塔 | 面 64 / 侧 25 / 后 19 / 顶 51 | 面 64 / 侧 25 / 后 19 / 顶 51 | 32-25 |
| 指挥塔 | 32 | 32 | 63 |

**两个重巡级的机舱/弹药库分配是完全相反的**：
北安普敦级 **机舱 76 < 弹药库 95**，彭萨科拉级 **机舱 64 < 弹药库 102**——
两级的弹药库都比机舱厚，但彭萨科拉级的弹药库更厚、机舱更薄。
**不要互换这两组数字。**

亚特兰大级的前后弹药库差得最极端（**前 28 vs 后 95-46**），
这是本级设计上最容易被忽略的一处。

---

## 5. 炮位方位：三处「来源没给、本站不得不做选择」的地方

SCHEMA 要求 `mount.position` 是枚举单值，但来源往往只给描述性说法。
以下三处是本轮**做了选择但不是来源原话**的地方，逐条列出以便主会话复核：

### 5.1 北安普敦级三座三联的方位

`classes/northampton.yaml` 里 `mount:northampton-triple-8in` 的 `position`
写了 `superfiring_fore`。
**来源只给了座数，没有逐座给方位**：NavWeaps "Northampton (3)"、
navypedia "3 x 3"。本级「前二后一」是从同级的常规布置推的，**属推断**。
本站在 note 里明确标注「逐座方位标为未获取」。

### 5.2 彭萨科拉级三联座的方位

navypedia 原句 "**end twin turrets and superfiring triple ones**"——
清楚的只有「双联在两端、三联是背负」。
**没有说清三联是「前部背负」还是「首尾各一背负」。**
本文件取 `superfiring_fore`，属**部分推定**。
另一种读法（前后各一）在本 note 保留。

### 5.3 彭萨科拉级双联座的方位

同一句 "end twin turrets"——双联在**两端**（首、尾）。
`mount.position` 只能填一个值，故填 `fore` 并在 note 里说明尾部的另一座。

---

## 6. 有争议的记载（并列不裁决）

### 6.1 亚特兰大有无 20 mm 炮 —— 两源直接冲突

**navypedia 说没有：** 逐舰武备行把 CL-51/52 与 CL-53/54 分开列，
CL51/52 行是 "8 x 2 - 127/38 Mk 12, 3 x 4 - 28/75 Mk 1, 2 x 4 - 533 TT, 2 DCR"
——**无 20 mm**；CL53/54 行才有 "8 x 1 - 20/70 Mk 4"。
https://www.navypedia.org/ships/usa/us_cr_atlanta.htm

**NavSource 说有 8 门：** 题头武备行
"Armament 16 x 5"/38AA, 16 x 1.1", 16 x 40mm, **8 x 20mm**, 8 x 21" tt."
https://navsource.net/archives/04/051/04051.htm

**本处理的处置**：`armament.aa_20mm.count` 整条不写（既不写 0 也不写 8）。
按红线「有分歧单列、不自己裁决」。

### 6.2 NavSource 的亚特兰大武备行整体不可靠

同一行还写了 **"16 x 40mm"**。但本级 40 mm 是 **1943 年以后**在
CL-95 起的改进型上换装的（navypedia "CL95: 6 x 2 - 127/38 Mk 12,
8 x 2 - 40/56 Mk 1.2, 14 x 1 - 20/70 Mk 4"）；
**CL-51 在 1942-11-13 就沉了，从未装过 40 mm。**
所以 NavSource 这一行是把本级多艘舰、多个年代的配置**混编**在一起的，
不能按单舰建成态读。本站在 `sources-fragment.yaml` 的 note 里标注了这点。

### 6.3 航速：每艘舰 3-4 个不同数字

| 舰 | DANFS | navypedia | NavSource | HyperWar 舰级页 |
|---|---|---|---|---|
| 北安普敦 | 32.5 | 32.5 | **32.7** | 32.5 |
| 彭萨科拉 | **32** | 32.5 | 32.5 | 32.5 |
| 亚特兰大 | **33.6** | 32.5 | 32.5 | **32** |

亚特兰大另有设计目标 35 节，且来源明说从未达到：
> "Ships were considerable overloaded: on lead-ship CL51 it was above 700t,
> and **designed 35kts speed was never reached.**"
> — https://www.navypedia.org/ships/usa/us_cr_atlanta.htm

**本处理**：取 navypedia 值（`propulsion.speed.design`），其余并列写进 note。

### 6.4 排水量：四源四值

| 舰 | DANFS 题头 | navypedia standard | NavSource | HyperWar 舰级页 |
|---|---|---|---|---|
| 北安普敦 | 9,050（口径未述） | **9,006** | 9,300 | 13,100 |
| 彭萨科拉 | 9,100（口径未述） | **9,097** | 9,100 | 9,100（**自述 normal**）/ 11,512 full |
| 亚特兰大 | 6,000（口径未述） | **6,590** | 6,000 | 8,200 |

**只有 navypedia 自述是 standard**，故 `displacement.standard` 只登记 navypedia 值。
**注意彭萨科拉**：HyperWar 舰级页明确把 9,100 标为 `normal` 而不是 `standard`——
即 9,100 与 9,097 不是同一口径的两个测量，**不能相减**。

### 6.5 编制：亚特兰大与彭萨科拉都出现近两倍的差异

| 舰 | DANFS | navypedia | NavSource | HyperWar 舰级页 |
|---|---|---|---|---|
| 北安普敦 | **621** | 617（CA26-28） | 621 | **1,155** |
| 彭萨科拉 | **653** | 631 | 635 | **1,113 - 1,135** |
| 亚特兰大 | **810** | 623 | 650 | **820** |

**HyperWar 舰级页那一列的两个数（1,155 / 1,113-1,135）比其他三源高出近一倍**，
疑为战时加强编制或误植。本站在 note 里并列记录，但**没有采用**，
也没有据此改任何 fact。

### 6.6 亚特兰大命中数：19 发 8 英寸 vs 约 50 发大口径

**DANFS 长稿：**
> "Atlanta reeled under the impact of a flurry of **what was estimated as 19 8-inch
> hits** when San Francisco, 'in the urgency of battle, darkness, and confused
> intermingling of friend or foe' fired into her."
— https://www.ibiblio.org/hyperwar/USN/ships/dafs/CL/cl51.html

**DANFS 简史页：**
> "the cruiser built to fight planes, destroyers and submarines had taken at least
> one torpedo and **approximately 50 major-caliber hits including several from
> battleship Hiei**."
— https://www.ibiblio.org/hyperwar/USN/ships/dafs/CL/cl51-history.html

**两说并列不裁决。** 注意长稿自己加了 "what was estimated as"（估计值），
简史页用的是 "approximately"（约数）——**两个来源自己都标注了不确定**。
后者把日舰比叡的命中算进来，前者只算旧金山号的 8 英寸，统计范围不同。

### 6.7 彭萨科拉结局：scuttled 还是 sunk as target

**navypedia：** "Pensacola was finally **scuttled** 10.11.1948"
**NavSource：** "Fate: **Sunk as target** on 10 NOV 1948 off the coast of Washington."

注册表 `construction.fate_type` 里 `expended_as_target` 与 `scuttled` 是两个不同值。
**本站取 `expended_as_target`**，理由是 NavSource 的 "as target" 更具体，
且 navypedia 同句自己先说 "Both ships were **used as targets** in nuclear tests in 1946"。
**这个选择是为了可复核而写出的，不是裁决。**

### 6.8 彭萨科拉掷瓶人中间名首字母

NavSource 的报纸剪报图注同一页出现两个写法：
"Mrs. **Josephine L.** Seligman" 与 "Mrs. **Josephine K.** Seligman"。
DANFS 写 "Mrs. Joseph L. Seligman"（用丈夫名）。
**并列不裁决。**

### 6.9 亚特兰大的舰种：CLAA 还是 CL

**ONI 战斗叙事把本舰归为 CLAA：**
> "United States losses were as follows: ... **CLAA  2 (Atlanta, Juneau)**  0"
> — https://www.ibiblio.org/hyperwar/USN/USN-CN-Guadalcanal/USN-CN-Guadalcanal-1.html

**但本舰的舷号是 CL-51、从未改过 CLAA**，理由是它在 1942-11-13 就沉了，
而本级改 CLAA 是 1949-03 的事（navypedia 舰名栏
"CL53, 3.1949- CLAA53" 这类记录，CL-51 一栏只写 "CL51"）。

**本处理的处置**：`identity.ship_type` 取 `light_cruiser`（注册表枚举无
anti_aircraft_cruiser），把 CLAA 这个说法写在 note 里，不改枚举值。
ONI 用的是**职能分类**（防空巡洋舰），navypedia 用的是**舷号序列**，
两者不矛盾——一艘 CL 可以是防空巡洋舰，只是当时还没有 CLAA 这个舷号前缀。

### 6.10 彭萨科拉失效炮塔数：3 座 vs 1 座

**DANFS：** "Her engine room flooded, **three gun turrets went out of commission**"
**ONI：** "flooded magazines and fires rendered **turret III useless**"（只点名 1 座）

**两说并列不裁决。** ONI 记的是直接损毁（III 号塔及其弹药库），
DANFS 的 3 座可能包含动力/通信中断导致的间接失效。
本站在 `armament.gun_failures` 里如实写了两边。

### 6.11 亚特兰大中弹数：三个数字不能相加

| 来源 | 数字 | 统计范围 |
|---|---|---|
| ONI | 13 发 5.5 in + 若干 3 in + 12 发 5 in | **日舰打的**（中雷前） |
| ONI | 19 发 8 in | **旧金山号误击**（中雷后） |
| DANFS 简史页 | 约 50 发大口径（含比叡） | **全部**，含日舰所有口径 |
| DANFS 长稿 | 估计 19 发 8 in | 只算旧金山号那一阵 |

**这四个数字的统计范围互不相同，不能相加成「总中弹 N 发」。**
本站在 `armament.gun_failures` 里按「日舰 / 友军」分开记，
在 `service.fate_category` 里把 DANFS 的两说并列。

---

## 7. 5"/25 与 5"/38 的区别（`docs/32` 那条纠正的技术依据）

任务书提到 `docs/32` 已记录纠正：「七艘重巡装 5"/25，只有亚特兰大装 5"/38」。
**本轮从炮本身的角度确认这条纠正成立**，依据是两页 NavWeaps 的并列数据：

| | 5"/25 Mk 10（重巡副炮） | 5"/38 Mk 12（亚特兰大主炮） |
|---|---|---|
| 倍径 | 25 | 38 |
| 膛线长 | 125 in (3.175 m) | 190 in (4.826 m) |
| 弹重 | HC Mk 36: 53.85 lb (24.43 kg) | AAC Mk 34: 55.18 lb (25.0 kg) |
| 初速 | 2,155 fps (657 mps) | 2,600 fps (792 mps) 新炮 / 2,500 平均 |
| 射速 | 15-20 发/分 | 12-15（无整体扬弹机）/ **15-22**（有整体扬弹机的基座炮座） |
| 炮座仰角上限 | -15 / **+85**（Mark 17/19/23/27） | -15 / **+85**（双联除 Mark 22） |
| 炮座俯仰/旋回 | **Mark 19 为纯手动** | 15-18 度/秒（动力） |
| 火箭药 | 9.6 lb (4.35 kg) SPD | 全装药 |

来源：https://www.navweaps.com/Weapons/WNUS_5-25_mk10.php
和 https://www.navweaps.com/Weapons/WNUS_5-38_mk12.php

**关键差别不在仰角**（两者都能到 85°），而在：
①倍径与初速（657 vs 792 mps，弹道平直度差很多）；
②**炮座驱动方式**——重巡的 Mark 19 是**手动**俯仰与旋回
（NavWeaps 两栏都写 "Manual operation, only"），
亚特兰大的 Mark 29 是动力驱动 15 度/秒。
**手动炮座跟不上 1942 年的高速目标**，这才是亚特兰大级存在的理由。

**注意**：本级 5"/25 用 Mark 19 炮座这一点，
NavWeaps 炮座表的原文是 "Cruisers / Pensacola (4), **Northampton (8)**, Portland (8)
and New Orleans (except Quincy and Vincennes) (8): **Mark 19**"。
彭萨科拉括注是 4（建成时），北安普敦是 8——**这两个数不是同一时点的座数**，
彭萨科拉 1941 年才加到 8 座。本站在两级文件的 note 里分别标注了。

---

## 8. 亚特兰大级没有水上飞机（不是「查不到」，是「没有」）

navypedia 的三个级页对比很干净：

- 北安普敦：`"Armament 3 x 3 - 203/55 ..., 4 x 1 - 127/25 ..., 2 x 3 - 533 TT,
  **2 catapults, 4 seaplanes** (OL, O2U, O3U)"`
- 彭萨科拉：`"... 2 x 3 - 533 TT, **2 catapults, 4 seaplanes** (OL, O2U)"`
- 亚特兰大：`"Armament CL51, 52: 8 x 2 - 127/38 Mk 12, 3 x 4 - 28/75 Mk 1,
  2 x 4 - 533 TT, 2 DCR"` ——**无 catapults、无 seaplanes**

**所以 `classes/atlanta.yaml` 的 aviation 组一条 fact 都不写。**
这不是漏采：两个重巡级的武备行都明确带弹射器与水上飞机，
亚特兰大级的武备行从头到尾（CL51 到 CL121）都没有。
写成 `aviation.aircraft.capacity: 0` 会被读成「设计上能带但实载零」，
与实际「没有航空设施」不是一回事，故留空并在本文件说明。

---

## 9. 一处需要主会话裁决的数据取舍（HyperWar 舰级页的编制数）

`ibiblio.org/hyperwar/USN/ships/` 下的舰级页（如 `CA/CA-26_Northampton.html`）
给了一组**与所有其他来源都不一致**的数据：

| 舰 | HyperWar 舰级页 | 其他三源 |
|---|---|---|
| 北安普敦 | Displacement 13,100 t / Complement 1,155 / Armament "3x3 8"/55, 4x2 5"/25, 6 21" tt." | 9,006-9,300 t / 617-621 / 副炮 8 门（1942 年） |
| 彭萨科拉 | 9,100 normal / 11,512 full / Complement 1,113-1,135 / "4 5"/25, 7x4 40mm, 28x1 20mm" | 9,097 / 631-653 / 1942 年无 40 mm |
| 亚特兰大 | 8,200 t / Complement 820 / "16 5"/38, 3x2 40mm, 1x4 40mm, 15 20mm" | 6,590 / 623-650 / 无 40 mm |

**三类不一致，模式很清楚：**
1. **排水量**：北安普敦的 13,100 t 明显是**满载**当成了标准值；
   亚特兰大 8,200 与之类似。
2. **编制**：1,155 / 1,113-1,135 / 820 全部偏高，疑为战时加强编制。
3. **武备**：彭萨科拉页写 "7x4 40mm, 28x1 20mm"、亚特兰大页写 "3x2 40mm, 1x4 40mm,
   15 20mm"——**这些是 1945 年（彭萨科拉）与改进型（亚特兰大）的配置**，
   不是建成态，也不是 1942 年状态。

**本轮的处置：HyperWar 舰级页只用于交叉核对日期与主尺度，
不用它支撑任何一条 fact。** 但它的数据性质（把后期改装态/满载值当题头）
值得主会话知道，因为本站已有的其他舰级（如企业号）也引过 HyperWar。

---

## 10. 交付摘要

| 项 | 数量 |
|---|---|
| 舰级文件 | **3**（northampton / pensacola / atlanta） |
| 单舰文件 | **3**（northampton / pensacola / atlanta） |
| 切片文件 | **0**（任务书输出清单未列，见 §3.2） |
| 正文文件 | **0**（同上） |
| 新登记来源 | **19** |
| fact 总数 | **310**（自检 0 问题） |
| 新建武器实体 | **3**：`weapon:8in-55-mk9`（美军 8"/55，与站内英制 `8in-50-mk8` 不是同一门）<br>`weapon:5in25-mk10`（美军 5"/25）<br>`weapon:21in-mk15`（美军 21" Mark 15 鱼雷） |
| 复用的既有武器实体 | 4：`weapon:5in38-mk12`、`weapon:11in75-mk1`、`weapon:20mm-oerlikon`、`weapon:40mm-bofors` |
| 新建炮位实体 | **15**（北安普敦 4 / 彭萨科拉 6 / 亚特兰大 4 / 共用 1） |

### 卡住的地方

见 §3.2 与 §3.3 的详表。按 SCHEMA 要求**整条不写**，不填 0、不推算、不跨来源拼凑。
第二轮补到了五项（见 §3.0），仍缺的主要是：

- **装甲总重 / 水下防护纵深**（六源全无，§3.3 有逐源排查表）
- **两个重巡级的燃油装载量**（来源只给区间，不给状态对应；ONI 手册路径 404）
- **北安普敦阵亡数**（生还 773 有了，但无编制数；ONI 的 19+398 是四舰合计不可拆）
- **彭萨科拉/亚特兰大的生还数**（有伤亡数但无编制数）
- **中途岛时期的三舰舰载机**（navypedia 只有建成态机型）

### 有争议的记载

见 §6，共 11 组。最需要注意的四组：
1. **亚特兰大 20 mm**（navypedia 无 vs NavSource 8 门）——整条不写
2. **亚特兰大中弹数**（13+12 日舰 / 19 友军 / 约 50 全部）——统计范围不同，不可相加
3. **彭萨科拉失效炮塔**（DANFS 3 座 vs ONI 1 座）——两说并列
4. **HyperWar 舰级页与所有其他来源的系统性不一致**（排水量/编制/武备全部偏高或错代）

### 三处必须让主会话看到的结构性提醒

1. **`weapon:8in-55-mk9` 与站内已有的 `weapon:8in-50-mk8` 不是同一门炮。**
   后者是英国 8"/50 Mk VIII（郡级），前者是美国 8"/55（彭萨科拉/北安普敦）。
   **id 里一个 50 一个 55 就是倍径**，不要合并。
2. **亚特兰大主炮是 8 座双联 = 16 门**，
   这既是 `docs/32` 那条纠正的具体内容，也是本轮最容易写成 8 门的地方。
3. **北安普敦 1942 年没有鱼雷管**（1931 年已拆）。
   「本级有鱼雷管」这句话必须带年份限定，否则会与中途岛/塔萨法隆加的描述冲突。

### 一处任务书没提、本轮自行发现的换人

**北安普敦号的舰长在 1942-06 与 1942-11 之间换过人：**
中途岛时是 Capt. William Dwight Chandler（NavWeaps 序列），
塔萨法隆加时是 **Capt. Willard A. Kitts, III**（ONI 战斗叙事）。
若正文写「Chandler 指挥本舰战沉」就是错的。

对照片：**彭萨科拉号的舰长同期未换**，两处都是 Capt. Frank L. Lowe
（NavWeaps 序列 + ONI 战斗叙事双源确认）。

