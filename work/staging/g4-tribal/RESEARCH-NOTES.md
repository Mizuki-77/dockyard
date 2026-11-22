# 调研底稿 —— 部族级（Tribal class）四艘
## HMS Cossack / Maori / Zulu / Sikh

> g4-tribal · 2026-11-22 · 调研 subagent 交付
>
> 本文件按 SCHEMA.md §11 的格式写。每条结论后面带英文原句与 URL。
> **主会话只读「交付摘要」「卡住的地方」「有争议的记载」三节也能独立看懂**，
> 但「任务表更正」一节务必先读 —— 里面列的是下发任务书里写错的条目。

---

## 0. 任务表更正（先读这一节）

下发任务书给了四艘舰的「关键战史 / 结局」表格，并明确要求逐条核实。
核实结果：**Cossack 与 Maori 完全正确；Zulu 的沉没原因需修正；Sikh 那一行几乎全错。**

### 0.1 HMS Cossack —— ✅ 全对

| 项 | 任务表 | 核实结果 |
|---|---|---|
| 1940-02 阿尔特马克事件，挪威领海强行登船救战俘 | 有 | **正确**，1940-02-16，约辛峡湾，救出 299 人 |
| 1941-05 追击俾斯麦时任第 4 驱逐舰分队旗舰 | 有 | **正确** |
| 1941-05-27 最终战深夜雷击（未命中） | 未命中 | **需细化**：打了两次。0140/27 射 3 条，来源记「观测到 1 条命中」；0335/27 射最后 1 条，明确未命中。任务表只说了后一次 |
| 1941-10 被 U-563 重创，拖带中沉没 | 有 | **正确** |
| 结局 sunk_by_enemy，1941-10-27 | 1941-10-27 | **正确**（另有 1941-10-24 一说，是「判定战损」口径，见争议节） |

### 0.2 HMS Maori —— ✅ 全对

| 项 | 任务表 | 核实结果 |
|---|---|---|
| 1941-05-27 最终战夜间雷击俾斯麦（记有命中宣称，但未证实） | 有 | **正确**。0137/27 射 2 条，原文 "a torpedo hit was observed... A bright glow illuminated the waterline"；0656/27 再射 2 条，明确 "Both missed" |
| 地中海马耳他护航（1941-42） | 有 | **正确** |
| 1942-02 在瓦莱塔港被德国空袭击沉 | 有 | **正确** |
| 结局 sunk_by_enemy，1942-02-12 | 1942-02-12 | **正确**，三源一致 |

### 0.3 HMS Zulu —— ⚠️ 沉没原因需修正

| 项 | 任务表 | 核实结果 |
|---|---|---|
| 1941-05-27 最终战夜间雷击 | 有 | **正确**，0121/27 于 5,000 码射 4 条，全部一次打光 |
| 地中海护航 | 有 | **正确** |
| 1942-09 在托布鲁克外海被意大利空袭击沉 | **意大利**空袭 | **日期正确（1942-09-14），机型归属需改**。见下 |
| 结局 sunk_by_enemy，1942-09-14 | 1942-09-14 | **正确** |

**关于「意大利空袭」：** 三份来源里只有一份提到意大利，且是「意大利/德国混合」，
另外两份明确指向德国 Ju 88：

- navypedia："Zulu was damaged by **German Ju 88 bomber** at Tobruk and sunk 14.9.1942 under tow."
- navy-history eBook 分册："by **Italian/German force** of Ju87 and Ju88 bombers."
- naval-history 单舰页与 uboat.net 单舰页：只写 "enemy aircraft" / "A bomb from an enemy aircraft"，**不指国籍**。

**处理：** fact 的 `construction.fate_type` 取 `sunk_by_enemy`（这点无误），
`note` 里写「德/意空袭（navypedia 明确记德国 Ju 88）」，正文里不写单一国籍。

### 0.4 HMS Sikh —— ❌ 三处错误，必须全改

任务表原文：*「1941-05-27 最终战夜间雷击；1942 年圣纳泽尔突袭（Operation Chariot，荣誉）；1943 年西西里；**1944-04 在的黎波里附近被德国岸防炮击沉**（实为 1944-04-14 于突尼斯外海被德军岸炮击沉）」，结局 `sunk_by_enemy`（1944-04-14）。*

| 项 | 任务表 | 核实结果 |
|---|---|---|
| 1941-05-27 最终战夜间雷击 | 有 | **正确**，0218/27 于停车的俾斯麦射 4 条，「相信获得一次命中」 |
| **1942 年圣纳泽尔突袭（Operation Chariot）** | 有，且标「荣誉」 | **❌ 错误。没有任何来源支持 Sikh 参加 Chariot。** 见下 |
| **1943 年西西里** | 有 | **❌ 错误。本舰 1942-09-14 已沉没，不可能参加 1943 年的任何行动。** |
| **1944-04 在的黎波里附近被德国岸防炮击沉** | 有 | **❌ 错误。实为 1942-09-14 在托布鲁克外海被德国岸防炮击沉。** |
| **1944-04-14 于突尼斯外海被德军岸炮击沉** | 括号里的「更正」 | **❌ 同样错误。日期、地点都不对。** |
| 结局 sunk_by_enemy，1944-04-14 | 1944-04-14 | **❌ 应为 1942-09-14**（三源一致） |

**逐条证据：**

**（1）圣纳泽尔突袭 —— 两条独立证据链都排除本舰：**

① Chariot 的参战序列里没有她。Wikipedia「St Nazaire Raid」条目的
units involved 列出：HMS Campbeltown、HMS Tynedale、HMS Atherstone、
HMS Sturgeon、MGB 314、MTB 74、第 28/7/20 摩托艇分队。
公开的 Chariot 记述（operation-chariot.org、VCGCA 的 A. C. Newman 传略、
CWGC 专题）一律只提 Campbeltown、Tynedale、Atherstone 三艘驱逐舰。

② 她自己的年表在 1942 年 3 月明确记在地中海东部：
naval-history 的 Sikh 页把 1942-03 记为参与 MF8（03-10 自亚历山大出击）、
罗得岛炮击（03-15，"Between 0130B/15 and 0145B/15 military installations
were bombarded on Rhodes"）、MG1 与第二次锡尔特（03-20 起护航 MW10）。
uboat.net 的单舰行动记录同样把 03-10、03-14/15、03-20 三次行动逐条列出。
Chariot 是 1942-03-28，那一天她在亚历山大。

**结论：任务表把「Chariot」错记在本舰名下。** 本组**没有**写入这条，
`ships/sikh.yaml` 里不含任何 Chariot 相关内容。

**（2）1943 年西西里 —— 时间上不可能：**
naval-history："SIKH, 14th September 1942, Eastern Mediterranean, off Tobruk,
eastern Libya - by German shore batteries."
navypedia："Sikh was sunk by German coastal battery at Tobruk 14.9.1942."
uboat.net："Lost 14 Sep 1942"。
三源一致，本舰 1942 年 9 月即已沉没。

**（3）1944-04 的黎波里 / 突尼斯 —— 实为 1942-09-14 托布鲁克：**
naval-history eBook 分册："SIKH, 14th September 1942, Eastern Mediterranean,
off Tobruk, eastern Libya - by **German shore batteries**. Landing Royal
Marines for British combined operations raid on Tobruk."
navypedia："Sikh was sunk by **German coastal battery at Tobruk** 14.9.1942."
uboat.net 给出逐发命中记录（六发 88 mm 炮弹）与沉没位置 32°05'N 24°00'E。

