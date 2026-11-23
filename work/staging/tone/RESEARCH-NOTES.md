# 利根级重巡洋舰 · 技术数据调研底稿

> 2026-11-23 · 战舰资料检索员（tone-tech）
> 本轮范围：只有技术数据。切片 / 正文 / 配图由主会话另行安排。
> 产出：`classes/tone.yaml` / `ships/tone.yaml` / `ships/chikuma.yaml` /
> `sources-fragment.yaml` + 本文件。
> 原始页面全部落在 `work/staging/tone/_raw/`（含 `.html` 与转出的 `.txt`）。

---

## 0. 抓取方式与站点可用性（给下一轮省时间）

按 SCHEMA §9.1 的规矩，`web_fetch` / `research` 全程未用。全部用
Python `urllib.request` + 自定义 UA 直连，原始页面存盘后再用 lxml 转纯文本。

**实测可直连（200）：**

| 站点 | 用途 | 备注 |
|---|---|---|
| `navypedia.org/ships/japan/jap_cr_tone.htm` | 本级主数据 | 主尺度/动力/装甲分段厚度/武备/编制/结局 |
| `combinedfleet.com/tone_t.htm` | 利根 TROM | 逐日年表，逐次改装与沉没全链条 |
| `combinedfleet.com/chikuma_t.htm` | 筑摩 TROM | 同上；萨马岛段落到分钟 |
| `combinedfleet.com/tone_c.htm` | 舰级速览 | 只用来取「四炮塔前置、舰尾无炮」的独立表述 |
| `pwencycl.kgbudge.com/T/o/Tone_class.htm` | 装甲材质与逐部位厚度 | **唯一给 NVNC / CNC 分材质配厚度的来源** |
| `navweaps.com/Weapons/WNJAP_8-50_3ns.htm` | 20 cm No.2 炮与 E3 炮座 | 已有登记 `navweaps-20cm-3ns` |
| `navweaps.com/Weapons/WNJAP_5-40_t89.htm` | 12.7 cm 八九式 | 含 "Tone (4) … A1 Mod 1" |
| `navweaps.com/Weapons/WNJAP_25mm-60_mg.htm` | 25 mm 九六式 | |
| `navweaps.com/Weapons/WTJAP_WWII.php` | 日本鱼雷（93 式） | 只用于确认 61 cm 口径族，未用作本级 fact 来源 |
| `en/ja.wikipedia.org` | 线索 | **tier E，不作任何 fact 的 src** |
| `ibiblio.org/hyperwar/Japan/IJN/index.html` | 索引 | 该索引是陆军的，IJN 部分没有本级条目 |

**实测失败（别重试，三次不通已记）：**

| 站点 | 结果 |
|---|---|
| `combinedfleet.com/tone.htm` / `chikuma.htm` / `toneclass.htm` / `cruiser.htm` | 404（本级只有 `_t` 与 `_c` 两个真实路径） |
| `naval-encyclopedia.com/ww2/japan/tone-class-cruisers` | 200 但返回的是首页/导航壳，无正文（SPA 渲染），抽取 0 字 |
| `ww2db.com`（三个 ship_id 都试过） | 403 |
| `militaryfactory.com` / `world-war.co.uk` / `asahi-index` | 403 |
| `globalsecurity.org` / `historyofwar.org` / `battleships-cruisers.co.uk` / `warshipsww2.eu` / `navypedia` 的日本巡洋舰索引页 | 404 |
| `hazegray.org` / `japanese-navy.com` / `history.navy.mil` | TLS `UNEXPECTED_EOF_WHILE_READING`（本机 SSL 层被拦，换 UA 无效） |
| `homepage2.nifty.com/nishidah/*`（西田式舰艇要目） | 502 / ConnectionReset |
| `navweaps.com/Weapons/WNJAP_Radar.htm`、`WNJP_Radar.htm` | 404；NavWeaps 把日本雷达做成了站外链，本站内无页 |
| `combinedfleet.com/radar.htm` | 200，但只有各型雷达的性能表，**没有逐舰装舰记录**，故未用 |

**结论**：本级可以上 tier D / C 的逐部位数据，但**日方一手档案
（防卫省防卫研究所 Ref.C0511xxxxxxx 系列）本轮完全没拿到**——
日文百科引了这些档案编号，但档案正文是 JACAR 的 PDF 扫描，本轮未抓。
这是本站目前最薄的一层，若要把 confidence 提到 A，下一步应去
`jacar.go.jp` 取 `第5275号 9.12.14 利根`（Ref.C05110625500）与
`第171号の13 10.10.18 筑摩`（Ref.C05110626300）两份要目文件。

