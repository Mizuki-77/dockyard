# HMS Rodney（罗德尼号，舷号 29）— 技术数据与最终战考据

> 检索日期：2026-11-21。
> **硬规则执行说明**：每个数值后附来源缩写、URL 与英文原句；查不到原话支撑者一律写「未获取」，不推算、不跨来源拼、不按同级舰类推。
> 分歧并列不裁决；「未获取」与「0」严格分开。
> 单位换算若为本报告所做，标注「（本报告换算）」。
> **一手材料优先**：本舰 1941-05-27 炮术战报原文（`kbismarck-rodney-report`，tier A）为 §3/§4 的主证据，凡与二手站冲突，一律以战报原文为准并注明冲突。

---

## 0. 任务书前提核查（先反驳，再写正文）

调研铁律第 4 条要求「发现任务书前提错了，直接反驳」。逐条核对结果如下。

| # | 任务书原文 | 核查结论 | 依据 |
|---|---|---|---|
| 1 | 「服役（1927-11-10 前后，需查证）」 | **前提错误。** 服役日是 **1927-12-07**，不是 11-10。而且本舰有两个「服役」节点：1927-12-07 正式服役（commissioned），1928-03-28 才真正进入现役执勤（entered service）。 | naval-history：「fully commissioned at Devonport on **7th December 1927** for service in the Atlantic Fleet」；wiki Rodney：「she was **commissioned on 7 December**」「Rodney's trials resumed after she was formally commissioned and continued until she **entered service on 28 March 1928**」 |
| 2 | 「结局（1948 拆解）」 | **方向正确，但日期需分段。** 1948-03 列入报废清单 → 售予 BISCO → 交 Thos. W. Ward → **1948-03-26 拖抵 Inverkeithing** 解体。三个日期在来源间不一致，见 §1.5。 | naval-history：「placed on the Disposal List in **March 1948**… arrived in tow at Inverkeithing to be broken-up on **26th March 1948**」 |
| 3 | 「从**一手战报**里逐条提取：射击开始/结束时间」 | **前提错误。** 这份《Preliminary Gunnery Report》**通篇没有任何钟点**，只有弹药消耗、齐射构成、炮塔可用性与故障。开火/停火时间只能从别的来源取（§3.1）。 | 原文全文（109 行）无一处时刻；对照 `admiralty-bismarck-interrogation`「Rodney opened fire at 0847」 |
| 4 | 「命中数（若有记录）」 | **战报不记命中。** 原文只记自己打了多少发，没有一处命中记载。这是本舰「命中数」永远说不清的直接原因。 | 原文只有 §1 弹药消耗与 §2 齐射统计；`last-battle.md` 亦记「Rodney 的炮术报告只记自己打了多少发、不记命中」 |
| 5 | 「X 炮塔 25 次齐射中只有 6 次能瞄准、25 次后又 9 次不能」 | **完全正确**，原文逐字一致（§4.1）。 | 战报 §2 NOTE |
| 6 | 「A 塔右炮 tilting tray 卡死」 | **正确。** 原文用词 `jammed tilting tray`。 | 战报 §3 |
| 7 | 「B 塔左炮 double loaded」 | **正确**，且原文注明是 `the lower cordite hoist` 被 double loaded。 | 战报 §3 |
| 8 | 「B 塔中炮两发弹无发射药」 | **正确。** 原文 `two shells and no cordite`。 | 战报 §3 |
| 9 | 「4.7 英寸高炮全程未开火」 | **正确**，原文 `These guns were not fired during the action with the BISMARCK.` | 战报 NOTE 段 |
| 10 | 「kbismarck.com 没有 `rodney.html` 这个舰船专页」 | **正确**，实测 404。但同站有 `rodney-gunnery-report.html`（即本地 txt），且同站的 `bismarck-last-battle.html` 有大量 Rodney 叙述。 | 实测 `https://www.kbismarck.com/rodney.html` → 404 |
| 11 | 「主炮页 navweaps-16in-45-mk1（实测 200）」 | **正确**，`Approximate Barrel Life: 200 - 250 rounds`。注意这是**区间**，200 是下限。 | navweaps 16"/45 表 |

### 0.1 ⚠️ 项目内既有的来源登记错误（部分已被并发修正，但**正文尚未跟着改**）

**Rodney 的 12 门副炮是 `6"/50 BL Mark XXII`，不是 `Mark XXIII`。** 项目里曾把 Mk XXIII 登记成「Rodney 副炮」，现状态分两半：

| 项 | 现状（本报告 2026-11-21 23:2x 复核） |
|---|---|
| `data/sources.yaml` 的 `navweaps-6in-50-mk23` | ✅ **已被改正**（不是我改的，任务是禁止改 data/）。现 note 写道「**不是 Rodney 副炮**（2026-11-21 更正，原登记写错了）…本页装舰栏列的是 Leander / Perth / Arethusa / Southampton(Town) / Edinburgh / Fiji / Ceylon / Swiftsure 等**巡洋舰**，通篇没有 Nelson class。Rodney 的 12 门 6 英寸副炮是 **Mk XXII**」 |
| `data/sources.yaml` 新增 `navweaps-6in-50-mk22` | ✅ **已登记**（第 1837 行），note 写「**Rodney 副炮**（纳尔逊级）。实测装舰栏写 "Ship Class Used On — Nelson Class"」 |
| **`work/raw/last-battle.md` 第 398–399 行** | ❌ **仍是错的** —— 「Rodney… 12 × 15.2 cm（**6"/50 Mark XXIII**，六座双联）」/「12 × 15.2 cm (6"/50 **Mk XXIII**)」 |
| **`work/raw/last-battle.md` 第 685 行来源表** | ❌ **仍是错的** —— 「`[NAV6]` \| `navweaps-6in-50-mk23` \| D \| … \| 6"/50 Mark XXIII：弹重 50.8 kg、初速 841 m/s」 |
| **`work/raw/last-battle.md` 第 720 行未获取表** | ⚠️ **判断已过期** —— 原文「Sheffield 的火炮配置**未获取**…本文不作断言」；实际上 Mk XXIII 页就是 Sheffield（Town 级）的炮，**手上一直有，只是被贴错了标签**。这一格应从「未获取」升为「已获取」 |

**为什么这件事必须写进本报告**：`last-battle.md` 是本站最终战叙事的底稿，它的武备行会直接进战役页。**模型型号写错不会导致校验器报错**（validate.py 不核型号与装舰的对应关系），只能靠人眼抓。

**硬证据三条（本报告实测）**：

1. navweaps **Mk XXII** 页（`WNBR_6-50_mk22.php`，本次直连 200）：「Ship Class Used On — **Nelson Class**」；「this gun was originally designed for the never-built "G3" battlecruisers. When those ships were canceled as a result of the Washington Naval Limitation Treaty, **the guns and mountings were then used on the Nelson class battleships**.」
2. navweaps **Mk XXIII** 页（`WNBR_6-50_mk23.php`，本次直连 200）：「Ship Class Used On — **Leander, Perth, Arethusa, Southampton ("Town"), Edinburgh ("Modified Town"), Fiji ("Colony"), Ceylon ("Improved Colony") and Swiftsure classes**」——**通篇没有 Nelson class。**
3. navypedia 纳尔逊级装备表：「**6 x 2 - 152/50 BL Mk XXII**」。

**错因（推测）**：两型弹重巧合——Mk XXII 的 1942 年型 CPBC 也是 **112 lbs（50.8 kg）**，与 Mk XXIII 相同；但初速不同（**Mk XXII 898 mps / Mk XXIII 841 mps**）。当初按弹重对上了号，没核「装舰」栏。

**建议动作**（本报告遵守「不改 data/」，只列不改）：
- ① `last-battle.md` 第 399 行的 `Mk XXIII` → `Mk XXII`；第 398 行中文同改。
- ② 第 685 行 `[NAV6]` 的 id 从 `navweaps-6in-50-mk23` 改 `navweaps-6in-50-mk22`，数值改「弹重 45.36 kg（1942 年型 50.8 kg）、初速 898 mps、5 发/分」。
- ③ 第 720 行「Sheffield 的火炮配置未获取」删掉或改为「已获取：`navweaps-6in-50-mk23`（Town 级，6"/50 Mk XXIII）」。

本文件后续所有 Rodney 副炮数据一律用 **Mk XXII**（`navweaps-6in-50-mk22`），不用 Mk XXIII。

---

**额外发现的两处「一手材料自身错误」，写在最前面，避免后续引用踩坑：**

- **战报自身的算术错**：B 塔三管分计 `45 + 44 + 52`，实为 **141**，但塔总计写 **144**。差 3 发。（转录文本此处已带一句方括号算术注 `[45 + 44 + 52 = 141 rounds]`，无法判定是原件所有还是转录者所加，故照录并注明。）
- **战报的 6 英寸数完全平账，16 英寸数不平账**：6 英寸六座炮塔分计 128+93+154+97+160+74 = **706**，与总计 706 精确吻合；16 英寸 A 塔 36+46+22=104 吻合、X 塔 44+42+44=130 吻合，唯 B 塔差 3。**说明错在 B 塔那一处，不在总数。**（本报告核对）

---

## 1. 身份与建造

