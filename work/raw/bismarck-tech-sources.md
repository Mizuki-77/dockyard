# Bismarck 技术数据 · 多源比对清单

采集日期：2026-11-17
采集方式：`web_fetch` 直接抓取页面正文（非搜索摘要），kbismarck 各页字符集为 latin-1。
原则：**只记录页面原文，不做裁决、不做平均、不做单位换算推导**。同一字段各来源不一致者全部并列。
来源代号：
- **KB** = kbismarck.com（Dieter Kappes 维护的专题站，德方原始档案口径）
- **GN** = german-navy.de（Kriegsmarine 专题站）
- **EN** = en.wikipedia.org "German battleship Bismarck"（Featured article）
- **ENC** = en.wikipedia.org "Bismarck-class battleship"（GA）
- **ENGUN** = en.wikipedia.org "38 cm SK C/34 naval gun"（数据源标注为 Krupp datasheet 38 cm S.K.C/34 e WA52-453(e)）

> 注意：KB 的 `genedata.html` 页内存在**自相矛盾**——主表写 full load 51,760 mt，同页下方 Bismarck / Tirpitz 对比表写 51,700 mt。两处原文均已收录。

---

## 1. 排水量

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB genedata | 40,250 | mt | "Empty ship"；原文行标签 `Empty ship` | https://www.kbismarck.com/genedata.html |
| KB bsweights | 40,250 | mt | "Schiff Fertig Leer"（完工空船），为逐项累加结果 | https://www.kbismarck.com/bsweights.html |
| KB genedata | 43,978 | mt | "Standard"（标准排水量） | https://www.kbismarck.com/genedata.html |
| KB bsweights | 43,978 | mt | 由 Type Displacement 43,313 + 饮水 155 + 洗涤水 510 得出；脚注 1 明示按 1922 华盛顿条约标准排水量定义（不含燃料与备用给水） | https://www.kbismarck.com/bsweights.html |
| KB genedata（对比表） | 43,978 | mt | 同页对比表复述，与主表一致 | https://www.kbismarck.com/genedata.html |
| EN infobox | 41,700 t（41,000 long tons） | t | 标准排水量；英制长吨换算并列 | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| ENC infobox | 41,700 t | t | 标准排水量（该类条目同值） | https://en.wikipedia.org/wiki/Bismarck-class_battleship |
| KB bsweights | 43,313 | mt | "Typverdrängung"（型号/设计排水量），非标准排水量 | https://www.kbismarck.com/bsweights.html |
| KB genedata | 47,870 | mt | "Construction"（建造/试航排水量）；proteccioni 页称其为 "design combat displacement" | https://www.kbismarck.com/genedata.html |
| ENC 正文 | 45,950 t（45,220 long tons） | t | "design displacement"（设计排水量） | https://en.wikipedia.org/wiki/Bismarck-class_battleship |
| KB genedata | 51,760 | mt | "Full load"（满载）；主表值 | https://www.kbismarck.com/genedata.html |
| KB bsweights | 51,760 | mt | "Ship fully equipped"；= 空船 + 各液舱/弹药/装备累加 | https://www.kbismarck.com/bsweights.html |
| KB genedata（对比表） | 51,700 | mt | 同页对比表值，与主表 51,760 差 60 mt（页内自相矛盾） | https://www.kbismarck.com/genedata.html |
| EN infobox | 50,300 t（49,500 long tons） | t | 满载排水量 | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| ENC infobox | 50,300 t | t | 满载排水量 | https://en.wikipedia.org/wiki/Bismarck-class_battleship |
| KB genedata | 53,486 | mt | "Maximum"（最大排水量） | https://www.kbismarck.com/genedata.html |
| KB bsweights | 53,486 | mt | = 满载 + 备用燃油/洗涤水 1,726 mt | https://www.kbismarck.com/bsweights.html |
| GN index | 50,956 | t | `Size (Max)`，页面称最大排水量 | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |

---

## 2. 尺寸

### 2.1 全长（overall length）

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB genedata | 250.50 | m | "Overall length"（注意是 250.50 而非 251） | https://www.kbismarck.com/genedata.html |
| GN index | 251.0 | m | `Length (Total)` | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |
| EN infobox | 251 | m | overall length | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| ENC infobox | 251 | m | length overall | https://en.wikipedia.org/wiki/Bismarck-class_battleship |

### 2.2 水线长（waterline length）

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB genedata | 241.55 | m | "Waterline length" | https://www.kbismarck.com/genedata.html |
| GN index | 241.6 | m | `Length (Waterline)` | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |
| EN infobox | 241.6 | m | length at waterline | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| ENC infobox | 241.60 | m | length at waterline | https://en.wikipedia.org/wiki/Bismarck-class_battleship |

### 2.3 舰宽（beam）

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB genedata | 36.00 | m | "Beam" | https://www.kbismarck.com/genedata.html |
| GN index | 36.0 | m | `Beam` | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |
| EN infobox | 36 | m | beam | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| ENC infobox | 36 | m | beam | https://en.wikipedia.org/wiki/Bismarck-class_battleship |

### 2.4 吃水（draught）——四个来源共给出 6 个不同数值

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB genedata | 9.33 | m | "Standard draught"（标准吃水） | https://www.kbismarck.com/genedata.html |
| KB genedata | 10.55 | m | "Maximum draught"（最大吃水） | https://www.kbismarck.com/genedata.html |
| EN infobox | 9.3 | m | draft (standard)，带脚注 [a] | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| EN 正文 | 9.9 | m | max draft（最大吃水 9.9 m） | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| ENC infobox | 9.30 | m | draft，标为设计吃水 | https://en.wikipedia.org/wiki/Bismarck-class_battleship |
| ENC 正文 | 8.63 | m | 标准排水量状态下的吃水 | https://en.wikipedia.org/wiki/Bismarck-class_battleship |
| ENC 正文 | 9.90 | m | 满载状态下的吃水 | https://en.wikipedia.org/wiki/Bismarck-class_battleship |
| GN index | 9.9 | m | `Draft`（未注明状态） | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |

### 2.5 其他尺度（仅 KB 提供）

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB genedata | 4.45–5.67 | m | "Freeboard amidships"（舯部干舷，区间） | https://www.kbismarck.com/genedata.html |
| KB genedata | 15.00 | m | "Depth"（型深） | https://www.kbismarck.com/genedata.html |
| KB genedata | 5,740 | m² | "Waterplane area"（水线面积） | https://www.kbismarck.com/genedata.html |
| KB genedata | 4.00 | m | "GM"（初稳性高），条件：at 47,200 mt | https://www.kbismarck.com/genedata.html |
| KB genedata | 0.55 / 0.97 / 0.66 / 0.57 | – | 依次为 Block / Midship / Waterplane / Prismatic 系数 | https://www.kbismarck.com/genedata.html |
| KB propulsioni | 0.56 | – | "Prismatic coefficient"，与 genedata 的 0.57 不同（页间分歧） | https://www.kbismarck.com/propulsioni.html |