---

## 1. 任务书陈述的核实结果

任务书里的史实陈述全部按「待核实」处理。逐条结论：

| # | 任务书说 | 核实结果 | 依据 |
|---|---|---|---|
| 1 | 主炮是「20cm/50 三年式」，需注意是 **2 号炮还是 1 号炮** | **是 No.2 炮（2 GÔ），不是 No.1** | NavWeaps 同一页两处：Ship Class Used On 栏 "As Completed / Takao and Tone classes"；正文 "the design of the Tone class was altered during construction to use these guns"；并明确 "The No. 2 (2 GÔ) designation was used to distinguish these guns from the older 20 cm (7.9") 3rd Year Type No. 1 (1 GÔ) guns." 实弹径 20.32 cm、初速 840 mps，No.1 是 20.0 cm / 870 mps。**本站已有的 `weapon:20cm-3ns` 是 No.1 炮**（见 `data/weapon-articles/20cm-3ns.yaml` 第 3 行「20 cm/50 三年式 No.1」），所以本轮另立 `weapon:20cm-3ns-no2`，没有复用那个 id。 |
| 2 | 主炮「四座双联的布置方式」 | **四座全在舰艏、舰尾无主炮**，这一点两源硬证；但**逐座（哪座背负、哪两座朝后）的非 E 级来源本轮未获取** | combinedfleet 舰级页 "with four dual turrets forward (some of which suffered from very poor firing arcs), and none aft"；navypedia 的 4 x 2 布置。日文百科写得最细（第 1・2 炮塔背负式、第 3・4 炮塔在最上甲板层朝后），但那是 tier E，**没有采用**，见 §5 未获取项。 |
| 3 | 利根级是「航空重巡」 | **成立，且比任务书的说法更极端**：设计编制 6 机、双弹射器、整个舰尾让给航空作业；**但没有机库** | navypedia "6 seaplanes (3 E7K1, 3 E8N1) … 2 catapults"；pwe "2 / Kure Type 2 Model 5 catapults"，并给「设计上限 8 机、实战从未超过 5 机、后期降到 4 机」。机库一项见 §5。 |
| 4 | 排水量「四口径分开」 | **只拿到两口径**：standard 11,215（两源互证）、full 15,200（navypedia）。**trial 与 declared 未获取**（只在 tier E 里有 13,320 与 8,636） | 见 §2 与 §5 |
| 5 | 定员 | **850 人，三源互证**；另有 869 / 874 两说只在 tier E | navypedia "Complement 850"；pwe "Complement \| 850"；combinedfleet 舰级页 "Crew \| 850"。 |
| 6 | 两舰雷达加装时间不同 | **成立，而且这是两舰最大的一处差异**：利根 1944-11 把 21 号换成 22 号，筑摩从未撤 21 号 | 见 §3 |
| 7 | 两舰沉没日期与原因 | 利根 1945-07-24 被机攻击毁、07-29 坐沉浅底；筑摩 1944-10-25 沉没，**但「谁打沉的」两源分歧** | 见 §4 |

**任务书本身需要修正的一处**：任务书把「10 门主炮的日本重巡」这种印象带进来了
（「主炮（20cm/50 三年式…四座双联的布置方式）」这句没问题，但沿用了
「利根级主炮 8 门、比最上型少」的说法时容易漏掉一件事）——**利根级竣工就是 8 门，
不存在「先 155 mm 后改 203 mm」的服役期变化**：改装发生在**建造中**，
两舰下水时炮座已经按 20 cm 双联设计（NavWeaps 原文 "the hull and barbettes of the
Tone class had already been completed up above the armored deck when the main
armament was changed from triple 15.5 cm turrets to twin 20 cm turrets"）。
所以「本级曾以轻巡身份服役」是不成立的说法，只有「曾以轻巡身份开工」成立。

---

## 2. 逐项数据：英文原句 + URL

### 2.1 主尺度与排水量

**标准排水量 11,215 t**（两源互证）
- navypedia：`Displacement standard, t11215` — <https://www.navypedia.org/ships/japan/jap_cr_tone.htm>
- pwe：`Tonnage | 11,215 tons standard displacement` — <http://pwencycl.kgbudge.com/T/o/Tone_class.htm>