的黎波里（Tripoli）在利比亚西部，托布鲁克（Tobruk）在利比亚东部，
相距一千余公里；突尼斯在更西边。三者不是同一片海。

**（4）任务表内部的「更正」也错了：**
「实为 1944-04-14 于突尼斯外海」——这个更正虽然把地点从的黎波里挪到了
突尼斯，但日期与原因仍然错。**这一类「以为自己在纠错、实际错在另一处」
的情况最危险**，因为读者会以为已经核过了。

---

## 1. 舰级骨架（classes/tribal.yaml）

### 1.1 这一级为什么长成这样

> "The Tribal class destroyers trace their roots to 1934 when the British
> Admiralty evaluated the threat posed by much larger destroyers being built
> in Japan, Italy and even Germany than the Royal Navy had. These ships were
> all around 2000 tons while the British destroyers were closer to 1300 tons."
> —— uboat-tribal-class
> https://uboat.net/allies/warships/class/1.html

> "'Tribal' class ships became the answer of Britain to occurrence in navies of
> probable opponents of large destroyers appreciable exceeding on armament
> standard British destroyers with their four 120mm guns. A starting point in
> designing of the new ship began requirement of Admiralty to place powerful
> armament including **ten 120mm guns** that should ensure the superiority over
> new foreign destroyers, such as Japanese Fubuki (3x2 127mm guns and 3х3 TT)."
> —— navypedia-tribal
> https://www.navypedia.org/ships/uk/brit_dd_tribal.htm

> "By basic design working out it has appeared what to fulfil all requirements
> within the limits of the resolved displacement (1850t was an upper limit for
> leaders according to decisions of the London conference) is impossible, and
> after considering of numerous variants were stopped on the design with 8
> 120mm guns, two quadruple 40mm pompoms (**one was excluded from the
> specification already after the bulding beginning**) and 1 quadruple TT."
> —— navypedia-tribal

> "The Tribal was finally accepted after **no less than 8 design proposals**."
> —— uboat-tribal-class

**要点（写进舰级的 identity.building_program）：**
十门炮的要求在 1,850 t 的领舰上限内放不下 → 降到八门 →
两座 pom-pom 也删掉一座。本级是「要求被吨位反复砍」的产物，
不是一次性设计出来的。

### 1.2 造价与订购节奏

> "Estimated cost per ship was 340,000 pounds excluding Admiralty supplied
> armaments putting the average cost around **520,000**."
> "The first 7 Tribals were ordered on 10 March, 1936 with the latter group of
> **9 Tribals being ordered on 9 June**."
> —— uboat-tribal-class

> "The ships were formed into the 1st and 2nd Tribal destroyer flotillas.
> By 1939 the Royal Navy had learned that while the Tribals were larger they
> were just normal destroyers. Thus the flotillas were renamed 4th and 6th
> destroyer flotillas."
> —— uboat-tribal-class

这条「1939 年皇家海军自己认为部族级只是普通的、更大的驱逐舰」很重要，
它解释了为什么本组四艘舰的分队编号会在 1939-04 从「第 1/2 部族分队」
改成「第 4/6 驱逐舰分队」。写进了每艘舰的 `service.unit`。

### 1.3 主尺度与排水量（两源并列，不裁决）

| 项 | navypedia | uboat.net | 本站取值 |
|---|---|---|---|
| 全长 oa | 114.9 m | 377 ft = 114.9 m | 114.9 m（一致） |
| 垂线间长 pp | 108.4 m | — | 108.4 m |
| 宽 | 11.1 m（"Breadth"） | — | 11.1 m（按最大宽登记） |
| 吃水 | 3.96 m（"later 4.16"） | — | 3.96 m |
| 标准排水量 | **1,959 t** | **1,883 tons** | **两条都登记** |
| 满载 | 2,519 t（"later 2,710"） | 2,559 t | 2,519 t + note |
| 功率 | 44,000 hp | 44,000 HP | 44,000 hp（一致） |
| 航速 | 36.25–36.5 kn | 36 knots | 设计 36 / 最大 36.5 分列 |
| 编制 | 190–250 | 190（四艘旗舰 219） | 190 + note |
| 燃油 | 505–516 t | — | 516 t |
| 续航 | 5,700 nm @ 15 kn | — | 成对登记 |

**⚠️ 1,959 vs 1,883 这 76 t 的差怎么解释 —— 不知道，故并列。**
值得记一笔的可能性：1930 年代英国文献惯用长吨（long ton），
1,870 lt ≈ 1,900 t，1,959 t 也接近 1,928 lt。但**两个来源都没写单位口径**，
所以图上表的换算只是提示，**没有据此改写任何数值**。

任务书给的「标准排水量约 1,870 t」在两份来源里都查不到直接对应值，
第三条常见值（1,870 t）本组未取到可引的原始页，故不作为 fact 登记。

**⚠️ navypedia 表头是两列并排**（"as completed" 与
"Canadian ships modernization 1951-55"），把第二列的值（2,200 t / 11.4 m）
当成部族级的值会全错。本组一律取第一列。

**⚠️ uboat.net 把排水量单位写成 "BRT"** —— 这是容积吨位，
军舰不适用。数值本身应理解成吨位数字，`unit` 按 `t` 记，note 里说明来源标注有误。

### 1.4 武备概览（两源互证，逐项一致）

> navypedia："RN ships: 4 x 2 - 120/45 QF Mk XII, 1 x 4 - 40/39 2pdr QF Mk VIII,
> 2 x 4 - 12.7/62, 1 x 4 - 533 TT, 2 DCT, 1 DCR (30 DC)"

> uboat.net："Armament 8 4.7" guns (4x2) / 4 x 2pdr AA (1x4) / 8 0.5" MG AA (4x2)
> / 4 21" torpedo tubes (1x4)"

两源在八个数字上完全吻合：8 门主炮（4 座双联）、4 门 2-pdr（1 座四联）、
8 门 12.7 mm（2 座四联）、4 管鱼雷（1 座四联）、深弹 30 枚。

**注意鱼雷只有 4 管。** 同期英国驱逐舰是 8 管（2 座四联），
这是本级为了主炮砍掉的另一半火力，写进了 `armament.torpedo.tubes` 的 note。

---

## 2. 主炮 4.7"/45 QF Mk XII（weapon id: `47in-45-mk12`）

### 2.1 来源 URL 的问题（与 g7-weapons 组一致）

- 任务书给的 `WNBR_47-45_mk12.php` → **实测 404**。
- 正确页是 `WNBR_47-45_mk9.php`，标题即
  "4.7"/45 (12 cm) QF **Mark IX and Mark XII**" —— 两型同页。
- 该来源已由 **g7-weapons 组**登记为 `navweaps-4-7in-45-mk12`，
  **本组不重复登记**，只在 sources-fragment 的注释里标明引用关系。

