# Nelson 级战列舰（纳尔逊级）— 舰级技术数据与设计考据

> 检索日期：2026-11-21。
> 同级两舰：**Nelson（纳尔逊，舷号 28）**、**Rodney（罗德尼，舷号 29）**。
> **硬规则执行说明**：每个数值后附来源缩写、URL 与英文原句；查不到原话支撑者写「未获取」，不推算、不跨来源拼。分歧并列不裁；「未获取」与「0」严格分开。
> **本文件的性质**：这是本站第一份纳尔逊级**舰级**文件（此前项目内没有）。舰级层只放**两舰共有**的设计参数；单舰差异见 §7 与 `work/raw/rodney-tech.md`。
> **来源厚度提醒**：本级的「武器」与「装甲」有 navweaps 的细数据，但**「舰体结构」「装甲总重」「电气」「造价分解」这几类大面积缺失**——不是没查，是现有可直连来源（navypedia / wiki / naval-history）都没有。逐项见 §9。

---

## 0. 一句话：这一级为什么长成这样

**因为英国必须在 35,000 吨 + 16 英寸炮的双重天花板下，同时保住 9 门主炮和能挡 16 英寸弹的装甲，而唯一的办法是把三座主炮塔全部挤到前面、把装甲堡（citadel）长度压到最短。**

原句（三条，互为因果）：

1. **吨位与口径的天花板** —— 华盛顿条约第五条：「No capital ship exceeding **35,000 tons (35,560 metric tons)** standard displacement shall be acquired by, or constructed by, for, or within the jurisdiction of, any of the Contracting Powers.」第六条：「No capital ship of any of the Contracting Powers shall carry a gun with a calibre in excess of **16 inches (406 millimetres)**.」https://www.ibiblio.org/pha/pre-war/1922/nav_lim.html
2. **英国被特批造两艘** —— 条约第二条：「The British Empire may, in accordance with the replacement table in Chapter II, Part 3, construct **two new capital ships not exceeding 35,000 tons (35,560 metric tons) standard displacement each**.」同条并列出代价：「On the completion of the said two ships the **Thunderer, King George V, Ajax and Centurion** shall be disposed of」——**即这两艘新舰是用四艘旧舰的舰名与吨位换来的。**
3. **缩短装甲堡 = 省装甲 = 能把省下的重量堆厚** —— navweaps 16"/45 页：「The unusual all-forward turret arrangement was adopted **in order to save weight, as this meant a reduced citadel length and thus less armor**.」
   - wiki 舰级页给同一逻辑的完整版：「To reduce the weight of armour, the main gun turrets were all mounted forward to **shorten the armoured citadel**.」

**这条因果链是本级存在的理由，也是它一切缺点的源头。** 省下来的吨位被用在装甲厚度上，代价落在动力（2 轴 45,000 shp / 23 节，同期世界最慢的主力舰之一）与储备浮力/结构强度上。

**任务书要求「这是这一级存在的理由，必须解释清楚」——上面三句就是答案。** 补充一层：这一级不是从零画的，是从**已取消的 G3 战列巡洋舰**缩下来的。
- navypedia：「Designers were **repelled from project G3** at creation of new battleships, **retaining an original arrangement of all main artillery in fore part of the ship**. It was possible to retain armour and armaments practically without changes **at the expense of a speed restriction in 23kts**.」https://www.navypedia.org/ships/uk/brit_bb1_nelson.htm
- wiki 舰级页：「The Nelson-class battleship was essentially a **smaller, 23-knot battleship version of the G3 battlecruiser** which had been cancelled for exceeding the constraints of the 1922 Washington Naval Treaty.」https://en.wikipedia.org/wiki/Nelson-class_battleship
- **炮和炮塔是现成的** —— navweaps 16"/45：「These weapons were **originally intended to be used on the never-built "G3" battlecruisers**. When those ships were canceled as a result of the Washington Naval Limitation Treaty, **the guns and mountings already on order were redesigned slightly and then used on** the only two British battleships built during the 1920s, HMS Nelson and HMS Rodney.」
- **副炮同理** —— navweaps 6"/50：「this gun was originally designed for the never-built "G3" battlecruisers. When those ships were canceled as a result of the Washington Naval Limitation Treaty, **the guns and mountings were then used on the Nelson class battleships**.」
- **4.7 英寸高炮同理** —— navweaps 4.7"/40：「The 4.7"/40 (12 cm) QF Mark VIII was **originally developed as an AAA weapon for the "G3" and "N3" capital ships of 1920**.」…「these weapons were then mounted on the Nelson class battleships」

**所以准确的说法是：纳尔逊级是 G3 的「降速减配版」，而不是一型全新设计的战列舰。**「Cherry Tree class」这个绰号就是这件事的注脚：
- wiki 舰级页：「They were often referred to as the "**Cherry Tree**" class, because they had been "**cut down by Washington**".」
- wiki Rodney：「the **Cherry Tree class** as they were cut-down by the Washington Naval Treaty」

---

## 1. 设计取舍：三座炮塔全前置的完整逻辑

### 1.1 为什么是「全前置」而不是传统的前二后一

原文（wiki 舰级页）：
> 「The "G3" and "N3" had **two turrets forward of the bridge with the third between the bridge and the funnels/aft superstructure**. However, in the Nelsons, this was taken further and **all three were in front of the bridge**; "B" mount superfiring over "A", with "X" turret on the forecastle deck behind "B", and therefore **unable to fire directly forward or aft**.」

即：G3/N3 已经是「前二 + 中间一」，纳尔逊级把中间那一座也推到舰桥之前，**于是三座炮塔占的长度比「前二后一」短得多**，装甲堡随之缩短。

### 1.2 全前置的四个代价（全部有原句）

| # | 代价 | 原句与来源 |
|---|---|---|
| 1 | **X 塔射界极窄，正前正后都不能打** | navweaps 16"/45 炮塔表：「"X" Turret: **About 60 to 130 degrees on either side**」；对照 A 塔 ±149°、B 塔 ±165° |
| 2 | **向正前射击会破坏甲板设施** | navweaps：「Firing "A" and "B" turrets on forward bearings **damaged many weather deck fittings** and made conditions in the mess deck areas directly below **very uncomfortable**.」 |
| 3 | **向舷后射击会打坏舰桥** | navweaps：「Considerable damage was inflicted to the superstructure and bridge whenever "X" turret was fired abaft the beam, with the **bridge becoming almost uninhabitable** when the guns were fired at close to 130 degrees and at high elevations.」；「The muzzles of "X" turret **overhung the deck at nearly all angles** of train and elevation.」 |
| 4 | **上层建筑被迫后移，变成「固定后桅帆」** | wiki 舰级页：「The location of the superstructure **towards the stern** caused manoeuvrability problems in high winds, especially when steaming at low speeds, where the superstructure acted somewhat like a **mizzen sail permanently set**, causing the ships to "**weathervane**"」 |

**代价 1 的实战后果（重要，直接决定最终战数据）**：1941-05-27 打俾斯麦时，X 塔在最初 25 次齐射中只有 6 次能瞄准。详见 `work/raw/rodney-tech.md` §4.1（一手战报原文）。

### 1.3 副炮为什么全在后部、且分两舷金字塔形布置

- **全后置** —— wiki 舰级页：「The secondary guns were placed in **totally enclosed director-controlled twin turrets at the upper deck level** and were **grouped aft** – another innovative element taken from the G3 and N3 design.」
- **每舷三座，P1–P3 / S1–S3** —— 一手战报 NOTE：「The secondary battery consists of three 6" twin turrets on each side. The twin turrets are numbered **from forward to aft on each side** as follows: Port side—P1, P2, P3; Starboard side—S1, S2, S3.」
- **全后置的致命弱点（原句）** —— navweaps 6"/50：「The arrangement on the Nelson class had a **major disadvantage** in that **all turrets and their working spaces were grouped tightly together**. As the turrets and working spaces were only **lightly protected by 1" (25 mm) HT plating**, this meant that **a single shell could have disabled all guns on one side**.」
- 这是「全前置」的镜像代价：主炮全前、副炮全后，各自占的长度最短，但**任一侧的副炮只要一发命中工作区就全瘫**。

### 1.4 其他为省重量做的取舍

| 措施 | 原句 |
|---|---|
| 锅炉舱放在机舱**之后**、共用一个烟囱 | wiki 舰级页：「In order that fuel gasses be kept clear of the superstructure, the **boiler rooms were moved behind the engine rooms**, exhausting into a **single funnel**. This orientation also **reduced the overall length of the armoured citadel**.」 |
| 只有 2 轴、大直径螺旋桨 | wiki 舰级页：「there were only **two shafts with quite large screws**. All previous British battleships after HMS Dreadnought of 1906 had **four** screws as did all British battleship classes after Nelson.」 |
| 上层建筑用轻材料、松木代替柚木甲板 | wiki 舰级页：「Additional weight-saving design measures included the use of light materials such as **aluminium for fittings**, and **fir instead of teak for deck planking**, although subsequently, **teak decks were fitted in the late 1920s**, following concerns that the ships could not fire a full broadside without causing structural damage to the decks.」 |
| 上层建筑本身只防破片 | wiki 舰级页：「Except for the emergency conning tower at its base, and the trunking for the main gun directors mounted on top, the superstructure was **lightly armoured against splinters only, to save weight**.」 |
| 总设计师的原话 | wiki 舰级页引 DNC Eustace Tennyson d'Eyncourt 对设计者 Edward Attwood：「"**In order to keep the displacement to 35,000 tons, everything is to be cut down to a minimum.**"」 |

### 1.5 省重量的代价：结构强度不够

- wiki 舰级页引 David K. Brown：「"It seems likely that **in the quest for weight saving, the structure was not quite strong enough**."」
- 同级两舰的实测后果（wiki 舰级页）：「Unlike Nelson, which exceeded the design specification for machinery weight, **the lighter machinery of Rodney resulted in chronic problems**. The ship's endurance declined substantially in the decade after her launch… Throughout the war **Rodney was plagued with leaks as a result of panting**, and the ship required repairs because of serious leaks in **1940, 1941 and 1944**. During one storm, the leaking was severe enough to **overwhelm a 50-ton pump**.」
- **注意这条是 Rodney 单独的问题**，Nelson 因为改装及时、机器超重反而没这么严重。**不要当舰级通用缺陷写。**

---

## 2. 主尺度与排水量

### 2.1 建造数据（两舰对照）

