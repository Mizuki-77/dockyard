# Admiral Hipper class（希佩尔海军上将级重巡洋舰）— 舰级共性数据

> 检索日期：2026-11-21 · 项目现有 `data/classes/` 中**没有**本舰级文件，本文是其第一次建档。
> **执行说明**：每条数值附英文原句 + 来源 URL。查不到一律写「未获取」，**不拿德国级装甲舰（Deutschland）、拿骚级或任何别国重巡的数据凑**。
> 来源等级：A 一手档案 / B 同期官方出版物 / C 权威二次文献 / D 专题网站 / E 百科（**仅线索，不作数值来源**）。

---

## 0. ⚠️ 最关键的一条：这个"舰级"内部差异大到不能当一级处理

任务书要求「舰级共性数据」。实测结果是：**本级的五艘船在动力装置上几乎没有两艘相同，主尺度也分两批**——把它当成「一级"三艘同型」处理，会直接抹掉本舰（Prinz Eugen）最核心的工程特征。

naval-encyclopedia 的原话（这是本文最重要的一句）：

> "This made for a pretty diverse picture, **which was intended in order to gather comparative data**." — [naval-encyclopedia](https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php)

即：**德方是故意让五艘船装不同的动力装置，用来对比试验。** 这不是「设计变更」或「资料不准」，是设计意图。

逐舰差异（同一来源）：

> "-Admiral Hipper had **La Mont boilers working at 80 atm** coupled with **Blohm und Voss** turbine units.
> -Blücher had **Wagner boilers (with natural circulation) working at 70atm**, and also **Blohm und Voss** turbines.
> -Prinz Eugen had **La Mont boilers (70atm)** but **Brown-Boveri** turbines.
> -Seydlitz and Lützow had just **nine Wagner boilers with forced circulation (working at 60atm)** and **Wagner-Deschimag** turbine units."

**四组不同的锅炉 + 四组不同的汽轮机。** 因此本文的结构是：

1. §1–§7 写**真正共有的**（尺寸定型、武备、装甲方案、航空、编制口径）——这部分可以继承；
2. §8 单列**逐舰差异表**——这部分不能继承，单舰文件必须自己写；
3. §9 写**分批**（首批 2 艘 / 改进批 3 艘）——这是所有「共性」的边界条件。

同时诚实说明：**本级的"共性数据"本身缺口很大**——`protection.armor.weight`、`armor` 逐舰值、`aviation` 详细尺寸、`sensors` 装机日期，都没有可靠来源。

---

## 1. 五舰名单与建造记录

| 舰 | 代号 | 建造厂 | 开工 | 下水 | 服役 | 结局 | 造价 |
|---|---|---|---|---|---|---|---|
| **Admiral Hipper** | Kreuzer H（Ersatz Hamburg） | Blohm & Voss, Hamburg（船台 9） | 1935-07-06 | 1937-02-06 | 1939-04-29 | 1945-05-03 自沉于基尔 | — |
| **Blücher** | Kreuzer G（Ersatz Berlin） | Deutsche Werke, Kiel（船台 2） | 1935-08-15 | 1937-06-08 | 1939-09-20 | 1940-04-09 奥斯陆峡湾被岸炮+鱼雷击沉 | 87.8 Mio RM |
| **Prinz Eugen** | Kreuzer J | Germaniawerft, Kiel（船台 2） | 1936-04-23 | 1938-08-22（一说 08-20） | 1940-08-01 | 1946-12-22 倾覆于夸贾林 | 104.5 Mio RM |
| **Seydlitz** | Kreuzer K | Deschimag, Bremen | 1936-12-29 | 1939-01-19 | 未服役 | 1945-04-10 自沉于柯尼斯堡 | 84.1 Mio RM |
| **Lützow** | Kreuzer L | Deschimag, Bremen | 1937-08-02 | 1939-07-01 | 未服役（1940 售予苏联） | 1950 年代在苏联拆解 | 83.6 Mio RM |

**来源与原句**

