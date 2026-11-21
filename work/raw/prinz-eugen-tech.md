# Prinz Eugen（欧根亲王号，重巡洋舰）— 技术数据、丹麦海峡炮战记录与生涯

> 检索日期：2026-11-21。
> **执行说明**：每条数值附英文原句 + 来源 URL。查不到一律写「未获取」，**不推算、不用姊妹舰数值填充**。
> 来源等级：A 一手档案 / B 同期官方出版物 / C 权威二次文献 / D 专题网站 / E 百科（**仅线索，不作数值来源**）。
> 本文不做平均、不做单位换算推导；同字段多来源冲突者全部并列。

---

## 0. 先说任务书：五处前提需要纠正

调研过程中发现任务书里有五条前提与实际材料不符，按调研铁律第 4 条先行反驳。

### 0.1 「kbismarck.com 没有本舰页面」——错，页面存在，只是文件名没有连字符

任务书实测 `kbismarck.com/prinz-eugen.html`、`kbismarck.com/prinz_eugen.html` 均 404。实测可用地址是**无连字符、无下划线**的：

```
https://www.kbismarck.com/prinzeugen.html   → 200, 25,035 bytes
```

该页是 José M. Rico 撰写的完整单舰页，含生涯时间线、舰长名录、技术数据表，**并挂了一份 A 级一手档案下载**（`archives/pg-ktb.zip`，2,377,700 bytes，122 页 PDF，Prinz Eugen 1941-05-18 至 06-01 战争日志德英对照全译本）。

这是本次调研最重要的发现：**本舰的一手档案是齐全的，缺的不是档案，是我一开始没找对文件名。** 下次做德舰先试「无分隔符小写全拼」这一种。

### 0.2 「1942 年被英军空袭于瑟堡（未沉）」——地点错、年份错

本舰**从未在瑟堡被空袭**。实际事件是 **1941-07-02 在布列斯特（Brest）干船坞内被炸弹命中**：