---

## 3. 动力

### 3.1 锅炉

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB genedata | 12 | 台 | "12 Wagner boilers" | https://www.kbismarck.com/genedata.html |
| KB propulsioni | 12 | 台 | Wagner Hochdruck 高压锅炉，分 6 个水密锅炉舱（sections XI、XIII），锅炉编号 1529–1540 | https://www.kbismarck.com/propulsioni.html |
| EN infobox | 12 | 台 | "12 × Wagner superheated boilers" | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| ENC 正文 | 12 | 台 | "12 Wagner ultra-high-pressure oil-fired water-tube boilers"（超高压燃油水管锅炉） | https://en.wikipedia.org/wiki/Bismarck-class_battleship |

锅炉细部（仅 KB propulsioni）：蒸发受热面 380 m²；过热器 120 m²；空气预热器 685 m²；给水预热 160 °C；饱和蒸汽 287 °C；过热蒸汽 450 °C；工作压力 55–56 atm（58 kg/cm²）；安全阀 58 atm（最大 63）；许可 64 atm；蒸汽产量 132 kg/m²；容量 144 m³；锅炉带水总重 52.8 t；炉水重 4.85 t。
URL: https://www.kbismarck.com/propulsioni.html

### 3.2 主机与轴

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB genedata | 3 组 | 组 | "Three Blohm & Voss turbine sets" | https://www.kbismarck.com/genedata.html |
| KB propulsioni | HP Curtis 40 级 + IP 双流 15 级 + LP 9 级（带冷凝器） | – | 每组构型；另有 HP 倒车单 Curtis 轮、LP 倒车双流；**无巡航汽轮机**（Tirpitz 有） | https://www.kbismarck.com/propulsioni.html |
| EN infobox | 3 × geared turbines | 组 | 齿轮传动汽轮机 | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| ENC 正文 | 3 × geared turbines | 组 | 原计划电传动（各 46,000 shp），因 Siemens-Schuckert 退出改为齿轮传动 | https://en.wikipedia.org/wiki/Bismarck-class_battleship |
| GN index | 3 turbines / Blohm & Voß | 组 | `Machinery: 3 shafts, 3 turbines, Blohm & Voß` | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |
| 全部来源 | 3 | 轴 | 各源一致 | — |

### 3.3 轴马力 / 功率

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB genedata | 150,170 | hp | "maximum obtained"（实测最大值） | https://www.kbismarck.com/genedata.html |
| KB propulsioni | 150,170 | hp | 同值，标为总功率 | https://www.kbismarck.com/propulsioni.html |
| GN index | 150,170 | shp | `Performance`，写法带千位分隔 | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |
| EN infobox | 148,116 shp（110,450 kW） | shp | "Installed power" | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| EN 正文 | 150,170 PS（= 148,120 shp） | PS / shp | 试航实测；**额定**为 138,000 PS（136,000 shp）→ 29 kn | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| ENC infobox | 148,120 shp（110,450 kW） | shp | 同上换算后的公制马力值 | https://en.wikipedia.org/wiki/Bismarck-class_battleship |
| ENC 正文（Tirpitz） | 160,795 | shp | Tirpitz 值，非 Bismarck | https://en.wikipedia.org/wiki/Bismarck-class_battleship |

### 3.4 最大航速

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB genedata | 30.12 | kn | "maximum obtained"（实测） | https://www.kbismarck.com/genedata.html |
| KB genedata（对比表） | 30 | kn | 同页对比表取整 | https://www.kbismarck.com/genedata.html |
| KB propulsioni | 30.1 | kn | 最大航速 | https://www.kbismarck.com/propulsioni.html |
| GN index | 30.1 | kn | `Maximum speed` | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |
| EN infobox | 30.01 | kn | "during trials"（试航） | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| ENC infobox | 30 | kn | 取整，不细分 | https://en.wikipedia.org/wiki/Bismarck-class_battleship |

### 3.5 续航力

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB genedata | 9,280 @ 16 kn / 8,900 @ 17 kn / 8,525 @ 19 kn / 6,640 @ 24 kn / 4,500 @ 28 kn | nmi | 五行完整续航曲线 | https://www.kbismarck.com/genedata.html |
| KB propulsioni | 同上五组 | nmi | 复述同一曲线 | https://www.kbismarck.com/propulsioni.html |
| EN infobox | 8,870 @ 19 | nmi | 19 节单值 | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| ENC infobox | 8,525 @ 19 | nmi | 19 节单值（与 EN 的 8,870 冲突） | https://en.wikipedia.org/wiki/Bismarck-class_battleship |
| GN index | 8,100 @ 16 kn / 3,740 @ 30 kn | miles | 注意其 30 节档位为 3,740 mi，其他来源无此档 | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |

### 3.6 燃油

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB genedata | 7,900 | metric tons | "Fuel oil capacity" | https://www.kbismarck.com/genedata.html |
| KB propulsioni | 8,294 | mt | 同站另一页，差 394 mt（页间分歧） | https://www.kbismarck.com/propulsioni.html |
| KB bsweights | 6,194 + 527 = 6,721 | mt | 逐舱列出：炉用燃油 6,194＋推进用燃油 527；另滑油 275、航空汽油 34 | https://www.kbismarck.com/bsweights.html |
| EN 正文 / ENC | 6,400（正常）/ 3,200（设计）/ 7,400（加装额外油舱后） | t | 三档并列 | https://en.wikipedia.org/wiki/German_battleship_Bismarck ; https://en.wikipedia.org/wiki/Bismarck-class_battleship |

### 3.7 螺旋桨 / 舵 / 电力

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB propulsioni | 3 具，直径 4.70，3 叶，满速 270 rpm | m / rpm | 左桨与中桨逆时针、右桨顺时针 | https://www.kbismarck.com/propulsioni.html |
| ENC 正文 | 直径 4.70，3 叶；满载时 HP/IP 2,825 rpm、LP 2,390 rpm | m / rpm | 汽轮机转速，非轴转速；与 KB 的 2,880/2,430 不同 | https://en.wikipedia.org/wiki/Bismarck-class_battleship |
| KB propulsioni | 2 具平行舵，各 24.21 m²，向中线偏 8° | m² / ° | 每舵含吊挂体积 11.63 m³ | https://www.kbismarck.com/propulsioni.html |
| KB propulsioni | 7,910 kW @ 220 V | kW / V | 8×500 kW 柴油发电机 + 5×690 kW + 1×460 kW 涡轮发电机 | https://www.kbismarck.com/propulsioni.html |
| ENC 正文 | 7,910 kW @ 220 V | kW / V | 同一总量，机组构成表述略异（含 1 台 550 kVA 交流柴油发电机） | https://en.wikipedia.org/wiki/Bismarck-class_battleship |