**满载排水量 15,200 t**
- navypedia：`Displacement full, t15200` — 同上 URL

**全长 / 水线长 / 垂线间长**
- navypedia：`Length, m190.3 pp 198.8 wl 201.6 oa` — 同上 URL
- pwe：`Dimensions | 661'1" by 60'8" by 21'2"` / `201.50m by 18.49m by 6.45m` — pwe URL
  → 201.50 m 与 navypedia 的 201.6 m 差 0.1 m，两说并列。

**最大宽 19.4 m** / **平均吃水 6.47 m**
- navypedia：`Breadth, m19.4` / `Draught, m6.47` — 同上 URL
- pwe 给 18.49 m × 6.45 m（口径未声明，未采用为 beam.wl）。

### 2.2 动力

- navypedia：`No of shafts4` / `Machinery 4 sets Kampon geared steam turbines,
  8 Kampon boilers` / `Power, h. p. 152000` / `Max speed, kts35` /
  `Fuel, t oil 2690` / `Endurance, nm(kts)8000(18)` — 同上 URL
- pwe：`Machinery | 4-shaft geared turbine (152,000 shp)` / `8 Kampon boilers` /
  `Maximum speed | 35 knots` / `Bunkerage | 2163 tons fuel oil` /
  `Range | 9000 nautical miles (17,000 km) at 18 knots` — pwe URL

→ 载油 2,690 vs 2,163、续航 8,000 vs 9,000，两处并列不裁决。

### 2.3 防护（按部位，全部来自 navypedia 同一段）

navypedia 的 `Ship protection` 整段原文（一次性引出，逐条 fact 都引这里的句子）：

> `Inner 20°-inclined 110.5m-long main belt protected machinery spaces, connecting
> with anti-torpedo bulkhead by lower edge. Its height was 2.6m at 77.8m length
> (or 5.85m with anti-torpedo bulkhead summary). Its thickness was 100mm on upper
> edge, tapering to 65mm on lower edge, connected with 65mm upper edge of
> longitudinal bulkhead. Thickness of bulkhead decreased to 34mm near double bottom.
> Belt was closed by 105-67mm transverse bulkheads. Magazines were protected by
> narrower belt (4.0m in height summary with longitudinal bulkhead, upper edge of
> belt was under wl). Its thickness changed from 145mm at upper edge to 55mm near
> double bottom, this belt also was closed by 175-130mm bulkhead. Main belt was
> connected with main 31mm deck by 20°-inclined 65mm slopes. Magazines were
> protected by flat 56mm lower deck. Steering gear compartment was protected by
> 100mm longitudinal and 35mm transverse bulkheads and 30mm medium deck.
> Underwater protection consisted of bulges and longitudinal bulkhead, its deep
> was about 3.3m. Guns had 25mm turrets and 25mm barbettes. CT had 100mm sides
> and 50mm roof.`

pwe 的防护段原文（材质与分部位，与上面逐条对照）：

> `Protection | 2073 tons`
> `4" to 0.7" (100mm to 18mm) NVNC and Dücol machinery belt sloped 20 degrees`
> `5.7" to 2.2" (145mm to 55mm) NVNC magazine belt`
> `6.9" to 2.6" (175mm to 67mm) NVNC bulkheads`
> `2.6" to 1.2" (65mm to 31mm) CNC middle deck`
> `2.2" (56mm) lower deck over magazines`
> `3.9"/1.4"/1.2" (100mm/35mm/30mm) steering sides/ends/crown`
> `4.1" (105mm) max uptakes`
> `1" (25mm) NVNC barbette`
> `1" (25mm) NVNC turret`
> `5.1" to 2.6" (130 mm to 70mm) side/1.6" (40mm) overhead conning tower`
> `Lower belt as torpedo holding bulkhead. Torpedo system depth 10'10" (3.3m).`

**两份材料的差别，须在页面上说清（不改 fact，只记在此）**：
- 机舱段装带下缘：navypedia 65 mm、pwe 18 mm；
- 横向隔壁：navypedia 机舱段 105–67 mm、弹药库段 175–130 mm；pwe 统一写 175–67 mm；
- 司令塔：navypedia 侧 100 / 顶 50；pwe 侧 130–70 / 顶 40；
- pwe 多给了材质（NVNC / CNC）与烟道口 105 mm、舵机舱分层，navypedia 都没有。

