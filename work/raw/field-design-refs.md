# 战舰资料站字段组织方式调研（外部参照）

> 采集日期：2026-11-17。全部结论来自实际抓取的页面正文，URL 逐条标注。
> 用途：为 `docs/00-framework.md` §3.4 的「字段注册表」提供外部参照，避免闭门造车。
> 本文只记录**这些站怎么组织字段**（分组方式、多值处理、时间维度），以及由此得出的**我们该怎么做**。
> 不转录具体数值——数值属于内容层，不属于字段设计层。

---

## 一、逐个来源的信息架构

### 1. 英文维基 `Template:Infobox ship`

URL：https://en.wikipedia.org/wiki/Template:Infobox_ship （`Infobox_ship_begin` 重定向至此）

**结构**：一个参数化容器 + 若干 `section` 子模板插入。子模板只有五个：

| 子模板 | 承担什么 |
|---|---|
| `Infobox ship/image` | 图片 |
| `Infobox ship/career` | 生涯：国家、舰名、订购、建造厂、下水、服役、退役、结局、荣誉 |
| `Infobox ship/characteristics` | 技术：class、displacement、length、beam、draught/draft、propulsion、speed、range、complement、sensors、EW、armament、armour、aircraft、aircraft_facilities |
| `Infobox ship/class_overview` | 舰级条目专用：前后级、子级、建造/服役年代区间、各类数量 |
| `Infobox ship/service record` | 服役记录 |

另有 `labeln` / `datan` 成对参数，可以塞任意自定义键值——这是模板的"逃生口"，也说明官方字段集不够用。

**分组只有三段**：图 / 生涯 / 技术参数。就这么粗。

**必填？没有任何必填字段。** 模板不强制任何参数，只在文档里按舰种给四套推荐样板（warship / submarine / age of sail / commercial）。潜艇样板多 `endurance`、`test_depth`；帆船样板多 `tons burthen`、`sail_plan`、`hold_depth`。——即**「必填」是靠舰种区分推荐集，而非 schema 约束**。

**`class_overview` 段值得单拎**：`total_ships_planned / on_order / building / completed / cancelled / active / laid_up / lost / retired / scrapped / preserved`。这不是技术参数，是**舰级的数量生命周期状态机**。任何"某级共造几艘、几艘沉、几艘留到今天"的统计都应该由这套字段算出来，而不是正文里手写。

**时间维度**：career 段全部是**单值时点**（ordered / laid_down / launched / commissioned / decommissioned / stricken / fate）。`refit` 字段存在但只是自由文本。
**多值/争议**：没有机制，`armament` 里手写多行，改动历史靠正文散文。

→ **继承**：身份/生涯 与 技术参数 两大块的切分是对的，这是最小骨架。
→ **必须补**：它把"随时间变化的参数"压成静态单值；`sensors` 只有一个字段，装三部雷达也只能写一段话。

---

### 2. Wikidata `WikiProject Ships`

URL：https://www.wikidata.org/wiki/Wikidata:WikiProject_Ships （属性清单见 /Properties 子页）

这是所有来源里**唯一有正式本体**的。三层：

```
ship type（P31 instance of）        ← 靠 subclass of P279 建树
  └ ship class（Q559026）
      └ individual ship（用 vessel class P289 挂到具体舰）
```

类型与舰级**严格分离**：一艘舰的 `P31` 是"类型"，`P289` 是"级"。这个区分很多中文站没做，导致"俾斯麦级"和"战列舰"混成一个维度。

**属性分档**（这是它最像 schema 的地方）：

- 舰级：必填 = short name `P1813`、operator `P137`、named after `P138`、image `P18`、service entry `P729`；推荐 = manufacturer `P176`、country of origin `P495`、armament `P520`、NATO reporting name `P561`、follows `P155`、followed by `P156`、service retirement `P730`。
- 单舰：essential = `P31` + `P289`；mandatory = `P18` + `P1813`；recommended = `P137`、`P176`、yard number `P617`、`P729`、country of registry `P8047`、port of registry `P532`、`P504`、`P138`、gross tonnage `P1093`、length `P2043`、beam `P2261`、width `P2049`、draft `P2262`、`P520`、powered by `P516`、significant event `P793`、`P458`/`P587`/`P2317`（IMO/MMSI/call sign）、cause of destruction `P770`、participated in conflict `P607`、pennant number `P879`。

**三个可直接抄的机制**：

1. **尺寸必须带测量口径**。`length P2043` 明确限定为 overall；`beam P2261` 是水线宽，`width P2049` 是最大宽——**分开两个属性**。`draft P2262` 也是。这正好印证我们框架里"排水量三个口径不合并"的做法，应推广到所有尺寸。
2. **`significant event (P793)` + 事件类型 item + qualifier**。事件类型是独立条目：order `Q566889`、keel laying `Q14592615`、ship launching `Q596643`、shipbuilding `Q474200`、ship naming ceremony `Q370553`、ship acquired `Q27454075`、maiden voyage `Q1501837`、ship commissioning `Q14475832`、ship reclassification `Q21725151`、ship decommissioning `Q7497952`、destruction `Q17781833`、shipwrecking `Q906512`、service retirement `Q29933838`、ship disposal `Q7497950`、scuttling `Q1786766`、ship breaking `Q336332`。qualifier 用 point in time `P585` / start time `P580` / end time `P582` / location `P276` / cause `P770`。
   → **日期不是字段，是事件的限定符。**
3. **`P520 armament` 只能挂条目链接**，挂不了数量、安装位置、拆除时间；**装甲厚度至今没有通行属性**（还在 Properties missing 列表）；**没有部位索引**。