| 项 | Nelson（28） | Rodney（29） | 来源 |
|---|---|---|---|
| 承造厂 | **Armstrong, Elswick**（navypedia）/ Armstrong Whitworth, Walker（wiki） | **Cammell Laird, Birkenhead** | navypedia 表；wiki 建造表 |
| 船台号 | 991 | 904 | navypedia 表 |
| 开工 | **1922-12-28** | **1922-12-28** | navypedia「28.12.1922」；naval-history 两舰同 |
| 下水 | **1925-09-03** | **1925-12-17** | navypedia「3.9.1925」/「17.12.1925」 |
| 服役 | **1927-08（navypedia）/ 1927-08-15（naval-history、wiki 建造表）** | **1927-11（navypedia）/ 1927-12-07（naval-history、wiki）** | 见下 |
| 结局 | 1948 作轰炸靶标试验 → 1949-03-15 拖抵 Inverkeithing 拆解 | 1948-03-26 拖抵 Inverkeithing 拆解 | naval-history 两舰；wiki class |

**同名混淆警告（重要）**：navypedia 与 wiki 上都有**另一型 1912 年的「King George V」级**，而纳尔逊级的首舰名在 1922 年条约里被用来交换——条约第二条要求建成新舰后拆掉旧「King George V」。**查资料时不要和 1911 年那艘同名舰混起来。**

**Nelson 承造厂的两说**：navypedia 记 `Armstrong, Elswick`（埃尔swick），naval-history 记 `Armstrong, High Walker, Newcastle upon Tyne`（High Walker 船台），wiki 记 `Armstrong Whitworth, Walker`。**High Walker 是船台所在，Elswick 是公司总部/炮厂所在**——两者不矛盾，是同一家的两个地址口径。**并列，不裁。**

**Nelson 服役日**：navypedia `8.1927`（月级）、naval-history「commissioned on **15th August 1927**」、wiki 建造表「15 August 1927」。**navypedia 只给月份，另两源给到日，不构成分歧。**

### 2.2 主尺度（舰级值，取来源原句）

| 项 | 值 | 来源与原句 |
|---|---|---|
| 全长 oa | **216.4 m / 709 ft 10 in**（Nelson）；**216.5 m / 710 ft 3 in**（Rodney） | wiki 舰级页：「an overall length of **709 feet 10 inches (216.4 m) (Nelson) or 710 feet 3 inches (216.5 m) (Rodney)**」 |
| 全长（navypedia 单一值） | **216.4 m** | navypedia：「Length, m — 201.2 pp **216.4 oa**」——**只给了一个值，未区分两舰；wiki 明确两舰差 5 英寸** |
| 垂线间长 pp | **201.2 m / 660 ft** | navypedia：「**201.2 pp**」；wiki：「length between perpendiculars of **660 feet (201.2 m)**」 |
| 最大宽 | **32.3 m / 106 ft** | navypedia：「Breadth, m — **32.3**」；wiki：「a beam of **106 feet (32.3 m)**」 |
| 吃水（平均，标准） | **9.2 m**（wiki：30 ft 4 in；wiki Rodney：30 ft 2 in） | wiki 舰级页：「a draught of **30 feet 4 inches (9.2 m) at mean standard load**」；navypedia：「Draught, m — **8.56 mean, 10.2 extra deep load**」 |
| 型深 | **未获取** | 无任何已抓来源给出 |
| 方形系数 / 水线面积 | **未获取** | 同上 |
| 稳心高 GM（深载） | **3.1 m / 10.2 ft** | wiki 舰级页：「At deep load, they had a **metacentric height of 10.2 feet (3.1 m)**」 |
| 横摇周期 | **11.2–13.6 s** | wiki 舰级页：「which gave them a quick roll between **11.2 and 13.6 seconds**」 |

**长宽比的结论**（本报告推算，非来源数据）：201.2 / 32.3 ≈ **6.23**（pp/宽）。这是英国战列舰里相当「短粗」的比例，直接对应 23 节的低速——**但计算式是本报告做的，不是来源给的，引用时须注明。**

**吃水分歧**：9.2 m（wiki，标准状态）vs 8.56 m（navypedia，`mean`，未注状态）。差 0.64 m，无法用取整解释。**并列，不裁。**

### 2.3 排水量（四档分开，绝不合并）

| 口径 | Nelson | Rodney | 来源与原句 |
|---|---|---|---|
| **标准** | **33,300 long tons（33,800 t）**（wiki 舰级页）/ **33,313 t**（navypedia） | **33,730 long tons（34,270 t）** | wiki 舰级页：「They displaced **33,300–33,730 long tons (33,830–34,270 t) at standard load**」；navypedia：「Displacement standard, t — **Nelson: 33313 / Rodney: 33730**」 |
| **满载 / 深载** | **37,780 long tons（38,390 t）**（wiki 舰级页，Nelson as built）/ 37,430 lt（38,030 t）（wiki Rodney，即 Rodney 值） | **37,430 long tons（38,030 t）** | wiki 舰级页：「**37,780 long tons (38,390 t) (full load)**」；wiki Rodney：「**37,430 long tons (38,030 t) at deep load**」；wiki 舰级页区间：「**37,430–37,780 long tons (38,030–38,390 t) at deep load**」 |
| **注水舱充满（navypedia 自设口径）** | — | — | **41,250 t** —— navypedia：「Displacement full, t — **41250 (with buoyancy spaces filled)**」 |
| **Nelson 1940-08 满载** | **43,300 t** | — | navypedia 改装记录：「8/1940, Nelson: … **Full displacement was 43300t**」 |
| **Nelson 1945-01** | 37,000 / 44,054 t | — | navypedia：「1/1945, Nelson: … **displacement: 37000/44054t**」 |
| **Rodney 1942-05** | — | 36,000 / 43,140 t | navypedia：「5/1942, Rodney: … **displacement: 36000/43140t**」 |
| **Rodney 1944 深载** | — | 43,100 lt（43,800 t） | wiki Rodney：「increased the ship's **deep displacement to 43,100 long tons (43,800 t)**」 |
| **空载（light）** | **未获取** | **未获取** | 各来源均不设此档 |

**必须提醒的两个口径陷阱**：

1. **navypedia 的 41,250 t 不是满载。** 它明确写「with buoyancy spaces filled」——把防雷系统的注水舱算成排水量了，比 wiki 的深载 37,430 t 高出 3,820 t。**这个值不能与「满载」并列，也不能用来算载重储备。**
2. **条约意义上的「标准排水量」不含燃油与锅炉给水。** 而英国正是靠这一点钻了空子：
   - wiki 舰级页：「The British had successfully ensured that the definition of maximum displacement – the standard displacement – **excluded both fuel and boiler feed water**. They had argued that having to protect the widespread British Empire meant their ships had to carry more of both… As a result, **water-filled internal anti-torpedo bulges could be incorporated, which did not contribute to the "dry" (standard) weights** and therefore did not exceed the treaty displacement limits.」
   - **这条极重要**：本级的防雷系统能做成「内部注水舱」而不是外置防雷突出部，是条约定义被英国改写的结果。防雷与航速（无突出部阻力）两头都赚了。

---

## 3. 动力

| 项 | 值 | 来源与原句 |
|---|---|---|
| 形式 | **2 组 Brown-Curtis 齿轮传动汽轮机，2 轴** | navypedia：「**2 sets Brown-Curtis geared steam turbines**」；wiki：「two sets of Brown-Curtis geared steam turbines, each driving one shaft」 |
| 锅炉 | **8 × Admiralty 三鼓水管锅炉，带过热器** | navypedia：「8 Admiralty 3-drum boilers」；wiki：「eight Admiralty 3-drum boilers fitted with superheaters」 |
| 锅炉压力 | **250 psi（1,724 kPa；17 atm）** | wiki 舰级页：「operated at a pressure of **250 psi (1,724 kPa; 17 atm)**」 |
| 蒸汽温度 | **未获取** | 无来源给出 |
| 设计功率 | **45,000 shp（34,000 kW）** | navypedia：「Power, h. p. — **45000**」；wiki：「rated at **45,000 shaft horsepower (34,000 kW)**」 |
| 实测功率（1927 试航） | **45,614–46,031 shp** | wiki 舰级页：「reaching speeds of 23.6–23.8 knots from **45,614–46,031 shp (34,014–34,325 kW)**」；Rodney 单舰值 **45,614 shp**（wiki Rodney，1927-09-07 试航） |
| 设计航速 | **23 kn** | navypedia：「Max speed, kts — **23**」 |
| 实测航速 | **23.6–23.8 kn** | 同上 |
| 螺旋桨 | 2 只，直径较大 | wiki：「only two shafts with quite **large** screws」；**具体直径未获取** |
| 舵 | **单舵，中线，不在螺旋桨尾流中** | wiki：「the ships having a **single, central rudder** which was out of the propeller race of the twin screws」 |
| 燃油 | **Nelson 3,805 t / Rodney 3,770 t** | navypedia：「Fuel, t — **Nelson: 3805 oil / Rodney: 3770 oil**」；wiki：「They carried **3,770–3,805 long tons (3,830–3,866 t)** of fuel oil」 |
| 续航（设计） | **7,000 nm @ 16 kn** | wiki：「to give them a **designed range of 7,000 nautical miles (13,000 km) at a cruising speed of 16 knots**」 |
| 续航（navypedia 口径） | **14,500 nm @ 10 kn** | navypedia：「Endurance, nm(kts) — **14500(10)**」 |
| 发电机 | **未获取** | 无来源给出台数与功率 |
| 舱段划分 | **未获取** | 只知「锅炉舱在机舱之后」，无逐舱描述 |

**续航两说并列不裁**：7,000 nm @16 kn 与 14,500 nm @10 kn 航速档不同，理论不冲突；但换算到同一档差异显著，且两源均未给计算口径。**并列。**

**为什么只有 23 节（原句）** ——
- navypedia：「It was possible to retain armour and armaments practically without changes **at the expense of a speed restriction in 23kts**.」
- wiki 舰级页：「the resulting Nelson class **sacrificed installed power (and hence speed) in order that the ships be well-armed and defended**.」
- 补偿手段：**船体线型极优** ——「As a countermeasure to the limited power, the hull was of a **very efficient hydrodynamic form**, to attain the best possible speed.」（wiki 舰级页）
- **实战后果**：1941-05-27 追击俾斯麦时 Rodney 的最高速只有 21 节，被 KGV 追上并超越。这是「23 节设计值」在 14 年服役后的实际表现，**不要拿设计值当战时值**。

---

## 4. 防护

> **本级的装甲方案是「all or nothing」在英国的第一次应用**（navypedia：「Armour, **for the first time in British practice**, corresponded to a principle "**all or nothing**".」），核心是**内置、外倾 18° 的装甲带**，用倾角换等效厚度。

### 4.1 主装甲带