### 2.4 武备

- navypedia：`Armament4 x 2 - 203/50 3-shiki, 4 x 2 - 127/40 89-shiki,
  6 x 2 - 25/60 96-shiki, 4 x 3 - 610 TT (24), 6 seaplanes (3 E7K1, 3 E8N1),
  2 catapults` — 同上 URL

**主炮本体（No.2 炮）**，全部来自 <https://www.navweaps.com/Weapons/WNJAP_8-50_3ns.htm>：
- `20 cm/50 (8") 3rd Year Type No. 2` / `Official Designation: 50 caliber 3rd Year Type No. 2 20 cm Gun`
- `Actual bore diameter was 20.32 cm (8.0")`
- `Gun Weight 18.7 tons (19 mt)`
- `Gun Length oa 405.9 in (10.310 m)` / `Bore Length 393.70 in (10.000 m)`
- `Chamber Volume 4,150 in3 (68.0 dm3)`
- `Rate Of Fire 3 to 4 rounds per minute`
- `Projectile Types and Weights — AP Type 91: 277.4 lbs. (125.85 kg)`
- `Muzzle Velocity — All except Illum: 2,756 fps (840 mps)`
- `Approximate Barrel Life 320 - 400 rounds`
- `Ammunition stowage per gun 120 - 126 rounds`
- 射表末行：`45.0 degrees / 32,150 yards (29,400 m)`
- 型号与炮座：`Tone (4) and Ibuki (5): Model E3`；
  `Model E1, E2, Modified E2 and E3: -5 / +55 degrees`；
  `The Modified E2 and the Model E3 mountings had 315 inch (8 m) rangefinders`

**高角炮（12.7 cm 八九式）**，来自 <https://www.navweaps.com/Weapons/WNJAP_5-40_t89.htm>：
- `Myôkô (4), Mogami (4),` / `Tone (4) and Ibuki (4): A1 Mod 1`
- `The A1 mount was unshielded. The A1 Mod 1 added a shield.`
- `A1 Mod 1: 24 tons (24.5 mt)`
- `Rate Of Fire — Type 89: 14 rounds per minute initially, 8 rounds per minute sustained`

### 2.5 航空

- navypedia：见 2.4 同一行（`6 seaplanes (3 E7K1, 3 E8N1), 2 catapults`）
- pwe：`Aircraft | 2` / `Kure Type 2 Model 5 catapults` / `5 seaplanes`，
  以及 `Though designed to carry up to eight seaplanes, it appears that the ships
  never carried more than five, and this was reduced to four later in the war.`
- 机库无正面表述（见 §5）。

### 2.6 编制

- navypedia `Complement 850`；pwe `Complement | 850`；
  combinedfleet 舰级页 `Crew | 850` — 三源同值。

### 2.7 建造（单舰）

| 项 | 利根 | 筑摩 |
|---|---|---|
| Yard No | 600 | 670 |
| 开工 | `1.12.1934` | `1.10.1935` |
| 下水 | `21.11.1937` | `19.3.1938` |
| 服役 | `20.11.1938` | `20.5.1939` |
| 结局 | `sunk 24.7.1945` | `sunk 25.10.1944` |

全部来自 navypedia 的 Ships 表（同一 URL）。
combinedfleet 独立佐证两舰首尾：利根 `1 December 1934: Nagasaki. Laid down at
Mitsubishi's Shipyard.` / `21 November 1937: Launched and named TONE.` /
`20 November 1938: Completed and registered in the IJN.`

---

## 3. 两舰差异（本轮的第二个重点）

判据：换一艘同级舰这个值会变吗？会变的一律写单舰文件。

### 3.1 雷达装拆时序