→ 它给我们的是**事件模型**（和我们 TROM 思路一致），它缺的正是我们要做的**配额与部位**。

---

### 3. `combinedfleet.com` 的 TROM（重点）

URL：
- 站点目录 https://www.combinedfleet.com/kaigun.htm
- 战舰索引 https://www.combinedfleet.com/senkan.htm （每条带 `(revised 8/1/2016)` 式逐条修订日期）
- 完整样例 https://www.combinedfleet.com/yamato.htm （页首 `© 2000-2016 ... Revision 18`）

**格式**：单个 HTML 页，正文是一串**日期开头的流水条**，没有任何字段分组。日期加粗独立成行。

日期粒度是**故意松弛**的，五种不同精度混在一条时间轴上：

```
18-19 January 1942          ← 区间
April-May 1942              ← 粗区间
Early May 1942              ← 模糊
March 1942                  ← 只到月
0015: ...  0255: ...        ← 同一天内多事件，时刻前缀 + 缩进 + 时区标记 (K)/(I)
```

每条事件是自由散文，但内部结构高度模式化，稳定出现这些槽位：
地点（Kure / Hashirajima / Truk / Lingga）、动作（Departs / Arrives / Anchors / Drydocked / Undocked / Launches / assumes command）、人物（军衔+姓名+"former CO of NAKA"这种履历括注）、编制变更（"assigned to BatDiv 1" / "transferred from First Fleet to Second Fleet"）、**改装细节**（"Two beam triple 6.1 inch turrets are removed and replaced by six (3x2) 5-inch HA AA mounts"、"Type 21, Mod 3 radar installed"、"total 25-mm AA suite is now 36 guns"）、战损（"torpedo hits starboard near turret No. 3, hole 15 ft down, 75 ft long between frames 151 and 173"）。

**争议处理 = 这个站点最强的设计**：脚注 `[1][2][3][4]` + 页尾 **Authors' Notes**。

- 例：德国武官访舰那段，作者把"他能否分辨 40cm 与 46cm 炮"的多方争论过程完整摊开，而不是给结论。
- 注 [3] 直接写 "the remainder of the message ... is not available"，并附一份 POW 报告作为另一说法——**证据缺失本身被显式记录**。
- 注 [4] 写改装方案 "in the event, the measure was inadequate"，还写了被否决的 5,000 吨补强建议**及否决理由**（增重要超吃水）。

另有"Previously recorded fate"式的前后修订（`uboat.net` 更规范，见下）。**结论与证据链分开存，旧说法不删。**

→ **对我们时间轴最重要的一条启发**：
**时间轴不是给舰船加一个"服役年表"字段，而是把"状态变更"本身作为一等对象。**
一条记录 = 日期（可带模糊粒度）+ 事件类型 + 主语（舰 / 某系统 / 某部位）+ 变更内容 + 来源与置信度。字段的"当时值"由事件流 **as-of 推导**，而不是在舰船上存一份会过时的静态参数表。
这样"1943-07 加装 25mm 高炮"和"1945-04 最终 152 门"可以同时成立、可回溯、可各自带来源——`navypedia` 的 Modernizations 段（见下）正是用 `+ / -` 手工表达了同一件事，只是没有机器可读的时间窗。

---

### 4. `uboat.net` 的 U 艇档案

URL：https://uboat.net/boats/u47.htm

**结构**：结构化固定字段表 + 分节叙述，两者混排。

固定字段：Type / Ordered / Laid down（含建造厂 + werk 号）/ Launched / Commissioned（含首任艇长）/ Fate（含位置、伤亡、**判定机构与判定年份**，例 "(FDS/NHB, June 1991)"）/ Loss position（地图 + marker）。

**三张日期区间表**——这是它最该被抄的部分：

| 表 | 列 |
|---|---|
| Commanders | 起 – 止 – 军衔 – 姓名 – 勋章 |
| Career（Flotilla 归属） | 起 – 止 – 舰队 – 状态（"active service"） |
| Wolfpack operations | 艇队 – 日期区间 |

同一艘艇在不同时间段属于不同舰队、由不同人指挥 → 用 **valid_from / valid_to 区间表**表达，不是单值时点。

另有：`Successes`（**按目标类型分桶统计**：商船 30 艘 162,769 GRT / 军舰 1 艘 29,150 t / 击伤 8 艘 62,751 GRT）、`Attacks on this boat and other events`（逐条日期 + 事件 + 行内来源引注如 "(Sources: Blair, vol 1, page 120)"，末尾给 "3 recorded attacks" 计数）、`Men lost from the boat`（日期 + 原因 + 人名）、`U-boat Emblems`（**一艇多徽，多值**，各带图与条目链接）、`Media links`。

**争议处理，比 TROM 更成体系**：
`Previously recorded fate` 独立区块保留旧结论 + 说明为何被推翻（"HMS Wolverine actually attacked Eckermann's U-A instead of U-47"），新结论标 `(Postwar assessment)`。
→ **结论带版本与推翻理由，旧值不删。** 这正是我们框架 §5.3 第 3 条"无法裁决则并列"的更彻底版本：不只是并列，是**留修订链**。

---

### 5. `Naval Encyclopedia`（现代整理站）

URL：https://naval-encyclopedia.com/ww1/uk/s-class-destroyer.php

（抓取教训：`/ww2/germany/battleship-bismarck.php`、`/ww2/germany/bismarck-class-battleships.php`、`/ww2/battleships/bismarck-class/` 全部 302 回首页。**站点改版后旧 slug 全废，只能从首页 Latest News 拿真实 URL，不能猜。**）

