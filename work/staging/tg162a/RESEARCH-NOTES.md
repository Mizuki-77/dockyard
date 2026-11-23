# 调研底稿 —— 新奥尔良级三舰（CA-36 / CA-32 / CA-44）· TG 16.2

> 采集日：2026-11-23 · 组名 `tg162a` · 抓取方式：Python urllib + 浏览器 UA 直连
> 原始页面全部存在 `work/staging/tg162a/_raw/`（含 3 份一手战损报告 PDF 与转出的 txt）。
>
> **抓取通道说明**：`web_fetch`/`research` 按规矩未用。`history.navy.mil` 主站在本机被
> TLS 层直接掐断（`SSL: UNEXPECTED_EOF_WHILE_READING`，换 TLS 版本、换 curl、换
> Invoke-WebRequest 全败，archive.org 的 Wayback 返回 429），因此 **DANFS 三舰词条改用
> ibiblio.org 的 HyperWar 转录版**（同一份 DANFS 文本，只差 HTML 排版）。
> HyperWar 上另拿到三份 War Damage Report 原始 PDF，这是本组唯一的一手来源。

---

## 一、给主会话的四条结论（先说最要紧的）

### 1. 「TG 16.2 旗舰是明尼阿波利斯号」——成立，而且有传记级原始表述

- HyperWar 官方战斗序列：
  > "Task Group 16.2 (TG 16.2) / Cruiser Group / Rear Admiral Thomas C. Kinkaid, USN /
  > Commander Cruiser Division 6 (Comcrudiv 6)"
  > —— http://www.ibiblio.org/hyperwar/PTO/TideTurns/Midway/Midway-OOB.html
- Gerald E. Wheeler《Kinkaid of the Seventh Fleet》第 208 页编成表（HyperWar 全文 PDF）：
  > "CTG 16.2 Cruiser Group RADM Thomas C. Kinkaid
  >  CTU 16.2.1 CAPT William D. Chandler — Northampton (CA 26) / Pensacola (CA 24) / Atlanta (CL 51)
  >  CTU 16.2.2 RADM Thomas C. Kinkaid — Minneapolis (CA 36) / New Orleans (CA 32) / Vincennes (CA 44)"
  > —— https://www.ibiblio.org/hyperwar/NHC/NewPDFs/USN/USN,%20KINKAID%20OF%20THE%20SEVENTH%20FLEET%20(Bio).pdf
- 同一传记还直接点明本舰是 CruDiv 6 的**常任旗舰**：
  > "The day after returning to Pearl Harbor Kinkaid shifted his flag from Astoria to
  > Minneapolis, the regular flagship of CRUDIV 6. … This ship would be home until July
  > when the admiral would move to the carrier Enterprise, leaving his staff behind."

**修正一条细节**（不算任务书写错，但很容易被简化掉）：TG 16.2 不止这三艘。
编成里还有 Northampton、Pensacola、Atlanta，共 6 艘巡洋舰。

### 2. 三舰的主炮**不是一个型号** —— 任务书这条提醒是对的，且差别比想的更大

| 舰 | 主炮 | 依据原句 |
|---|---|---|
| CA-32 New Orleans | 8"/55 **Mk 9 族**（Mk 9/11/13/14） | navweaps Mk 9 页 "New Orleans (CA-32, 34 and 36 only)" |
| CA-36 Minneapolis | 8"/55 **Mk 9 族**；**1945 年换 Mk 15 Mod 1 炮身** | 同上 + Mk 12 页 "Minneapolis (CA-36) was regunned with Mark 15 Mod 1 in 1945" |
| CA-44 Vincennes | 8"/55 **Mk 12** | navweaps Mk 12 页脚注 "The Tuscaloosa sub-class consisted of Tuscaloosa (CA-37), San Francisco (CA-38), Quincy (CA-39) and Vincennes (CA-44)" |

- https://www.navweaps.com/Weapons/WNUS_8-55_mk9.php
- https://www.navweaps.com/Weapons/WNUS_8-55_mk12.php
- 旁证（navypedia 逐子级清单）："Armament CA32, 34, 36: 3 x 3 - 203/55 Mk 9.11.13/14 …
  CA37 - 39, 44: 3 x 3 - 203/55 Mk 12.15"
  —— https://www.navypedia.org/ships/usa/us_cr_new_orleans.htm

**为什么这条重要**：Mk 9 炮身 30.48 t，Mk 12 炮身 17.38–17.45 t，差 13 t/门。
把三舰写成同一种主炮，等于把 1.2 万吨级条约巡洋舰最有意义的一次减重抹掉。

