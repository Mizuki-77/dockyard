# HMS King George V（英王乔治五世号，舷号 41）— 技术数据与生涯时间线

> 检索日期：2026-11-18。
> **硬规则执行说明**：本文每个数值后附来源缩写、URL 与英文原句；凡查不到原话支撑者一律写「未获取」，不做推测填充。
> 全部分歧并列，**不做裁决**，仅注明「疑为 X 口径」。
> 来源优先级：NavWeaps > navypedia > Royal Museums Greenwich（RMG，档案机构一手研究指南）> kbismarck.com > naval-history.net / tynebuiltships / Hansard > Wikipedia（仅作线索与交叉核对）。
> 单位换算若为本报告所做，均标注「（本报告换算）」。

---

## 0. YAML 片段（便于直接落库）

```yaml
ship:
  name: HMS King George V
  name_origin: "英王乔治五世（King George V）；原拟名 HMS King George VI，国王本人要求改为纪念其父"
  class: "King George V class（英王乔治五世级）battleship"
  class_built: 5
  yards:
    - "Vickers-Armstrong, Walker Navy Yard, Newcastle-upon-Tyne（本舰）"
    - "Cammell Laird, Birkenhead（Prince of Wales）"
    - "John Brown, Clydebank（Duke of York）"
    - "Swan Hunter, Wallsend（Anson）"
    - "Fairfield, Govan（Howe）"
  builder: "Vickers-Armstrong, Walker Navy Yard, Newcastle-upon-Tyne"
  yard_number: 10
  pendant_number: "41"
  nickname: "KGV"
  fleet:
    - "Home Fleet（1940-12-11 起，Scapa Flow 为主要基地，至 1944）"
    - "Force H / Force Z 分队（1943-05 起临时配属）"
    - "British Pacific Fleet / Task Force 57（1944-10 起）"
  ordered: "1936-07-29"
  laid_down: "1937-01-01"
  launched: "1939-02-21"
  launched_by: "HM King George VI"
  commissioned: "1940-10-01（for trials）"
  joins_home_fleet: "1940-12-11（至 Scapa Flow 加入本土舰队）"
  cost: "未获取（单舰精确值）；Hansard 1957 给同级四舰均价约 £8.5M"
  fate: "1958 起由 Arnott Young & Co 在 Dalmuir 拆解，舰体拖至 Troon 拆完"

dimensions:
  length_oa: "227.1 m / 745 ft 0.13 in（RMG）"
  length_wl: "225.6 m / 740 ft 0.25 in（RMG，本报告换算）"
  length_pp: "213.4 m / 700 ft 0.25 in（RMG / navypedia）"
  beam_max: "34.2 m / 112 ft 4.25 in（RMG，本报告换算）"
  beam_wl: "31.5 m / 103 ft 2.56 in（RMG，本报告换算）"
  draught_standard_1940: "8.84 m / 29 ft（mean）"
  draught_deep_1940: "9.90 m / 32 ft 6 in（mean）"
  depth_at_side: "15.6 m / 51 ft 1.31 in（RMG，本报告换算）"
  block_coefficient: "未获取"
  waterplane_area: "未获取"
  freeboard: "未获取具体数值；仅有一句「freeboard 过低」的定性原文"

displacement:
  1940_standard: "38,031 t（RMG）"
  1940_deep: "42,237 t（RMG）"
  1945_standard: "39,100 t（RMG）"
  1945_deep: "44,460 t（RMG）"
  navypedia_standard: "36,727 t"
  navypedia_full: "42,076 t"
  light: "未获取（各来源均不设「空载」一栏）"

machinery:
  boilers: "8 × Admiralty 3-drum small-tube，带过热器"
  boiler_pressure_max: "400 lb/sq in（RMG）"
  steam_temperature: "未获取"
  boiler_heating_surface: "78,144 ft²（wiki 单舰页，转引来源）"
  turbines: "4 × Parsons single-reduction geared，4 轴"
  screws: "4 × 三叶锰青铜，直径 14 ft 6 in / 14.5 ft（两说）"
  power_designed: "110,000 shp"
  power_trials: "125,000 shp（wiki 单舰页 infobox）— 与 110,000 存分歧，见 §5"
  speed_designed: "28 kn"
  speed_trials: "28.0 kn（1941 trials，wiki）；28.25 kn（tynebuiltships）"
  endurance: "14,000 nm @10 kn / 10,250 nm @15 kn / 4,000 nm @25 kn（设计值）；16 kn 实测约 6,300 nm"
  fuel_oil: "3,700 t（navypedia，后改 4,030）；3,918 t（wiki 单舰页）；4,100 t 最大 / 3,886 t 平均（nh）"
  generators: "未获取（功率与台数均无原话）"

armour:
  main_belt: "弹药库段 373 mm（14.7 in） cemented + 25.4 mm cement + 22.2 mm Ducol；机舱段 349 mm（13.7 in）"
  main_belt_size: "高 7.2 m（23.5 ft），从主装甲甲板延伸到深水线以下 4.6 m；沿舰自前炮塔前至后炮塔后"
  lower_belt: "下段递减至 4.5–5.5 in（114–140 mm）"
  inclination: "无倾角（navypedia：「placed without a declination」）"
  deck_magazines: "三层共 232 mm：32 mm Ducol + 149 mm 非渗碳装甲钢 + 13 mm Ducol，另有 1.5 in splinter deck"
  deck_machinery: "124 mm（4.88 in）非渗碳装甲钢 + 13 mm Ducol"
  turret: "正面 324 mm（12.75 in），炮室处侧面 225 mm（8.84 in），侧面与后部 174–225 mm，顶 149 mm（5.88 in）"
  barbette: "侧面 324 mm（12.75 in），炮塔前 298 mm（11.76 in），炮塔后 275 mm（10.82 in）"
  conning_tower: "侧 102 mm（4 in），前后 75 mm（3 in），顶 38 mm（1.47 in）（wiki 舰级页）；navypedia 另给 114–76 mm 侧 / 51 mm 顶，见 §6"
  torpedo_protection: "深 4.1 m，设计抗 454 kg TNT（navypedia）；SPS 设计指标 1,000 lb（wiki 舰级页）"
  armour_weight: "12,413 t，占 34,133 t 的 32.5%（RMG）"
  steel_types: " cemented armour（表面渗碳）、non-cemented steel armour、Ducol (D) steel、'composition material'（cement）"

armament:
  main: "10 × 14 in/45 BL Mk VII：2 座 Mk III 四联（A 前、Y 后）+ 1 座 Mk II 双联（B 前背负）"
  secondary: "16 × 5.25 in/50 QF Mk I，8 座双联 HA/LA Mk I 两用炮塔"
  pompom_1940: "4 × 八联 2-pdr Mk VI（32 门）"
  up_rockets_1940: "4 × UP 二十管发射器（B 炮塔顶 1、Y 炮塔顶 2、舰尾 1）"
  bofors: "1944-07 起 2 座四联美制 40 mm Mk II；1945-09 另有 2 座单装英制 40 mm"
  oerlikon: "1941-12 起 18 门单装 20 mm；1944-07 增至 26 单装 + 6 双联；1945-09 为 24 单装 + 6 双联"
  torpedoes: "无（各来源装备表均无鱼雷发射管，见 §7 说明）"

fire_control:
  table: "Admiralty Fire Control Table Mk IX"
  main_directors: "2 座主炮指挥仪塔（前桅楼顶 1、主桅后 1），各配 15 ft 测距仪"
  turret_rangefinders: "A / Y 炮塔内置 41 ft；B 炮塔 30 ft"
  secondary_directors: "4 × HACS Mk IVGB（KGV 与 PoW 独有；后续舰为 Mk V / Mk VI）"
  pompom_directors: "6 × Mk IV pom-pom director，均带 Gyro Rate Unit 测速瞄准"
  radar_1940: "Type 279（对空警戒）+ Type 284（主炮测距）"
  radar_1941_05: "同上两型（Type 271 是 1941-06-15~30 才装）"
  radar_later: "Type 273、Type 282×5、Type 285×4（1941 末—1942）；1944 改 279B、284→274，加 277/293"

aviation:
  catapult: "1 座 D-III-H 双向弹射器"
  aircraft: "Walrus（1941 年初 2 架带 ASV 11N 雷达）；编制表给 2–4 架"
  crane: "未获取（型号与位置均无原话）"
  removal: "1944-02~06 利物浦改装中拆除弹射器与水机，原位改建上层建筑安置小艇"

complement:
  navypedia: "1,422"
  rmg: "未获取"
  wiki_class: "1,422 (1941)"
  wiki_kgv: "1,314 – 1,631"
  maritimequest: "1,422 平时 / 1,511 战时"
  1941_05_actual: "未获取"

camouflage:
  1941_05: "未获取（无任何来源明文写 KGV 1941-05 的具体色号）"
  home_fleet_norm_1940_41: "overall medium grey（507B）"
```