**条目结构**（自上而下）：

1. hero 图 + 单行 lead：`United Kingdom (1917-18): 67 Destroyers.`
2. 同舰种所有级别的横向链接条（"系列"索引）
3. **带小标题的编年叙事**：`The S-class in brief` / `The Original Scare (1916)` / `A counter reaction by the admiralty` / `Construction`
4. 建造厂逐行列表（`- Alexander Stephen and Sons, Linthouse` × 8）
5. **逐舰条目**：标题即 `Steadfast (F.99, H.37)`——**舰名 + 多个舷号逗号分隔**，因为舷号随年代/舰队变化；正文一句流水 `laid down ... launched ... commissioned ... Fate: Sold on ... and BU ...`
6. `⚙ Specifications` — 全站唯一真正结构化的块，**仅 9 行两列表**：
   `Displacement`（"1,075/1,225 long tons" 标准/满载用斜杠并列，不拆字段）、`Dimensions`（"276 ft x 26 ft 8 in x 9 ft 10 in (84.1 x 8.1 x 3 m) deep" 三尺寸挤一行，括号换单位）、`Propulsion`、`Speed`、`Range`、`Armament`、`Sensors`、`Crew`
7. `### Armament` 用散文讲演变："1943, Sabre, Saladin, Sardonyx saw the removal of their four 4 DC throwers. Displacement, full was close to 1,400 tonnes and stability was a concern"——**改装带来的吨位变化只写在正文，不回填规格表**
8. 尾部 `Books` / `Links` / **`Model Kits`**（fleetscale.com 1/96、turbosquid 3D）——套件是条目的**标准尾部区块**，但只给外链、不结构化
9. 站级 `Abbreviations & acronyms` 表（AA / AP / BL / BU / CA / CT / DD / DP / GRT / HA / LA / lwl / Mk 等 200+ 条）——**全站共享术语表，应直接抄成我们的 enum 字典**
10. 站点自述 "version #7，2023 与 2026 两次 refit"——整站有版本号

→ 它是"好文章 + 弱数据"的典型：9 行规格表撑不起对比器；标准排水量和满载挤在一个字符串里，机器读不了。

---

### 5b. `navypedia.org`（同代整理站，数据化程度更高）

URL：https://www.navypedia.org/ships/germany/ger_bb_bismarck.htm

**结构**：四块，比 Naval Encyclopedia 硬得多。

1. `Photo`
2. `Ships` 表：`Name | No | Yard No | Builder | Laid down | Launched | Comp | Fate`——**逐舰一行，舰级页就带完全部单舰**，且 `Yard No` / `Builder` 是独立列。
3. `Technical data` 两列表，13 行：`Displacement standard, t` / `Displacement full, t` / `Length, m`（"241.5 wl 250.0 oa" 把两个口径并列）/ `Breadth, m` / `Draught, m`（"8.70 mean 10.6 max"）/ `No of shafts` / `Machinery` / `Power, h.p.` / `Max speed, kts` / `Fuel, t` / `Endurance, nm(kts)` / `Armour, mm` / `Armament` / `Electronic equipment` / `Complement`。
   → **同字段不同舰的值并列写法**：`Bismarck: 41700 / Tirpitz: 42900`。即在舰级页里做"逐舰差异"，跟我们要的"舰级 + 单舰只写差异"同一思路，只是用文本凑。
4. 四段散文，**分工明确**：`Project history`（设计决策）/ `Ship protection` / `Modernizations` / `Naval service`。

**两个关键设计**：

- **`Armour, mm` 一行内按部位分号切分**：`belt: 320 - 270, upper belt: 145, upper deck: 50, main deck: 120 - 80, slopes: 100, torpedo bulkhead: 45, main gun turrets: 360 - 180, main gun barbettes: 340, secondary turrets: 100 - 40, CT: 355 - 50`，且每项用 `A - B` 表示**上缘到下缘的递减**。
  → 这是全部六个来源里**唯一真正"按部位组织"的字段结构**，也是唯一表达"厚度是个梯度不是一个数"的。直接对应我们想要的 `armor.belt.thickness` 拆法，还多一层 `thickness_top/bottom`。
- **`Modernizations` 用 `+ / -` 逐条记账，每条带年月**：
  `till 11.1940, Bismarck: only 4 x 2 - 105/60 SK C/33 were installed instead of 8 x 2`
  `9/1941, Tirpitz: - 4 x 1 - 20/65; + 6 x 4 - 20/65 C/38, 2 x 4 - 533 TT, FuMO 27 radar, FuMB 4, FuMB 7 ECM suites`
  → 已经是"事件流"的手工版：日期 + 舰 + 增项/减项。**但它没有 valid_to**（看不出某个配置在什么时候被下一次改装终止），也没跟规格表联动。

---

### 6. 武器页：`combinedfleet` 与 `NavWeaps`

- 索引 https://www.combinedfleet.com/guns.htm —— 炮按**口径-用途分四桶**：Heavy Caliber / Medium Caliber / Dual Purpose / Anti-Aircraft。条目名 = 口径/倍径 + 型号（`18.1"/45`、`8"/50 Type II`、`25mm/60`），URL 是纯参数（`460_45.htm`、`127_50.htm`）。
- 单炮页 https://www.combinedfleet.com/460_45.htm —— 一句定性导语 + 图 + **8 字段两列表**：`Bore` / `Weight` / `Length OA` / `Weight Projectile` / `Muzzle Velocity` / `Max. Elevation`（"+45/-5 degrees" 一个字段装上下限）/ `Max. Range` / `Rate of Fire`。每个值都带单位，没有裸数字。
- **NavWeaps 抓不到**：https://www.navweaps.com/Weapons/index_weapons.php 与三个具体炮页（`WNUS_16-50_mk7.php`、`WNUS_16-45_mk1.php`、`WNGER_15-52_skc34.php`）全部 30s timeout；换 `web.archive.org` 两个时点快照同样 timeout；换 `r.jina.ai` 代理 ECONNRESET。**结论：该站对自动抓取不友好，本报告不以它为证据源**，仅确认其与 combinedfleet 同构（每炮独立页 + 值/单位成对表 + 大量脚注）。