### 3. 「弹药库装甲加强是本级与北安普敦级的关键差别」——成立，且有两侧原句

- 本级（弹药库段有独立窄装甲带）：
  > "There were narrow belts abreast magazines. Thickness of these belts was 102mm
  > decreasing to 76mm at lower edge. Magazines were protected by 37mm bulkheads fore
  > and aft, machinery and magazines were separated by 76-51mm bulkheads."
  > —— navypedia，同上 URL
- 北安普敦级（提议过加强、最终只做到弹药提升井防破片）：
  > "During designing it was offered to strengthen armour, ensuring protection at least
  > of magazines against 203mm shells, but works were limited only by splinterproof
  > protection of ammunition elevators."
  > "Under 203mm shells immune zone was absent."
  > —— https://www.navypedia.org/ships/usa/us_cr_northampton.htm
- 旁证（同页给出的两组装甲数值对比，可直接引用）：
  > 北安普敦级 "Armour, mm belt: 95 - 76, deck: 51 - 25, barbettes: 38, turrets: 64 - 19, CT: 32"
  > 新奥尔良级 "belt: 127 - 76, bulkheads: 76 - 38, deck: 57, barbettes: 127, turrets: 203 - 38, CT: 127"

**代价也说清了**（historyofwar 原句，可直接写进正文）：
> "The previous pair of ships, Tuscaloosa (CA-37) and San Francisco (CA-38) had been
> given a lighter 8in gun and a smaller turret, saving around 40 tons. This weight was
> used to increase the amount of barbette armour, but this turned out to bring them very
> close to the treaty limits. In order to counter this Quincy and Vincennes had some
> armour removed, especially in the barbettes."
> —— https://www.historyofwar.org/articles/weapons_USS_Vincennes_CA44.html

即**炮座厚度三档：CA-32/34/36 = 127 mm → CA-37/38 = 152 mm → CA-39/44 = 133 mm**。
这是本级内部唯一一处「装甲厚度逐子级往复」的地方，已写进舰级 note 与文森斯单舰文件。

### 4. 塔萨法隆加的「断艏」有两份一手/官方来源，且因果比通说更细

- ONI 官方叙述：
  > "At 2327, however, the Japanese struck the first of a series of crippling torpedo
  > blows. Within one minute both the Minneapolis and the New Orleans had their bows
  > blown off. … 2327 Minneapolis torpedoed. 2328 New Orleans torpedoed.
  > 2339 Pensacola torpedoed. 2348 Northampton torpedoed."
  > —— http://www.ibiblio.org/hyperwar/USN/USN-CN-Tassafaronga/index.html
- 明尼阿波利斯（本舰）：
  > "The Minneapolis received her first hit forward of turret I, abreast the aviation
  > gasoline compartment. An instant later, another torpedo struck No. 2 fireroom. …
  > The entire bow section tore loose at frame 22, folded downward, and dangled from the
  > rest of the hull. The water level flowed aft as far as No. 1 barbette. Soon firerooms
  > 1, 2, and 3 were flooded and all personnel inside were drowned or suffocated."
- 新奥尔良（本舰）——**战损报告的官方结论，通说里常被漏掉**：
  > "It was established that the bomb and mine magazine, A-502-1/8-M, contained the 160
  > pound demolition charge and forty-nine 100-pound bombs and that small arms magazine
  > A-502-M contained five 325-pound depth bombs. These magazines extended to the shell
  > with no armor or liquid protection. … this Bureau is of the opinion that the severe
  > damage to NEW ORLEANS was the result of the combined effects of the torpedo
  > detonation and a mass detonation of aircraft bombs and demolition charge caused by
  > fragments produced by the torpedo. The Bureau of Ordnance concurs with this opinion."
  > —— War Damage Report No.38，http://www.ibiblio.org/hyperwar/USN/rep/WDR/U.S.S.%20NEW%20ORLEANS%20(CA-32),%20TORPEDO%20DAMAGE%20-Lunga%20Point,%20November%2030,%201942.pdf

**即：新奥尔良不是「被鱼雷切断舰艏」，是「鱼雷引爆了旁边的航空炸弹库」。**
这一条改变了对该级防护的评价（不是装甲不够厚，是弹药库位置本身没被装甲/液舱包住），
建议写进正文的损伤段，并连到同报告那句后续处理：
> "Where required, action has been taken to provide protection for all magazines of
> cruisers, either by relocating the magazines behind armor or liquid or else by
> creating a liquid layer outboard of the magazine."

---

## 二、逐条证据（英文原句 + URL）

### 2.1 建造与身份