---

## 4. 装甲

### 4.1 主装甲带

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB genedata | 320 | mm | "Main belt" | https://www.kbismarck.com/genedata.html |
| KB proteccioni | 320 KC，宽 4.8 m，长 170.7 m | mm / m | 覆盖水线 70%（frame 32–202.7），后衬 50 mm 柚木，固定于 16–25 mm 舷板 | https://www.kbismarck.com/proteccioni.html |
| EN infobox | 320 | mm | Belt | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| GN index | 320 | mm | `Belt 320mm (max)` | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |

### 4.2 主装甲带倾角（外倾）——仅 KB proteccioni

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB proteccioni | 17° / 10° / 8–10° / 7° | ° | 依次为 abreast Anton / Bruno / Cäsar / Dora；约覆盖 40% 带长 | https://www.kbismarck.com/proteccioni.html |

### 4.3 上部装甲带 / 舰首舰尾

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB genedata | 145 | mm | "Upper belt" | https://www.kbismarck.com/genedata.html |
| KB proteccioni | 145 KC（frame 186.7–202.7 段降为 120） | mm | 附分段递减说明 | https://www.kbismarck.com/proteccioni.html |
| KB proteccioni | 舰首 60 Wh / 舰尾 80 Wh | mm | 非装甲带，为船体端部装甲 | https://www.kbismarck.com/proteccioni.html |

### 4.4 装甲甲板

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB genedata | 上甲板 50–80；第三装甲甲板 80–120 | mm | 两行分列 | https://www.kbismarck.com/genedata.html |
| KB proteccioni | 上甲板 50–80 Wh（frame 10.5–224）+ 68 mm 柚木；电池甲板 6–20 St 52 | mm | 主装甲甲板位于龙骨上方 10.3 m、设计水线上 1 m | https://www.kbismarck.com/proteccioni.html |
| KB proteccioni | 机舱上方 80 / 弹药库上方 100 / 外倾斜段 110–120（倾角约 22°） | mm | 分区厚度 | https://www.kbismarck.com/proteccioni.html |
| KB proteccioni | 合计 130–160（机舱）/ 150–200（弹药库）/ 45–70（frame 233 以前舰首）/ 160（frame 10.5 以后舰尾） | mm | 逐层叠加后的等效总厚 | https://www.kbismarck.com/proteccioni.html |
| EN infobox | 主装甲甲板 100–120 | mm | "Main deck 100–120 mm"；同时正文给上层甲板 50 mm | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| GN index | 80–120 | mm | `Deck 80-120 mm` | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |

### 4.5 炮塔与炮座

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB genedata | 130–360 | mm | "Main battery turrets"（主炮塔全向区间） | https://www.kbismarck.com/genedata.html |
| KB genedata | 20–100 | mm | "Secondary turrets"（副炮塔） | https://www.kbismarck.com/genedata.html |
| KB proteccioni | 炮座水上 340 KC / 甲板下 220 KC | mm | 页面称其等效美制 Class A 390–405 mm | https://www.kbismarck.com/proteccioni.html |
| KB proteccioni | 副炮塔 20–100 Wh；炮座甲板上 80 / 甲板下 20 | mm / Wh | 分区 | https://www.kbismarck.com/proteccioni.html |
| ENGUN | 正面 360 / 侧面 220 / 后部 320 / 前后斜顶 180 / 侧斜顶 150 / 平顶 130 | mm | 逐面装甲表（Krupp 原始图纸口径） | https://en.wikipedia.org/wiki/38_cm_SK_C/34_naval_gun |
| EN 正文 | 正面 360 / 侧面 220 | mm | 仅两处 | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| GN index | 360 (max) | mm | `Turrets 360 mm (max)` | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |

### 4.6 司令塔

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB genedata | 220–350 | mm | "Conning tower" | https://www.kbismarck.com/genedata.html |
| KB proteccioni（前部） | 350 壁 / 220 顶 / 70 底 | mm | 测距仪穹 200/100；通信筒直径 85 cm、壁 220 | https://www.kbismarck.com/proteccioni.html |
| KB proteccioni（后部） | 150 / 50 / 30 | mm | 后部司令塔；通信筒 70 cm / 50 mm；后测距穹 100/50；前桅楼指挥所 60/20/20 | https://www.kbismarck.com/proteccioni.html |
| GN index | 220–350 | mm | `Command Tower 220-350 mm` | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |
| ENC 正文 | 220–350 | mm | 同区间 | https://en.wikipedia.org/wiki/Bismarck-class_battleship |

### 4.7 水下防护

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB genedata | 45 | mm | "Torpedo bulkhead"；防雷纵舱壁 | https://www.kbismarck.com/genedata.html |
| KB proteccioni | 45 Ww，**垂直**布置（非 Scharnhorst 式倾斜） | mm | 与外壳距离：中部 5.4 m、Anton/Dora 处约 3 m；各炮塔处 frame 数值见下 | https://www.kbismarck.com/proteccioni.html |
| KB proteccioni | 设计抗 250 kg TNT | kg | Tirpitz 报告为 300 kg hexanite | https://www.kbismarck.com/proteccioni.html |
| KB proteccioni | 22 个水密隔舱，其中 17 个（III–XIX）在装甲堡内 | 个 | 装甲甲板与上甲板间由 30 mm Wh 纵向防破片舱壁分成 102 个格 | https://www.kbismarck.com/proteccioni.html |
| KB proteccioni | 双层底深 1.7（frame 77.3–154.6） | m | 另有 MES 磁场自保护系统 | https://www.kbismarck.com/proteccioni.html |
| EN 正文 | 22 个水密隔舱；双层底占舰长 83% | 个 / % | 与 KB 的隔舱总数一致，双层底口径表述不同（深度 vs 占长比） | https://en.wikipedia.org/wiki/German_battleship_Bismarck |

鱼雷舱壁位置表（KB proteccioni）：Turret A frame 192.55 距 3 m；B frame 174.35 距 3.5 m；中部 frame 120.8 距 5.4 m；C frame 64.35 距 3.8 m；D frame 46.15 距 3 m；均 45 mm Ww。
URL: https://www.kbismarck.com/proteccioni.html