> **⚠️ 与老炮的区分（任务书特别强调的一点）：**
> `data/sources.yaml` 里已有一条 `navweaps-4-7in-40-mk8`
> （`WNBR_47-40_mk8.php`），那是 **4.7"/40 Mark VIII** ——
> 纳尔逊级与 KGV 级的高射炮，与部族级的 4.7"/45 Mark XII **不是同一门炮**。
> 本组全部武器参数引 `navweaps-4-7in-45-mk12`，一处都没引错。

### 2.2 关键原句

> "The **almost identical Mark XII** was designed for use in **twin mountings**
> and differed from the Mark IX in being **slightly heavier and longer**."
> "Both Marks fired separate ammunition, otherwise they were similar to the
> preceding 4.7" (12 cm) BL Mark I."

> "**The lack of a DP function for these weapons was keenly felt throughout the
> war as more British destroyers were sunk by air attack than from any other
> cause.** What little AA capability that these weapons did have was hindered
> by a lack of a tachymetric (predictive) fire control system and the setting of
> HE time fuzes by hand."

> "The **CPXIX twin mounting was the first British power mounting specifically
> designed for destroyers.**"

> "The Tribal class had their four CPXIX mountings **split in two groups, each
> powered by a 140 HP steam turbine and oil hydraulic pump**. The J, K and N
> classes had a 70 HP electric motor and pump on each individual mounting."

> "Guns **shared a cradle and could not elevate independently**."
> "The gun axes were 38 in (96.5 cm) apart."

> "Each mounting had two dredger projectile hoists which ran vertically from the
> shell rooms to the deck below the guns **except for 'Y' mounting on the Tribal
> class where the hoists terminated on the upper deck**."

> "As these were all open mountings, **bad weather conditions** such as
> experienced by many of these ships on Arctic convoy duty during World War II
> **greatly reduced the ROF figures** given above."

### 2.3 数据表（照录，未换算方向错误）

| 项 | Mark XII | Mark IX（对照，勿混） |
|---|---|---|
| 炮身重 | 3.238–3.245 t（3,290–3,297 kg） | 2.963–2.984 t（3,011–3,032 kg） |
| 身管全长 | 224.08 in（5.692 m） | 220.62 in（5.604 m） |
| 膛线长 | 5.400 m（两型共用） | 同 |
| 膛径 | 4.724 in（12 cm） | 同 |
| 药室容积 | 628 in³（10.29 dm³） | 同 |
| 弹重 | HE 50 lb（22.68 kg）/ SAP 50 lb | 同 |
| 初速 | 2,650 fps（808 mps） | 同 |
| 射速 CPXIX | 10–12 发/分 | — |
| 身管寿命 | 1,400 发 | 同 |
| 射程 | 30° 15,800 yd（14,450 m）/ 40° 17,000 yd（15,545 m） | 同 |
| 仰角 CPXIX | −10 / **+40°** | — |
| 射界 CPXIX | ±160°（J/K 级的 X 炮座 ±170°） | — |
| 炮座重 CPXIX | 25.09 t（25.50 mt） | — |
| 弹药基数 | **Tribals: 200 SAP + 50 HE + 50 星弹 = 300 发/舰** | 其他舰未给 |
| 产量 | **372 门**（Mark XII 各型） | 742 门 |

**弹药基数 300 发/舰 这条要特别说明：** 这是**全舰**基数，不是每炮基数。
八门炮平均 37.5 发/门，比同期巡洋舰的每炮基数低得多。
写进 `weapon.ammo_outfit` 时 note 明确标注「全舰，不是每炮」。

**倍径计算法：** 该页未明说，但膛线长 5.400 m ÷ 0.120 m = 45，
与型号中的 45 吻合；若按身管全长 5.692 m 算则得 47.4，与型号不符。
故 `weapon.caliber_method` 取 `usa_uk_method`，note 里写明推算依据。
**这是推断，已在 note 里标明。**

### 2.4 炮位实体（四座）

按英式字母命名 A / B / X / Y，登记为 `mount:tribal-a/b/x/y`。
A、B 在前（B 为背负），X、Y 在后（X 为背负）。
**未获取：** 逐座的 frame 位置、实际射界限制角、
各座的测距仪数量与基线（navweaps 只说 CPXIX 有 96.5 cm 炮轴间距，
未给指挥仪配置）。这几项整条不写。

---

## 3. 四艘舰：逐舰结论与原句

### 3.1 HMS Cossack（F03 / G03）

**建造**

> "TRIBAL-Class Fleet Destroyer ordered on **10th March 1936** under the 1935
> Build Programme. The contract for the hull and engines was placed with
> Vickers-Armstrong at Newcastle and the ship was **laid down on 9th June 1936**.
> Launched on **8th June 1937** ... Build of this destroyer was completed on
> **7th June 1938** and she commissioned for service in the 1st Tribal Destroyer
> Flotilla"
> —— naval-history-cossack
> https://www.naval-history.net/xGM-Chrono-10DD-34Tribal-HMS_Cossack1.htm

**阿尔特马克事件**

> "At 2312hours, Cossack approached the German ship. A boarding party consisting
> of **three officers and thirty men** was ready to move on a moment's notice.
> While coming alongside, the big tanker tried to crash her heavy stern into the
> destroyer's thin plates. Expert seamanship saved the Tribal from serious
> damage. Before Altmark was seized, **four Germans were killed and five
> wounded**. When the boarding party searched the ship, they discovered and
> rescued **299 captives** in the hold of the ship."
> —— uboat-cossack
> https://uboat.net/allies/warships/ship/4423.html

> "16th After interception of ALTMARK by HMS INTREPID and HMS IVANHOE boarded
> German ship in **Joessing Fjord. Norway** and released the **299** British
> seamen held on board. ... Sustained slight structural damage to bows during
> boarding."
> —— naval-history-cossack

两源在 299 这个数字上完全一致 → confidence B。
**299 是精确数，不是「约三百」**，正文里单独写了一段强调这点。

**纳尔维克（1940-04-13）**

> "2nd Battle of Narvik. Engaged and sank German destroyer **ERIC GIESE** with
> HMS FOXHOUND. Engaged crippled German destroyer **DIETHER VON ROEDER** with
> the other two Home Fleet destroyers and **hit by nine 5in shells** in return
> fire before enemy destroyer sank. Sustained serious damage with **11 killed
> and 23 of ship's company wounded**. One shell exploded in forward structure
> killing all of the ammunition supply party for 'A' gun. Other hits in Boiler
> Rooms and consequential damage disabled ship which **grounded** as then unable
> to manoeuvre."
> —— naval-history-cossack

与 navypedia 的「4 发 127 mm」冲突 → **两说并列，见「有争议的记载」§5.1**。

**皇家海军驱逐舰的第一部雷达（本组最重要的一条设备记录）**

> "（Note: Refit work included: Installation of **Radar Type 286**, which was an
> RAF air/surface equipment modified for naval use and **the first radar outfit
> to be fitted in RN destroyers**.）"
> "**Twin 4.7in mounting in X position was replaced by twin 4in HA mounting** and
> modifications were made to other ship services."
> —— naval-history-cossack（1940-05 至 1940-06 改装段）

> "（Note: Repair included docking for structural work on plating and
> modification of accommodation in view of the **increase in complement to 236**
> because of changes in equipment fit. **Type 286 radar modified to allow use of
> a rotating aerial unit**.)"
> —— naval-history-cossack（1941-01-07 至 1941-02-20 改装段）