**CA-36 Minneapolis**
> "The second Minneapolis (CA-36) was laid down 27 June 1921 by Philadelphia Navy Yard;
> launched 6 September 1933; sponsored by Miss Grace L. Newton; and commissioned 19 May
> 1934, Capt. Gordon W. Haines in command."
> —— http://www.ibiblio.org/hyperwar/USN/ships/danfs/CA/ca36.html

⚠️ **「1921」是 DANFS 自己的排印错误**（1921 年本级还在设计阶段），另两源分别为：
> navypedia 表：CA36 Minneapolis … "27.6.1931 / 6.9.1933 / 20.6.1934"
> navsource："Keel laid on 27 JUN 1931 by the Philadelphia Navy Yard / Launched 06 SEP 1933 / Commissioned 19 MAY 1934"

采用 1931-06-27。**服役日另有一处两源分歧**：navypedia 记 20.6.1934，DANFS 与
navsource 均为 19 May 1934，取后者（DANFS 与 navsource 舰长任期表起点
05/19/1934 自洽）。

**CA-32 New Orleans**
> "The second New Orleans (CA-32), formerly CL 32, was laid down 14 March 1931 by New
> York Navy Yard, launched 12 April 1933; sponsored by Miss Cora S. Jahncke, daughter of
> the Assistant Secretary of the Navy, and commissioned 15 February 1934, Captain Allen B.
> Reed in command."
> —— http://www.ibiblio.org/hyperwar/USN/ships/danfs/CA/ca32.html

**CA-44 Vincennes**
> "Vincennes (CA-44) was laid down on 2 January 1934 at Quincy, Mass., by the Bethlehem
> Shipbuilding Company's Fore River plant; launched on 21 May 1936; sponsored by Miss
> Harriet Virginia Kimmell daughter of the mayor of Vincennes, Ind.; and commissioned on
> 24 February 1937, Capt. Burton H. Green in command."
> —— http://www.ibiblio.org/hyperwar/USN/ships/danfs/CA/ca44.html

**级别名的来历（易被忽略）**
> "The New Orleans class was also sometimes known as the Astoria class, as she was the
> first of the class to have been laid down. The New Orleans name was officially adopted
> after the loss of the Astoria in 1942."
> —— https://www.historyofwar.org/articles/weapons_new_orleans_class_cruisers.html

**为何三舰先造（设计史的关节）**
> "The original plan had been for CA-32 to CA-36 to be modified Northampton class ships
> and for CA-37 to CA-41 to be the improved New Orleans design. This plan was modified
> when it became clear that the earlier designs were almost 1,000 tons under their 10,000
> ton limit. The two Portland class cruisers were being built at private yards, where the
> cost of a late change would have been excessive, but three were allocated to Navy Yards.
> These three ships thus became the first of the New Orleans class cruisers."
> —— 同上

### 2.2 主尺度与排水量

| 项 | 值 | 原句 | URL |
|---|---|---|---|
| 标准排水量 | 10,136 t | "Displacement standard, t 10136" | navypedia |
| 满载排水量 | 12,463 t | "Displacement full, t 12463" | navypedia |
| 全长 | 179.2 m | "Length, m 176.2 wl 179.2 oa" | navypedia |
| 水线长 | 176.2 m | 同上；WDR-38 实测 "Length (W.L.) 578'-5/16"" | navypedia + WDR-38 |
| 水线宽 | 18.8 m | "Breadth, m 18.8" | navypedia |
| 满载吃水 | 6.93 m | "Draught, m 6.93 full" | navypedia |
| 航速 | 32.7 kn | "Max speed, kts 32.7" | navypedia |
| 续航 | 10,000 nm @ 15 kn | "Endurance, nm(kts) 10000 (15)" | navypedia |

**CA-32 的实测主尺度（一手，WDR-38 扉页）**：
> "Length (W.L.) 578'-5/16" / Beam (W.L.) 60'-1-3/8" / Draft 23'-9" (Before Damage)"

换算 176.19 / 18.32 / 7.24 m。**水线宽与 DANFS 的 61'9"（18.82 m）差 0.5 m**，
已作为「水线宽 vs 最大宽」的两说并列处理，未裁决。

**另有三套排水量口径并存，全部保留在舰级 note 里**：
- DANFS 技术行 "dp. 9,950"（CA-44 写 9,400，未标口径）
- navsource 三舰页 "Displacement 9,950 Tons"
- ibiblio / Vincennes 协会 "9375-9973 tons (normal) / 12,411 tons (full load)"

### 2.3 动力

> "Machinery 4 sets Westinghouse geared steam turbines, 8 Babcock & Wilcox boilers"
> "Power, h. p. 107000 / No of shafts 4 / Fuel, t oil 1241 - 1861"
> —— navypedia