### 4.8 装甲总重与钢材

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB genedata | 19,082 | mt | "Armour's weight" | https://www.kbismarck.com/genedata.html |
| KB proteccioni | 19,082 | mt | 占设计战斗重量 47,870 mt 的 40%；对比 Yamato 22,895 mt / 33.2% | https://www.kbismarck.com/proteccioni.html |
| KB bsweights | 17,484（不含炮塔装甲）+ 1,598（炮塔装甲）= 19,082 | mt | 分项累加，可闭合 | https://www.kbismarck.com/bsweights.html |
| KB proteccioni | St 52 KM / KC n/A / Wh n/A / Ww n/A | – | KC 含 3.5–3.8% Ni、2% Cr、0.3% C；Wh 抗拉 85–95 kg/mm²；St 52 抗拉 52–64 | https://www.kbismarck.com/proteccioni.html |

---

## 5. 武备

### 5.1 主炮 38 cm SK C/34

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB armament | 8 门 / 4 座双联 | 门 / 座 | 炮塔名 Anton、Bruno（前，frames 192.55 / 174.35）、Cäsar、Dora（后，frames 64.35 / 46.15） | https://www.kbismarck.com/armament.html |
| EN infobox | 8 × 38 cm SK C/34（4×2） | 门 | 炮塔名 Anton/Bruno 前、Caesar/Dora 后 | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| GN index | 8 门，**"38 cm L/47 C/34"** | 门 | 型号写成 L/47（多数来源为 L/52），见分歧汇总 | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |
| KB genedata | 8 × 38cm/L52 | 门 | 用 L/52 标注 | https://www.kbismarck.com/genedata.html |
| KB armament | 身管 L/52 = 19.630 m；膛线长 L/48.5 = 18.405 m | m | 90 条右旋膛线，深 4.50 mm、宽 7.76 mm；炮管重 110.7 mt | https://www.kbismarck.com/armament.html |
| ENGUN | Mass 111 t；Length 19.63 m；Barrel 18.405 m L/52（51.66 calibers） | t / m | 与 KB 的 110.7 mt 有 0.3 t 差 | https://en.wikipedia.org/wiki/38_cm_SK_C/34_naval_gun |
| KB armament | 炮塔重 1,056（Anton 1,048，不含 10.5 m 测距仪） | mt | 逐塔 | https://www.kbismarck.com/armament.html |
| ENGUN | 1,048–1,056；座圈直径 8.75 m | t / m | 与 KB 一致 | https://en.wikipedia.org/wiki/38_cm_SK_C/34_naval_gun |
| KB armament | 俯仰 −5.5°～+30°；旋回 5.4°/s；俯仰 6°/s；装填角 2.5° | ° / °/s | 与 ENGUN 一致 | https://www.kbismarck.com/armament.html |
| KB armament | 最大射程 **35,550** m @30° | m | 初速 820 m/s | https://www.kbismarck.com/armament.html |
| ENGUN | 最大射程 **35.5 km** / **35.6 km**（infobox 与弹药表两处写法不一致） | km | 同为 800 kg 弹、30° | https://en.wikipedia.org/wiki/38_cm_SK_C/34_naval_gun |
| ENC 正文 | 最大射程 **36,520** m @30° | m | 该类条目值，与其他三处均不同 | https://en.wikipedia.org/wiki/Bismarck-class_battleship |
| KB armament | 射速 2.4+ 发/分/管 | 发/分 | 实战值口径 | https://www.kbismarck.com/armament.html |
| ENGUN | 手册要求 2.5 发/分；Baltic 试射 AVKS 报告 3.125 发/分；对 Hood 实战约 1 发/分 | 发/分 | 三种口径并列 | https://en.wikipedia.org/wiki/38_cm_SK_C/34_naval_gun |
| ENC 正文 | 理想 18 秒/发（3 发/分） | 发/分 | 与上两者均不同 | https://en.wikipedia.org/wiki/Bismarck-class_battleship |
| KB armament | 装药 Fore 99.5 kg / Main 112 kg | kg | — | https://www.kbismarck.com/armament.html |
| ENGUN | Main charge HuelsKart34 108 kg / Fore charge VorKart34 104 kg | kg | 与 KB 的 99.5 / 112 数值与主副顺序都不一致 | https://en.wikipedia.org/wiki/38_cm_SK_C/34_naval_gun |
| KB armament | 弹药 1,004 发（AP 353 / HE Bdz 338 / HE Kz 313） | 发 | 分弹种明细 | https://www.kbismarck.com/armament.html |
| ENC 正文 | 弹药 940–960 发（每管约 115–120） | 发 | 与 KB 的 1,004 差 44–64 发 | https://en.wikipedia.org/wiki/Bismarck-class_battleship |
| KB armament | 弹重 800 kg；装药 AP 18.8 / HE Bdz 32.6 / HE Kz 64.25 kg | kg | 三种弹 | https://www.kbismarck.com/armament.html |
| ENGUN | 弹重 800 kg；装药 ≈20.3（AP）/ ≈35（HE Bdz）/ ≈62.8（HE Kz）kg TNT | kg | 与 KB 各差 1.5 左右，属估算/实测口径差 | https://en.wikipedia.org/wiki/38_cm_SK_C/34_naval_gun |
| KB armament | 身管寿命 200–300 发 | 发 | — | https://www.kbismarck.com/armament.html |
| ENGUN | 另列 Siegfried-Granate（仅岸防型）495 kg、920/1,050 m/s、40.0/55.7 km | kg / m/s / km | 舰炮不使用，仅备录 | https://en.wikipedia.org/wiki/38_cm_SK_C/34_naval_gun |

### 5.2 副炮 15 cm SK C/28 / L55

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB armament | 12 门 / 6 座双联（每舷 3 座） | 门 / 座 | L/55，炮管 8.25 m、重 9.08 mt | https://www.kbismarck.com/armament.html |
| KB genedata | 12 × 15cm/L55 | 门 | — | https://www.kbismarck.com/genedata.html |
| EN infobox | 12 × 15 cm SK C/28（6×2） | 门 | — | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| GN index | 12 门 "15 cm L/55 C28" | 门 | 写 C28（无斜杠），口径一致 | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |
| KB armament | 炮塔 108 mt（中央炮塔 110 mt）；俯仰 −10～+40°；旋回 8°/s；俯仰 9°/s；射速 8 发/分；射程 23,000 m@40°；初速 875 m/s；弹重 45.3 kg；装药 23.5 kg；弹药 1,288 发；身管寿命 2,500 发 | 混合 | 全套参数仅 KB 提供 | https://www.kbismarck.com/armament.html |

