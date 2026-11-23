# 调研底稿：美国海军三艘驱逐舰（Hammann / Monaghan / Benham）

> 组名 `us-dd` · 2026-11-23 至 2026-11-24 · 为 Dockyard 二战战舰资料站中途岛专题
>
> 本文件是分片的底稿：每条结论给**英文原句 + URL**。
> 分片本身在 `work/staging/us-dd/classes/` 与 `ships/`。

---

## 0. 抓取方式与站点可用性（实测记录）

`web_fetch` / `research` 按任务书要求完全未用。全程用 Python `urllib` + `User-Agent`，
脚本留在 `_raw/fetch.py`（直连）、`_raw/wb.py`（Wayback 兜底）、`_raw/txt.py`（HTML→文本）。

| 站点 | 直连结果 | 处理方式 |
|---|---|---|
| `navypedia.org` | **通** | 直连抓取 |
| `destroyerhistory.org` | **通** | 直连抓取 |
| `navweaps.com` | **通** | 直连抓取 |
| `combinedfleet.com` | **通** | 直连抓取 |
| `history.navy.mil` | **TLS 握手失败** `SSL: UNEXPECTED_EOF_WHILE_READING` | 全部走 Wayback 快照（`id_` 原始内容模式） |
| `navsource.org` | **TLS 握手失败**（http 则 502 / 连接重置） | 全部走 Wayback 快照 |
| `ibiblio.org/hyperwar` | 试了两个 URL 均 404 | 放弃；本轮未从该站取到任何内容 |

Wayback CDX 接口本身也有 429/503 限流，靠 `_raw/wb.py` 里的重试退避解决。
**每一份 Wayback 快照的时间戳都写进了 `sources-fragment.yaml` 的 note**，便于复核。

---

## 1. 交付摘要

| 项 | 数量 | 文件 |
|---|---|---|
| 舰级文件 | 3 | `classes/sims.yaml`（80 fact）/ `classes/farragut.yaml`（78）/ `classes/benham.yaml`（72） |
| 单舰文件 | 3 | `ships/hammann.yaml`（31）/ `ships/monaghan.yaml`（34）/ `ships/benham.yaml`（31） |
| 状态切片 | 0 | **未做**，见下方说明 |
| 正文文件 | 0 | **未做**，见下方说明 |
| 新登记来源 | 20 | `sources-fragment.yaml` |
| fact 总数 | 326 | 自检脚本 `_raw/selfcheck.py` 输出 |
| SCHEMA §10 自检 | **通过，0 error / 0 warning** | 同上 |
| 分歧组（两说并列） | 5 组，每组双方都写了 note | `_raw/disputes.py` 输出 |
| 同源自相矛盾 | **0** | 同上 |

**关于切片与正文**：任务书的「输出」清单只列了 7 个文件，不含 `slices/` 与 `articles/`，
故本轮未产出。但改名时发现时间轴信息量很大（三舰各有 4-6 个可切片的配置节点，
原句均已逐条抄进各单舰文件的 note），若主会话要补，材料是齐的：

- Hammann：建成 1939-08 → 1940 夏拆鱼雷管 → 1941 夏拆 5 号炮 → 1941 末换 20 mm → 1942 初改深弹 → 1942-06 沉没
- Monaghan：建成 1935-04 → 1941 中加深弹滑轨 → 1942 年 5-9 月拆 No.3 炮 + 8 门 20 mm → 1942 末加 40 mm → 1944-12 沉没
- Benham：建成 1939-02 → 中立巡逻期 → 1941 年其余八舰改装（本舰未动）→ 1942 初本舰专属改装 → 1942-11 沉没

---

## 2. 任务书史实核实结果

> 按 SCHEMA §9.3：任务书里的史实陈述一律当「待核实」，不符则以来源为准并指出错在哪。

### 2.1 【重大】「Hammann 沉没时是唯一在场的驱逐舰」——**不成立**

任务书原文：「我此前写过『沉没时唯一在场的驱逐舰』，这个说法我无法用作战序列证实。」

**核实结论：这句话在「周围只有她一艘」的意义上是错的。** 四份独立来源同时否定它：

**证据一｜一手，Hammann 自己的行动报告，第 7 节**
<https://www.history.navy.mil/research/archives/digital-exhibits-highlights/action-reports/wwii-battle-of-midway/uss-hammann-action-report.html>