**这两条只出现在 naval-history**，uboat.net 与 navypedia 都没有。
「第一」这种断言（first radar outfit in RN destroyers）单源支撑，
故 `sensors.radar.installed` 的 confidence 记 B 而非 A，
正文里保留原话并标明出处。**没有把它写成无来源的「世界第一」。**

**俾斯麦夜战（1941-05-26/27）—— 本组四舰共用同一份战役叙述**

> "At this time HMS Zulu was in touch with her ... At 2342 hours the Bismarck
> opened fire on **HMS Cossack**, then about 4 miles to the south-south-west and
> **shot away her aerials**."
> "at **0140/27**, only three minutes after Maori had fired two torpedoes,
> **Cossack launched three torpedoes from 6000 yards** ... **One torpedo was seen
> to hit.** Flames blazed on the forecastle of the Bismarck after this hit but
> they were **quickly extinguished**."
> "At **0335/27**, HMS Cossack made another attack **firing her last remaining
> torpedo** from a range of **4000 yards**. It **missed**."
> —— uboat-cossack（与 naval-history-cossack 同源同文）

**⚠️ 任务表写「1941-05-27 于最终战中深夜雷击（未命中）」—— 不完整。**
实际是两次攻击：第一次 3 条、来源记「观测到命中」；第二次 1 条、明确未命中。
fact 里两条都写，正文专门用一段讲「观测到命中」与「确认战果」的区别。

**沉没（1941-10-23 → 10-27）**

> "On the night of the 23rd, she was at the rear of the convoy when a torpedo
> from **U-563** hit forward of the bridge **killing Captain Berthon and 158 of
> his officers and men**. A further **29 were injured**. Ammunition had exploded;
> No.1 boiler room was flooding and the survivors abandoned ship using Carley
> floats. The Commodant Duboc and the Legion picked them up however **the Cossack
> did not sink** and was reboarded and towed by the Tug Thames after damage
> control teams managed to effect repairs, again however due to the worsening
> weather their efforts were in vain and she **foundered on the 27**."
> —— uboat-cossack

> "23rd Under attacks by submarines of BRESLAU Group during which ship was hit by
> torpedo from U563 in position **35.36N 10.04W** whilst stationed astern of
> convoy. Structure forward of bridge demolished killing the Captain and **158**
> of ship's company. ... **27th Weather worsened and personnel taken on board HMS
> JONQUIL before ship sank at 1043 in position 35.12N 08.17W.**"
> —— naval-history-cossack

**但 uboat.net 的舰页信息栏与 U 艇战果表写的是：**

> "Lost **24 Oct 1941**"
> "Sunk on **24 Oct 1941** by U-563 (Bargsten)."

→ **同一来源内部两个日期并存**（叙述正文写 27 日沉没，信息栏写 24 日损失）。
这不是跨源冲突，是「判定战损日」与「实际沉没日」两套口径。
**两说并列，见 §5.2。**

### 3.2 HMS Maori（F24 / G24）

**建造与造价**

> "TRIBAL-Class Destroyer ordered from Fairfield Shipyard at Govan, Glasgow on
> **10th March 1936** under the 1935 Build Programme and laid down on **6th July
> 1936**. The ship was launched on **2nd September 1937** as the 2nd RN ship
> introduced in 1909 ... Build was completed on **30th November 1938**.
> **Tender cost was £340,622** which excluded items supplied by the Admiralty,
> such as weapons and communications outfits."
> —— naval-history-maori
> https://www.naval-history.net/xGM-Chrono-10DD-34Tribal-HMS_Maori.htm

**服役日的两说**（见 §5.3）：naval-history 把 1938-11 整段记为
"Contractors trials and **commissioning** for service"，uboat.net 记
"Commissioned **2 Jan 1939**"。两条并列。

**纳姆索斯（1940-05-02）**

> "During this operation, Maori was bombed by German aircraft. **Two bombs, both
> fitted with screamers burst alongside**; one to port abreast of the bridge and
> the other to starboard near the torpedo tubes. **Both motor boats and a whaler
> were blown to pieces.** Splinters pierced the hull, the funnels, and the
> superstructure. **About twenty men were injured, five dying of their wounds.**"
> —— uboat-maori
> https://uboat.net/allies/warships/ship/4425.html

**X 炮座换装（1940-12 / 1941-01）**

> "（Note: **X twin 4.7in mounting was replaced by twin 4in AA mounting**. Similar
> change was made in other ships of the Class **to overcome the lack of suitable
> defence against air attacks as established during the operations in Norway**.)"
> —— naval-history-maori

这句话是全级改装的官方理由，比 navypedia 的干巴巴改装表有用得多，
写进了 slices/maori.yaml 与 articles。

**邦角（1941-12-13）**

> "13th - Following receipt of information about passage of Italian cruisers to
> North Africa carried out interception of **ALBERICO DA BARBIANO** and
> **ALBERTO DI GUISSANO** off Cape Bon. 14th - Engaged enemy ships which were
> sunk in a **brilliantly executed night torpedo attack**. Destroyer CIGNO which
> was in company escaped."
> —— naval-history-maori

> "Carried out attacks by torpedo and surface gunfire with the other three ships.
> DA BARBIANO hit by torpedoes and sunk. DI GUISSANO hit and set on fire but sank
> later. **960 Italians were lost with these two ships and 650 rescued by an
> Italian Torpedo Boat (CIGNO)**."
> —— naval-history-sikh（伤亡数字只在这一份里）

**沉没（1942-02-12）**

> "On **12th February 1942 at 0200hours**, while anchored at Malta, HMS Maori was
> attacked from the air and **a bomb found its way into her engine and gear
> room**. The Tribal **blew up and sank, still moored at the emergency destroyer
> buoy at the entrance to Dockyard Creek**. Crews from other ships helped in the
> rescue work as blazing oil spread across the water. **Since off-duty personnel
> customarily slept ashore in shelters while in Malta, only one man was killed
> in the attack.**"
> —— uboat-maori

> "12th - Whilst moored in Grand Harbour, Malta at extended notice, hit by bomb
> during night air raid. Serious damage caused fire which resulted in **explosion
> in Torpedo Head magazine**. Ship sank at mooring."
> —— naval-history-maori

**两源对「炸弹落点」的说法略有不同**：
uboat.net 说落进机舱与齿轮舱，naval-history 说引发鱼雷战斗部弹药库爆炸。
这两者不必然冲突（炸弹击中机舱后可能引燃并导致弹药库爆炸），
但也没有一份来源说清先后。**fact 里写 uboat.net 的落点，note 里补
naval-history 的弹药库爆炸，不合并因果。**

**残骸处理（两说）**

> "By the end of 1942, the Admiralty decided that her wreck should be **lifted,
> moved out of Grand Harbour and set down off Sliema**. On **5 July 1945**,
> Maori's hulk was **scuttled finally in deep water** far away from the harbour."
> —— uboat-maori

> "Later in 1942 the wreck was raised and moved to Sliema Creek where it was
> scuttled. **During May 1945** the hulk was again raised and taken to a position
> off Malta where it was sunk."
> —— naval-history-maori

→ 1945-05 vs 1945-07-05，**两说并列**（见 §5.4）。

### 3.3 HMS Zulu（F18 / G18）