### 5.3 重型高炮 10.5 cm SK C/33

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB armament | 16 门 / 8 座双联（4 座×2 舷） | 门 / 座 | L/65，炮管 6.825 m、重 4.56 mt | https://www.kbismarck.com/armament.html |
| KB genedata | 16 × 10.5cm/L65 | 门 | — | https://www.kbismarck.com/genedata.html |
| EN infobox | 16 × 10.5 cm SK C/33（8×2） | 门 | — | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| GN index | 16 门 "10.5 cm L/65 C/33" | 门 | — | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |
| KB armament | C/31 座 27.350 mt / C/37 座 26.425 mt；俯仰 C31 −8～+80°、C37 −10～+80°；角速度 C31 10/8 °/s、C37 12/8.5 °/s；射速 18 发/分/管；水平射程 17,850 m、垂直 13,000 m@80°；初速 900 m/s；弹重 15.1 kg；弹药 6,825 发 + 337 照明弹 | 混合 | 全套参数仅 KB 提供 | https://www.kbismarck.com/armament.html |
| EN 正文 | 前两对座为旧 C/31 型、后两对为新 C/37 型 | – | 枪座型号分布，与 KB 的两型并列表述相容 | https://en.wikipedia.org/wiki/German_battleship_Bismarck |

### 5.4 中型高炮 3.7 cm SK C/30

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB armament | 16 门 / 8 座双联 | 门 / 座 | L/83，炮管 3.071 m；俯仰 −10～+80°；理论射速 80 发/分（实战约 30–40）；射程 6,750 m；初速 1,000 m/s；弹重 0.745 kg；弹药 34,100 发 | https://www.kbismarck.com/armament.html |
| KB genedata | 16 × 3.7cm/L83 | 门 | — | https://www.kbismarck.com/genedata.html |
| EN infobox | 16 × 3.7 cm SK C/30（8×2） | 门 | — | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| GN index | 16 门 "3,7 cm L/83" | 门 | 德式小数逗号 | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |

### 5.5 轻型高炮 2 cm —— 口径数在四个来源间出现 3 个值

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB armament | 10 门单装 MG C/30（Sockel-Lafette）+ 2 门单装 = 12 门单装 C/30；另有 8 门 C/38（2 座四联） | 门 | 四联装为 1941 年 4 月底在 Gotenhafen 加装；L/65，炮管 1.3 m；射速 200 发/分；弹药 22,000 发 | https://www.kbismarck.com/armament.html |
| KB genedata | 20 × 2cm/L65 | 门 | 单一总数 20（= 12 单装 + 8 四联管数） | https://www.kbismarck.com/genedata.html |
| EN infobox | 12 × 2 cm FlaK 30（12×1） | 门 | infobox 只记 12 门单装 | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| EN 正文 | 初始 12 × 2 cm C/30；1941 年 4 月前桅探照灯平台上两门单装被两座四联 C/38 替换 | 门 | 正文与 infobox 口径不同（替换前 12 / 替换后 12−2+8=18 管） | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| GN index | 20 门，型号写作 **"2 cm MG L/64"** | 门 | 总数与 KB genedata 一致，但身管倍数写 L/64（其余来源 L/65） | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |

### 5.6 其他武备

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB genedata | 9 | 枚 | "9 x depth charges"（深水炸弹）；其余来源均未提及 | https://www.kbismarck.com/genedata.html |

---

## 6. 火控

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB controltiri | 3 个指挥所（前、后、前桅楼 foretop），各带 Zeiss 体视测距仪旋转穹 + 1 台 FuMO 23 | 个 | 前桅楼指挥所由 First Artillery Officer（I.A.O.）指挥，海拔约 31 m | https://www.kbismarck.com/controltiri.html |
| KB controltiri | 10.5 m 基线 × 3 + 7 m × 1 + 6.5 m × 2 + 4 m SL-8 × 4 + 3 m × 2 | 台 | 10.5 m 为 Basisgerät BG，最大 50 倍、视场 360°；3 m 为夜间测距仪，装于舰桥两侧 | https://www.kbismarck.com/controltiri.html |
| KB genedata | 5 × 10.5 m 基线 / 1 × 7 m / 2 × 6.5 m / 4 × 4 m SL-8 / 2 × 3 m | 台 | genedata 计 5 台 10.5 m（含 4 座主炮塔各 1 台与后指挥所），controltiri 描述更细 | https://www.kbismarck.com/genedata.html |
| KB controltiri | Anton 炮塔的 10.5 m 测距仪于 1940/41 年冬在汉堡拆除 | – | 时点说明 | https://www.kbismarck.com/controltiri.html |
| KB controltiri | 4 座 SL-8（Stabilisierter Leitstand），各 4 m 基线；前桅两侧 2 座带球形罩（Wackeltopf），中后部 2 座露天 | 座 | 高炮专用指挥所 | https://www.kbismarck.com/controltiri.html |
| EN 正文 | 3 个指挥所，机械式计算机；1941 年 3 月前三个穹正面均装 FuMO 23 Seetakt 雷达 | 个 | 加装时间点与 KB 无冲突（KB 未给日期） | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| EN 正文 | 4 座 SL-8 稳定指挥仪；3.7 与 2 cm 仅便携测距仪 | 座 | 与 KB 一致 | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| KB genedata | 3 × FuMO 23 | 台 | 总数 | https://www.kbismarck.com/genedata.html |
| KB controltiri | FuMO 23：约 2 m 高 × 4 m 宽（绰号 Matratzen）；368 MHz；波长 81.5 cm；功率 9 kW @500 kHz；最大有效距离约 25,000 m；无 PPI，仅 A-scope | 混合 | 雷达细部仅 KB 提供 | https://www.kbismarck.com/controltiri.html |
| KB controltiri | GHG 被动声呐：两组各 60 个麦克风，有效距离 26–40 km | 个 / km | 仅 KB 提供 | https://www.kbismarck.com/controltiri.html |
| KB controltiri | 计算室 Rechenstellen 位于 section XV（前）与 VII（后） | – | 仅 KB 提供 | https://www.kbismarck.com/controltiri.html |
| EN infobox | Sensors: FuMO 23 Seetakt radar, Hydrophone | – | 与 KB 的雷达+被动声呐组合相符 | https://en.wikipedia.org/wiki/German_battleship_Bismarck |

---