> "Power was provided by eight Babcock and Wilcox high-pressure steam boilers, providing
> 107,000 horsepower to four Westinghouse geared steam turbines. The machinery space was
> shortened, partly by abandoning the unit system (with the engine room placed between two
> boiler rooms)."
> —— historyofwar，同上

> "Bunkerage 1861 tons fuel oil / Range 10,000 nautical miles (19,000 km) at 15 knots"
> —— http://pwencycl.kgbudge.com/N/e/New_Orleans_class.htm

**未获取**：锅炉蒸汽压力与温度（英文来源一致不给具体数值）、CA-44 的轮机厂
（DANFS 与 navsource 的 CA-44 页都没给，故舰级里 Westinghouse 的写法对 CA-44
只能算延伸，单舰文件不重复断言）。

### 2.4 防护（含三批差异）

navypedia 原句（三批同段，只差炮座）：
> "Main belt abreast machinery extended to 1.5m below and 2.86m over waterline. It was
> 127mm thick (76mm at lower edge) on 19mm STS plating. There were narrow belts abreast
> magazines. Thickness of these belts was 102mm decreasing to 76mm at lower edge.
> Magazines were protected by 37mm bulkheads fore and aft, machinery and magazines were
> separated by 76-51mm bulkheads. Armoured deck over main belt was 57mm over the
> machinery (on 2nd deck level) and magazines (on 1st platform level). Its thickness
> decreased to 32mm fwd from fore magazines. Barbettes were 127mm thick. Turrets had
> 203mm faces, 95-38mm sides, 38mm rears and 70mm crowns."
> （CA37/38 段 barbettes 152mm；CA39/44 段 barbettes 133mm）

historyofwar 的另一套口径（并列，未裁决）：
> "Armour – belt 5in to 3.25in over 0.75in STS / - over machinery 2.25in /
> - magazines 4in-3in side 2.25in above / - barbettes 6in-5in /
> - turrets 8in face 2.25in roof 1.5in side"

pwencycl 的第三套（按 ONI 222）：
> "Protection 1520 tons: 5" (127mm) belt tapering to 3" (76mm) on 0.75" (19mm) STS
> plating / 3" (76mm) machinery bulkheads tapering to 2" (51mm) / 4.7" (119mm) magazine
> sides tapering to 3" (76mm) / 1.5" (38mm) magazine bulkheads / 2.25" (57mm) armor deck /
> 8"/1.5"/2.25" (203mm/38mm/57mm) turret faces/sides and rear/roof / 5" (127mm) barbette /
> 2.5" (64mm) conning tower / Immune zone 12,000 to 24,000 yards against 8" gunfire"

→ **三处真实分歧**：弹药库侧甲（102 / 119 / 101.6 mm）、炮塔顶（70 / 57 mm）、
指挥塔（127 / 64 mm）。三处全部并列写进 fact 的 note，正文里也照规矩并列。

**免疫区两源吻合**（可互证）：
> navypedia: "the immune zone under fire of 203mm guns at a relative 60° bearing laid in
> a band between 60 and 120 cables." （60–120 缆 = 12,000–24,000 码）
> pwencycl: "Immune zone 12,000 to 24,000 yards (11,000 to 22,000 m) against 8" gunfire"

**装甲总重的两条独立路径得同一数**：
> pwencycl "Protection 1520 tons"
> navypedia "The protection weight made 15% of standard displacement" → 15% × 10,136 = 1,520.4 t

### 2.5 武备（逐舰已拆开，见 §1.2 与舰级文件）

8"/55 Mk 9 关键数据（navweaps）：
> "Gun Weight 30.0 tons (30.48 mt)" / "Gun Length 449.0 in (11.405 m)" /
> "Bore Length 440.1 in (11.179 m)" / "Rifling Length 373.65 in (9.491 m)" /
> "Chamber Volume Marks 9, 10, 11 and 13: 5,300 in3 (86.8 dm3)" /
> "Rate Of Fire 3 - 4 rounds per minute" / "Muzzle Velocity Marks 9, 10, 11 and 13 guns:
> 2,800 fps (853 mps)" / "Approximate Barrel Life 715 rounds" /
> "Ammunition stowage per gun 150 rounds"
> "Elevation -10 / +41 degrees" / "Train about +150 / -150 degrees"

**45° 最大射程与 41° 机械上限的矛盾（必须写明）**：
> 射表 "45.00 degrees / 32,330 yards (29,563 m)"，脚注 "This range table applies to those
> cruisers armed with Mark 9, Mark 11 and Mark 13 guns."
→ 射表 45° 那行是弹道外推，实船炮塔只能到 41°。已在 fact note 里点明。