| 时点 | 利根 | 筑摩 | 原句 |
|---|---|---|---|
| 1943-02 | 21 号装（舞鹤） | 21 号装（吴，修理改装） | 利根：`21 February 1943: Arrives at Maizuru for a refit. Two additional 25-mm twin AA guns are installed and a Type 21 air-search radar is fitted.` 筑摩：`CHIKUMA is repaired and undergoes a refit. Two additional 25-mm twin mounts are installed and a Type 21 air-search radar is fitted.` + `27 February 1943: The refit is completed.` |
| 1944-07 | +22 号 ×2、+13 号 ×1（吴） | +22 号 ×2、+13 号 ×1（吴） | 利根：`26 June-8 July 1944: In drydock at Kure. … New antennas are installed for the two Type 22 surface-search radars and a Type 13 air-search radar is fitted.` 筑摩：TROM 只写 `26 June 1944: Arrives at Kure. Drydocked.`，加装内容改引 navypedia：`6 - 7.1944, Chikuma: … 2x 2-shiki 2-go, 3-shiki 1-go radars` |
| 1944-11 | 21 号 → 22 号 ×1 | 不变 | 利根：`17 November 1944: Arrives at Maizuru. Drydocked. … Her Type 21 radar is replaced with a Type 22.` |

**最终状态因此不同**：利根 = 22 号 ×3 + 13 号 ×1（21 号已撤）；
筑摩 = 21 号 ×1 + 22 号 ×2 + 13 号 ×1（21 号未撤）。

**月份口径分歧（单列，不裁决）**：navypedia 把利根撤 21 号记在 `2/1945`，
combinedfleet 记在 `1944-11-17`。本站取后者（进坞确切日期），
差异在本节留档，单舰 fact 的 note 里也写了。

### 3.2 25 mm 机铳

- 两舰 1943-12 / 1944-02 那次改装的结果相同，都是 `20 (4 x 3 and 4 x 2)`
  （利根 1943-12-14 完工、筑摩 1944-02-01 完工）。
- 1944-06/07 之后：利根有明确总数 `57 barrels (8x3, 4x2, 25x1)`，
  再改装后 `62 barrels (12x3, 4x2, 18x1)`；**筑摩的对应总数本轮未获取**，见 §5。

### 3.3 舰体工艺

- pwe：`The ships were originally to be partially welded. However, because of
  concerns about hull strength, Chikuma was almost entirely riveted.`
  → 写入 `ships/chikuma.yaml` 的 `construction.builder` note。

### 3.4 结局与战损

- 筑摩 1942-10-26 圣克鲁斯：`Her crew suffers 190 killed and 154 wounded including
  Captain Komura.`（单人单场伤亡，写入 `service.casualties`，带当日时间窗）
- 利根无对应的单场大伤亡记录。

---

## 4. 结局（两舰各自的原句）

### 4.1 利根

- navypedia：`Tone 24.7.1945 was sunk on shallow water off Kure by American carrier
  aircraft of TF.38. Wreck was additionally damaged 28.7.1945 and abandoned
  5.8.1945. She was later salvaged and scrapped in 1947 - 1948.`
- pwe：`Sunk by aircraft 1945-7-24 at Hashirajima`
- combinedfleet（链条最完整）：
  - `19 March 1945: … TONE, caught in the middle of Kure Bay, receives one direct
    hit, jamming her No. 3 turret in train, and several near misses.`
  - `24 July 1945: … TONE receives three direct hits and several near misses.`
  - `28 July 1945: … TONE receives two direct hits to port side (one of them a
    1,000-lb aft) and six near misses. … TONE develops a 21-degree list to port.`
  - `29 July 1945: Settles on the bottom in shallow water.`
  - `20 November 1945: Removed from the Navy List.`
  - `7 April 1947: Harima Shipyard starts the removal of superstructure and turrets.`
  - `4 May 1948: The hull is refloated.`
  - `30 September 1948: The scrapping of the hull is completed.`

**注意「击毁日」与「坐沉日」是两个日期（07-24 / 07-29），不要合并。**

### 4.2 筑摩

- combinedfleet（逐时）：
  - `At 0853, CHIKUMA is attacked by four TBM "Avenger" torpedo-bombers from
    "Taffy Two". She is hit by a Mk.13 torpedo that disables her port screw and
    rudder; two minutes later she goes dead in the water.`
  - `At 0907, CHIKUMA reports to YAMATO that she has been torpedoed and is
    unnnavigable.`
  - `At 1105, CHIKUMA is attacked by five VC-5 TBM-1Cs from KITKUN BAY. …
    CHIKUMA is hit port side amidships by two torpedoes and her engine rooms flood.`
  - `After 1415, CHIKUMA is attacked by three TBM-1Cs from OMANNEY BAY (CVE-79) …
    Three torpedoes hit her port side amidships. Around 1430, CHIKUMA capsizes and
    sinks by the stern at 11-52N, 126-36E. NOWAKI rescues some 120 survivors.`
  - `NOWAKI goes down with all hands, including CHIKUMA's survivors.`
  - `20 April 1945: Removed from the Navy List.`