**建造与 lead ship 身份**

> "TRIBAL-Class Fleet Destroyer ordered from Stephens of Govan on **10th March
> 1935** under the 1935 Build Programme. The ship was laid down on **10th August
> 1936** and launched on **23rd September 1937** ... Build was completed on
> **7th September 1938** at a contract price of **£351,135**. **Because of speedy
> construction achieved, she was nominated as Lead Ship for this Class.**"
> —— naval-history-zulu
> https://www.naval-history.net/xGM-Chrono-10DD-34Tribal-HMS_Zulu.htm

> "There was always something different about HMS Zulu. **Perhaps being launched
> with boilers and funnels in place makes a happy ship.**"
> —— uboat-zulu
> https://uboat.net/allies/warships/ship/4428.html

**⚠️ naval-history 的「1935年3月10日下单」是错的。**
同站 Cossack 页写 1936-03-10，uboat.net 全部四艘的 Zulu 写 1936-03-10。
同批七艘不可能一发 1935、一发 1936。fact 按 1936-03-10 登记，
1935 视为「1935 年造舰计划」的程序年度被误写进日期栏。

**服役日两说：** naval-history 记 "**6th** Commissioned"（1938-09-06），
uboat.net 记 "Commissioned **7 Sep 1938**"，navypedia 记 9.1938。
差一天，fact 取 uboat.net，note 里并列。

**1942-03-22 第二次锡尔特 —— 结构损伤**

> "Took part in **brilliant handled tactical night engagement** resulting in
> withdrawal of the greatly superior Italian fleet. ... **Sustained structural
> damage due to high speed manoeuvring during this action**"
> —— naval-history-zulu

配合 navypedia 对本级缺点的评价：

> "Structurally, except transition to heavier twin main gun mounts, application
> of yacht stem instead of straight one ... and using of 30% more powerful
> machinery, 'Tribal' essentially did not differ from the predecessors: the same
> internal arrangement and **the same traditional framing**. **Lastter also became
> the main lack of these in remaining very successful ships.**"
> —— navypedia-tribal

→ 「高速机动导致结构损伤」不是孤例，是本级骨架强度不足的直接体现。
这条写进了 articles/zulu.yaml 的一段，是全组少有的「设计缺陷被实战证实」的证据。

**托布鲁克与沉没（1942-09-14）**

> "For the better part of 1942, Zulu was attached to Force H at Gibraltar ...
> HMS Zulu (Cdr. Richard Taylor White, DSO and Bar, RN) and HMS Sikh's final
> operation together was the attack on Tobruk, Libya on **13/14th September
> 1942**. As a result of shelling from coastal batteries, Zulu was hit but she
> could still make 30 knots. Her crew had been at full watch since dusk on the
> 13th and daylight on the 14th did not bring any rest. In spite of surviving
> multiple bomb attacks during that day, Zulu was **mortally wounded at
> 1600hours. A bomb from an enemy aircraft had pierced her side and exploded in
> the engine room**, thus flooding it along with #3 Boiler Room and the Gear
> Room. She stopped dead in the water and settled two feet deeper. HMS Croome
> came along side to take off any remaining personnel except for a towing party.
> Zulu was taken in tow by HMS Hursley. By **1900hours**, and only a hundred
> miles from Alexandria, Egypt, she was sinking fast. The towing party was
> rescued after a strafing pass by an enemy aircraft. Suddenly, Zulu rolled to
> starboard and sank in position **32º00'N, 28º56'E**. In both attacks, **twelve
> men had been killed, twenty seven went missing and one was wounded**."
> —— uboat-zulu

> "14th Took HMS SIKH in tow after she had been seriously damaged by shore fire.
> HMS SIKH sank during towing operation. Under heavy air attacks during which HMS
> COVENTRY was set on fire and had to be abandoned. **Sank HMS COVENTRY.** ...
> Sank **in position 32.00N 28.56E**. **Twelve** members of the ship's company
> were killed, **24** Missing and one injured."
> —— naval-history-zulu

→ 位置完全一致；**失踪数 27 vs 24 冲突，两说并列**（见 §5.5）。

### 3.4 HMS Sikh（F82 / G82）

**建造、造价、服役早于完工**

> "Tribal-Class Fleet Destroyer ordered from Stephens of Govan on **19th June
> 1936** under the **1936** Build Programme. The ship was laid down on **24th
> September 1936** and launched on **17th December 1937** ... Build was completed
> on **12 October 1938 at a cost of £337,704 5s**. Following a successful WARSHIP
> WEEK National Savings campaign in March this ship was adopted by the civil
> community of Beckenham, Kent."
> —— naval-history-sikh
> https://www.naval-history.net/xGM-Chrono-10DD-34Tribal-HMS_Sikh.htm

> "her builders trials commenced in August 1938 and after being fitted with a
> gyro-compass and other equipment at Chatham, England **she was completed on
> 2 November 1938 even though she had been commissioned a month earlier**."
> —— uboat-sikh
> https://uboat.net/allies/warships/ship/4434.html

→ **1938-10-12 服役、1938-11-02 完工，服役早于完工一个月。**
这是英国造舰的常规两段式流程，不是记录错误。fact 里两条都登记。

**注意：本舰属 1936 年造舰计划，与另外三艘（1935 年计划）不同批。**
这在只入库四艘的情况下是个容易被抹平的差异，写进了 `identity.building_program`。

**1941 年初改装 —— 来源有一处笔误**

> "（Note: Work carried out included **replacement of single 4.7in gun by twin
> 4in mounting** to improve AA defence. Modified RAF air-surface radar fitted
> (**Naval Type 286M.**) This had an aerial fixed to ship structure and was of
> **limited value**.)"
> —— naval-history-sikh

**⚠️「single 4.7in gun」是错的** —— 本级没有单装 4.7 英寸炮，
四座全是双联。同站对 Cossack 与 Maori 的同一改装都写作
"Twin 4.7in mounting in X position was replaced by twin 4in HA mounting"。
fact 按「X 炮座换装」登记，笔误记进 §6。

**俾斯麦夜战（本舰独有的一处细节）**

> "HMS Sikh, however, who had lost sight of the enemy half an hour previously,
> had observed her firing at HMS Cossack and now succeeded in shadowing from
> astern until 0020/27 when the enemy made a large alteration to port and
> commenced firing at her. HMS Sikh altered course to port, intending to fire
> torpedoes, but **the view of the Torpedo Control Officer was obscured by shell
> splashes** and Sikh then withdrew to the southward."
> "Four torpedoes were fired at **0218/27** at the stopped battleship. **It is
> believed that one hit was obtained.** After this attack Sikh remained in radar
> contact with the enemy until **0359/27**."
> —— uboat-cossack（战役叙述，含本舰段落）

**托布鲁克沉没（1942-09-14）—— 本组最重要的一份叙述**