> "About 0400, sighted Yorktown, screened by Hughes, Gwin and Monaghan, about 8 miles on
> starboard beam. Changed course to join this screen and continue screening till daylight."

> "Upon completion, Hammann, Balch, and Benham, designated as Taskgroup 17.5,
> Captain BUCKMASTER, set course 285° T. speed 16 knots to return to Yorktown."

**证据二｜一手，约克城号行动报告，1942-06-06 段**
<https://www.history.navy.mil/research/archives/digital-exhibits-highlights/action-reports/wwii-battle-of-midway/uss-yorktown-action-report.html>

> "The other five destroyers, Balch, Benham, Gwin, Anderson, and Monaghan, under the command
> of Commander Destroyer Squadron SIX, Captain E.P. Sauer, USN, formed anti-submarine and
> anti-aircraft screen around Yorktown at a distance of about 2,000 yards, speed 14 knots."

**证据三｜官方舰史，DANFS Vireo**
<https://www.history.navy.mil/research/histories/ship-histories/danfs/v/vireo-i.html>

> "Accordingly, Vireo received a summons to take Yorktown in tow. The tug arrived on the scene
> by 1135 on 5 June and closed and maneuvered to pass Yorktown a towline, accomplishing this
> by 1308. Vireo and her unwieldy charge then labored painfully ahead, at a speed of under
> 3 knots, with a protective brood of destroyers standing by."

> "The next day, Hammann (DD-412) secured alongside Yorktown to assist the salvage parties on
> the larger ship working to correct her trim and to repair her battle damage."

**证据四｜日方视角，combinedfleet.com I-168 TROM**
<https://www.combinedfleet.com/I-168.htm>

> "As he closes, he sees six destroyers circling a mile away. The minesweeper VIREO has
> YORKTOWN in tow."

**准确的表述应当是**：

- Hammann 是**唯一靠在约克城号舷侧（moored alongside）**的舰——这是对的，且一手战报反复写
  "the Hammann was moored portside to the Yorktown"、"Hammann came in and moored alongside
  Yorktown forward"。
- 但她周围 2,000 码的屏护圈上还有 **Balch、Benham、Gwin、Anderson、Monaghan** 五艘驱逐舰，
  另有拖船 **Vireo（AT-144，原 AM-52）** 用拖缆拖着约克城号。
- 因此「唯一在场的驱逐舰」若不改口，至少要与四份来源同时冲突。

**建议写法**：「Hammann 是当时唯一贴靠约克城号舷侧提供消防水、电力与排水泵的舰；
屏护圈上另有五艘驱逐舰，约克城号本身则由拖船 Vireo 拖带。」

### 2.2 【更正】Benham 的结局不是「战沉」，官方叙述是「被日军鱼雷致残后由友舰炮火击沉」

任务书原文：「1942-11 瓜岛海战受损后自沉（**待核实具体经过**）」。

**核实结论：「受损后自沉」这个方向对，但「自沉」二字需要限定**——不是开阀通海，
而是**舰体自行裂成两段后，两个浮体由友舰的 5 英寸炮火打沉**。

DANFS 原句：

> "Because of heavy debris forward, Benham made little headway. Despite exhaustive damage
> control efforts, worsening seas progressively weakened the destroyer's hull; and, after she
> slowly split in half, the crew transferred to Gwin late on the 15th. Benham's two floating
> sections were then sunk by 5-inch gunfire off the south coast of Guadalcanal at 1938 on
> 14 November 1942."

受损经过：

> "Then, at 2338, Japanese torpedoes began to score, mortally damaging Walke with a hit forward.
> At the same time, another torpedo struck Benham on her starboard side, blowing off her bow
> back to gun mount number one."

**注意 DANFS 这一段本身时序矛盾**：先说「15 日晚些时候」人员转移，后说「14 日 1938 击沉」。
两说并列，分片里不裁断（见 §3.2）。

**另有一条与任务书无关但值得记的**：本舰全员生还——

> "Interestingly, the man washed overboard during the battle was later rescued by Meade (DD-602),
> so that Benham's entire crew survived her sinking."

### 2.3 【确认】Monaghan 属 DesRon 1、中途岛护卫企业号——**成立**

两份来源，其中一份是一手战报编成表：

<https://www.history.navy.mil/research/library/online-reading-room/title-list-alphabetically/c/composition-of-us-forces.html>