- navypedia：`In battle at Samar 25.10.1944 she was heavy damaged by American
  carrier aircraft and sunk by destroyer Nowaki.`
  → **「被空袭击沉」vs「被己方野分雷击处分」两说**，已在 `ships/chikuma.yaml`
  写成两条不同 `fate_type` 的 fact，各带来源，note 里写明「两说并列，不裁决」。

---

## 5. 未获取（查不到就写查不到，一条都没有推）

| 项 | 字段 | 为什么没有 |
|---|---|---|
| 公试（trial）排水量 | `displacement.trial` | 只有日文百科给 13,320 t（tier E），不作 fact 来源。 |
| 对外申报排水量 | `displacement.declared` | 只有日文百科给 8,636 t（tier E）。**这是政治申报值，属敏感项，宁可空着。** |
| 试航实测功率 | `propulsion.power.trial` | 152,189 hp（利根）/ 152,915 hp（筑摩）只在 tier E。 |
| 试航实测航速 | `propulsion.speed.trial` | 35.55 kn（利根公试）/ 35.44 kn、35.74 kn（筑摩）只在 tier E。 |
| 公试吃水 6.23 m | `dimensions.draught.mean` 的第二值 | 同上，tier E。 |
| **机库（有无/尺寸）** | `aviation.hangar.*` | 「本级没有机库」只有 tier E 有正面表述（日文「格納庫はない」）。navypedia 与 pwe 都只写机数，**没有一句正面说「无机库」**，所以 0 也不能填（0 = 设计上就没有，需来源直说）。 |
| 主炮塔逐座布置（哪座背负、哪两座朝后） | `mount.position` 的细分 | 日文百科写得最细但属 tier E；combinedfleet 只到「四座全在前、舰尾无炮」。故 `mount.position` 只写 `fore`，**没有拆成四个 mount 实体**。 |
| 鱼雷再装填机构（有无备雷装填装置、备雷数） | `armament.torpedo.*` 无对应字段 | navypedia 的 `(24)` 含义未解释（携雷总数 or 备雷数，两种读法差一倍），不猜。 |
| 高角炮 12.7 cm 的装舰年份（逐舰） | `mount.installed` | navweaps 只给炮座型号，不给本级装舰年份；建造期推定属推算。 |
| 筑摩 1944-06/07 改装后的 25 mm 总数 | `armament.aa_25mm.count`（最终状态） | navypedia 只给增量（+4 座三联 +23 挺单装），未说旧双联是否保留；相加得 57 属自算，55 只在 tier E 且自称「推定」。两条路都不合法，故留空。 |
| 筑摩 1944-10-25 阵亡总数 | `service.casualties`（全生涯） | 来源只给「约 120 人生还」。用 850 减 121 是推算，不做。 |
| 利根 1945-07 伤亡数 | `service.casualties` | 两源都未给。 |
| 雷达型号的正式番号（一号三型等） | — | combinedfleet/TROM 只用「Type 21 / 22 / 13」，细节型号只有日文来源。 |
| 装甲总重的口径 | `protection.armor.weight` 的判定 | pwe 给 `2073 tons` 但未说是否含炮座与司令塔、是否含防雷隔壁，故只登记数值并带注，未据此算 `weight_ratio`。 |
| 定员的逐舰差异（869 / 874） | `service.complement.standard` | 只在 tier E。**利根与筑摩都按舰级 850 处理。** |

---

## 6. 有争议的记载（单列，不裁决）

### 6.1 标准排水量：11,215 vs 11,213

- **11,215**（本站采用，两源互证）：navypedia `Displacement standard, t11215`；
  pwe `11,215 tons standard displacement`。
- **11,213**：英文维基 `11,213 tons (11,392 tonnes) (standard load)`；
  日文维基 `基準排水量 11,213トン`。
- 两者差 2 t，在换算/取整量级内。本站按「tier E 不作 fact 来源」的规矩取 11,215，
  11,213 不进 fact。

### 6.2 满载排水量：15,200 vs 15,443