→ **武器必须是独立实体、独立页面、独立字段集**，舰船页只引用。这与我们框架 §2「武器与装备：独立实体，多舰复用」一致，并得到外部印证。

---

## 二、横向对比表

| 来源 | 字段分组方式 | 多值 / 争议数据怎么处理 | 有时间维度吗 | 对我们的启发 |
|---|---|---|---|---|
| Wikipedia Infobox ship | 三段：图 / 生涯 / 技术参数；`labeln`+`datan` 兜底自定义 | 无机制，自由文本多行 | 仅单值时点（下单/下水/服役/退役/结局）；`refit` 是散文 | 身份与技术二分的骨架可继承；`class_overview` 的"数量状态机"字段集直接可用 |
| Wikidata Ships | 正式本体：type（P31/P279）→ class（P289）→ individual；属性分 essential/mandatory/recommended | 多 statement + rank（preferred/normal/deprecated）+ qualifier | **事件 P793 + P585/P580/P582 限定符——日期不占字段位** | ①类型与舰级必须分离 ②尺寸必须带测量口径（oa / wl / max 分开） ③事件是一等对象 |
| combinedfleet TROM | 无分组，纯日期流水 | **脚注 + Authors' Notes**：结论与证据链分开；缺失也记录下来（"the remainder ... is not available"）；页级 Revision 号 | **全文以日期为骨架**，故意混用 5 种精度（日/区间/旬/月/模糊），同日多事件用时刻+时区 | ①时间轴以"状态变更事件"为单位，字段值靠 as-of 推导 ②日期粒度必须可松弛 ③每条可挂证据链 |
| uboat.net | 固定字段表 + 分节（Commanders / Career / Wolfpack / Successes / Fate / Attacks / Emblems） | **`Previously recorded fate` 保留旧结论 + 写推翻理由**，新结论标 `(Postwar assessment)` | **三张日期区间表**（起–止–…），不是时点 | ①"隶属/指挥/编队"用区间表 ②战果按目标类型分桶 ③推翻历史要留链，不覆盖 |
| navypedia.org | 舰级页四块：Ships 表 / Technical data 表 / 四段散文（Project history、Ship protection、Modernizations、Naval service） | 舰级页内用 `Bismarck: x / Tirpitz: y` 并列；`A - B` 表达厚度梯度 | **Modernizations 每条带年月 + `+/-` 增删记账**，但无 valid_to | ①**装甲按部位分行**是唯一真·部位化先例 ②改装用增减记账而非整表快照 ③但缺区间终止 → 我们要补 |
| Naval Encyclopedia | 9 行规格 2 列表 + 带小标题编年叙事 + Books/Links/Model Kits 尾块 + 全站术语表 | 无结构化处理，冲突写在正文 | 无字段级时间；改装吨位变化不回填规格表 | ①**套件应是条目标配区块** ②术语表做成全站 enum 字典 ③规格表必须是"一字段一值一单位"，不能斜杠并列 |
| combinedfleet guns / NavWeaps | 一炮一页，8 字段两列；索引按口径-用途四桶 | — | 无（武器参数不随时间） | 武器独立实体；每个值带单位；仰角上下限合用一个字段 |
| shipcamouflage.com | 四轴：按舰库 / 按 Measure 编号 / 色卡 / 官方文件原文 | — | **无 valid_from/valid_to** | 涂装应是 scheme 实体 + 生效区间 + 参考侧视图，而不是给舰挂一张图 |
| suburbanshipmodeler 套件库 | 三视图 Kits / Ships / Manufacturers，可按厂牌、船型、难度、比例、价格过滤 | 站点自承数据 out of date、无法自动更新 | 无 | ①`kit.status` + `kit.discontinued_at`，不要布尔 in_stock ②"builds 计数"是可用热度信号 ③套件与舰是多对多 |
| the-blueprints.com | 每个线图条目：Model years / Format / Projections / Scale / Price | — | **`Model years: 1940` 用年份标签表达时间切片** | ①线图要显式存 `scale`、`projections`、`format` ②文件名/标题带年份是民间表达时间状态的事实标准，我们要把它变成字段 |

---

## 三、模型制作者视角的缺口

框架 §2 判断"模型制作模块的检索轴是部位，不是舰"。以下四个方向逐个查证现状。

### 3.1 按部位索引的细节图 —— **没人做过**

- https://www.worldwarphotos.info/gallery/germany/kriegsmarine/bismarck/ ：35,500+ 张 WWII 照片，按 国家 → 军种 → 舰 分相册。单舰相册内**唯一的组织方式是缩略图顺序**。照片标题里确实出现部位词（"Bismarck superstructure"、"Bismarck Anton and Bruno turrets"、"Bismarck bow August 1940"、"Bismarck deck 2"、"Bismarck 380 mm guns"），但**部位只存在于自由文本标题里，没有任何字段**，不能用它筛。这是全站最强的"未结构化"证据。
- https://www.modelshipgallery.com/gallery/index.html 返回空内容（纯 JS 壳），无法评估，不作为证据。
- 唯一真正"部位化"的结构是 **navypedia 的 `Armour, mm` 按部位分号切分**（belt / upper belt / upper deck / main deck / slopes / torpedo bulkhead / turrets / barbettes / secondary turrets / CT）——但那只是装甲厚度，不是图片索引。