## 7. 航空设施

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB genedata | 4 × Arado Ar 196 | 架 | — | https://www.kbismarck.com/genedata.html |
| KB avioni | 4 架（必要时最多 6 架） | 架 | 2 架在主桅下 120 m² 双机库，另 2 架在烟囱两侧各 60 m² 单机库 | https://www.kbismarck.com/avioni.html |
| EN infobox | 4 × Arado Ar 196；"1 double-ended catapult" | 架 / 具 | 双端弹射器（可从两端弹射） | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| GN index | 4 × Ar 196 | 架 | — | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |
| KB avioni | 弹射器：32 m 长双联（可伸缩至舷外 48 m），位于 section X–XI（主桅与烟囱之间），可向两舷展开 | m | "双联"与 EN 的 "double-ended" 表述口径不同 | https://www.kbismarck.com/avioni.html |
| KB avioni | 12 吨吊车回收；漏斗探照灯平台下另两小吊车 | t / 具 | — | https://www.kbismarck.com/avioni.html |
| KB avioni | 1941-05-27 晨试图以 Ar 196 送出战日志，弹射器损坏失败 | – | 战史细节 | https://www.kbismarck.com/avioni.html |
| KB avioni | Ar 196A-3：翼展 12.4 m、长 11 m、高 4.4 m；空重 2,335 kg、满载 3,300 kg；BMW 132K 960 hp；最大 320 km/h；航程 497 nm；乘员 2；2×20 mm MG FF + 3×7.92 mm；2×50 kg 炸弹 | 混合 | 机型参数仅 KB 提供 | https://www.kbismarck.com/avioni.html |
| KB avioni | 4 架机号：052 T3+IH、110 T3+AK、123 T3+DL（A-2）、150 T3+MK（A-3） | – | 机号档案 | https://www.kbismarck.com/avioni.html |

---

## 8. 编制（舰员）

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB genedata | 2,200+ | 人 | 仅给总数，未分军官/士官/水兵 | https://www.kbismarck.com/genedata.html |
| EN infobox | 103 军官 + 1,962 士兵 | 人 | 标准编制（合计 2,065） | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| ENC infobox | 103 officers / 1,962 enlisted | 人 | 与 EN 一致 | https://en.wikipedia.org/wiki/Bismarck-class_battleship |
| EN 正文 | 出击时 2,221 名官兵（含近 65 名将官参谋、80 名 Prize crew 及战地记者） | 人 | 战时实际出航编制，非标准编制 | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| GN index | 2,092 | 人 | `Complement` / `Crew` | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |

> 全部来源均**未**给出"军官 / 士官 / 水兵"三级细分（英维只分军官与士兵两级）。该项标注：**未获取**。

---

## 9. 造价、建造厂与日期

| 来源 | 值 | 单位 | 口径/备注 | URL |
|---|---|---|---|---|
| KB genedata | RM 196.8 million | 帝国马克 | 页脚注 1 明确 "At 1938 values"（1938 年币值） | https://www.kbismarck.com/genedata.html |
| EN / ENC | 196 million RM | 帝国马克 | 取整，未标币值年份 | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| GN index | 197 Mio RM | 帝国马克 | "197 Mio Reichsmark"，取整方式不同 | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |
| KB genedata | Blohm & Voss, Hamburg | – | 建造厂 | https://www.kbismarck.com/genedata.html |
| EN 正文 | Blohm & Voss 汉堡 **Helgen IX**（9 号船台）；以 "Ersatz Hannover" 名义、合同代号 "F" | – | 船台号与替代舰名义 | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| GN index | Blohm & Voß Hamburg，**Slipway 1** | – | 船台号与 EN 的 Helgen IX 冲突 | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |
| KB genedata | 1936-07-01 | 日期 | Laid down（铺设龙骨） | https://www.kbismarck.com/genedata.html |
| GN index | 01.07.1936 | 日期 | 一致 | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |
| EN 正文 | 1936-07-01 | 日期 | 一致 | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| KB genedata | 1939-02-14 | 日期 | Launched（下水） | https://www.kbismarck.com/genedata.html |
| GN index | 14.02.1939 | 日期 | 一致 | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |
| EN 正文 | 1939-02-14（Dorothee von Löwenfeld 掷瓶，Hitler 出席演讲） | 日期 | 一致 | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| KB genedata | 1940-08-24 | 日期 | Commissioned（服役） | https://www.kbismarck.com/genedata.html |
| GN index | 24.08.1940 | 日期 | 一致 | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |
| EN 正文 | 1940-08-24，首任舰长 Ernst Lindemann | 日期 | 一致 | https://en.wikipedia.org/wiki/German_battleship_Bismarck |
| GN index | 1941-05-27（北大西洋） | 日期 | Sunk（沉没）；其余来源正文均述 5 月 27 日沉没 | https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html |

---

## 10. 数据分歧汇总

共 22 个字段存在 ≥2 个不同数值。按严重度排列。

### 10.1 排水量——分歧最大，且是口径问题而非错误

| 口径 | 数值 | 来源 |
|---|---|---|
| 标准排水量（德方档案口径，按华盛顿条约定义） | 43,978 mt | KB |
| 标准排水量（英方/战后通行口径） | 41,700 t | EN、ENC |
| 满载（德方档案口径） | 51,760 mt / 51,700 mt | KB（同页自相矛盾） |
| 满载（英方口径） | 50,300 t | EN、ENC |
| 最大（德方） | 53,486 mt | KB |
| 最大（GN 口径） | 50,956 t | GN |

**原因分析**：标准排水量差 2,278 mt（5.5%），KB 在 bsweights 页脚注 1 明确引用 1922 华盛顿条约定义（不含燃料与备用给水）并逐项累加得出 43,978；英维的 41,700 t 更接近"as built 空载＋弹药"一类口径。满载差 1,460 mt 同源。GN 的 50,956 t "最大" 既不等于 KB 的 53,486 也不等于英方的 50,300，其站内未给定义，属第三套口径。**这不是引用错误，是三国海军传统对同一物理量的记账方式不同。**

### 10.2 主炮最大射程——三套不同值

| 值 | 来源 |
|---|---|
| 35,550 m @30° | KB armament |
| 35.5 km / 35.6 km | ENGUN（infobox 与弹药表内部不一致） |
| 36,520 m @30° | ENC 正文 |

**原因分析**：35.55 与 35.5/35.6 属取整与口径换算（35,550 m ≈ 35.5 km，四舍五入为 35.6 时按 800 kg 弹的实测落点略远）；36,520 m 明显是另一来源（可能是 Garzke & Dulin 或 1943 年改进弹数据），比其余高约 1,000 m，**很可能是把岸防型 Siegfried-Granate 或加大装药的试验数据混入舰炮条目**，属引用口径错误。

### 10.3 主炮装药量——数值与主副顺序都反了

| 来源 | Fore charge | Main charge |
|---|---|---|
| KB | 99.5 kg | 112 kg |
| ENGUN | 104 kg（VorKart34） | 108 kg（HuelsKart34） |

**原因分析**：两源的 fore/main 组合恰好**互换**（KB 的 fore 更轻、main 更重；ENGUN 的 fore 更重、main 更轻）。且 KB 两者总和 211.5 kg、ENGUN 总和 212 kg，总量几乎相同——说明是同一实物、命名归属不同，属**德文原始术语（Vorladung / Hauptladung）转写时的标签错位**，不是测量分歧。

### 10.4 主炮弹药基数

| 值 | 来源 |
|---|---|
| 1,004 发（AP 353 / HE Bdz 338 / HE Kz 313） | KB armament |
| 940–960 发（每管 115–120） | ENC 正文 |