---

## 1. 身份

### 舰级（King George V class，5 艘）

- King George V 级，同级建成 5 艘 —— Wikipedia 舰级页「Five ships of this class were built」https://en.wikipedia.org/wiki/King_George_V-class_battleship_(1939)
- 五舰及其厂、舷号（navypedia 表格）：King George V / 41 / Yard 10 / Vickers-Armstrong, Tyne；Prince of Wales / 53 / Yard 1026 / Cammell Laird, Birkenhead；Duke of York (ex-Anson) / 17 / Yard 554 / John Brown, Clydebank；Anson (ex-Jellicoe) / 79 / Yard 1553 / Swan Hunter, Wallsend；Howe (ex-Beatty) / 32 / Yard 669 / Fairfield, Govan —— navypedia「King George V battleships (5, 1940 - 1942)」https://www.navypedia.org/ships/uk/brit_bb1_king_george_v.htm
- **注意同名混淆**：navypedia 上另有一级 1912 年的「King George V」战列舰（`brit_bb_kinggeorgev.htm`），与本级无关；本舰为「第二次使用该舰名」。

### 舰名来源（King George V）

- RMG（Royal Museums Greenwich 研究指南 B9）：「Originally, she was to have been named HMS King George VI following the tradition of naming the first capital ship of a new reign after the monarch. The King requested that the ship be named in honour of his late father, King George V, after whom an earlier class of battleships had been named in 1911.」https://www.rmg.co.uk/collections/research-guides/research-guide-b9-royal-navy-hms-king-george-v
- 同上：「A later member of this class of battleship was named HMS Duke of York in honour of the King instead」——即国王本人的名号让给了二号舰 Duke of York（本条为命名让渡的旁证）。
- naval-history.net：「as the second major RN ship to carry this name, previously carried by a 1911 battleship sold in 1926」https://www.naval-history.net/xGM-Chrono-01BB-HMS_King_George_V.htm

### 舷号 41

- RMG 年表：「1 October 1940: Commissioned – pendant number 41」
- tynebuiltships：「Lead ship of the 5 strong KING GEORGE V Class & allocated pennant number 41」https://www.tynebuiltships.co.uk/K-Ships/kinggeorgev1940.html
- maritimequest：「Pennant Number: 41」https://www.maritimequest.com/warship_directory/great_britain/battleships/king_george_v/hms_king_george_v_data.htm

### 建造代号 / 船台号

- navypedia 表：「Yard No 10」
- tynebuiltships：「Yard Number: 10」「Yard: High Walker」

### 所属舰队

- RMG：「She was assigned to the Home Fleet at Scapa Flow, and this remained her principal base until 1944.」→ 1941-04-01 起为本土舰队旗舰（Tovey 上将）。
- RMG 1944：「Sails to Trincomalee, Ceylon, to join newly-formed British Pacific Fleet (BPF). Hoists flag of Rear-Admiral Sir Bernard Rawlings」
- 1943 年临时配属 Force H：naval-history.net「for temporary duty with Force H… (This deployment was to reinforce Force H in preparation for Operation HUSKY, the invasion of Sicily)」

### 绰号

- Wikipedia 单舰页 infobox：「nickname = KGV」https://en.wikipedia.org/wiki/HMS_King_George_V_(41)
- **除此之外未见任何来源给出别的绰号**。对比同级/他舰（Hood 有 "The Mighty Hood" 等），KGV 无类似流传绰号，此处不做补充。

### 舰徽（badge）

- naval-history.net：「On a Field Blue, the Royal Cypher of HM King George V ensigned by the Imperial Crown proper.」

---

## 2. 建造

### 下单

- navypedia / wiki 建造表 / RMG / maritimequest 一致：1936-07-29
- naval-history.net：「ordered 29 July 1936 under 1936 Build Programme」
- maritimequest：「Ordered: July 29, 1936」
- 无分歧。

### 铺龙骨

- RMG：「1 January 1937: Laid down at Walker Navy Yard, Newcastle-upon-Tyne」
- navypedia：「1.1.1937」
- tynebuiltships：「Keel: 01/01/1937」
- naval-history.net：「laid down on 1 January 1937」
- 无分歧。

### 下水（日期 + 掷瓶人）

- RMG：「21 February 1939: Launched by HM King George VI」/「The King George V was launched by King George VI on 21 February 1939」
- navypedia：「21.2.1939」
- tynebuiltships：「Launched: 21/02/1939」
- maritimequest：「Launched: February 21, 1939」
- **掷瓶人 = 英王乔治六世本人**（RMG 唯一明确写出，其余来源只给日期）。此条与「原拟名 King George VI」互为因果，是命名让渡的直接证据。

### 服役

- **1 October 1940 = commissioned（服役，但未完工）**
  - RMG：「1 October 1940: Commissioned – pendant number 41」；「she was commissioned into the Royal Navy on 1 October 1940」
  - maritimequest：「Commissioned: October 1, 1940」
  - naval-history.net：「October 1st - Commissioned for trials at Vickers Armstrong, Newcastle on Tyne. Commanding officer Captain W. R. Patterson CVO RN… at the time of commissioning she was incomplete and was to be taken to Rosyth for completion」
  - wiki 舰级页建造表：「commissioned 1 October 1940」
- **11 December 1940 = 完工/加入本土舰队**
  - navypedia：「Comp 11.12.1940」
  - tynebuiltships：「Completed: 11/12/1940」
  - RMG：「11 December 1940: Joins Home Fleet at Scapa Flow」
  - Hansard 1957-03-20：「"KING GEORGE V". Commissioned 11th December, 1940.」https://api.parliament.uk/historic-hansard/commons/1957/mar/20/battleships
  - wiki 单舰页正文：「commissioned on 11 December 1940」
- **分歧原因**：不是真矛盾，是「服役（commissioned for trials）」与「完工/加入舰队（completed / joins Home Fleet）」两个节点被不同来源各自标成「commissioned」。naval-history.net 明写 10-01 是「for trials」且「incomplete」，RMG 明写 12-11 是「Joins Home Fleet」——两者合起来即解释全部。**残留分歧**：naval-history.net 正文另一处把完工写成「Build was completed on 11th December 1941」，「1941」为该页自身笔误（同页上文与全部其他来源均为 1940）。
- 舰长（首任）：Captain W. R. Patterson，1940-07-15 任命（RMG 与 naval-history.net 一致）。

### 造价（币值 + 年份）

- **单舰精确值：未获取。**
- 议会口径（1957-03-20）：Hansard 原文「Her Majesty's Ships "King George V," "Duke of York," "Anson", and "Howe" were completed between 1940 and 1942 at a cost of approximately £M8½ each.」——即四舰**均价约 £8,500,000**，未分舰，也未注币值年份（英国战时计价惯例为当年英镑）。URL 同上。
- 官方 1939 答复（未给 KGV 数）：「No battleship has been completed since the "Rodney" in 1927 which cost approximately £6,150,000. No battle cruiser has been completed since the "Hood" in 1920, which cost approximately £5,700,000.」并附「The foregoing figures are exclusive of the cost of first outfit and reserves of guns, torpedoes and ammunition.」https://api.parliament.uk/historic-hansard/written-answers/1939/mar/15/royal-navy-ship-construction-costs —— 该答复明确说明造价口径**不含首备弹药与火炮储备**。
- 二手引述（**原页 403，未能直接核验**）：Buxton & Johnston《The Battleship Builders》被引为「King George V - £7,391,000 / Prince of Wales - £7,426,000」。仅作线索登记，不作数据来源。
- 存疑点：£7,391,000（单舰，含或不含首备不明）vs £8.5M（四舰均价）——两者差约 15%，疑为口径差（是否含首备、是否含改装），**不做裁决**。

---

## 3. 主尺度

### 全长（oa）