**结论：部位索引是真实的空白**。而且我们比别人多一个天然抓手——navypedia 已证明"部位"是可以用固定词表枚举的（十几个部位名），不需要自由文本。

### 3.2 按时间点的涂装方案 —— **做过，但只做到一半**

https://www.shipcamouflage.com/warship_camouflage.htm （Snyder & Short，USN WWII 涂装库）。站内分区：

`Camouflage Database`（按舰查）/ `Measures`（按 Measure 编号查方案定义）/ `Paint Colors`（色卡，与实际漆片比对）/ `Painting & Cementing`（官方文件原文）/ `Flags and Pennets` / `Ship Call Letters` / `Development of Naval Camouflage`（演变史）/ `Special Topics`

做得好的：**Measure 被当成独立实体**（方案有编号、有定义、有依据文件），色卡与实际漆片比对（不是印刷色）。
做得不够的：舰 ↔ Measure 只是**弱关联**——给一张 GIF 侧视涂装图（文件名如 `CV-6_Enterprise_SS2.gif`，用 `SS2` 这种 Measure 后缀区分），**没有 `valid_from / valid_to`**，也没做成"某舰在某年某月是哪个 Measure"的可查询表。

**我们的机会**：`scheme` 实体（配色定义）+ `ship.scheme` 生效区间 + 参考侧视图 + 依据文件。四件套一步到位，别人只做了第一件。

### 3.3 套件对照 —— **有做得不错的，但存活性都解决不了**

https://suburbanshipmodeler.com/model-ship-kit-database/ ：650+ 套件，三个视图 **Kits / Ships / Manufacturers**，可按 manufacturer、hull type、skill level、scale、price range 过滤；每行带 **builds 计数**。

数据来源很土但很聪明：抓 Model Ship World 论坛 "Build Logs for SHIP MODEL KITS" 版的**帖子标题**，用正则拆出 ship / manufacturer / scale——页面原话 "thread titles are generally in a specific format, so code was written to pick apart the thread titles"。之后**手动重新导入**，明确拒绝自动爬（"automatically crawling other people's sites is bad"）。

它的死穴自己也承认：**数据一发布就过时，且无法自动更新**；out of stock 遍地。

`https://www.scalemates.com/kits/` 返回 **Access Denied（Akamai，Reference #18.1335cb17…）**，抓不通。但它是业界事实标准——Naval Encyclopedia 的 Model Kits 区块明写 "I'm currently using scalemates"。

**教训**：套件库能做，但要把"在产状态"设计成 `kit.status`（枚举）+ `kit.first_seen_at` / `kit.discontinued_at`（时间），而不是布尔 `in_stock`。布尔值一定会腐烂，时间戳不会。

### 3.4 可打印线图与比例尺 —— **比例尺有做，分块打印没人做**

https://www.the-blueprints.com/blueprints/ships/battleships-germany/ 与单条目 https://www.the-blueprints.com/vectordrawings/show/7153/dkm_bismarck/

它是全部来源里**唯一把线图元数据字段化**的：

| 字段 | 示例值 |
|---|---|
| `Model years` | 1940 |
| `Format` | Adobe Illustrator (.ai) / .eps / .pdf / .svg / .dwg / .dxf（六种全给） |
| `Projections` | top, side |
| `Scale` | 1:1000 |
| `Price` | $18.00 / 14 credits |

另外它用**标题里的年份**表达同一艘舰的不同状态：同一艘 Bismarck 在库里有 11 条（`DKM Bismarck`、`DKM Bismarck (1940)`、`DKM Bismarck (1941)`、`Bismarck 1940-1941`…），Scharnhorst 有 `1938/1939/1940/1941/1942/1943` 六个年份版本。**这是民间用命名法表达时间切片的典型做法**——能查到，但没法算（不能问"1942 年 3 月这条舰长什么样"）。

navypedia 有 `Standard scale images` 与 `Graphics` 两节，但图片无任何元数据（只有 `Bismarck 1941` 这样的说明串）。

**没人做的**：按 A4/A3 分块的"可打印"版本（贴纸式拼接、带定位十字线、标明拼接偏移）、图纸的比例尺换算器、以及"这套图纸对应哪个时间切片/哪个套件"的三角关联。

---

## 四、建议的字段分组方案

### 设计原则（由上面调研直接推出）

1. **只有 12 个内容组**，组名用英文小写单词，字段名 `group.sub.name` 点分。组是给人看的导航，字段名是给机器算的。
2. **每个数值字段必须带口径后缀**（`oa` / `wl` / `max` / `mean` / `standard` / `full` / `deep`）——Wikidata 与 navypedia 的双重印证。
3. **凡"会变、会争议"的都不设成舰船上的静态字段**，而是 `fact`（框架 §3.2）；分组只是给 `fact.field` 提供命名空间，不改变存储层。
4. **引用型字段用 `_id` / `_ids` 后缀**（`identity.class_id`、`armament.mount.weapon_id`），表示指向独立实体而不是存副本。
5. **枚举值进全站字典**——照抄 Naval Encyclopedia 的 Abbreviations 表做 `data/enums.yaml`。

---

### 组 1 · `identity` — 身份标识