> "Task Group 16.4 — Destroyer Screen
> Capt. Alexander R. Early, USN
> Commander Destroyer Squadron 1 (ComDesRon 1)
> USS Phelps (DD-360) / USS Worden (DD-352) / USS Monaghan (DD-354) / USS Aylwin (DD-355)"

DANFS 佐证：

> "Through the first two days of the Battle of Midway on 3 and 4 June 1942, Monaghan screened
> Enterprise, faithfully keeping station on the carrier as she launched planes in the desperate
> fighting."

### 2.4 【确认】Benham 属 DesRon 6、中途岛护卫企业号、后加入 TF 17——**成立**

一手，DesRon 6 作战报告第 1 节：

<https://www.history.navy.mil/research/archives/digital-exhibits-highlights/action-reports/wwii-battle-of-midway/commander-destroyer-squadron-six-action-report.html>

> "At 1434, June 4, 1942, Commander Task Force SIXTEEN directed Vincennes, Pensacola, Balch
> (Commander Destroyer Squadron SIX), and Benham to proceed to he aid of Task Force SEVENTEEN
> which shortly before had been under a heavy Japanese dive bombing attack. ... At 1522 the above
> unit joined Task Force SEVENTEEN and augmented screening circle around Yorktown, distance
> 2000 yards at speed 20 knots."

编成表旁证：DesRon 6 属下 Balch / Conyngham / Benham / Ellet / Maury（TG 16.4）。

### 2.5 【更正】「法拉格特级是老式 4 烟囱驱逐舰」——**查不到支持，来源只支持两根烟囱**

任务书原文：「法拉格特级是老式 4 烟囱驱逐舰」。

本组三份独立来源给出的都是**两根烟囱**：

- **destroyerhistory-farragut**（本级专页）：
  > "Their original armament consisted of five 5-inch/38 caliber guns—two forward, two aft,
  > and the No. 3 mount **abaft the second stack**—plus eight 21-inch torpedo tubes..."
- **NavSource DD-348**（首舰）图注：
  > "Farragut (DD-348) steaming in harbor, 14 March 1938. Note the colored band and the red
  > Engineering Excellence 'E' painted on her **after smokestack**."
- **navypedia-farragut** 项目史（谈本级相对前代的变革）：
  > "There was a full withdrawal from the ideas included in **'flushdeckers'**: all armament
  > placed in a centreline, flushdeck hull was refused in favour of more traditional with a
  > forecastle."

四烟囱是一战平甲板型（Wickes / Clemson）的特征；**法拉格特级正是取代它们的那一代**，
1931 年设计、1935 年完工。把「四烟囱」安在本级头上，是把前一代的外形特征错移到下一代。

**建议写法**：「法拉格特级是美军第一代条约型 1,500 吨驱逐舰，双烟囱、高艏楼船型，
用来取代四烟囱的平甲板型。」

### 2.6 【补充，非更正】西姆斯级的炮座型号**已查到明确分型**

任务书原文：「西姆斯级的炮座型号待核实」。

navweaps 的 5"/38 条目 Mount/Turret Data 表分两行列得很清楚：

<https://www.navweaps.com/Weapons/WNUS_5-38_mk12.php>

> "Single Enclosed Base Ring Mounts — **Sims (3) Mark 30: Mods 0 and 2 [mounts 1, 2 and 5]**"

> "Single Open Base Ring Mounts — **Sims (2), Benson (2) and Gleaves (2): Mark 30 Mod 1
> [mounts 3 and 4]**"

即：**五座炮位 = 三座封闭式（1、2、5 号）+ 两座敞开式（3、4 号），全部是 Mark 30 系列。**
三舰的分型对照（同一份表）：

| 级 | 封闭式（前部等） | 敞开式（后部） |
|---|---|---|
| Farragut（5 门） | 无 | Mark 21 × 5 |
| Benham（4 门） | Mark 30 Mods 0/2 × 2（bow） | Mark 30 Mod 1 × 2（stern） |
| Sims（5 门） | Mark 30 Mods 0/2 × 3（mounts 1/2/5） | Mark 30 Mod 1 × 2（mounts 3/4） |

### 2.7 【确认】Monaghan 的损失性质不是战沉——**成立，且比「台风」更精确**

> "Monaghan rolled to starboard at least six times and on her final roll continued and capsized.
> The typhoon violently ripped off most of the ship's bridge."