| 项 | 值 | 来源与原句 |
|---|---|---|
| **位置** | **舰体内侧**（built into the hull，不是贴在舷外） | navypedia：「Internal main 330mm (356mm abreast magazines) belt was 3.96m-deep」；「Belt was **internal and inclined at 18° to vertical**」 |
| **倾角** | **18°（向外倾）** | navypedia：「inclined **inside** at 18°」；wiki：「its upper edge was inclined **18° outward**」 |
| **厚度：弹药库段** | **356 mm（14 in）** | navypedia：「330mm (**356mm abreast magazines**)」；wiki：「**14 in (356 mm) thick between the main gun barbettes**」 |
| **厚度：机舱与 6 英寸弹药库段** | **330 mm（13 in）** | wiki：「and thinned to **13 inches (330 mm) over the engine and boiler rooms as well as the six-inch magazines**」 |
| **纵向范围** | **117.0 m**，从 A 炮座到副炮弹药库之间 | navypedia：「protected **117.0m of ship length** between barbette "A" and secondary magazines」 |
| **高度（depth）** | **3.96 m** | navypedia：「belt was **3.96m-deep**」 |
| **未覆盖首尾** | **前不到舰首、后不到舰尾** | wiki：「but **did not reach either the bow or the stern**」 |
| **下端连接** | 与 30° 斜板相连，斜板再接 15° 倾斜的 38 mm 纵舱壁 | navypedia：「its lower edge connected with **30°-sloped plate**, this plate connected with **15°-inclined longitudinal 38mm bulkhead**」 |
| **为什么用倾角** | 提高对落弹的等效厚度 | wiki：「To improve its ability to **deflect plunging fire**, its upper edge was inclined 18° outward.」；「The slope **increased the relative thickness of the belt to a plunging projectile**」 |
| **为什么内置** | 外壳先引爆、爆点落在装甲之外 | wiki：「Water-filled compartments, surrounded by air-filled ones, formed internal torpedo bulges which were fitted **between the armour and the external hull of the ship, which was not armoured**. The outer hull plating was **meant to initiate detonation of shells which would then explode outside the armour**.」 |

### 4.2 装甲甲板

| 部位 | 厚度 | 来源与原句 |
|---|---|---|
| **主弹药库上方** | **159 mm（6.25 in）** | navypedia：「Its thickness was **159mm over magazines** and 95mm over machinery」；wiki：「ranged in thickness from **6.25 inches (159 mm) over the main-gun magazines**」 |
| **机舱与副炮弹药库上方** | **95 mm（3.75 in）** | wiki：「**3.75 inches (95 mm) over the propulsion machinery spaces and the secondary magazines**」 |
| 舰尾（下层甲板，舵机上方） | **108 mm（4.25 in）** | wiki：「Aft of the citadel was an armoured deck **4.25 inches (108 mm) thick** at the level of the lower edge of the belt armour that extended almost to the end of the stern to **cover the steering gear**」 |
| 上层建筑外的中间甲板 | 前部 **178 mm** 平 / 后部 **108 mm** + 108 mm 斜部 | navypedia：「Fore part of this deck was flat and has **178mm** thickness, aft part was **108mm with 108mm slopes**」 |
| 底下结构板 | + **12.7 mm**（0.5 in） | wiki：「both on top of the **0.5 in (12.7 mm) deck plating**」 |
| **是不是「单层厚甲板」** | **是，英国战列舰第一次** | wiki：「For the **first time a British battleship had a single, 6.25 in (159 mm) thick armoured deck** to protect against plunging shells and aircraft-launched bombs」 |

**「一层甲板 vs 多层甲板」是本级与他国的关键差异**：德国俾斯麦级走「多层薄甲板逐层减速」，纳尔逊级走「单层厚甲板一次挡住」。两种哲学都不算错，但**不能拿「甲板总厚度」直接比大小**——俾斯麦三层合计 230 mm 与纳尔逊单层 159 mm 不是一回事。

### 4.3 炮塔与炮座

**navweaps 给的是「按板重（lbs）与厚度（in）双标」的英国口径**（因为英国按 40 lb/ft² = 1 in 标板厚），这是本级炮塔数据唯一带板重的一手化来源：

> 「Face: **15.68 in (39.8 cm) (640 lbs.)**
> Fore Sides: **10.78 in (27.4 cm) (440 lbs.)**
> Rear Sides: **8.82 in (22.4 cm) (360 lbs.)**
> Rear: **8.82 in (22.4 cm) (360 lbs.)**
> Roof: **7.105 in (18.0 cm) (320 lbs.)**」
> —— navweaps 16"/45，转引 Campbell《Naval Weapons of World War Two》与 Raven & Roberts《British Battleships of World War Two》

| 部位 | navweaps（in / cm / 板重） | navypedia（mm） | wiki（in/mm） |
|---|---|---|---|
| 正面 | **15.68 in / 39.8 cm / 640 lbs** | **406** | **16 in / 410 mm** |
| 前侧面 | **10.78 in / 27.4 cm / 440 lbs** | 280（「sides」单值） | **11 in / 280 mm** |
| 后侧面 | **8.82 in / 22.4 cm / 360 lbs** | 280（同上） | — |
| 后面 | **8.82 in / 22.4 cm / 360 lbs** | **229** | **9 in / 230 mm** |
| 顶部 | **7.105 in / 18.0 cm / 320 lbs** | **184** | **7.25 in / 184 mm** |

**为什么正面有 15.68 / 16 / 406 / 410 四个数**：这是英国「按板重标厚」与「名义厚度」两套口径 + 英制/公制换算的三重叠加。
- 15.68 in × 40 lb/ft² ≈ 627 lbs，与标注 640 lbs 接近（取整差）；
- 16 in × 40 = 640 lbs **正好对上**，所以「16 in」是**板重口径**的取整值，「15.68 in」是**名义厚度**；
- 410 mm 是 16 in 的精确公制换算（406.4 → 410 取整），406 mm 是 16 in 的直接换算。
- **结论：这不是四个互斥的数，是两套口径 × 两种单位。引用时必须注明是哪一套。**（本报告分析，非来源明说）

**炮座（barbettes）**：

| 来源 | 值 |
|---|---|
| navypedia | 「barbettes: **381 - 305**」；正文：「Barbettes were **381mm at beam sides** and **305mm at fore and aft sides**.」 |
| wiki | 「The KC armour of the barbettes ranged in thickness from **12 to 15 inches (305 to 381 mm)**」；正文：「with **15 in (380 mm)** around the barbettes」 |

**两源一致（305–381 mm），只是区间表述方式不同。**

### 4.4 司令塔 / 横向舱壁 / 烟道