``` 
identity.name                  # 原名，不翻译
identity.name_latin            # 转写（西里尔/日文假名罗马字）
identity.name_translations     # 多语言译名，多值
identity.class_id              # 指向 class 实体（对应 Wikidata P289）
identity.type                  # 舰种枚举（battleship / carrier / heavy-cruiser …，对应 P31）
identity.subtype               # 更细的子型（fast-battleship / pocket-battleship）
identity.navy                  # 所属海军/国家，随时间可变 → fact
identity.pennant_number        # 舷号，多值且带年代（见 Naval Encyclopedia 的 "(F.99, H.37)"）
identity.hull_number           # 船体编号
identity.yard_number           # 建造编号（navypedia 的 Yard No 列）
identity.contract_designation  # 合同代号/替代舰代号（"Ersatz Hannover"、"F"）
identity.imo / identity.mmsi / identity.call_sign   # 现代舰
identity.name_sake             # 命名来源（Wikidata P138）
```

### 组 2 · `dimensions` — 尺寸与排水

``` 
dimensions.displacement.standard      # 标准排水量
dimensions.displacement.full          # 满载排水量
dimensions.displacement.deep           # 深载
dimensions.displacement.max            # 试航实测（navypedia 并列的那种）
dimensions.length.oa                  # 全长 overall
dimensions.length.wl                  # 水线长 waterline
dimensions.length.pp                  # 垂线间长
dimensions.beam.wl                    # 水线宽（Wikidata P2261）
dimensions.beam.max                   # 最大宽（Wikidata P2049）
dimensions.beam.molded                # 型宽
dimensions.draught.mean               # 平均吃水
dimensions.draught.max                # 最大吃水（Wikidata P2262）
dimensions.freeboard                  # 干舷
dimensions.metacentric_height.gm      # 稳心高（试航实测，Bismarck 打过样就有 GM）
dimensions.block_coefficient          # 方形系数
```

### 组 3 · `propulsion` — 动力与推进

``` 
propulsion.plant_type            # 蒸汽轮机 / 柴油机 / 燃机 / 核
propulsion.shafts                # 轴数（navypedia "No of shafts"）
propulsion.boiler.count
propulsion.boiler.type           # 例：Wagner 高压水管锅炉
propulsion.boiler.pressure_atm
propulsion.boiler.temperature_c
propulsion.turbine.count
propulsion.turbine.manufacturer  # 逐舰不同（Bismarck 用 Blohm & Voss，Tirpitz 用 Brown-Boveri）
propulsion.propeller.count
propulsion.propeller.diameter_m
propulsion.rudder.count
propulsion.power.design_hp       # 设计功率
propulsion.power.trial_hp         # 试航实测功率
propulsion.fuel.oil_t              # 燃油携带量
propulsion.fuel.type              # 燃料种类
propulsion.maneuver.turning_radius # 回转直径
propulsion.maneuver.rudder_angle   # 最大舵角
```

> 注：`speed.*` 与 `range.*` 建议**并入本组**（`propulsion.speed.max` / `propulsion.range.max`），因为航速航程是动力系统的输出指标，放一起对比器读起来才顺；若要独立成组，理由只能是"现代舰还要挂巡航/静音航速"，此时另立 `mobility` 组。

### 组 4 · `protection` — 装甲与防护

**按部位分行，每行再用 `.thickness` / `.thickness_top` / `.thickness_bottom` / `.angle` 四件套。** 部位词表直接取自 navypedia 的实证切分法。

```
protection.armor.belt.thickness          / .thickness_top / .thickness_bottom
protection.armor.belt.length_m
protection.armor.belt.height_m
protection.armor.upper_belt.thickness
protection.armor.deck.main.thickness
protection.armor.deck.upper.thickness
protection.armor.deck.lower.thickness
protection.armor.deck.slope.thickness / .angle
protection.armor.bulkhead.torpedo.thickness
protection.armor.bulkhead.splinter.thickness
protection.armor.turret.face.thickness   / .side / .rear / .roof
protection.armor.barbette.thickness_above / .thickness_below
protection.armor.secondary_turret.face
protection.armor.conning_tower.fore.thickness / .roof
protection.armor.conning_tower.aft.thickness
protection.torpedo_bulge.depth_m
protection.torpedo_bulge.type
protection.underwater_protection.depth_m
protection.armor.weight_t               # 装甲总重
protection.armor.weight_ratio           # 占排水量百分比（navypedia 给了 44%）
protection.scheme                       # 装甲布置体系：all-or-nothing / incremental
protection.mine_protection
```

> `armor.*` 一律标 `compare: false` 或 `compare: context`——厚度不是越大越好（倾角、材质、布置同样重要），与框架 §3.4 的 `better: context` 呼应。

### 组 5 · `armament` — 武备装载

**两层：装载（本组，属于舰）引用 武器实体（独立表，字段见 `weapon.*`）。**

``` 
armament.mount.id                 # 装载实例 id，如 turret Anton
armament.mount.label             # 炮位名（Anton / Bruno / Cäsar / Dora）
armament.mount.type              # turret / barbette / casemate / open_mount / tube / rack
armament.mount.weapon_id         # 指向 weapon 实体
armament.mount.count             # 数量（如 4x2）
armament.mount.barrels           # 每座炮管数
armament.mount.position          # 位置：fore / aft / midships_port …
armament.mount.arc               # 射界
armament.mount.elevation_max     # 该装载的仰角上限（可能改于武器本体）
armament.mount.installed_at      # 装舰时间 → 走 fact
armament.mount.removed_at        # 拆除时间 → 走 fact
armament.torpedo.tube_count
armament.torpedo.tube_diameter_mm
armament.torpedo.weapon_id
armament.depth_charge.count
armament.mine.capacity
armament.total_weight_t
armament.broadside_weight_kg     # 舷侧齐射重量，对比器最好用的一项
```