> "The fueling day was the first of the typhoon that claimed the lives of 790 men, sank **Hull,
> Monaghan, and Spence (DD-512)**, and seriously damaged 21 ships."

即她是同一次台风（1944-12-18，菲律宾以东）中被刮沉的三艘驱逐舰之一。
`construction.fate_type` 填 `wrecked`，**不填 `sunk_by_enemy`**。

---

## 3. 有争议的记载（两说并列，不裁决）

### 3.1 续航力：三舰全部出现 6500 vs 5640 / 5980 / 7800 的两源分歧

| 舰级 | navypedia 与 NavSource | destroyerhistory（引 Friedman） | 差 |
|---|---|---|---|
| Sims | 6,500 nm @ 12 kn | 5,640 nm @ 12 knots | 860 nm |
| Farragut | 6,500 nm @ 12 kn | 5,980 nm @ 12 knots | 520 nm |
| Benham | 6,500 nm @ 12 kn | 7,800 nm @ 12 knots | 1,300 nm |

destroyerhistory 三处都在同一页给了不同的数，且都注脚 3 = Friedman。
**本站无法判定差别来源**（可能是「设计值 vs 实测值」或「不同燃油装载」），
故分片里两个值都写、各带自己的 src。

### 3.2 Benham 的沉没日期与性质：14 日 vs 15 日；DANFS 自己内部矛盾

同一份 DANFS 文档内：

> "…the crew transferred to Gwin **late on the 15th**."（人员转移 → 15 日）
> "…sunk by 5-inch gunfire … at 1938 on **14 November 1942**."（击沉 → 14 日）

NavSource 与 navypedia 都写 11-15。分片按多数取 `fate_date: 1942-11-15`，
但 DANFS 的 14 日原句原样保留在 note 里。

### 3.3 Hammann 阵亡人数：80 / 81 / 107 三个数

- DANFS：「bringing the toll in dead to over 80」→ 取 80
- NavSource：「80 of her crew were lost with the ship」
- 一手战报第 9 节分解：「two officers were known dead and seven missing, twenty five men were
  known dead and forty seven missing」→ (2+7)+(25+47) = **81**
- 同一段又说在 Benham 上伤重不治 26 人 → 若计入则为 **107**
- 日方 combinedfleet：「kill 81 of her 241-strong crew」→ 81

分片两个值都写（80 与 81），107 写在 note 里说明它是「含 Benham 上不治者」的口径。

### 3.4 Benham 沉没时刻：美方 1536 vs 日方 1331

美方战报用 `Zone plus ten`（GMT+10），日方用 JST（GMT+9）。
即使按 1 小时时差换算，1331 JST = 1431 GMT+10，仍比美方记录的 1536 早一小时。
**两方时刻并列，不裁断**——时区之外可能还有一方记录误差。

### 3.5 法拉格特级锅炉厂牌：Yarrow（navypedia）vs Bethlehem（destroyerhistory）

- navypedia：「4 **Yarrow** boilers」
- destroyerhistory：「4 x **Bethlehem Shipbuilding Corporation, Ltc.** boilers」

两者可能都对但指的不是同一件事（Bethlehem 是设计方；Yarrow 是锅炉型式名）。
分片把两条都写进 `propulsion.boiler.type`，**这会让校验器报一条 dispute，是预期行为**。

### 3.6 Benham 级锅炉数：3 vs 4，且 destroyerhistory 自己前后矛盾

同一份 destroyerhistory 页面：

- **技术行**：「Propulsion machinery: **4 x Babcock & Wilcox boilers**; 400 psi, 645° F.」
- **正文**：「the Benhams had **three boilers at 565 psi** instead of the Bagley class' four at
  400 psi, and thus did not need the Bagleys' prominent boiler uptakes」

navypedia 两处都独立给 3：

- 技术行：「3 Babcock & Wilcox boilers」
- 项目史：「with **three bigger boilers**」＋「Thanks to presence of only **three smoke pipes
  trunked to a funnel**, its size was less, in comparison with previous class.」

分片取 **3**，并采用正文的 **565 psi**（技术行的 400 psi 与「4 锅炉」同属那一行，整行判为排版错误）。
**这一条留给主会话复核：若日后拿到 BuC&R General Information book 原页，应优先于所有二手来源。**

### 3.7 Benham 级航速：38.5 节（navypedia + NavSource）vs 36.5 节（destroyerhistory）

两值差 2 节，分片都写。