- 227.1 m / 745 ft 0.13 in —— RMG「Length: 745ft 0.13in overall」https://www.rmg.co.uk/collections/research-guides/research-guide-b9-royal-navy-hms-king-george-v
- 227.1 m —— navypedia「Length, m: 213.4 pp 227.1 oa」https://www.navypedia.org/ships/uk/brit_bb1_king_george_v.htm
- 227.1 m（745 ft 1 in）—— wiki 舰级页「Length 745 ft 1 in (227.1 m) o/a」
- 745 ft —— wiki 单舰页 infobox「length = 745 ft」
- 745 ft —— maritimequest「Length: 745'」
- **分歧**：0.13 in 与 1 in 的差（745'0.13" vs 745'1"），仅 2 cm 级，疑为**英制取整口径**不同。所有公制值同为 227.1 m，无实质分歧。

### 水线长（wl）

- 225.6 m / 740 ft 0.25 in —— RMG「Length: … 740ft 0.25in waterline」（本报告换算：740 ft = 225.55 m）
- **其余来源均未给水线长**。此为 RMG 独有数据。

### 垂线间长（pp）

- 213.4 m / 700 ft 0.25 in —— RMG「700ft 0.25in between perpendiculars」
- 213.4 m —— navypedia「213.4 pp」
- 213.4 m —— wiki 舰级页「(213.4 m) (between perpendiculars)」
- 无实质分歧（RMG 的 700'0.25" = 213.37 m）。

### 最大宽

- 34.2 m / 112 ft 4.25 in —— RMG「Beam: 112ft 4.25in max」（本报告换算：112'4.25" = 34.24 m）
- 112 ft —— wiki 单舰页正文「beam 112 ft」
- **分歧**：navypedia「Breadth, m: 31.4」、wiki 舰级页「Beam 103 ft 2.5 in (31.5 m)」、tynebuiltships「103.0 ft」——这几家给的是**水线宽**，而非最大宽（含防雷鼓包/外板突出部）。RMG 把两者分列（112'4.25" max / 103'2.56" waterline），可解释全部差异。

### 水线宽

- 31.5 m / 103 ft 2.56 in —— RMG「103ft 2.56in waterline」
- 31.4 m —— navypedia「Breadth, m: 31.4」
- 31.5 m（103 ft 2.5 in）—— wiki 舰级页
- 103.0 ft —— tynebuiltships「700.0 x 103.0 x 29.0ft」
- **分歧**：31.4 vs 31.5 m，1 dm 级，疑为换算取整。

### 吃水

- 标准 8.84 m / 满载 9.90 m（mean）—— navypedia「Draught, m: 8.84 (9.90 mean at deep load)」
- 标准 29 ft（mean）/ 满载 32 ft 6 in（mean）—— RMG「Draught (1940): Standard – 29ft (mean), Deep load – 32ft 6in (mean)」（换算 8.84 m / 9.91 m，与 navypedia 吻合）
- 32.6 ft —— wiki 单舰页 infobox「draught = 32.6 ft」（只给一个值，疑为满载）
- 33 ft 7.5 in（10.2 m）—— wiki 舰级页「Draught 33 ft 7.5 in (10.2 m)」
- 34 ft —— wiki 单舰页正文「draught 34 ft」
- 29.0 ft —— tynebuiltships「700.0 x 103.0 x 29.0ft」
- **分歧原因**：三套口径混用——① 设计标准吃水（29 ft / 8.84 m）② 1940 年实测满载（32'6" / 9.90 m）③ 战时超载后的实际吃水（33'7.5" / 10.2 m、34 ft）。wiki 单舰页正文的「34 ft」与 infobox 的「32.6 ft」在同一页内即已矛盾。RMG 1945 年数据未单列吃水，但排水量已从 42,237 t 涨到 44,460 t，吃水随之增加可解释 10.2 m 一档。

### 型深（depth at side）

- 15.6 m / 51 ft 1.31 in —— RMG「Depth at side: 51ft 1.31in」（本报告换算）
- **其余来源均未给型深**。RMG 独有。

### 方形系数

- **未获取。** 全部已抓来源（navypedia、RMG、wiki 两页、maritimequest、tynebuiltships、navweaps）均未给出 Cb 值。

### 水线面积

- **未获取。** 同上，无来源给出该值。

### 干舷

- **具体数值：未获取。** 只有定性原文：
  - wiki 单舰页：「Designed within the tight 35,000 ton limitations of the Washington Naval Treaty, wartime service necessitated increases over the design displacement, seriously reducing freeboard and affecting seaworthiness. This was most acute at the already low bow. With too little buoyancy forward the bows were easily buried even in moderate seas, with spray washing up over both forward turrets. Heavy seas could flood 'A' turret, drenching both men and machinery within.」
  - naval-history.net（最终战当天）：「In addition the low freeboard forward caused significant flooding of shell rooms in the heavy weather.」
  - 干舷低是本级公认缺陷，但**没有任何来源给出英尺数**，故不填数字。

---

## 4. 排水量

### 1940 年（服役时）

- 标准 38,031 t / 满载 42,237 t —— RMG「1940 Standard: 38,031 tons – Deep load: 42,237 tons」
- 同上数值 —— wiki 单舰页：「She displaced 38,031 tons at normal load and 42,237 tons at full load.」（注意这里把 38,031 叫 **normal load**，与 RMG 的 **Standard** 不同名）
- 标准 36,730 t / 满载 42,080 t —— maritimequest「Displacement: 36.730 std. / 42,080 full」
- 标准 36,727 t / 满载 42,076 t —— navypedia「Displacement standard, t: 36727 / Displacement full, t: 42076」
- 标准 36,730 t / 满载 42,080 t —— tynebuiltships「36730disp - 42080disp」
- 42,200 t（1941）—— wiki 单舰页 infobox「displacement = 42,200 tons (1941)」
- 44,400 t —— kbismarck.com 最终战参战表 https://www.kbismarck.com/bismarck-last-battle.html

### 1944–45 年（改装后）

- 标准 39,100 t / 满载 44,460 t —— RMG「1945 Standard: 39,100 tons – Deep load: 44,460 tons」
- 同上 —— wiki 单舰页：「After her refit in 1944, she displaced 39,100 tons at standard load, and 44,460 tons at full load.」
- 39,100 / 44,460 t —— navypedia（挂在 Prince of Wales 12/1941 条目下，实为该级后期状态）「displacement was 39100/ 44460t」

### 空载（light）

- **未获取。** 所有来源都不设「空载」一栏；最接近的是 RMG 的 Weights 分解（见 §6），但那是重量分组而非排水量。

### 最大（maximum）

- **未获取**（没有任何来源给「maximum displacement」这一档；kbismarck 的 44,400 mt 是其自设口径，见下）。

### 分歧汇总

- **36,727 / 36,730 / 38,031 t 三个「标准」值**：前两者（navypedia、maritimequest、tynebuiltships）几乎同源（36,730 t ≈ 36,727 t，差 3 t 为换算），是**设计标准排水量**；38,031 t 是 RMG（档案机构，基于 1940 年实际状态）给出的**服役时实测标准排水量**，wiki 单舰页转引 RMG。差额约 1,300 t，原因是建成后实际重量超出设计（增设高炮、雷达、装甲补强等）。
- **42,237 / 42,080 / 42,076 / 42,200 t 四个「满载」值**：42,237（RMG 1940 deep）与 42,080（设计 full，navypedia/tyne）差 157 t；42,200 是 wiki infobox 的 1941 年取整。
- **44,400 mt（kbismarck）**：该站最终战参战表给 KGV 44,400 mt，比 RMG 1945 年 deep load（44,460 t）略低，疑为其自算的「战时满载」。**不做裁决**。
- 口径提醒：**long ton（英吨，1,016 kg）与 metric ton（1,000 kg）在不同来源间混用**，本文照原文抄录，不做统一换算。

---

## 5. 动力

### 锅炉（型号 / 数量 / 压力 / 温度）

- 型号数量：8 台 Admiralty 三鼓小管锅炉，带过热器
  - navypedia：「8 Admiralty 3-drum boilers」
  - RMG：「Boilers: 8 x Admiralty 3-drum small-tube with superheaters」
  - wiki 单舰页：「eight Admiralty boilers」「8 Admiralty three-drum small-tube boilers with superheaters」
  - maritimequest：「8 Admiralty 3 drum type (oil fired)」
- 最大工作压力：**400 lb/sq in** —— RMG「Working pressure (max): 400lb/sq in」（约 28.1 kgf/cm²，本报告换算）
- 蒸汽温度：**未获取。** 无来源给出过热蒸汽温度（对比俾斯麦：navypedia 给 12 台 Wagner 锅炉 58 atm / 475 °C）。
- 受热面积：78,144 ft²（7,259.8 m²）—— wiki 单舰页「The total heating surface of the boiler plants in King George V was 78,144 ft2 (7,259.8 m2). The 416-ton boiler installation produced more than 100,000 shaft horsepower (75,000 kW)」
- 效率对比（wiki 单舰页原话）：「The eight boilers were more economic in space and fuel than the twenty-four boilers in the battlecruiser HMS Hood.」