> "On 12/13th September, HMS Sikh (Capt. St John Aldrich Micklethwait, DSO and 2
> Bars, RN) and HMS Zulu were supporting an assault off the coast of Africa.
> While picking up troops in boats at **0505hours**, a searchlight on shore
> suddenly lit up HMS Sikh. Quickly, HMS Zulu moved away, then came in bow first
> into the searchlight. **Shore batteries opened fire. One 88mm shell exploded
> in Sikh's Gear Room**, damaging the lubrication feed system and the steering
> gear. **A second hit forward, blew up the ready-use ammunition locker for 'A'
> gun** and started a fierce fire that killed, burned, or disabled all of the
> Royal Marines who had just been picked up. It also trapped more Royal Marines
> who had been waiting in the messdecks. Emergency damage control and first aid
> parties rescued the wounded, flooded 'A' and 'B' magazines, and dealt with the
> blaze. Sikh was steaming in circles at 10 knots and getting slower. **A third
> shell struck her range finder director** and from then on, all her guns had to
> fire under local control. As Sikh came to a stop, Captain Micklethwait, Sikh's
> Commanding Officer, ordered all Royal Navy Forces to leave the area while HMS
> Zulu towed Sikh away from danger. While under tow, **a forth shell hit the
> unlucky destroyer setting off the charges around Sikh's 'Y' mounting**. This
> started another bad fire aft while **a fifth shell struck 'B' mounting killing
> the gun crew**. Others took up their places and the guns continued firing.
> During the shelling, the towline broke and Zulu made attempts to get a heaving
> line to Sikh. Captain Micklethwait, went forward to supervise the towing
> preparations on the fo'c'sle when **a sixth shell smashed the bridge**. It was
> now broad daylight and the two ships were getting underway when another 88mm
> shell hit the towline and severed it. There was no hope of saving Sikh. HMS
> Zulu laid a smokescreen around Sikh and tried to come in to take Sikh's crew.
> It was too dangerous. HMS Zulu was ordered away. Shells continued to hit Sikh
> but her 'X' gun kept firing until the ammunition in the ready use locker was
> exhausted. **Captain Micklethwait fired the scuttling charges which flooded the
> engine and boiler rooms. He made a final tour of his ship and left. Sikh took a
> long time to die, heeling over to starboard as she sank in position 32º05'N,
> 24º00'E while shells continued to hit. All the survivors were taken as prisoner
> of war.**"
> —— uboat-sikh
> https://uboat.net/allies/warships/ship/4434.html

**这份叙述是全组细节密度最高的一段。** 六发炮弹各自的落点、
Zulu 两次试图靠帮、舰长做最后巡查后离舰、生还者全部被俘 ——
这些只在这一处，naval-history 的同一页只有四行。

**沉没位置的三源对照（本组最清楚的一处转录错误）：**

| 来源 | 位置 |
|---|---|
| naval-history-sikh | "32.05N **42.00E**" ← **错** |
| uboat-sikh | "32º05'N, **24º00'E**" |
| navypedia-tribal | 未给坐标，只写 "sunk by German coastal battery at Tobruk 14.9.1942" |
| britainsnavy.uk | "sank close inshore"（托布鲁克） |

经度 42°E 在托布鲁克以东一千多公里、深入埃及内陆，而同一页明写
「off Tobruk」。24°00'E 与托布鲁克的实际经度（约 23°57'E）吻合。
**采用 24°00'E，42°00'E 记为转录错误。**

**阵亡数：未获取。** 两个主力来源（naval-history / uboat.net）都只写
"All the survivors were taken as prisoner of war"，不给阵亡数字。
maritimefindings.com 的搜索摘要提到「115 of her 190 crew were lost」，
但该站实测返回 **403**（试过普通 UA 与浏览器 UA），原页未取到。
按项目规矩不据搜索摘要入库，`service.casualties` **整条未写**。

---

## 4. 来源清单与本轮抓取情况

| id | URL | tier | 实测 |
|---|---|---|---|
| navypedia-tribal | https://www.navypedia.org/ships/uk/brit_dd_tribal.htm | D | 200，74 KB |
| uboat-tribal-class | https://uboat.net/allies/warships/class/1.html | D | 200 |
| uboat-cossack | https://uboat.net/allies/warships/ship/4423.html | D | 200 |
| uboat-maori | https://uboat.net/allies/warships/ship/4425.html | D | 200 |
| uboat-zulu | https://uboat.net/allies/warships/ship/4428.html | D | 200 |
| uboat-sikh | https://uboat.net/allies/warships/ship/4434.html | D | 200 |
| naval-history-cossack | https://www.naval-history.net/xGM-Chrono-10DD-34Tribal-HMS_Cossack1.htm | D | 200，260 KB |
| naval-history-maori | https://www.naval-history.net/xGM-Chrono-10DD-34Tribal-HMS_Maori.htm | D | 200，207 KB |
| naval-history-zulu | https://www.naval-history.net/xGM-Chrono-10DD-34Tribal-HMS_Zulu.htm | D | 200，217 KB |
| naval-history-sikh | https://www.naval-history.net/xGM-Chrono-10DD-34Tribal-HMS_Sikh.htm | D | 200，260 KB |
| （复用）navweaps-4-7in-45-mk12 | https://www.navweaps.com/Weapons/WNBR_47-45_mk9.php | D | 200，56 KB |
| （复用）navweaps-2pdr-mk8 | data/sources.yaml 已登记 | D | — |

**新登记 10 条**（6 条舰级/年表 + 4 条 uboat.net 单舰页）。
全部 tier D，故所有 fact 的 confidence 上限为 C，
只有多源互证且来源自述清楚的少数条目记 B。

**本轮未使用的来源：**
- `naval-history.net` 的 eBook 分册
  `EBook02-WW2RN27-BritishShipsDestroyers.htm` 抓到了并用来核对四艘的
  结局一句话描述（"SIKH ... by German shore batteries" 等），
  但它本身是 naval-history 的另一个页面，未单独登记为来源，
  **只在核实时看过，没有作为 fact 的 src**。若主会话认为需要登记，
  可以补一条，但会与四个单舰 page 来源高度重复。
- `britainsnavy.uk` 的 Sikh 页抓到了（1.4 KB，很薄），只用来核对
  「sank close inshore」这一点，未登记。

---

## 5. 有争议的记载（逐条并列，不裁决）

### 5.1 Cossack 纳尔维克损伤：9 发 vs 4 发

- **naval-history-cossack**："hit by **nine 5in shells** in return fire"
- **navypedia-tribal**："Cossack 13.4.1940 was seriously damaged by hits of
  **four 127mm shells** from German destroyers and as a result of beaching in
  harbour of Narvik"

口径相同（5 in = 127 mm），数目差 5 发。
可能是「命中数」与「命中且造成损伤数」的差别，也可能只是统计来源不同。
**两条都写进 fact 的 note，数值分别保留，不做平均。**

### 5.2 Cossack 沉没日期：10-27 vs 10-24

- **naval-history-cossack**："27th ... ship sank at 1043 in position 35.12N
  08.17W"
- **uboat-cossack（叙述正文）**："foundered on the **27**"
- **uboat-cossack（信息栏 + U 艇战果表）**："Lost **24 Oct 1941**" /
  "Sunk on **24 Oct 1941** by U-563 (Bargsten)"

这两者不是跨源冲突，是同一场事件的两个节点：10-23 中雷、
10-24 判定为战损、10-27 舰体实际沉没。
**`construction.fate_date` 取 10-27（实际沉没），
note 里写 10-24 是判定战损日。两条并列，不合并。**

### 5.3 Maori 服役日：1939-01-02 vs 1938-11（服役）