独立武器实体 `weapon.*`（照 combinedfleet 炮页 + Wikidata）：

``` 
weapon.id / weapon.designation / weapon.type / weapon.nation
weapon.bore_mm / weapon.caliber_length       # L/52 里的 52
weapon.barrel_weight_t / weapon.length_oa_m
weapon.projectile_weight_kg
weapon.muzzle_velocity_mps
weapon.elevation_min_deg / .max_deg
weapon.range_max_m / weapon.range_aa_m
weapon.rate_of_fire_rpm
weapon.ammo_types                 # AP / HE / AA / SAP，多值
weapon.penetration_table          # 距离-穿深 表（穿深查询器用）
weapon.in_service_from / .to
weapon.used_by                    # 反向索引到舰/级
```

### 组 6 · `sensors` — 探测、火控、电子战

维基的 `sensors` 只有一个字段、`EW` 一个字段——这是必须拆的地方。

``` 
sensors.radar.*                   # 按型号多值，各带数量与装/拆时间
  sensors.radar.model             # FuMO 23 / Type 21 / SG …
  sensors.radar.count
  sensors.radar.function          # search / fire-control / surface / air
  sensors.radar.band
  sensors.radar.installed_at / .removed_at
sensors.sonar.model / .count / .function
sensors.fire_control.director_count
sensors.fire_control.director_type   # 主/副/高炮指挥仪分开
sensors.fire_control.rangefinder_baseline_m   # 基线长（10.5 m 这种）
sensors.fire_control.rangefinder_count
sensors.combat_system                # 现代舰战斗系统
sensors.ecm.suite                    # FuMB 4 / FuMB 7
sensors.decoy                         # 诱饵/干扰弹
sensors.iif                           # 敌我识别
sensors.compass.gyro_count
```

### 组 7 · `aviation` — 航空设施

``` 
aviation.aircraft.capacity            # 搭载架数
aviation.aircraft.types               # 机型，多值（Ar196、Fieseler Fi 156…）
aviation.hangar.count
aviation.catapult.count
aviation.catapult.type                # 弹射器/旋转弹射器
aviation.crane.count
aviation.recovery.arrestor             # 拦阻索（航母用）
aviation.flight_deck.length_m
aviation.flight_deck.width_m
aviation.elevator.count
aviation.avgas_t                       # 航空燃油
```

### 组 8 · `construction` — 建造与改装

``` 
construction.builder                   # 建造厂（navypedia 单列）
construction.builder_location
construction.yard_number
construction.order_date
construction.laid_down_date
construction.launched_date
construction.commissioned_date
construction.fate_date
construction.fate_type                 # sunk / scrapped / scuttled / preserved …
construction.building_time_days        # 可派生，不手填
construction.refit.list                # 改装事件流，见下方 event 模型
construction.cost
construction.displacement_declared_t   # 政治申报值！与真实值并存（Bismarck 申报 35,000 t vs 实际）
```

> 最后一项是这次调研逼出来的：navypedia 明写"官方宣布 35,000 t，实际多 7,000 t"。**"申报值"和"实际值"是不同字段，不是分歧**——正好对应框架 §5.3 第 1 条"先判口径冲突"。

### 组 9 · `service` — 服役、编制、人员、战果

``` 
service.flag                          # 旗号/国籍，区间
service.unit                          # 所属编队，区间表（uboat.net Career）
service.unit.from / .to
service.commander.name / .rank / .from / .to / .decorations
service.complement.standard           # 编制人数
service.complement.wartime            # 战时编制
service.complement.officers
service.manpower.lost                 # 阵亡，附日期与原因（uboat.net Men lost）
service.battle_participated           # 关联 battle 实体
service.successes.ships_sunk
service.successes.tonnage_sunk_grt
service.successes.ships_damaged
service.fate.category                 # 结局枚举
service.fate.assessment_authority     # 判定机构（uboat.net 的 "FDS/NHB"）
service.fate.assessment_date
service.fate.previous_records         # 被推翻的旧结论，留链（uboat.net Previously recorded fate）
service.honors                        # 荣誉/战斗之星
```

### 组 10 · `appearance` — 涂装与标识

``` 
appearance.scheme.id                  # 涂装方案实体引用（Measure 21 / Baltic stripe …）
appearance.scheme.valid_from / .valid_to
appearance.scheme.reference_view      # 对应侧视参考图 image_id
appearance.scheme.authority_doc       # 依据文件（官方 Painting & Cementing 通告）
appearance.colors.hull
appearance.colors.superstructure
appearance.colors.deck
appearance.colors.boot_topping
appearance.colors.measure_number      # USN Measure 编号
appearance.markings.pennant_style
appearance.markings.dazzle_pattern    # 迷彩图案名（disruptive / dazzle / splinter）
appearance.markings.bow_wave          # 假艏波等欺骗涂装
appearance.insignia.decal             # 舰徽/艇徽，多值（uboat.net Emblems）
```

### 组 11 · `media` — 影像、线图、图纸

``` 
media.image.id / .caption / .date_taken / .location
media.image.part_index                # ← 部位索引（我们的差异化）
media.image.source / .license / .credit
media.image.view                      # bow / stern / broadside / deck / detail
media.plan.id                          # 线图/图纸实体
media.plan.scale                       # 1:1000（the-blueprints 实证）
media.plan.projections                 # top / side / section（同样实证）
media.plan.format                      # pdf / svg / dwg / dxf / ai
media.plan.model_year                  # 该图对应的时间切片（the-blueprints "Model years"）
media.plan.block_scheme                # A4 / A3 分块数，可打印用
media.plan.baseline_mm                 # 图上 1 cm 对应实际多少 mm
media.plan.accuracy_note               # 依据哪些图纸、哪些是推测
```