### 汽轮机（型号 / 厂家 / 数量）

- 4 套 Parsons 单级减速齿轮汽轮机，4 轴
  - navypedia：「4 sets Parsons geared steam turbines」
  - RMG：「Turbines: 4 x Parsons single-reduction geared, 4 shafts」
  - tynebuiltships：「4 x Steam turbines, Parsons type, SR geared, 110000shp」并注明「Engines by: Vickers-Armstrongs Ltd, Barrow」**——这是唯一给出主机承造厂的来源**
- 结构细节（wiki 单舰页）：「Two main turbines were arranged in series and drove a shaft through double helical gears. An astern turbine was incorporated in the exhaust casing of the low-pressure turbine, and a cruising turbine was coupled directly to the high-pressure turbine.… The turbine unit was a low-speed type (2,257 rpm) coupled to a single reduction gear which produced 236 rpm at the propeller shaft.」

### 轴数与螺旋桨

- 4 轴 —— navypedia「No of shafts: 4」；RMG「4 shafts」
- 螺旋桨：4 只三叶锰青铜
  - RMG：「Propellers: 4 x 3-bladed manganese bronze 14.5ft diameter」
  - wiki 单舰页：「4 three-bladed propellers, 14 ft 6 in diameter」
  - **分歧**：14.5 ft vs 14 ft 6 in —— **其实是同一个数**（14.5 ft = 14'6"），无实质分歧。
- naval-history.net 补一条建造细节：到 Rosyth 后「for the fitting of her outer propellers, strengthening her rudder and to complete installation of armament and radar fit」——即**外侧两只螺旋桨是到 Rosyth 才装的**。

### 设计功率 / 实测功率

- 设计 110,000 shp
  - navypedia：「Power, h. p. 110000」
  - tynebuiltships：「110000shp」
  - maritimequest：「HP: 110,000」
  - wiki 舰级页：「installed power 8 Admiralty 3-drum boilers 110,000 shp (82,000 kW)」
- 实测/试航 125,000 shp —— wiki 单舰页 infobox：「125000 shp」，speed「28.0 kn (1941 trials)」
- **分歧**：110,000 vs 125,000 shp。110,000 是**设计持续功率**（设计指标），125,000 疑为**试航超载功率**（overload）。wiki 单舰页正文另有一句可佐证超载余量：「A speed of 28.5 knots was expected at standard displacement and 27.5 knots at full-load displacement on normal output; corresponding speeds at overload condition were 29.25 and 28.25 knots respectively.」——即设计时就分了 normal output 与 overload 两档。**未找到 125,000 shp 对应的原始试航报告，故不做裁决。**

### 设计航速 / 实测航速

- 设计 28 kn —— navypedia「Max speed, kts 28」；maritimequest「Speed: 28 knots」
- 实测 28.0 kn（1941 trials）—— wiki 单舰页 infobox
- 28.25 kn —— tynebuiltships「4 x Screws, 28.25knots」
- 设计预期分档（wiki 单舰页）：「28.5 knots was expected at standard displacement and 27.5 knots at full-load displacement on normal output; corresponding speeds at overload condition were 29.25 and 28.25 knots respectively.」
- **分歧**：28.0 与 28.25 kn。tynebuiltships 的 28.25 疑取自试航实测（与 wiki 的「overload 28.25 kn at full load」数值巧合），wiki 的 28.0 kn 疑为 1941 年服役状态下测得。**不裁决。**

### 续航（各档）

- 设计值（wiki 单舰页）：「4,000 nautical miles at 25 knots, 10,250 nautical miles at 15 knots and 14,400 nautical miles at 10 knots. However, in practice fuel consumption was much higher, and at 16 knots the actual range was about 6,300 nautical miles with a five per cent reserve allowance.」
- 14,000 nm @10 kn —— maritimequest「Range: 2,540 NM @ 27 knots / 14,000 NM @ 10 knots」
- 14,000 nmi @10 kn —— wiki 舰级页 infobox「range 14,000 nmi at 10 knots」
- 15,600 nm @10 kn —— navypedia「Endurance, nm(kts) 15600(10)」
- 5,400 nmi @18 kn —— wiki 单舰页 infobox「range = 5,400 nmi at 18 kn (11.9 tons/hour fuel burn)」
- **分歧**：10 kn 档有 14,000 / 14,400 / 15,600 nm 三个值。14,000 与 14,400 差 400 nm，疑为**设计理论值与含 5% 储备值之别**；15,600 nm（navypedia）明显更乐观，疑为**理论极值/未扣储备**。18 kn 档 5,400 nmi 是 wiki infobox 独有。
- **实战反证**（重要）：Patterson 战报与 naval-history.net 都记 1941-05-27 战后 KGV 因缺油几乎必须离场——naval-history.net：「KING GEORGE V and RODNEY now retired northerly at an economical speed of 17 knots to conserve fuel」；海军部 1137 电「BISMARCK must be sunk at all costs and if to do this it is necessary for KING GEORGE V to remain on the scene, then she must do so, even if it subsequently means towing KING GEORGE V」。说明**实际可用续航远低于纸面值**，与 wiki 的「in practice fuel consumption was much higher」一致。

### 燃油容量

- 3,700 t 油，后改 4,030 t —— navypedia「Fuel, t: 3700 oil, later 4030」
- 3,918 t 燃油 + 192 t 柴油 + 256 t 备用给水 + 444 t 淡水 —— wiki 单舰页「She could carry 3,918 tons of fuel oil, 192 tons of diesel oil, 256 tons of reserve feed water and 444 tons of freshwater.」
- 最大 4,100 t / 平均 3,886 t —— naval-history.net「(KGV maximum fuel capacity 4100 tons, average capacity 3886 tons)」
- **三说并列**：3,700→4,030（navypedia）、3,918（wiki）、4,100 max / 3,886 avg（nh）。**不做裁决**；疑为「设计容量 / 实际可装 / 含非燃油舱柜」三种口径。

### 电机功率

- **未获取。** 所有已抓来源均未给出主发电机台数与总功率（对比 Hood 也缺此项，属同类资料空白）。已专门检索 naval-history 全文 `dynamo|generator|turbo-generator`，**0 命中**。

### 锅炉/机舱布置（补充）

- **未获取舱段划分的原文描述。** 已抓来源只给锅炉台数与受热面积，未给「几个锅炉舱、如何与机舱交替」的原话，故不填。
- 可用的间接原文（wiki 单舰页）：「The total heating surface of the boiler plants in King George V was 78,144 ft2 (7,259.8 m2). The 416-ton boiler installation produced more than 100,000 shaft horsepower (75,000 kW), giving a top speed of 28 knots.」

---

## 6. 防护

### 主装甲带（厚度 / 高度 / 长度 / 倾角）

**厚度**

- 弹药库段 373 mm（14.7 in）cemented armour + 25.4 mm 水泥 + 22.2 mm Ducol 钢板 —— wiki 舰级页：「along the magazines, the belt was 14.7 inches thick (373 mm) cemented armour, laminated onto 1 inch (25.4 mm) of "composition material" (cement) and an additional 0.875 inch (22.2 mm) of Ducol steel hull plating (this steel was also effective as armour)」https://en.wikipedia.org/wiki/King_George_V-class_battleship_(1939)
- 机舱段 349 mm（13.7 in）—— 同上：「over the machinery spaces, the belt was 13.7 inches (349 mm)」
- 弹药库段 381 mm / 机舱段 356 mm —— navypedia：「Upper part, 4.62m in height was 381mm abreast magazines and 356mm abreast machinery.」https://www.navypedia.org/ships/uk/brit_bb1_king_george_v.htm
- 15 in（381 mm）—— wiki 单舰页 infobox：「Main belt: 15 in」https://en.wikipedia.org/wiki/HMS_King_George_V_(41)
- 348–374 mm —— kbismarck.com 最终战参战表：「Belt 348-374 mm」https://www.kbismarck.com/bismarck-last-battle.html
- **这不是真分歧，wiki 舰级页自己给了官方解释**：「Most secondary and some primary sources describe the maximum thickness of the belt armour varying between 14.7 and 15 inches (due to the practice of indicating plate thicknesses on weight (at 40 lbs per inch of square foot of armour), as opposed to nominal thickness in inches)」——即英国按「每平方英尺 40 磅 = 1 英寸」的重量法标板厚，故「15 in」是重量口径，「14.7 in / 373 mm」是名义厚度口径。navypedia 的 381 mm（=15 in）走重量口径，356 mm（=14 in）与之同理；kbismarck 的 348–374 mm 是由 373 mm 派生的区间。**不做裁决，四值实为两种口径。**