### 3.8 Sims 级功率：50,000 shp（navypedia + destroyerhistory）vs 52,000 shp（NavSource）

分片都写。

### 3.9 Sims 级鱼雷管：建成 12 管 vs 8 管

- navypedia：DD409-413 建成 **3 座四联（16 枚备雷）**，DD414-420 **2 座四联**
- DANFS / NavSource / destroyerhistory：一律写 **8 管（2×4）**

分片把「建成 12 管（仅前五艘）」记在舰级，把「1940 夏减为 8 管」记在舰级改装年表与 Hammann 单舰里。
**这不是矛盾，是「建成态」与「服役态」的差别**；但若主会话的页面只显示舰级值，
读者会看到 12 与各单舰的 8 并存，建议在舰级 note 里保留这段说明（已有）。

### 3.10 Farragut 级吃水：3.12 m（设计，destroyerhistory）vs 3.53 m（navypedia，未标状态）

分片把 3.12 记 `draught.mean`（状态明确），3.53 只在 note 里并列，
`draught.max` 用两源一致的 4.98 m（16' 4"）。

---

## 4. 卡住的地方（未获取，不硬补）

| 项目 | 试了什么 | 为什么没写 |
|---|---|---|
| **Hammann 1942-06 时是否装了雷达、装了哪一型** | navypedia 只有一句笼统的「1942-1944, almost all survived: + SC, SG, Mk 4 or Mk 12.22 radars」，无逐舰年份；一手战报只提到舰上有 "radar room"（有舱室 ≠ 装了雷达） | 无逐舰记载。已在 `ships/hammann.yaml` 里以 `sensors.radar.installed: 未获取` 显式标出（**该条 value 是中文字符串，与字段 string 类型相容，但若主会话不喜欢这种写法可直接删**） |
| **Monaghan 中途岛当天的确切炮数** | navypedia 改装年表只写「5 - 9.1942」，中途岛（6 月）落在这个窗口内部，**无法确定是否已完成**；本组未获取 Monaghan 自己的中途岛行动报告全本（NHHC 该页目录里未见此舰条目） | 窗口内无法定位到日。已在 note 里标明是推定不是记载 |
| **Benham 的迷彩方案编号** | DANFS / NavSource / destroyerhistory 三处图注全部未提 Measure 号 | 无记载。以 `appearance.scheme: 未获取` 显式标出（**同上，可否入库请主会话定**） |
| **Benham 1942-11 在舰实际人数** | DANFS 只说 "entire crew survived"，未给编制数；NavSource 的 184 是平时编制 | 无记载。故 `service.survivors` **未写**（原本写了一版 `未获取`，因违反 integer 类型已删除，见 §5） |
| **Benham 是否完成了「No.4 加炮室 / No.3 加半炮盾」改装** | destroyerhistory 只描述了大西洋编队（DesDiv 16）与「太平洋各舰后来也做了同样改装」，**没有逐舰名录**；本舰 1942-11 就沉了 | 无逐舰记载 |
| **Monaghan 突入珍珠港当日的火炮故障** | DANFS 有完整叙述但未提任何火炮失效 | 未写（`armament.gun_failures` 字段本来也不适合记「无故障」这一否定事实） |
| **三舰 1941-1942 年各时点的迷彩方案**（除已注明的两处） | 只有 Hammann 1942-01 的 Measure 12 (Modified) 与 Monaghan 1944-09 的 Measure 31/7d 有明确图注 | 其余时点无记载 |
| **Monaghan 珍珠港当日舰长 Burford 的任期起止** | DANFS 只证明 1941-12-07 当天在任 | 无起止日 |
| **Benham 首任舰长 Darden 的任期终点** | DANFS 只给上任日 | 无卸任日 |
| **Farragut 级建成时的深弹数** | destroyerhistory 只说首两舰 1936 年加装滑轨，其余六舰未说何时；navypedia 第一条确切枚数在 1941 年中（14 枚） | 建成态无记载，故该 fact 的 `valid.from` 取 1941-07 而非建成日 |
| **Hammann 沉没当天日本的鱼雷型号** | I-168 的 TROM 只说 "Type 91 torpedoes" 用于 6 月 4 日对约克城号空投的那批（**那是航空鱼雷**，舰载机投的），6 月 6 日潜艇发射的是潜艇用 95 式，TROM 未明写型号 | 未确认，故不写 |
| **三舰的舷号涂装位置/舰名铭牌等外观细节** | NavSource 图注只零星提及（如 DD-348「her hull number is now painted higher up on the bow」） | 不足成条 |