- **uboat-maori**："Commissioned **2 Jan 1939**"
- **naval-history-maori**：1938-11 段记 "Contractors trials and
  **commissioning** for service in 1st TRIBAL Destroyer Flotilla"，
  并把 "Build was completed on **30th November 1938**" 写在前面

英国舰「服役」与「完工」常相差数周，两个日期不必然冲突，
但两份来源都用了 "commissioned" 这个词，**故两条 `construction.commissioned`
都登记，各自带自己的 src 与 note，不裁决。**

### 5.4 Maori 残骸最终沉放日期：1945-05 vs 1945-07-05

- **naval-history-maori**："**During May 1945** the hulk was again raised and
  taken to a position off Malta where it was sunk."
- **uboat-maori**："On **5 July 1945**, Maori's hulk was scuttled finally in
  deep water far away from the harbour."

差两个月。**未写进 fact**（残骸处理属于叙述层，不是舰体数据），
在 articles/maori.yaml 里两说并列。

### 5.5 Zulu 失踪人数：27 vs 24

- **uboat-zulu**："twelve men had been killed, **twenty seven** went missing and
  one was wounded"
- **naval-history-zulu**："Twelve members of the ship's company were killed,
  **24** Missing and one injured"

阵亡 12、伤 1 两源一致；失踪数差 3。**两条都写进
`service.casualties` 的 note（fact 值取 12 = 阵亡），失踪数并列不裁决。**

### 5.6 Zulu 沉没的机型归属：德国 vs 意大利

- **navypedia-tribal**："damaged by **German Ju 88 bomber** at Tobruk"
- **naval-history eBook 分册**："by **Italian/German force** of Ju87 and Ju88
  bombers"
- **naval-history 单舰页 / uboat-zulu**：只写 "enemy aircraft"，不指国籍

**任务表写「意大利空袭」缺乏支撑。** fact 写「德/意空袭，
navypedia 明确记德国 Ju 88」，正文不指单一国籍。

### 5.7 Sikh 沉没坐标：24°00'E vs 42°00'E

见 §3.4 末。**24°00'E 为准，42°00'E 记为转录错误。**
这不是「争议」，是明确的一处错误，故只在一处标注，不做两说并列。

### 5.8 20 mm Oerlikon vs 2-pdr：四艘舰的加装内容三源不一致

**这是本组牵涉面最广的一处记载冲突，四艘舰里三艘受影响。**

navypedia 的 1941 年初加装表把全级分两行：

> "early 1941, Ashanti, Bedouin, Cossack, Eskimo, **Maori**, Mashona, Matabele,
> Mohawk, Nubian, Punjabi, Somali, Tartar: **+ 2 x 1 - 20/70 Oerlikon Mk II/IV**"
> "early 1941, **Sikh, Zulu**: **+ 2 x 1 - 40/39 2pdr QF Mk VIII**"

按这一说：Cossack 与 Maori 加的是 20 mm Oerlikon，Sikh 与 Zulu 加的是 2-pdr。

uboat.net 说的是另一回事（1941-07）：

> "More rapid firepower was needed against the fast moving E-boats so **HMS
> Cossack, HMS Maori, HMS Sikh and HMS Zulu had single 2 pounder guns mounted on
> each side of the bridge**."

按这一说：四艘都加的是 2-pdr。

naval-history 的逐舰记载又是第三种：

- Cossack 页：**没记** 1941-07 加 2-pdr，只记了 1941 年两次改装（286 雷达、X 炮座）
- Maori 页：**没记** 任何 2-pdr 或 20 mm
- Zulu 页：1941-06 法尔茅斯改装 "**20mm single Oerlikon mountings were fitted
  on bridge wings**"
- Sikh 页：1941-06 前后 "fit of **two additional 2Pdr mountings in Bridge
  wings**"，1941-09 又 "**two single 20mm Oerlikon guns**"

**处理方式：**
- `armament.aa_20mm.count` 只在有明确记载的 Zulu（2 门，1941-08 起）
  与 Sikh（2 门，1941-09 起）登记，Maori 的那条按 navypedia 记 2 门并
  在 note 里写明「uboat.net 记为 2-pdr」。
- Cossack 的 `armament.aa_20mm.count` **未登记** —— 三源都不足以确定，
  按红线「查不到就写查不到」整条不写。
- 每艘舰的 `armament.mount.summary` 的 note 里都写清这处三源分歧。

**主会话若要合并，请保留这些 note —— 它们不是啰嗦，是这处冲突的唯一记录。**

### 5.9 俾斯麦夜战「观测到命中」vs「未取得确认命中」

涉及 Cossack、Maori、Zulu、Sikh 四艘，处理方式统一：

- **来源原话**：Cossack "One torpedo was seen to hit"；
  Maori "a torpedo hit was observed ... A bright glow illuminated the
  waterline"；Sikh "It is believed that one hit was obtained"；
  Zulu "no hits were observed and they are believed to have missed ahead"
- **战后对残骸的调查**一般认为驱逐舰夜战未取得确认命中

**本组的处理：fact 里保留来源原话（用「观测到」「相信获得」这类转述），
正文里明确写「这是观测宣称，不是确认战果」，
并说明两种证据强度不同、不互相否定。绝不写成「击中了俾斯麦」。**

---

## 6. 发现并记录下来的来源笔误（不是争议，是错字）

| 来源 | 错误 | 更正 |
|---|---|---|
| naval-history-sikh | 沉没位置 "32.05N **42.00E**" | 应为 24°00'E（三源对照，见 §3.4） |
| naval-history-sikh | 1941 改装 "replacement of **single** 4.7in gun" | 本级无双装 4.7 in 炮；应为 twin 4.7in |
| naval-history-zulu | 下单日 "10th March **1935**" | 应为 1936-03-10（同站 Cossack 页与 uboat.net 均为 1936） |
| uboat-tribal-class | 排水量单位标 "BRT"（容积吨位） | 军舰不适用，应为吨位 |
| naval-history-sikh | 原文 "Hindi community"（指锡克人） | 语义应为 Sikh community，按语义写 |

**这五处都只在一处标注，没有把错误值写进 fact。**

---

## 7. 交付摘要

| 项 | 数量 |
|---|---|
| 舰级文件 | 1（`classes/tribal.yaml`，80 条 fact） |
| 单舰文件 | 4 |
| 切片文件 | 4 |
| 正文文件 | 4 |
| 新登记来源 | 10 |
| **fact 总数** | **211** |

**逐舰 fact 数：**

| 舰 | fact 数 | 说明 |
|---|---|---|
| Cossack | 34 | 战史最复杂（阿尔特马克 + 纳尔维克 + 雷达 + 俾斯麦 + 沉没），但 8 条舰级值不重复 |
| Maori | 33 | |
| Sikh | 33 | |
| Zulu | 31 | |
| 舰级 tribal | 80 | 含 4.7" Mk XII 武器实体 20 条 + 4 座炮位实体 26 条 |

四艘单舰都在 31–34 条区间，符合任务书预期的 30–60 条，
**没有为凑数硬写** —— 反而主动删掉了 12 条误用字段的条目（见下）。

**结构说明：**

- `classes/tribal.yaml` 80 条：舰级骨架 31 条 + 武器实体（`weapon:47in-45-mk12`）20 条
  + 四座炮位实体（`mount:tribal-a/b/x/y`）26 条 + 2-pdr 4 条（有重叠计数）