**高度 / 长度 / 延伸**

- 高 7.2 m（23.5 ft），从主装甲甲板延伸到深水线以下 4.6 m（15 ft）—— wiki 舰级页：「The main armour belt was 23.5 feet (7.2 m) high and covered the hull side from the main armoured deck to finish 15 feet (4.6 m) below the deep waterline.」
- 高 7.16 m、长 126.5 m —— navypedia：「External vertical main belt was 7.16m in height and 126.5m in length, it protected citadel between end barbettes.」
- 上段高 4.62 m、下段高 2.54 m —— navypedia（同上）
- 沿舰自前炮塔前至后炮塔后 —— wiki 舰级页：「the belt started just forward of the forward turret and finished just aft of the aft turret. The armour consisted of three equal-depth strakes. The strakes were tongue-and-grooved together, and each individual plate in a strake was keyed into neighbouring plates.」（三层等深列板 + 舌槽咬合 + 逐块键接）
- 下段延伸：前 12.2 m、后 11.3 m —— navypedia：「Lower strike of belt continued for 12.2m fwd and 11.3m aft from citadel.」
- 高度分歧 7.2 vs 7.16 m，4 cm 级换算取整；长度 126.5 m 是 citadel 段，与 wiki「前炮塔前至后炮塔后」基本同义。

**倾角**

- **无倾角** —— navypedia：「The main belt placed without a declination, connecting over a side shell to plating surface (instead of behind it as on Nelson), but thus was notably more widely.」
- 设计理由（wiki 舰级页）：「Post-World War I studies had indicated that it was possible for delayed-action AP shells to dive under a shallow belt and penetrate into vital areas of the ship and therefore the main belt was made to extend as far below the waterline as possible.」——即**用「深带」代替「斜带」**对付水中弹。

### 上装甲带 / 中装甲带

- **未获取「上装甲带」独立数值。** 本级走「all or nothing」+ 深主带方案，navypedia 与 wiki 舰级页均不单列 upper belt 一栏（对比 Bismarck 有 145 mm upper belt、Hood 有 178 mm medium belt / 127 mm upper belt）。
- navypedia：「Here, as well as on Nelson, the principle "all or nothing" was used.」
- 唯一边缘原文（wiki 舰级页）：「The main armoured belt extended forward and aft of the main armoured bulkheads with reduced height to protect the waterline and gradually reduced in thickness from 13 to 5.5 inches.」——这是**主带端部递减段**，不是独立的上装甲带。

### 装甲甲板（分层）

**弹药库上方（三层，共 232 mm）**

- wiki 舰级页：「The horizontal protection over the magazines consisted of three layers with a total thickness of 9.13 in (232 mm); the weather deck consisted of 1.25 in (32 mm) of Ducol (D) steel, the main armoured deck was of non-cemented steel armour 5.88 in (149 mm) thick over a 0.5 in (13 mm) D steel deck and above the shell rooms there was another 1.5-inch splinter deck.」
- 药库在弹库之下 —— 同上：「The powder magazines were below the shell rooms for added protection, a practice that was begun with the Nelson-class battleships.」

**机舱上方（两层）**

- 同上：「The weather deck thickness was the same over the machinery spaces but there the main armoured deck was reduced to 4.88 in (124 mm) over a 0.5 in (13 mm) D steel deck.」

**延伸与递减**

- 同上：「The main armoured deck was continued forward of the forward armoured bulkhead and gradually reduced from full thickness to 2.5 in (64 mm), while aft of the after magazines an armoured turtle-back deck covered the steering gear with 4.5–5 in (110–130 mm) of armour whilst also providing protection along the waterline.」

**navypedia 口径（单层厚值）**

- 「Flat main deck within citadel was 152mm over magazines and 127mm over machinery, it connected with upper edge of main belt. There was a lower deck outside citadel… has thickness 127 - 64mm; its aft part was 114mm thick (127mm over steering gear), closed by 102mm bulkhead.」
- **分歧**：navypedia 给 152 / 127 mm，wiki 给 149+13 / 124+13 mm。152 ≈ 149+13 的装甲板组合口径，127 ≈ 124+取整。**口径差，不裁决。**

### 炮塔（正面 / 侧面 / 顶部 / 背面）

- wiki 舰级页：「The turret faces had 12.75 in (324 mm) of armour at the front; 8.84 inches (225 mm) sides (at the gun chamber); 6.86 inches (284–174 mm) on the sides and rear; the roof plate was 5.88 in (149 mm) thick.」
  - 正面 324 mm，侧面（炮室处）225 mm，侧后 174–225 mm，顶部 149 mm
  - **该页此句英制与公制不对应（6.86 in = 174 mm，284 疑为 224 之误），本文照抄并标注为原页笔误。**
- navypedia：「Turret faces were 324mm, sides was 224 - 174mm.」（未给顶/背单值）
- wiki 单舰页 infobox：「main turrets: 13 in」（=330 mm，疑为取整或含背板）
- 定性（wiki 舰级页）：「The main gun turrets were relatively lightly protected in comparison to contemporary battleships.… Maximum turret and barbette armour was reduced to 12.75 inches in this class from the 16 inches of the Nelson class.… The reduction in turret and barbette armour was a compromise in favour of the thickest possible protection for the magazines.」
- 同上：「To some extent the higher quality of the armour minimised the loss of protection and the turret's flat face improved ballistic resistance at long ranges, while the low profile of the turret minimised target area at closer ranges.」

### 炮座（barbettes）

- wiki 舰级页：「The main armament barbettes were of varying thickness: 12.75 in (324 mm) thick on the sides, 11.76 in (298 mm) forward and 10.82 in (275 mm) aft of the turret.」
- navypedia：「Thickness of barbettes was 330mm at sides, 280mm to amidships, 305mm to ship ends.」
- wiki 单舰页 infobox：「barbettes: 13 in」
- **三说并列**：324/298/275（wiki 舰级页，按炮塔前后分区）vs 330/280/305（navypedia，按中段/两端分区）vs 330（infobox）。分区方式不同 + 重量/名义口径差，**不裁决**。

### 司令塔（conning tower）

- wiki 舰级页：「the King George V class had comparatively light conning tower protection with 4-inch (102 mm) sides, 3 in (75 mm) forward and aft and a 1.47 in (38 mm) roof plate.」
- navypedia：「Conning tower had 114 - 76mm sides and 51mm roof, deck and communication tube.」
- **分歧**：102/75/38 mm（wiki）vs 114–76/51 mm（navypedia）。差 10 mm 级，疑为名义厚度 vs 含衬板/重量口径。**不裁决。**
- 设计理由（wiki 舰级页）：「The RN's analysis of World War I revealed that command personnel were unlikely to use an armoured conning tower, preferring the superior visibility of unarmoured bridge positions.… The conning tower armour was sufficient to protect against smaller ship guns and shell fragments.」

### 横向舱壁

- 前 305 mm（12 in），后 254 mm（10 in）—— wiki 舰级页：「The armoured bulkhead was 12 in (305 mm) thick forward and 10 in (254 mm) thick at the after end of the citadel」
- navypedia：「Thickness of bulkheads was 305 (fore) / 254 (aft)mm over lower deck and 51mm under lower deck.」另于汇总行给「bulkheads: 305 - 102」
- 两源一致（305 / 254），navypedia 多给「下甲板以下 51 mm」层。

### 防雷系统（深度 / 设计指标）