---

## 5. 分片里已经处理掉、但需主会话知道的两个特殊写法

### 5.1 `ships/benham.yaml` 曾写一条 `未获取` 的 `service.survivors`，**已删除**

原因：`service.survivors` 在 `fields.yaml` 里注册为 `integer` + `unit: persons`，
填中文字符串会直接让校验器报类型错误（本组自检第一轮就抓到了）。
「Benham 全员生还但编制人数未知」这一事实改由本文件的 §4 表格承载。

### 5.2 两处 `未获取` 的 fact 仍然留在分片里

- `ships/hammann.yaml` 的 `sensors.radar.installed: 未获取`（string 字段，类型无损）
- `ships/benham.yaml` 的 `appearance.scheme: 未获取`（string 字段，类型无损）

这两条在技术上能通过校验，但**语义上是「此处无数据」而非「此处有个叫未获取的值」**。
若主会话的合并脚本会把它们当成真值渲染出来，请删掉这两条；
内容已在本文件 §4 完整保留。

---

## 6. 来源清单与使用方式

20 条新来源见 `sources-fragment.yaml`。按层级分布：

| tier | 条数 | 来源 |
|---|---|---|
| **A**（一手档案） | 2 | `nhhc-hammann-action-report`、`nhhc-dessron6-action-report` |
| **B**（同期官方出版物） | 4 | `nhhc-danfs-hammann`、`nhhc-danfs-monaghan`、`nhhc-danfs-benham`、`nhhc-danfs-vireo` |
| **C**（权威二次文献） | 2 | `navweaps-us-torpedoes`、`navweaps-us-asw` |
| **D**（专题站） | 12 | navypedia ×3、destroyerhistory ×6、NavSource ×3 |

复用既有来源（未重复登记）：`navweaps-5in38-mk12`、`navweaps-20mm-oerlikon`、
`combinedfleet-i168`、`nhhc-midway-us-order-of-battle`。
（`navweaps-40mm-bofors` 与 `nhhc-yorktown-midway-report` 虽在登记表里，但本轮**实际未引用**；
约克城号方面改用了同目录下的 `nhhc-hammann-action-report` 与 `nhhc-dessron6-action-report`。）

**已检查 `data/sources.yaml` 的 363 条现存 id**，确认下列 id 此前**不存在**、可以新登记：
`danfs-*`（含 hammann/monaghan/benham/vireo）、`navsource-dd-*`、`navypedia-sims/farragut/benham`、
`destroyerhistory-*`、`navweaps-us-torpedoes`。

⚠️ **一处容易踩的重复登记陷阱**：`data/sources.yaml` 里已有 `navweaps-torpedoes-wwii`，
但那一条是**德国鱼雷**（`WTGER_WWII.php`）。本组新增的 `navweaps-us-torpedoes` 是
**美制鱼雷**（`WTUS_WWII.php`），是两个不同页面，**不是重复登记**。
两者 id 只差一个字母（`torpedoes-wwii` vs `us-torpedoes`），合并时请勿误并。

---

## 7. DANFS 页面自身的错误（引用时须避开）

| 页面 | 错误 | 正确处理 |
|---|---|---|
| `nhhc-danfs-hammann` | 页首技术行写 **(DD-112**; dp. 1620; ...; a. 4 5", 8 21" tt.)——舷号应是 DD-412，炮数应是 5 门 | 该行整行不采用；舷号取正文的 DD-412 |
| `nhhc-danfs-monaghan` | 页首技术行写 **complement 100**——该级通行值 160（三源一致） | 不采用 100 |
| `nhhc-danfs-benham` | 页首技术行写 dp. 1,500（沿用官方设计值），与 navypedia 的实测标准 1,657 t 不同口径 | 记入 `displacement.standard` 的 note，不单独作 fact |
| `nhhc-danfs-farragut` | 抓到的页面是 **Farragut III**（DD-348），但本组只需要它的**舰级**信息，故未从中取任何 fact，只用于对照本级烟囱数 | 无 fact 引用 |

**另注卷次陷阱（合并时最易出错的地方）**：