### 1.1 身份

| 项 | 值 | 来源与原句 |
|---|---|---|
| 舰名 | HMS Rodney | — |
| 命名 | 海军上将 George Brydges Rodney（1722–1792），圣文森特角与桑特海峡海战胜利者 | wiki Rodney：「Rodney, named for Admiral Lord George Rodney」；wiki class：「George Brydges Rodney, 1st Baron Rodney, victor of the Battle of Cape St. Vincent and the Battle of the Saintes」https://en.wikipedia.org/wiki/Nelson-class_battleship |
| 舷号 | **29** | wiki Rodney infobox：「Pennant number: 29」；navypedia 表列 `No = 29` |
| 舰级 | Nelson class（纳尔逊级），同级 2 艘 | navypedia 页题：「NELSON battleships (2, 1927)」https://www.navypedia.org/ships/uk/brit_bb1_nelson.htm |
| 船台号 | 904 | wiki Rodney：「Given the yard number 904」；navypedia 表 `Yard No 904` |
| 绰号 | `Rodnol`；`Queen's Mansions`；`the pair of boots`；`the ugly sisters`；`Cherry Tree class` | wiki Rodney：「The Nelson-class ships received several nicknames: Rodnol and Nelsol after the Royal Fleet Auxiliary oil tankers… The Queen's Mansions after a resemblance between her superstructure and the Queen Anne's Mansions block of flats, the pair of boots, the ugly sisters and the Cherry Tree class as they were cut-down by the Washington Naval Treaty」 |
| 是第几艘用此名 | 第 8 艘（naval-history）/ 第 6 艘（wiki）——**两者冲突** | naval-history：「as the **8th** RN ship to carry this name, introduced in 1759」；wiki Rodney：「Rodney was the **sixth** ship of her name to serve in the Royal Navy」 |

### 1.2 建造

| 项 | 值 | 来源与原句 |
|---|---|---|
| 承造厂 | Cammell Laird, Birkenhead | navypedia 表：「Cammell Laird, Birkenhead」；naval-history：「ordered from Cammell Laird, Birkenhead」 |
| 订购 | 1922-12-11 | naval-history：「ordered from Cammell Laird, Birkenhead on **11 December 1922**」；wiki class 建造表 Nelson 行「Ordered 11 December 1922」（Rodney 行该格空缺，见 §1.6） |
| 开工 | **1922-12-28** | navypedia 表：「28.12.1922」；naval-history：「laid down on **28th December 1922**」；wiki Rodney：「laid down on 28 December 1922 as part of the 1922 Naval Programme」 |
| 下水 | **1925-12-17** | navypedia：「17.12.1925」；naval-history：「launched on 17th December 1925」；wiki Rodney：「launched on 17 December 1925」 |
| 掷瓶人 | HRH The Princess Royal（玛丽长公主） | naval-history：「launched on 17th December 1925 by **HRH The Princess Royal**」；wiki Rodney：「by **Princess Mary, Viscountess Lascelles**, after three attempts at cracking the bottle of Imperial Burgundy」 |
| 完工 | 1927-08（wiki）/ 1927-11（navypedia）——**冲突**，见 §1.6 | wiki Rodney：「she was completed and her trials began in **August 1927**」；navypedia：「Comp **11.1927**」 |
| 服役 | **1927-12-07** | naval-history：「fully commissioned at Devonport on **7th December 1927** for service in the Atlantic Fleet」；wiki：「commissioned on 7 December under the command of Captain Henry Kitson」 |
| 首任舰长 | Captain Henry Kitson | wiki Rodney：「commissioned on 7 December under the command of Captain Henry Kitson」 |
| 正式进入现役 | 1928-03-28 | wiki Rodney：「trials resumed after she was formally commissioned and continued until she entered service on **28 March 1928**」 |
| 编制 | 1,314（private ship）/ 1,361（旗舰） | navypedia：「Complement 1314; **1361 as flagship**」；wiki 同值 |
| 造价 | **£6,150,000（1939 议会口径，不含首备）** vs **£7,617,799（wiki 单舰口径）**——**两说并列** | 见 §1.4 |

### 1.3 无分歧项

开工、下水、服役三个日期在 navypedia / naval-history / wiki 三源完全一致，无需并列。

### 1.4 造价（两说，口径不同）

- **£6,150,000** —— 英国议会 1939-03-15 书面答复，原文：「No battleship has been completed since the "**Rodney**" in 1927 which cost approximately **£6,150,000**.」同段并注明口径：「The foregoing figures are **exclusive of the cost of first outfit and reserves** of guns, torpedoes and ammunition.」https://api.parliament.uk/historic-hansard/written-answers/1939/mar/15/royal-navy-ship-construction-costs
- **£7,617,799** —— wiki Rodney：「The ship cost **£7,617,799**.」https://en.wikipedia.org/wiki/HMS_Rodney_(29)（该页脚注 28 指向 Ballantyne 2008，属二手转引，非一手档案）
- **£7,504,055–7,617,799（同级区间）** —— wiki class infobox：「Cost **£7,504,055–7,617,799**」https://en.wikipedia.org/wiki/Nelson-class_battleship
- **判断**：两者差约 24%，最可能的口径差正是议会明说的「是否含首备火炮/鱼雷/弹药储备」。**本报告不裁决**，两者并列；引用 £6,150,000 时必须同时带上「exclusive of first outfit」这句限定。

### 1.5 结局（三个日期不一致）

- **1945-11-30 在 Portsmouth 退役** —— naval-history：「before she **paid off at Portsmouth on 30th November** that year」（1945）
- **1945 年末降为预备役，Rosyth 封存** —— wiki Rodney：「she was **reduced to reserve in late 1945**」；naval-history：「The ship was **laid-up in Reserve at Rosyth**」
- **1946-08 退出服役** —— wiki Rodney infobox：「Out of service **August 1946**」「Decommissioned 1946」
- **1948-03 列入报废清单** —— naval-history：「placed on the **Disposal List in March 1948**」
- **1948-03-26 拖抵 Inverkeithing 解体** —— naval-history：「Sold to BISCO for demolition by TW Ward she arrived in tow at Inverkeithing to be broken-up on **26th March 1948**」；wiki Rodney：「the ship was allocated to **Thos. W. Ward on 26 March** to be scrapped at **Inverkeithing**」
- **1948-03-19 售出（另一说）** —— wiki class 建造表 Rodney 行：「Sold for scrap, **19 March 1948**」
- **1948 年 1–3 月曾在 Rosyth 3 号干船坞检视补漏** —— wiki Rodney：「She arrived at Rosyth on 2 December where she was docked in No. 3 dry dock **from 8 December until 1 March 1948**; during this time, Rodney's condition was surveyed and her leaks were patched.」
- 附：1948-12 至 1949-03 之间 Nelson 作为轰炸试验靶标后被拆，**两舰拆解年份相差一年**（wiki class：「Rodney was scrapped in 1948 at Inverkeithing… and **Nelson in 1949** following its use as a target for bombing trials」）

**「1948 拆解」这个结论成立**，但「3 月 19 日售出」与「3 月 26 日抵达拆解地」是两件事，不要合并成一个日期。

### 1.6 建造数据的分歧（并列不裁）

- **完工月份**：1927-08（wiki，据「trials began in August 1927」）vs 1927-11（navypedia `Comp 11.1927`）。同期 Nelson 是 1927-08（navypedia `8.1927`；naval-history 服役 1927-08-15）。**navypedia 给 Rodney 的 11.1927 与 wiki 的「8 月完成、12 月服役」不冲突——中间三个月可能正是「完工后继续试航」的窗口**，但两源均未明说，故并列。
- **wiki class 建造表有排版残缺**：Rodney 行的 `Ordered`、`Laid down`、`Launched` 三格空白，只剩 `17 December 1925`（下水）与 `7 December 1927`（服役）两个日期错位填入。**该表不可作为 Rodney 建造日期的独立来源**，只能用其 Nelson 行。
- **「第几艘同名舰」**：8（naval-history）vs 6（wiki）。naval-history 明写「introduced in 1759… It had previously been used for an 1884 battleship, sold in 1909」，是逐代计数的口径；wiki 的 6 未说明计数规则。**并列，不裁。**

---

## 2. 主尺度 / 排水量 / 动力（单舰值）

> 舰级共有值见 `work/raw/nelson-class.md`。本节只列 Rodney 与 Nelson **不同**或 Rodney 独有的值。

### 2.1 排水量

| 口径 | 值 | 来源与原句 |
|---|---|---|
| 标准 | **33,730 long tons（34,270 t）** | wiki Rodney：「She displaced **33,730 long tons (34,270 t) at standard load**」；navypedia：「Displacement standard, t — Nelson: 33313 / **Rodney: 33730**」https://www.navypedia.org/ships/uk/brit_bb1_nelson.htm |
| 满载/深载 | **37,430 long tons（38,030 t）** | wiki Rodney：「and **37,430 long tons (38,030 t) at deep load**」 |
| 舰级满载（另说） | 37,780 long tons（38,390 t） | wiki class：「37,780 long tons (38,390 t) (full load)」（该值是 **Nelson as built** 栏，非 Rodney） |
| 注水舱充满状态 | **41,250 t** | navypedia：「Displacement full, t — **41250 (with buoyancy spaces filled)**」 |
| 1942-05 状态 | 36,000 / 43,140 t | navypedia 改装记录：「5/1942, Rodney: … **displacement: 36000/43140t**」 |
| 1944 深载 | 43,100 long tons（43,800 t） | wiki Rodney：「These additions increased the ship's **deep displacement to 43,100 long tons (43,800 t)**」 |