**本级不能装超重弹（极易抄错处）**：
> "None of these ships ever carried the "super-heavy" AP projectiles as their ammunition
> hoists could not accommodate the longer, heavier round."
> —— navweaps Mk 9 页开头

**本级弹药基数在 1942-08 后被下调**：
> "The New Orleans (CA-32) class was reduced during refits after August 1942 to 125 rounds
> per gun."

5"/25 副炮（navweaps）：
> "This was the first USN heavy AA gun designed for the purpose" /
> "Barrel Weight (all except Mark 17): 2,105 lbs. (955 kg)" /
> "Rate Of Fire 15 - 20 rounds per minute" / "Muzzle Velocity 2,155 fps (657 mps)" /
> "Approximate Barrel Life 3,000 rounds" / "Ammunition stowage per gun about 200 rounds" /
> "Elevation Marks 17, 19, 23 and 27: -15 / +85 degrees"

**副炮座逐舰不同（三舰唯一的第三处硬差别）**：
> "Pensacola (4), Northampton (8), Portland (8) and New Orleans (except Quincy and
> Vincennes) (8): Mark 19"
> "Quincy (8), Vincennes (8) and Brooklyn (8): Mark 23"
> "The Mark 23 was an improved power-driven mounting and could be used with the Mark 33
> director."

→ **CA-32 与 CA-36 是手动的 Mk 19，CA-44 是动力驱动的 Mk 23。**

### 2.6 航空

> navypedia "2 catapults, 4 seaplanes (OL, O2U, O3U, OJ)"（CA32/34/36）
> 「CA37 - 39, 44: … 4 seaplanes (OL, O2U, O3U, OJ, SOC)」
> DANFS CA-44: "ripping a Curtiss SOC Seagull floatplane from its "moorings" on the
> storm-lashed well-deck amidships"
> navsource CA-44 图注: "an airframe flown by VCS-7, attached to the USS Vincennes (CA 44),
> circa April 1942"
> navsource CA-32 图注（1945-03-08）: "The port catapult has been removed."

### 2.7 编制（三套数字，全部并列，不裁）

> DANFS 三舰技术行: "cpl. 708"（CA-44 写 952）
> navypedia: "Complement 868"
> ibiblio / Vincennes 协会: "Complement: 1042-1121"

三份来源都没说清是平时/战时编制、哪一年。舰级文件里两条 `service.complement.standard`
并列（868 与 708），**这是全组唯一一处同窗重复值**，两条都写了 note 说明差异来源。
校验器会给这个出一条 warn，不是错——是刻意的并列。

### 2.8 战历关键节点（三舰对照）

**中途岛（1942-06-03 ~ 06-07）**
> navweaps 战斗序列分派：
> "USS Minneapolis (CA-36) … Notes: Escorting Hornet."
> "USS New Orleans (CA-32) … Notes: Escorting Hornet."
> "USS Vincennes (CA-44) … Notes: Escorting Enterprise; joined TF-17."
> —— https://www.navweaps.com/index_oob/OOB_WWII_Pacific/OOB_WWII_Midway.php

> ONI 中途岛叙述（6-04 下午）："When this attack developed the Yorktown was screened by
> the two cruisers and five destroyers of Task Force FOX, and by the Vincennes, Pensacola,
> Balch, and Benham, which had been sent from Task Force SUGAR after the first attack on
> the carrier."
> —— http://www.ibiblio.org/hyperwar/USN/USN-CN-Midway/index.html

→ **任务书说「三舰都护卫企业号/大黄蜂」是对的，但文森斯在 6-04 下午被调去支援
约克城**，这一点值得在正文里点出来：它的中途岛不止是「掩护企业号」。

**萨沃岛（1942-08-09）—— 文森斯**
> WDR-29: "VINCENNES received 57 known hits as well as one torpedo hit (possibly two) on
> the port side in way of the forward magazine group."
> "Damage to QUINCY and VINCENNES was so extensive that loss of the vessels was inevitable.
> It is not possible for any lightly protected vessel to absorb such punishment and
> survive."
> —— http://www.ibiblio.org/hyperwar/USN/rep/WDR/U.S.S.%20QUINCY%20(CA-39),%20U.S.S.%20ASTORIA%20(CA-34)%20and%20U.S.S.%20VINCENNES%20(CA-44),%20GUNFIRE%20AND%20TORPEDO%20D.PDF