### 组 12 · `modelling` — 模型套件与改造

``` 
modelling.kit.id / .manufacturer / .name / .kit_number / .scale
modelling.kit.release_year
modelling.kit.status                  # in_production / discontinued / unknown（枚举，不是布尔）
modelling.kit.discontinued_at
modelling.kit.ship_id                 # 多对多：一套件可对应多舰/多级
modelling.kit.represents_state        # 套件呈现的是哪个时间切片/状态
modelling.kit.material                # injection / resin / wood / 3d-print
modelling.kit.parts_count
modelling.kit.review_ref              # 评测链接
modelling.kit.builds_count            # 热度信号（suburbanshipmodeler 实证）
modelling.aftermarket.item            # 蚀刻/木甲板/炮管/涂装模板，多值
modelling.aftermarket.maker
modelling.conversion.note             # 改造参考：哪套件改成哪套
modelling.paint_set                   # 配套漆（Snyder & Short 那种漆片套装）
```

> `modelling.kit.status` 用枚举 + `discontinued_at` 时间戳，而不是 `in_stock` 布尔——理由来自 suburbanshipmodeler 自承"数据一发布即过时"的教训。

### 元数据组（横切，不算内容组）

``` 
provenance.source_id / .tier / .url / .fetched_at
provenance.confidence                 # A–E，对应框架 §5.2
provenance.disputed                   # 自动派生：同 field 同窗多条即 true
provenance.note
provenance.supersedes                 # 修正链，指向被取代的 fact
```

---

## 五、几条硬结论（写进注册表设计时的约束）

1. **日期不占字段位。** `service.commander.*` 这类不能用 `service.commander` 单值字段，必须走 `fact` 的 `valid.from/to`（框架 §3.2 已有），或事件流的 qualifier（Wikidata P585 做法）。维基与 Naval Encyclopedia 都在这里失败——它们的"改装"是散文。
2. **尺寸必须带口径后缀**，且是独立字段不是同一个字段的别名。`length.oa` / `length.wl` / `length.pp` 三个都要有；`beam.wl` 与 `beam.max` 也是。Naval Encyclopedia 把三个尺寸挤进一个 `Dimensions` 字符串，等于放弃对比。
3. **装甲是唯一"天然按部位"的字段域**，navypedia 已经证明部位词表可枚举（十项左右）。从这一域开始试点 `part_index` 机制，比从图片索引开始容易得多——数据源现成，不需要先有图。
4. **事件要能表达"不完整的日期"**。TROM 混用五种精度是内容真实样貌，不是懒惰。`valid.from/to` 得允许 `{year, month?, day?}` 三级精度，以及 `precision: exact | day | month | period | vague` 标记。
5. **推翻旧结论要有位置。** uboat.net 的 `Previously recorded fate` 证明：读者要的不是唯一答案，是"为什么变了"。`provenance.supersedes` + `provenance.note` 两个字段就能承载。
6. **"申报值 vs 实际值"是不同字段，不是分歧。** 框架 §5.3 第 1 条（先判口径冲突）在字段注册表层的实现方式就是：把它们命名成两个不同 field。
7. **套件、涂装、线图都必须是独立实体 + 时间戳**，不能是挂在舰上的一张图或一个布尔。三个方向的外部证据一致指向同一个失败模式：**没有生效区间的关联，等于没有关联**。

---

## 引用清单

**一手抓取成功**
- https://en.wikipedia.org/wiki/Template:Infobox_ship
- https://www.wikidata.org/wiki/Wikidata:WikiProject_Ships
- https://www.combinedfleet.com/kaigun.htm · https://www.combinedfleet.com/senkan.htm · https://www.combinedfleet.com/yamato.htm · https://www.combinedfleet.com/guns.htm · https://www.combinedfleet.com/460_45.htm
- https://uboat.net/boats/u47.htm
- https://naval-encyclopedia.com/ww1/uk/s-class-destroyer.php · https://naval-encyclopedia.com/goodies/ships-model-kits-modellers-corner.php
- https://www.navypedia.org/ships/germany/ger_bb_bismarck.htm
- https://www.shipcamouflage.com/ · https://www.shipcamouflage.com/warship_camouflage.htm
- https://suburbanshipmodeler.com/model-ship-kit-database/
- https://www.the-blueprints.com/blueprints/ships/battleships-germany/ · https://www.the-blueprints.com/vectordrawings/show/7153/dkm_bismarck/
- https://www.worldwarphotos.info/gallery/germany/kriegsmarine/bismarck/

**抓取失败 / 不可用（结论中已标注，未作为证据）**
- navweaps.com 全站：`index_weapons.php`、`WNUS_16-50_mk7.php`、`WNUS_16-45_mk1.php`、`WNGER_15-52_skc34.php` — 均 30s timeout；web.archive.org 两时点快照同样 timeout；`r.jina.ai` 代理 ECONNRESET。
- scalemates.com/kits/ — Access Denied (Akamai, Reference #18.1335cb17…)。
- naval-encyclopedia.com 旧 slug（`/ww2/germany/battleship-bismarck.php` 等）— 302 回首页。
- modelshipgallery.com/gallery/index.html — 返回空壳。
- hnsa.org 船图页 — 404。