**口径提醒**：navypedia 的 41,250 t「with buoyancy spaces filled」**不是**标准满载——它把防雷系统的注水舱算成排水量了。与 wiki 的 37,430 t 深载差 3,820 t，两者不可互替。

### 2.2 主尺度

| 项 | 值 | 来源与原句 |
|---|---|---|
| 全长 oa | **216.5 m / 710 ft 3 in** | wiki Rodney：「an overall length of **710 feet 3 inches (216.5 m)**」；navypedia：「Length, m — 201.2 pp **216.4 oa**」 |
| 垂线间长 pp | **201.2 m / 660 ft** | wiki Rodney：「length between perpendiculars of **660 feet (201.2 m)**」；navypedia：「**201.2 pp**」 |
| 最大宽 | **32.3 m / 106 ft** | wiki Rodney：「a beam of **106 feet (32.3 m)**」；navypedia：「Breadth, m — **32.3**」 |
| 吃水（标准，平均） | **9.2 m / 30 ft 2 in** | wiki Rodney：「a draught of **30 feet 2 inches (9.2 m) at standard load**」 |
| 吃水（mean / 超深载） | 8.56 m / **10.2 m** | navypedia：「Draught, m — **8.56 mean, 10.2 extra deep load**」 |
| 稳心高 GM | 3.1 m / 10.2 ft（深载） | wiki class：「At deep load, they had a **metacentric height of 10.2 feet (3.1 m)**」 |
| 横摇周期 | 11.2–13.6 s | wiki class：「which gave them a quick roll between **11.2 and 13.6 seconds**」 |
| 型深 / 方形系数 / 水线面积 | **未获取** | 见 §8 |

**长度分歧**：216.4（navypedia）vs 216.5 m（wiki）。wiki class 页自己写「709 feet 10 inches (216.4 m) (**Nelson**) or 710 feet 3 inches (**216.5 m**) (Rodney)」——即两舰全长确实不同，Rodney 长 5 英寸。**这不是分歧，是两舰差异。**

**吃水分歧**：9.2 m（wiki，标准状态）vs 8.56 m（navypedia，mean）。差 0.64 m，无法用取整解释。wiki 明确绑定「at standard load」，navypedia 只写 `mean`，未注状态。**并列不裁**，引用时须带状态限定。

### 2.3 动力

| 项 | 值 | 来源与原句 |
|---|---|---|
| 形式 | 2 组 Brown-Curtis 齿轮传动汽轮机，2 轴 | navypedia：「Machinery — **2 sets Brown-Curtis geared steam turbines**, 8 Admiralty 3-drum boilers」；wiki Rodney 同 |
| 锅炉 | 8 × Admiralty 三鼓水管锅炉，带过热器，**250 psi** | wiki class：「eight Admiralty 3-drum boilers fitted with superheaters that operated at a pressure of **250 psi (1,724 kPa; 17 atm)**」 |
| 设计功率 | **45,000 shp** | navypedia：「Power, h. p. — **45000**」；wiki 同 |
| 实测功率 | **45,614 shp**（Rodney 1927-09-07 试航）；姊妹舰区间 45,614–46,031 shp | wiki Rodney：「During her sea trials on **7 September 1927**, Rodney reached a top speed of 23.8 knots (44.1 km/h; 27.4 mph) from **45,614 shp (34,014 kW)**」；wiki class：「reaching speeds of 23.6–23.8 knots from **45,614–46,031 shp**」 |
| 设计航速 | **23 kn** | navypedia：「Max speed, kts — **23**」 |
| 实测航速 | **23.8 kn** | 同上 |
| 燃油 | **3,770 t 油** | navypedia：「Fuel, t — Nelson: 3805 oil / **Rodney: 3770 oil**」 |
| 续航（navypedia 口径） | **14,500 nm @10 kn** | navypedia：「Endurance, nm(kts) — **14500(10)**」 |
| 续航（wiki 口径） | **7,000 nm @16 kn** | wiki Rodney：「range of **7,000 nautical miles (13,000 km) at a cruising speed of 16 knots**」 |
| 螺旋桨 | 2 只，直径较大 | wiki class：「there were only **two shafts with quite large screws**」 |
| 舵 | 单舵，位于中线、不在螺旋桨尾流中 | wiki class：「the ships having a **single, central rudder** which was out of the propeller race of the twin screws」 |
| 锅炉舱布置 | 锅炉舱在机舱**之后**，共用一个烟囱 | wiki class：「the **boiler rooms were moved behind the engine rooms**, exhausting into a single funnel」 |
| 发电机 | **未获取** | 见 §8 |
| 蒸汽温度 | **未获取** | 见 §8 |

**续航三说并列不裁**：14,500 nm @10 kn（navypedia）vs 7,000 nm @16 kn（wiki）。两者**航速档不同**，理论上不矛盾；但换算成同一档差异很大（10 kn 档若按平方律估，16 kn 折 10 kn 约 1.7 万 nm，与 14,500 仍差一截）。两源均未给计算口径，**并列，不裁**。

**实战反证（重要）**：Rodney 的续航是这一级最著名的短板，属设计妥协的直接后果。
- wiki class：「Unlike Nelson, which exceeded the design specification for machinery weight, **the lighter machinery of Rodney resulted in chronic problems. The ship's endurance declined substantially in the decade after her launch; in her 1941 action against Bismarck, Rodney was nearly forced to abandon the pursuit because of a lack of fuel.**」
- 英海军部审讯：「Shortage of fuel had now become a matter of grave anxiety in the Home Fleet battleships. "King George V" had only 1,200 tons (32 per cent.) remaining, and "**Rodney" reported she would have to part company at 0800 the next morning.**」https://www.uboatarchive.net/Int/BismarckINT.htm
- naval-history（战后返港）：「**RODNEY's fuel tanks were virtually empty** and she immediately commenced bunkering」

---

## 3. 最终战（1941-05-27）：一手战报逐条提取