- **15,200**（本站采用）：navypedia `Displacement full, t15200`。
- **15,443**：英文维基 `15,200 tons (15,443 tonnes) (full load)` ——
  注意这句本身是「15,200 短吨 = 15,443 公吨」的换算写法，
  **不是两个独立测量值**。英文维基把它写成 `15,200 tons (15,443 tonnes)`，
  日文维基与单舰页又写成 `15,443 (final)`，容易读成「满载 15,443」。
  本站按 navypedia 的 15,200 登记，并在此说明换算关系。

### 6.3 弹药库装带：145 mm vs 225 mm

- **145 mm**（本站采用，两源互证）：navypedia `to 145mm of waterline belt abreast
  [magazines]`；pwe `5.7" to 2.2" (145mm to 55mm) NVNC magazine belt`。
- **225 mm**：英文维基 `The main belt armor was 150 mm (5.9 in) thick next to
  machinery spaces (225 mm (8.9 in) next to magazines)`，
  同一句还把机舱段写成 150 mm（navypedia 是 100 mm）。
- **225 mm 这个数字在任何非 E 级来源里都找不到**，且与「本级防护优于最上型但
  弹药库只加强到 145」的叙述矛盾。本站不采用，仅记在此。

### 6.4 横向舱壁厚度：105–67 / 175–130 vs 175–67

- navypedia：机舱段 `105-67mm`，弹药库段 `175-130mm`（两段分列）。
- pwe：`6.9" to 2.6" (175mm to 67mm) NVNC bulkheads`（一段笼统给区间）。
- 两说在「弹药库段上缘 175」这一点一致，在「机舱段上缘是 105 还是 175」不一致。
  本站按两段各登记一条（105 与 175），并把 pwe 的 175–67 记进 note。

### 6.5 司令塔：100/50 vs 130–70/40

- navypedia：`CT had 100mm sides and 50mm roof.`
- pwe：`5.1" to 2.6" (130 mm to 70mm) side/1.6" (40mm) overhead conning tower`
- 两说差 30–50 mm。本站 `armor.thickness` 的 qual 只有 `side`/`roof` 两级，
  无法表达 pwe 的区间，故登记 navypedia 的 100/50 两条，pwe 值记进 note。

### 6.6 载油与续航：2,690/8,000 vs 2,163/9,000

- navypedia：`Fuel, t oil 2690` / `Endurance, nm(kts)8000(18)`
- pwe：`Bunkerage | 2163 tons fuel oil` / `Range | 9000 nautical miles at 18 knots`
- 两源对应的航速相同（18 kn），但油量与续航都不同，且方向相反
  （油少反而续航远），说明其中一源的口径必有问题，但两源都没交代。
  四条 fact 两两并列，不裁决。

### 6.7 利根 21 号雷达的撤除时间：1944-11-17 vs 1945-02

- combinedfleet：`17 November 1944: Arrives at Maizuru. Drydocked. … Her Type 21
  radar is replaced with a Type 22.`
- navypedia：`2/1945, Tone: - 7 x 1 - 25/60, 21-go radar; + 4 x 3 - 25/60 96-shiki,
  2-shiki 2-go radar (3rd)`
- 日文百科也记 1945-02（tier E）。
- 本站取 combinedfleet 的 1944-11-17（进坞确切日期），差异记在此与单舰 note。
  **若主会话倾向 navypedia 的月份，只需改 `ships/tone.yaml` 两条 fact 的 valid 边界。**

### 6.8 筑摩的沉没原因

- combinedfleet：三次空袭中雷后自行倾覆（详见 §4.2）。
- navypedia：`sunk by destroyer Nowaki`（野分雷击处分）。
- 日文百科与 navypedia 同侧（「駆逐艦野分により雷撃処分された」，tier E）。
- 本站写成两条 `construction.fate_type`（`sunk_by_enemy` / `sunk_by_own_forces`），
  各带来源，note 写「两说并列，不裁决」。

### 6.9 载机数：编制 6 / 设计上限 8 / 实载 5

- navypedia：编制 `6 seaplanes (3 E7K1, 3 E8N1)`
- pwe：`designed to carry up to eight seaplanes, it appears that the ships never
  carried more than five, and this was reduced to four later in the war`
- 三个数字不是同一件事（设计编制 / 理论极限 / 实战实载），
  本站登记 6（编制）与 5（实载上限）两条，8 与 4 记进 note 与本文件。

---

## 7. 与已有数据的衔接（给主会话）