> ONI Savo 叙述（本舰的第一次反击，含一个可引用的数字）：
> "The Vincennes replied with an 8-inch salvo, using a radar range of 8,250 yards. …
> Before the Vincennes could fire again an enemy salvo landed on the well deck and hangar,
> where intense fires broke out. The bridge, too, was hit, and the communications officer
> and two men in the pilot house were killed."
> —— http://www.ibiblio.org/hyperwar/USN/USN-CN-Savo/index.html

> DANFS 的沉没时刻（Riefkohl 原话）：
> "The Magnificent Vincennes, which we were all so proud of, and which I had the honor to
> command since 23 April 1941, rolled over and then sank at about 0250, 9 August 1942,
> about 2 1/2 miles east of Savo Island . . . Solomons Group, in some 500 fathoms of water."

**8 英寸 AP 打穿本级炮塔面板的实测（WDR-29 的装甲实效评估）**
> "The hit on the face plate of turret I made a clean hole 11 inches in diameter through
> the 8" class "B" face plate and the 51 lb. medium steel angle which joined together the
> face plate and the side plate. … six of the nine turrets on ASTORIA, QUINCY and VINCENNES
> were put out of action due to direct hits by 8" A.P. projectiles. The average range of
> these was about 5,000 yards."

→ 这是本站能拿到的、关于该级「8 英寸面板到底挡不挡得住 8 英寸弹」的最硬证据：
**5,000 码上下，同口径 AP 直接打穿**。写正文时必须给这句，否则「本级能挡 8 英寸」
会被读成「免疫」。

**塔萨法隆加（1942-11-30）—— 明尼阿波利斯与新奥尔良**，见 §1.4。

另记两条损伤经过（navsource 图注，CA-36）：
> "Minneapolis was flagship of TF-67 and was hit by two torpedoes; one blew her bow off,
> ahead of #1 turret and the other struck further aft amidships."
> "Minneapolis settling by the bow after a heavy vapor torch caused gas explosion on
> 6 December 1942 during the preparation and fabrication of the log breakwater at Tulagi.
> Seven feet of freeboard was lost at the bow from this explosion."

→ 1942-12-06 的二次爆炸（椰木防浪堤施工引燃汽油蒸汽）只有 navsource 一条来源，
DANFS 未提，故按 C 记并写进 note。

### 2.9 结局

| 舰 | 退役 | 除名 | 售拆 | 原句 |
|---|---|---|---|---|
| CA-36 | 1947-02-10 | 1959-03-01 | 1959-08-14 | DANFS: "sold for scrapping 14 August 1959 to Union Metals and Alloys Corp." |
| CA-32 | 1947-02-10 | 1959-03-01 | 1959-09-22 | DANFS: "sold for scrapping 22 September 1959 to Boston Metals Co., Baltimore, Md." |
| CA-44 | — | 1942-11-02 | — | DANFS: "Struck from the Navy list on 2 November 1942" |

战斗之星：CA-36 = 16（DANFS "Minneapolis received 16 battle stars"）；
CA-32 = 17（navsource 勋表栏 "Asiatic Pacific Campaign Medal (17)"）；
CA-44 = 2（DANFS "Vincennes was awarded two battle stars"）。

---

## 三、有争议的记载（两边原话并列，不裁决）

### 3.1 服役日：navypedia 与 DANFS/navsource 差一到两个月

| 舰 | navypedia | DANFS / navsource | 本站取 |
|---|---|---|---|
| CA-32 | "18.4.1934" | 1934-02-15（两源一致） | DANFS |
| CA-36 | "20.6.1934" | 1934-05-19（两源一致） | DANFS |
| CA-44 | "24.2.1937" | 1937-02-24（两源一致） | 三源一致，无争议 |

取 DANFS 的理由：它是官方出版物（tier B），且与 navsource 的**舰长任期表起点**
（CA-32 的 02/15/1934、CA-36 的 05/19/1934）自洽——独立字段互证。
navypedia 那两个日期在已抓到的任何来源里都找不到第二个支持者。

### 3.2 中途岛当天 CA-32 的舰长是谁

- navsource 舰长表 + navweaps 战斗序列：**Capt. Howard H. Good**
  > navsource: "Good, Howard Harrison, CAPT … 08/22/1941 - 06/18/1942"
  > navweaps: "USS New Orleans (CA-32) Commanding officer: Capt. Howard H. Good"
- Kinkaid 传记第 208 页编成表：**CAPT Walter S. DeLany**
  > "CTU 16.2.2 RADM Thomas C. Kinkaid — Minneapolis (CA 36) CAPT Frank J. Lowry /
  > New Orleans (CA 32) CAPT Walter S. DeLany / Vincennes (CA 44) CAPT Frederick L. Riefkohl"