> **原始材料**：`work/raw/kb-rodney-report.txt`，即 `kbismarck-rodney-report`（tier A）。
> 该件标题原文：「**HMS Rodney Preliminary Gunnery Report of Action, 27 May 1941.** (Enclosure "E" to JHW's Report, serial F-1; x-27 dated July 1941.)」
> https://www.kbismarck.com/rodney-gunnery-report.html

### 3.1 射击起止时间（**战报本身没有**，只能从他源取）

战报通篇无钟点。以下时刻全部来自其他来源，**逐条标源、并列不裁**：

| 事件 | 时刻 | 来源与原句 |
|---|---|---|
| Rodney 发现 Bismarck | 0843（距约 24,700 yd） | naval-history：「At **0843** hours RODNEY sighted the BISMARCK at a range of about **24,700 yards**」https://www.naval-history.net/xGM-Chrono-01BB-HMS_Rodney.htm |
| 同上（另说） | 0843，方位 118°，约 25,000 yd | `admiralty-bismarck-interrogation`：「at **0843** the enemy came in sight, bearing 118°, about **25,000 yards** distant」 |
| 同上（三说） | 0844 | wiki Rodney：「Rodney spotted Bismarck at **08:44** on 27 May, one minute after King George V」 |
| **Rodney 开火** | **0847** | `admiralty-bismarck-interrogation`：「"Rodney" **opened fire at 0847**」；naval-history：「At **0847** hours RODNEY, sailing at 16 knots, opened fire on the BISMARCK at a range of **23,400 yards**」 |
| 开火距离（另说） | 约 20,000 m | `last-battle.md` 引 Tovey 战报：「Rodney opened fire at 0847 at about **20,000 m**」 |
| KGV 开火 | 0848 | 同上（KGV 自身报告口径，见 `last-battle.md`：「her own report: 0848, 24,600 yards」） |
| Bismarck 还击 | 0849 | 审讯：「"Rodney" opened fire at 0847, followed one minute later by "King George V," and at **0850** by "Bismarck"」←**审讯作 0850，naval-history 作 0849**，并列 |
| **Rodney 停火** | **1014**（naval-history）/ **1016**（kbismarck、wiki）/ **1022**（审讯） | naval-history：「At **1014** hours RODNEY ceased fire」；kbismarck：「The Rodney **ceased fire at 1016**」https://www.kbismarck.com/bismarck-last-battle.html；审讯：「fire ceased at **1022**」 |

**结论：Rodney 本舰的炮术战报对「打了多久」一个字没写。** 凡本页后续引用「0847–1016」这类区间，均为他源拼合，不是一手数据。

### 3.2 弹药消耗（**战报 §1，一手**）

原文逐字：

> 「1. Total number of rounds of 16" fired—**378**.
> Total number of rounds of 6" fired—**706**.」

分塔分炮管（原文逐字）：

| 炮塔 | 塔总计 | 左炮 | 中炮 | 右炮 | 分计之和 | 是否平账 |
|---|---|---|---|---|---|---|
| A | **104** | 36 | 46 | 22 | 104 | ✅ |
| B | **144** | 45 | 44 | 52 | **141** | ❌ **差 3 发** |
| X | **130** | 44 | 42 | 44 | 130 | ✅ |
| 合计 | 378 | — | — | — | 375 | 差 3 |

原文（B 塔）：「(b) "B" turret fired a total of **144** rounds. Left gun fired **45**, Centre gun fired **44**, Right gun fired **52**,」后接转录者的方括号注 `[45 + 44 + 52 = 141 rounds]`。

6 英寸副炮（原文逐字，一手）：

> 「(d) Each 6" twin turret fired the following rounds: S1 - **128**, P1 - **93**; S2 - **154**, P2 - **97**; S3 - **160**, P3 - **74**」

六座相加 = **706**，与总计精确吻合。（本报告核对）

**与二手来源的冲突（并列，以战报为准但不抹掉另一说）**：

| 口径 | 16 英寸 | 6 英寸 | 来源 |
|---|---|---|---|
| **战报（A）** | **378** | **706** | `kbismarck-rodney-report` |
| Admiralty War Diary | 380 | 716 | 「RODNEY **380 rounds 16 inch, 716 - 6 inch**, 12 torpedoes」`work/raw/lb-admiralty-diary.txt` |
| KGV 舰长 Patterson 报告 | 380 | 716 | 「I understand Rodney fired **380 rounds of 16-inch and 716 of 6-inch**」 |
| navweaps 16"/45 页 | 380 | — | 「Rodney fired a total of **380 rounds**」 |
| wiki Rodney | 378 | 706 | 「Rodney fired **378** sixteen-inch shells and **706** six-inch shells」 |

**为什么两说都对**：`last-battle.md` 已给出判断：「the same expenditure recorded two ways」——378/706 是炮术报告的**实发统计**，380/716 是返港补给申请的**领用数**（naval-history：返港后「immediately commenced bunkering and replenishing her ammunition」；War Diary 同段正是补给申请「At Greenock for RODNEY 16 inch **380**, 6 inch **716**」）。**这解释了 2 发与 10 发的固定差额，且两处差额方向一致（补给数 > 实发数）。**

### 3.3 齐射数量与构成（**战报 §2，一手**）

**关键前提（原文）**：

> 「2. In salvo fire the RODNEY fires double salvos. The first salvo consisting of **5 guns**—wing guns of "A" and "X" turrets plus the center gun of "B" turret, the second salvo consisting of **4 guns**—the center guns of "A" and "X" turrets plus the wing guns of "B" turret. In broadside fire all guns of all turrets that are loaded and can bear on the target fire simultaneously.」

**注意**：Rodney 的「齐射」是 5 发 / 4 发交替的**双联齐射**（double salvos），不是 9 门齐射——这是因为三门炮同塔不能齐放（弹道互相干扰），必须内外炮分管分批。战报 NOTE 明写原因：

> 「NOTE: Since double salvos are used in broadside firing 5 and 4 gun salvoes should be fired alternately provided all turrets can bear on the target and all guns in each turret are ready to fire. Under the same conditions in broadside firing each salvo should consist of **9 guns**.」

**按齐射法统计（原文表）**：

| 每齐射炮数 | 齐射次数 |
|---|---|
| 1 发 | 6 |
| 2 发 | 22 |
| 3 发 | 41 |
| 4 发 | 28 |
| 5 发 | 6 |
| 6 发 | 1 |
| **合计** | **104** |

**按舷射法（broadside）统计（原文表）**：

| 每舷射炮数 | 次数 |
|---|---|
| 8 发 | 1 |
| 7 发 | 3 |
| 6 发 | 1 |
| 5 发 | 2 |
| 3 发 | 1 |
| 2 发 | 1 |
| **合计** | **9** |

**必须注意的两点（本报告核对）**：

1. 原文小标题写的是「A summary of the 16" **rounds** fired by the salvo method and by the broadside method」，但两个 `Total`（104 与 9）实际是**齐射/舷射的次数**，不是发数。**照字面把 104 当成「打了 104 发」是误读。**
2. 按次数乘炮数得发数：齐射 6×1+22×2+41×3+28×4+6×5+1×6 = **321**；舷射 1×8+3×7+1×6+2×5+1×3+1×2 = **50**；合计 **371**。与战报 §1 的 **378** 差 7 发。**战报内部第二处不平账，且方向与 B 塔那 3 发不同。**两处差异均无法从原文内部解释，只能如实记录。

**「104 是齐射次数、不是发数」这条判断的独立交叉验证**（本报告做，值得写进来，因为它堵住了最容易被误读的一处）：

navweaps 16"/45 页从 Roberts 转引：「During the entire battle, she fired **1.6 salvos per minute during salvo firing** and **1.1 broadsides per minute during broadside firing** with outputs of **77% and 62%** respectively」。

- 104 次齐射 ÷ 1.6 次/分 = **65 分钟**
- 9 次舷射 ÷ 1.1 次/分 = **8 分钟**
- 合计 **73 分钟**，落在 0847–1016 的 **89 分钟**窗口内（中间有停射观察段），**吻合**。
- 若把 104 当发数：104 发 ÷ 89 分钟 = 1.2 发/分，与「平均每门炮 1.5 发/分 × 9 门」量级差一个数量级，**不成立**。

**→ 因此「104 = 齐射次数」是有独立来源支撑的结论，不是本报告的猜测。** 但也正因如此，战报 §2(a) 那句「A summary of the 16" **rounds** fired」的用词是**错误的**（应为 salvos），这是这份一手材料自身的第三处瑕疵。

### 3.4 命中数

**战报不记命中。** 原文全篇无任何「hit」字样（唯一近似的是 `out of action`，指自身故障）。

二手来源的命中口径，并列不裁：

- **wiki class**：「Rodney's main guns were credited with an estimated **100 to 130 hits**, contributing greatly to Bismarck's final destruction.」https://en.wikipedia.org/wiki/Nelson-class_battleship
- **双方合计命中无法确知** —— kbismarck：「The number of hits will never be known. **200, 300, maybe more?**」
- **英方维基口径**：四舰合计约 2,800 发、命中约 400 发（转引自 `last-battle.md` 争议 2）
- **德方战俘的反向证据（A 级）**：审讯原文「All prisoners, with the exception of one junior officer, state that **no shells penetrated the armour belt**.」——即命中再多数百，**落在主装甲带上的穿透为零**。

**这三条必须同时用**：命中数（100–130 是「Rodney 一舰」估算）、总命中（200–400）、装甲带穿透（0）是三个不同层级的数，混用就会得出「Rodney 打沉了俾斯麦」的错误链条。

### 3.5 决定性的一击？——两边都写

**支持「Rodney 那一击是转折」的证据链（A 级为主）**：

1. **0902 命中前舰楼，废掉前主炮塔** —— 英海军部审讯（A）：「"Rodney" reported **a hit on "Bismarck's" forecastle at 0902 with a 16-in. shell, which apparently put these turrets out of action**.」（"these turrets" 指前部的 A、B 两塔）
2. **同一击摧毁舰桥与主火控** —— kbismarck：「at 0902, the Bismarck was hit by several shells that struck the forecastle, foremast and **disabled the foretop rangefinder**」；「At 0908, the forward range finder and turrets "Anton" and "Bruno" were put out of action. **Bismarck's fire control was, therefore, shifted to the after command post.**」
3. **德方火控官本人承认这一击是致命的** —— 审讯：「Kapitänleutnant von Müllenheim-Rechberg believes that this hit was scored by a shell from "**Dorsetshire**"… this hit, which, metaphorically speaking, "**blew out 'Bismarck's' brains.**"」——**注意：他归给 Dorsetshire，不归 Rodney。**
4. **Rodney 自己的战果陈述** —— 审讯转述：「"Rodney" reports that shortly before "Bismarck" sank, her 16-in. shells had **caused indescribable devastation** and the ship was an inferno. One hit had **blown the back of "Bismarck's" "B" turret into the water** (this has not been confirmed by prisoners).」——**括号里那句「未被战俘证实」必须一起引。**
5. **德方炮术军官的当面评价** —— 审讯：「"Dorsetshire" signalled "Rodney": "**Bismarck's" Gunnery Officer says you knocked seventeen bells out of him.** A one west country ship to another, may we say: "Well done."」

**反对「决定性一击」/ 支持「自沉说」的证据链（同为一手）**：

1. **官方结论是「加速」不是「击沉」** —— 审讯原文：「The actual cause of sinking is still a matter of dispute among survivors. There is however a considerable body of evidence to support the view that the inevitable end of the "Bismarck" was **hastened** by the explosion of specially prepared scuttling charges.」
2. **装甲带零穿透** —— 同上：「no shells penetrated the armour belt」（除 1 名下级军官外全员一致）
3. **战俘认为不打雷不沉舰她还能回港** —— 同上：「in the opinion of some prisoners, it might still have been possible to get the ship back to harbour at the close of the artillery action, **had the final torpedoes not been fired or scuttling attempted**.」
4. **首弹时刻对不上** —— 审讯：「At **0851** "Rodney" had straddled "Bismarck" but it was not until **0857**, according to prisoners, that "Bismarck" sustained her first hit.」——**战俘把首弹记在 0857，不是 0902。**
5. **德方官方口径（1941 年公告与 KTB）完全不提自沉**，写成「成为优势兵力之牺牲品」，见 `work/raw/last-battle.md` 争议 1 第 5 说。
6. **残骸物证** —— 仅 2 处 320 mm 主装甲带被完全穿透，均在右舷舯部；Cameron 等 2002 结论「BOTH」，但同时认定「Bismarck unquestionably would have sunk due to progressive flooding hours after the battle ended」。

**本报告的立场（不是裁决，是措辞建议）**：

> Rodney 的 0902 那一发是**单发效果最大的一击**（废掉前主炮塔 + 舰桥 + 前桅火控），但它**不是「击沉俾斯麦的那一击」**。把它写成决定性一击会同时违反三份一手材料：审讯的 `hastened` 措辞、`no shells penetrated the armour belt`、以及战俘的 0857 首弹时刻。**页面正文应写「Rodney 的一发 16 英寸弹摧毁了俾斯麦号的前部火控与主炮塔，使其失去有组织还击能力；沉没的直接原因仍是累积战损 + 自沉（英方官方用语为 hastened）」**，并把「Dorsetshire 的那发才毁掉主火控」这条德方证词一并列出。

### 3.6 最终战时间线（多源并列）

| 时刻 | 事件 | 来源 |
|---|---|---|
| 0730 | KGV、Rodney、Tartar、Mashona 向东大转弯，准备从西面接战 | naval-history |
| 0735 | 改向 080° 接敌，Rodney 奉命占 010° 方位、间距不小于 6 链 | `admiralty-bismarck-interrogation` |
| 0820 | Norfolk 出现在视界内，提供目视连接 | 同上 |
| 0843 | 发现 Bismarck（约 24,700–25,000 yd） | naval-history / 审讯 |
| **0847** | **Rodney 开火，23,400 yd，航速 16 kn** | naval-history / 审讯 |
| 0848 | KGV 开火 | KGV 报告（转引） |
| 0849–0850 | Bismarck 以 Anton、Bruno 还击 Rodney（Cäsar、Dora 无法转向） | naval-history 0849 / 审讯 0850 |
| 0850 | 一发德弹在左舷首外水中爆炸，冲击波**卡死 Rodney 左舷鱼雷发射管门** | naval-history：「the force of the explosion **jammed her port torpedo tube doors**」 |
| 0851 | Rodney 跨射 | 审讯：「At **0851** "Rodney" had straddled "Bismarck"」 |
| 0854 | Norfolk 于 18,000 yd 开火 | naval-history |
| 0857 | 战俘记 Bismarck **首次中弹** | 审讯 |
| 0858 | Bismarck 仍以主副炮稳定射击 Rodney | 审讯：「She was, however, still firing steadily at "Rodney" with main and secondary armament at **0858**」 |
| 0858 | Rodney 副炮加入射击（6 英寸） | kbismarck：「at **0858** the secondary battery of Rodney joined the action」 |
| 0901 | Rodney 第 4 次齐射：2 发近失、**2 发命中** | naval-history：「At **0901** hours RODNEY fired her fourth salvo, two shells missed and two were hits.」 |
| **0902** | 一发 16 英寸命中前舰楼，废 A/B 塔与舰桥、前桅测距仪 | 审讯 + kbismarck + wiki |
| 0904 | Dorsetshire 开火 | kbismarck |
| 0908 | 前桅测距仪与 Anton、Bruno 塔失效，火控转后指挥所 | kbismarck |
| 0913 | 后指挥所被 14 英寸弹摧毁 | kbismarck |
| **0916** | **Rodney 从左舷（一说右舷）发射鱼雷，史上首次战列舰对战列舰发射鱼雷** | naval-history：「At **0916** hours RODNEY fired the first of twelve torpedoes from her starboard tube」 |
| 0918 | Rodney 接近至 8,000 yd | naval-history |
| 0921 | Dora 塔因自身右炮膛内炸而失效 | kbismarck |
| 0927 | Bismarck 前塔最后一次齐射 | naval-history / kbismarck |
| **0930** | 一发 Rodney 16 英寸弹穿透俾斯麦甲板、在**左舷机舱**内爆炸，机舱报废 | naval-history：「a 16in shell from RODNEY penetrated BISMARCK's deck armour and exploded in the port engine room」 |
| 0930 | Rodney 因**自身火控设备失效**而接近至 6,000 yd | naval-history：「At **0930** hours RODNEY closed to **6,000 yards to compensate for the failure of her fire control equipment**」 |
| 0931 | 一发 Rodney 16 英寸命中 Dora 塔，该塔因烟毒被弃；Cäsar 打完最后一发 | naval-history |
| 0931 | Cäsar 最后一次齐射（另说） | kbismarck：「at **0931** turret "Cäsar" fired its last salvo」 |
| 0940 | Dorsetshire 于 20,000 yd 开火 | naval-history |
| 0948 | Norfolk 停止侧翼标定、加入射击；Rodney 获准自由行动 | 审讯 |
| 0956 | Rodney 又射 2 雷（2,700 m），可能 1 雷命中左舷 | kbismarck：「At **0956**, the Rodney launched two more torpedoes from 2,700 metres with one possible hit scored on the portside」 |
| 1000–1015 | 俾斯麦舰员引爆预设自沉装药 | naval-history（括注段） |
| 1003 | Rodney 接近至 4,000 yd | naval-history |
| **1014 / 1016** | **Rodney 停火** | naval-history 1014 / kbismarck 与 wiki 1016 |
| 1021 | KGV 由 Y 塔打完最后一次齐射 | naval-history |
| 1022 | Dorsetshire 2 雷命中右舷 | naval-history |
| 1036–1037 | Dorsetshire 第 3 雷命中左舷 | naval-history / kbismarck |
| 1039 | Bismarck 沉没（48°09′N 16°07′W） | naval-history / kbismarck |
| 1037 | 审讯口径的沉没时刻 | 审讯：「sank, with her colours flying, at **1037**」 |

### 3.7 鱼雷：数量与是否命中（三说并列）

- **12 枚**（naval-history，且称自右舷发射）：「RODNEY fired the first of **twelve** torpedoes from her **starboard** tube… All the torpedoes except possibly one missed.」
- **6 枚 + 2 枚 = 8 枚**（kbismarck）：「had launched **six** torpedoes at Bismarck, none of them hit」＋「At 0956, the Rodney launched **two more** torpedoes… with one possible hit」
- **6 枚（部分二手）** —— `last-battle.md`：「Rodney fired **six** torpedoes at long range, none hitting」
- **英方一手审讯：命中 1 雷** —— 「All Home Fleet ships had expended their torpedoes, including "**Rodney," who had scored one hit**」
- **wiki 舰级页：命中 1 雷，且是史上唯一一次**：「Rodney fired a pair of 24.5-inch torpedoes from her **port-side** tube and claimed one hit. According to Ludovic Kennedy, "if true, [this is] **the only instance in history of one battleship torpedoing another**".」
- **舷别**：naval-history 说右舷发射；wiki 说左舷发射管命中。而 naval-history 同页又记「一发德弹近失**卡死了左舷鱼雷管门**」——**若左舷门已卡死，则左舷不可能发射；wiki 的「左舷命中」与 naval-history 的「左舷门卡死」直接冲突。三说并列，不裁。**

---

## 4. 炮术故障逐条（一手战报 §2 NOTE 与 §3）

> 全部原文照抄，数字不改写。这是本舰最有价值的一节。

### 4.1 X 炮塔无法瞄准 —— 28 次（原文逐字）

> 「In the action with the BISMARCK "**X" turret could only bear on the target on 6 out of the first 25 salvoes. After the 25th salvo "X" could not bear on 9 occasions, making a total of 28 salvoes or broadside that "X" turret could not bear on the target.**」

拆解（原文数字，不改写）：
- 前 25 次齐射中，X 塔**只有 6 次**能瞄准目标 → **19 次**不能瞄准
- 第 25 次之后，X 塔又**9 次**不能瞄准
- 合计 **28 次**齐射/舷射不能瞄准

**为什么不能瞄准（形制原因，非故障）**：三座炮塔全在前部，X 塔在最靠后、位置最低（`X "turret" on the forecastle deck behind "B"`），射界被上层建筑与舰桥挡住。navweaps：「"X" Turret: **About 60 to 130 degrees on either side**」——即正前正后都不能打。**这是设计后果，不是机械故障，两者必须分开写。**

### 4.2 战报 §3 原文（三处失效，逐字）

> 「3. At the end of the action the following guns were out of action:
> **Right gun of "A" turret completely, caused by a jammed tilting tray.**
> **Left gun of "B" turret very temporarily, caused by the lower cordite hoist being "double loaded" when loaded cage was lowered.**
> **Center gun of "B" turret temporarily, due to two shells and no cordite.**」

逐条对应任务书：

| 任务书表述 | 战报原文 | 核对 |
|---|---|---|
| A 塔右炮 tilting tray 卡死 | `Right gun of "A" turret completely, caused by a jammed tilting tray.` | ✅ 完全一致，且**「completely」= 全程报废**，不是暂时 |
| B 塔左炮 double loaded | `Left gun of "B" turret very temporarily, caused by the lower cordite hoist being "double loaded" when loaded cage was lowered.` | ✅ 一致；原文额外给出机理：**装好的弹笼下放时，下部发射药扬升机被 double loaded** |
| B 塔中炮两发弹无发射药 | `Center gun of "B" turret temporarily, due to two shells and no cordite.` | ✅ 一致；原文措辞是 `two shells and no cordite`（两发弹、零发射药） |

**四条口径提醒**（引用时必须带上）：
1. A 塔右炮是**「completely」**——全程失效，与 B 塔两门的**「temporarily / very temporarily」**性质不同，不要并列成「三处故障」。
2. B 塔左炮是 **「very temporarily」**，中炮是 **「temporarily」**——两个程度副词不同，原文有区分。
3. 战报的 §3 只记**战斗结束时**的状态，不记过程。过程性的故障（missed salvos）在别处，见 §4.3。
4. **战报没有说 X 塔「故障」**——原文用的是 `could not bear`（不能指向），不是 `out of action`。**把 X 塔写进「故障清单」是错的。**

### 4.3 补充：战报之外的过程性故障（B 级，转引 John Roberts）

navweaps 16"/45 页从 John Roberts《The Final Action: The Sinking of Bismarck, 27 May 1941》转引：

> 「She experienced various minor problems with mechanical failures and drill errors, the worst being with the right gun of A turret. This gun **missed 11 salvos** due to problems with the **slide locking gear** and then, at **salvo 65**, a **complete jam** occurred in the right **shell pusher hoist**. As a result of drill errors the top shell was rammed up the hoist and jammed in the gunhouse with its nose against the rangefinder supports. **It was not cleared until 12 hours after the action.** In addition the centre gun of A **missed 2 salvos** due to slow drill and **all the salvos from 64 to 88** due to mechanical failures, the left gun of A **missed 10 salvos** and **did not fire after salvo 97** due to mechanical failures. B turret's centre gun **misfired at salvo 4** and missed 5 or 6 over a period of 7 minutes towards the end of the action due to drill errors. The left gun of B had several delays as a result of drill errors but **X turret suffered only two jams** which caused only minor delays.」https://www.navweaps.com/Weapons/WNBR_16-45_mk1.php

**与战报的对照（本报告核对）**：
- Roberts 说 A 塔右炮卡在**右炮扬弹机**（shell pusher hoist），战报说 **tilting tray**。**两个不同的部件名，指同一门炮的失效。** 并列，不裁——战报是一手，Roberts 是二手转引，但 Roberts 给了战报没有的机理（顶弹被误推上升弹机、卡在炮房内、抵住测距仪支架、战后 12 小时才清出）。
- Roberts 说 **X 塔只发生过两次卡壳**（"X turret suffered only two jams which caused only minor delays"）——**这与「X 塔 28 次不能瞄准」不矛盾**：前者是机械卡壳，后者是射界受限。**两件事，别混。**
- Roberts 的「salvo 65」「salvo 64–88」「salvo 97」这些编号是战报里没有的，属 Roberts 独有的过程记录。

### 4.4 4.7 英寸高炮全程未开火（一手）

> 「The long range A.A. guns consist of three 4.7" single mount guns on each side. **These guns were not fired during the action with the BISMARCK.**」

**「未开火」是事实，但不是「火炮损坏」。** 战报只陈述未开火，未给原因。可能的解释（**均为推断，不作数据**）：射程/仰角无法对水面目标、目标在视界内过近、或防空指挥仪未获射击诸元。**本报告不给原因，标「原因未获取」。**

### 4.5 自身火炮造成的损伤（B/C 级，二手）

naval-history（Rodney 战后记录）：

> 「The blast effects from RODNEY's main armament **caused the Douglas fir decking on the upper deck to be ripped up**. Also the adoption of aluminium alloys for most of the minor ships fittings, such as kit lockers, mess racks, store cupboards and wash facilities caused all these fittings to be shaken up and some dislodged when the main armament was fired. **Cast iron water mains were ruptured and in many instances broke, flooding compartments.**」

wiki Rodney：「Ironically, **Rodney's own main guns firing at low elevation had damaged her more extensively than had Bismarck.** Deck plates around the main-gun turrets had been depressed by the effects of the guns' muzzle blast, and some of the structural members supporting them had cracked or buckled. Piping, urinals and water mains had broken, while the shock of firing had loosened rivets and bolts in the hull plating, flooding various compartments.」

---

## 5. 舰体与形制（细节见 `work/raw/nelson-class.md`）

**本舰形制的三个定义性特征**（每项带原句）：

1. **三座三联装主炮塔全部前置** —— 战报 NOTE：「The RODNEY has **three 16" triple gun turrets. All 16" turrets are located in the forward part of the ship** and are named "A", "B" and "X" turrets in order from forward to aft. "B" turret is the high turret.」
2. **舰桥/上层建筑被推到后部** —— wiki class：「The most unusual feature however, and one that is immediately noticeable, is that these were **all carried forward of the bridge**.」
3. **副炮全部后置、分两舷金字塔形布置** —— 战报 NOTE：「The secondary battery consists of **three 6" twin turrets on each side**. The twin turrets are numbered from forward to aft on each side as follows: Port side—P1, P2, P3; Starboard side—S1, S2, S3.」

**任务书的「舰桥后置」表述基本成立**，但有一处需要精确化：**上层建筑确实整体位于三座主炮塔之后、舰体中部偏后**，但「舰桥」本身仍在距舰首约一半舰长处，不是真的在舰尾。wiki class 给的原因是重量：「To reduce the weight of armour, the main gun turrets were all mounted forward to **shorten the armoured citadel**」，并解释「The location of the superstructure **towards the stern** caused manoeuvrability problems in high winds… the superstructure acted somewhat like a **mizzen sail permanently set**, causing the ships to "weathervane"」。**「towards the stern」是来源自己的措辞，可用。**

**为什么这么设计（一句话）**：把三座主炮塔挤到前面，装甲堡（citadel）长度可以缩短，同样重量的装甲就能堆得更厚——这是在 35,000 t + 16 英寸炮的双重约束下唯一能同时保住火力与防护的办法。详见 `nelson-class.md` §1。

---

## 6. 生涯要点（只列有原句支撑的节点）

| 时间 | 事件 | 来源 |
|---|---|---|
| 1927-12-07 | Devonport 服役，隶属大西洋舰队 | naval-history |
| 1928-03-28 | 正式进入现役 | wiki Rodney |
| 1934-01 | Nelson 在朴茨茅斯搁浅后，Rodney 任临时舰队旗舰（Boyle 上将） | wiki Rodney |
| 1937-05 | 部分舰员参加乔治六世加冕，5-20 参加 Spithead 海上阅兵 | wiki Rodney |
| 1938 | **首装雷达**（Type 79Y），为英海军第二套舰载雷达；原定装 Nelson，因天线位置会挤占舰队司令旗位而改给 Rodney | naval-history：「She was **the first RN battleship to be fitted with any radar** and the **second installation in the Fleet**. Type 79Y… had been intended to go in her sister ship HMS NELSON. However this was changed because the chosen site for the radar aerial would have required the Admiral's flag to occupy an inferior position!」 |
| 1939-12-04 | Nelson 触雷，Rodney 任临时舰队旗舰至 1940-08 | wiki Rodney |
| 1940-04-09 | 挪威外海被 500 kg 炸弹命中：炸穿 4.7 英寸弹药箱角、碎片穿数层甲板后被 4 英寸装甲甲板弹开、厨房起火；3 人伤、15 人电灼伤 | wiki Rodney |
| 1941-05-22 | 护送 MV Britannic 赴 Halifax，原计划随后赴 Boston 大修 | wiki Rodney：「she was scheduled to continue onward to Boston for repairs and a refit」 |
| 1941-05-24~27 | 被调去拦截 Bismarck → 最终战 | 见 §3 |
| 1941-05-29 | 返 Greenock，油舱几乎见底，立即补给 | naval-history |
| 1941-06~08 | Boston 海军船厂改装：换 4 联装 + 2 座八联装 pom-pom 替代后部 6 英寸射击指挥仪；装 Type 281/271/284 | wiki Rodney |
| 1941-08 | Operation Halberd（马耳他运输）；9-27 Nelson 被意机雷击，Somerville 将旗转至 Rodney | wiki Rodney |
| 1942-02~05 | 大改装：加 17 门单装 20 mm、0.5 英寸四联换 Mk III pom-pom 指挥仪、HACS Mk I 换 Mk III、加 Type 273/291/285 | wiki Rodney |
| 1942-08 | Operation Pedestal（马耳他）；被 Ju 87 攻击，一发穿甲弹被 X 塔顶弹开 | wiki Rodney |
| 1942-11 | Operation Torch（奥兰）；对 Fort du Santon 岸炮射 16 发 | wiki Rodney |
| 1943 | Husky（西西里）、Baytown（意大利） | wiki Rodney |
| 1944-06-06 | 诺曼底：对 Le Havre 岸炮射 2 发穿甲弹；夜间撞沉 LCT 427（13 人全亡） | wiki Rodney |
| 1944-09 | 护送 JW 60 / RA 60 往返摩尔曼斯克 | wiki Rodney |
| 1944-10-09 | 任本土舰队旗舰（Moore 上将） | wiki Rodney |
| 1945-09-29 | 乔治六世、伊丽莎白王后及两位公主登舰 | naval-history / wiki Rodney |
| 1945-11-30 | Portsmouth 退役 | naval-history |
| 1948-03 | 报废，拖往 Inverkeithing 解体 | 见 §1.5 |

**战功表（battle honours）** —— naval-history 原文：「QUEBEC 1759 - SYRIA 1840 - CRIMEA 1854 - NORWAY 1940 - ATLANTIC 1940-41 - **BISMARCK Action 1941** - MALTA CONVOYS 1941-42 - NORTH AFRICA 1942-43 - SICILY 1943 - SALERNO …」

---

## 7. 涂装 / 编制 / 雷达（本舰相关的可用原句）

- **编制**：1,314（private ship）/ 1,361（旗舰）；1944 年改装后增至 1,631–1,650 —— wiki Rodney：「These additions increased the ship's deep displacement to 43,100 long tons (43,800 t) and **her crew to 1,631–1,650 men**.」
- **1941-05-27 当日实际编制**：**未获取**（无任何来源给当日人数）
- **涂装**：1941-05 具体色号 **未获取**。（`navweaps-camouflage` 未给 Rodney 1941-05 的色号；本报告不按 Home Fleet 通例推填）
- **雷达（1941-05-27 当日）**：**未获取确切清单**。navypedia 的改装记录显示 **8/1941 才**装 Type 271/281/284，1941-05 时按该记录应只有 Type 279（1938 装的 79Y 已在 8/1940 换成 279）。**但 navypedia 给的是「某月改装」的整体口径，不能反推该月之前某一天的状态**，故当日清单记「未获取」。

---

## 8. 未获取字段汇总

**A. 战报本身缺失的（一手材料就这么短，不是没查）**

| 字段 | 状态 | 说明 |
|---|---|---|
| 射击开始/结束的钟点 | **一手未获取** | 战报无任何时刻；§3.1 的时刻全是他源 |
| 命中数 / 逐次命中记录 | **一手未获取** | 战报只记发射数，不记命中。`kbismarck-rodney-report` 只有统计段，完整版报告未找到 |
| 各炮失效的**时刻** | **未获取** | 战报只记「战斗结束时」的状态 |
| 4.7 英寸高炮未开火的**原因** | **未获取** | 战报只陈述 `were not fired` |
| 齐射编号对应的时刻 | **未获取** | Roberts 给了 salvo 64/65/88/97 的编号，但没给时刻 |

**B. 舰体数据类**

| 字段 | 状态 | 说明 |
|---|---|---|
| 型深（depth molded） | **未获取** | navypedia / wiki / naval-history 三源均无 |
| 方形系数 Cb | **未获取** | 同上 |
| 水线面积 | **未获取** | 同上 |
| 干舷（数值） | **未获取** | 只有「上层建筑像后桅帆、逆风偏航」这类定性原文 |
| 装甲总重与占排水量比 | **未获取** | Nelson 级的 armor weight 没有任何已抓来源给出（对照 KGV 有 RMG 的 12,413 t / 32.5%） |
| 主发电机台数与总功率 | **未获取** | 无来源给出 |
| 蒸汽温度 | **未获取** | 只有 250 psi 压力，无温度 |
| 舵角 / 回转直径 | **未获取** | wiki 只有「comparatively small tactical diameter」的定性评语 |
| 防雷系统设计指标的确切口径 | **部分未获取** | 见 `nelson-class.md` §4（3.1 m 与 3.7 m 两种深度并存） |
| 1941-05-27 当日编制人数 | **未获取** | — |
| 1941-05 涂装色号 | **未获取** | — |
| 1941-05-27 当日雷达清单 | **未获取** | navypedia 只有月度改装口径 |
| 单舰精确造价（含/不含首备统一口径） | **未获取** | £6.15M 与 £7.62M 口径不一致，无第三方调和 |
| 主机（汽轮机）承造厂 | **未获取** | 对照 KGV 有 tynebuiltships 给「Vickers-Armstrongs, Barrow」，Rodney 无同类来源 |

**C. 明确「不是未获取」的项（区分「未获取」与「0」）**

| 字段 | 值 | 依据 |
|---|---|---|
| 鱼雷发射管 | **2 具（每舷 1 具），24.5 英寸（622 mm），水下、偏中线 10°** | navypedia：「2 - 622 TT (fwd)」；wiki：「two submerged **24.5-inch (622 mm)** torpedo tubes, one on each broadside, **angled 10° off the centreline**」——**不是 0，是 2** |
| 舰载机弹射器（建成时） | **0** | navypedia 改装记录：「**1936, Rodney: + 1 catapult on turret "X", 1 seaplane**」——即 1936 年才加装，建成时无。**这是真正的 0** |
| 弹射器（1936–1942） | **1 座（X 炮塔顶）** | 同上；「**8/1942, Rodney: - 1 catapult with seaplane**」 |
| 弹射器（1942-08 之后） | **0** | 同上，1942-08 拆除 |
| 40 mm Bofors | **0（战时全程未装）** | navypedia 与 wiki 的 Rodney 改装记录中从无 Bofors；对照 Nelson 1945-01「+ 4 x 4 - 40/56 Bofors」。**这是真正的 0，不要写成未获取** |
| 深水炸弹 | **0（无记录）** | 各来源装备表均无 |

---

## 9. 来源清单

| 缩写 | 来源 id | 等级 | URL | 用途 |
|---|---|---|---|---|
| `[ROD]` | `kbismarck-rodney-report` | **A 一手档案** | https://www.kbismarck.com/rodney-gunnery-report.html | 1941-05-27 炮术战报原文（378/706、各塔分计、齐射统计、X 塔 28 次、三处失效、4.7 英寸未开火） |
| `[INT]` | `admiralty-bismarck-interrogation` | **A 一手档案** | https://www.uboatarchive.net/Int/BismarckINT.htm | 英海军部 C.B. 4051 (24) 战俘审讯（hastened、no shells penetrated、0857 首弹、0902 命中、Rodney 鱼雷 1 命中） |
| `[NW16]` | `navweaps-16in-45-mk1` | D 专题网站（内含 Campbell / Raven & Roberts 转引） | https://www.navweaps.com/Weapons/WNBR_16-45_mk1.php | 16"/45 Mk I 全部炮与炮塔数据、Roberts 转引的故障过程、X 塔射界 |
| `[NW6]` | `navweaps-6in-50-mk22` | D （**本次新建**） | https://www.navweaps.com/Weapons/WNBR_6in-50-mk22.php | 6"/50 Mk XXII 副炮数据、Rodney 实战 150/98 次舷射统计 |
| `[NW47]` | `navweaps-47-40-mk8` | D （**本次新建**） | https://www.navweaps.com/Weapons/WNBR_47-40-mk8.php | 4.7"/40 Mk VIII 高炮数据、175 发/门基数 |
| `[NP]` | `navypedia-nelson` | D 专题网站 | https://www.navypedia.org/ships/uk/brit_bb1_nelson.htm | 两舰建造表、排水/尺寸/动力/装甲汇总、逐次改装记录 |
| `[NH]` | `naval-history-rodney` | C 权威二次文献（官方舰史体例） | https://www.naval-history.net/xGM-Chrono-01BB-HMS_Rodney.htm | 逐日战史、最终战时间线、自身火炮损伤、结局 |
| `[WKR]` | `wiki-en-rodney` | E 百科（仅线索） | https://en.wikipedia.org/wiki/HMS_Rodney_(29) | 造价、绰号、编制、改装、碰撞事故——**只作线索，关键值已回查 C/A 源** |
| `[WKC]` | `wiki-en-nelson-class` | E 百科（仅线索） | https://en.wikipedia.org/wiki/Nelson-class_battleship | 设计动机、装甲方案、GM、横摇周期、100–130 命中估算 |
| `[KB-LB]` | `kbismarck-last-battle` | D 专题网站 | https://www.kbismarck.com/bismarck-last-battle.html | 最终战德方视角时间线、Rodney 停火 1016、鱼雷 6+2 |
| `[HANS]` | `hansard-rodney-cost-1939` | **B 同期官方出版物** | https://api.parliament.uk/historic-hansard/written-answers/1939/mar/15/royal-navy-ship-construction-costs | Rodney 造价 £6,150,000 及「不含首备」口径 |
| `[AWD]` | `kbismarck-admiralty-war-diary` | A 一手档案 | https://www.kbismarck.com/admiralty-war-diary.html（本地 `work/raw/lb-admiralty-diary.txt`） | 380 发 / 716 发、12 鱼雷（补给申请口径） |

**本次新增抓取并落盘的原始件**（供后续复核）：
- `work/raw/nw-16in45-mk1.html` / `.txt`
- `work/raw/nw-6in50-mk22.html` / `.txt`
- `work/raw/nw-47-40-mk8.html` / `.txt`
- `work/raw/navypedia-nelson.html` / `.txt`
- `work/raw/nh-rodney.html` / `.txt`
- `work/raw/nh-nelson.html` / `.txt`
- `work/raw/wiki-rodney.html` / `.txt`
- `work/raw/wiki-nelson-class.html` / `.txt`
- `work/raw/washington-treaty-1922.html` / `.txt`

### 9.1 需要新登记进 `data/sources.yaml` 的来源（本次已核实 200，本报告未改 data/）

已逐一检索过 `data/sources.yaml`：**除 `navweaps-16in-45-mk1` 与 `navweaps-2pdr-mk8` 外，下表全部是新增**（文件里没有 rodney/nelson 的任何 URL 条目）。建议按此登记：

```yaml
  - id: navweaps-6in-50-mk22
    title: 'British 6"/50 (15.2 cm) BL Mark XXII'
    url: https://www.navweaps.com/Weapons/WNBR_6-50_mk22.php
    type: website
    tier: D
    role: [data]
    operator: NavWeaps
    lang: en
    access: direct          # 本次实测直连 200，无需代理
    fetched: 2026-11-21
    license: all_rights_reserved
    note: >
      **Rodney / Nelson 的副炮（炮身为 Mk XXII，炮座为 Mark XVIII）**。
      与已登记的 navweaps-6in-50-mk23 不是一回事——Mk XXIII 是 Town/Fiji/Leander 等巡洋舰的炮。
      页内含 Rodney 打俾斯麦的实战射速：150 次舷射（右舷，5 次/分）+ 98 次（左舷，3.9 次/分），
      首 9 分钟 5.9 发/分、输出率近 100%。注意该页给 716 发，与一手炮术报告的 706 发冲突。

  - id: navweaps-47-40-mk8
    title: 'Britain 4.7"/40 (12 cm) QF Marks VIII and X'
    url: https://www.navweaps.com/Weapons/WNBR_47-40_mk8.php
    type: website
    tier: D
    role: [data]
    operator: NavWeaps
    lang: en
    access: direct          # 本次实测直连 200
    fetched: 2026-11-21
    license: all_rights_reserved
    note: >
      纳尔逊级重型高炮。备弹 175 发/门（Nelson class 专值），含 150 发照明弹 + 20 发目标烟幕弹/舰。
      **Rodney 有一座炮座用齿条式送弹机，仰角限 77°**（本舰独有例外）。
      1941-05-27 打俾斯麦时这 6 门炮全程未开火，见 kbismarck-rodney-report 原文。

  - id: navypedia-nelson
    title: 'NELSON battleships (2, 1927)'
    url: https://www.navypedia.org/ships/uk/brit_bb1_nelson.htm
    type: website
    tier: D
    role: [data]
    operator: Navypedia
    lang: en
    access: direct
    fetched: 2026-11-21
    license: all_rights_reserved
    note: >
      纳尔逊级舰级骨架：两舰建造表、排水/尺寸/动力/装甲汇总，**以及全项目最完整的逐次改装时序**
      （1932–1946 两舰逐月列出加装/拆除的每一门炮与每一部雷达）。
      **装甲总重、型深、方形系数、发电机功率仍无**——该页也不给这些。
      注意其 "Displacement full 41250 (with buoyancy spaces filled)" 不是满载，不可与 wiki 的 37,430 lt 并列。
      URL 陷阱：brit_bb_nelson.htm 是 404，正确路径带 bb1。

  - id: naval-history-rodney
    title: 'HMS RODNEY — Royal Navy ship history'
    url: https://www.naval-history.net/xGM-Chrono-01BB-HMS_Rodney.htm
    type: website
    tier: C
    role: [data, narrative]
    operator: naval-history.net (Gordon Smith)
    lang: en
    access: direct
    fetched: 2026-11-21
    license: all_rights_reserved
    note: >
      逐日战史，最终战时间线最细（0843 发现 / 0847 开火 / 0901 第 4 次齐射 2 命中 / 0916 鱼雷 /
      0930 火控失效被迫抵近 6000 yd / 1014 停火 / 1039 沉没序列）。
      **也含自身火炮造成损伤的原文**（松木甲板被掀、铸铁水管爆裂进水）。
      页内 6 英寸消耗记 716 发，与一手报告的 706 冲突。

  - id: naval-history-nelson
    title: 'HMS NELSON — Royal Navy ship history'
    url: https://www.naval-history.net/xGM-Chrono-01BB-HMS_Nelson.htm
    type: website
    tier: C
    role: [data, narrative]
    operator: naval-history.net (Gordon Smith)
    lang: en
    access: direct
    fetched: 2026-11-21
    license: all_rights_reserved
    note: >
      Nelson 建造与结局。**唯一给出 1948 年作轰炸靶标试验、1949-03-15 拖抵 Inverkeithing 的来源**
      （wiki 只给 "1949"）。含触雷、被意机雷击等战损逐日记录。

  - id: wiki-en-nelson-class
    title: 'Nelson-class battleship'
    url: https://en.wikipedia.org/wiki/Nelson-class_battleship
    type: website
    tier: E
    role: [narrative]
    operator: Wikipedia
    lang: en
    access: direct
    fetched: 2026-11-21
    license: cc_by_sa
    note: >
      **⚠️ 本级舰体数据的唯一「全」来源，属 tier E，可靠性必须打折。**
      有用的部分：设计动机（DNC 原话 "everything is to be cut down to a minimum"）、
      省重量手段逐条、装甲方案分层、GM 3.1 m、横摇 11.2–13.6 s、操纵性（Binney 与反对意见并列）、
      Rodney 100–130 命中的估算（**估算，非数据**）。
      它的脚注指向 Burt / Raven & Roberts / Brown / Konstam，**真正该引的是一手书，本次未能直接取到**。

  - id: wiki-en-rodney
    title: 'HMS Rodney (29)'
    url: https://en.wikipedia.org/wiki/HMS_Rodney_(29)
    type: website
    tier: E
    role: [narrative]
    operator: Wikipedia
    lang: en
    access: direct
    fetched: 2026-11-21
    license: cc_by_sa
    note: >
      Rodney 单舰：造价 £7,617,799（与议会 £6,150,000 冲突）、绰号、编制、逐次改装、
      撞击 LCT 427 事故、自身火炮损伤。**其"建造数据表"在 Rodney 行有排版残缺**（Ordered/Laid down/Launched 三格空白），
      不可用作独立来源。

  - id: washington-treaty-1922
    title: 'Washington Naval Limitation Treaty, 1922 (full text)'
    url: https://www.ibiblio.org/pha/pre-war/1922/nav_lim.html
    type: document
    tier: A
    role: [data, narrative]
    operator: ibiblio.org (条约原文转录)
    lang: en
    access: direct
    fetched: 2026-11-21
    license: public_domain
    note: >
      **解释纳尔逊级为什么长成这样的第一手依据。**
      Art.II：英国可造 two new capital ships not exceeding 35,000 tons，代价是拆掉 Thunderer/KGV/Ajax/Centurion；
      Art.V：35,000 t 上限；Art.VI：16 英寸口径上限。
      **并给出"标准排水量"不含燃油与锅炉给水**——这正是本级能做内部注水防雷舱（而非外置防雷突出部）的条约漏洞。
```

### 9.2 ⚠️ 一个极易踩的型号混淆：Mk XXII（炮身）vs Mark XVIII（炮座）

纳尔逊级的 6 英寸副炮，**炮身与炮座是两个不同编号，来源写法不统一**：

| 来源 | 写法 | 指什么 |
|---|---|---|
| navweaps 6"/50 Mk XXII 页 | `Designation: 6"/50 (15.2 cm) BL Mark XXII` / `Mount: Nelson (6): Mark XVIII` | **炮身 Mk XXII，炮座 Mark XVIII** |
| navypedia 初始装备表 | `6 x 2 - 152/50 BL Mk XXII` | 炮身 |
| navypedia 1946 状态 | `6 x 2 - 152/50 Mk XVIII` | **跳到炮座编号了** |
| `last-battle.md` | `6"/50 Mark XXIII` | **完全错**（见 §0.1） |

**引用规则**：写「Rodney 装了 12 门 6 英寸炮」时，型号写 **Mk XXII**（炮身）或 **Mark XVIII**（炮座），**绝不能写 Mk XXIII**。两舰 1946 年状态都记为 Mk XVIII 是**换了炮座编号的写法**，不代表换了炮。

---

**抓取失败 / 未取到的来源**：
- `https://www.kbismarck.com/rodney.html` → **404**（任务书已指出，实测确认；该站无 Rodney 舰船专页）
- `https://www.navypedia.org/ships/uk/brit_bb_nelson.htm` → 404（正确路径是 `brit_bb1_nelson.htm`）
- `https://www.navweaps.com/Weapons/WNBR_2pdr_mk8_octuple.php` → 404（八联装 pom-pom 页路径不同，本次未取得；Rodney 的 pom-pom 数量与改装节点改用 navypedia 改装记录）
- **Rodney 完整版炮术报告**（非 "Preliminary" 的那一份）→ 未获取，试过 kbismarck 的档案索引页（`work/raw/kb-archives-index.txt`）无此件