1. **武器实体**：本轮新建 `weapon:20cm-3ns-no2`。它**不是** `weapon:20cm-3ns`
   的重复——后者是 No.1 炮（20.0 cm、870 mps、Akagi/Kaga 用），
   前者是 No.2 炮（20.32 cm、840 mps、Takao/Tone 用）。
   `validate.py` 通过 `about: weapon:*` 收集武器 id，
   所以新 id 会自动被识别为「已登记实体」，不会报 404。
   **但武器正文页 `data/weapon-articles/20cm-3ns-no2.yaml` 本轮没有写**
   （本轮范围只有技术数据），若要让该实体在站内可点，需主会话另派。
2. **复用未重复登记**：`navweaps-20cm-3ns` / `navweaps-127cm-89` /
   `navweaps-25mm-96` 三条已在 `data/sources.yaml`，本轮直接复用。
3. **tier E 来源登记了 3 条但零引用**：`wiki-en-tone-class` /
   `wiki-ja-tone-class` / `wiki-ja-tone-ship`，role 只有 `lead`。
   自检脚本已确认没有任何 fact 以它们为 src。
4. **本轮没有写**：`slices/`、`articles/`、`data/images.yaml`。
5. **一个待主会话决定的结构问题**：`protection.scheme` 我填了 `other`。
   理由是没有任何来源直接给体系名，而「内侧倾斜装带 + 集中防御 + 多层液舱」
   既不是纯 all-or-nothing 也不是纯 incremental。若主会话认为应归
   `incremental`（因为日本重巡普遍按此），改一条即可，但需要主会话给出依据来源。

---

## 交付摘要

| 项 | 数量 |
|---|---|
| 舰级文件 | 1（`classes/tone.yaml`，91 fact） |
| 单舰文件 | 2（`ships/tone.yaml` 25 fact、`ships/chikuma.yaml` 23 fact） |
| 切片文件 | 0（本轮不做） |
| 正文文件 | 0（本轮不做） |
| 新登记来源 | 8（tier B 2 条、tier D 3 条、tier E 3 条零引用） |
| fact 总数 | 139 |
| 其中带 `about: weapon:*` | 16（全部指向 `weapon:20cm-3ns-no2`） |
| 其中带 `about: mount:*` | 13（2 个 mount 实体） |
| 其中带 `qual`（装甲按部位） | 20 |
| 自检 | YAML 4 文件全部可解析；错误 0 / 警告 0 |

### 卡住的地方

- **日方一手档案完全没拿到。** 日文百科引了防卫省防卫研究所的档案号
  （`Ref.C05110625500` 利根要目、`Ref.C05110626300` 筑摩要目），
  但档案是 JACAR 的 PDF 扫描，本轮未抓。这一层不补，本级所有「公试值」
  （13,320 t / 35.55 kn / 152,189 hp / 6.23 m）都只能留在「未获取」。
- **「无机库」这个利根级最出名的特征，反而没有非 E 级来源正面写过。**
  navypedia 与 pwe 都只说机数与弹射器。所以 `aviation.hangar.*` 全部留空。
- **筑摩 1944 年之后的 25 mm 总数没有可靠总数**（详见 §5 最后几条）。
- **主炮塔逐座布置**（哪座背负、哪两座朝后）只有在 tier E 里写清，
  故 `mount:` 实体只建了一个组实体，没拆四座。
- 打了 20 多个站点，`ww2db` / `militaryfactory` / `world-war.co.uk` 全是 403，
  `hazegray` / `history.navy.mil` / `nishidah` 全部 TLS 层被拦（本机问题，非站点问题）。

### 有争议的记载（五处，均已并列或留档）

1. 标准排水量 11,215（navypedia+pwe）vs 11,213（tier E）—— 取前者。
2. 弹药库装带 145 mm（navypedia+pwe）vs 225 mm（tier E）—— 取前者，
   225 mm 在任何非 E 级来源都查不到。
3. 司令塔 100/50（navypedia）vs 130–70/40（pwe）—— 两条都留。
4. 载油 / 续航 2,690/8,000（navypedia）vs 2,163/9,000（pwe）—— 四条都留，不裁决。
5. 筑摩沉没原因「空袭击沉」（combinedfleet）vs「野分雷击处分」（navypedia）——
   写成两条 `fate_type`，不裁决。
   另：利根 21 号雷达撤除时间 1944-11-17（combinedfleet）vs 1945-02（navypedia），
   取前者并在 note 保留后者。