两说并列。**时间线偏向 Good**：DeLany 的任期从 1942-06-18 才开始，中途岛是 06-04。
但传记是学术出版物，不能简单判它错——所以两条都留在 note 里，正文只写 Good 并注明另有一说。

### 3.3 中途岛当天 CA-32 掩护的是哪艘航母

- navweaps 战斗序列：**"Escorting Hornet"**
- DANFS：**"New Orleans sailed 28 May screening Enterprise, to surprise the Japanese in the
  Battle of Midway"**

两说并列。可能的解释是航渡期间编队位置调整过，但来源未给解释，不作推断。

### 3.4 CA-44 的炮塔面板厚度

- navypedia（同级三批统一）：**"Turrets had 203mm faces"**
- historyofwar 文森斯专页：**"turrets 6in face"**（= 152 mm）

两说并列。historyofwar 同一页的 barbettes 写「6in-5in」，怀疑是把炮座与炮塔面板
串了行，但来源未解释，故在文森斯单舰文件里单列一条 152 mm 的 fact，
**让冲突显式暴露**，而不是被舰级的 203 mm 盖掉。

### 3.5 炮塔顶板：70 mm 还是 57 mm

- navypedia："70mm crowns"
- historyofwar / pwencycl：2.25 in（57 mm）

两说并列。没有来源解释差在哪。

### 3.6 指挥塔：127 mm 还是 64 mm

- navypedia 三批均："CT: 127"
- pwencycl："2.5" (64mm) conning tower"

两说并列。另有一层时间因素：navypedia 记 1943 年底存活舰「CT was removed」
（拆掉指挥塔减重），所以这个值的有效期本来就到那时为止。

### 3.7 CA-36 的 20 mm 数量：6 门还是 12 门

- navypedia（同级）："mid-1942, all: … + 6 x 1 - 20/70 Mk 4"
- historyofwar（本舰专页）："Minneapolis had 12 single 20mm guns installed in 1942"

两说并列。本级各舰的 20 mm 数量本来就逐舰不同，不能互推——这也正是为什么
本组把防空炮数全部写进单舰文件而不是只写舰级。

### 3.8 CA-44 的阵亡人数：332

只有 historyofwar 一条来源给这个数：「losing 332 crewmen」。
WDR-29 只写「The personnel casualties, as on the other two ships, were very heavy」（不定量），
DANFS 与 navsource 均未给。故 fact 给 C，正文里必须注明是单一来源。

---

## 四、任务书里被我核实/更正的地方

任务书写得基本准确，四条史实陈述**全部核实为真**。以下是三处需要补严的：

1. **「1942-06 中途岛时三舰都属 TG 16.2，护卫企业号/大黄蜂」** —— 成立，
   但文森斯 6-04 下午已被调去支援约克城（ONI 原句见 §2.8）。
   另：TG 16.2 共 6 艘巡洋舰（还有 Northampton、Pensacola、Atlanta），不止三舰。

2. **「明尼阿波利斯 CA-36，TG 16.2 旗舰，RA Kinkaid」** —— 完全成立，
   而且比任务书说的更硬：Kinkaid 1942-01 就把旗移到本舰，
   本舰是 **CruDiv 6 的常任旗舰**（传记原句见 §1.1）。
   同编成表还显示 TG 16.2 内部还分了 CTU 16.2.1 / 16.2.2 两个战术单元。

3. **「主炮 8"/55，具体 Mk 型号三舰可能不同」** —— 提醒是对的，实际差别是：
   CA-32/CA-36 = Mk 9 族，CA-44 = Mk 12，且 CA-36 1945 年换 Mk 15 Mod 1 炮身。
   另外还有一处任务书没提的差别：**副炮座**，CA-32/CA-36 是 Mk 19（手动），
   CA-44 是 Mk 23（动力驱动，配 Mk 33 指挥仪）。

**没有发现任务书里有硬错误。** 唯一要提醒的是「本级能挡 8 英寸弹」这个通行说法
需要收紧：WDR-29 的一手证据是同级炮塔 203 mm 面板在约 5,000 码被 8 英寸 AP
打出 11 英寸直径的干净穿孔（§2.8 末）。

---

## 五、卡住的地方（明确未获取，不是漏填）