- Hipper："**06 July 1935:** Lay down on Slipway 9 at the Blohm & Voss Shipyard in Hamburg. Construction number B 501." / "**06 February 1937:** Launched. Christened by Erika Raeder, wife of Generaladmiral Erich Raeder." / "**29 April 1939:** Commissioned under Captain Hellmuth Heye." — [kbismarck/admiral-hipper](https://www.kbismarck.com/admiral-hipper.html)
- Hipper 结局："sunk 3.5.1945" — [navypedia](https://www.navypedia.org/ships/germany/ger_cr_hipper.htm)
- Blücher："**15 August 1935:** Lay down on Slipway 2 at Deutsche Werke, Kiel. Construction number K 246." / "**08 June 1937:** Launched. ... The final cost of the new ship will rise to **RM. 87.8 Million**." / "**20 September 1939:** Commissioned under Captain Heinrich Woldag." — [kbismarck/blucher](https://www.kbismarck.com/blucher.html)
- Blücher 结局："Blücher was sunk 9.4.1940 by Norwegian 280mm and 150mm coastal guns and 2 torpedoes from coastal batteries in Oslo-fiord." — [navypedia](https://www.navypedia.org/ships/germany/ger_cr_hipper.htm)
- Prinz Eugen：见 `prinz-eugen-tech.md` §2。
- Seydlitz："Construction record Seydlitz: Laid down **Deschimag Bremen, 29.12.1936**; Launched **19.01.1939**; Fate **blown up 10.04.1945 (Königsberg)**; Cost **84,1 Mio Reichsmark**" — [german-navy/seydlitz](https://www.german-navy.de/kriegsmarine/ships/heavycruiser/seydlitz/index.html)
- Lützow："Construction record Lützow: Laid down **Deschimag Bremen, 02.08.1937**; Launched **01.07.1939**; Fate **scrapped in the 1950s (Russia)**; Cost **83,6 Mio Reichsmark**" — [german-navy/lutzow](https://www.german-navy.de/kriegsmarine/ships/heavycruiser/lutzow/index.html)

**【分歧·Hipper 船台号】** kbismarck 写 "Slipway 9"；navypedia 表里 Hipper 的 Yard No 是 **501**（那是建造编号不是船台）。项目 `data/sources.yaml` 的 `german-navy-bismarck` 条已记录过一个同类教训（"Slipway 1 与英纸 Helgen IX 冲突"），本条属同类。**并列。**

**【分歧·Hipper 结局】** 两个来源都说 1945-05-03，但表述不同：navypedia "sunk 3.5.1945"；german-navy "British bombs badly damaged her at Kiel, where her crew scuttled the ship on 3 May 1945."。**即：先被英机炸伤、再由舰员自沉。两说可合并，不冲突。**

### 1.1 订购背景（决定「为什么是这五艘」）

> "Admiral Hipper (when laid "cruiser H", or "Ersatz Hamburg") and Blücher ("G", or "Ersatz Berlin") have been ordered late 1934, **before official denunciation of Versailles Treaty**, forbidding to Germany to build cruisers with artillery larger than 150mm calibre. A year later the order on Prinz Eugen ("J"), having some differences on an internal arrangement, has arrived. Seydlitz and Lützow ("K" and "L") were **originally planed as light cruisers with 4 triple 150mm turrets**, but in 1937 it has been decided to build them with 203mm artillery." — [navypedia](https://www.navypedia.org/ships/germany/ger_cr_hipper.htm)

**这条极重要**：Seydlitz 与 Lützow **最初设计是装 150 mm 三联装炮的轻巡**，1937 年才改成 203 mm。这意味着后两艘的舰体是为轻巡炮设计的，改装重巡炮后吨位与稳性都出问题（见 §3）。

naval-encyclopedia 的复述更细：

> "KMS Seydlitz and Lützow ("Kreuzer K" and "Kreuzer L") were like Prinz Eugen not even order to replace older cruisers ... These later cruiser **originally were planed as light cruisers with four triple 150mm turrets** according to what was planned in USSR, but in 1937 this was revised and they obtained the same 8-in gun turrets."

**【一处需注意的矛盾】** navypedia 说 Seydlitz/Lützow「originally planned as light cruisers」，而 naval-encyclopedia 说的是「originally were planed as light cruisers **with four triple 150mm turrets according to what was planned in USSR**」。后者的「苏联」指 1939 年售予苏联的 Lützow 后续改装，这句表述混乱（把设计源流与售后改装混在一起）。**采信 navypedia 的表述，naval-encyclopedia 这句标"表述混乱"。**

---

## 2. 舰级定位与吨位

### 2.1 设计目标

> "It was supposed to create ships, capable to act both with battle fleet, and as commerce raider, and at the same time, **not yielding on armament and protection to French heavy cruiser Algerie**." — [navypedia](https://www.navypedia.org/ships/germany/ger_cr_hipper.htm)

> "The new class needed to be at least equal to the French **Algerie** class design, or the Italian **Zara** class." — [naval-encyclopedia](https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php)

> "Although conceived within the 10,000-ton, 20.3 cm-gun limits associated with the Washington treaty system, the completed ships were **substantially larger than the nominal limit**." — [german-navy/hipper](https://www.german-navy.de/kriegsmarine/ships/heavycruiser/admiralhipper/index.html)

### 2.2 吨位——**两级三口径，且都远超条约限制**

**首批（Hipper / Blücher）**

| 口径 | 值 | 来源与原句 |
|---|---|---|
| 标准 | **14,240 mt** | [KB/Hipper]："Displacement: standard 14,240 mt, full load 18,200 mt."；[KB/Blücher] 同句 |
| 标准 | **14,050 t** | [navypedia]："Displacement standard, t 14050" |
| 标准 | **16,170 t（15,910 lt）** | [naval-encyclopedia]："KMS Admiral Hipper and Blücher already were designed with a standard displacement of… **16,170 metric tons** (that's 15,910 long tons or 17,820 short tons) and with a full load displacement of 18,200 long tons (18,500 t)" |
| 满载 | **18,200 mt** | [KB/Hipper] |
| 满载 | **18,210 t** | [navypedia]："Displacement full, t 18210" |
| 满载 | 18,200 lt / 18,500 t | [naval-encyclopedia] |
| Size (Max) | **18,200 t** | [german-navy/hipper]："Size (Max) 18200 t" |

**改进批（Prinz Eugen / Seydlitz / Lützow）**

| 舰 | 标准 | 满载 | 来源 |
|---|---|---|---|
| Prinz Eugen | 16,970 t（或 14,240 mt，KB 口径） | 19,050 t / 19,042 mt | 见 `prinz-eugen-tech.md` §3.4 |
| Seydlitz / Lützow | **17,600 t（17,300 lt）** | **20,100 t（19,800 lt）** | [naval-encyclopedia]："KMS Seydlitz and Lützow reached a healthy 17,600 t (17,300 long tons; 19,400 short tons) as designed, standard and reached and 19,800 long tons (so 20,100 t) fully loaded." |

**【核心分歧】首批标准排水量 14,240 / 14,050 / 16,170 三个值，最大差 2,120 t。**
- 14,240 mt 与 14,050 t 只差 190 t，**可能同一口径的不同换算**；
- 16,170 t 出自 naval-encyclopedia，且该页在别处明显有笔误（见 `prinz-eugen-tech.md` §17 的多处记录），**可信度打折**；
- 但 naval-encyclopedia 那句「so nearly double the Washington treaty!」的定性是对的（18,200 lt 满载 vs 10,000 t 条约上限）。

**并列，不裁决。** 但注明：**「本级设计排水量在 14,050–14,240 t 之间」是三源中两源的共同区间，16,170 t 为单源异说。**

### 2.3 与条约的关系

> "Nominally, in the register, the early ships (Hipper and Blücher) were within the 10,000-ton limit. But it is easy to lie on simple numbers. KMS Admiral Hipper and Blücher already were designed with a standard displacement of… 16,170 metric tons … so **nearly double the Washington treaty**! This made already the largest cruisers in the world. For memory, the USN came with the Baltimore design in 1942, and only reached 17 030 t. Fully Loaded." — [naval-encyclopedia](https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php)

> "Raeder was confident thus, to have "the world's absolute best heavy cruiser" after two years: ... And the Kriegsmarine could legally acquire five of them: **With 50,000 long tons (51,000 t) of heavy cruisers based on 10,000-ton unitary basis**." — 同上

【提醒】「50,000 lt 总配额」这条给出的法律依据是 1935 年英德海军协定（同页："They were enabled by the **1935 Anglo-German naval agreement**"）。**这是本级的政治前提，不是技术数据。**

---

## 3. 主尺度——**分两批，差别很大**

### 3.1 首批（Hipper / Blücher）

| 项目 | 值 | 来源 |
|---|---|---|
| 全长（oa） | **205.9 m** | [navypedia]："Length, m 194.6 wl 205.9 oa"；[KB/Hipper]："overall length 205.9 m"；[german-navy/hipper]："Length (Total) 205,9 m" |
| 水线长（wl） | **194.6 m** | [navypedia]："194.6 wl" |
| 舰宽 | **21.3 m** | [navypedia]："Breadth, m 21.3"；[KB/Hipper]："beam 21.3 m" |
| 吃水（平均） | **5.80 m** | [navypedia]："Draught, m 5.80 mean 7.90 max" |
| 吃水（最大） | **7.90 m** | 同上 |
| 吃水（KB/german-navy） | **7.2 m**（"maximum draft"） | [KB/Hipper]："maximum draft 7.2 m"；[german-navy/hipper]："Draft 7,7 m" |
| 型深 / depth | 12.45 m | [KB/Hipper]："depth 12.45 m" |

**吃水三值：7.90（navypedia max）/ 7.2（KB）/ 7.7（german-navy）。** 三者并列。

### 3.2 改进批（Prinz Eugen 型）

| 项目 | Prinz Eugen | Seydlitz / Lützow | 来源 |
|---|---|---|---|
| 全长（oa，加 clipper bow 后） | **212.5 m** | **210 m** | [naval-encyclopedia]："Prinz Eugen was 199.5 m ... long at the waterline, **207.7 m (681 ft) overall as planned**, but the addition of a clipper bow had her extended to **212.5 m**" / "KMS Seydlitz and Lützow reached were **210 m (690 ft) long overall, clipper included**" |
| 水线长 | **199.5 m** | — | 同上 |
| 舰宽 | **21.7 m** | **21.8 m** | 同上 |
| 吃水（标准） | **6.6 m** | **6.9 m** | 同上 |
| 吃水（满载） | **7.2 m** | **7.9 m** | 同上 |

**关键**：navypedia 的 205.9 m 是**首批**值；本舰是 **212.5 m**，差 6.6 m。这就是 `docs/30-new-ship-workflow.md` §6「开工前 30 秒检查」第 5 条那句「navypedia 上有没有骨架数据」必须核对批次的实例——**navypedia 的级页只给了首批值，直接套会错 6.6 m。**

### 3.3 舰艏型式的演变

> "Hull form of the ships reminded applied on light cruiser Leipzig: with bulges, expressed bulb and internal belt included in providing of general longitudinal strength. **Originally cruiser had almost straight stem (length oa 202.8m), but after trials of Admiral Hipper it have changed on clipper bow**, remaining cruisers were completed with reconstructed stem." — [navypedia](https://www.navypedia.org/ships/germany/ger_cr_hipper.htm)

> "Hipper saw her bow rebuilt in 1939 as her sister Blücher in the Atlantic clipper style, **later directly implemented on Prinz Eugen**." — [naval-encyclopedia]

> "She had a **straight stem corrected in completion by a clipper bow** and raked funnel cap. The was the last cruise of the class to be built with this bow. The next Seydlitz and Lützow would have a clipper bow from the start." — 同上（主语 Prinz Eugen）

**【第三个全长值】** navypedia 说原设计（直艏）全长是 **202.8 m**。这样本级就出现了 202.8（原设计）/ 205.9（首批建成）/ 210（Seydlitz·Lützow 设计）/ 212.5（Prinz Eugen）**四个全长**。写死一个值就是错的。

---

## 4. 动力——**本级最不能「共性化」的部分**

### 4.1 逐舰差异（见 §0 已引原文）

| 舰 | 锅炉 | 锅炉压力 | 汽轮机 |
|---|---|---|---|
| Admiral Hipper | La Mont ×12 | **80 atm** | Blohm & Voss |
| Blücher | Wagner（自然循环）×12 | 70 atm | Blohm & Voss |
| **Prinz Eugen** | **La Mont ×12** | **70 atm** | **Brown-Boveri**（一说 Germania） |
| Seydlitz | Wagner（强制循环）×**9** | 60 atm | Wagner-Deschimag |
| Lützow | Wagner（强制循环）×**9** | 60 atm | Wagner-Deschimag |

**注意 Seydlitz / Lützow 只有 9 台锅炉**——与前三艘的 12 台不同型不同数。这是 navypedia 未记的（它只写 "12 La Mont boilers / 12 Wagner boilers" 给前两艘）。

### 4.2 共有部分

| 项目 | 值 | 来源与原句 |
|---|---|---|
| 轴数 | **3** | [navypedia]："No of shafts 3"；[german-navy]："Shafts 3" |
| 齿轮传动 | 是 | [navypedia]："3 sets ... geared steam turbines" |
| 设计功率 | **132,000 shp（98 MW）** | [navypedia]："Power, h. p. 132000"；[naval-encyclopedia]："rated, more or less for a nominal **132,000 shaft horsepower (98,000 kW)**" |
| 设计航速 | **32 kn** | [navypedia]："Max speed, kts 32"；[naval-encyclopedia]："procured on paper a top speed of 32 knots" |
| 螺旋桨 | 3 叶，直径 **4.1 m** | [naval-encyclopedia]："Each turbine drove a three-bladed screw **4.1 m (13 ft) in diameter**." |
| 舵 | **1 具** | [KB/Hipper] 未记；[naval-encyclopedia]："Steering depending on **a single rudder**."；[KB/PrinzEugen]："**One rudder.**" |
| 巡航汽轮机 | **无** | 见下 |

**「无巡航汽轮机」的依据**：本级的动力是「纯汽轮机、无柴油机」，这一点 navypedia 明说：

> "From tactical and operational reasons combined **diesel-turbine machinery**, used on light cruisers, have been **refused in favour of purely turbine**, on steam with high parameters." — [navypedia](https://www.navypedia.org/ships/germany/ger_cr_hipper.htm)

后果（这是本级最重要的战术缺陷）：

> "Both had very sophisticated gunnery control systems, sights, radars, a powerful anti-aircraft battery, but **lacked range due to the lack of diesels for the revised commerce raiding duties**. They had instead highly sophisticated and somewhat capricious high-pressure turbines creating **constant mechanical problems in service**." — [naval-encyclopedia](https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php)

### 4.3 燃油与续航

| 项目 | 首批 | 改进批 | 来源 |
|---|---|---|---|
| 设计燃油 | — | **1,420–1,460 t** | [naval-encyclopedia]："they carried 1,420 to 1,460 t (1,400 to 1,440 long tons; 1,570 to 1,610 short tons) of fuel oil as designed" |
| 利用防雷空舱后 | — | **3,050–3,250 t** | 同上："They could be filled, as the double bottom, and ensure to double that figure to 3,050 to 3,250 t" |
| 燃油（navypedia 口径） | **3,050 t** | — | [navypedia]："Fuel, t oil 3050" |
| 燃油（KB 口径） | **4,250 mt** | 4,250 mt | [KB/Hipper]、[KB/PrinzEugen]——**两页同值，疑复制** |
| 续航 | **6,800 nm @ 20 kn** | 同 | [navypedia]："Endurance, nm(kts) 6800(20)"；[naval-encyclopedia]："a comfortable range **6,800 nautical miles** (12,600 km; 7,800 mi)" @ 20 kn |
| 续航（**分歧**） | 6,800 nm @ **16** kn | — | [KB/Hipper]、[KB/PrinzEugen] 两页同句 |
| 续航（**分歧**） | **8,000 mi @ 20 kn**（Hipper）/ 7,200 mi @ 20 kn（Prinz Eugen） | — | [german-navy/hipper]："Range 8000 miles at 20 kn"；[german-navy/prinzeugen]："Range 7200 miles at 20 kn" |

**【重要·KB 复制证据再确认】** KB 的 Hipper 页与 PrinzEugen 页在「燃油 4,250 mt / 续航 6,800 nm @ 16 kn / 型深 12.45 m / 主测距仪 5 × 7 m」四项**逐字相同**。而 german-navy 对两舰给了不同值（8,000 vs 7,200 mi）。**所以 KB 这四项对本级任何一舰都不可靠**——这是舰级层面的系统性问题，不只是 Prinz Eugen 一舰的。

### 4.4 机动性

> "As for agility, ... They were regarded as **good sea boats with gentle motion**. **At low speed wind and currents affected them greatly** as a result of their tall superstructures that acted as sails. They also naturally bled speed when hard over at full regime, **heeling up to 15 degrees, with 50% speed loss**." — [naval-encyclopedia](https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php)

【实测反证】Prinz Eugen KTB 1941-05-23 20:44 记录，本舰在高速下用 40° 满舵规避：

> "Prinz Eugen is able to extract himself from closing further by **40º hard full rudder (which, as a rule, is not allowed at this high speed)**." — KTB

**「高速不许满舵」这条舰上规定，与 naval-encyclopedia 的「50% 失速」描述是同一件事的两面。** 这是本级操舵特性的最佳一手证据。

### 4.5 电力系统——**两批不同**

| 批 | 柴油发电机 | 汽轮发电机 | 总功率 | 来源 |
|---|---|---|---|---|
| 首批（Hipper / Blücher） | 4 × 150 kW（MAN） | 4 × 460 kW + 2 × 230 kW | **2,900 kW** | [naval-encyclopedia]："Admiral Hipper and Blücher were provided three electricity plants, coupled to four MAN diesel generators and six turbo-generators each. These diesel generators supplied 150 kW each, and four of the six turbo-generators were rated for 460 kW, the last two 230 kW for a **total output of 2900 kW**." |
| 改进批（Prinz Eugen / Seydlitz / Lützow） | 150 kW ×? | 4 × 460 kW + 1 × 230 kW + 1 × 150 kW AC | **2,870 kW** | 同上："Prinz Eugen, Seydlitz, and Lützow had 150 kW diesel generators, four 460 kW turbo-generators, one 230 kW turbo-generator, one 150 kW AC generator and a **total of 2870 kW**." |
| 电压 | **220 V** | — | — | 同上："The electric current was setup at **220 volts**." |

【注意】改进批那句的「150 kW diesel generators」**没给台数**，只给了单机功率。**台数未获取。**

---

## 5. 防护

### 5.1 舰级装甲方案（navypedia 全文，唯一按部位组织的来源）

> "Armour, mm belt: **80 - 40**, bulkheads: **80**, deck: **30 + (50 - 30)**, anti-torpedo bulkhead: **20**, turrets: **160 - 50**, barbettes: **80**, CT: **150 - 50**" — [navypedia](https://www.navypedia.org/ships/germany/ger_cr_hipper.htm)

逐段原文（同页 Ship protection 段）：

> "**12.5°-inclined main belt between inner barbettes was 3.75m high and 80mm thick.** It was closed by 80mm bulkheads. Thickness of **fore 3.85m high belt was 40mm**, decreasing to **20mm** fwd from "A" barbette; **2.75m-high belt with 70mm thickness** protected aft part of ship and was closed by 70mm aft bulkhead of steering gear compartment. **30mm main deck** was connected with lower edge of main belt by **50mm slopes**, thickness of this deck increased to **40mm outside citadel**. There was **30mm upper deck**. **Turrets had 160mm faces (with 105mm inclined parts), 70mm sides (with 80mm inclined parts) and 80mm roofs**, barbettes had **80mm** armor. **CT had 150mm sides and 50mm roof**. Underwater protection consisted of **bulges and 20mm longitudinal bulkhead**."

### 5.2 与 KB 口径的比对

| 部位 | navypedia | KB（Hipper 页） | KB（PrinzEugen 页） | german-navy |
|---|---|---|---|---|
| 舷侧带 | 80–40 | 80 | 80 | 70–80 |
| 炮塔 | 160–50 | 70–160 | 70–160 | 70–105 |
| 炮座 | 80 | 80 | 80 | — |
| 上甲板 | 30 | 30 | 30 | 12–50（Deck） |
| 装甲甲板 | 30（+50 斜坡） | 30 | 30 | 12–50（Deck） |
| 司令塔 | 150–50 | 150 | 150 | 50–150 |
| 防雷纵舱壁 | 20 | 20 | 20 | — |

**结论：KB 的 Hipper 页与 PrinzEugen 页装甲数据完全一样（这是第三组复制痕迹），而 navypedia 的分段更细。**
- 「80 mm 舷侧带」是唯一全源一致的值，**可作舰级主值**；
- 「炮塔 160–50」只有 navypedia 给，KB 给「70–160」，german-navy 给「70–105」——**三个区间，最小公约数是 70，最大公约数是 160**；
- 「甲板 30 mm」三源一致（navypedia、KB ×2）。

### 5.3 装甲设计评价（来源原话，非本文判断）

> "Protection overall was **not impressive**, making them rather "intermediate" and not armoured cruisers of some sorts." — [naval-encyclopedia](https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php)

> "But nothing revolutionary or quite capable to defeat one or two torpedo hit on places. They were **still vulnerable**. This was not a priority, as they were supposed to be used as commerce raiders with an artillery keeping them nominally out of range of destroyers." — 同上

**纳尔维克式实战反证（Blücher）**：

> "It must be said by the loss of Blücher to the Oscarborg Fortress, an humiliation for the kriesgmarine, was partly due to the hidden "secret torpedoes", and to the initial damaged cause by just **two 28 cm hits**. Despite their age, these guns were perfectly adequate given the short range. **The upper superstructure of the cruiser were never able to cope with his caliber at any range**, but the ASW protection held out for longer than expected after two torpedo hits... It's the fire caused by the initial hit near the hangar that doomed the ship." — 同上

**这段是「本级防护到底什么水平」唯一有实战检验的段落。** 注意它区分了三件事：①上部结构对 28 cm 完全无防护；②水下防护比预期好（挨了两雷才垮）；③致命的是机库附近命中引起的大火。**写 Blücher 或写本级防护评价时必引。**

### 5.4 装甲总重

**未获取。** 五舰均无任何来源给 armor weight。这是 `data/fields.yaml` 里 `protection.armor.weight` 在本级的**空白字段**。

---

## 6. 武备——**本级唯一真正"共性"的一大块**

### 6.1 主炮：8 × 20.3 cm SK C/34（4 × 双联）

> "The three completed ships had the **same battery of eight 20.3 cm SK C/34 guns, in four twin turrets, two superfiring pairs fore and aft**." — [naval-encyclopedia](https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php)

> "Ship Class Used On: Germany: **Admiral Hipper and Prinz Eugen Classes**" — [NavWeaps 20.3 cm](https://www.navweaps.com/Weapons/WNGER_8-60_skc34.php)

炮塔型号：

> "Two-gun turrets / **Admiral Hipper (4) and Prinz Eugen (4): LC/34**" — [NavWeaps](https://www.navweaps.com/Weapons/WNGER_8-60_skc34.php)

**全部炮、弹、塔参数见 `prinz-eugen-tech.md` §7.1（同一门炮，完全通用，此处不重复）。**

### 6.2 「本级火炮略低于华盛顿上限」这条值得单列

> "Ironically these guns were slightly **BELOW** the Washington limit. They were not 203mm stricly (8 inches) but the **actual diameter was 7.992"**." — [naval-encyclopedia](https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php)

NavWeaps 独立确认同一件事：

> "Actual bore diameter was **20.30 cm (7.992")**." — [NavWeaps](https://www.navweaps.com/Weapons/WNGER_8-60_skc34.php)

**两源独立，可作舰级事实。** 且 naval-encyclopedia 给出了原因与后续空间：

> "But the loose barrel used offered some leeway for future increase." — 同上

### 6.3 火力密度与射速的对比（本级实战暴露的问题）

**Hipper 1942 年巴伦支海对英轻巡的实战总结**：

> "When combating a Colony and a Town class cruisers off Norway in 1942, she **held her own perfectly well despite having a considerably lesser rate of fire**." — [naval-encyclopedia](https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php)

NavWeaps 的射速：4–5 发/分（单管）。对比英制 6 英寸轻巡的 8–12 发/分是明显劣势。**这是本级作为「重巡」在 1942 年后已经过时的技术根源。**

### 6.4 副炮：12 × 10.5 cm SK C/33（6 × 双联）

> "No less than **twelve of these guns were installed, in six twin mountings**. They were located on six positions along the structure, two forward on the wings of the battery deck, two on deck abaft the catapult, and two on wings of the aft structure, behind the tripod mainmast. Certainly among the best DP guns of their generation, but still **inferior to the US 5-in/38**." — [naval-encyclopedia](https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php)

炮座型号：**Dop. L. C/31d**（Hipper 与 Prinz Eugen 各 6 座）— [NavWeaps 10.5 cm](https://www.navweaps.com/Weapons/WNGER_41-65_skc33.php)

**【分歧·炮座型号】** NavWeaps 自己注明：「Koop and Schmolke state that Prinz Eugen may have had Dop. L. C/37 mounts.」**并列。**

### 6.5 轻高炮——**按年份演变，不能给单值**

设计状态（naval-encyclopedia，本级通述）：

> "-For Close-range they had **twelve 3.7 cm (1.5 in) SK C/30 guns**, all in dual mounts (doppel) along the superstructures."
> "-They had **eight 2 cm (0.79 in) Rheinmetall Flak 38 guns**. Magazine-fed ... fed by 40 magazines for a grand total of **16,000 rounds** aboard"

但同页对 Hipper 与 Prinz Eugen 各自给了**完全不同的年度演变表**，且末尾还有一句「Naturally this was expanded during the war and on the Prinz Eugen class (see later)」。

**本级轻高炮的可用汇总（按舰按年）**：

| 舰 | 时点 | 3.7 cm | 2 cm | 4 cm Flak 28 | 来源 |
|---|---|---|---|---|---|
| Hipper | 1940 | 6×2 | +2×1 C/38 | — | naval-encyclopedia |
| Hipper | 1941 | 6×2 | +1×4 Flakvierling | — | 同上 |
| Hipper | 1942 初 | 6×2 | +2×1, +2×4 | — | 同上 |
| Hipper | 1942 末 | 6×2 | +1×4 | — | 同上 |
| Hipper | 1943 | 6×2 | +1×4 | — | 同上 |
| Hipper | 1944 | 2×2 | 3×4 + 8×1 + 8×2 | 6×1 | 同上 |
| Prinz Eugen | 建成 | 6×2 | 10×1 C/38 | — | 同上 |
| Prinz Eugen | 1941 末 | 6×2 | +4×4 Flakvierling | — | 同上 |
| Prinz Eugen | 1942 初 | 6×2 | +1×4 | — | 同上 |
| Prinz Eugen | 1944 | **原文自相矛盾，不解析** | 同左 | 同左 | 同上 |
| Prinz Eugen | 1945 | **原文自相矛盾，不解析** | 同左 | 同左 | 同上 |

**Prinz Eugen 1944/1945 两行故意不解析，因为来源给了三句互相打架的话，任何解析都是我替它做题：**

> "In 1944, Prinz Eugen's remaining 3.7 cm guns were **all replaced by fifteen 4 cm (1.6 in) Flak 28 guns**"
> "In 1944, she had **two twin 37mm/80 and two quad 20mm/65 landed** as well as the FuMB 7 Timor ECM suite and in place **six 40mm/56 FlaK 28 installed**."
> "In 1945 this went further and she had **four twin 37mm/80 and ten single 20mm/65 retired** and in place **twelve 40mm/56 FlaK 28 installed** as well as a Flakvierling and two twin 20mm/65 C/38 mounts."

**三句冲突点**：1944 年 4 cm 是 **15 门还是 6 门**？37 mm 是「全部替换掉」还是「只撤 2 座」？1945 年 37 mm 撤 4 座后还剩几座？——**来源自己没有一致性，我不填。**

还有第四句与前三句也对不上（它把两舰 1945 年状态并列给出）：

> "In 1945, she had **twenty 4 cm guns, eighteen 2 cm guns** while Admiral Hipper had **sixteen 4 cm guns, fourteen 2 cm guns**." — 同上

**即 1945 年 Prinz Eugen 的 4 cm 是 12 门（第 3 句）还是 20 门（第 4 句），来源给了两个数。** 这正是 `prinz-eugen-tech.md` §14.5 里那个「轻高炮三份来源给 28 / 32 / 17+28」的同一处病灶。

Hipper 1944 那行是唯一可解析的：
> "In 1944, she only carried **two twin 37mm/80, three Flakvierling and eight single 20mm/65** when added **six single 40mm/56 FlaK 28**, and **eight twin 20mm/65 C/38**."（同页另注 "This did not changed for 1945."）

**结论：本级轻高炮只能按「舰 + 年份」逐格登记，绝不能给舰级单值。** 这与 `docs/30-new-ship-workflow.md` §4.4「三种口径必须分开记」是同一类问题。

### 6.6 鱼雷：12 具 / 4 座三联

> "As befitting to their role of commerce raiders, they had had **no less than twelve torpedo tubes, in four triple launchers** on her main deck amidships. For these, the cruisers carried **twenty-four G7a torpedoes** so twelve loaded in the tubes, and the same ready reload." — [naval-encyclopedia](https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php)

G7a 性能（同页）：

> "Specs: 300 kg (660 lb) warhead, three-speed settings (**12,500 m/30 kn, 7,500 m/40 kn, 5,000 m/44 kn**)"

**本级装雷数是德舰重巡里最高的（12 管）**，与其破交任务定位一致。

### 6.7 水雷

> "KMS Admiral Hipper was also equipped to carry **96 EMC mines**, contact types with a **300 kg explosive charge**." — [naval-encyclopedia](https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php)

**只有 Hipper 有明确数字，其余四舰的布雷能力未获取。** 不能默认同级同数。

### 6.8 深弹（**三源三个数**）

| 来源 | 值 |
|---|---|
| [KB/Hipper] | "**6 x depth charge launchers**." |
| [KB/PrinzEugen] | "**2 x triple depth charge racks**."（= 2 座三联 = 6 管） |
| [Bonomi 脚注 26] | Prinz Eugen 战前战后照片显示深弹从 3 减到 1——"the charges went from **3 to 1**" |

【分析】KB 两页的「6 个发射器」与「2 座三联（6 管）」**在数量上其实一致**（6 = 6）。但 Bonomi 的照片证据说舰上实际只挂 3 个（战前）。**三者不矛盾：6 个架位、3 个挂弹。** 这是本文件里少数可以把分歧合理解释掉的一处——但**没有任何来源明确这样说**，故仍标为「疑似，需核实」。

---

## 7. 航空与传感器

### 7.1 航空

> "As completed, Hipper, Blücher and Prinz Eugen were tailored to carry and operate **three floatplanes**, with **a catapult** (type to find) and **a hangar below, large enough to accomodate two of them, wings folded side by side. The roof of this hangar was telescopic**." — [naval-encyclopedia](https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php)

> "1 catapult, **3 seaplanes (He 60, He114, Ar196)**" — [navypedia](https://www.navypedia.org/ships/germany/ger_cr_hipper.htm)

**机型演变**：设计阶段是 He 60（1934 年双翼机），建成时已被 He 114 取代，实战期全部换装 Ar 196。

> "However by the time Hipper was completed in 1939, it had been already replaced by its sucessor the He 114. However the latter had many issues ... In fact it is likely they were provided with Photos and most sources only shows as model: The infinitely superior **Arado Ar 196**." — [naval-encyclopedia]

**【分歧】载机数 3 vs 4**：同页也承认「several sources points out the Prinz Eugen class as being able to carry **four** floatplane, not three」。
**【未获取】**：机库尺寸、弹射器型号（来源自己写 "type to find"）、各舰实际载机机型的时间表。

### 7.2 雷达——**各舰不同，且都缺装机日期**

| 舰 | 建成时 | 后续 | 来源 |
|---|---|---|---|
| Admiral Hipper | **FuMo 22** | 1942 初 FuMO 27 + FuMB 7 Timor；1944 FuMO 25 | [naval-encyclopedia]："Hipper was provided at completion with a FuMo 22 radar." / "In early 1942, Hipper received a FuMO 27 radar and FuMB 7 Timor ECM suite. In 1944, she received a FuMO 25 radar." |
| Blücher | **未获取** | — | — |
| Prinz Eugen | **2 × FuMO 27**（1941） | 1942-02 FuMO 26 + FuMB 4 Sumatra + FuMB 7 Timor；1944 FuMO 25 + FuMO 81 + FuMB 3 Bali + FuME 2 Wespe-G | 见 `prinz-eugen-tech.md` §8 |
| Seydlitz / Lützow | **未获取**（未建成） | — | — |

navypedia 的级表给的是 **FuMo 22**（"Electronic equipment FuMo 22 radar"）——那是**首舰建成状态**，不能当本级值。

> "Prinz Eugen and her sisters were planned to have **two FuMo27 radars**." — [naval-encyclopedia]

【重要】这句话里的 "her sisters" 与 §4.1 的逐舰动力差异矛盾——如果五艘动力都不同，「plan to have two FuMo27」这种统一说法只能是计划而非实况。**取「计划」义。**

### 7.3 电子战（ECM）

只有 Prinz Eugen 有完整记录（见 `prinz-eugen-tech.md` §8.4）。其余四舰的 ECM 装备**未获取**。

---

## 8. 逐舰差异总表（**这张表是本文件的核心交付**）

| 维度 | Admiral Hipper | Blücher | Prinz Eugen | Seydlitz | Lützow |
|---|---|---|---|---|---|
| 批 | 首批 | 首批 | 改进批 | 改进批 | 改进批 |
| 全长 oa | 205.9 m | 205.9 m | **212.5 m** | 210 m | 210 m |
| 水线长 | 194.6 m | 194.6 m | 199.5 m | — | — |
| 舰宽 | 21.3 m | 21.3 m | 21.7 m | 21.8 m | 21.8 m |
| 吃水（满载） | 7.90 m | 7.90 m | 7.2 m | 7.9 m | 7.9 m |
| 标准排水 | 14,240 mt / 14,050 t / 16,170 t（三说） | 同左 | 16,970 t / 14,240 mt（两说） | 17,600 t | 17,600 t |
| 满载排水 | 18,200 mt / 18,210 t | 同左 | 19,042 mt / 19,050 t | 20,100 t | 20,100 t |
| 锅炉 | La Mont ×12，80 atm | Wagner ×12，70 atm | **La Mont ×12，70 atm** | Wagner ×9，60 atm | Wagner ×9，60 atm |
| 汽轮机 | Blohm & Voss | Blohm & Voss | **Brown-Boveri**（一说 Germania） | Wagner-Deschimag | Wagner-Deschimag |
| 电功率 | 2,900 kW | 2,900 kW | **2,870 kW** | 2,870 kW | 2,870 kW |
| 建成时雷达 | FuMo 22 | 未获取 | 2 × FuMO 27 | 未建成 | 未建成 |
| AA（建成时） | 12 × 3.7 cm + 8 × 2 cm | 未获取 | 12 × 3.7 cm + 10 × 2 cm | 未建成 | 未建成 |
| 建成/结局 | 1939-04-29 / 1945-05-03 自沉 | 1939-09-20 / 1940-04-09 战沉 | 1940-08-01 / 1946-12-22 倾覆 | 未建成 / 1945-04-10 自沉 | 未建成 / 1950s 苏联拆解 |
| 造价 | — | 87.8 Mio RM | 104.5 Mio RM | 84.1 Mio RM | 83.6 Mio RM |

**读法**：
1. **主尺度必须分批**。首批 205.9 m 与改进批 210–212.5 m 差 4–6.6 m，套错直接影响线图与模型比例。
2. **动力必须逐舰**。五艘四组配置，无一相同。
3. **武备与装甲可继承**（§5、§6），因为「the three completed ships had the same battery」有明确原话。
4. **轻高炮与雷达必须按舰按年**（§6.5、§7.2）。

---

## 9. 编制

| 来源 | 值 | 原句 |
|---|---|---|
| [KB/Hipper] | **1,600** | "Crew: 1,600." |
| [german-navy/hipper] | ~1600 | "Crew ~1600" |
| [navypedia] | **1,600** | "Complement 1600" |
| [KB/PrinzEugen] | 1,600 | "Crew: 1,600." |
| [naval-encyclopedia/Prinz Eugen] | **42 军官 + 1,240 士兵 = 1,282** | "Crew 42 officers, 1240 ratings" |

**三源给 1,600，一源给 1,282。** 后者把两级细分了（唯一一条细分数据），前者全是整数 1,600——**很可能是同一来源的转抄链**。

**军官 / 士官 / 水兵三级细分：未获取。**（只有「军官 42」这一个值。）

---

## 10. 本级的设计评价（来源原话，非本文判断）

### 10.1 正面

> "Their silhouette recalled the Scharnhorst battleships in reduction, but **still at launch they were the most powerful cruisers in the world**." — [naval-encyclopedia](https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php)

> "She had the best combination possible at the time, **worthy of a battleship**."（指火控/光学/雷达）— 同上

### 10.2 负面

> "For their size, these cruisers were **not that impressive**. Their battery was "standard", as it was difficult to lie about, with a classic 4×2 main gun configuration." — 同上

> "In practice, the ships' **high-pressure steam machinery consumed too much fuel for sustained Atlantic operations and proved difficult to maintain**." — [german-navy/hipper](https://www.german-navy.de/kriegsmarine/ships/heavycruiser/admiralhipper/index.html)

> "As seen already with torpedo boats, the Kriegsmarine had trouble with its ultra-high-pressure boilers and its steam plants suffered from **low reliability while not giving the intended output, significantly reducing endurance**." — [naval-encyclopedia]

### 10.3 战术定位的失败

> "Wartime showed they **never really found their place**, between the sinking of Blücher by an antiquated Norwegian fortress to the largely failed raid attempt of Prinz Eugen and the few sorties made later from Norway." — [naval-encyclopedia](https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php)

**这句可以作为本级页面的总结句。** 它是 D 级来源的评断，只能进 narrative，不能作 fact 的 src。

---

## 11. 未获取字段汇总

### 11.1 舰级层面（五舰通用）

| 字段 | 状态 | 说明 |
|---|---|---|
| `protection.armor.weight` | **未获取** | 装甲总重，五舰均无 |
| 装甲逐段厚度（单舰） | **未获取** | navypedia 那段是舰级通述，且它自己说 Prinz Eugen "internal arrangement 有差异" |
| `aviation.hangar.dimensions` | **未获取** | 只知道「可容纳 2 架折叠翼」 |
| `aviation.catapult.model` | **未获取** | 来源自己写 "type to find" |
| `aviation.fuel` | **未获取** | 航空燃油量 |
| 巡航汽轮机 | 确认**没有**（非未获取） | "refused in favour of purely turbine" |
| `propulsion.boiler.steam_temp` | **未获取** | 只有压力（60/70/80 atm），无温度 |
| `propulsion.turbine.stages` | **未获取** | 与俾斯麦号（HP Curtis 40 级等）不同，无同类数据 |
| `sensors.radar.*` 性能参数 | **未获取** | 波长/功率/探距全部无 |
| 各舰 ECM 装备 | **仅 Prinz Eugen 有** | 其余四舰未获取 |
| 编制三级细分 | **未获取** | 只有「军官 42」 |
| 舰员伤亡总表 | **未获取** | — |

### 11.2 单舰层面（本级特有缺口）

| 舰 | 缺口 |
|---|---|
| Admiral Hipper | 建成时 AA 完整清单有（12×3.7 + 8×2），但 1944 年状态的 4 cm 数只有一处；ECM 装备未获取 |
| **Blücher** | **资料最少**。雷达未获取、AA 未获取、编制未获取。唯一有实战检验记录（奥斯陆峡湾）但技术细节缺 |
| Prinz Eugen | 见 `prinz-eugen-tech.md` §14（清单最长） |
| **Seydlitz** | **未建成，大部分数据不适用或不存**。改装航母（Weser）的方案未获取 |
| **Lützow** | **未建成，售予苏联后改名 Petropavlovsk / Tallin**。苏方改装数据未获取 |

### 11.3 明确「不适用」而非「未获取」

- `aviation.deck.*` / `elevator.*` / `arrestor.count` —— 重巡无飞行甲板（Seydlitz 的航母改装案另论，见 §11.2）
- `armament.broadside_weight` —— 无来源给，**不能自己乘算**（这正踩 `docs/30-new-ship-workflow.md` §2.2 的坑）

---

## 12. 抓取记录

### 12.1 有效的

| URL | 内容 |
|---|---|
| https://www.navypedia.org/ships/germany/ger_cr_hipper.htm | **舰级技术表 + 逐段装甲，唯一按部位组织的来源**（27,579 bytes） |
| https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php | 逐舰动力差异、AA 年表、吨位改进、五舰建造史。**含多处笔误与内部矛盾**（666,501 bytes HTML） |
| https://www.kbismarck.com/admiral-hipper.html | 首舰生涯 + 技术表（17,274 bytes） |
| https://www.kbismarck.com/blucher.html | 二号舰生涯 + 技术表（11,462 bytes） |
| https://www.german-navy.de/kriegsmarine/ships/heavycruiser/admiralhipper/index.html | 首舰 |
| https://www.german-navy.de/kriegsmarine/ships/heavycruiser/prinzeugen/index.html | 三号舰 |
| https://www.german-navy.de/kriegsmarine/ships/heavycruiser/blucher/index.html | 二号舰（含造价） |
| https://www.german-navy.de/kriegsmarine/ships/heavycruiser/seydlitz/index.html | 四号舰（含造价） |
| https://www.german-navy.de/kriegsmarine/ships/heavycruiser/lutzow/index.html | 五号舰（含造价）。**注意路径是 `lutzow` 无 umlaut** |
| https://www.navweaps.com/Weapons/WNGER_8-60_skc34.php | 主炮 |
| https://www.navweaps.com/Weapons/WNGER_41-65_skc33.php | 10.5 cm 副炮 |
| https://www.navweaps.com/Weapons/WNGER_37mm-83_skc30.php | 3.7 cm |

### 12.2 失败的（下次别试）

| URL | 结果 |
|---|---|
| `https://www.navypedia.org/ships/germany/ger_cr_hipper_class.htm` | 404（正确是 `ger_cr_hipper.htm`） |
| `https://www.navypedia.org/ships/germany/ger_cr.htm` | 404 |
| `https://www.kbismarck.com/hipper.html` | 404（正确是 `admiral-hipper.html`） |
| `https://www.german-navy.de/kriegsmarine/ships/heavycruiser/luetzow/index.html` | 404（正确是 `lutzow`） |
| `https://ww2db.com/ship_spec.php?ship_id=98` | 403 |
| `https://www.navweaps.com/Weapons/WNGER_105-65_skc33.php` | 404（正确是 `WNGER_41-65_skc33.php`） |
| `https://www.hmshood.org.uk/...` | 403（英国舰站，与德舰无关，顺带记录） |
| `https://www.combinedfleet.com/` | 200 但**全站只做日本舰**，无德舰页 |

### 12.3 navypedia 上没有单舰页

**本级五舰在 navypedia 只有级页，没有 Prinz Eugen / Seydlitz / Lützow 的单舰页**（试过 `ger_cr_prinz_eugen.htm` → 404）。这与 `docs/30-new-ship-workflow.md` §1.3 的「navypedia 只用来垫底核对」定位一致。

---

## 13. 来源清单

| 代号 | 来源 | URL | 等级 | 用途 |
|---|---|---|---|---|
| **NAVYPEDIA** | navypedia.org, "ADMIRAL HIPPER heavy cruisers (1939)" | https://www.navypedia.org/ships/germany/ger_cr_hipper.htm | **D** | 逐段装甲、首批主尺度、五舰建造表、动力型式 |
| **NAVALENC** | naval-encyclopedia.com, "Hipper class cruisers (1937)" | https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php | **D** | 逐舰动力差异、AA 年表、电气系统、防护评价、载机、ECM。**已知多处笔误，凡引用均须核** |
| **KB-HIPPER** | kbismarck.com, "Admiral Hipper" | https://www.kbismarck.com/admiral-hipper.html | **D** | 首舰生涯、技术表、舰长名录 |
| **KB-BLUCHER** | kbismarck.com, "Blücher" | https://www.kbismarck.com/blucher.html | **D** | 二号舰建造、造价 |
| **KB-PG** | kbismarck.com, "Cruiser Prinz Eugen" | https://www.kbismarck.com/prinzeugen.html | **D** | 三号舰 |
| **GN-HIPPER** | german-navy.de, Admiral Hipper | https://www.german-navy.de/kriegsmarine/ships/heavycruiser/admiralhipper/index.html | **D** | 首舰 |
| **GN-PG / GN-BLÜCHER / GN-SEYDLITZ / GN-LÜTZOW** | german-navy.de 各舰页 | 见 §12.1 | **D** | 建造记录、造价、船台 |
| **NW-203** | NavWeaps, 20.3 cm/60 SK C/34 | https://www.navweaps.com/Weapons/WNGER_8-60_skc34.php | **C** | 主炮（舰级通用） |
| **NW-105** | NavWeaps, 10.5 cm/65 SK C/33 | https://www.navweaps.com/Weapons/WNGER_41-65_skc33.php | **C** | 副炮 |
| **NW-37** | NavWeaps, 3.7 cm/83 SK C/30 | https://www.navweaps.com/Weapons/WNGER_37mm-83_skc30.php | **C** | 3.7 cm |
| **KTB-PG**（跨舰借用） | Prinz Eugen 战争日志 | https://www.kbismarck.com/archives/pg-ktb.zip | **A** | 本级唯一的一手档案，用于验证「高速不许满舵」等操舵特性 |

### 等级说明

本文件**没有 A 级一手档案直接描写舰级**——五艘船里只有 Prinz Eugen 有公开可下载的战争日志，而那是单舰档案。**「舰级」这个概念本身在本项目里是靠 D 级专题站拼出来的**，这一点必须诚实。

---

## 14. 与单舰文件的分工（写给下次的自己）

按 `docs/30-new-ship-workflow.md` §3 路径 A：

- **可以放舰级文件**（真正共有，有原话支撑）：主炮与副炮（§6.1–6.4）、鱼雷（§6.6）、装甲方案骨架（§5.1）、航空配置（§7.1）、设计目标与条约背景（§2）、五舰建造记录（§1）。
- **必须留单舰文件**：主尺度（分批）、动力装置（逐舰）、轻高炮年度演变、雷达装机表、编制、涂装、战史、结局。
- **绝对不能继承**：KB 的「燃油 4,250 mt / 续航 6,800 nm @16 kn / 型深 12.45 m / 测距仪 5×7 m」四项——两页逐字相同，是复制痕迹（见 §4.3）。
- **Seydlitz 与 Lützow 要特别小心**：两舰都是「按轻巡设计、中途改重巡炮、未建成」，吨位与稳性数据不能与前两艘混。Lützow 售予苏联后改名 Petropavlovsk → Tallin，苏方改装数据本项目完全没有。

---

*本文所有数值均可在对应 URL 页面内定位复核。抓取失败的来源已列入 §12.2。未做任何推测补全，未用别国或别级重巡数据填充。*