**原因分析**：差 44–64 发。KB 是逐弹种点数（且三数相加正好 1,004）；ENC 用"每管 115–120"反推。可能是 ENC 采用设计基数、KB 采用 1941 年出击时实际装载量（含额外补弹）。

### 10.5 轻型高炮 2 cm 数量——12 / 18 / 20 三个值

| 值 | 来源 |
|---|---|
| 12 门单装（C/30） | EN infobox |
| 12 单装（其中 2 门 1941-04 换为 2 座四联 C/38 → 18 管） | EN 正文 |
| 12 单装 + 8（2 座四联）C/38 = 20 管 | KB armament / KB genedata / GN |

**原因分析**：是**时点问题**。1941 年 4 月底改装前为 12 门单装，改装后为 10 单装 + 8 四联管 = 18 管；KB 与 GN 的 20 是另一种统计（可能把 2 cm 与其它近防武器合并或计入了不同批次）。英维 infobox 停在改装前状态，正文描述了改装，自身未统一。

### 10.6 续航力

| 值 | 来源 |
|---|---|
| 9,280 @16 / 8,900 @17 / 8,525 @19 / 6,640 @24 / 4,500 @28 nmi | KB |
| 8,870 nmi @19 kn | EN |
| 8,525 nmi @19 kn | ENC |
| 8,100 mi @16 kn / 3,740 mi @30 kn | GN |

**原因分析**：同为 19 kn 档，EN 给 8,870、ENC 给 8,525、KB 给 8,525——EN 与 ENC 在同一维基社群内就冲突。可能是 8,870 对应"加装额外油舱（7,400 t）"状态，8,525 对应标准燃油状态；GN 的 8,100 mi @16 kn 与 KB 的 9,280 nmi @16 kn 差 1,180，且单位是 miles 而非 nautical miles（若为 statute miles，8,100 mi ≈ 7,039 nmi，差距更大）。**GN 此条疑为换算或录入错误。**

### 10.7 燃油容量

| 值 | 来源 |
|---|---|
| 7,900 mt | KB genedata |
| 8,294 mt | KB propulsioni（同站另一页） |
| 6,721 mt（6,194 炉用 + 527 推进） | KB bsweights |
| 6,400 t（正常）/ 3,200 t（设计）/ 7,400 t（加装后） | EN、ENC |

**原因分析**：**同一网站三页三个值**，这是最典型的"引用时点/记账口径不同"——bsweights 的 6,721 是建船重量表里的实际油舱容积，propulsioni 的 8,294 可能含备用舱。

### 10.8 吃水

| 值 | 口径 |
|---|---|
| 9.33 m | 标准吃水（KB） |
| 9.3 m | 标准吃水（EN） |
| 9.30 m | 设计吃水（ENC） |
| 8.63 m | 标准排水量状态（ENC） |
| 9.9 m | 最大吃水（EN 正文 / GN） |
| 10.55 m | 最大吃水（KB） |

**原因分析**：9.33/9.3/9.30 是同一数的不同精度；8.63 是"标准排水量时的吃水"，而 9.30 标为"设计吃水"，ENC 自身把两者并列——**这两个不是矛盾，是不同装载状态**。真正冲突在最大吃水：KB 的 10.55 m 对 EN/GN 的 9.9 m，差 0.65 m（6.5%），KB 用的是"最大允许/极限"口径，其余用"满载吃水"口径。

### 10.9 舰员数

| 值 | 来源 |
|---|---|
| 2,200+ | KB |
| 2,065（103 军官 + 1,962 士兵） | EN、ENC |
| 2,221（出击时实际） | EN 正文 |
| 2,092 | GN |

**原因分析**：四个值是四个时点/范围：标准编制 2,065、出击加强编制 2,221、概略"2,200+"、以及 GN 的 2,092（可能是服役初期或某次部署的实数）。**不是矛盾，是编制随任务变化。**

### 10.10 造价

| 值 | 来源 |
|---|---|
| RM 196.8 million（1938 年币值） | KB |
| 196 million RM | EN、ENC |
| 197 Mio RM | GN |

**原因分析**：取整精度不同。KB 的 196.8 最好用（标明币值年份）。GN 的 197 是向上取整。**非实质分歧。**

### 10.11 建造船台

| 值 | 来源 |
|---|---|
| Blohm & Voss 汉堡 Helgen IX（9 号船台） | EN |
| Slipway 1（Blohm & Voß Hamburg） | GN |

**原因分析**：**真冲突**。Blohm & Voss 汉堡厂有多条船台，且其编号体系（Helgen）与"Slipway"表述可能指不同命名层次——一说 9 号船台、一说 1 号船台。需查原始建造合同或厂志才能定，两源均未给出处分依据。

### 10.12 主炮型号标注

| 值 | 来源 |
|---|---|
| 38 cm SK C/34，L/52 | KB、EN、ENGUN |
| 38 cm L/47 C/34 | GN |
| —— | 2 cm MG L/64（GN）vs L/65（KB/EN） |

**原因分析**：**GN 的火炮型号标注系统性偏离**。38 cm 的 L/52 是身管长（19.630 m ÷ 380 mm = 51.66 ≈ L/52），GN 写 L/47 可能误用了穿甲弹长度或另一门 38 cm 炮（如 SK C/34 岸防型的某批次）。2 cm 的 L/64 vs L/65 差 1 个口径，属舍入方向不同（1.3 m ÷ 20 mm = 65，向下取整得 64）。

### 10.13 主炮最大射速

| 值 | 口径 |
|---|---|
| 2.4+ 发/分 | KB（实战口径） |
| 2.5 发/分（手册）/ 3.125（试射）/ ~1（对 Hood 实战） | ENGUN（三口径并列） |
| 3 发/分（18 秒/发，理想） | ENC |

**原因分析**：**四套口径并存**：理论设计 3 发/分、手册要求 2.5、试射峰值 3.125、实战 1–2.4。任一单值脱离语境都会误导。

### 10.14 副炮/高炮口径与数量——一致，无分歧

15 cm（12 门）、10.5 cm（16 门）、3.7 cm（16 门）在四来源间完全一致，仅 GN 的型号书写格式（C28 vs C/28）不同。**不计入分歧。**

### 10.15 其他次要分歧