| 项 | 试过什么 | 为什么停 |
|---|---|---|
| `history.navy.mil` 主站 DANFS 原页 | Python urllib（多 TLS 版本）、curl、Invoke-WebRequest、Wayback、r.jina.ai | 全部失败：TLS 握手被掐断 / Wayback 429 / jina 403。**改用 ibiblio 的 HyperWar 转录版**（同一份 DANFS 文本） |
| CA-44 的轮机厂与型号 | DANFS CA-44、navsource CA-44、historyofwar CA-44、ussvincennes.org | 四份来源都只写「Steam turbines, 8 boilers, 4 shafts, 107,000 hp」，不给厂名 |
| 锅炉蒸汽压力/温度 | navypedia、historyofwar、pwencycl | 三源都只写「high-pressure」，无数值 |
| 试航实测功率与航速（三舰） | 全部已抓来源 | 无任何一源给逐舰试航值（107,000 hp / 32.7 kn 是设计值） |
| 水下防护纵深 | navypedia、historyofwar、WDR-29/36/38 | 本级无防雷突出部，无任何纵深数值。WDR-29 那句「4 英尺液体层」是给后续改装的设计建议，不是本舰参数 |
| 造价（三舰） | DANFS、navypedia、navsource、historyofwar | 英文来源一致不给 |
| 垂线间长 pp / 型深 / 干舷 / 方形系数 / 水线面积 / 稳心高 / 螺旋桨直径 / 舵数 / 发电机功率 | 同上 | 全部未获取，不留空壳 fact |
| 各次战斗的弹药消耗数 | ONI 三份叙述、DANFS、WDR | ONI 叙述只给时间与命中，不给发数 |
| CA-36 / CA-32 的阵亡人数 | WDR-36（OCR 不可读）、WDR-38、ONI、DANFS | 都只写「heavy」，无数字 |
| CA-44 残骸坐标 | navsource | 只有「depth of over 3,000 feet」与 RV Petrel 的照片，无坐标 |
| WDR-36 正文 | 已下载 18 页 PDF | **扫描质量差，OCR 只出 8,647 字符**，正文段落读不出，只能读到图注。故 CA-36 的损伤细节改由 WDR-38（同批、同型、可读）+ ONI 叙述支撑 |

---

## 六、交付摘要

| 项 | 数量 |
|---|---|
| 舰级文件 | 1（`classes/new-orleans.yaml`，97 条 fact） |
| 单舰文件 | 3（`ships/minneapolis.yaml` 43 条 / `new-orleans.yaml` 35 条 / `vincennes.yaml` 34 条） |
| 切片文件 | 3（minneapolis 7 片 / new-orleans 7 片 / vincennes 4 片） |
| 正文文件 | 3（每舰 intro 4 段；history 分别 25 / 23 / 15 条事件） |
| 新登记来源 | 27 条（`sources-fragment.yaml`） |
| fact 合计 | 209 条 |
| 一手来源 | 3 份 War Damage Report（WDR-29 / WDR-36 / WDR-38），其中 WDR-36 正文不可读，已在来源 note 里写明 |

### 自检结果（SCHEMA §10）

- **209 条 fact 全部通过本地校验**：字段注册 / 单位与注册表一致 / qual 键值合法 /
  枚举值合法 / src 均已登记 / 日期格式 / confidence 只有 A-B-C
- 无 `confidence: D`，**无 tier E 来源支撑任何 fact**（维基一条都没用）
- 所有 `protection.armor.*` 均带 `{part, region}` 两键
- 全组只有一处同窗重复（`service.complement.standard` 868 vs 708），
  是刻意的多源并列，两条各带 note 说明差异来源，校验器会给 warn 不给 err
- 3 份 articles 全部有 `ship` / `intro` / `history`；每段有 heading + text.zh + src；
  每条事件有 date + text.zh + src；正文无禁用词
- 3 份 slices 均为 P0 起连续编号、时间窗不重叠、3~8 片
- **未获取的项一律不写 fact**，只在各舰文件头部的注释段与本文 §5 列明

### 需要在合并时注意

1. `classes/new-orleans.yaml` 与 tg172 组的阿斯托里亚号共用，本文件已写完整（含七艘的
   子级差异）。合并时若 tg172 也写了同名 class 文件，请以本文件为基底做去重，
   特别注意**炮座三档值（127 / 152 / 133 mm）不要被压成单一值**。
2. 武器实体新建了两个：`weapon:8in-55-mk9`、`weapon:8in-55-mk12`、`weapon:8in-55-mk15`
   （第三个只挂在 CA-36 上），外加 `mount:neworleans-triple-turret`。
   `weapon:5in25-mk10` 复用已有 id（已核对 `data/sources.yaml` 的
   `navweaps-5in25-mk10` 条目），未重复建。
3. 三舰的 `service.unit` 都写了多条（不同时期的编队），valid 窗口互不重叠，
   若合并脚本按 field 去重会丢信息，请勿压平。