| 部位 | navypedia | wiki |
|---|---|---|
| 司令塔 | 「CT: **356 (sides) - 305 (face) - 254 (rear) - 165 (roof) - 102 (deck)**」 | 「12 to 14 inches (**305 to 356 mm**) thick with a **6.5-inch (170 mm) roof**」 |
| 司令塔通信筒 | 「communication tube: **152**」 | — |
| 前横舱壁 | 「Fore bulkhead was **305mm** between main and intermediate decks」；另「Second fore bulkhead was **203mm**」 | 「transverse bulkheads of non-cemented armour **8 and 12 inches (203 and 305 mm)** thick at the forward end」 |
| 后横舱壁 | 「aft bulkhead was **254mm**」；「aft bulkhead of steering room has **102mm**」 | 「**4 and 10 inches (102 and 254 mm)** thick at the aft end」 |
| 烟道（funnel uptakes） | 「funnel uptakes: **229 - 203**」 | **未获取** |
| 副炮塔 | 「secondary turrets: **38 - 25**」；「its gunhouses had **38mm faces and 25mm sides, rears and crowns**」 | 「only **1 in (25 mm) NC all round over 0.5 in (12.7 mm) structural steel plates**」；另处「1–1.5 inches (**25–38 mm**）」 |

**司令塔顶部分歧**：165 mm（navypedia）vs 170 mm（wiki，6.5 in）。5 mm 差，换算取整级，**不构成实质分歧**。

**副炮塔防护**：navypedia 说「正面 38 / 侧面、后、顶 25」，wiki 说「全向 25 mm NC 覆在 12.7 mm 结构板上」。**两说法的差别在于「正面 38 mm」是否单独加厚**——navweaps 6"/50 页说「 seulement 1" (25 mm) HT plating」。**三说并列，不裁；但「副炮塔极薄，一发就可能全瘫」这个定性判断三源一致。**

### 4.5 防雷系统

| 项 | 值 | 来源与原句 |
|---|---|---|
| **总深度** | **3.7 m / 12 ft** | wiki：「They had a **total depth of 12 feet (3.7 m)**」；navypedia：「Underwater protection was **3.1m deep**」←**两说不一致** |
| **结构** | 外空舱 + 内水舱（void-liquid） | wiki：「an **empty outer watertight compartment** and an **inner water-filled compartment**」；navypedia：「Distance between this bulkhead and ship side (deep of underwater protection) was **3.05-3.7m**」 |
| **保持舱壁** | **38 mm** | navypedia：「included **38mm longitudinal bulkhead**」；wiki：「backed by a torpedo bulkhead **1.5 inches thick**」（1.5 in = 38.1 mm，**同值**） |
| **设计指标** | **340 kg TNT** | navypedia：「It could resist exploding of **340kg TNT**.」；wiki：「rated to withstand an explosion of **750 lbs (340 kg) TNT**」（**同值，单位不同**） |
| **双层底** | **1.5 m / 5 ft** | wiki：「provided by a **double bottom 5 feet (1.5 m) deep**」 |
| **与胡德号的关系** | 同族方案、同级效果 | wiki：「The system was **similar in design and effectiveness to that of Hood**」 |

**防雷深度的两说（必须并列）**：3.7 m（wiki，总深度）vs 3.1 m（navypedia，`Underwater protection was 3.1m deep`）。navypedia 同页另有一句「Distance between this bulkhead and ship side (deep of underwater protection) was **3.05-3.7m**」——**即 navypedia 自己给了 3.05–3.7 的区间，3.1 是区间下限，wiki 的 3.7 是区间上限。**（本报告判断）两者不是矛盾，是区间表述。**但本报告不代来源裁决，两组数并列记录。**

### 4.6 装甲总重与占比

- **未获取。** 全部已抓来源（navypedia、wiki 舰级页、wiki 单舰页、naval-history 两舰页）**均未给出纳尔逊级的装甲总吨位或占排水量比**。
- 对照：本级最常被引用的一句话是「省下的重量堆到装甲上」，但**没有任何来源给出这个「堆」到底堆了多少吨**。这是本文件最大的数据空洞，见 §9。
- 已知的间接线索（wiki 舰级页）：「Armour weight was also reduced by using an internal, inclined armour belt sloped outward at 18 degrees from the vertical.」——**注意这句说的是「装甲重量也被降低了」，与「堆厚装甲」的通行叙事方向相反**。它的意思是：整体装甲重量比 G3 低（因为吨位砍了），但把有限的重量集中到堡内、堆到最厚。**两个说法都对，但表述必须精确，否则会自相矛盾。**

### 4.7 装甲钢型号

| 部位 | 钢种 | 来源 |
|---|---|---|
| 舷侧带 | **KC（Krupp cemented）** | wiki：「The ships' waterline belt consisted of **Krupp cemented armour (KC)**」 |
| 横舱壁 | **NC（non-cemented，均质）** | wiki：「transverse bulkheads of **non-cemented armour**」 |
| 装甲甲板 | **NC** | wiki：「Its **non-cemented armour plates** ranged in thickness」 |
| 副炮塔 | **NC + 结构钢** | wiki：「1 in (25 mm) **NC** all round over 0.5 in (12.7 mm) **structural steel plates**」 |
| 6 英寸炮塔（navweaps 口径） | **D quality steel** | navweaps 6"/50：「Armor protection was **D quality steel**.」 |
| 副炮工作区外板 | **HT（high tensile）1 in** | navweaps 6"/50：「only lightly protected by **1" (25 mm) HT plating**」 |

**注意**：英国自己用 KC/NC 这套命名，与德式 KC n/A、Wh、Ww 不是同一体系，**不要混用缩写**。

---

## 5. 主炮：16"/45（40.6 cm）Mark I

> 本节数据主要来自 `navweaps-16in-45-mk1`（D 级，但内容转引 Campbell / Raven & Roberts / Burt 三部权威二次文献，可靠性接近 C）。
> **炮与炮塔是 G3 的遗产**，见 §0。

### 5.1 炮本身

| 项 | 值 | 原句 |
|---|---|---|
| 型号 | **16-inch Mark I** | 「Designation — **16-inch Mark I**」 |
| 装舰 | Nelson class | 「Ship Class Used On — **Nelson class**」 |
| 设计年份 | **1922** | 「Date Of Design — **1922**」 |
| 服役年份 | **1927** | 「Date In Service — **1927**」 |
| 炮重（含炮闩） | **108 tons（109.7 mt）** | 「With Breech mechanism: **108 tons (109.7 mt)**」 |
| 炮重（不含炮闩） | **106 tons（107.7 mt）** | 「Without Breech mechanism: **106 tons (107.7 mt)**」 |
| 全长 oa | **742.2 in（18.852 m）** | 「Gun Length oa — **742.2 in (18.852 m)**」 |
| 膛线部长度（bore） | **720.0 in（18.288 m）= 45 倍径** | 「Bore Length — **720.0 in (18.288 m) / 45 calibers**」 |
| 膛线长度（Mark I 膛线） | **586.96 in（14.909 m）** | 「Mark I rifling: **586.96 in (14.909 m)**」 |
| 膛线长度（Mark II 膛线） | **588.95 in（14.959 m）** | 「Mark II rifling: **588.95 in (14.959 m)**」 |
| 阴膛线（Mark I） | **80 条**，深 0.135 in × 宽 0.377 in | 「Mark I rifling: **(80)** 0.135 in deep x 0.377」 |
| 阴膛线（Mark II） | **96 条**，深 0.124 in × 宽 0.349 in | 「Mark II rifling: **(96)** 0.124 in deep x 0.349」 |
| 缠度 | **等齐右旋 1 转 / 30 倍径** | 「Twist — **Uniform RH 1 in 30**」 |
| 药室容积 | **35,205 in³（576.9 dm³）** | 「Chamber Volume — **35,205 in3 (576.9 dm3)**」 |
| 射速 | **1.5 发/分** | 「Rate Of Fire — **1.5 rounds per minute**」 |
| 炮管寿命 | **200–250 发** | 「Approximate Barrel Life — **200 - 250 rounds**」 |
| 每门备弹 | **95 发 APC + 10 发练习弹** | 「Ammunition stowage per gun — **95 APC and 10 practice rounds**」 |
| 制造数 | **29 门**，由 Elswick、Vickers、Beardmore、Royal Gun Factory 造 | 「Some **29 guns** were made by **Elswick, Vickers, Beardmore and the Royal Gun Factory**.」 |
| 结构 | 锥形内 A 管 + 全长锥形绕丝 + B 管 + 套筒 + 炮尾环 | 「Constructed of a **tapered inner A tube** with two rear locating shoulders, A tube, **full length taper wound wire**, B tube, overlapping jacket and breech ring」 |
| **是否最后一代绕丝炮** | **是**，且是英海军**唯一装在三联装里的** 16 英寸炮 | 「These were the **last wire-wound guns built for the Royal Navy** and the **only ones to see service mounted in triple turrets**.」 |
| 炮闩 | Welin 式，Asbury 液压操作 | 「A breech bush was used to attach the **Welin breech block** which was operated by an **Asbury hydraulic mechanism**.」 |

### 5.2 弹药与初速（本级最受争议的技术点）

| 项 | 值 | 原句 |
|---|---|---|
| **弹重（APC Mark IB）** | **2,048 lbs（929 kg）** | 「APC Mark IB: **2,048 lbs. (929 kg)**」 |
| 弹重（HE Mark IB / HE Mark IIC(?)） | 同为 **2,048 lbs（929 kg）** | 「HE Mark IB: 2,048 lbs. (929 kg)」「HE Mark IIC(?): 2,048 lbs. (929 kg)」 |
| APC 装药 | **51.2 lbs（23.2 kg）TNT** | 「APC Mark IB: **51.2 lbs. (23.2 kg) TNT**」 |
| HE IB 装药 | **166 lbs（75.3 kg）** | 「HE Mark IB: **166 lbs. (75.3 kg)**」 |
| APC 弹长 | **66.23 in（168.2 cm）** | 「APC Mark IB: **66.23 in (168.2 cm)**」 |
| **发射药** | **初期 498 lbs（225.9 kg）MD45；1930 年后 495 lbs（224.5 kg）SC280** | 「Initial: **498 lbs. (225.9 kg) MD45** / After 1930: **495 lbs. (224.5 kg) SC280**」 |
| 发射药包装 | **6 包** | 「The propellant charge was in **six bags**.」 |
| **初速（Mark I 膛线，新炮）** | **2,586 fps（788 mps）** | 「New gun Mark I rifling: **2,586 fps (788 mps)**」 |
| **初速（Mark II 膛线，新炮）** | **2,614 fps（797 mps）** | 「New gun Mark II rifling: **2,614 fps (797 mps)**」 |
| 膛压（Mark I） | **20.0 tons/in²（3,150 kg/cm²）** | 「Mark I rifling: **20.0 tons/in2 (3,150 kg/cm2)**」 |
| 膛压（Mark II） | **21.3 tons/in²（3,355 kg/cm²）** | 「Mark II rifling: **21.3 tons/in2 (3,355 kg/cm2)**」 |

### 5.3 射程与穿深

**射程表（AP，初速 2,525 fps / 770 mps 条件）**：

| 仰角 | 射程 | 落速 | 落角 |
|---|---|---|---|
| 2.3° | 5,000 yd（4,570 m） | 2,248 fps（685 mps） | 2.5° |
| 5.1° | 10,000 yd（9,140 m） | 1,996 fps（608 mps） | 5.9° |
| 8.5° | 15,000 yd（13,720 m） | 1,778 fps（542 mps） | 10.2° |
| 12.5° | 20,000 yd（18,290 m） | 1,606 fps（490 mps） | 16.5° |
| 17.5° | 25,000 yd（22,860 m） | 1,486 fps（453 mps） | 24.6° |
| 23.7° | 30,000 yd（27,430 m） | 1,431 fps（436 mps） | 33.5° |
| 32.4° | 35,000 yd（32,000 m） | 1,453 fps（443 mps） | 43.7° |
| 39.2° | 37,500 yd（34,290 m） | 1,503 fps（458 mps） | 50.5° |
| **40.0°（最大仰角）** | **约 38,000 yd（34,750 m）** | — | — |

**穿深表（USN 经验公式，初速 2,525 fps）**：

| 射程 | 舷侧装甲 | 甲板装甲 |
|---|---|---|
| 15,000 yd（13,716 m） | **14.4 in（366 mm）** | 1.95 in（50 mm） |
| 20,000 yd（18,288 m） | **12.2 in（310 mm）** | 2.85 in（72 mm） |
| 25,000 yd（22,860 m） | **10.3 in（261 mm）** | 3.90 in（99 mm） |
| 30,000 yd（27,432 m） | **8.8 in（224 mm）** | 5.10 in（130 mm） |
| 35,000 yd（32,004 m） | **7.6 in（193 mm）** | 6.50 in（165 mm） |

**注**：穿深表来自 Garzke & Dulin《Battleships: Allied Battleships in World War II》，用的是**美国海军经验公式**。**俄式/德式公式会给出不同结果，跨舰比较时必须统一公式。** 本报告不换算。

### 5.4 「轻弹高速」这个决定为什么是错的（本级技术史最重要的一段）

原文（navweaps，逐段引）：
> 「From inadequate firing trials, a **mistaken theory** was promulgated by the Director of Naval Ordnance (DNO) that held that a **high-velocity, low-weight projectile would have superior armor penetration characteristics at large oblique angles of impact**, a conclusion which was **the opposite of previous findings**. This theory **was not substantiated by later trials**, but these took place **too late to affect the decision** to use a lightweight APC projectile for new designs. As a result, **these guns proved to be only marginally better in terms of armor penetration than the previous 15"/42 (38.1 cm) Mark I and much less satisfactory than those older guns in terms of accuracy and barrel life**.」

wiki 舰级页给同一件事的来源：
> 「The BL 16-inch Mk I naval guns themselves deviated from standard British designs. Where previous RN weapons fired **heavy shells at a moderate velocity**, the Nelson's weapons **followed the German practice of a lighter shell at a higher velocity**. This change in Director of Naval Ordnance policy was due to **British testing of surrendered German equipment after World War I**, although much later, subsequent testing proved contradictory.」

**后果链（三步，每步有原句）**：

1. **膛线被磨秃** —— navweaps：「The very first test firings of these guns found that they had a **serious wear problem, with a barrel life of only 180 rounds**. It was also found that there was a **considerable loss of accuracy during continuous firing**, as there was a tendency for the projectiles to **strip the rifling out of the guns** ". . . due to the hammering action of the **short bodied, long headed projectile** on its way down the bore . . ."」
2. **改膛线、减装药、改弹带** —— 同上：「As a result, **the rifling in the liners was changed (known as Mark II rifling)** for newer guns, **the powder charge and chamber size were reduced** to the figures shown in the tables above and **the diameter of the projectile driving band was increased**.」
3. **仍然不如老的 15 英寸** —— 同上：「**Even with these changes, the barrel life and accuracy still compared poorly with the previous 15"/42 (38.1 cm) Mark I.**」

**两级膛线混装的怪现象（本级独有）**：
> 「The different riflings were **mixed on each ship and even in each turret**. According to "Naval Weapons of World War Two," this was **unique** as "**such differences were totally at variance with the usual British policy** for heavy guns in important ships" whereby every effort was made to ensure that each ship had guns of uniform characteristics.」

具体换装时序（含两舰差异）：
- 建成时：**两舰全部为 Mark I 膛线**
- **Rodney 1937-12**：B 塔换成 **2 门 Mark II + 1 门 Mark I**
- **1938**：Rodney X 塔换 **3 门全新 Mark I**；**Rodney A 塔 1942-02** 换 **3 门全新 Mark II**
- **Nelson 1944-05**：B、X 两塔换 Mark II；**A 塔到 1945-03 才换**
- 后果：「This mixing on Nelson and Rodney **caused initial dispersion problems due to the differing muzzle velocities**, but these reportedly **became less pronounced as the guns wore**.」
- **A 塔的三门短药室炮**：「Guns Nos. 3, 4 and 24 had chambers of the same volume as the others but **the chamber length was less** and the rifled length longer as a consequence. **These three guns were used in A turret on Nelson until March 1945.**」

### 5.5 三联装炮塔

| 项 | 值 | 原句 |
|---|---|---|
| 型号 | **Mark I**（Nelson 级三座） | 「Nelson (3): **Mark I**」 |
| **重量：A、X 塔** | **1,464 tons（1,487 mt）** | 「"A" and "X": **1,464 tons (1,487 mt)**」 |
| **重量：B 塔（背负）** | **1,483 tons（1,506 mt）** | 「"B": **1,483 tons (1,506 mt)**」 |
| 俯仰 | **−3° / +40°** | 「Elevation — **-3 / +40 degrees**」 |
| 俯仰速率 | **10°/s** | 「Rate of Elevation — **10 degrees per second**」 |
| 旋回范围 | **A 塔 ±149°；B 塔 ±165°；X 塔约每侧 60–130°** | 「"A" Turret: **+/- 149 degrees**；"B" Turret: **+/- 165 degrees**；"X" Turret: **About 60 to 130 degrees on either side**」 |
| 旋回速率 | **4°/s**（横摇 >5° 时降为 **2°/s**） | 「Rate of Train — **4 degrees per second**」；「Rate of Train was **limited to 2 degrees per second when the ship's roll exceeded 5 degrees**.」 |
| 后座行程 | **44.6 in（113 cm）** | 「Gun Recoil — **44.6 in (113 cm)**」 |
| 装填角 | **+3°（固定）** | 「Loading Angle — **+3 degrees**」 |
| 炮间距 | **98 in（249 cm）** | 「The gun axes were **98 in (249 cm)** apart.」 |
| B 塔炮组人员 | **1 名军官 + 98 人**（含弹药舱、弹库、发射药转运间、药库） | 「The turret crew for "B" turret was **1 officer and 98 men** including those in the handling room, shell room, cordite handling room and magazine. The other turrets had **12 less men** in the ammunition supply chain.」 |

**三联装的机械复杂度（原句，这是全部故障的根源）**：
> 「These triple mountings proved to be **quite troublesome** during their early careers due to their **complex design**. This complexity was partially due to the nature of mounting **three independently sleeved guns**, but it was also because of the **British excessive use of interlocks** in the ammunition loading and supply systems and by the use of a **large number of swash-plate engines**. There were **nearly 50 mechanical interlocks associated with the loading of each gun**. Although the anti-flash precautions were good in these mountings, **the turrets still lacked flash shields between the guns**.」

**装填机构（原句，解释为什么射速只有 1.5 发/分）**：
> 「Each gun was served by a **pusher shell hoist** and a **cordite hoist**. The shell hoist delivered the shells in a bucket vertically to the rear of the gun. The **cordite hoists were a dual canister design**… each canister holding **three bags** of propellant vertically.」

**射速为什么这么低（原句，最关键的一段）**：
> 「The designed loading-cycle for these mounts was **30 seconds**, but in practice, it was **35 seconds for one gun**. As the shell loading in the handling rooms **required 50 seconds**, the **maximum sustained rate of fire was one round per gun every 50 seconds**. However, because of the necessity of firing **wing and center guns of turrets in different salvos** [in order to reduce dispersion problems], the firing rate was **further reduced to one round every 60 to 65 seconds**.」

**实战对照**：1941-05-27 打俾斯麦时，Rodney 平均 **1.6 齐射/分**（齐射法，输出率 77%）、**1.1 舷射/分**（舷射法，输出率 62%）；第一小时约 **1.5 齐射/分**。（navweaps 16"/45）

**三联装的历史评价（两个方向都引）**：

- **批评**（Binney 舰长 1930 年报告）：「The main disadvantage of Nelson's triple mounting is **loss of output** on account of the fact that **the three guns cannot be fired together owing to ballistic difficulties, whereas they must be loaded together**.」
- **辩护**（同一份报告，前一段）：「The **great advantage of the triple mounting system** from construction point of view (which is that the armament can be **concentrated in a much smaller space, and will require less of armoured protection**) has not, perhaps been **sufficiently emphasized**.」
- **实测证明**（同一份报告）：「The mounting may be said to have proved itself, when in **October 1929**, one turret crew with two years experience **loaded and fired 33 rounds without mishap**. The main defects appear to be the **roller paths and the rollers**.」

**滚轮路径缺陷（1927 年发现，两舰都中招）** —— navweaps：
> 「An inspection of **Rodney's turret roller-paths in 1927** showed that the inner edge of the lower roller path was **cutting into the flanges of the turret-rollers**. A quickly-ordered inspection of **Nelson found much the same problem**. The damage was determined to be caused by the **lateral thrust created when the heavy turrets were trained**, especially when in a seaway.」
> 解决：「a satisfactory solution was found by the fitting of a **new set of vertical rollers**… **Addition of these vertical rollers to both battleships was completed by October 1929** and the restriction in maximum training speeds was eliminated.」

---

## 6. 副炮与高炮

### 6.1 6"/50（15.2 cm）BL Mark XXII（副炮）

> **⚠️ 型号陷阱（先读这条）**：本级副炮是 **炮身 Mk XXII + 炮座 Mark XVIII**，**不是** Mk XXIII。
> `data/sources.yaml` 已在 2026-11-21 被更正（`navweaps-6in-50-mk23` note 改为「不是 Rodney 副炮」，并新增 `navweaps-6in-50-mk22`），
> 但 **`work/raw/last-battle.md` 第 398–399 / 685 行仍是 Mk XXIII，尚未跟改**。
> 硬证据：navweaps Mk XXIII 页的 `Ship Class Used On` 是「**Leander, Perth, Arethusa, Southampton ("Town"), Edinburgh, Fiji, Ceylon, Swiftsure**」——**全是巡洋舰，通篇没有 Nelson class**。
> 详见 `rodney-tech.md` §0.1 与 §9.2。

| 项 | 值 | 原句（navweaps 6"/50） |
|---|---|---|
| 型号 | **6"/50 (15.2 cm) BL Mark XXII** | 「Designation — **6"/50 (15.2 cm) BL Mark XXII**」 |
| 装舰 | Nelson class | 「Ship Class Used On — **Nelson Class**」 |
| 设计年份 | 约 **1921** | 「Date Of Design — **about 1921**」 |
| 服役年份 | **1926** | 「Date In Service — **1926**」 |
| 炮重（不含炮闩） | **19,824 lbs（8,992 kg）** | 「Without Breech: **19,824 lbs. (8,992 kg)**」 |
| 炮闩重 | **364 lbs（165.1 kg）** | 「Weight of Breech: **364 lbs. (165.1 kg)**」 |
| 全长 oa | **309.7 in（7.866 m）** | 「Gun Length oa — **309.7 in (7.866 m)**」 |
| 膛线部 | **300 in（7.620 m）** | 「Bore Length — **300 in (7.620 m)**」 |
| 阴膛线 | **36 条**，深 0.046 in × 宽 0.3759 in | 「**(36)** 0.046 in deep x 0.3759」 |
| 药室容积 | **1,750 in³（28.7 dm³）** | 「Chamber Volume — **1,750 in3 (28.7 dm3)**」 |
| 射速 | **5 发/分** | 「Rate Of Fire — **5 rounds per minute**」 |
| **弹重（CPBC Mark XXVB）** | **100 lbs（45.36 kg）** | 「CPBC Mark XXVB: **100 lbs. (45.36 kg)**」 |
| 弹重（CPBC，1942 年型） | **112 lbs（50.8 kg）** | 「CPBC (1942): **112 lbs. (50.8 kg)**」 |
| **发射药** | **31 lbs（14.1 kg）SC 150，单包装** | 「**31 lbs. (14.1 kg) SC 150**」；「The propellant was in a **single bag**.」 |
| **初速** | **2,945 fps（898 mps）** | 「Muzzle Velocity — **2,945 fps (898 mps)**」 |
| 膛压 | **20 tons/in²（3,150 kg/cm²）** | 「Working Pressure — **20 tons/in2 (3,150 kg/cm2)**」 |
| 炮管寿命 | **600 发** | 「Approximate Barrel Life — **600 rounds**」 |
| 备弹 | 正常 **100 发/门**，最大 **150 发/门** | 「Normal: **100 rounds** / Maximum: **150 rounds**」 |
| 最大射程 | **25,800 yd（23,590 m）@45°** | 「45.0 degrees … **25,800 yards (23,590 m)**」 |
| 装舰数 | **6 座双联** | 「Nelson (6): **Mark XVIII**」 |
| 炮塔重 | **168,000 lbs（76,204 kg）** | 「Weight — **168,000 lbs. (76,204 kg)**」 |
| 俯仰 | **−5° / +60°** | 「Elevation — **-5 / +60 degrees**」 |
| 俯仰速率 | **8°/s** | 「Elevation Rate — **8 degrees per second**」 |
| 旋回范围 | 前座 **±75°**；中（背负）座 **±90°**；后座 **±72.5°** | 「Forward Mountings: **+75 / -75 degrees** / Center (superfiring) Mountings: **+90 / -90 degrees** / After Mountings: **+72.5 / -72.5 degrees**」 |
| 旋回速率 | 约 **5°/s** | 「Train Rate — **about 5 degrees per second**」 |
| 后座行程 | **16.5 in（42 cm）** | 「Gun recoil — **16.5 in (42 cm)**」 |
| 装填角 | **+5°** | 「Loading Angle — **+5 degrees**」 |
| 防护 | **D 级钢**（见 §4.7） | 「Armor protection was **D quality steel**.」 |

**「高仰角但打不了飞机」这个设计尴尬（原句）**：
> 「Like many British medium-caliber mountings of the 1920s, these guns had a **high maximum elevation so that they could engage aircraft**, but this was of **secondary importance** to their use in the anti-ship role. In reality, the **training and elevation speeds of the mountings were too slow for the AA role**.」

**为什么射速达不到设计要求（原句）**：
> 「The **original design requirement was for a rate of fire of 7 to 8 rounds per minute** but **On trials, the best rate achieved was 4 rounds per minute**. Some modifications were carried out afterwards, and these improved the rate of fire.」

**实战表现（Rodney，1941-05-27 —— 这是本炮唯一有实战射速记录的战例）**：
> 「During her battle with Bismarck, HMS Rodney fired **150 salvos** (one gun from each turret) from her **starboard battery at an average of 5 salvos per minute** and **98 salvos** from her **port battery at an average of 3.9 salvos per minute**. During the first 9 minutes at close range she achieved **5.9 rounds per minute at an output of nearly 100%**. In all, Rodney fired **716 rounds** of 6" CPBC during this action.」

**注意**：这里 navweaps 给的 716 与炮术报告的 **706** 冲突（战报为 A 级一手）。口径差同 16 英寸那 2 发——补给领用数 vs 实发数。详见 `rodney-tech.md` §3.2。

### 6.2 4.7"/40（12 cm）QF Mark VIII（重型高炮）

| 项 | 值 | 原句（navweaps 4.7"/40） |
|---|---|---|
| 型号 | **4.7"/40 (12 cm) QF Mark VIII** | 页题 |
| 装舰 | **Nelson**、Courageous、Albatross、Adventure | 「Mark VIII: **Nelson**, Courageous, Albatross and Adventure classes」 |
| 起源 | **G3 / N3 的防空炮** | 「originally developed as an AAA weapon for the **"G3" and "N3" capital ships of 1920**」 |
| 发射药 | **定装弹（Fixed）** | 「Type — **Fixed**」 |
| 整弹重 | **76 lbs（34.5 kg）** | 「HE: **76 lbs. (34.5 kg)**」 |
| 弹重 | **50 lbs（22.68 kg）** | 「HE: **50 lbs. (22.68 kg)**」 |
| 发射药 | **9.34 lbs MC19 / 10.19 lbs SC103 / 10.94 lbs NF/S 164-048** | 三种并列 |
| **初速** | **2,457 fps（749 mps）** | 「Muzzle Velocity — **2,457 fps (749 mps)**」 |
| 膛压 | **20.5 tons/in²（3,230 kg/cm²）** | 「Working Pressure — **20.5 tons/in2 (3,230 kg/cm2)**」 |
| 射速 | **8–12 发/分** | 「Rate Of Fire — **8 - 12 rounds per minute**」；最快循环约 5 秒，最高记录 15 发/分但送弹机不可靠 |
| 炮管寿命 | **1,050–1,200 发** | 「Approximate Barrel Life — **1,050 - 1,200 rounds**」 |
| **备弹（Nelson 级）** | **175 发/门** | 「Ammunition stowage per gun — **Nelson class: 175 rounds**」 |
| 弹种构成 | **175 发 HE + 150 发照明弹 + 20 发目标烟幕弹/舰** | 「Outfit for Nelson class was **175 HE per gun plus 150 Star Shell and 20 target smoke rounds per ship**.」 |
| 装舰数 | **6 座单装** | 「Nelson (6)」 |
| 炮座型号 | **HA Mark XII** | 「Nelson (6): **HA Mark XII**」 |
| 炮座重 | **27,692 lbs（12,561 kg）** | 「Weight — **27,692 lbs. (12,561 kg)**」 |
| 俯仰 | **−5° / +90°** | 「HA Mark XII: **-5 / +90 degrees**」 |
| 俯仰速率 | **10°/s** | 「HA Mark XII: **10 degrees per second**」 |
| 旋回 | **360°**，速率 **10°/s** | 「Train — **360 degrees**」/「Train Rate — **10 degrees per second**」 |
| 后座行程 | **18 in（46 cm）** | 「Gun recoil — **18 in (46 cm)**」 |
| **功率** | 9 hp 电机 + 液压泵 | 「The HA mountings had a **9 hp electric motor and hydraulic pump** to provide elevation and training. This provided about **twice the speed of manual** training and elevation.」 |
| 防护 | **建成时无炮盾**；1940 年加简易护盾+装甲 `zareba`；1943-05 正式加护盾 | 「Some mountings had **simple shields added** and an armored "**zareba**" was fitted around the 4.7" gun decks on Nelson and Rodney **in 1940**」；wiki Rodney：「In **May 1943** gun shields were added to the 4.7-inch guns」 |
| **Rodney 独有的例外** | **一座炮座用齿条式送弹机，仰角限 77°** | 「**HMS Rodney had one mounting with rack type rammer gear, which limited elevation to 77 degrees.**」 |

**为什么这门炮最终被认为不合格（原句）**：
> 「[the] weapon could not maintain a high rate of fire - a necessity for an AA weapon - as the **heavy round rapidly wore out the gun crews**」

**实战表现（本级两舰都很难看）**：
- **1941-05-27，Rodney 的 6 门 4.7 英寸全程未开火** —— 一手战报：「These guns were **not fired during the action with the BISMARCK**.」（详见 `rodney-tech.md` §4.4）
- 该炮设计给的是防空，实战中连水面目标都没打。

### 6.3 2-pdr（40 mm）Mark VIII 高炮

| 项 | 值 | 原句（navweaps 2-pdr） |
|---|---|---|
| 型号 | **Vickers 2-pdr Mark VIII** | 「Designation — **Vickers 2-pdr Mark VIII**」 |
| 设计年份 | **1923** | 「Date Of Design — **1923**」 |
| 服役 | 八联装 **1930**；四联装 **1936** | 「Octuple Mounting: **1930** / Quad Mounting: **1936**」 |
| 炮重 | **LV 572 lbs（259.5 kg）/ HV 850 lbs（385.6 kg）** | 「LV: **572 lbs. (259.5 kg)** / HV: **850 lbs. (385.6 kg)**」 |
| 口径/身管 | 口径 40 mm；**实际膛线长 39.37 倍径** | 「Actual bore length was **39.37 calibers**.」 |
| 阴膛线 | **12 条**，深 0.0141 in × 宽 0.322 in | 「**(12)** 0.0141 in deep x 0.322」 |
| 药室 | **9.98 in³（0.165 dm³）** | 「Chamber Volume — **9.98 in3 (0.165 dm3)**」 |
| 射速 | **受控射击 96–98 发/分；自动射击 115 发/分** | 「Controlled Firing Gear: **96 to 98 rounds per minute** / Automatic Firing Gear: **115 rounds per minute**」 |

**装舰数与改装时序（navypedia 改装记录，逐条）**：
- **建成时（两舰各 8 门单装）** —— navypedia 初始装备表：「**8 x 1 - 40/39 2pdr QF Mk II**」
- **1932（Rodney）/ 1934（Nelson）**：−8×1，+1×8（八联装）
- **1935（两舰）+2×4 - 12.7 mm**（0.5 英寸四联装机枪，非 pom-pom）
- **1935（Rodney）/ 1937（Nelson）**：+1×8 pom-pom
- **1938-11（Rodney）**：+1×8 pom-pom + **Type 79Y 雷达**
- **1940-08（Nelson）**：+1×8 + 2×4 pom-pom + 4×20 UP 火箭 + Type 281 雷达（满载达 43,300 t）
- **1941-08（Rodney）**：+2×8 + 1×4 pom-pom + Type 271/281/284 雷达（−2×1 20 mm、−Type 279）
- **1942-03（Nelson）**：−4×20 UP、−2 具 622 鱼雷管；+1×8 pom-pom、13×1 20 mm、Type 273/282×5/283×4/284/285
- **1942-05（Rodney）**：−2×4 12.7 mm；+17×1 20 mm、Type 273/282×5/283×4/285
- **1943 秋（Nelson）**：+28×1 20 mm
- **1943–1944（Nelson）**：−2×4 pom-pom；+2×8 pom-pom
- **1945-01（Nelson）**：+4×4 40 mm Bofors + 24×1 20 mm
- **1946-01 两舰最终状态**：见 §7.3

**2-pdr 的技术评价（原句）**：
> 「[by the 1930s] **advances in aircraft design had rendered it obsolescent**, as it had a **low muzzle velocity**」https://www.navweaps.com/Weapons/WNBR_2pdr_mk8.php

### 6.4 12.7 mm（0.5 in）四联装机枪

- **1935 年加装 2 座四联**（两舰）—— navypedia：「**1935, both: + 2 x 4 - 12.7/62**」
- **Rodney 1942-05 拆除** —— navypedia：「5/1942, Rodney: **- 2 x 4 - 12.7/62**」
- **Nelson 1943 秋拆除** —— navypedia：「autumn 1943, Nelson: **- 2 x 4 - 12.762**」（原页 `12.762` 显为 `12.7/62` 之误，照录并标注）
- **详细性能未获取**（本次未抓 0.5 英寸机枪页）

### 6.5 UP 火箭（仅 Nelson）

- **1940-08 加装 4 座 20 管** —— navypedia：「8/1940, Nelson: … + **4 x 20 - 178 UP rockets projectors**, type 281 radar」
- **1942-03 拆除** —— navypedia：「3/1942, Nelson: **- 4 x 20 - 178 UP**」
- **Rodney 从未装过**（navypedia 的 Rodney 改装记录中无 UP 条目）
- 性能数据见 `work/raw/nw-up.txt`（本项目已有）

### 6.6 鱼雷

| 项 | 值 | 原句 |
|---|---|---|
| 数量 | **2 具，每舷 1 具** | navypedia：「**2 - 622 TT (fwd)**」；wiki：「The ships were fitted with **two submerged 24.5-inch (622 mm) torpedo tubes, one on each broadside**」 |
| 口径 | **24.5 in（622 mm）** | 同上 |
| 位置 | **水下，前部** | navypedia `(fwd)` |
| 安装角 | **偏中线 10°** | wiki：「**angled 10° off the centreline**」 |
| 战果 | Rodney 1941-05-27 声称命中 1 雷，是史上唯一一次战列舰雷击战列舰 | wiki 舰级页：「Rodney fired a pair of 24.5-inch torpedoes from her **port-side** tube and claimed one hit. According to Ludovic Kennedy, "if true, [this is] **the only instance in history of one battleship torpedoing another**"」 |
| Nelson 的鱼雷管是否拆除 | **两说不一** | wiki 舰级页：「On 27 September 1941, Nelson's port torpedo station almost proved to be a liability when an Italian air-launched 18-inch torpedo holed the compartment behind the torpedo body room, allowing 3,750 tons of water to enter the ship. **Following this, Nelson's torpedo tubes may have been removed** although **another source suggests the torpedo tubes were retained in both ships into 1945**.」 |

**注意「0 vs 未获取」**：本级的鱼雷管是 **2 具（建成时确定有）**，不是 0；Nelson 后期是否拆是**分歧**，不是「未获取」。

---

## 7. 两舰差异（Nelson vs Rodney）

> 舰级文件最容易被忽略的一节。两舰虽然同级，但**在改装节奏、结构强度、武器细节上差异显著**，直接导致战时表现不同。

### 7.1 建成时的差异

| 项 | Nelson | Rodney | 来源 |
|---|---|---|---|
| 全长 | **216.4 m（709 ft 10 in）** | **216.5 m（710 ft 3 in）** | wiki 舰级页（明确两舰不同） |
| 标准排水量 | **33,313 t**（navypedia）/ 33,300 lt | **33,730 t** | navypedia |
| 燃油 | **3,805 t** | **3,770 t** | navypedia |
| 承造厂 | Armstrong（Elswick / High Walker） | Cammell Laird, Birkenhead | 见 §2.1 |
| 船台号 | 991 | 904 | navypedia |
| 下水 | 1925-09-03 | 1925-12-17 | navypedia |
| 服役 | 1927-08-15 | 1927-12-07 | naval-history / wiki |
| **主机重量** | **超设计指标** | **低于设计指标** | wiki 舰级页：「Unlike Nelson, which **exceeded the design specification for machinery weight**, the lighter machinery of Rodney resulted in **chronic problems**.」 |

### 7.2 结构强度与续航的差异（Rodney 独有缺陷）

- wiki 舰级页：「**The ship's endurance declined substantially in the decade after her launch; in her 1941 action against Bismarck, Rodney was nearly forced to abandon the pursuit because of a lack of fuel.**」
- 「Throughout the war **Rodney was plagued with leaks as a result of panting**, and the ship required repairs because of serious leaks in **1940, 1941 and 1944**. During one storm, the leaking was severe enough to **overwhelm a 50-ton pump**. Leaks, defective riveting, and other problems **continued to affect Rodney even after a 1941 refit in Boston**.」
- 「The **design compromises had less negative consequences for Nelson** because that ship **underwent a number of refits immediately before and during the war**.」
- 「By 1943 officials concluded that **she required a complete modernization** to extend her service life. The ship **never received the necessary upgrades** and as a result was **unfit for service by the end of 1944**.」
- **结论**：**不要把「Rodney 的漏水和续航问题」写成「纳尔逊级的问题」**——来源明确说 Nelson 没这么严重。

### 7.3 战时改装节奏对比（navypedia 逐条）

| 时间 | Nelson | Rodney |
|---|---|---|
| 1932 / 1934 | — | 1932：−8×1 2-pdr，+1×8 |
| 1934 | 同 Rodney 1932 的改动 | — |
| 1935 | +2×4 12.7 mm | +2×4 12.7 mm |
| 1935 / 1937 | 1937：+1×8 2-pdr | 1935：+1×8 2-pdr |
| 1936 | — | **+1 弹射器（X 塔顶）+ 1 水上飞机** |
| 1938-01 | **加装 70 或 76 mm 下层甲板**（305 mm 前舱壁之前） | — |
| 1938-11 | — | +1×8 2-pdr + **Type 79Y 雷达** |
| 1940-08 | +1×8 + 2×4 2-pdr + 4×20 UP + **Type 281**（满载 43,300 t） | **−Type 79Y；+2×1 20 mm + Type 279** |
| 1941-08 | — | **−2×1 20 mm、−Type 279；+2×8 + 1×4 2-pdr + Type 271/281/284** |
| 1942-03 | **−4×20 UP、−2 具 622 鱼雷管**；+1×8 2-pdr、13×1 20 mm、Type 273/282×5/283×4/284/285 | — |
| 1942-05 | — | −2×4 12.7 mm、−Type 271；+17×1 20 mm、Type 273/282×5/283×4/285；排水量 36,000/43,140 t |
| 1942 中 | — | +4×1 20 mm |
| 1942-08 | — | **−1 弹射器与水机；+35×1 20 mm** |
| 1942 末 | — | +5×1 20 mm |
| 1943 秋 | −2×4 12.7 mm；+28×1 20 mm | — |
| 1943–44 | −2×4 2-pdr；+2×8 2-pdr | — |
| 1944 初 | **+Type 650 ECM** | — |
| 1944-06 | — | +2×1 20 mm + **Type 650 ECM** |
| 1944–45 | — | −5×1 20 mm；+5×2 20 mm |
| 1945-01 | **+4×4 40 mm Bofors + 24×1 20 mm**（排水量 37,000/44,054 t） | — |
| 1945-04 | −4×1 20 mm | — |

**1946-01 两舰最终武备（navypedia，几乎完全不同的两套）**：

| 项 | Nelson（1946-01） | Rodney（1946-01） |
|---|---|---|
| 主炮 | 3×3 406/45 Mk I | 3×3 406/45 Mk I |
| 副炮 | 6×2 152/50 **Mk XVIII** | 6×2 152/50 **Mk XVIII** |
| 4.7 英寸 | 6×1 120/40 HA **Mk XII** | 6×1 120/40 HA **Mk XII** |
| 40 mm Bofors | **4×4 40/60 Mk 2** | — |
| 2-pdr | **6×8 40/39 Mk VIA** | **5×8 40/39 Mk VIA + 1×4 40/39 Mk VII** |
| 20 mm | **65×1 20/70 Mk III** | **5×2 20/70 Mk V + 58×1 20/70 Mk III** |
| 鱼雷管 | —（已拆或不计） | **2 - 622 TT (fwd)** |
| 雷达 | Type 273/281/282×5/283×4/284/285 | 同 + Type 650 ECM |
| ECM | Type 650 | Type 650 |

**关键差异三条**：
1. **Bofors 只有 Nelson 有**（4 座四联），Rodney 全程未装 —— 这是真正的 **0**，不是未获取。
2. **20 mm 的构型完全不同**：Nelson 65 门单装；Rodney 5 座双联 + 58 门单装。
3. **鱼雷管**：1946 年 Rodney 仍在册，Nelson 不在 —— 与 §6.6 的分歧互相印证。

### 7.4 战时经历差异（要点）

| 事件 | Nelson | Rodney |
|---|---|---|
| 1939-12-04 | **触磁性水雷，修理 9 个月** | — |
| 1940-04-09 | — | **被 500 kg 炸弹命中**（3 伤 15 电灼伤） |
| 1940-06 | — | 参与挪威撤兵掩护 |
| 1941-03 | — | 参与马塔潘角（未直接交战） |
| **1941-05-27** | — | **打俾斯麦（本舰一生最高光）** |
| 1941-09-27 | **被意机 18 英寸鱼雷命中，进水 3,750 t，修至 1942-04** | — |
| 1941-08 | 参加 Halberd | 参加 Halberd，**误击落一架 Fulmar** |
| 1942-08 | — | **Pedestal，被 Ju 87 攻击，一发穿甲弹被 X 塔顶弹开** |
| 1942-11 | 参加 Torch | 参加 Torch（奥兰，对 Fort du Santon 射 16 发） |
| 1943 | Husky / Baytown | Husky / Baytown / Salerno |
| 1944-06-06 | **诺曼底，诺曼底战役中在 Caen 方向击毁 5 辆虎式坦克（据称）** | **诺曼底，撞沉 LCT 427（13 人全亡）** |
| 1944-06-18 | **触雷受伤退出** | — |
| 1944-09 | — | 护送 JW 60 / RA 60 至摩尔曼斯克 |
| 1948-49 | 作轰炸靶标试验，1949-03-15 拖抵 Inverkeithing 拆解 | **1948-03-26 拖抵 Inverkeithing 拆解** |

来源：navypedia（Nelson 战损）、wiki Rodney（逐条战历）、wiki 舰级页（Caen 虎式坦克、拆解年份）、naval-history 两舰页。

---

## 8. 服役与评价

### 8.1 服役年份

- **1927–1947** —— wiki 舰级页 infobox：「In service **1927–1947**」
- **建成 2 艘，拆解 2 艘** —— wiki 舰级页：「Completed **2** / Scrapped **2**」
- **造价区间** —— wiki 舰级页：「Cost **£7,504,055–7,617,799**」（单舰口径，见 `rodney-tech.md` §1.4 与议会 £6,150,000 的口径差）

### 8.2 同时代人的评价（两个方向都引，不裁）

**批评方**：
- 绰号本身就是批评 —— 「Cherry Tree class, because they had been cut down by Washington」；「the ugly sisters」；「the pair of boots」；「Rodnol / Nelsol」（因单烟囱轮廓像一战船队油轮）
- wiki 舰级页：「Despite the **derisive criticism** directed at this class of battleship by some of the media and some sailors upon their debut…」
- 上层建筑的外号 —— 「The large superstructure, which was **octagonal in plan**, was known to its crew as the "**Octopoidal**" and was sometimes referred to as "**Queen Anne's Mansions**" due to its similarity to a 14-storey brick residential development opposite St James's Park tube station in London.」

**肯定方**（Antony Preston）：
- wiki 舰级页：「naval historian Antony Preston considered that "they were **soundly conceived ships** reflecting all the hard-won experience of World War One" and that "they **proved to be very well-protected and well-designed ships**"」

**舰长本人的评价（Binney，1930，两段都值得引）**：
- 关于主炮：「I hold the opinion that the low-angle gun equipment as a whole, and particularly the **16in main armament, is a very marked advance on any previous capital ship**, and should result in **improved rate of hitting at all ranges**.」
- 关于副炮：「In the case of the secondary armament, although the **rate of fire is rather low**, the **increased range at which fire can be opened**, and the **absence of loss of output due to fatigue**, combined with **excellent ammunition supply arrangements**, will be a very pronounced [improvement]」
- 关于机动性：「In the early stages of the ship's first commission, there was a **general misconception** that the Nelson class were **unhandy and difficult to manoeuvre**. Both my predecessor and myself, however, very soon discovered that **this opinion was entirely fallacious**! In calm weather, the ship's manoeuvring capabilities are **in no way inferior, and in many ways superior to those of Queen Elizabeth or Revenge**.」

**操纵性的客观缺陷（同一页，必须并列）**：
- 「They could also be **awkward to manoeuvre when moving astern**. This was attributed to the ships having a **single, central rudder which was out of the propeller race of the twin screws**.」
- 「the large surface area of the superstructure gave them a **large amount of weather helm** and they could be **a handful in confined spaces with a strong wind** as was demonstrated when **Nelson ran aground off Southsea beach in 1934**.」
- 一个反例（wiki 舰级页）：「Nelson and Rodney were the **only battleships never to have bumped the boom gate vessel** as they passed through Hoxa Sound.」

### 8.3 本级在英舰序列里的位置

- wiki 舰级页：「They were the **only British battleships built between the Revenge class, ordered in 1913, and the King George V class, ordered in 1936**.」
- **唯一装 9 门 16 英寸的英国战列舰** —— 「The Nelsons were **unique in British battleship construction**, being the **only ships to carry a main armament of nine 16-inch (406 mm) guns**.」
- **唯一的三联装 16 英寸装舰** —— navweaps：「the **only ones to see service mounted in triple turrets**」
- 前型/后型：前接 Revenge 级（1913 订购），后接 King George V 级（1936 订购）。**两级之间隔了 23 年、只造了 2 艘**——这是华盛顿条约十年「海军假日」的直接结果。

---

## 9. 未获取字段汇总

> 任务书要求「纳尔逊级的舰体数据可能大面积缺失，如实说」。**确认：大面积缺失，且缺失集中在「舰体结构」与「重量分配」两类。**

### 9.1 完全未获取（试过的来源都没有）

| 字段 | 试过的来源 | 说明 |
|---|---|---|
| **装甲总重（吨）** | navypedia、wiki 舰级页、wiki 两舰单页、naval-history 两舰页 | **本级最大空洞。** 对照 KGV 有 RMG 的 12,413 t / 32.5%，本级一个数都没有 |
| **装甲占排水量比（%）** | 同上 | 同上 |
| **重量分配表**（船体/舾装/动力/武备/装甲各多少吨） | 同上 | 只有 KGV 有 RMG 的 Weights 表，本级没有对应来源 |
| **型深（depth molded）** | 同上 | — |
| **方形系数 Cb** | 同上 | — |
| **水线面积** | 同上 | — |
| **干舷（数值）** | 同上 | 只有定性的「上层建筑像后桅帆」 |
| **蒸汽温度** | 同上 | 只有 250 psi 压力 |
| **主发电机台数与总功率** | 同上 | 对照俾斯麦有 7,910 kW 的完整分解 |
| **螺旋桨直径** | 同上 | 只有「quite large screws」的定性描述 |
| **舵面积 / 舵角 / 回转直径** | 同上 | 只有「comparatively small tactical diameter」的定性评语 |
| **舱段划分**（几个锅炉舱、如何与机舱交替） | 同上 | 只有「锅炉舱在机舱之后」一句 |
| **单舰造价（口径统一）** | 议会 1939、wiki | £6.15M（不含首备）vs £7.50–7.62M（wiki），**无第三方调和** |
| **烟道装甲的 wiki 口径** | — | navypedia 给 229–203 mm，wiki 未给 |
| **舱室/住舱条件** | 同上 | 无来源描述 |
| **0.5 英寸机枪详细性能** | 本次未抓对应页 | 只有数量与拆装时序 |
| **UP 火箭详细性能** | （项目内已有 `nw-up.txt`，本次未核） | — |

### 9.2 部分获取（有数但有口径问题）

| 字段 | 状态 |
|---|---|
| 防雷深度 | 3.7 m（wiki 总深度）vs 3.1 m（navypedia 下限）——**同一区间两种表述，见 §4.5** |
| 副炮塔正面装甲 | 38 mm（navypedia）vs 全向 25 mm（wiki）vs 1 in HT（navweaps）——**三说，见 §4.4** |
| 炮塔正面 | 15.68 in / 16 in / 406 mm / 410 mm——**板重口径 vs 名义厚度，见 §4.3** |
| 吃水 | 9.2 m（wiki，标准）vs 8.56 m（navypedia，mean）——**状态未对齐** |
| 续航 | 7,000 nm @16 kn vs 14,500 nm @10 kn——**档位不同** |
| 全长 | 216.4 m（navypedia 单值）vs 216.4/216.5（wiki 分舰给值）——**navypedia 未区分两舰** |
| 主机承造厂 | **未获取**（对照 KGV 有 tynebuiltships 给出） |

### 9.3 明确「不是未获取」的项（区分「未获取」与「0」）

| 字段 | 值 | 依据 |
|---|---|---|
| **40 mm Bofors（Rodney）** | **0，全程未装** | navypedia 与 wiki 的 Rodney 改装记录中从无 Bofors；对照 Nelson 1945-01 有「+4 x 4 - 40/56 Bofors」。**这是真正的 0** |
| **UP 火箭（Rodney）** | **0，从未装** | navypedia Rodney 改装记录无 UP 条目；Nelson 1940-08 装了 4 座 |
| **弹射器（建成时，两舰）** | **0** | navypedia：「**1936, Rodney: + 1 catapult on turret "X"**」——1936 年才加，建成时无。Nelson 加装时间**未获取**（navypedia 只在 Rodney 条目下记） |
| **弹射器（Rodney，1942-08 之后）** | **0，已拆** | 「8/1942, Rodney: **- 1 catapult with seaplane**」 |
| **三联装炮塔的闪光隔板** | **0，确实没有** | navweaps：「the turrets **still lacked flash shields between the guns**」；照片说明亦记「Note that the guns are **not separated by flash walls**」 |
| **鱼雷管（建成时，两舰）** | **2 具（每舷 1）** | 见 §6.6。**不是 0** |
| **深水炸弹** | **0（无记录）** | 各来源装备表均无 |

---

## 10. 来源清单

| 缩写 | 来源 id | 等级 | URL | 用途 |
|---|---|---|---|---|
| `[TREATY]` | `washington-treaty-1922` | **A 一手档案**（条约原文） | https://www.ibiblio.org/pha/pre-war/1922/nav_lim.html | 35,000 t / 16 in 上限、英国可造两艘、标准排水量定义 |
| `[NW16]` | `navweaps-16in-45-mk1` | D（内含 Campbell / Raven & Roberts / Burt / Garzke & Dulin 转引） | https://www.navweaps.com/Weapons/WNBR_16-45_mk1.php | 主炮全部数据、炮塔数据、射速机理、炮塔装甲、Binney 报告、滚轮缺陷、全前置代价 |
| `[NW6]` | `navweaps-6in-50-mk22` | D（**本次新建**） | https://www.navweaps.com/Weapons/WNBR_6in-50_mk22.php | 副炮全部数据、副炮布置弱点、Rodney 实战射速 |
| `[NW47]` | `navweaps-47-40-mk8` | D（**本次新建**） | https://www.navweaps.com/Weapons/WNBR_47-40_mk8.php | 4.7 英寸高炮全部数据、Rodney 独特炮座例外 |
| `[NW2P]` | `navweaps-2pdr-mk8` | D | https://www.navweaps.com/Weapons/WNBR_2pdr_mk8.php | 2-pdr 炮身数据与「已过时」评语 |
| `[NP]` | `navypedia-nelson` | D | https://www.navypedia.org/ships/uk/brit_bb1_nelson.htm | 两舰建造表、排水/尺寸/动力/装甲汇总、**逐次改装记录（本级最完整的改装时序）**、Nelson 战损 |
| `[NH-R]` | `naval-history-rodney` | C（官方舰史体例） | https://www.naval-history.net/xGM-Chrono-01BB-HMS_Rodney.htm | Rodney 建造与结局 |
| `[NH-N]` | `naval-history-nelson` | C | https://www.naval-history.net/xGM-Chrono-01BB-HMS_Nelson.htm | Nelson 建造与结局（含 1948 轰炸靶标试验、1949-03-15 拖抵 Inverkeithing） |
| `[WKC]` | `wiki-en-nelson-class` | **E 百科（仅线索）** | https://en.wikipedia.org/wiki/Nelson-class_battleship | 设计动机、省重量手段、装甲方案、GM、横摇、操纵性、评价——**关键值已尽量回查 D/C 源，但本级舰体数据只能靠它，属唯一的「全」来源，可靠性打折** |
| `[WKR]` | `wiki-en-rodney` | **E 百科（仅线索）** | https://en.wikipedia.org/wiki/HMS_Rodney_(29) | Rodney 单舰差异、战历、改装 |
| `[ROD]` | `kbismarck-rodney-report` | **A 一手档案** | https://www.kbismarck.com/rodney-gunnery-report.html | 炮塔/副炮命名与布置的原文、4.7 英寸未开火 |

**本次新增抓取并落盘的原始件**（供复核）：
- `work/raw/nw-6in50-mk22.html` / `.txt`
- `work/raw/nw-47-40-mk8.html` / `.txt`
- `work/raw/navypedia-nelson.html` / `.txt`
- `work/raw/nh-nelson.html` / `.txt`
- `work/raw/wiki-nelson-class.html` / `.txt`
- `work/raw/washington-treaty-1922.html` / `.txt`

**抓取失败 / 未取到**：
- `https://www.navweaps.com/Weapons/WNBR_2pdr_mk8_octuple.php` → **404**（八联装 pom-pom 页路径不同，本次未取得；装舰数量改用 navypedia 改装记录）
- `https://www.navypedia.org/ships/uk/brit_bb_nelson.htm` → **404**（正确路径 `brit_bb1_nelson.htm`）
- **RFC / RMG 的纳尔逊级研究指南** —— 未检索到（对照 KGV 有 RMG B9 页，给出 Armour 12,413 t / 32.5% 这类关键重量数据；**本级很可能也有对应的 RMG 页，若找到可补上 §9.1 的大面积缺失**）。这是本文件最值得再试一次的方向。

---

## 11. 给主会话的落库建议（不含 data/ 改动）

> 任务书要求不改 `data/`，故本节只是建议，不是已执行。

**舰级 fact 建议优先写这些**（都有原句、都属两舰共有）：

1. `identity.ship_type = battleship`、`identity.operator`、`identity.nation = uk`、`identity.era = ww2`
2. `dimensions.length.pp = 201.2 m`（两源一致，最硬）
3. `dimensions.beam.wl = 32.3 m`（两源一致）
4. `dimensions.draught.mean` —— **必须带 note**：9.2 m（wiki，标准状态）/ 8.56 m（navypedia，mean 未注状态），**并列两条**
5. `displacement.standard` —— Nelson 33,313 / Rodney 33,730，**分两条**，因为舰级层不能二选一
6. `propulsion.boiler.count = 8`、`propulsion.boiler.type = Admiralty 3-drum with superheaters`、`propulsion.boiler.pressure = 250 psi`
7. `propulsion.power.design = 45000 shp`、`propulsion.speed.design = 23 kn`、`propulsion.shafts = 2`
8. `protection.scheme` —— 建议填 **`all_or_nothing`**，但 note 必须写「来源原词：for the first time in British practice」并引 navypedia 原句
9. `protection.armor.thickness` 按部位分 6 条（belt 356/330、deck 159/95、turret face、barbette、CT、bulkhead），**每条带 qual**
10. `protection.underwater.depth` —— **必须并列 3.7 / 3.1 两条**并写口径
11. `armament.broadside_weight` —— **注意**：9 × 929 kg = **8,361 kg**，但这是**本报告算的**，来源没给。按 `kgv-tech.md` 的做法（「来源给才算」），**建议不填或标 confidence B + note 注明为派生值**
12. `armament.torpedo.count = 2`，`armament.torpedo.bore = 622 mm`
13. `protection.armor.weight` —— **绝对不要填**，本级没有来源

**武器实体建议**（`about: weapon:*`）：
- `weapon:16in-45-mk1` —— **数据最全的一个，可写 25+ 条**（弹重、初速、膛压、药室、射速、寿命、膛线、炮重、制造数、穿深表、射程表）
- `weapon:6in-50-mk22` —— 可写 15+ 条
- `weapon:47in-40-mk8` —— 可写 12 条
- `weapon:2pdr-mk8` —— 可写 8 条（但项目里可能已有该实体，先查 `getWeaponIndex()`）

**炮位实体建议**（`about: mount:*`）：
- `mount:a` / `mount:b` / `mount:x`（主炮三联，**注意 X 塔射界只有每侧 60–130°，这是本级的定义性缺陷，必须写进 `mount.traverse`**）
- `mount:6in-twin-mk18`（6 座，P1–P3 / S1–S3）
- `mount:47in-ha-mk12`（6 座）