- 深 4.1 m，可抗 454 kg TNT —— navypedia：「Last longitudinal bulkhead was 44mm thick, underwater protection deep was 4.1m. It could resist exploding of 454kg TNT.」
- 设计指标 1,000 lb —— wiki 舰级页：「This scheme was designed to protect against a 1000 lb warhead, and had been tested and found effective in full-scale trials.」
- 结构（wiki 舰级页）：「It was subdivided into a series of longitudinal compartments in a void-liquid-void layout; the outer and inner were filled with air, and the middle compartment with liquid (fuel or water).… The SPS void-liquid-void layer was generally about 13 feet wide, and the auxiliary machinery spaces added approximately another 8 feet of space from the outer hull plating to the major machinery spaces.」
- 内侧保持舱壁：37 mm（机舱段）→ 44 mm（弹药库段）—— 同上：「an armoured bulkhead which varied in thickness from 1.5 in (37 mm) over the machinery spaces to 1.75 inch (44 mm) abreast of the magazines. This bulkhead formed the "holding bulkhead"」
- **「分歧」其实是同值**：454 kg TNT（navypedia）= 1,000 lb（wiki），仅单位不同。
- **实战检验**：navypedia 评语「Internal anti-torpedo protection paid can resist explosion of 450 kgs TNT, however a loss Prince of Wales has shown, that underwater protection does not withstand explosion of much lighter aircraft torpedo.」wiki 舰级页给 2007 年残骸调查：PoW 四雷中三雷打在 SPS 区外，第四雷处保持舱壁完好，沉没主因是「B」螺旋桨轴支架断裂撕裂舱壁（「The conclusion of the subsequent 2009 paper and analysis was that the primary cause of the sinking was uncontained flooding along "B" propeller shaft.」）。

### 装甲总重与占比

- **12,413 t，占 32.5%** —— RMG Weights 表：「Armour: 12,413 tons (32.5%)」https://www.rmg.co.uk/collections/research-guides/research-guide-b9-royal-navy-hms-king-george-v
- 同表另四组：「Hull: 13,830 tons (36.4%) / Outfit: 1,619 tons (4.3%) / Machinery: 2,768 tons (7.3%) / Armament: 7,401 tons (19.5%)」
- 五项相加 = 32,031 t，与隐含分母 34,133 t 差 2,102 t（疑为未列项），RMG 未解释。
- 对照俾斯麦：19,082 t / 约 40% —— kbismarck.com「Bismarck devoted 19,082 mt to belt, deck, turret, underwater, and splinter armour, which amounted to about 40% of its designed combat weight (47,870 mt).」https://www.kbismarck.com/proteccioni.html

### 装甲钢型号（NC / KC 等）

- **英国侧**（wiki 舰级页逐层给名）：
  - 主带：cemented armour（表面渗碳装甲钢）—— 「14.7 inches thick (373 mm) cemented armour」
  - 主装甲甲板：non-cemented steel armour（非渗碳均质装甲钢）—— 「the main armoured deck was of non-cemented steel armour 5.88 in (149 mm) thick」
  - 结构钢兼装甲：Ducol (D) steel —— 「Ducol steel was an extra-high-strength silicon-manganese high-tensile construction steel developed in the 1920s. It had very good armour properties and was used extensively on the King George V…」
  - 主带背衬「composition material」= cement（水泥层）
- **未获取**：英方档案的原始钢种代号表（英国体系为 CA / NC / Ducol / D steel，与德式 KC / Wh 不同名，本文按来源原词列出，**未找到 Admiralty 钢种代号表原件**）。
- 质量评语（wiki 舰级页引 Garzke & Dulin）：「Side armour protection of these ships was better than indicated in mere thickness tabulations, as the excellent quality of British Cemented armour provided the resistance of about 25% greater thickness of US Class "A" armour.」
- 对照德方（kbismarck.com）：「KC n/A (Krupp Cemented)… Face-hardened armour steel… used for the side belt, turrets, barbettes, and conning towers.」「Wh n/A (Wotan hart)… Homogeneous armour steel… used for the armoured decks」；并注「Post WWII proving ground test indicated that KC was only slightly less resistant than British cemented armour (CA), and markedly superior to US Class A plates.」

---

## 7. 武备

### 主炮：14 in/45 BL Mk VII（2 座四联 + 1 座双联）

**为什么用四联装（伦敦条约限制）**

- 条约上限：Second London Naval Treaty（1936 年 3 月签署）把主力舰主炮上限定为 14 英寸 —— wiki 舰级页：「The Second London Naval Treaty, a result of the Second London Naval Conference begun in December 1935, was signed in March 1936 by the United States, France and Britain and this set a main battery of 14-inch (356 mm) naval guns as the limit.」
- 条约还有 opt-out 条款，但英国不愿用 —— wiki 舰级页：「Stephen Roskill noted that the London Naval Treaty stipulated a 14-inch maximum gun size, with an opt out clause, which Britain was very reluctant to exercise, since the Admiralty was hoping to persuade the other naval powers to stick to 14-inch guns, though there was little or no debate within Parliament.」
- 换 15 英寸的代价 —— wiki 舰级页：「The Admiralty controller wrote that a change to 15-inch guns would entail an 18-month delay (which would have meant no new RN battleships until 1942).」
- 16 英寸 escalator 条款（可用但同样延工期）—— wiki 舰级页：「The last naval treaty had an escalator clause that permitted a change to 16-inch guns if another signatory did not conform to it by 1 January 1937. Although they could have invoked this clause, the effect would have been to delay construction...」
- **因此四联装是「在 35,000 t 与 14 英寸双重限制下凑出 12 门炮」的唯一办法** —— wiki 舰级页：「The class was designed to carry twelve 14-inch guns in three quadruple turrets… It proved impossible to include this amount of firepower and the desired level of protection on a 35,000 ton displacement and the weight of the superimposed quadruple turret made the stability of the vessel questionable.」
- 结果：**十二门削成十门**，B 炮塔降为双联 —— 同上：「The second forward turret was changed to a smaller two-gun turret in exchange for better armour protection, reducing the broadside weight to below that of the nine gun arrangement.」
- 另一层理由（原设计对比）：「had a heavier broadside than the nine 15-inch guns」——即**十门 14 英寸的舷侧投射量仍优于九门 15 英寸**，这是四联装方案得以保留的根本算术。
- 丘吉尔 1936 年曾反对 —— wiki 单舰页：「Churchill argued in 1936 for nine 16-inch guns instead of ten 14-inch.」（该页仅记其主张，未记表决结果）
- **设计时明知有风险仍采用**：wiki 舰级页的故障根因段（见 §专题一）明写「Wartime haste in building, insufficient clearance between the rotating and fixed structure of the turret, insufficient full calibre firing exercises and extensive arrangements to prevent flash from reaching the magazines made it mechanically complex」——即四联装的机械复杂度是**设计阶段即已知**的代价，换取的是火力密度与吨位合规。

**炮塔布置 A / B / Y**

- 前二后一：A（四联，前）、B（双联，背负于 A 之上）、Y（四联，后）
- navweaps：「1x MkII twin gun turret (forward) – 2x MkIII quadruple gun turrets (1 forward, 1 aft)」https://www.navweaps.com/Weapons/WNBR_14-45_mk7.php
- wiki 单舰页：「mounted in one Mark II twin turret forward and two Mark III quadruple turrets, one forward and one aft.」
- **注意：本舰后炮塔是「Y」而非「X」** —— navweaps 的训练角条目写「"A" Turret: - 143 / +143 degrees」「"B" and "X" Turrets: - 135 / +135 degrees」，此处 navweaps 用「X」指代后炮塔（英舰惯例差异）；Patterson 战报与 wiki 均用「Y」。**本文统一用 Y，并注明 navweaps 原文作 X。**

**座重（mounting weight）**

- 四联 Mk III：1,582 t（1,557 mt）—— navweaps「Mark III: 1,582 tons (1,557 mt)」；wiki 单舰页「The quadruple turrets weighed 1,582 tons」
- 双联 Mk II：915 t（900.5 mt）—— navweaps「Mark II: 915 tons (900.5 mt)」；wiki 单舰页「the twin turret 915 tons」
- 无分歧。

**俯仰 / 旋回**

- 俯仰 -3° / +40° —— navweaps「Elevation -3 / +40 degrees」；RMG「Max elevation 40 degrees」
- 俯仰速率 8°/s —— navweaps「Rate of Elevation 8 degrees per second」；RMG「Max rate of gun elevation 8 deg/s」
- 旋回速率 2°/s —— navweaps「Rate of Train 2 degrees per second」；RMG「Max rate of gun training 2 deg/s」
- 训练角：A ±143°，B/Y ±135° —— navweaps（见上）
- 装填角 +5° —— navweaps「Loading Angle +5 degrees」
- 后座行程 45 in（114 cm）—— navweaps「Gun Recoil 45 in (114 cm)」
- **无 RPC（远程动力控制）** —— navweaps：「The British battleships lacked RPC almost entirely until late in the war.」（见 §8）；navweaps 14 in 页另记「RPC …」（原文被截断），另有 Buxton 称 1945 年 KGV 装过 RP 40，**未获取原始出处，标为存疑。**
- 对照 wiki 单舰页：「Training and elevating was achieved through a hydraulic drive, with rates of two and eight degrees per second, respectively.」