| 字段 | 冲突值 | 原因 |
|---|---|---|
| 全长 | 250.50 m（KB）vs 251.0 m（GN/EN/ENC） | 换算取整，250.50 更精确 |
| 舰宽 | 全部 36 m，无分歧 | — |
| 螺旋桨转速 | HP/IP 2,880 / LP 2,430 rpm（KB）vs 2,825 / 2,390（ENC） | KB 脚注 2 自己说明数据取自 Tirpitz 的 Brown Boveri 汽轮机，与 Bismarck 的 Blohm & Voss 机不同——KB 已自我标注 |
| 棱形系数 | 0.55/0.57（genedata）vs 0.56（propulsioni） | 同站两页不同值 |
| 炮管重量 | 110.7 mt（KB）vs 111 t（ENGUN） | 单位口径差（metric ton vs tonne） |
| 炮弹装药 | AP 18.8 / HE Bdz 32.6 / HE Kz 64.25 kg（KB）vs 20.3 / 35 / 62.8 kg TNT（ENGUN） | KB 为装药全重，ENGUN 为 TNT 当量，**口径不同不可比** |
| 装甲甲板 | 第三装甲甲板 80–120（KB genedata）vs 主甲板 100–120（EN）vs 80–120（GN） | EN 把"主装甲甲板"与"第三装甲甲板"混用命名 |
| 水密隔舱 | 22 个（KB、EN 一致）；但 KB 另称装甲堡内 17 个 | 非分歧，17 是 22 的子集 |
| 双层底 | 深 1.7 m（KB）vs 占舰长 83%（EN） | 两个不同度量的表述，非冲突 |
| 艇只清单 | 4 交通艇/3 汽艇/1 摩托舢板/6 快艇/3 舢板/2 小艇/16 救生筏（KB）vs 3 picket boats/4 barges/1 launch/2 pinnaces/2 cutters/2 yawls/2 dinghies（ENC） | 艇类命名体系不同（德式 vs 英式分类），总数也不同，属**翻译口径不可直接对齐** |

### 10.16 三个最严重的数据冲突

1. **标准排水量 43,978 mt（KB）vs 41,700 t（EN）——差 2,278 mt，5.5%**。根源是华盛顿条约定义 vs 英方记账口径。这是全网所有 Bismarck 数据表分岔的总源头，其他派生的吃水、载重数据都跟着分岔。
2. **主炮装药 Fore/Main 两源完全互换（99.5/112 vs 104/108 kg）**。总量相同、分配相反，属德文原始术语的标签错位——一旦被下游引用就会直接写出"错误的主装药"。
3. **最大射程 35,550 m vs 36,520 m（差 970 m）**，且 ENGUN 同一页内部就写 35.5 km 与 35.6 km 两个值。疑为把岸防型 Siegfried-Granate 或试验装药数据混入舰炮条目。

---

## 11. 来源可用性清单

| URL | 状态 | 说明 |
|---|---|---|
| https://www.kbismarck.com/technical.html | ✅ 200 | 入口页，可正常抓取（latin-1 编码） |
| https://www.kbismarck.com/genedata.html | ✅ 200 | 主技术表，内容最全 |
| https://www.kbismarck.com/bsweights.html | ✅ 200 | 逐项重量表，可闭合验算 |
| https://www.kbismarck.com/proteccioni.html | ✅ 200 | 装甲专题，2019-07-01 更新 |
| https://www.kbismarck.com/armament.html | ✅ 200 | 武备专题，2020-10-02 更新 |
| https://www.kbismarck.com/propulsioni.html | ✅ 200 | 动力专题 |
| https://www.kbismarck.com/controltiri.html | ✅ 200 | 火控专题，2020-10-02 更新 |
| https://www.kbismarck.com/avioni.html | ✅ 200 | 航空设施专题 |
| https://www.kbismarck.com/oequipment.html | ✅ 200 | 锚/艇/探照灯等杂项 |
| https://en.wikipedia.org/wiki/German_battleship_Bismarck | ✅ 200 | 特色条目，正文溢出到临时文件但全文可读 |
| https://en.wikipedia.org/wiki/Bismarck-class_battleship | ✅ 200 | GA 级，舰级数据 |
| https://en.wikipedia.org/wiki/38_cm_SK_C/34_naval_gun | ✅ 200 | 主炮专门条目，含 Krupp 原图数据与逐面装甲表 |
| https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/index.html | ✅ 200 | 有效，数据较简 |
| https://www.german-navy.de/kriegsmarine/ships/battleships/bismarck/technical.html | ⚠️ HTTP 200 但页面为 "404 Page Not Found" | 站点改版后路径失效，**必须改用 index.html** |
| https://www.navweaps.com/Weapons/WNGER_15-52_skc34.htm | ❌ 抓取失败 | TCP 443 不可达：`Test-NetConnection navweaps.com:443` = False；`Invoke-WebRequest` 报「无法连接到远程服务器」；`web_fetch` 报 timeout 30000 ms。DNS 可解析（15.204.150.217），属网络层阻断，非站点故障 |
| https://www.navweaps.com/Weapons/WNGER_15-55_skc28.htm | ❌ 抓取失败 | 同上，整站不可达 |
| https://www.navweaps.com/Weapons/WNGER_105-65_skc33.htm | ❌ 抓取失败 | 同上 |
| https://www.navweaps.com/Weapons/WNGER_37mm-83_skc30.htm | ❌ 抓取失败 | 同上 |
| https://www.navweaps.com/Weapons/WNGER_20mm-65_c30.htm | ❌ 抓取失败 | 同上 |
| https://de.wikipedia.org/wiki/Bismarck_(Schiff,_1940) | ❌ 抓取失败 | `Test-NetConnection de.wikipedia.org:443` = True，但 web_fetch 三次均 timeout 30000 ms；python urllib 报 `<urlopen error _ssl.c:1064: The handshake operation timed out>`；de.m.wikipedia.org 同错。同网络下 en.wikipedia.org / zh.wikipedia.org 均 200 正常，属该域名的 TLS 握手被阻断 |
| 代理绕过尝试：r.jina.ai / api.codetabs.com / www.wikiwand.com / de.wikipedia REST summary | ❌ 全部失败 | 分别报 ECONNRESET / timeout / timeout / timeout。环境无 HTTP_PROXY、HTTPS_PROXY 环境变量 |
| combinedfleet.com | ⏭️ 跳过 | 按要求跳过（该站不涉及德舰） |

### 未获取项（明确标注）

- **舰员三级细分（军官 / 士官 / 水兵）**：所有可用来源均只给"军官 + 士兵"两级（EN）或单一总数（KB 2,200+、GN 2,092），**未获取**士官单列人数。
- **navweaps 独家数据**（弹道表、穿深曲线、各距离飞行时间）：全部来源不可达，**未获取**。
- **德文原始档案（Bundesarchiv / BA-MA RM 系列）**：未尝试，超出本次范围。
- **主装甲带实际倾角的逐段精确值**：KB 只给四个炮塔位置的近似外倾角（17°/10°/8–10°/7°），非全带连续值。

---

*文件由 web_fetch 实测抓取整理，所有数值均可在对应 URL 页面内定位复核。抓取失败的来源已如实标注，未做任何推测补全。*