- `monaghan.html` = Monaghan **I**（DD-32，一战平甲板型）；**本舰是 `monaghan-ii.html`**
- `benham-i.html` = Benham **I**（Destroyer No. 49）；**本舰是 `benham-ii.html`**
- 本组第一轮就抓错了 Monaghan（拿到了 DD-32），靠页面标题 `Monaghan I (Destroyer No. 32)` 发现后重抓

---

## 8. SCHEMA §10 自检结果

自检脚本 `_raw/selfcheck.py`（本组自写，逐条对照 `data/fields.yaml` 与来源表）输出：

```
facts checked: 326 in 6 files
new sources: 20

=== ERRORS (0) ===
=== WARNINGS (0) ===
```

清单逐项核对：

- [x] 每条 fact 的 `field` 都在 `data/fields.yaml` 里
- [x] 每条 fact 都有 `src`，且 src 都在 `sources-fragment.yaml` 或 `data/sources.yaml` 里
- [x] 每个带单位字段的 `unit` 与注册表一致（含 `date` 类字段的 `unit: date`）
- [x] `protection.armor.*` 都带 `qual`——**本轮三舰均未写任何 protection 字段**。
      理由：三份舰级来源（navypedia / destroyerhistory / NavSource）**没有一家明确写过
      「本舰无装甲」或给过任何装甲厚度**，只在 navypedia 的 armor 栏留空。
      按 SCHEMA §1「查不到就写查不到」，本组宁可不写，也不按「驱逐舰通例」推定
      `protection.scheme: none`——那是跨来源类推，属红线 §1 第 1 条禁止的行为。
      **若主会话手上有明确的「无装甲」来源，请自行补 `protection.scheme: none`。**
- [x] 没有 `confidence: D`
- [x] 没有用 tier E 来源支撑 fact（本轮**一条 E 级来源都没用**，维基一次也没打开）
- [x] `articles/` 顶层必须有 `ship`/`intro`/`history`——**本轮无 articles 文件**，不适用
- [x] 正文没出现「据说/有人认为/据信/或许/大概/应该是」——**本轮无 articles 文件**，不适用；
      RESEARCH-NOTES 本文件里也刻意未用这些词（用「未获取」「并列不裁决」代替）
- [x] 没有编造的数字

---

## 9. 三舰横向对照（给主会话做对比页时用）

| 项 | Hammann (DD-412) | Monaghan (DD-354) | Benham (DD-397) |
|---|---|---|---|
| 舰级 | Sims | Farragut | Benham |
| 标准排水量 | 1,764 t（navypedia） | 1,358 t（navypedia） | 1,657 t（navypedia） |
| 满载排水量 | 2,313 t | 2,064 t | 2,250 t |
| 全长 | 106.2 m | 104.0 m | 103.9 m |
| 水线宽 | 11.0 m | 10.4 m | 10.8 m |
| 锅炉 | 3 × B&W / 665 psi | 4 × Yarrow 或 Bethlehem / 400 psi | 3 × B&W / 565 psi |
| 出力 | 50,000 hp（一说 52,000） | 42,800 hp | 50,000 hp |
| 设计航速 | 35 kn（一说 37） | 36.5 kn | 38.5 kn（一说 36.5） |
| 建成主炮 | 5 × 5"/38（Mk 30：3 封闭 + 2 敞开） | 5 × 5"/38（全 Mk 21 敞开） | 4 × 5"/38（Mk 30：2 封闭 + 2 敞开） |
| 1942 年主炮 | 4 门（1941 夏拆 1 门） | 4 门（1942 年 5-9 月拆 No.3） | 4 门（未拆） |
| 建成鱼雷 | 12 管（→1940 夏 8 管） | 8 管 | 16 管（→1942 初 8 管） |
| 编制 | 192 | 160 | 184 |
| 结局 | 1942-06-06 被 I-168 击沉 | 1944-12-18 台风倾覆 | 1942-11-15 断成两段后由友舰击沉 |
| 结局性质 | `sunk_by_enemy` | `wrecked` | `sunk_by_scuttling` |

**中途岛时的三个不同位置**（这是三舰同场却分工不同的关键）：

- **Hammann**：TF 17 / TG 17.4（DesRon 2），6 月 6 日贴靠约克城号舷侧
- **Monaghan**：TF 16 / TG 16.4（DesRon 1），6 月 5 日 1830 到达约克城号身旁加入屏护
- **Benham**：TF 16 / DesRon 6，6 月 4 日 1522 转归 TF 17，救起 721 名约克城号幸存者