**射速**

- 2 发/分/门 —— navweaps「Rate Of Fire 2 rounds per minute」；RMG「Rof 2 rpg/min」；maritimequest「Rate of fire 2 RPM」
- 齐射间隔 30 s —— wiki 单舰页：「a salvo could be fired every 30 seconds.」
- 全齐射重量 15,950 lb（=1,595 lb × 10）—— wiki 单舰页：「A full gun broadside weighed 15,950 pounds」

**弹重与初速（关键：MK VII 是「轻弹」）**

- 弹重 1,590 lb / 721.2 kg（APC Mark VIIb）—— navweaps「APC Mark VIIb: 1,590.0 lbs (721.2 kg)」；RMG「Weight of shell 1590lb」；wiki 单舰页「1,590 lb AP」
- **这是本炮最受争议的一点：同为 14 英寸，英国弹比美、日同类轻得多**，换来的是更高的初速与更大的药室容比。navweaps 原话：「and had a longer barrel life than the larger 16"/45 (40.6 cm) Mark I.」（指该弹与炮的组合优点）
- 初速（新炮）2,483 fps / 757 mps —— navweaps「2,483 fps (757 mps)」
- 初速（平均，炮队平均状态）2,400 fps / 732 mps —— navweaps「2,400 fps (732 mps)」
- 初速 2,475 ft/sec —— RMG「Muzzle velocity 2475 ft/sec」；navweaps 注「The mounting handbook says that new gun MV was 2,475 fps (754 mps) nominal」
- **分歧**：2,483（navweaps 表列）vs 2,475（navweaps 注 + RMG）。差 8 fps，疑为**名义值 vs 实测平均**。**不裁决。**
- 发射药：338 lb 四包 —— RMG「Weight of charge 338lb」；navweaps 注「The propellant charge was in four bags.」
- 炮口动能 67,520 ft-tons —— RMG「Muzzle energy 67,520 ft/tons」
- 弹的爆破装药 39.8 lb（18.1 kg）—— wiki 舰级页：「The 14-inch Armour Piercing (AP) shell also carried a proportionally large bursting charge of 39.8 lb (18.1 kg).」——**这是轻弹的补偿：弹轻但装药大。**

**最大射程**

- 36,500 yds（33,380 m）@ 40.7° —— navweaps「36,500 yds (33,380 m)」
- 36,300 yards @ 40° —— RMG「Maximum range 36,300 yards」
- 38,560 yards @ 40°（21.9 miles）—— maritimequest「38,560 yards @ 40° (21.9 miles)」
- navypedia（换成电缆）：「had 190 cables firing range at the 40° maximum elevation angle」（190 cables = 19,000 yd？此处 navypedia 用 cable 计，与英美 yds 口径不同，**照抄不换算**）
- **分歧**：36,300 / 36,500 / 38,560 yds。前两者差 200 yd（1%），疑为**名义弹 vs 实际弹道**；maritimequest 的 38,560 明显更高，疑为**含超装药或换算错误**。**三者并列不裁决。**

**弹药基数**

- 全舰 1,100 发：A 432、B 216、Y 452 —— navweaps 弹库分配（「1,100 rounds total, A 432 / B 216 / Y 452」，本报告据 navweaps 原文转述）
- 每门 80 发（最大 100）—— RMG「Shell stowage: 80 rounds per gun (100 max)」；navweaps「每门 100 发」为最大档
- 无实质分歧（80 为定额，100 为满载）。

**炮管寿命（关键分歧）**

- **340 发** —— navweaps「Approximate Barrel Life: 340 rounds」
- **375 发** —— RMG「Barrel life 375 rounds」
- **分歧 35 发（约 10%）**。navweaps 的 340 疑为**以全装药计的名义寿命**，RMG 的 375 疑为**含减装药训练弹的加权寿命**。两者均未给计算方法，**不裁决**。
- 对照：5.25 英寸副炮 750 发（两源一致）；15 英寸 Mk I 为 335 发（navweaps）。

**炮身与制造**

- 身管长 651 in（oa）—— navweaps「Gun Length oa 651 in」
- 药室→炮口 52 ft 6 in，全长 54 ft 2.8 in —— RMG
- 炮重（裸）早期 79.588 t / 后期 78.988 t —— navweaps；RMG 给「77 tons 14 cwt 84 lb」（裸）/「89 tons 2cwt 84lb」（含配重）
- 膛线：72 条右旋，1 转 / 30 倍径 —— RMG「polygroove, 72 grooves plain section uniform right-hand twist of one turn in 30 calibres」
- 制造：78 门，RGF 24 / Vickers-Armstrong Elswick 39 / Beardmore 15 —— navweaps
- 炮塔设计方：Vickers Armstrong Elswick Works，各类设备由 Vickers Armstrongs Barrow 制造 —— wiki 单舰页：「The turrets were designed by the Vickers Armstrong's Elswick Works, but sets of each type of equipment were manufactured by Vickers Armstrongs in Barrow.」

**四联装的机械复杂度（设计层面的代价）**

- 「over 3,000 working parts」—— navweaps 引《The Big Gun》：「"The Big Gun" states that the quadruple mounting had over 3,000 working parts.」
- 「These mountings had very elaborate flash precautions, perhaps overly so given the problems encountered during World War II.」—— navweaps 编者注
- 供弹路径（navweaps 全段，见 §专题一引用）

### 副炮：5.25 in/50 QF Mk I 双联（8 座 / 16 门）

**数量与座数**

- 8 座双联，16 门 —— navypedia「8 x 2 - 133/50 QF Mk I」；RMG「Mounting: 8 x twin HA/LA Mk 1」；wiki 单舰页「16 × 5.25 in/50 QF Mk I guns」
- **RMG 该行首写「6 x 5.25in, 50 cal. Mk1」，与同段「8 x twin」自相矛盾，属 RMG 页面笔误**，以 16 门为准（其余全部来源一致）。
- 座重 Mark I：77.5 t（78.7 mt）—— navweaps「Mark I: 77.5 tons (78.7 mt)」

**射速**

- 实测 7–8 发/分 —— navweaps「All except Vanguard: 7 - 8 rounds per minute」；RMG「10 to 12 rounds per gun per minute (nominal) [actual rate closer to 7–8 rounds as gunners could not load any faster]」；maritimequest「Rate of fire 7-8 RPM」
- 设计值 10–12 发/分，达不到 —— navweaps 引《British Battleships of World War Two》：「The mounting was designed for a rate of fire of ten to twelve rounds per minute, but, in fact, the crews could not transfer shell and cordite from the hoists to the loading-trays at this speed, and the more usual rate of fire was seven to eight rounds per minute.」
- 原因（navweaps 编者）：「the heavy weight of the projectile and cartridge case plus the semi-automated fuze setting mechanism meant that this round required much crew handling before it could be rammed into the breach. The tight design of the gunhouse also interfered with the smooth crew operation necessary to achieve high rates of fire.」
- **实战验证（Patterson 战报）**：「5.25-in. … fired 77 rounds a gun without a hitch」——即 1941-05-27 副炮全程无故障，与主炮形成反差。

**射程 / 仰角**

- 仰角 -5° / +70° —— navweaps「Elevation -5 / +70 degrees」；RMG 写「elev 80°」（**RMG 说 80°，navweaps 说 70°，分歧**；navypedia 亦写「70° elevation angle」）
- 水面射程 23,400 yds（21,397 m）@ 45° —— navweaps；RMG；maritimequest 三源一致
- 对空升限：46,500 ft（14,170 m）@ 70° —— navweaps「AA Ceiling @ 70 degrees: 46,500 feet (14,170 m)」
- 对空升限 29,544 ft @ 80° —— RMG（**与 navweaps 差 17,000 ft，量级差**；RMG 用 80° 仰角，navweaps 用 70°，但仰角差无法解释如此大的差）
- 对空升限 49,000 ft —— maritimequest「AA ceiling 49,000'」
- **三说并列**：46,500 ft / 49,000 ft / 29,544 ft。navweaps 自己加了注：「There are disagreements in the sources below as to the maximum range and AA ceiling of these guns. I have chosen to use those figures given in "Naval Weapons of World War Two."」——**即 navweaps 也承认此数无定论。不做裁决。**
- 俯仰 / 旋回速率：均 10°/s —— navweaps「Mark I and Mark II: 10 degrees per second」；Anson 后期的 RP10 提到 20°/s（wiki 舰级页）