> "02 July 1941: While drydocked in Brest, the ship is hit at 0144 hours by a bomb in the port side, Section X. 60 dead, including Executive Officer (I.O.) *Fregattenkapitän* Otto Stooß." — [kbismarck/prinzeugen](https://www.kbismarck.com/prinzeugen.html)

1942 年 2 月的实际事件是「瑟布鲁斯行动」（穿越英吉利海峡）与随后被英潜艇 *Trident* 雷击（见 §12）。**编号与年份都不对，按 Brest / 1941 更正。**

### 0.3 「1960 年代倾覆于夸贾林」——错，倾覆日期是 1946-12-22

四个独立来源一致：

> "**22 December 1946:** Due to leaks takes a 35º starboard list and capsizes over Enubuj reef in position 08º 45' 08" North, 167º 40' 59" East" — [kbismarck/prinzeugen](https://www.kbismarck.com/prinzeugen.html)

> "she capsized and sank 22 December 1946. Into 1970 she remains rusting on a coral reef at Enubuj, Kwajalein Atoll." — [DANFS / NHHC](https://web.archive.org/web/2023id_/https://www.history.navy.mil/research/histories/ship-histories/danfs/p/prinz-eugen.html)

> "22.12.1946 After six days of increased list, the Prinz Eugen capsized and sinks." — [german-navy.de](https://www.german-navy.de/kriegsmarine/ships/heavycruiser/prinzeugen/index.html)

「1960 年代」大概是把它和 **1978 年拆螺旋桨**这件事混了（见 §13）。**倾覆是 1946 年，1960 年代只是「仍在那儿」的时间坐标。**

### 0.4 「必须接上 data/narratives/bismarck.yaml 里已有的『谁打沉了胡德』争议条目」——该条目不存在

`data/narratives/bismarck.yaml` 现存的五条是：

| id | 主题 |
|---|---|
| `bismarck-sinking-cause` | 俾斯麦号是战损沉没还是自沉 |
| `bismarck-lindemann-death` | 林德曼阵亡时刻 |
| `bismarck-hits-received` | 最终战命中数 |
| `bismarck-survivors-count` | 生还者人数 |
| `bismarck-wreck-discovery-date` | 残骸发现日 |

**没有一条涉及「胡德被谁打沉」。** 「谁打沉了胡德」的材料实际散在三处：

1. `work/raw/hood-sinking.md` §争议二（第 161–191 行）——这是全项目对这个问题最完整的整理，含 Jurens 的定量反驳；
2. `data/ships/hood.yaml` 第 941 行的 note：「但『是哪一发、从哪条路径进去的』仍有争议，另见 narrative」——**这句引用的 narrative 并不存在**，是个悬空引用；
3. `data/sources.yaml` 里 `hooddenmark2` 与 `hoodsinking-jurens` 两条的 note。

所以本文 §11.4 的做法是：**以 `hood-sinking.md` §争议二 的既有立场为基准接续，加上本次从 Prinz Eugen 战争日志与炮术官报告里新取得的一手证据**，不另开一套说法。同时提示：`hood.yaml` 第 941 行那句「另见 narrative」目前指向空气，要么补建 narrative，要么改措辞——这需要主会话决定，本文只指出。

### 0.5 「先于俾斯麦开火」——来源之间互相矛盾，不能当既定事实写

任务书说「它在俾斯麦前方，先于俾斯麦开火」。前半句成立（KTB 多处可证），**后半句两条 kbismarck 页面自相矛盾**：

> "It was Prinz Eugen, at 05:55, the first German ship to open fire" — [Bonomi, The Denmark Strait Battle (PDF)](https://www.kbismarck.com/ds-barticle.pdf)

> "Finally at 0555 ... the *Bismarck* opened fire, followed by the *Prinz Eugen* immediately afterwards." — [kbismarck/denmark-strait](https://www.kbismarck.com/denmark-strait-battle.html)

> "0555. *Prinz Eugen* fires her first salvo at *Hood* from 20,200 meters **immediately after** *Bismarck*." — [kbismarck/prinzeugen](https://www.kbismarck.com/prinzeugen.html)

同一个站的两页，一页说欧根先开火，另一页说俾斯麦先开火。本舰炮术官 Jasper 的报告只说「接到开火许可后立即打出全齐射」，**不比较两舰先后**：

> "I received "permission to fire" from the bridge at 0455 hours and immediately commenced firing a full salvo at 202 hectometers [20,200 meters]." — Prinz Eugen KTB，第 39 页，Jasper 炮术报告

结论：**「两舰几乎同时开火，先后次序在来源之间不一致」** 才是可写的表述。详见 §11.2。

---

## 1. 身份

| 项目 | 值 | 来源 |
|---|---|---|
| 原名 | *Prinz Eugen* | 全部来源一致 |
| 舰名来源 | 萨伏依的欧根亲王（1663–1736），奥地利将领 | [DANFS](https://web.archive.org/web/2023id_/https://www.history.navy.mil/research/histories/ship-histories/danfs/p/prinz-eugen.html)："Prince Eugene of Savoy (1663-1736), an Austrian general, fought France and the Ottoman Empire during various wars." |
| 曾拟用名 | *Wilhelm von Tegetthoff* | [naval-encyclopedia](https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php)："Her initial name was "Wilhelm von Tegetthoff" to commemorate the Battle of Lissa and to concile the good will of Austria, but it was seen at the time as an insult to Italy... the more neutral "Prinz Eugen" was chosen" |
| 代号 | 「Kreuzer J」 | [navypedia](https://www.navypedia.org/ships/germany/ger_cr_hipper.htm)："A year later the order on Prinz Eugen ("J"), having some differences on an internal arrangement, has arrived." |
| 建造编号 | G 564（KB）/ hull number 564（naval-encyclopedia） | [kbismarck](https://www.kbismarck.com/prinzeugen.html)："Construction number G 564." |
| 舰种 | 重巡洋舰（heavy cruiser） | [kbismarck](https://www.kbismarck.com/prinzeugen.html)："the third and last heavy cruiser commissioned by the *Kriegsmarine*" |
| 舰级 | 希佩尔海军上将级（Admiral Hipper class）第 3 号舰，属**改进批**（PG / Seydlitz / Lützow） | 见 `hipper-class.md` |
| 同型建成舰 | 3 艘（Admiral Hipper、Blücher、Prinz Eugen） | [naval-encyclopedia](https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php)："Only Admiral Hipper, Blücher and Prinz Eugen were completed as heavy cruisers" |
| 造价 | 104.5 Mio Reichsmark | [german-navy.de](https://www.german-navy.de/kriegsmarine/ships/heavycruiser/prinzeugen/index.html)："Cost 104,5 Mio Reichsmark" |
| 美军舷号 | IX-300（1946） | [DANFS](https://web.archive.org/web/2023id_/https://www.history.navy.mil/research/histories/ship-histories/danfs/p/prinz-eugen.html)："(IX-300: ...)" |

**KB 的一句话定位**（可直接用作页面摘要）：

> "The *Prinz Eugen* (fourth warship to wear that name) was the third and last heavy cruiser commissioned by the *Kriegsmarine*." — [kbismarck/prinzeugen](https://www.kbismarck.com/prinzeugen.html)

---

## 2. 建造与服役

### 2.1 日期（四项，四来源比对）

| 事件 | 值 | 来源与原句 |
|---|---|---|
| 签订建造合同 | 1935-11-16 | [KB]："**16 November 1935:** Building contract placed." |
| 开工 | **1936-04-23** | [KB]："**23 April 1936:** Lay down at the Germania shipyards in Kiel. Construction number G 564." |
| 开工（一致复述） | 1936-04-23 | [german-navy]："Laid down Germaniawerft Kiel, 23.04.1936 (Slipway 2)" |
| 开工（仅年份） | 1936 | [DANFS]："Prinz Eugen was laid down in 1936 by the Krupp Germania Werft Yards, Kiel, Germany" |
| 开工（一致复述） | 1936-04-23 | [naval-encyclopedia]："laid down on 23 April 1936 as hull number 564, "Kreuzer J"" |
| 下水 | **1938-08-22** | [KB]："**22 August 1938:** Launched. Christened by Frau Magda von Horthy, wife of the Hungarian Regent." |
| 下水（一致） | 1938-08-22 | [german-navy]："Launched 22.08.1938" |
| 下水（**分歧**） | **1938-08-20** | [DANFS]："launched 20 August 1938" |
| 服役 | **1940-08-01** | [KB]："**01 August 1940:** Commissioned under Captain Helmuth Brinkmann." |
| 服役（一致） | 1940-08-01 | [german-navy]："01.08.1940 Commissioned"；[DANFS]："commissioned in the German Navy 1 August 1940" |

**【分歧】下水日**：22 August（KB、german-navy、naval-encyclopedia）vs 20 August（DANFS）。三比一，但 DANFS 是美国海军官方舰史（B 级），不是随手抄的站点。**并列不裁决。**

### 2.2 厂

**Krupp Germaniawerft, Kiel** ——任务书的猜测成立，可确认：

> "Prinz Eugen was laid down in 1936 by the **Krupp Germania Werft Yards, Kiel**, Germany" — [DANFS](https://web.archive.org/web/2023id_/https://www.history.navy.mil/research/histories/ship-histories/danfs/p/prinz-eugen.html)

> "23 April 1936: Lay down at the **Germania shipyards in Kiel**." — [KB](https://www.kbismarck.com/prinzeugen.html)

船台号：Slipway 2（[german-navy]："(Slipway 2)"）。

### 2.3 服役前即被炸

> "July 1940 Before commissioned, the Prinz Eugen was twice hit by British bombs in the Germaniawerft, Kiel" — [german-navy.de](https://www.german-navy.de/kriegsmarine/ships/heavycruiser/prinzeugen/index.html)

KB 只记了一次，日期是服役后两天（07-02）：

> "02 July 1940: Hit by a bomb during a British air raid on Kiel. Damage is slight." — [KB](https://www.kbismarck.com/prinzeugen.html)

**分歧**：german-navy 说「服役前两次」（即 1940-08-01 之前），KB 说 1940-07-02 一次、损伤轻微。两者时间不冲突（7 月 2 日在 8 月 1 日之前），但「两次 / 一次」冲突。并列。

### 2.4 建造期试航与战前磨合（KB 时间线原文）

| 日期 | 事件 | 原句 |
|---|---|---|
| 1940-08-21 | 巡洋舰部队司令登舰海上检阅 | "The commander of Cruisers (B.d.K.), *Vizeadmiral* Hubert Schmundt, boards the *Prinz Eugen* for a inspection at sea." |
| 1940-12-14 – 1941-01-24 | 波罗的海 | "Baltic Sea." |
| 1941-01-25 – 1941-04-08 | 基尔 | "At Kiel." |
| 1941-04-14 | 测速（重要） | "Performs measured mile runs off Neukrug achieving a top speed of **32.837 knots at 74% payload**." |
| 1941-04-15/16 | 充当 U 艇靶标；FuMO 27 探潜 | "On the 16th, the ship's FuMO 27 radar at the foretop is able to detect half-surfaced submarines from a distance of 6,000-7,000 meters at night." |
| 1941-04-23 | 触磁雷 | "Damaged by a magnetic mine while en route to Kiel." |
| 1941-04-24 – 05-02 | Deutsche Werke Kiel C 坞修理 | "Drydocked for repairs at Deutsche Werke Kiel (Dock C)." |

**32.837 节 / 74% 载荷** 是本舰唯一一条实测航速，比任何「设计航速」都硬。来源 D 级，但它是引原文的实测记录。

触雷的具体损伤，KTB 里有一条关键交叉印证（此后一直是本舰主机故障的根源）：

> "On 23 April 1941, 1501, detonation 15 m outboard, caused temporary shutdown of the entire machinery." — [KTB 第 64 页脚注 1，引 Schmalenbach]

---

## 3. 主尺度与排水量

### 3.1 全长

| 值 | 口径 | 来源与原句 |
|---|---|---|
| **212.5 m** | overall length（加装 clipper bow 后） | [KB]："Dimensions: overall length 212.5 m" |
| **212,5 m** | Length (Total) | [german-navy]："Length (Total) 212,5 m" |
| **212.50 m** | — | [naval-encyclopedia]："212,50 m x 21,70 m x 7,20 m (697 ft 2 in x 71 ft 2 in x 24 ft)" |
| 199.5 m（水线） | waterline | [naval-encyclopedia]："Prinz Eugen was 199.5 m (655 ft) long at the waterline, 207.7 m (681 ft) overall as planned, but the addition of a clipper bow had her extended to 212.5 m (697 ft), making her the longest cruiser in Europe." |
| 207.7 m | 原设计全长（加 clipper bow 前） | 同上 |

**只有 naval-encyclopedia 给了水线长 199.5 m 与「加装前 207.7 m」。** KB / german-navy 均无 length.wl 字段。**本舰水线长只有一个 D 级来源，其余来源未获取。**

【注意】navypedia 的希佩尔级表给 `Length, m 194.6 wl 205.9 oa`，那是**首批舰（Hipper/Blücher）**的数据，不能套到本舰（见 `hipper-class.md` §3）。

### 3.2 舰宽

| 值 | 来源 |
|---|---|
| 21.7 m | [KB]："beam 21.7 m" |
| 21,7 m | [naval-encyclopedia]："212,50 m x 21,70 m x 7,20 m" |
| **21,8 m** | [german-navy]："Beam 21,8 m" |

**三源二分：21.7 vs 21.8。** 并列。

### 3.3 吃水

| 值 | 口径 | 来源 |
|---|---|---|
| **7.2 m** | "maximum draft" | [KB]："maximum draft 7.2 m" |
| 7,2 m | Draft（未注状态） | [german-navy]："Draft 7,2 m" |
| 6.6 m / 7.2 m | 标准排水 / 满载 | [naval-encyclopedia]："with a draft of 6.6 m (22 ft) on standard displacement, up to 7.2 m fully loaded" |

标准状态吃水 6.6 m **只有 naval-encyclopedia 一个来源**。

### 3.4 排水量——四个来源四种口径，且有一个来源疑为姊妹舰抄写

| 值 | 口径 | 来源与原句 |
|---|---|---|
| **14,240 mt** | "standard" | [KB]："Displacement: standard 14,240 mt, full load 19,042 mt." |
| **19,042 mt** | "full load" | 同上 |
| **18,400 t** | "Size (Max)" / "Maximum displacement" | [german-navy] quick-facts："18400 t Maximum displacement"；tech-grid："Size (Max) 18400 t" |
| **16,970 t** | "as designed standard" | [naval-encyclopedia]："KMS Prinz Eugen, which displacement increased to 16,970 t (16,700 long tons; 18,710 short tons) as designed standard, and this rose to 18,750 long tons and (19,050 t) fully loaded." |
| **19,050 t / 18,750 lt** | full load | 同上 |
| **19,250 (f.)** | 满载（美制短吨口径，1946 年美方实测/编制） | [DANFS]："(IX-300: dp. 19,250 (f.); ...)" |

**【重要·疑似抄错】** KB 的 Prinz Eugen 页给的标准排水量 **14,240 mt**，与它自己 Admiral Hipper 页的 **14,240 mt 完全相同**；同时它的 fuel capacity（4,250 mt）、endurance（6,800 nm at 16 knots）、"height/depth"（12.45 m）也**与 Hipper 页逐字相同**：

> KB/Hipper："Displacement: standard 14,240 mt, full load 18,200 mt. ... Endurance: 6,800 nm at 16 knots. Fuel capacity: 4,250 mt. ... depth 12.45 m."
> KB/PrinzEugen："Displacement: standard 14,240 mt, full load 19,042 mt. ... Endurance: 6,800 nm at 16 knots. Fuel capacity: 4,250 mt. ... height 12.45 m."

两舰满载不同（18,200 vs 19,042），但标准排水量、续航、燃油、型深四项一字不差。**这四项在 KB 内部高度可疑为从 Hipper 页复制的默认值，不宜单独作为本舰数据。** 而 naval-encyclopedia 明确说改进批的标准排水量涨到 16,970 t——与「比首批大得多」的定性一致。

**【结论】** 本舰标准排水量**在 14,240 与 16,970 之间无法用现有来源判定**，两个值都登记，标注 conflict。满载值较可靠：19,042 / 19,050 / 19,250（三源集中在 19,0xx–19,25x）。

### 3.5 其他尺度

| 项目 | 值 | 来源 |
|---|---|---|
| 型深 / height | 12.45 m | [KB]："height 12.45 m"（注：与其 Hipper 页 "depth 12.45 m" 同值，见上） |
| 干舷 | **未获取** | — |
| 水线面积 | **未获取** | — |
| 方形系数 / 棱形系数 | **未获取** | — |
| 初稳性高 GM | **未获取** | — |

---

## 4. 动力

### 4.1 锅炉——**本舰与首舰不同型**，这是舰级层面的关键差异

| 来源 | 原句 |
|---|---|
| [naval-encyclopedia] | "-Admiral Hipper had **La Mont** boilers working at 80 atm coupled with Blohm und Voss turbine units." / "-Blücher had **Wagner** boilers (with natural circulation) working at 70atm, and also Blohm und Voss turbines." / "-**Prinz Eugen had La Mont boilers (70atm) but Brown-Boveri turbines**" |
| [navypedia] | "Machinery Admiral Hipper: 3 sets Blohm & Voss geared steam turbines, 12 La Mont boilers Blücher: 3 sets Blohm & Voss geared steam turbines, 12 Wagner boilers" |
| [KB] | "Propulsion plant: 12 boilers, three **Germania** turbine sets, 132,000 hp. One rudder." |
| [german-navy] | "Turbines 3 / Type **Germania**" |

**【分歧·重要】汽轮机厂**：
- naval-encyclopedia 说本舰是 **Brown-Boveri** 汽轮机（并明确与 Hipper 的 Blohm&Voss 相对）；
- KB 与 german-navy 说 **Germania** 汽轮机。

**两说不能同时成立。** 有可能 Germania 是主承包商、Brown-Boveri 是子供应商（本舰在 Germaniawerft 建造，由船厂配套主机是常见做法），但**没有任何来源这样说**，属我的推测，不入库。**并列不裁决。**

锅炉数量：12 台（KB、navypedia 均给 12；naval-encyclopedia 对本舰未给数量，只给型式与压力）。锅炉型式：La Mont，70 atm（naval-encyclopedia）。**KB 未给锅炉型式与压力，未获取于 KB。**

### 4.2 主机与轴

| 项目 | 值 | 来源 |
|---|---|---|
| 轴数 | 3 | [navypedia]："No of shafts 3"；[german-navy]："Shafts 3" |
| 汽轮机 | 3 组齿轮传动 | [navypedia]（对本级首批）"3 sets Blohm & Voss geared steam turbines"；本舰见 §4.1 分歧 |
| 舵 | 1 | [KB]："One rudder."；[naval-encyclopedia]："Steering depending on a single rudder." |
| 螺旋桨 | 3 叶，直径 4.1 m | [naval-encyclopedia]："Each turbine drove a three-bladed screw 4.1 m (13 ft) in diameter." |

### 4.3 功率与航速

| 项目 | 值 | 来源与原句 |
|---|---|---|
| 设计功率 | 132,000 shp | [KB]："132,000 hp"；[navypedia]："Power, h. p. 132000" |
| 设计功率（**分歧**） | **136,000 shp** | [german-navy]："Total Performance 136000 shp" |
| 设计航速 | 32 kn | [navypedia]："Max speed, kts 32"；[naval-encyclopedia]："procured on paper a top speed of 32 knots" |
| 航速（**分歧**） | 32.5 kn | [german-navy]："Speed 33,5 kn"（注：quick-facts 与 tech-grid 均写 33,5） |
| 航速（**分歧**） | **33.5 kn** | [german-navy]："Speed 33,5 kn" |
| 航速（KB 区间） | 32–33 kn | [KB]："Speed: 32-33 knots." |
| **实测最大航速** | **32.837 kn（74% 载荷）** | [KB]："Performs measured mile runs off Neukrug achieving a top speed of 32.837 knots at 74% payload." |

**四源四值：32 / 32.5 / 33.5 / 32–33。** 唯一有测量性质的是 32.837 kn（测速标柱实测）。german-navy 的 136,000 shp + 33.5 kn 是唯一给出「超设计值」的一家，其余三家都落在 32 附近。

### 4.4 续航与燃油

| 项目 | 值 | 来源 |
|---|---|---|
| 续航 | 6,800 nm @ 16 kn | [KB]："Endurance: 6,800 nm at 16 knots."（注：与 Hipper 页逐字相同，见 §3.4） |
| 续航（**分歧**） | 6,800 nm @ 20 kn | [naval-encyclopedia]："This resulted, for a cruising speed of 20 knots ..., of a comfortable range 6,800 nautical miles"；[navypedia]："Endurance, nm(kts) 6800(20)" |
| 续航（**分歧**） | **7,200 miles @ 20 kn** | [german-navy]："Range 7200 miles at 20 kn" |
| 燃油容量 | **4,250 mt** | [KB]："Fuel capacity: 4,250 mt." |
| 燃油容量（**分歧**） | **3,050 t oil**（设计额定）；可注满防雷空舱后加倍至 3,250 t | [navypedia]："Fuel, t oil 3050"；[naval-encyclopedia]："they carried 1,420 to 1,460 t ... as designed, but ... They could be filled, as the double bottom, and ensure to double that figure to 3,050 to 3,250 t" |

**【分歧·口径】** 4,250 mt（KB）vs 3,050 t（navypedia）vs 1,420–1,460 t 设计 + 空舱利用后 3,050–3,250 t（naval-encyclopedia）。**三者不可能是同一口径。** KB 的 4,250 很可能把可注水舱段全算进去了，但它没解释；naval-encyclopedia 明确区分了「设计装载」与「利用防雷空舱后的最大值」。**三者并列，标 comparable: false。**

KTB 里有一条本舰实际油量的硬记录，可作交叉校验：

> "Starting oil transfer from "Wollin". Hourly output 250 to 300 cubic meters. All together 764 cubic meters were taken on. Total stores after oil transfer: **3,233 cubic meters**." — KTB 第 11 页（1941-05-21，挪威 Kalvanes 湾加油后）

且 KTB 脚注明写：**"3,250 t was maximum capacity of PG; later modified to hold 3400 t."** — 这与 naval-encyclopedia 的 3,050–3,250 t 区间吻合，**并与 KB 的 4,250 mt 直接冲突**。所以 KB 的 4,250 基本可以判定为不可靠。

### 4.5 本舰主机在实战中的实际状态（KTB 独家，很有价值）

KTB 1941-05-29 的机械报告列了三条同时存在的故障，这是「高压蒸汽动力不可靠」最直接的一手证据：

> "1.) a flange on the main steam-line is whistling. ... [pressure dropped to] 50 atmospheres [normal is 85 atmospheres]. Therefore, **the portside engine is not clear for flank** [speed]."
> "3.) The main water cooling pump amidships has been defective for several days. ... If the pump does not withstand this overload, the center [amidships] engine must shut down."
> "4.) **The portside engine has now failed quite suddenly.** Report of noises in the low pressure turbines."

以及舰长对全舰机械的总评：

> "At this point in time, one engine cannot be fully deployed because of the damaged screw blade, the second is dependent on the survival of the overloaded pump, and now the third engine is nearly sidelined ..." — KTB 第 61 页

**这三条故障最终决定了本舰 1941-06-01 进布列斯特而不是继续破交**，是「瑟布鲁斯行动」的前因。写生涯叙事时这条比任何装备表都重要。

---

## 5. 防护

### 5.1 逐部位装甲厚度

| 部位 | 值 | 来源与原句 |
|---|---|---|
| 舷侧装甲带（belt） | **80 mm** | [KB]："Armour: belt 80 mm" |
| 舷侧装甲带（区间） | 80 – 40 mm | [navypedia]："Armour, mm belt: 80 - 40" |
| 炮塔 | **70–160 mm** | [KB]："turrets 70-160 mm" |
| 炮塔（区间） | 160 – 50 mm | [navypedia]："turrets: 160 - 50" |
| 炮塔（german-navy） | **70–105 mm** | [german-navy]："Turrets 70 - 105 mm" |
| 炮座（barbette） | **80 mm** | [KB]："barbettes 80 mm"；[navypedia]："barbettes: 80" |
| 上甲板 | **30 mm** | [KB]："upper deck 30 mm" |
| 装甲甲板 | **30 mm** | [KB]："armour deck 30 mm" |
| 装甲甲板（navypedia 详细） | 30 mm 主甲板 + 50 mm 斜坡（connecting slope），citadel 外增至 40 mm | [navypedia]："30mm main deck was connected with lower edge of main belt by 50mm slopes, thickness of this deck increased to 40mm outside citadel. There was 30mm upper deck." |
| 司令塔（CT） | **150 mm** | [KB]："conning tower 150 mm" |
| 司令塔（区间） | 150 – 50 mm | [navypedia]："CT: 150 - 50" |
| 横向舱壁 | 80 mm | [navypedia]："bulkheads: 80" |
| 防雷纵舱壁 | **20 mm** | [KB]："torpedo bulkhead 20 mm"；[navypedia]："anti-torpedo bulkhead: 20" |

**【分歧】炮塔正面**：KB 70–160 / navypedia 160–50 / german-navy 70–105 / naval-encyclopedia 对本舰单列 "Same but turret faces: 105 mm"。**four 源四种，全部并列。** 其中 naval-encyclopedia 的 105 mm 与 german-navy 的 105 吻合，可能指改进批的正面减薄（与首批 160 mm 相对）。

### 5.2 装甲方案（navypedia 逐段原文，唯一按部位组织的来源）

> "Armoured belt with 2.75m height and 80mm thickness was fitted raked at 12.5° outside, covering about 70% of hull length, and closed by 80mm transverse bulkheads. In an fore part the belt had 3.85m height and 40mm thickness, tapering at stem to 20mm; in aft part, respectively, it was 2.75m and 70mm, ..." — [navypedia](https://www.navypedia.org/ships/germany/ger_cr_hipper.htm)

> "12.5°-inclined main belt between inner barbettes was 3.75m high and 80mm thick. It was closed by 80mm bulkheads. Thickness of fore 3.85m high belt was 40mm, decreasing to 20mm fwd from "A" barbette; 2.75m-high belt with 70mm thickness protected aft part of ship and was closed by 70mm aft bulkhead of steering gear compartment. ... Turrets had 160mm faces (with 105mm inclined parts), 70mm sides (with 80mm inclined parts) and 80mm roofs, barbettes had 80mm armor. CT had 150mm sides and 50mm roof. Underwater protection consisted of bulges and 20mm longitudinal bulkhead." — 同上

注意 navypedia 这段是**本级通述**，它自己在 Project history 段说本舰「internal arrangement 有差异」，所以这段能否直接用作本舰值，**存疑**。本文只把它作为舰级参考（见 `hipper-class.md` §5），本舰逐段值标注「按舰级通述推得，本舰未单独核实」。

### 5.3 水下防护

> "Underwater protection consisted of bulges and 20mm longitudinal bulkhead." — [navypedia]

> "There was a double bottom extending for 72 percent of the keel. There was also the usual sub-compartmentation system below the armor belt ... But nothing revolutionary or quite capable to defeat one or two torpedo hit on places. They were still vulnerable." — [naval-encyclopedia]

【实测反证】本舰 1942-02-23 被一条 21 英寸鱼雷命中艉部即**整段艉部（含舵）被切断**：

> "The damage is severe, the rudder is lost, and 50 men lose their lives, but she manages to reach Trondheim by her own power" — [KB](https://www.kbismarck.com/prinzeugen.html)

> "After the removal of 40 feet of her stern and the installation of two temporary rudders" — [DANFS](https://web.archive.org/web/2023id_/https://www.history.navy.mil/research/histories/ship-histories/danfs/p/prinz-eugen.html)

**这不是防护不足的证据，而是「艉部本来就没有防雷纵深」的实例**——写页面时别把它写成装甲评价。

### 5.4 装甲总重

**未获取。** 所有可用来源都只给厚度，不给 armor weight。`data/fields.yaml` 里的 `protection.armor.weight` 本舰无值。

---

## 6. 航空设施

| 项目 | 值 | 来源 |
|---|---|---|
| 水上飞机 | **3 × Arado Ar 196** | [KB]："Seaplanes: 3 x Arado ar 196."；[german-navy]："Arado Ar 196 3" |
| 弹射器 | 1 座 | [navypedia]（本级）："1 catapult, 3 seaplanes (He 60, He114, Ar196)" |
| 机库 | 1 座，可容纳 2 架（机翼折叠并排），**库顶为伸缩式** | [naval-encyclopedia]："tailored to carry and operate three floatplanes, with a catapult (type to find) and a hangar below, large enough to accomodate two of them, wings folded side by side. **The roof of this hangar was telescopic.**" |
| 机库尺寸 | **未获取** | — |
| 弹射器型号 | **未获取**（naval-encyclopedia 自己写 "type to find"） | — |
| 载机数（**分歧**） | 有来源称可载 4 架 | [naval-encyclopedia]："several sources points out the Prinz Eugen class as being able to carry four floatplane, not three" |

**实战使用记录（KTB 独家）**：1944-08-20 对 Tuckum 岸轰时三架全用上了——

> "All three ship-borne Arado seaplanes are used to observe the fall of shot." — [KB](https://www.kbismarck.com/prinzeugen.html)

这证明「3 架」是实际编制而非纸面数。

---

## 7. 武备

### 7.1 主炮：20.3 cm SK C/34（4 × 双联）

**装舰与炮塔型号**：

> "Two-gun turrets / Admiral Hipper (4) and Prinz Eugen (4): **LC/34**" — [NavWeaps 20.3 cm/60 SK C/34](https://www.navweaps.com/Weapons/WNGER_8-60_skc34.php)

**炮本身**（[NavWeaps]，C 级）：

| 项目 | 值 | 原句 |
|---|---|---|
| 口径 | 20.3 cm（实径 20.30 cm / 7.992"） | "Actual bore diameter was 20.30 cm (7.992")." |
| 身管长（全长） | 12.150 m | "Gun Length oa 478.4 in (12.150 m)" |
| 膛线长 | 9.527 m | "Rifling Length 375.1 in (9.527 m)" |
| 炮身重 | 20,700 kg | "Gun Weight 45,636 lb. (20,700 kg)" |
| 射速 | 4–5 发/分 | "Rate Of Fire 4 - 5 rounds per minute" |
| 初速 | 925 m/s | "Muzzle Velocity All except illum: 3,035 fps (925 mps)" |
| 身管寿命 | 300 发（一说 500） | "Approximate Barrel Life 300 rounds (one source says 500 rounds)" |
| 每炮备弹 | 120 发（设计） | "Ammunition stowage per gun 120 rounds" |
| 备弹（**分歧**） | 120–160 发 | "'German Warships 1815-1945' says that the actual outfit per gun ranged from 120 to 160 rounds." |
| 备弹（1940 总量） | 320 APC + 320 HE Bdz + 320 HE Kz + 每弹库 40 照明 | "'German Naval Guns 1939 - 1945' says that in 1940 the total outfit was 320 APC, 320 HE base fuse and 320 HE nose fuze. In addition, "B" and "C" magazines each held 40 starshell." |
| 备弹（1944 总量） | 1,470 发（以 HE 为主）+ 40 照明 | "'Warship Pictorial #21' says that in 1944 the total outfit was 1,470 shells of mostly HE plus 40 starshells." |

**炮塔**（[NavWeaps]）：

| 项目 | 值 | 原句 |
|---|---|---|
| A、D 塔重 | 249,000 kg | "Turrets "A" and "D": 548,951 lbs. (249,000 kg)" |
| B、C 塔重 | 262,000 kg | "Turrets "B" and "C": 577,611 lbs. (262,000 kg)" |
| 俯仰（A 塔） | **−9 / +37°** | "Turret "A": -9 / +37 degrees" |
| 俯仰（B/C/D 塔） | −10 / +37° | "Turrets "B", "C" and "D": -10 / +37 degrees" |
| 俯仰速率 | 8°/s | "Elevation Rate 8 degrees per second" |
| 回旋 | ±145° | "Train +145 / -145 degrees" |
| 回旋速率 | 6–8°/s | "Train Rate 6 - 8 degrees per second" |
| 后座行程 | 62.5 cm | "Gun recoil 24.6 in (62.5 cm)" |
| 装填角 | +3° | "Loading Angle +3 degrees" |
| 炮间距 | 216 cm | "Distance between gun axes was 85.0 in (216 cm)." |
| 塔员 | A/D 各 72 人；B/C 各加 4 名测距手 | "Turrets "A" and "D" each had 72 crewmen. Turrets "B" and "C" each had an additional four men who operated the rangefinders." |

【注意】A 塔负俯仰受舰艏舷弧限制——"Negative elevation for "A" turret was limited by the shear of the bow." 这是本舰 1944 年照片里 A 塔前有两具扫雷具（paravanes）挂在炮座上的几何原因之一，写图注时可引。

**弹重与弹种**（[NavWeaps]）：

| 弹种 | 德文原名 | 重 | 装药 |
|---|---|---|---|
| APC | 20.3 cm Psgr. L/4,4 (m.Hb) | 122 kg | 2.950 kg (G) / 2.648 kg TNT (S) |
| HE 底榴 | 20.3 cm Spgr. L/4,7 Bdz (m.Hb) | 122 kg | 5.650 / 5.349 kg |
| HE 头榴 | 20.3 cm Spgr. L/4,7 Kz (m.Hb) | 122 kg | 9.445 / 8.884 kg |
| HE 头榴防空型 | 20.3 cm Spgr. L/4,7 Kz (m.Hb) – Haube abgeschraubt | 约 120 kg | 同上 |
| HE 燃烧 | 20.3 cm Spgr. L/4,7 Kz (m.Hb) Br | 124 kg | 2.820 kg TNT + 6.064 kg 燃烧剂 |
| 照明 | 20.3 cm Lg. L/4,5 | 103 kg | — |

【项目内对照】`kb-ds` 脚注给的三种弹装药是 2.30 / 6.54 / 8.93 kg（与 NavWeaps 的 2.95 / 5.65 / 9.445 不同）。**两源两种口径，并列**——这影响「PG 打不打得穿胡德」的定量讨论，见 §11.4。

**弹道表**（[NavWeaps]，本舰无单独核实，为炮本身数据）：

| 仰角 | 射程 | 存速 | 落角 | 飞行时间 |
|---|---|---|---|---|
| 1.9° | 5,000 m | 744 m/s | 2.1° | 6.0 s |
| 4.4° | 10,000 m | 587 m/s | 6.1° | 13.6 s |
| 8.1° | 15,000 m | 463 m/s | 12.8° | 23.4 s |
| 13.3° | 20,000 m | 382 m/s | 23.6° | 35.9 s |
| 20.3° | 25,000 m | 353 m/s | 36.8° | 51.1 s |
| 29.1° | 30,000 m | 363 m/s | 48.8° | 69.0 s |
| 37.0° | 33,500 m | — | — | — |

**穿深**（[NavWeaps]）：

> "Armor Penetration with Psgr. L/4,4 (m.Hb): 10,400 yards (9,500 m) → 9.4" (24 cm) of Face-hardened Armor; 20,000 yards (18,300 m) → 3.9" (10 cm) of Face-hardened Armor"

> "Armor Penetration with Spgr. L/4,7 Kz (m.Hb): 10,389 yards (9,500 m) → 2.0" (5 cm) of Homogeneous Armor"

**20,000 m（丹麦海峡实际交战距离）处 APC 对表面硬化装甲的穿深只有 10 cm。** 这是 §11.4 定量讨论的物理基础，与 `hood-sinking.md` 引 Jurens 的「Hood 最薄的上装带也厚于 10 cm」完全一致，两条独立来源互相印证。

### 7.2 副炮/高炮：10.5 cm SK C/33（6 × 双联）

| 项目 | 值 | 原句与来源 |
|---|---|---|
| 数量 | 12 门 / 6 座双联 | [KB]："12 x 10.5cm SK C/33 guns in six double mounts." |
| 炮座型号 | **Dop. L. C/31d** | [NavWeaps 10.5 cm/65](https://www.navweaps.com/Weapons/WNGER_41-65_skc33.php)："Admiral Hipper (6) and Prinz Eugen (6) 5b: Dop. L. C/31d" |
| 炮座重量 | 27,350 kg | 同页："Dop. L. C/31d: 60,300 lbs. (27,350 kg)" |
| 俯仰 | −8 / +80° | 同页："Dop. L. C/31, Dop. L. C/31gE and Dop. L. C/31d: -8 / +80 degrees" |
| 备弹（本舰） | **420 发** | 同页："Admiral Hipper and Prinz Eugen: 420 rounds" |
| 备弹（**分歧**） | 400 发 | 同页："... 420 rounds and that for Admiral Hipper was 400 rounds." |
| 三轴稳定 | 有（电动） | 同页（配图说明）："10.5 cm/65 SK C/33 guns in Dop. L. C/31 Twin Mounting showing the triaxial motion." |
| 炮座型号（**分歧**） | 可能为 C/37 | 同页："Koop and Klaus-Peter Schmolke state that Prinz Eugen may have had Dop. L. C/37 mounts. However, ..." |

### 7.3 轻高炮

| 项目 | 值 | 来源 |
|---|---|---|
| 3.7 cm SK C/30 | **12 门 / 6 座双联** | [KB]："12 x 3.7cm SK C/30 guns in six double mounts." |
| 3.7 cm 炮座型号 | 双联 LC/30 | [NavWeaps 3.7 cm](https://www.navweaps.com/Weapons/WNGER_37mm-83_skc30.php)："Graf Zepplin (11), Bismarck (8), Admiral Hipper (6), Prinz Eugen (6)" |
| 3.7 cm 备弹 | 单装座 7,000 发 / 双联座 1,500 发 | 同页："Admiral Hipper and Prinz Eugen - single: 7,000 rounds / Admiral Hipper and Prinz Eugen - twin: 1,500 rounds" |
| 2 cm | **28 门** | [KB]："28 x 2cm guns" |
| 2 cm（**分歧**） | 32 门 | [german-navy]："2 cm MG L/64 32" |
| 2 cm（**分歧·按年份**） | 1941 初：10 门单装 C/38；1941 后：+4 座 Flakvierling；1945：18 门 | [naval-encyclopedia]："KMS Prinz Eugen had six twin 37mm/80 SK C/30, and ten single 20mm/65 C/38 AA guns plus two FuMo27 radars. Later in 1941 she received four Flakvierling 20mm/65 C/38..." / "In 1945, she had twenty 4 cm guns, eighteen 2 cm guns" |
| 4 cm Flak 28（1944 起） | 1944：6 门；1945：12 门或 20 门（两说） | [naval-encyclopedia]："In 1944, Prinz Eugen's remaining 3.7 cm guns were all replaced by fifteen 4 cm (1.6 in) Flak 28 guns" / "In 1945, she had twenty 4 cm guns"；[german-navy]："4 cm Flak 17" |

**轻高炮是本舰最不能取单一值的字段**：三份来源给的数（28 / 32 / 17+28）分属不同年份，且 naval-encyclopedia 自己内部就有 1944=15 门与 1944=6 门两处不一致。**按年份分条登记，不给单值。**

### 7.4 鱼雷

| 项目 | 值 | 来源 |
|---|---|---|
| 数量 | **12 具 / 4 座三联** | [KB]："12 x 53.3cm torpedo tubes in four triple mounts." |
| 口径 | 53.3 cm | 同上 |
| 备雷 | 24 条（12 装管 + 12 备） | [naval-encyclopedia]（本级）："the cruisers carried twenty-four G7a torpedoes so twelve loaded in the tubes, and the same ready reload" |
| 型号 | G7a | 同上 |

**【本舰专属·重要】丹麦海峡一雷未发。** 这是德军战后专门出了一份 OKM 文件调查的事故（`T Wa Ib B. Nr. 2386/41 g.Kdos.`，1941-10-03），KB 全文收录：

> "Im Seegefecht bei Grönland am 24.5.1941 ist die Torpedowaffe vom Kreuzer "Prinz Eugen" **nicht eingesetzt worden**." — [kbismarck/torpedowaffe-pg](https://www.kbismarck.com/torpedowaffe-pg.html)

官方结论（不是「技术故障」，是「人」）：

> "Für den Nichteinsatz der Waffe wird jetzt sowohl vom Kommando als auch von B.d.K. und Flotte allein die ungenügende Ausbildung des T.O. und seines Personals verantwortlich gemacht."

即：**鱼雷官与鱼雷部门训练不足**，且火控雷达分配不当（"Auf "Prinz Eugen" waren zu Anfang des Gefechtes alle E-Geräte bzgl. der Zielanweisung auf Artillerie geschaltet."）。舰长 Brinkmann 事后在 1941-07-17 呈文里撤回了「鱼雷射击指挥仪反应太慢」的说法。

**这条必须写进页面**：本舰是全舰唯一在丹麦海峡全程「主炮开火、鱼雷哑火」的主力舰，且原因是训练与雷达分配，不是装备故障。中文资料普遍漏掉这一条。

### 7.5 深水炸弹

| 来源 | 值 |
|---|---|
| [KB] | "2 x triple depth charge racks."（2 座三联深弹架） |
| [KB/Hipper] | "6 x depth charge launchers." |
| [Bonomi] | 证本舰在丹麦海峡确实用了深弹：从战前战后照片看深弹数从 3 减到 1——"Evidence from photos of the Prinz Eugen stern before and after the battle demonstrate the utilization of the depth charges during the engagement as the charges went from 3 to 1."（脚注 26） |

**【说明】** 深弹在这里不是反潜武器而是**当作烟幕/干扰手段在炮战中使用**，这是德舰 1941 年的实际做法，Bonomi 的脚注是唯一解释为什么炮战里会掉深弹的来源。**深弹架数量两页不一致（2 vs 6），并列。**

---

## 8. 雷达与火控

### 8.1 雷达装备（按年份）

| 时间 | 装备 | 来源与原句 |
|---|---|---|
| 1941（丹麦海峡） | **2 × FuMO 27** | [KB]："In 1941: 2 x FuMO 27." |
| 1941-02 升级 | FuMO 26 + FuMB 4 Sumatra + FuMB 7 Timor | [naval-encyclopedia]："In February 1942, she obtained a new state of the art equipment, comprising the FuMO 26 radar, FuMB4 Sumatra, and FuMB 7 Timor ECM suites." |
| 1944 升级 | FuMO 25 + FuMO 81 + FuMB 3 Bali + FuME 2 Wespe-G | 同页："In 1944, this was upgraded to the FuMO 25, FuMO 81 radars, FuMB3 Bali, and FuME 2 Wespe-G ECM suites, kept until she was captured in 1945." |
| 1945（KB 口径） | 1 × FuMO 26, 1 × FuMO 81 "Berlin", 1 × FuMO 25, 1 × FuMO 27 | [KB]："In 1945: 1 x FuMO 26, 1 x FuMO 81 "Berlin", 1 x FuMO 25, 1 x FuMO 27." |

**【分歧】** naval-encyclopedia 说 1942 年 2 月装 FuMO **26**；KB 说 1941 年就是 **FuMO 27 ×2**、1945 年四型并存。两岸都保留了 27，但 1942 升级型号一说是 26（naval-encyclopedia）——不冲突（26 与 27 可以并存），但 KB 说 1941 年就有 2 台 27、1945 年还有 1 台 27，则「1942 年才获得 FuMO 26」这句需要理解为「新增」。

**KTB 的直接证据**：1941-04-16 试航时本舰前桅楼 FuMO 27 能在夜间探测到半潜状态的潜艇 6,000–7,000 m（§2.4 已引）。

### 8.2 雷达代号问题——德方档案里叫 "EM II"，不叫 FuMO

这是读德方原文时最容易踩的坑：KTB 通篇用 **EM II**（*Funkmessgerät* 的旧代号体系）而不是 FuMO：

> "Ab 0228 übernimmt "Prinz Eugen" die EM II-Messung auch für den achteren Sektor, da die Bismarck-..." / "As of 0228 "Prinz Eugen" takes over the radar range finder measurements also for [both ships'] stern [sector]" — KTB

> "The radar [EM II], which failed often on Bismarck, did not improve the situation" — KTB

**因此「本舰 1941 年装的雷达」在德方档案里的名字是 EM II，Bundesarchiv 检索用这个词，用 FuMO 搜不到。** 这条对下次查档案很关键。

### 8.3 火控

| 项目 | 值 | 来源 |
|---|---|---|
| 主炮测距仪 | **5 × 7-m 基线** | [KB]："Fire control: 5 x 7-m base rangefinders."（KB 对 Hipper 页同句，逐字相同，见 §3.4 的复制疑虑） |
| 主炮指挥仪 | 前桅楼 + 后部站位（可互换） | [KTB·Jasper]："I gave the order to transfer fire control to Oberleutnant zur See z.V Albrecht in the aft gunnery position"（KTB 第 40 页） |
| 高炮指挥仪 | 三轴稳定 | [NavWeaps 10.5]："showing the triaxial motion" |
| 主炮齐射周期 | **27–28 秒**（实测） | [KTB·Jasper]："The heavy artillery attained a salvo rate of fire of **27-28 seconds**."（KTB 第 41 页） |

**【实测·独家】27–28 秒的齐射周期是本舰唯一一条实测射击循环数据**，比 NavWeaps 的「4–5 发/分」理论值（=12–15 秒/发）低得多——因为那是单管射速，而这里是全炮塔组齐射间隔。两者不矛盾，但**不能互相替代**。

### 8.4 电子战（ECM）

本舰是**轴心国重巡里电子设备最全的一艘**：

> "This was the most extensive and sophisticated electronics suite of any axis cruiser of WW2 and thus, under US custody this was examined in great detail." — [naval-encyclopedia](https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php)

战后美方评价（同一段）：

> "The most striking piece of equipment that was studied in detail was of course the top end fire control systems, optics and radar of the ship. She had the best combination possible at the time, worthy of a battleship."

【注意】这两句是 D 级来源的评价性文字，**不能当 fact 的 src**，只能作 narrative 证据。

---

## 9. 编制

| 值 | 来源与原句 |
|---|---|
| **1,600** | [KB]："Crew: 1,600." |
| ~1600 | [german-navy]："Crew ~1600" |
| ~1600 | [navypedia]："Complement 1600" |
| **42 名军官 + 1,240 名士兵（= 1,282）** | [naval-encyclopedia]："Crew 42 officers, 1240 ratings" |
| **830**（1946 年美军队编制） | [DANFS]："cpl. 830" |

**【分歧】** 1,600 ×3 vs 1,282 ×1 vs 830（美方）。1,282 与 1,600 差 318 人，**可能是「平时编制 vs 战时编制」**，但没有任何来源这样说。830 是 1946 年美军接舰后的编制，**不是德方编制**，不可当德方值。

**军官/士官/水兵三级细分：未获取。** 与 `bismarck-tech-sources.md` 的结论一致——德舰来源普遍只给两级或单一总数。

---

## 10. 涂装

### 10.1 波罗的海斜条纹迷彩 —— 两舰都有，且同一天被涂掉

这是任务书特别提醒「别搞混」的一点，实测结论是：**任务书的提醒是对的，两舰确实都有，而且是同一天、同一个地点、同一道命令涂掉的。**

**本舰战争日志原文（1941-05-21，挪威 Korsfjord）**：

> "Während des Einlaufens und Liegens im Kors-Fjord wurde die gesamte Tarnbemalung mit Außenbordsgrau auf Befehl Flotte übermalt."
> "While running into and lying in Korsfjord **the entire camouflage was painted over with outboard gray by orders from Fleet**." — KTB 第 11 页

**同一事件的 kbismarck 叙述（两舰并列）**：

> "During their brief stay anchored in Norway, the **Bismarck and the Prinz Eugen** painted over their striped camouflage paint with outboard grey." — [kbismarck/operheini](https://www.kbismarck.com/operheini.html)

**俾斯麦侧的条纹描述（可作本舰的形态参照，但注意主语是俾斯麦）**：

> "This included **three angled black and white stripes over the hull and superstructure, with the ship's ends in dark grey and false white waves**." — [kbismarck/drawings](https://www.kbismarck.com/drawings.html)

> "The black and white stripes of the hull were painted over while in Korsfjord on 21 May 1941." — [kbismarck/24-may-drawing](https://www.kbismarck.com/24-may-drawing.html)

**出发前舰队命令里也提到了迷彩的处理原则**（KTB 第 5 页，1941-05-18 作战命令摘录）：

> "7.) Tarnfarbanstrich bleibt b.a.w. Befehl folgt. Für evtl. längeren Aufenthalt in Norwegen (Drontheim) bunten Tarnanstrich bereithalten."
> "7. Camouflage will remain as is until further notice. Order to follow. For a potentially longer layover in Norway (Trondheim) keep colored camouflage [well] maintained."

### 10.2 本舰涂装的**未获取**部分（必须如实写）

| 项目 | 状态 |
|---|---|
| 本舰条纹的**具体条数** | **未获取**。三条规定只对俾斯麦明确（"three angled black and white stripes"），本舰无任何来源给条数 |
| 本舰条纹的**角度/位置** | **未获取** |
| 本舰条纹的**黑白比例与色号** | **未获取** |
| 本舰改涂舷外灰后的**具体色号** | **未获取**（俾斯麦有 RAL 7000/7001/7024/7016/9006/8013 六色清单 [kbismarck/24-may-drawing]，本舰无对应清单） |
| 本舰 1942/1944/1945 各期涂装 | **未获取** |

**这是本舰与俾斯麦最大的资料落差**：俾斯麦有 kbismarck 专门做的涂装线图页 + 六色 RAL 清单；本舰只有「有过条纹、5 月 21 日涂掉了」这两条硬事实。

**试过但未取得的涂装专项来源**（见 §15）：`kbismarck.com/camouflage.html` 404、`kbismarck.com/bismarck-camouflage.html` 404、`navweaps.com` 的迷彩综述页只有俾斯麦没有本舰。

【一条可用的旁证】项目 `data/images.yaml` 第 297 行的图注（俾斯麦在 Grimstadfjord 那张，从本舰拍摄）写着「舰体仍可见波罗的海斜条纹迷彩，与 1941-05-21 改涂舷外灰的记载同日」——**那张照片拍的是俾斯麦，不是本舰**，但它确实是 5 月 21 日从本舰舰上拍的。写图注时要分清「拍摄者」与「被摄者」。

---

## 11. 丹麦海峡（1941-05-24）—— 本舰最重要的一节

### 11.1 ⚠️ 先说一个会毁掉整份时间线的问题：KTB 里的时间基准有两套

**这是本次调研最重要的方法论发现，比任何一个数值都重要。**

Prinz Eugen 的战争日志里同时存在两套时间：

- **KTB 正文时间轴用 DSZ（德国夏令时，Deutsche Sommerzeit = UTC+2）**；
- **Jasper 的炮术官报告用 MEZ（中欧时间 = UTC+1）**。

证据是三组一一对应的成对事件（相差整 1 小时）：

| 事件 | KTB 正文 | Jasper 报告 |
|---|---|---|
| 开火 | "0555 wird das Feuer von "Prinz Eugen" und "Bismarck" erwiedert" | "I received "permission to fire" from the bridge at **0455** hours" |
| 停火 | "0609 Fires last salvo at Prince of Wales"（KB 转述） | "**Firing ceased at 0509 hours.**" |

且 KTB 自己在 1941-05-23 13:00 有条明确记录：

> "Auf Befehl Flotte Schiffsuhren um 1 Stunde auf MEZ [Mitteleuropäische Zeit] zurückgestellt." / "According to Fleet order: set back ship's clocks 1 hour to CET [Central European Time]." — KTB 第 16 页

kbismarck 在丹麦海峡页脚注里也对同一现象做了换算：

> "0601 hours German Summer Time. 0501 hours Central European Time (set on board the German ships)." — [kbismarck/denmark-strait](https://www.kbismarck.com/denmark-strait-battle.html)

**【实操结论】**
1. 项目 `data/battles/denmark-strait.yaml` 用的 05:52–06:13 是 **DSZ**，与 KTB 正文、kbismarck、Bonomi 一致，**没错，不要改**。
2. 引用 Jasper 炮术报告的任何时刻，**必须加 1 小时**才能与项目时间轴对齐。他的「0455 开火」「0509 停火」直接抄进页面就会差一小时。
3. 英方时间（Hood / PoW 记录）也是另一套（GMT/当地时），`hooddenmark2` 的 note 已提醒「分钟级时间戳相对可靠、绝对有误差」。**三套时间不能混排。**

### 11.2 本舰在战斗中的实际角色

**队位：本舰在俾斯麦前方。** 这一点 KTB 从头到尾一致：

> "We were advancing at the front of the battle-line, with Bismarck behind us." — KTB 第 38 页，Jasper 炮术报告

> "Prinz Eugen positions himself according to Fleet order in front of Bismarck." — KTB 第 18 页（1941-05-23 20:44 换位条）

**为什么换位**：德舰在 23 日夜间调换了队位，目的是给后方的俾斯麦留出射界。KTB 记录得很直白：

> "They were located by Prinz Eugen using sound and radar bearings and reported to Bismarck, since **Fleet had exchanged numbers [order of position] to gain a clear field of fire abaft**." — KTB 第 35 页

**这个换位直接造成了英方的误判。** Bonomi 的分析：

> "the German ships profile at great distance were very similar, they had not noticed that the leading ship was not the Bismarck but the Prinz Eugen. Consequently, Admiral Holland, at 05:49, signalled to the Prince of Wales "G.S.B. 337 L1" that means engage the first ship on the left of the enemy formation bearing 337°, which was the Prinz Eugen." — [Bonomi, PDF 第 4 页](https://www.kbismarck.com/ds-barticle.pdf)

**德方自己的判断也错了一轮**：本舰炮术官一开始把英舰当成重巡，因此选了高爆弹而不是穿甲弹：

> "I did not recognize the opponents as battleships, and until the conclusion [of the battle] I considered them as being cruisers (under consideration, according to my memory or experience "Exeter", "Birmingham", or "Fiji" Class). Accordingly, I decided to use high explosive base-fuzed shells." — KTB 第 38–39 页

> "The 1st Artillery Officer ... had counted on engaging a **10,000-ton** opponent and had therefore selected base fused shells." — KTB 第 35 页

【关键】这个「错」反而对：**122 kg 的高爆弹打胡德的薄装甲上层建筑比穿甲弹更有效**（穿甲弹打不穿战列巡洋舰的主装，高爆弹能烧上层建筑）。kbismarck 的脚注明说：

> "Korvettenkapitän Paulus Jasper choice proved to be correct in the end, since 20.3 cm armour piercing shells (Psrg. L/4,4) would not have been effective against heavily armoured ships such as Hood and Prince of Wales. 20.3 cm high explosive shells (Spgr. L/4,7) were much more adequate to destroy un-armoured superstructures and other light equipment on decks." — [kbismarck/denmark-strait 脚注 1](https://www.kbismarck.com/denmark-strait-battle.html)

### 11.3 炮击记录

#### 11.3.1 发射弹数——**三个数字，无法合并**

| 数字 | 口径 | 来源与原句 |
|---|---|---|
| **157 发 20.3 cm**（8 发 Kz 头榴 + 149 发 Bdz 底榴） | Jasper 炮术官报告的**逐弹种实发统计** | KTB 第 41 页："We had expended: Heavy artillery: **8 rounds of nose fuzed shells, 149 base fuzed shells**, heavy [10.5cm] antiaircraft guns: against naval [surface] targets 78 with nose fuzed shells, against air targets 31 with delayed detonators." |
| **179 发** | 舰长 KTB 总结段 | KTB 第 35 页："By that time **PG had fired 179 rounds**." |
| **183 发** | NavWeaps 的叙述 | [NavWeaps 20.3 cm](https://www.navweaps.com/Weapons/WNGER_8-60_skc34.php)："During the entire Denmark Strait battle, Prinz Eugen fired a total of **183 shells**, hitting HMS Hood at least once and HMS Prince of Wales three times." |
| 157 / 184 可能 | 维基（tier E，仅线索） | `hood-sinking.md` 引 WIKI-DS:760："Total 184 possible shots, Actually fired 157" |

**这是本舰最硬的一个内部矛盾**：同一份 KTB 里，炮术官的实发统计（157）与舰长总结（179）差 22 发，NavWeaps 又给 183。

三种可能（**均为推测，不入库**）：
1. 157 只统计主炮对海射击，179 含对空/对艇射击；
2. Jasper 的 149 是「底榴」而 8 是「头榴」，可能有第三种弹未列；
3. 179 是估计数，157 是事后清点。

**没有任何来源解释这个差额。** 页面应写「157（炮术官实发统计）/ 179（战报总结）/ 183（NavWeaps）三说并列」，**不要挑一个**。

同段还有 10.5 cm 的实发数：**对海 78 发 + 对空 31 发 = 109 发**（Jasper 报告）。KB 的生涯页另给「66 x 10.5 cm」：

> "179 x 20.3 cm and **66 x 10.5 cm** projectiles expended." — [KB/prinzeugen](https://www.kbismarck.com/prinzeugen.html)

**66 vs 109 又冲突。** 并列。

#### 11.3.2 命中记录

| 目标 | 命中数 | 来源与原句 |
|---|---|---|
| Hood | **至少 1 发（起火的那一发）** | KTB 第 20 页："After the impact at 0557 of the 2nd salvo from "Prinz Eugen," a rapidly spreading fire at the level of the aft mast was observed, apparently involving the aircraft hangar or petrol storage [gasoline]." |
| Hood | 至少 1 发 | [NavWeaps]："hitting HMS Hood at least once" |
| Hood | 「至少一次命中」 | [KB/prinzeugen]："obtains at least one hit on the British battlecruiser" |
| Prince of Wales | **3 发** | [NavWeaps]："and HMS Prince of Wales three times" |
| Prince of Wales | 「另外三发」 | [KB/prinzeugen]："Afterwards obtains three more hits on the battleship Prince of Wales." |
| Prince of Wales | **3 发** | [Bonomi]："the Prince of Wales had received 7 hits (4 from Bismarck and 3 from Prinz Eugen)" |
| Prince of Wales | **4 发**（**分歧**） | [Bonomi] 另一处："which she got 7 hits (**3 from Bismarck and 4 from Prinz Eugen**)" |
| Prince of Wales | 本舰自己观察到 2 发「确定」 | KTB 第 20 页："Artillery is well on target. **2 hits are certainly observed.** A small fire."（0559，换目标后首次评估） |

**【分歧·重要】** 同一篇 Bonomi 文章里，「7 发命中」的归属前后不一致：正文前半段写 3 俾斯麦 + **4 欧根**，同文后半段写 4 俾斯麦 + **3 欧根**。这是文章自身的笔误，**不能取其一**。（原句见上表最后两行；核对时按 `ds-barticle.txt` 搜索 "7 hits" 可定位到这两处。）

**本舰自己的观察记录与「3 发」也有落差。** 一炮术官 Jasper（主炮指挥位）看到的是「两次舷侧命中」，但他紧接着注明那两发是俾斯麦的副炮也在打同一目标：

> "During the completion of ranging fire's effectiveness, I observed two well-placed simultaneous portside strikes which again were fired by the secondary artillery of the "Bismarck"." — KTB 第 39 页（Jasper 报告）

注意这句的歧义：德文原文 "beide wieder Bb.-gleichzeitig von der Mittelartillerie des "Bismarck" beschossen" 可以是「两发命中，同时俾斯麦的副炮也在打该目标（掩护良好）」，也可以是「两发命中其实是俾斯麦副炮打的」。**英译本就带这个歧义，我不裁决。**

而二炮术官 Schmalenbach（主高炮战斗位，观察角完全不同）**明说自己也分不清是谁打中的**：

> "I cannot judge who [Bismarck or Prinz Eugen] made these hits because I had turned my attention to the portside heavy flak battery's operations" — KTB 第 47 页（Schmalenbach 报告）

**所以「本舰命中 PoW 三发」这个数字，来源是 NavWeaps / KB / Bonomi 的战果统计，不是本舰任何一位炮术军官的确认。** 页面写的时候要把这层分清——这是本节最容易被下游误用的一处。

### 11.4 「谁打沉了胡德」—— 核心争议

#### 11.4.1 先对齐项目已有立场（不另开新说）

`work/raw/hood-sinking.md` §争议二 的结论是：

> **主流：PG 能打伤、不能打死。** 20.3 cm 的理论穿深差得太远，不是「概率低」而是「机制上不通」。

支撑三条：①时间线（KB 脚注 3：0600 时 PG 已在打 PoW）；②穿深不足（Jurens 定量）；③弹种（PG 打的是 HE 不是 AP）。

**本文完全接受这个框架，只补本舰侧的一手证据。**

#### 11.4.2 本舰一手档案怎么说的（新增证据，A/B 级）

**（a）本舰 KTB 把致命爆炸明确记在俾斯麦名下，且与自己那一发分开记：**

> "0557 ... After the impact at 0557 of the 2nd salvo from "Prinz Eugen," a rapidly spreading fire at the level of the aft mast was observed, apparently involving the aircraft hangar or petrol storage."
> "0601 20 ... an extraordinarily violent detonation aboard "Hood". A high pillar of metal debris is becoming visible." — KTB 第 21 页
**两件事在日志里是分开的两条，间隔约 4 分 20 秒。** 这是德方自己的记录，不是事后辩解。

**（b）炮术官 Jasper 明说他**没看见**俾斯麦那一致命齐射，因为已经换了目标：**

> "I was unable to observe "Bismarck's" decisive salvo because I was no longer in a position to do so. I ordered the targeting officer [target designator] to acquire the second target and thus lost the first [target] from the [range finder's] visual field of action. Consequently, **I did not perceive the detonation of the first target [Hood]**." — KTB 第 39 页

**这段话的分量在于：它同时否掉了「PG 打了致命那发」的可能性和「PG 观察到致命那发」的可能性。** PG 的测距仪在 0557–0558 之间就转走了。

**（c）归因用的是「very probable, nearly certain」而不是确定，而且说这话的是二炮术官 Schmalenbach，不是 Jasper：**

> "A few seconds (3-5) transpired between the salvo's impact and the absolutely instantaneous initiation of the described conflagration. I deem it as **very probable, nearly certain**, that the above mentioned salvo was from Prinz Eugen [and that it] caused the conflagration. A few seconds later, a salvo from Bismarck hit the ship aft, and that resulted in an explosion of massive consequence." — KTB 第 45 页

**【勘误·本文自行纠正】** 我起初把这段当成 Jasper 的话，核对页码后确认是 **Schmalenbach（II.A.O.，第二炮术官）**：KTB 第 43 页起是「Report of the 2nd Artillery Officer」，第 48 页末署 "gez. Schmalenbach, Kaptlt. u. II AO."；Jasper 的报告是第 38–42 页，末署 "gz. Jasper, K.Kapt. u. I A O"。

这个区分不是小事：**它意味着「PG 那一发引起大火」这个判断，是由一个站在主高炮战斗位（而非主炮指挥位）的军官独立作出的目击判断，且他明确说那发之后 3–5 秒才看到俾斯麦的齐射命中。** 两个军官的观察位不同，结论却一致，比一个人说两遍硬得多。

**（d）Schmalenbach 还交代了他为什么敢这么判——他否掉了另一种解释：**

> "Shortly after the impacts of a salvo from Bismarck (I cannot explain it in any other way because of the rapid sequence of impacts on the opponent to the right as well as the change in the color and height of the impacts), a salvo from Prinz Eugen was delivered, which, according to my observations through large binoculars, caused a conflagration in the vicinity of the aft mast." — KTB 第 45 页

即：他先看到俾斯麦一发的落弹、再看到本舰一发的落弹，紧接着后桅处起火，**时间顺序排除了把火归给俾斯麦那发的可能**。这段推理链比结论本身更值得引用。

**（e）Schmalenbach 还留了一条对判断弹道有用的观察：胡德全程只打本舰，没打俾斯麦：**

> "With certainty, I observed that Hood fired only against Prinz Eugen, because this could have been readily recognized, based on the minimal battle distance, if the turrets had been pointed more aft toward Bismarck." — KTB 第 46 页（Schmalenbach 报告）

【注意】这条是**德方单方面的目击**，且与英方证词冲突：`hood-sinking.md` 引 Bonomi 脚注 22 记了四方说法不一（Hood 生还者说打过本舰至少两轮、PoW 舰长 Leach 说换目标命令在开火前就下、德方老兵说 Hood 只打本舰、俾斯麦生还者说 Hood 只打俾斯麦）。**Schmalenbach 这句不能当「胡德没打俾斯麦」的定论，只能当「本舰军官认为胡德全程瞄着自己」。**

#### 11.4.3 支持「PG 打的」的一方说什么

| 主张者 | 说法 | 出处 |
|---|---|---|
| 海军圈流传（未具名） | 「有时有人提出是欧根亲王号打出了对胡德的致命一击」 | [kbismarck/denmark-strait 脚注 3](https://www.kbismarck.com/denmark-strait-battle.html)："It has been sometimes suggested in naval circles that it was the Prinz Eugen the ship that actually scored the fatal hit on the Hood." |
| hmshood.org.uk（英国官方协会） | **起火那一发**（不是致命那发）倾向于判给 PG | `hood-sinking.md` 引 HOOD2："It is widely believed that the hit was from Prinz Eugen rather than Bismarck." |
| naval-encyclopedia | 「她在一定程度上被记功于胡德的爆炸」 | "She fired first and essentially is credited in part for the explosion of the hood. Historians still debates today over the exact nature "killer blow"." |
| Schmalenbach（本舰二炮术官） | 本舰目标就是胡德 | `hood-sinking.md` 引 WIKI-DS:617 |

#### 11.4.4 反对「PG 打的」的一方说什么

| 论据 | 原文 |
|---|---|
| **时间线**：0600 时 PG 已在打 PoW | "the Prinz Eugen could not have been responsible for this hit because at the time the decisive hit occurred (0600 hours) the German cruiser was **firing at Prince of Wales**. PG had shifted fire to POW at about 0557 just after hitting Hood in the shelter deck." — [kbismarck，脚注 3](https://www.kbismarck.com/denmark-strait-battle.html) |
| **穿深**：机制上不通 | "**Prinz Eugen may have been able to hurt the Hood, but she would almost certainly be unable to kill her.**" — Jurens, INRO，转引自 `hood-sinking.md` |
| **弹种**：打的是 HE | "Also keep in mind that **PG was firing HE shells instead of APs**. Prinz Eugen's shells were considerably smaller than those of Bismarck, weighting only 122 kg." — 同上 |
| **德方炮术官本人否认** | Schmalenbach 德文原话：**"Diese Behauptung ist eine reine Erfindung"**（此说纯属虚构），转引自 `hood-sinking.md` |
| **英方当时根本没有 PG 落弹的确凿观察** | Walker 委员会："There is **no very definite evidence of the fall of shot from PRINZ EUGEN**, though one salvo was described as falling astern of HOOD." — ADM116-89:65，转引自 `hood-sinking.md` |

#### 11.4.5 本次新增的一条定量支撑（独立于 Jurens）

NavWeaps 的炮本身穿深表给了一个可以独立验算的数：

> "Armor Penetration with Psgr. L/4,4 (m.Hb): 20,000 yards (18,300 m) → 3.9" (**10 cm**) of Face-hardened Armor" — [NavWeaps](https://www.navweaps.com/Weapons/WNGER_8-60_skc34.php)

丹麦海峡实际交战距离 20,200 m（首齐射）到 14,000 m（最近）。**即便按 18,300 m 算，APC 也只有 10 cm 的均质/表面硬化装甲穿深**；而本舰打的是 HE，穿深更差。这与 Jurens 的「对面装甲板约 40–60 mm、对舷侧 100/103 mm」在数量级上一致。

**两条完全独立的来源（NavWeaps 的德方穿深曲线、Jurens 的弹道重建）得出了同一个量级。这是「PG 打不死胡德」最强的支撑，且不依赖任何一方的叙事。**

#### 11.4.6 本站立场（照 `hood-sinking.md`，不裁决）

**并列呈现，不做结论：**

- **能确定的**：本舰至少命中了胡德 1 发，造成后桅附近的大火（德方三份独立证词：KTB 正文逐时条、Jasper「异常明亮的火光」目击、Schmalenbach 的 3–5 秒时序推理）；这发是 HE。
- **不能确定的**：这发火是否间接导致了 4 分钟后俾斯麦那一发引起的弹药库爆燃。Walker 委员会明确否掉（"the fire… was not the cause of her loss"），但 hmshood 官方站留了口子。
- **基本可以排除的**：本舰那一发**直接**引爆弹药库。三条独立论证（时间线 / 穿深 / 弹种），加本次新增的穿深数量级核验。

**注意与 `hood.yaml` 第 941 行悬空引用的关系**：那句「另见 narrative」目前没有对应条目。若主会话决定补建，本节 11.4.2 的五段原句可以直接作 evidence。

### 11.5 本舰在战斗中未受损伤

四个来源一致：

> "The *Prinz Eugen* was not hit during the battle and remained undamaged, even though some Hood's shells landed close by in the opening phase of the engagement and fragments landed on board." — [kbismarck/denmark-strait](https://www.kbismarck.com/denmark-strait-battle.html)

> "[We] did not experience any damage to ourselves. The battery was fully combat-ready." — KTB 第 41 页

> "Report of the commander [Brinkmann] to the Fleet Chief [Lütjens]: Commander to Admiral. **No damage.**" — KTB 第 21 页（0628）

> "Verluste an Toten, Schwer und Leichtverwundeten sind nicht eingetreten, obwohl an Deck Geschossteile einer 38 cm Granate gefunden wurden." / "Casualties in dead, seriously and lightly wounded did not occur, although shell fragments of a 38 cm [15"] projectile were found on deck." — [KTB 军医报告](https://www.kbismarck.com/pg-medical-report.html)

**但「未受伤」不等于「未被击中威胁」**：本舰被胡德的近失弹夹叉多次，甲板上捡到一块 38 cm 弹片，经弹道鉴定判定来自英王乔治五世级而不是胡德：

> "A piece of shrapnel from a heavy caliber shell was found on the portside boat deck. It showed the telltale marks of two guide rings and was, according to data tables in a technical bulletin on weapons intelligence, **not from the Hood, but it was instead attributed to a ship of the King George class**." — KTB 第 42 页

**这是「威尔士亲王号确实向本舰附近开过火」的物证**，而且是从德方自己的弹道手册判出来的，很硬。

---

## 12. 后续生涯

### 12.1 脱离与赴法（1941-05-24 – 06-01）

| 时间 | 事件 | 原句与来源 |
|---|---|---|
| 1941-05-24 18:14 | 脱离俾斯麦 | [KB]："**1814.** *Prinz Eugen* leaves *Bismarck* and heads south."；KTB 第 23 页同 |
| 1941-05-26 | 从 Spichern 海上加油 | [KB]："Refuels at sea from tanker *Spichern*." |
| 1941-05-28 | 从 Esso Hamburg 加油，**发现三台主机全有严重缺陷** | [KB]："Refuels at sea from tanker *Esso Hamburg*."；[NavWeaps OOB Cerberus](https://www.navweaps.com/index_oob/OOB_WWII_Atlantic/OOB_WWII_Cerberus.php)："Refueled by Esso Hamburg on 28th May, when **Prinz Eugen discovered serious defects in all 3 engines plus a propeller blade chipped by ice in the Denmark Straits**." |
| 1941-06-01 19:30 | 进布列斯特并入坞 | KTB 第 71 页："**1930 Brest** / Brest. Eingelaufen, und eingedockt. / [In] Brest. Entered, and docked." |

**航程统计（独有数据，一手与二源完全吻合）**：

> "Returned to Brest on 1st June, having steamed **7,000 miles at an average speed of 24 knots** since leaving Gotenhafen" — [NavWeaps OOB Cerberus](https://www.navweaps.com/index_oob/OOB_WWII_Atlantic/OOB_WWII_Cerberus.php)

> "Handwriting: Total track distance **7,000 nautical miles**. Average speed **above 24 knots**." — KTB 第 71 页，Brinkmann 手写批注

**这是本舰全文件里少见的「一手档案与二源完全一致」的字段。** 注意 KTB 那 7,000 明确是**海里**，NavWeaps 写的 "miles" 未注明单位——按 KTB 应为海里。

**【分歧】抵达布列斯特的日期**：KB / KTB / DANFS / Bonomi 都是 **6 月 1 日**；但 german-navy 写 **5 月 29 日**：

> "29.05.1941 Returns to Brest because of engine problems." — [german-navy](https://www.german-navy.de/kriegsmarine/ships/heavycruiser/prinzeugen/index.html)

**四比一，判 german-navy 有误的可能性大**（可能是起意赴法或与 Spichern 会合的日期）。并列，标 conflict。

### 12.2 布列斯特被炸（1941-07-02）

| 值 | 来源与原句 |
|---|---|
| **60 死**，含副舰长 Otto Stooß | [KB]："**60 dead**, including Executive Officer (I.O.) *Fregattenkapitän* Otto Stooß." |
| **52 死** | [DANFS]："an Allied air strike destroyed her damage control center and her main gunnery control room, **killing 52 of the crew** 2 July 1941" |
| **over 50 killed** | [NavWeaps OOB Cerberus]："Bombed 1st / 2nd July; hit on the bridge, **with over 50 killed**; estimated 6 months to repair." |
| 命中位置 | [KB]："hit at 0144 hours by a bomb in the port side, Section X." |
| 修复期 | [NavWeaps OOB]："Ready for service in December 1941 and undocked 15th December." |

**三个死亡数字：60 / 52 / over 50。并列。** KB 是唯一给出具体姓名的（副舰长 Stooß）。1960–70 年代德文文献常写 60，美方 DANFS 写 52——差异可能来自「是否计入当夜在舰上死亡者」，但无来源证实。

### 12.3 瑟布鲁斯行动（Channel Dash，1942-02-11/13）

**任务书说「如果查得到」——查得到，而且相当详细。**

编制（[NavWeaps OOB Cerberus](https://www.navweaps.com/index_oob/OOB_WWII_Atlantic/OOB_WWII_Cerberus.php)）：

> "KM Prinz Eugen Commanding officer: KptzS Helmuth Brinkman"
> 编队司令：Vizeadmiral Otto Ciliax；编队序列：Scharnhorst（旗舰）、Gneisenau、Prinz Eugen；护航 6 艘驱逐舰（Z29 旗舰 + Richard Beitzen、Paul Jacobi、Herman Schoemann、Frederich Inn、Z25）+ 2/3/5 鱼雷艇支队 + S 艇 3 个支队 + 扫雷部队

本舰参战细节（[KB]）：

> "**11-13 February 1942:** Operation *Cerberus*. The *Prinz Eugen* leaves Brest with the battleships *Scharnhorst* and *Gneisenau* escorted by six destroyers for a dash through the English Channel. Group commanded by *Vizeadmiral* Otto Ciliax. **She expends over 5,000 rounds of AA ammunition, and fires some 20.3cm shells at British destroyers.** *Prinz Eugen* reaches Brunsbüttel undamaged in the morning of the 13th, then navigates the lock of the Kiel Canal, and makes fast in the north chamber."

**「>5,000 发高炮弹」是本舰单次战斗最高弹药消耗记录。**

**三舰里唯一无损但有人阵亡的一艘**：

> "In this operation, the Prinz Eugen was the **only one of the large units to remain undamaged**, but suffered the **only loss of life** of the three deplore large ships." — [naval-encyclopedia](https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php)

（这句话本身有内部矛盾——「un damaged」却「suffered the only loss of life」，可能指本舰有人因防空炮位暴露阵亡。**照引，不加解释。**）

**行动前的一个硬约束（希特勒的附加条件）**：

> "The only provision was that the **Prinz Eugen should not sail alone**." — [NavWeaps OOB Cerberus](https://www.navweaps.com/index_oob/OOB_WWII_Atlantic/OOB_WWII_Cerberus.php)

**舰上还打了防空弹幕的 20.3 cm 专用弹**（NavWeaps 独家）：

> "These AA shells were reportedly used at least by *Prinz Eugen* during the Channel Dash (Operation *Cerberus*)..." — [NavWeaps](https://www.navweaps.com/Weapons/WNGER_8-60_skc34.php)

### 12.4 被 Trident 雷击（1942-02-23）

| 值 | 来源与原句 |
|---|---|
| 时间地点 | [KB]："At 0704 hours, the British submarine *Trident* (Commander G. M. Sladen) scores a torpedo hit on *Prinz Eugen*'s stern off Trondheim (quadrant AF 8263)." |
| 损伤 | [KB]："The damage is severe, the **rudder is lost**, and **50 men lose their lives**, but she manages to reach Trondheim by her own power" |
| 艉部切除 | [DANFS]："After the removal of **40 feet** of her stern and the installation of two temporary rudders" |
| 临时舵 | [KB]："Two jury-rudders are installed on to the stern transverse bulkhead." |
| 修复船 | [KB]："The ship undergoes temporary repairs carried out by the repair ship *Huascaran* in the Lofjord." |

**死亡人数两处都是 50**（KB）。这一条比布列斯特那次的三个数字干净。

### 12.5 回基尔与修复（1942-05-17/18 – 10 月）

| 时间 | 事件 | 原句 |
|---|---|---|
| 1942-05-17/18 | 回基尔（Zauberflöte 行动） | [KB]："Operation *Zauberflöte*. ... leaves Trondheim and returns to Kiel for final repairs. On the way back home the German flotilla is attacked by British Beaufort torpedo bombers off the Norwegian coast, but repels the attack and escapes undamaged" |
| 1942-05-17/18 | 期间用 20.3 cm 高炮打鱼雷机 | [NavWeaps]："...and on 17 May 1942 while transiting from Norway to Germany when she **fired AA barrages from "B" and "C" turrets** at attacking British torpedo bombers." |
| 1942-05-23 | Deutsche Werke Kiel V 坞 | [KB]："Drydocked for repairs at Deutsche Werke Kiel (Dock V)." |
| 1942-10 中 | 修完，转波罗的海 | [KB]："Mid-October 1942: Repair work finished. Subsequently leaves Kiel for the Baltic." |

**注意：主炮塔打防空弹幕**这条很罕见，是写「20.3 cm 能不能防空」时唯一的实弹记录。

### 12.6 训练舰时期（1943）

| 时间 | 事件 | 原句 |
|---|---|---|
| 1943-01-09 | Fronttheater 行动（赴挪威，被英机发现折返） | [KB]："Detected by British planes off Skagen on the 11th, the group returns to Gotenhafen where it arrives on the 12th." |
| 1943-01-23 | Domino 行动（再次赴挪威，再被发现） | [KB]："Sails for Norway again with *Scharnhorst* but is detected one more time by British planes and returns to the Baltic." |
| 1943-03 – 1944 | 波罗的海训练舰 | [KB]："March 1943-1944: Used as a training ship in the Baltic." |

**希特勒曾下令所有大型舰退役，是邓尼茨拦下来的**（naval-encyclopedia，D 级，作 narrative）：

> "Originally, Hitler ordered all heavy units to be decommissioned, which Karl Dönitz, as the new commander-in-chief of the Navy, was able to prevent."

### 12.7 波罗的海岸轰与撞舰（1944）

| 时间 | 事件 | 弹数 |
|---|---|---|
| 1944-06-19/28 | 芬兰湾出击 | — |
| 1944-08-20 | 里加湾 Tuckum 岸轰 | **240 发** |
| 1944-10-10/15 | Memel 岸轰 | **1,196 发** |
| 1944-10-15 20:04 | 撞莱比锡号 | — |
| 1944-11-20/21 | Sworbe 半岛（Ösel 岛）岸轰 | **514 发** |
| 1944-12 | Gotenhafen 换主炮内管 | — |
| 1945-01-26 – 02-02 | Samlandküste 行动 | **871 发**（01-29 至 01-31） |
| 1945-03-10 – 04-04 | 但泽湾岸轰 | **4,871 发 20.3 cm + 2,644 发 10.5 cm**（26 天） |

全部来自 [KB/prinzeugen](https://www.kbismarck.com/prinzeugen.html) 逐条原句，例：

> "**20 August 1944:** Shore bombardment against the Soviets on Tuckum in the Gulf of Riga. All three ship-borne Arado seaplanes are used to observe the fall of shot. *Prinz Eugen* fires 240 projectiles on Tuckum."

> "In twenty-six days the ship has expended 4,871 rounds of 20.3 cm ammunition, and 2,644 rounds of 10.5 cm ammunition."

**这些弹数是本舰生涯里最扎实的一批数据**（逐行动、逐日、有地点），而且总计上万发，正好解释了为什么 1944-12 要换炮管内管。

**撞莱比锡号**：

> "**15 October 1944:** At 2004 hours off the coast of Hela, the *Prinz Eugen* rams the light cruiser *Leipzig* amidships. **It takes fourteen hours to separate both ships.**" — [KB](https://www.kbismarck.com/prinzeugen.html)

> "At 2004 hours on 15 October 1944, as the *Prinz Eugen* returned to Gotenhafen from a naval support operation off Memel, the heavy cruiser accidentally rammed the light cruiser *Leipzig* amidships off the coast of Hela. It took fourteen hours before it was considered safe to separate both ships." — [kbismarck/prinz-eugen-leipzig-collision](https://www.kbismarck.com/prinz-eugen-leipzig-collision.html)

**莱比锡号侧的人员损失**（只有 naval-encyclopedia 给）："27 crew members of the cruiser were killed"，D 级，单源。

**本舰在此后只做了两周抢修就复役**：

> "13 November 1944: After two weeks in dock at Gotenhafen, repair work is finished and the ship is ready again for action." — [KB]

DANFS 的说法不同，说舰艏被换掉了：

> "**Her bow was replaced** following a collision with light cruiser *Leipzig* in October 1944." — [DANFS](https://web.archive.org/web/2023id_/https://www.history.navy.mil/research/histories/ship-histories/danfs/p/prinz-eugen.html)

**【分歧】** KB/naval-encyclopedia 说「两周抢修、不需进坞」，DANFS 说「换了舰艏」。**「换舰艏」与「两周完工」在工程上不相容**，两者并列。

### 12.8 战争结束（1945）

| 时间 | 事件 | 原句 |
|---|---|---|
| 1945-04-10 | 打光弹药后离开波罗的海 | [KB]："After expending all her ammunition, the *Prinz Eugen* leaves the Baltic for Copenhagen where she arrives on the 20th." |
| 1945-05-07 16:00 | 哥本哈根投降 | [KB]："At 1600 hours, the battle flag is lowered and the ship surrenders in Copenhagen with the light cruiser *Nürnberg*." |
| 1945-05-08 | 移交英国 | [KB]："The *Prinz Eugen* is handed over to the British." |
| 1945-05-26/28 | 由 Dido、Devonshire 押送威廉港 | [KB]："Leaves Copenhagen with *Nürnberg*, and sails to Wilhelmshaven escorted by British cruisers *Dido* and *Devonshire* arriving on the 28th." |
| 1945-12 | 抽签归美 | [naval-encyclopedia]："In December 1945, the ship fell by lot as spoils of war to the Americans" |
| 1946-01-05 | 挂美国旗，USS *Prinz Eugen* (IX-300) | [KB]："The American flag is hoisted and the ship put into service in the US Navy as USS *Prinz Eugen* (IX-300)." |

**任务书说「1945 年移交美国」——方向对，但精确说法是「1945-05 交英国、1945-12 抽签归美、1946-01-05 正式入美籍」。**

### 12.9 比基尼与夸贾林（1946）

| 时间 | 事件 | 原句 |
|---|---|---|
| 1946-01-13 | 赴波士顿（美德混编舰员） | [KB]："Leaves for Boston with a mixed crew of Germans and Americans." |
| 1946-01-22 | 抵波士顿 | [KB]："Arrives in Boston. Shortly after moves to Philadelphia where the barrels of turret "Anton" are removed." |
| 1946-03 | 经巴拿马运河赴太平洋 | [KB]："Leaves for the Pacific through the Panama Canal." |
| 1946-05-01 | 圣迭戈，德籍舰员离舰 | [KB]："In San Diego, the last German crew members leave the ship." |
| **1946-07-01** | **Able 空爆**，距爆心 1,194 码，**未损** | [KB]："A-bomb test Able. At 0900, a nuclear bomb dropped over a target fleet of ships by a B-29 detonates at 518 feet above the surface. *Prinz Eugen* is located 1,194 yards from the point of explosion and survives the test undamaged." |
| **1946-07-25** | **Baker 水下爆**，距爆心 1,990 码，「无显著损伤」 | [KB]："A-bomb test Baker. At 0835, and nuclear bomb is detonated underwater at a depth of about 90 feet. *Prinz Eugen* is located 1,990 yards from the explosion, and again survives the test with no appreciable damage." |
| 1946-08 末 | 除籍 | [KB]："Late August 1946: Decommissioned." |
| 1946-09 初 | 拖往夸贾林 | [KB]："Early September 1946: Towed to Kwajalein Atoll." |
| **1946-12-22** | **倾覆沉没** | [KB]："Due to leaks takes a 35º starboard list and capsizes over Enubuj reef in position 08º 45' 08" North, 167º 40' 59" East" |

**「未损」的分歧**：KB 说 Able「undamaged」、Baker「no appreciable damage」；german-navy 说 Baker 有水下损伤：

> "01.07.1946 Used in atomic bomb test "Able", only light damage. 25.07.1946 Used in atomic bomb test "Baker", **ship took some damage below the waterline**." — [german-navy](https://www.german-navy.de/kriegsmarine/ships/heavycruiser/prinzeugen/index.html)

**而 naval-encyclopedia 的说法更完整，把「为什么最后会沉」串起来了：**

> "The hull close to the propeller shafts became leaky due to tests vibrations and flooding commenced. The bilge pumps could not be used to their strong irradiation, and no crew was allowed aboard. From December 16, 1946, she started to list from starboard side and by December 21, was a meter deeper in aft." — [naval-encyclopedia](https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php)

**「抽水泵因强辐射不能用、又不准上人」——这才是 1946-12-22 倾覆的真正原因**，KB 的「due to leaks」只说了现象。写页面时这句必须用。

**Baker 的深度与距离，另一个来源给了不同数**：

> "When test "Able" was done on July 1, 1946 (dropped from a B-29, detonating at 170 m and 1100 m (1184 yards) away. ... On July 25, 1946, "Baker" was underwater, 30 m deep, **1800 m (1990 yards)** away from the fleet." — [naval-encyclopedia]

170 m ≈ 518 ft（KB）、1,100 m ≈ 1,194 码（KB）、30 m ≈ 90 ft（KB）、1,800 m ≈ 1,990 码（KB）——**四组数彼此换算吻合，两源实际一致**。这是少见的完全对得上的字段。

---

## 13. 现状（1946 年后）

### 13.1 残骸

| 项目 | 值 | 来源与原句 |
|---|---|---|
| 位置 | 08°45′08″N, 167°40′59″E，Enubuj 礁 | [KB]："capsizes over Enubuj reef in position 08º 45' 08" North, 167º 40' 59" East" |
| 离岸距离 | 约 250 m | [naval-encyclopedia]："capsized and sank on December 22, 1946 in shallow water **about 250 meters from the beach of Enubuj island**" |
| 姿态 | 右倾 35° 后翻覆，艉部露出水面 | [KB]、[naval-encyclopedia]："Her stern essentially still stuck out of the water but her superstructure was mushed when hitting the bottom of the lagoon while **three turrets slipped out of their barbettes**, "Anton" being previously welded in place." |
| 可见性（1970） | 仍在 | [DANFS]："Into 1970 she remains rusting on a coral reef at Enubuj, Kwajalein Atoll." |
| 可见性（当代） | 仍在，且美方在抽油 | 见下 |

### 13.2 拆件与纪念

| 时间 | 事件 | 原句 |
|---|---|---|
| 1978 | 拆左舷螺旋桨（12 吨）运回德国 | [KB]："By initiative of former crew members, and after seeking for permission, the **12 ton port propeller** is removed from the hull and shipped to Germany where it is erected as a naval memorial **near Kiel**." |
| 现存文物：Ar 196 | 一架存于 Smithsonian | [german-navy]："One of her Arado Ar 196 aircraft is preserved by the Smithsonian Institution" |
| 现存文物：舰钟 | 美国海军国家博物馆 | [german-navy]："the ship's bell is held by the National Museum of the United States Navy in Washington, D.C." |
| 现存文物：Anton 塔炮管 | 弗吉尼亚 Dahlgren 海军试验场 | [german-navy]："Guns removed from turret Anton before the Bikini tests remain at the naval test facility in Dahlgren, Virginia" |
| 现存文物：螺旋桨 | 德国 Laboe 海军纪念馆 | [german-navy]："one of the ship's propellers is displayed at the Naval Memorial in Laboe, Germany" |

**【分歧·螺旋桨位置】** KB 说「near Kiel」，german-navy 说「Laboe 海军纪念馆」。Laboe 在基尔峡湾口，**严格说两者不矛盾**（Laboe 就在基尔附近），但精确地址应写 Laboe。

**炮管的去向，NavWeaps 的说法与 german-navy 不同**：

> "One gun was scrapped in the 1950s and other remained there on display until sometime in the 1970s when it was also scrapped." — [NavWeaps](https://www.navweaps.com/Weapons/WNGER_8-60_skc34.php)

即：**1946 年拆下的 Anton 塔炮管运到 Dahlgren，1950 年代拆一门、1970 年代拆掉剩下那门。** 与 german-navy 的「remain at Dahlgren」冲突（后者暗示仍存）。**并列，标 conflict。**

### 13.3 当代：抽油作业

naval-encyclopedia 收录了一段美方公开说明（无日期，但提到 Ronald Reagan 弹道导弹靶场，可定在 2010 年代）：

> "The U.S. Army, in partnership with the U.S. Navy and the Republic of the Marshall Islands, are safely recovering oil from the capsized World War II German heavy cruiser Prinz Eugen in the Kwajalein Atoll. These recovery efforts will ensure mission capability of the U.S. Army Space and Missile Defense Command/Army Forces Strategic Command's Ronald Reagan Ballistic Missile Defense Test Site on Kwajalein while protecting the sensitive ecosystem within the atoll." — [naval-encyclopedia](https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php)

**这是「现状」一节唯一一条当代材料。** 具体年份未获取。

---

## 14. 未获取字段汇总

**这一节是本舰的核心交付。任务书预期「未获取会比别多」，实测结果比预期好，但仍有一批硬缺口。**

### 14.1 舰体与尺度

| 字段 | 状态 | 说明 |
|---|---|---|
| `dimensions.length.wl` | **单源（D 级）** | 只有 naval-encyclopedia 的 199.5 m，其余来源均无 |
| `dimensions.length.pp` | **未获取** | 垂线间长，无任何来源 |
| `dimensions.draught.standard` | **单源** | 6.6 m 仅 naval-encyclopedia |
| `dimensions.freeboard` | **未获取** | KB 对本级的 12.45 m 是 "height/depth"，不是干舷 |
| `dimensions.waterplane_area` | **未获取** | — |
| `dimensions.coefficients` | **未获取** | 方形/棱形/水线面系数全无 |
| `dimensions.gm` | **未获取** | 初稳性高，无来源 |
| `dimensions.depth` | **可疑（疑为姊妹舰抄写）** | KB 给 12.45 m，与其 Hipper 页 "depth 12.45 m" 逐字相同 |

### 14.2 排水量（**口径严重不全**）

| 字段 | 状态 | 说明 |
|---|---|---|
| `displacement.standard` | **冲突未决** | 14,240 mt（KB，疑抄 Hipper）vs 16,970 t（naval-encyclopedia），差 2,730 t |
| `displacement.empty` | **未获取** | 完工空船，无来源 |
| `displacement.design` / `Typverdrängung` | **未获取** | 德制型号排水量口径，无来源 |
| `displacement.construction` | **未获取** | 建造/试航排水量，无来源 |
| `displacement.full` | 有值但三源不一 | 19,042 / 19,050 / 18,400 / 19,250(美制) |
| `displacement.maximum` | 口径不明 | german-navy 的 18,400 t 标 "Size (Max)" 却低于满载值，口径不清 |

### 14.3 动力

| 字段 | 状态 | 说明 |
|---|---|---|
| 锅炉型式/压力 | **单源** | La Mont 70 atm，仅 naval-encyclopedia；KB 未给型式 |
| 汽轮机厂 | **冲突未决** | Brown-Boveri（naval-encyclopedia）vs Germania（KB / german-navy） |
| 蒸汽参数（温度/压力细节） | **未获取** | 与俾斯麦号不同，无同类详细页 |
| 燃油容量 | **口径冲突** | 4,250 mt（KB，疑抄）/ 3,050 t（navypedia）/ 3,233 m³ 实测（KTB）/ 3,250 t 上限（KTB 脚注） |
| 续航 | **口径冲突** | 6,800 nm @16 kn（KB）/ @20 kn（navypedia、naval-encyclopedia）/ 7,200 mi @20 kn（german-navy） |
| 螺旋桨直径 | **单源（舰级通述）** | 4.1 m，naval-encyclopedia，且是整级的表述 |

### 14.4 防护

| 字段 | 状态 |
|---|---|
| `protection.armor.weight` | **未获取**（装甲总重，全项目缺口） |
| 逐段装甲厚度（本舰专属） | **未获取**。navypedia 那段是**舰级通述**，本舰「internal arrangement 有差异」，不能直接套 |
| 炮塔正面厚度 | **四源四值**（160 / 105 / 70–160 / 160–50） |
| 水下防护分舱细节 | **未获取** |

### 14.5 航空

| 字段 | 状态 |
|---|---|
| 机库尺寸 | **未获取** |
| 弹射器型号 | **未获取**（naval-encyclopedia 自己写 "type to find"） |
| 载机数 | **有争议**（3 vs 4） |
| 航空燃油量 | **未获取** |

### 14.6 雷达与火控

| 字段 | 状态 |
|---|---|
| FuMO 型号的**装机日期精度** | 只到「1941 / 1942-02 / 1944 / 1945」四档，无月日 |
| 雷达性能（波长/功率/探距） | **未获取**（只有 1941-04-16 探潜 6,000–7,000 m 一条实测） |
| 火控计算机型号 | **未获取** |
| 主测距仪基线 | 5 × 7 m（KB，但与其 Hipper 页逐字相同，疑抄） |

### 14.7 涂装（**本舰最大的资料落差**）

| 字段 | 状态 |
|---|---|
| 条纹条数、角度、位置 | **未获取**（三条规定只对俾斯麦明确） |
| 色号（RAL 清单） | **未获取**（俾斯麦有六色清单，本舰无） |
| 各期涂装时间表 | **未获取**（只知道 1941-05-21 涂掉条纹） |

### 14.8 编制与人员

| 字段 | 状态 |
|---|---|
| 军官/士官/水兵三级 | **未获取** |
| 编制数 | **冲突**（1,600 ×3 / 1,282 / 830 美军） |
| 舰员伤亡总表（全战争） | **未获取**（只有零散几处：Brest 60/52、Trident 50、1945 各次 1 人 / 9 人） |

### 14.9 建造与造价

| 字段 | 状态 |
|---|---|
| 下水日 | **冲突**（08-22 ×3 / 08-20 DANFS） |
| 造价 | 104.5 Mio RM（单源 german-navy） |
| 合同签订日 | 1935-11-16（单源 KB） |

### 14.10 战史（数字类）

| 字段 | 状态 |
|---|---|
| 丹麦海峡发射弹数 | **三值冲突**（157 / 179 / 183） |
| 10.5 cm 发射弹数 | **两值冲突**（109 / 66） |
| 对 PoW 命中数 | **冲突**（3 / 4，Bonomi 文内自相矛盾） |
| 对 Hood 命中数 | 「至少 1 发」——**上限未获取** |
| 全战争弹药消耗总计 | **未获取**（只有逐次行动的子项） |
| 炮管寿命消耗记录 | **未获取** |

### 14.11 明确「不是未获取，而是不适用」的字段

按 `docs/30-new-ship-workflow.md` §2.2 的判据，以下字段在本舰**不成立**，不登记为「未获取」：

- `aviation.deck.*` / `aviation.hangar.*` / `aviation.elevator.*` / `arrestor.count` —— 重巡无飞行甲板
- `armament.broadside_weight` —— 无来源给，也不该由我乘算

---

## 15. 抓取失败清单（下次别重复）

### 15.1 任务书已实测、本文未重复的

| URL | 结果 |
|---|---|
| `https://www.kbismarck.com/prinz-eugen.html` | 404（**正确地址是 `/prinzeugen.html`**） |
| `https://www.kbismarck.com/prinz_eugen.html` | 404（同上） |
| `https://de.wikipedia.org/wiki/...` | 403（任务书实测，未重试） |
| `https://www.deutsche-kriegsmarine.de/` | 连接失败（任务书实测，未重试） |
| `https://kriegsmarine.de/` | 连接失败（任务书实测，未重试） |
| `https://www.bundesarchiv.de/` | 站内搜不到舰船档案（任务书实测，未重试） |

### 15.2 本次新试并失败的

| URL | 结果 | 备注 / 替代路径 |
|---|---|---|
| `https://www.navweaps.com/Weapons/WNGER_105-65_skc33.php` | **404** | **真实路径是 `WNGER_41-65_skc33.php`**（41 = 4.1 inch 而非 105 mm）。改用后者成功 |
| `https://www.history.navy.mil/research/histories/ship-histories/danfs/p/prinz-eugen.html` | **SSRF 拦截**（域名解析到私网地址 198.18.0.87） | 改走 `web.archive.org` 镜像成功 |
| `https://www.kbismarck.com/camouflage.html` | 404 | — |
| `https://www.kbismarck.com/bismarck-camouflage.html` | 404 | 涂装资料实际在 `drawings.html` 与 `24-may-drawing.html` |
| `https://www.hmshood.com/denmarkstrait/index.html` | 连接被关闭 | Bonomi 文章书目里引的老站，已不可用 |
| `https://www.hmshood.org.uk/history/denmarkstrait/bismarck2.htm` | **403** | 该站对直连封禁。项目里已有此页的抓取文本（`hood-sinking.md` 引用 HOOD2） |
| `https://www.kbismarck.com/hipper.html` | 404 | **正确是 `admiral-hipper.html`** |
| `https://www.german-navy.de/.../prinzeugen/history.html` | 404 | — |
| `https://www.german-navy.de/.../prinzeugen/history/index.html` | 404 | 站内只有 `index.html` 一页 |
| `https://www.german-navy.de/.../heavycruiser/luetzow/index.html` | 404 | **正确是 `lutzow`（无 umlaut）** |
| `https://www.navypedia.org/ships/germany/ger_cr_prinz_eugen.htm` | 404 | 本舰在 navypedia **没有独立页**，只有级页 |
| `https://www.navypedia.org/ships/germany/ger_cr_hipper_class.htm` | 404 | 正确是 `ger_cr_hipper.htm` |
| `https://ww2db.com/ship_spec.php?ship_id=98` | **403** | — |
| `https://www.combinedfleet.com/` | 200，但**全站只做日本舰** | 任务书的预判正确，该站确实没有德舰页 |
| `https://www.kbismarck.com/pg003.html` | 404 | 档案索引页里挂了但文件不在 |
| `https://www.kbismarck.com/pg004.html` | 404 | 同上 |
| `https://www.kbismarck.com/prinz-drawings.html` 等 4 个猜测路径 | 404 | 本舰没有独立的线图/涂装页 |

### 15.3 试过且有效的（供下次直接用）

| URL | 说明 |
|---|---|
| `https://www.kbismarck.com/prinzeugen.html` | **本舰主页面，25,035 bytes** |
| `https://www.kbismarck.com/archives/pg-ktb.zip` | **本舰战争日志全译本 PDF，2,377,700 bytes，122 页** |
| `https://www.kbismarck.com/ds-barticle.pdf` | Bonomi 丹麦海峡逐齐射分析，706,501 bytes，19 页 |
| `https://www.kbismarck.com/torpedowaffe-pg.html` | OKM 关于鱼雷未使用的调查文件全文 |
| `https://www.kbismarck.com/pg-medical-report.html` | 本舰军医报告（含战斗伤亡）|
| `https://www.kbismarck.com/admiral-hipper.html` | 首舰页（用于舰级对照） |
| `https://www.kbismarck.com/blucher.html` | 二号舰页 |
| `https://www.kbismarck.com/operheini.html` | 莱茵演习行动页（含两舰涂装记载） |
| `https://www.kbismarck.com/drawings.html` / `24-may-drawing.html` | 俾斯麦涂装线图 + 六色 RAL 清单 |
| `https://www.kbismarck.com/archives/index.html` | **档案总索引——本舰所有一手文件的入口** |
| `https://www.german-navy.de/kriegsmarine/ships/heavycruiser/prinzeugen/index.html` | 本舰页（含造价、船台） |
| `https://www.german-navy.de/kriegsmarine/ships/heavycruiser/admiralhipper/index.html` | 级首舰页 |
| `https://www.german-navy.de/kriegsmarine/ships/heavycruiser/{blucher,seydlitz,lutzow}/index.html` | 同级其余四舰的建造记录（全部可用） |
| `https://www.navypedia.org/ships/germany/ger_cr_hipper.htm` | 舰级技术表 + 逐段装甲（**唯一按部位组织的装甲来源**） |
| `https://www.navweaps.com/Weapons/WNGER_8-60_skc34.php` | 20.3 cm 主炮（含弹道表、穿深、炮塔数据） |
| `https://www.navweaps.com/Weapons/WNGER_41-65_skc33.php` | 10.5 cm 高炮 |
| `https://www.navweaps.com/Weapons/WNGER_37mm-83_skc30.php` | 3.7 cm 高炮 |
| `https://www.navweaps.com/Weapons/WNGER_20mm-65_c30.php` | 2 cm 高炮 |
| `https://www.navweaps.com/index_oob/OOB_WWII_Atlantic/OOB_WWII_Cerberus.php` | 瑟布鲁斯行动战斗序列（76,830 bytes，含本舰航程统计） |
| `https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php` | 本舰动力/AA/吨位差异最详细的单一来源（D 级，含笔误，须核对） |
| `http://web.archive.org/web/2023id_/https://www.history.navy.mil/.../prinz-eugen.html` | DANFS 镜像（直连被 SSRF 拦时用它） |

---

## 16. 来源清单

| 代号 | 来源 | URL | 等级 | 用途 |
|---|---|---|---|---|
| **KB-PG** | kbismarck.com, "Cruiser Prinz Eugen" (José M. Rico) | https://www.kbismarck.com/prinzeugen.html | **D** | 生涯时间线、技术数据表、舰长名录 |
| **KTB** | Prinz Eugen 战争日志（Bundesarchiv 原件 / NARA T1022 roll 2815，Rudofsky 译） | https://www.kbismarck.com/archives/pg-ktb.zip | **A**（原件 A，博物馆转录+译本） | 丹麦海峡逐时记录、炮术官报告、机械报告、军医报告 |
| **BONOMI** | Antonio Bonomi, *The Denmark Strait Battle, May 24th 1941* | https://www.kbismarck.com/ds-barticle.pdf | **C** | 逐齐射重建（引 ADM 234/509、ADM 116/4351 等英方一手） |
| **OKM-T** | OKM T Wa Ib B. Nr. 2386/41 g.Kdos.（1941-10-03），鱼雷未使用调查 | https://www.kbismarck.com/torpedowaffe-pg.html | **A** | 本舰鱼雷哑火的官方结论 |
| **KTB-MED** | Prinz Eugen 军医战斗报告（1941-06-01） | https://www.kbismarck.com/pg-medical-report.html | **A** | 战斗伤亡、38 cm 弹片 |
| **KB-DS** | kbismarck.com, "The Battle of the Denmark Strait" | https://www.kbismarck.com/denmark-strait-battle.html | **D** | 战斗叙述、脚注 3（PG 与致命命中的关系） |
| **KB-HIPPER** | kbismarck.com, "Admiral Hipper" | https://www.kbismarck.com/admiral-hipper.html | **D** | 舰级对照（并用于识别 KB 复制痕迹） |
| **KB-BLUCHER** | kbismarck.com, "Blücher" | https://www.kbismarck.com/blucher.html | **D** | 同级对照 |
| **KB-OPS** | kbismarck.com, "Operation Rheinübung" | https://www.kbismarck.com/operheini.html | **D** | 两舰涂装记载 |
| **KB-DRAW** | kbismarck.com, "Bismarck Drawings and Paint Schemes" | https://www.kbismarck.com/drawings.html | **D** | 条纹迷彩形态（主语为俾斯麦）、RAL 清单 |
| **KB-24MAY** | kbismarck.com, "Bismarck Drawings 24 May" | https://www.kbismarck.com/24-may-drawing.html | **D** | 5-21 涂掉条纹的日期确认 |
| **KB-ARCH** | kbismarck.com, Archives index | https://www.kbismarck.com/archives/index.html | **D**（索引） | 一手文件入口 |
| **KB-LEIPZIG** | kbismarck.com, "Prinz Eugen collision with Leipzig" | https://www.kbismarck.com/prinz-eugen-leipzig-collision.html | **D** | 撞舰细节 |
| **GN-PG** | german-navy.de, Prinz Eugen（Michael Emmerich） | https://www.german-navy.de/kriegsmarine/ships/heavycruiser/prinzeugen/index.html | **D** | 造价、船台、航速/功率、文物去向 |
| **GN-HIPPER** | german-navy.de, Admiral Hipper | https://www.german-navy.de/kriegsmarine/ships/heavycruiser/admiralhipper/index.html | **D** | 舰级对照 |
| **GN-BLÜCHER / GN-SEYDLITZ / GN-LÜTZOW** | german-navy.de 同级三舰 | 见 §15.3 | **D** | 舰级五舰建造记录 |
| **NAVYPEDIA** | navypedia.org, "ADMIRAL HIPPER heavy cruisers (1939)" | https://www.navypedia.org/ships/germany/ger_cr_hipper.htm | **D** | 逐段装甲（唯一按部位组织）、本级主尺度 |
| **NW-203** | NavWeaps, "Germany 20.3 cm/60 (8") SK C/34" | https://www.navweaps.com/Weapons/WNGER_8-60_skc34.php | **C** | 主炮全参数、弹道表、穿深、炮塔、发射弹数 |
| **NW-105** | NavWeaps, "Germany 10.5 cm/65 (4.1") SK C/33" | https://www.navweaps.com/Weapons/WNGER_41-65_skc33.php | **C** | 副炮座型号、备弹 |
| **NW-37** | NavWeaps, "Germany 3.7 cm/83 SK C/30" | https://www.navweaps.com/Weapons/WNGER_37mm-83_skc30.php | **C** | 3.7 cm 备弹 |
| **NW-20** | NavWeaps, "Germany 2 cm/65 C/30 & C/38" | https://www.navweaps.com/Weapons/WNGER_20mm-65_c30.php | **C** | 2 cm 参考（本舰无专属数据） |
| **NW-OOB-CERBERUS** | NavWeaps, "Orders of Battle — Operation Cerberus" | https://www.navweaps.com/index_oob/OOB_WWII_Atlantic/OOB_WWII_Cerberus.php | **C** | 瑟布鲁斯编成、本舰航程统计、布列斯特被炸 |
| **NAVALENC** | naval-encyclopedia.com, "Hipper class cruisers (1937)" | https://naval-encyclopedia.com/ww2/germany/hipper-class-cruisers.php | **D** | 逐舰动力差异、AA 改装年表、吨位改进、沉没原因、当代抽油。**注意该页多处笔误与内部矛盾** |
| **DANFS** | Naval History and Heritage Command, DANFS "Prinz Eugen" | https://web.archive.org/web/2023id_/https://www.history.navy.mil/research/histories/ship-histories/danfs/p/prinz-eugen.html | **B**（官方舰史） | 美方口径、IX-300、服役/下水日异说 |
| **HOOD-SINKING**（项目内） | `work/raw/hood-sinking.md` | — | 内部整理 | 「谁打沉了胡德」的既有立场，本文 §11.4 接续它 |
| **HOOD2 / ADM116 / JURENS**（项目内已登记） | 见 `data/sources.yaml` | — | **C / A / C** | 转引自 `hood-sinking.md`，本文不重复抓取 |

### 等级说明（本次判定依据）

- **A**：本舰战争日志原件转录、OKM 原始文件、军医报告原件——均为一手档案的完整转录/翻译。
- **B**：DANFS（美海军官方舰史出版物）。
- **C**：NavWeaps（长期被学界引用的武器专题数据库，数据溯自德方 M.Dv. 系列技术手册）、Bonomi 文章（引英方 ADM 系列一手）。
- **D**：kbismarck、german-navy、navypedia、naval-encyclopedia——专题站，质量参差，**naval-encyclopedia 已知含多处笔误，kbismarck 的 PG 页有疑似从 Hipper 页复制的字段**。
- **E**：en/de.wikipedia——**本次未用作任何数值来源**，只用于确认页面存在与找书目。

---

## 17. 差点用姊妹舰数据填、最后没填的字段

按要求列出，这是本文件可信度的自证。

| 字段 | 当时想用来填的值 | 来源 | 为什么没填 |
|---|---|---|---|
| `displacement.standard` | 14,240 mt | KB/PrinzEugen | 与 KB 自己的 Hipper 页**逐字相同**，同时 naval-encyclopedia 说改进批涨到 16,970 t。这是典型的姊妹舰复制痕迹，**宁可写「冲突未决」** |
| `fuel.capacity` | 4,250 mt | KB/PrinzEugen | 同样与 Hipper 页逐字相同，且与本舰 KTB 记载的实际油量（3,233 m³、上限 3,250 t）**差 1,000 t**。已判为不可靠 |
| `endurance` | 6,800 nm @ 16 kn | KB/PrinzEugen | 同上，与 Hipper 页逐字相同 |
| `dimensions.depth` | 12.45 m | KB/PrinzEugen | 同上（Hipper 页写 "depth 12.45 m"） |
| `fire_control.rangefinder` | 5 × 7 m | KB/PrinzEugen | 同上，与 Hipper 页同句 |
| `armament.aa_20mm.count` | 32 门 | german-navy | german-navy 给的是**无年份的静态快照**（本舰 28 门 / 4 cm 17 门），与 naval-encyclopedia 的分年演变（1941 初 10 → 1941 末 14 → 1945 18）任何一年都对不上，无法判它是哪一年的状态。**宁可不给单值** |
| `displacement.standard`（备选） | 14,050 t | navypedia | 那是 **Hipper/Blücher 首批舰**的值，不是本舰 |
| `dimensions.length.oa` | 205.9 m | navypedia / KB-HIPPER | 那是首舰值；本舰加装 clipper bow 后是 212.5 m，四源一致 |
| `armour.belt`（逐段） | navypedia 的 80/40/70 分段 | navypedia | 那段是**舰级通述**，navypedia 自己在 Project history 里说本舰「internal arrangement 有差异」，不能直接套本舰 |
| `machinery.turbine` | Blohm & Voss | navypedia（本级） | 本级首批是 Blohm&Voss，本舰两说（Brown-Boveri / Germania），都不是 B&V |
| `crew` | 1,282 或 1,600 | naval-encyclopedia / KB | 差 318 人且无来源解释口径；**没有取中间值或平均** |
| `armament.aa_37mm.count`（1945 状态） | 0 | 由「1944 全部换成 4 cm」推得 | 这是**推算**，且 naval-encyclopedia 自己 1944 年就给了 15 与 6 两个矛盾的 4 cm 数，不能据此反推 37 mm 归零 |
| `construction.launched` | 08-20 | DANFS | DANFS 是 B 级但孤证（三比一），**并列而非取多数** |
| 丹麦海峡发射弹数 | 179 | KB/PrinzEugen | 炮术官的 157 是逐弹种实发统计，比舰长总结更硬；NavWeaps 又给 183。**三值并列，不取其一** |
| 对 PoW 命中数 | 4 | Bonomi 第 609 行 | 同一篇文章第 668 行说 3，是文内自相矛盾。**并列，不挑** |
| 涂装条纹条数 | 3 条 | kbismarck/drawings | 那句的主语是**俾斯麦**，不是本舰。**明确写本舰未获取** |

**没有一处用「俾斯麦号」「希佩尔号」「布吕歇尔号」的数值直接填充本舰字段。** 上表里出现的姊妹舰数值只用于**舰级对照与识别复制痕迹**，没有一处进入本舰的数据条目。

---

*本文所有数值均可在对应 URL 页面内定位复核。抓取失败的来源已如实列入 §15。未做任何推测补全。*