- 单舰文件只写差异：建造日期、舷号变更、舰长任期、逐次改装、本舰战史标志事件
- 四艘的 `displacement.standard` 都在单舰文件里重复了一次（与舰级同值），
  目的是让解析链在该级只入库四艘的情况下仍有单舰落点。
  **note 里明写「与舰级同值，navypedia 未给逐舰数据」，不冒充逐舰实测值。**

### 中途修正：删掉了 12 条误用字段的 fact

初稿把「战斗细节」写进了 `armament.gun_failures`，共 12 条。
复核 `data/fields.yaml` 后确认该字段的定义是
「逐条记录某一场战斗中的**炮塔/火炮失效**情况」，
而初稿里有大量内容不属于这个定义：
阿尔特马克登船行动、鱼雷攻击、结构损伤、运送罗马尼亚王室、友舰救援等。

**已全部删除。** 保留的只有真正描述本舰火炮被打掉的条目：

- Cossack 纳尔维克：A 炮供弹组全员阵亡、锅炉舱中弹
- Sikh 托布鲁克：A 炮待发弹药架殉爆、测距指挥仪被毁、B 炮座炮组阵亡

**这些被删的内容在 `slices/` 与 `articles/` 里都完整保留，信息没丢。**
带 `about: weapon:*` 的武器实体 fact 不受影响。

---

### 卡住的地方

1. **Sikh 的阵亡数 —— 未获取。**
   naval-history 与 uboat.net 都只写 "All the survivors were taken as prisoner
   of war"。maritimefindings.com 的搜索摘要提到 115 人，但该站实测 **403**
   （普通 UA 与浏览器 UA 都试过），原页取不到。
   按项目规矩不据搜索摘要入库，`service.casualties` **整条未写**。
   若主会话要补这一条，需要一个能打开的来源。

2. **部族级的装甲数据 —— 本来就是空的，不是漏采。**
   本级是无装甲带的舰队驱逐舰，navypedia 与 uboat.net 都没有装甲厚度、
   装甲重量、装甲占比任何一项。`protection.*` 全部未登记。
   **没有用别级的值填充。**

3. **逐舰的试航实测功率与航速 —— 未获取。**
   navypedia 只给 44,000 hp（设计）与 "36.25–36.5 kn"（未注明是试航值），
   uboat.net 给 44,000 HP / 36 knots。四艘舰都没有逐舰试航数据。
   故只有 `propulsion.power.design` 与 `speed.design` / `speed.max`，
   `power.trial` / `speed.trial` 全部未登记。

4. **炮位实体的细节 —— 部分未获取。**
   navweaps 给了 CPXIX 的炮座重、仰角、射界、炮轴间距（96.5 cm），
   但**没有**给：各炮位的 frame 位置、逐座射界限制角、
   每座炮塔的测距仪数量与基线（`mount.rangefinder_count` 未登记）。
   `mount.installed` / `mount.removed` 也只在 X 炮座上有意义
   （1940-41 年间被换掉），但来源只给到月份，故未登记该字段。

5. **鱼雷型号 —— 未获取。**
   两个舰级来源都只写 "533 TT" / "21 inch"，不给 Mark 号
   （同期英国驱逐舰用 Mk IX / Mk IX**）。**没有推测填入**，
   只登记了 `armament.torpedo.tubes` 与 `armament.torpedo.diameter`。

6. **深度：四艘舰的「逐次改装完整清单」不齐。**
   navypedia 有一张全级改装表，但它按年份批量列，不逐舰；
   naval-history 的逐舰记载又有缺漏（例如 Cossack 页完全没记 1941-07 加 2-pdr）。
   结果是 `armament.mount.summary` 只能给「建成 + 已知主要改装」，
   做不到完整的逐月配置表。**这一点已在每艘舰的 summary note 里写明。**

7. **`navypedia.org` 本次可以直连**（与任务书预警不同）。
   实测 `brit_dd_tribal.htm` 返回 200、74 KB，未走代理。
   任务书说「可能被 SSRF 拦」，本轮没遇到。

8. **`naval-history.net` 的 URL 形式与任务书给的不一样。**
   任务书建议的 `xGM-Chrono-05DD-HMS_Cossack.htm` 与
   `xGM-Chrono-06DD-HMS_Cossack.htm` **全部 404**。
   正确形式是带舰种批次的：
   `xGM-Chrono-10DD-34Tribal-HMS_Cossack1.htm`（Cossack 有 `1` 后缀，
   因为有两艘同名舰）。四艘舰都已抓取成功。
   **主会话若要写文档，这个 URL 形式值得记一笔。**

9. **维基百科抓不到**（`web_fetch` 报 SSRF blocked，
   `en.wikipedia.org` 解析到 198.18.0.18）。
   本组因此完全没依赖维基 —— 这也符合项目规矩（tier E 不能作 fact 来源）。
   仅在核实「Chariot 参战序列」时用过一次搜索结果的标题摘要，
   且该结论另有一条独立证据链（Sikh 自己的 1942-03 年表）支撑，见 §0.4。

### 有争议的记载（索引）

详细并列见 §5，此处只列清单：

| # | 争议项 | 各方说法 |
|---|---|---|
| 5.1 | Cossack 纳尔维克损伤 | 9 发 5 in（naval-history）vs 4 发 127 mm（navypedia） |
| 5.2 | Cossack 沉没日 | 10-27 实际沉没 vs 10-24 判定战损（同源两口径） |
| 5.3 | Maori 服役日 | 1939-01-02（uboat.net）vs 1938-11（naval-history） |
| 5.4 | Maori 残骸沉放日 | 1945-05（naval-history）vs 1945-07-05（uboat.net） |
| 5.5 | Zulu 失踪人数 | 27（uboat.net）vs 24（naval-history） |
| 5.6 | Zulu 沉没机型 | 德国 Ju 88（navypedia）vs 意/德混合（naval-history eBook） |
| 5.7 | Sikh 沉没坐标 | 24°00'E（两源）vs 42°00'E（naval-history，判为错字） |
| 5.8 | 20 mm vs 2-pdr 加装 | navypedia（分两行）vs uboat.net（四艘都 2-pdr）vs naval-history（逐舰不一） |
| 5.9 | 俾斯麦夜战命中 | 来源「观测到命中」vs 战后残骸调查「无确认命中」 |

### 待主会话决定的两件事

1. **`navweaps-4-7in-45-mk12` 由 g7-weapons 组登记。**
   本组大量引用它（舰级 20 条武器 fact + 4 篇正文）。
   若合并时 g7 的分片被跳过或改动 id，本组会有 40+ 处悬空引用。
   **合并顺序必须先 g7 后 g4。**

2. **四艘舰的 fact 数都在 31–34 条，接近任务书下限（30）。**
   这不是偷懒：本级无装甲数据、无逐舰试航数据、鱼雷型号缺失，
   三个方向的字段天然是空的。本组宁可少写也没有用别级的值填充。
   若主会话认为需要补厚，建议方向是：
   补充战役档案（ADM 53 系列的逐日日志）或
   `The Tribals`（Brice）/ `Tribal Class Destroyers`（Hodges）两本专著。