**对空性能与实际评价（关键查证点）**

- navweaps 直接评价：「Unfortunately, the design of the gunhouse was cramped and the heavy projectile and cartridge cases resulted in a lower rate of fire than expected. In addition, the slow elevating and training speeds of the mounts were found to be inadequate for engaging modern high-speed aircraft.」
- 后续改进：「The later mountings designed for HMS Vanguard enjoyed a much improved RPC system and were coupled with the USN's outstanding...」（指向 Mk 37 GFCS）
- 设计选择（navweaps）：「that this size would provide the maximum weight of shell that could still be manually handled by the average gun crew.」——**即「人工装填的上限口径」决定了 5.25 英寸，这是它射速与随动性能不足的根源。**
- 结论：**这种炮作为两用炮在纸面上合理（80 lb 弹、70° 仰角、46,500 ft 升限），但实战中因炮室狭窄、随动慢、人工装填而难以对付高速机；它是本级公认的薄弱环节之一。**

**弹药**

- 弹重 80 lb（36.3 kg）SAP/HE —— navweaps；RMG「shell 80lb」；maritimequest「80 lb. HE shell」
- 初速 2,672 fps（814 mps）—— navweaps；RMG 给 2,600 ft/sec（**分歧 72 fps，疑为名义 vs 实测**）
- 发射药 18.05 lb SC 或 21.0 lb NF/S —— navweaps；RMG 给 18.6 lb
- 身管寿命 750 发 —— navweaps「Approximate Barrel Life 750 rounds」；RMG 同
- 每门 400 发 —— navweaps「King George V and Lion: 400 rounds」；RMG「Shell stowage 400 rounds per gun」
- 工作压力 20.5 tons/in² —— navweaps
- 全级共造 267 门 —— navweaps

### 高炮：2-pdr 八联 pom-pom（Mk VI）

**1940 年服役时：4 座八联（32 门）**

- navypedia「4 x 8 - 40/39 2pdr QF Mk VIII」；RMG「4 x 8-barrelled MkVI 2pdr pom-poms」；maritimequest「32 / 4 octuple mounts」；tynebuiltships「4 x 8 x 2pdr QF guns」

**逐年变化（RMG 全表）**

- 1941-12：5 座八联 + 1 座四联 Mk VII + 18 门单装 20 mm
- 1943 年中：5 座八联 + 1 座四联 + 38 门 20 mm
- 1944-07：8 座八联 + 26 门单装 20 mm + 6 门双联 20 mm + 2 座四联 40 mm Bofors
- 1945-09：8 座八联 + 24 门单装 20 mm + 6 门双联 20 mm + 2 座四联美制 40 mm + 2 门单装英制 40 mm
- tynebuiltships 1945 年口径：「64 x 2pdr, 10 x 40mm, 36 x 20mm guns」
- naval-history.net 1942-04-03：「to have two additional eight barrelled Pom-Poms fitted atop B and Y turrets」
- naval-history.net 1944-02~06 改装：「the removal of 1 x 4 barrelled 2pdr pom-pom and 12 x single barrelled 20mm Oerkilons; and augmented by the addition of 3 x 8 barrelled 2pdr pom-poms, 6 x 2 barrelled 20mm Oerkilons and 2 x 4 barrelled 40mm Bofors」

**性能**

- 弹重 1.81 lb（1.8 lb）—— RMG；wiki 舰级页「1.8-pound shells」
- 初速 2,300 ft/sec —— RMG；wiki 舰级页同
- 射速：96–98 发/分（控制射击）/ 115 发/分（自动射击）—— wiki 舰级页；RMG 给 115 rpm；maritimequest 给 115 RPM
- 射程 5,000 yds —— RMG；wiki 舰级页给 Mk VI* 为 6,800 yds（**型号不同，非分歧**）
- 升限 13,300 ft —— maritimequest；RMG 未给
- 座重 16 t（八联 Mk VI）—— wiki 舰级页：「The Mark VI octuple mount weighed 16 tons... elevated to 80 degrees and depressed to 10 degrees at a rate of 25 degrees per second... 1,800 rounds per barrel」
- 射控：KGV 是**世界上第一艘装陀螺测速高炮指挥仪的军舰** —— wiki 舰级页：「King George V introduced the Mk IV Pom-pom director to the Royal Navy in 1940, becoming the first ship in the world to feature gyroscopic target tracking in tachymetric anti-aircraft directors.」

### 高炮：40 mm Bofors（战时加装）

- **1944-07 起：2 座四联美制 Mk II（8 门）** —— RMG「2 x 4-barrelled American MkII 40mm Bofors」；wiki 舰级页；naval-history.net（1944 改装）；navypedia（7/1944）
- **1945-09：另有 2 门单装英制 40 mm** —— RMG「2 x single RN pattern 40mm Bofors」；wiki 舰级页「2 × single 40 mm Bofors」
- 性能：弹重 1.98 lb，初速 2,890 ft/sec，有效射程 2,500 yds，升限 18,000 ft，射速 120 发/分 —— RMG
- 1945 年总数 10 门（2×4 + 2×1）—— tynebuiltships「10 x 40mm」

### 高炮：20 mm Oerlikon（战时加装）

- 1941-12：18 门单装 Mk IIIA —— RMG；navypedia（late 1941「18 x 1 - 20/70 Oerlikon Mk II/IV」）
- 1943-05：+20 门（累计 38 门）—— RMG「Mid-1943: 5 x 8br + 1 x 4br + 38 x 20mm」；navypedia「5/1943: + 20 x 1 - 20/70」
- 1944-07：26 门单装 + 6 门双联 —— RMG；navypedia（7/1944 记 −12 单装 +6 双联）
- 1945-09：24 门单装 + 6 门双联（合计 36 门）—— RMG；tynebuiltships「36 x 20mm」
- 性能：弹重 0.27 lb，初速 2,770 ft/sec，射程 4,800 yds，仰角 90°，射速 450 发/分 —— RMG

### UP 火箭（Unrotated Projectile，1940–1941）

- 1940 年装 4 座二十管 —— navypedia「4 x 20 - 178 UP rockets projectors」；RMG「4 x unrifled projector (UP) rocket-launchers」；wiki 舰级页「1940 加 4 座 UP（B 炮塔 1、Y 炮塔 2、舰尾 1）」
- 1941 年末拆除 —— navypedia「late 1941, King George V: - 4 x 20 - 178 UP」；wiki 单舰页（1941 拆 UP）
- 该武器实战无效，是英国战时应急产物，本级是最早装备的舰之一。

### 鱼雷（需确认「无」）

- **装备表中无鱼雷发射管**：
  - navypedia KGV 装备行：「2 x 4 - 356/45 BL Mk VII, 1 x 2 - 356/45 BL Mk VII, 8 x 2 - 133/50 QF Mk I, 4 x 8 - 40/39 2pdr QF Mk VIII, 4 x 20 - 178 UP rockets projectors, 1 catapult D-III-H, 2 seaplanes」——**无 TT（torpedo tube）一项**
  - wiki 舰级页 infobox armament 全列，无鱼雷
  - wiki 单舰页 infobox armament 全列，无鱼雷
  - RMG 详细统计表（主炮、副炮、近程高炮、弹道共 5 节）无鱼雷节
- **结论**：**本舰未装鱼雷发射管。** 但须诚实说明口径——各来源是「装备表缺项」，**未见任何来源明文写「本舰无鱼雷」**，故此为**据装备表推定**，而非直接引证。
- 旁证（final battle）：Tovey 战后信号「Any ship with torpedoes to close the BISMARCK and torpedo her」——若 KGV 有鱼雷，此令不必泛指「any ship」；最终是 DORSETSHIRE 用鱼雷（naval-history.net：「DORSETSHIRE 2600 码两条鱼雷均中、另一侧 2000 码再中一条」）。这是间接但有力的旁证。

### 0.5 英寸机枪（设计案，未装）

- 设计原案为 4 座四联 0.5 in —— maritimequest「16 / .5"/62 (12.7mm) / 4 quad mounts」；tynebuiltships「4 x 4 x 0.5ins guns」
- 实际 1939 年即以 2 座 Mk VI pom-pom 取代 —— wiki 舰级页：「设计 4 座四联 0.5 in 机枪，1939 换 2 座 Mk VI pom-pom」
- **即：KGV 建成时并无 0.5 英寸机枪**，maritimequest 与 tynebuiltships 抄的是设计案。

---
