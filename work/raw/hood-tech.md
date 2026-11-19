# HMS Hood（胡德号，舷号 51）— 技术数据与生涯时间线

> 检索日期：2026-11-18。**硬规则执行说明**：本文每个数值后附来源缩写与英文原句；凡无原句支撑者一律标「未获取」。
> 分歧全部并列，不做裁决，仅标注「疑为 X 口径」。
> 来源优先级：HMS Hood Association（hmshood.org.uk）> navweaps > kbismarck > navypedia > 其他。

---

## 0. YAML 片段（便于直接落库）

```yaml
ship:
  name: HMS Hood
  name_origin: "First Viscount Samuel Hood（官方命名对象；非 Robin Hood，亦非 Sir Horace Hood）"
  class: "Admiral class battlecruiser（海军上将级战列巡洋舰）"
  class_planned: 4
  class_completed: 1
  builder: "John Brown & Company Ltd, Clydebank, Scotland"
  build_number: "460"
  slip: "Number 3 slip"
  pendant_number: "51"
  callsign: "GECV"
  nickname_public: "The Mighty Hood"
  nickname_crew: ["The Seven Bs", "H.M.S. Wobbly", "Largest Submarine in the Fleet"]
  fleet:
    - "Battle Cruiser Squadron, Atlantic Fleet (1920)"
    - "Battle Cruiser Squadron, Home Fleet (1939-)"
    - "Force H (1940)"
  ordered: "1916-04-21"
  laid_down: "1916-09-01"
  launched: "1918-08-22 13:05"
  launched_by: "Lady Hood（Sir Horace Hood 遗孀）"
  commissioned: "1920-03-29"
  completed: "1920-03-05"
  cost: "£6,025,000"
  fate: "1941-05-24 sunk by Bismarck in Denmark Strait"

dimensions:
  length_oa: "262.3 m / 860 ft 7 in"
  length_wl: "259.2 m / 850 ft 5 in"
  length_pp: "247 m / 810 ft 6 in"
  beam_extreme: "32 m / 105 ft 2.5 in"
  beam_bulge: "31.7 m / 104 ft 2 in"
  beam_moulded: "31.7 m / 103 ft 11.5 in"
  beam_wl: "≈28.9 m / ≈95 ft"
  draught_light_1920: "8.6 m / 28 ft 3 in"
  draught_deep_1920: "9.7 m / 31 ft 11 in"
  draught_deep_1939: "10.1 m / 33 ft 4 in"
  depth_amidships: "15.4 m / 50.5 ft（龙骨底到舷侧甲板面）"
  block_coefficient: "未获取"
  waterplane_area: "未获取"
  watertight_sections: "未获取"

displacement:
  1920: {light: "41,125 t / 41,785 MT", deep: "46,680 t / 47,429.8 MT"}
  1931: {light: "42,037 t / 42,712 MT", deep: "48,000 t / 48,777.1 MT"}
  1939: {light: "42,752 t / 43,438.7 MT", deep: "48,650 t / 49,431.5 MT"}
  1940: {light: "42,462 t / 43,144 MT", deep: "48,360 t / 49,136.8 MT"}
  normal_navypedia: "42,670 t"
  full_navypedia: "46,680 t"
  standard_full_actual: "未获取（图上只有 Light / Deep 两列）"

machinery:
  boilers: "24 × Yarrow small tube 3-drum"
  boiler_pressure: "235 psi"
  boiler_heating_surface: "7,290 ft²/台"
  steam_temperature: "未获取"
  turbines: "4 sets Brown-Curtis geared steam turbines（单级减速 + 巡航涡轮）"
  shafts: 4
  screws: "4 × 三叶锰青铜，直径 15 ft / 4.57 m，每只 20 t"
  shaft_diameter: "28.5 in / 72.4 cm"
  power_designed: "144,000 shp"
  power_trials: "151,000 shp"
  speed_designed: "32 kn"
  speed_trials: "32.07 kn（Arran 1 英里测速段，42,000 t，6 级风）"
  speed_1941: "约 28.8 kn"
  endurance: "4,500 nm @20 kn；5,000 nm @18 kn"
  endurance_navypedia: "7,500 nm @14 kn"
  fuel_oil: "常规约 1,200 t；最大 4,000 t（hoodspecs3）/ 4,600 t（1930s 手册）/ 3,895 t（navypedia）/ 4,615 t（1931 改装后，navypedia）"
  generators: "8 台发电机（2 柴油、2 高速冲动汽轮机、4 往复式），AC/DC 均可；总功率未获取"
  motors: "约 360 台电动机；总功率未获取"

armour:
  main_belt: "305 mm（12 in），向舰首减至 152/127 mm，向舰尾减至 152 mm"
  main_belt_size: "长 562 ft / 171.3 m，高 9 ft 6 in / 2.9 m（navypedia：深 2.89 m）"
  medium_belt: "178 mm（7 in），深 2.75 m（navypedia）"
  upper_belt: "127 mm（5 in，navypedia）；hmshood 页未单列此层"
  inclination: "12° to the vertical（navypedia）"
  deck: "主甲板 76 mm（弹库上方）/ 51-38 mm（机舱上方）+ 51 mm 斜面；中甲板 25→76 mm；上甲板 19 mm；艏楼甲板 51-32 mm"
  turret: "正面 381 mm，侧面 305-279 mm，后部 279 mm，顶部 127 mm（navypedia）"
  barbette: "305 mm（主甲板以上）→ 152-127 mm（以下）"
  conning_tower: "280-76 mm（navypedia）/ 9-11 in 垂直 + 2 in 甲板（hmshood）"
  torpedo_bulkhead: "38 mm"
  underwater_depth: "3.1 m"
  armour_weight: "13,800 t（1930s 手册宣传口径）"
  armour_ratio: "未获取原话；按 13,800/44,600 计算约 30.9%（本报告换算，非来源原句）"
  steel_type: "未获取"

armament:
  main: "8 × 15 in/42 (38.1 cm) BL Mk I，4 座双联 Mk II 炮塔（A/B/X/Y）"
  secondary_5_5: "12 × 5.5 in/50 (14 cm) BL Mk I，单装 CPII，射速 12 rpm，1940-05 全部拆除"
  aa_4in_twin: "7 × 双联 4 in/45 QF Mk XVI（Mk XIX 座），14 门"
  aa_4in_single: "4-8 × 单管 4 in Mk V（1939 改装时拆除）"
  pompom: "3 × 八联 2-pdr Mk VIII（Sammy/Peter/Auntie）"
  mg_half_inch: "4 × 四联 0.5 in Vickers Mk III"
  up_rockets: "5 × UP Mk I 二十管发射器（1940 年加装）"
  torpedoes: "4 × 21 in 水上发射管（2 舷各 2）；2 具水下管 1937 年拆除"
  torpedo_type: "Mk IV / Mk IV*，533.4 mm，TNT 233.6 kg，40 kn @5,000 yd / 25 kn @13,500 yd"

fire_control:
  table: "Dreyer Table Mk V（全舰队唯一）"
  afct: "未装（Admiralty Fire Control Table 非本舰装备）"
  directors: "15-inch tripod-type director：每座 15-inch Director Tower 一座（旋转指挥仪罩，位于 Spotting Top 上方）"
  rangefinders: "30 ft：每炮塔一座 + Director Tower 一座；15 ft：Spotting Top 上方一座（1941 装 284 时拆除）；30 ft：Conning Tower 顶部一座"
  radar_284: "1941-01-16～03-15 Rosyth 改装中安装，主炮测距，10 nm"
  radar_279m: "同期安装，对空预警，7.5 m 波长"
  radar_282_285: "未装（C.A.F.O. 509 曾计划 3 部 282 + 3 部 285，确认 282 指挥仪未装）"

aviation:
  aircraft: "1-2 × Fairey Flycatcher（至 1933）；1 × Fairey IIIF（1929-1933）；Sopwith 1½ Strutter 亦曾登舰"
  catapult: "F-IV-H（navypedia），1929-1931 改装装于 Y 炮塔后方甲板，1932 年中拆除"
  platforms: "B、X 炮塔上装飞行甲板（hmshood other.htm）；1920 年记录为 A、B 炮塔（timeline2）——分歧"
  crane: "同期装于 Y 炮塔后方"

complement:
  peacetime: "约 1,200"
  wartime: "1,400+"
  war_complement_1940_06: "1,237（ADM 136/13）"
  final_1941_05_24: "1,418（RN 89 军官 + 约 1,157 士兵；RM 约 4 军官 + 约 161 兵；NAAFI 约 7 文职）"
  lost: "1,415（Association 核证值）"
  survivors: 3

camouflage:
  1920_1936: "Home Fleet dark grey（1920s 中期起略带蓝）"
  1936_1939: "Pattern 507C light grey（地中海舰队/海外站）"
  1939_1941: "Home Fleet grey；1941 年初短暂双色调试验"
  as_sunk: "AP507B / 507A Home Fleet Grey 单色；最后一次记录涂装 1941-05-12"
```

---

## 1. 身份

### 舰名来源
- 官方命名对象为 **First Viscount Samuel Hood** —— FAQ「records show that the ship was **officially named after First Viscount Samuel Hood**. In fact, _Hood_ and her sisters (none of which were completed) were all named for Admirals of First Viscount Hood's era (Rodney, Howe, etc.).」
  - 同段否证常见说法：「It has also been claimed that she was named specifically for Sir Horace Hood who died at Jutland. This is not entirely true.」「Contrary to some claims, she was also not named after Sir Arthur Hood of Avalon.」
  - 来源：https://www.hmshood.org.uk/admin/faq.htm

### 舰级
- 「The Admiralty Board placed orders for three Admiral-class battlecruisers: _Hood_ (John Brown), _Howe_ (Cammell Laird), _Rodney_ (Fairfield).」——https://www.hmshood.org.uk/history/timeline1.htm
- 第四艘：「July: … an order was placed a for a fourth Admiral-class battlecruiser, _Anson_ (Armstrong Whitworth).」——同上
- 只建成 1 艘：「**October 1918:** The Admiralty cancels the other three Admiral-class battlecruisers.」——同上
- 官方分类：「H.M.S. _Hood_ was **officially classed by the Royal Navy as a battle cruiser**. In reality, she was arguably closer to what would later be termed a **fast battleship**.」——https://www.hmshood.org.uk/admin/faq.htm
- 同级四舰建造厂与船台号（navypedia）：「Rodney | 527 | Fairfield, Govan」「Howe | 834 | Cammell Laird, Birkenhead」「Anson | 909 | Armstrong, Elswick」——https://www.navypedia.org/ships/uk/brit_bb1_hood.htm

### 建造代号 / 船台号
- 「**Hull number (for construction):** 460」——https://www.hmshood.org.uk/ship/hoodspecs7.htm
- 「**Pendant number:** 51」「**Callsign:** GECV」——同上
- 「Built on **Number 3 slip** at John Brown & Company, Lt. Clydebank」——同上
- 交叉：navypedia Ships 表第二列 51、第三列 460——https://www.navypedia.org/ships/uk/brit_bb1_hood.htm

### 所属舰队 / 分队
- 「**18 May 1920:** Rear Admiral Sir Roger Keyes took command of the Battle Cruiser Squadron. _Hood_ became the Flagship, Battle Cruiser Squadron, Atlantic Fleet.」——https://www.hmshood.org.uk/history/timeline2.htm
- 「1939-06-02 recommissioned as Flagship BCS Home Fleet」——https://www.hmshood.org.uk/history/timeline3.htm
- 1940 年米尔斯克比尔：「**02–04 July:** Force H … undertakes Operation CATAPULT」——https://www.hmshood.org.uk/history/timeline4.htm
- 1941 年：「Vice Admiral Lancelot E. Holland, new commander of the Battle Cruiser Squadron and Second in Command of the Home Fleet, set up command in _Hood_」——同上

### 绰号
- 「Public Nickname: The "Mighty Hood"」——https://www.hmshood.org.uk/ship/hoodspecs7.htm
- 舰员内部绰号（同页）：「'The Seven Bs' ('Britain's Biggest Bullsh*ttingest B*stard Built By Brown')」「'H.M.S. Wobbly'」「'Largest Submarine in the Fleet'」

---

## 2. 建造

### 下单
- 「**21 April:** The Admiralty Board placed orders for three Admiral-class battlecruisers: _Hood_ (John Brown)…」——https://www.hmshood.org.uk/history/timeline1.htm（年份 1916）
- 「**14 July:** Admiralty informed John Brown that their ship is to be named _Hood._」——同上

### 铺龙骨（**关键分歧：1916-05-31 被权威专题站否定**）
- **1916-09-01（Association 认定的确认日期）**：「**01 September:** Confirmed date _Hood's_ keel was laid at John Brown & Company Ltd., shipyards in Clydebank, Scotland. She was ship number 460.」——https://www.hmshood.org.uk/history/timeline1.htm
- 同页对 5 月 31 日的否证：「**31 May:** Rumoured date that _Hood's_ keel was first laid… this date is NOT supported by the construction yard records… This 31 May date is therefore **not confirmed and most unlikely**.」——同上
- navypedia 两存：「Hood | 51 | 460 | John Brown, Clydebank | **31.5.1916, again 1.9.1916** | 22.8.1918 | 15.5.1920」——https://www.navypedia.org/ships/uk/brit_bb1_hood.htm
- navypedia 解释「again」：「_Hood_ was laid down 31.5.1916, however the Jutland battle which has taken place **that day**, forced to reconsider the design completely… _Hood_ was re-laid in September, 1916」——同上
- **分歧记录**：任务给的「1916-05-31 铺龙骨（日德兰海战后 4 小时）」在 Association 处被判为「rumoured / not confirmed / most unlikely」；navypedia 保留 5-31 为首次铺设并记 9-1 为「re-laid」。两说并列，不裁决。
- 补充：navypedia 记设计最终批准「only **30.8.1917**」——同上

### 下水
- 日期时间：「**22 August:** _Hood_ was launched at **1305 hours** by Lady Hood (widow of Sir Horace Hood lost at Jutland).」——https://www.hmshood.org.uk/history/timeline1.htm
- 掷瓶人：「Lady Hood, wife of Sir Horace Hood lost at Jutland, launched the battle cruiser _Hood_ at John Brown and Company, Clydebank, Scotland, on 22 August 1918.」——https://www.hmshood.org.uk/history/construct/launch.htm

### 服役（**关键分歧：1920-05-15 vs 1920-03-29**）
- Association 口径 **1920-03-29**：「**29 March:** _Hood_ was commissioned by Captain Tomkinson and **967 crew** (the majority of which came from _H.M.S. Lion_) on 29 March. This is the first day for which Hood maintained a ship's log.」——https://www.hmshood.org.uk/history/timeline2.htm
- 同页明确否证 5-15：「NB. Over the years an urban myth has grown up that Hood was Commissioned into the Royal Navy on this day… neither ADM53/78910 (ship's log) nor the list of Commissions, Dockings etc. in the Ship's Book (ADM136/13) make any reference to 15th of May as a date when Hood was commissioned. The Association therefore retains **29th March** as the date of first commission」——同上
- navypedia 口径 **15.5.1920**：「Hood | 51 | 460 | … | 15.5.1920 | sunk 24.5.1941」——https://www.navypedia.org/ships/uk/brit_bb1_hood.htm
- 1930s 观光手册："完工"口径：「**Begun on 1st September, 1916, she was not completed until 5th March, 1920.**」——https://www.hmshood.org.uk/ship/pamphlet30s.htm
- **分歧记录**：三套日期（03-29 服役 / 05-15「完工交付」/ 03-05「建成」）并存。疑为「commission（服役）」与「completion（建成交付）」两个口径混用。

### 造价
- 「Original construction cost was **£6,025,000** (of which John Brown & Company, Ltd, reportedly made £214,108.00)」——https://www.hmshood.org.uk/ship/hoodspecs7.htm
- **币值年份：未获取**（该页未标注）。对照：Bismarck 造价页明确标 1938 年币值，Hood 页无对应标注。

### 建造插曲
- 「**19 May 1919:** Explosion in watertight compartment… killed two dockyard workers」——https://www.hmshood.org.uk/history/timeline1.htm
- 死者与调查结论（construction 页）：「John Morton（engineer, 25 岁）」「James McGregor（32 岁）」；Dumbarton Sheriff Court「could find no obvious cause… most probably caused by a build up of gas」——https://www.hmshood.org.uk/history/construct/construction.htm
- 「**09-10 December 1919:** Basin trials.」——https://www.hmshood.org.uk/history/timeline1.htm
- 「**09 January 1920:** _Hood_ departs Clydebank under her own power… working up to over 130,000-horse power」——https://www.hmshood.org.uk/history/construct/construction.htm

---

## 3. 主尺度

> 本站 hoodspecs1.htm 正文只有图片（dimensions.gif / displacement.gif 等），原图直连 403；以下数值取自该图的 Wayback 原始文件快照，图面文字为来源原文。

### 全长（oa）
- **262.3 m / 860 ft 7 in** —— https://www.hmshood.org.uk/ship/dimensions.gif（经 Wayback 快照）「Overall Length: 860' 7" / 262.3m」
- **262.1 m** —— https://www.navypedia.org/ships/uk/brit_bb1_hood.htm「Length 262.1 m」
- **860 ft** —— https://www.naval-history.net/OWShips-WW1-02-HMS_Hood.htm「860(oa), 810(pp)x104x28ft」
- **873 ft** —— https://www.hmshood.org.uk/ship/pamphlet30s.htm「She is 873 feet long」
- 分歧原因：873 ft 为 1930s 宣传手册的取整/含突出物口径；262.1 m 疑为换算取整差（860'7" = 262.31 m）。

### 水线长（wl）
- **259.2 m / 850 ft 5 in** —— https://www.hmshood.org.uk/ship/dimensions.gif「At Waterline: 850' 5" / 259.2m」
- 其他来源未获取。

### 垂线间长（pp）
- **247 m / 810 ft 6 in** —— https://www.hmshood.org.uk/ship/dimensions.gif「Between Perpendiculars: 810' 6" / 247m」
- **810 ft** —— https://www.naval-history.net/OWShips-WW1-02-HMS_Hood.htm「810(pp)」
- 口径一致（810'6" ≈ 810'）。

### 最大宽
- **32 m / 105 ft 2.5 in** —— https://www.hmshood.org.uk/ship/dimensions.gif「Extreme (over rubbing pieces): 105' 2.5" / 32m」
- **31.7 m** —— https://www.navypedia.org/ships/uk/brit_bb1_hood.htm「Breadth 31.7 m」
- **105 ft** —— https://www.hmshood.org.uk/ship/pamphlet30s.htm「has a beam of 105 feet」
- 分歧原因：32 m 含舷外护舷木条（over rubbing pieces）；31.7 m 对应鱼雷防雷鼓包/模制宽。

### 水线宽 / 鼓包宽
- 鼓包：「Torpedo bulges: **104' 2" / 31.7m**」——dimensions.gif
- 模制宽：「Do. Moulded (frame): **103' 11.5" / 31.7m**」——同上
- 水线宽：「At Waterline: **@95ft / 28.9m**」——同上
- 舷侧甲板宽（主桅处）：「Shelter Deck (abreast main mast): **@95ft / 28.9m**」——同上

### 吃水
- 1920 空载：「**28ft 3in / 8.6m**」；满载深载：「**31ft 11in / 9.7m**」——https://www.hmshood.org.uk/ship/displacement.gif
- 1931：8.8 m（light）/ 10 m（deep）；1939：8.9 m / 10.1 m；1940：8.9 m / 10.1 m——同上
- **8.70 m** —— https://www.navypedia.org/ships/uk/brit_bb1_hood.htm「Draught 8.70 m」（未标口径，疑为标准排水量吃水）
- **32½ ft** —— https://www.hmshood.org.uk/ship/pamphlet30s.htm「draught 32½ feet」（宣传口径，≈9.9 m）
- Association 侧证：「sat nearly 4 feet deeper in the water than originally planned」——https://www.hmshood.org.uk/ship/hoodspecs4.htm

### 型深
- **15.4 m / 50.5 ft** —— https://www.hmshood.org.uk/ship/dimensions.gif「Foc'sle Deck Amidships (from bottom of keel to top of deck planks): 50.5ft / 15.4m」

### 方形系数
- **未获取**（hmshood 无此数据；navypedia 未列；Bismarck 侧有 0.55 作对照）

### 水线面积
- **未获取**

### 干舷
- 1920 light：「22ft / 6.7m (mid only)」；1920 deep：「25ft 6in / 7.7m; 18ft 4in / 5.5m; 15ft / 4.5m」（艏/舯/艉）
- 1931 light：「29ft 2in / 8.9m; 20ft 6in / 6.2m; 17ft 6in / 5.3m」；1931 deep：「23ft / 7m; 17ft 5in / 5.3m; 15ft 6in / 4.7m」
- 1939 light：「21ft / 6.4m (mid only)」；1939 deep：「22ft 10in / 6.9m; 17ft / 5.1m; 14ft 10in / 4.5m」
- 1940 light：「20ft 10in / 6.3m (mid only)」；1940 deep：「23ft 6in / 7.1m; 17ft 3in / 5.2m; 14ft 8in / 4.4m」
- 来源：https://www.hmshood.org.uk/ship/displacement.gif

### 上层建筑高度（1941 年，自水线量起）
- 「Compass Platform windows: **@75.5ft / 23m**」「Spotting Top windows: **@115ft / 35m**」「Main Mast Starfish: **@92ft / 28m**」「Upper Conning Tower: **@53ft / 16.1m**」「Shelter Deck: **@28ft / 8.5m**」——dimensions.gif
- 「Funnel Tops: **@49ft / 21.5m above Shelter Deck**」——同上

### 水密段数
- **未获取**（Association 与 navypedia 均未列；对照：Bismarck 22 段 / 17 段在 citadel 内）

---

## 4. 排水量

> 来源图 displacement.gif 的术语定义（照录）：「**Light**= no fuel, full ammunition, 50% of food & grease, full crew. **Standard**= no fuel, water or stores, but full crew & full ammunition. **Full**= full ammunition, provisions & crew plus normal fuel load. **Deep**= full ammunition, 6 months provisions, full crew & maximum fuel」
> **注意：图上实际只有 Light / Deep 两列，没有 Standard / Full 的数值行。**

### 1920 年（服役时）
- Light：**41,125 t / 41,785 MT**；Deep：**46,680 t / 47,429.8 MT** —— https://www.hmshood.org.uk/ship/displacement.gif

### 1931 年（大改装后）
- Light：**42,037 t / 42,712 MT**；Deep：**48,000 t / 48,777.1 MT** —— 同上

### 1939 年
- Light：**42,752 t / 43,438.7 MT**；Deep：**48,650 t / 49,431.5 MT** —— 同上

### 1940 年
- Light：**42,462 t / 43,144 MT**；Deep：**48,360 t / 49,136.8 MT** —— 同上

### 第三方口径
- navypedia：「Displacement normal **42670 t**；full **46680 t**」——https://www.navypedia.org/ships/uk/brit_bb1_hood.htm（normal 与本站 1931 年 light 42,037 接近但不等；full 与本站 1920 年 deep 46,680 完全一致 → 疑为引用 1920 年 deep 值）
- 1930s 手册：「displacement **44,600 tons**」——https://www.hmshood.org.uk/ship/pamphlet30s.htm（宣传取整）
- navypedia 1931 改装后：「displacement: **45693 (normal) / 48000ts**」——同上（48,000 与本站 1931 deep 一致）
- naval-history：「**41,200 tons**」——https://www.naval-history.net/OWShips-WW1-02-HMS_Hood.htm

### 标准 / 满载（任务指定口径）
- **未获取**。本站只给 Light 与 Deep；「Standard」「Full」在来源中仅为定义、无数值。**不做推算填充。**

---

## 5. 动力

### 锅炉
- 「Steam was supplied by **24 Yarrow Small Tube 3 Drum Boilers**… six of these boilers in each of the four boiler rooms. The working pressure was **235 lbs psi**, and the heating surface per boiler was 7,290 feet².」——https://www.hmshood.org.uk/ship/hoodspecs3.htm
- navypedia：「24 Yarrow boilers」——https://www.navypedia.org/ships/uk/brit_bb1_hood.htm
- **蒸汽温度：未获取**（hoodspecs3 未给）

### 汽轮机
- 「four sets of turbines. Each turbine served one propeller shaft… compound ahead turbines… single reduction gearing… Brown-Curtis type cruising turbine」——https://www.hmshood.org.uk/ship/hoodspecs3.htm
- 「The ship's main propelling machinery, **Brown Curtis geared turbines**, were the most powerful manufactured at that time with a designed output of **144,000 shp**.」——https://www.hmshood.org.uk/history/construct/construction.htm
- navypedia：「4 sets Brown-Curtis geared steam turbines」——https://www.navypedia.org/ships/uk/brit_bb1_hood.htm
- **厂家：未获取**（navypedia 未标；Association 未标）

### 轴数与螺旋桨
- 4 轴：「No of shafts 4」——navypedia
- 「Screws: 4x **three bladed** Manganese Bronze screws」「Screw Diameter: **15ft / 4.57m**」「Screw Weight: 20 tons apiece」「Shaft Diameter: 28.5in / 72.4cm」——hoodspecs3

### 功率
- 设计：「The engines were designed to develop a total horsepower of **144,000**, with about 210 revolutions…」——hoodspecs3
- 试航实测：「On the measured five mile run off Arran, a mean speed of 32.07 knots was attained, the horsepower being **151,000**.」——https://www.hmshood.org.uk/history/construct/construction.htm
- 1939 年状态：「the engines could still attain 144,000hp with a screw rotation of 197.6 rpm」——https://www.hmshood.org.uk/ship/hoodspecs4.htm

### 航速
- 设计：「Originally designed 210 rpm. Achieved **206 rpm** at full speed on trials in Feb/March 1920.」——hoodspecs3
- 实测：「**32.07 knots / 59.4 km/h** was achieved during a full power run on the Arran Mile, at a displacement of 42,000 tons / 42674.6MT and with Force 6 winds.」——https://www.hmshood.org.uk/ship/hoodspecs4.htm（页面标题错排为「Designed Max. Horsepower」，实给航速）
- 平均最高：「Average Top Speed: **31 knots**」——同上
- 1941 年实际：「By 1941 however… _Hood_ could only manage about **28.8 knots**」——同上；交叉：「as high as **28.8 knots** per _Prince of Wales's_ log for 24 May 1941」——https://www.hmshood.org.uk/history/denmarkstrait/bismarck2.htm
- navypedia：「Max speed 31 kts」——https://www.navypedia.org/ships/uk/brit_bb1_hood.htm

### 续航
- 「Un-refuelled Range: **4,500 nm / 8,334 km at 20 knots** or **5,000 nm / 9,260 km at 18 knots**.」——https://www.hmshood.org.uk/ship/hoodspecs4.htm
- navypedia：「Endurance **7500 nm(14 kts)**」——https://www.navypedia.org/ships/uk/brit_bb1_hood.htm
- **分歧记录**：两套续航曲线互不相容（4,500@20 / 5,000@18 vs 7,500@14）。疑为不同年份/不同油量口径。

### 燃油容量（三方冲突，全列）
- 「average load of approximately **1,200 tons / 1219.3 MT**… Maximum load was **4,000 tons / 4064.3 MT**」——hoodspecs3
- 「The oil fuel tanks have a capacity of **4,600 tons**.」——https://www.hmshood.org.uk/ship/pamphlet30s.htm
- 「Fuel **3895 t oil**」——navypedia；1931 改装后「fuel tanks capacity increased to **4615t** of oil」——同上
- 日志实证：「**Received 3465 tons of oil fuel** from RFA FORTOL」（1923-11-24）——https://www.naval-history.net/OWShips-WW1-02-HMS_Hood.htm

### 电机/发电机功率
- 发电机：「The ship was fitted with **eight dynamos**. Two were powered by 8 cylinder diesel engines, two by high speed impulse turbine engines and four by reciprocating engines. The generators could supply either **AC or DC** power as required.」——https://www.hmshood.org.uk/ship/hoodspecs5.htm
- 电动机：「estimated that she contained **around 360 motors**… small ventilation fans could use a ¼ hp motor, whereas… boat hoists required motors of **140bhp**」——同上
- **总电功率：未获取**（两页均未给 kW 总数）

---

## 6. 防护

### 主装甲带
- 「Main Armour Belt: **Length/Height-** 562ft X 9ft 6in / 171.3m X 2.9m.」「**Thickness-** 12in/30.5cm (max), tapering to 5in/12.7cm forward & 6in/15.2cm aft」——https://www.hmshood.org.uk/ship/hoodspecs2.htm
- navypedia：「Main 305mm belt extended between barbettes "A" and "Y" and was **2.89m deep**… Its thickness decreased to stem up to **152 and 127mm** consequently and to stern up to **152mm**.」——https://www.navypedia.org/ships/uk/brit_bb1_hood.htm
- 口径一致（12 in = 305 mm；562 ft = 171.3 m；9'6" ≈ 2.9 m）。

### 倾角
- 「Ship sides and belts were **inclined at 12° to the vertical**.」——navypedia
- hmshood hoodspecs2.htm **不含倾角数据**。

### 上装甲带 / 中装甲带（**术语分歧**）
- navypedia：「**178mm medium belt** between end barbettes was 2.75m deep. **Upper 127mm belt** connected with forecastle deck.」——同上
- hmshood：「**Lower Armour Belt:** 7in / 17.8cm」——hoodspecs2（178 mm = 7 in，但被称作 "Lower"）
- **分歧记录**：同一层 7 in / 178 mm，navypedia 称 "medium belt"，hmshood 称 "lower belt"；navypedia 另有 127 mm "upper belt"，hmshood 该页未列此层（仅列 Bulkheads 4in & 5in）。

### 装甲甲板（分层）
- hmshood：「Forecastle 1¾-2in / 4.4-5cm；Main 1-3in / 2.5-7.6cm（averaged 2in on the slope）；Upper ¾-2in；Lower 1-3in（3in amidships in vicinity of boiler rooms）」——hoodspecs2
- navypedia：main deck **76mm** flat over magazines、**51-38mm** over machinery、**51mm** slopes、25mm fore / 51mm aft outside citadel；medium deck 25mm→76mm over steering gear / 51mm over magazines；upper deck 19mm（over magazines 51mm）；forecastle 51-32mm（38mm over fore magazines）——https://www.navypedia.org/ships/uk/brit_bb1_hood.htm
- 两说不矛盾但分层命名体系不同。

### 炮塔装甲
- hmshood：「Gun Houses: **Face 15in/38.1cm，Sides 11-12in，Rear 11in/27.9cm，Roof 5in/12.7cm**」——hoodspecs2
- navypedia：「turrets: **381 (face) - 305 - 279 (sides) - 279 (rear) - 127 (roof)**」——navypedia
- 口径一致。

### 炮座（barbettes）
- hmshood：「Barbettes **12in/30.5cm max**」——hoodspecs2
- navypedia：「barbettes: **305 - 127**」「305mm armour over main deck, armour thickness under main deck changed from 305 - 229mm (aft side of the "Y" barbette) and 254mm (fore side of the "A" barbette) to **152 - 127mm**」——navypedia

### 司令塔
- hmshood：「Conning Tower **9-11in / 22.9-27.9cm vertical、2in/5cm decks**；Funnel Uptakes 1in」——hoodspecs2
- navypedia：「CT: **280 - 76**」——navypedia
- 疑为同物换算（11 in = 279 mm ≈ 280 mm）。

### 横向舱壁
- hmshood：「Bulkheads: **4in & 5in / 10.2cm & 12.7cm**」——hoodspecs2
- navypedia：「305mm belt area was closed by **127mm fore and 102mm aft bulkheads**」；「bulkheads: 127 - 102」——navypedia

### 防雷舱壁与水下防护
- navypedia：「Main belt was closed by bulges as its inside bulkhead and extended to the double bottom as **38mm torpedo bulkhead**. **Underwater protection deep was 3.1m.**」——navypedia
- hmshood hoodspecs2.htm **未列防雷舱壁**（这是该页明显缺项）。

### 装甲总重与占比
- 「**13,800 tons of armour is fitted**, that on the side being twelve inches thick.」——https://www.hmshood.org.uk/ship/pamphlet30s.htm
- **占比：来源未直接给**。按同页 13,800/44,600 计算约 **30.9%**（本报告换算，非来源原句）。
- 对照：Bismarck 为 19,082 t / 47,870 t「about **40%**」——https://www.kbismarck.com/proteccioni.html

### 装甲钢型号
- **未获取**（hmshood、navypedia 均未标 Hood 的钢种；对照 Bismarck 为 KC n/A、Wh n/A、Ww n/A、St 52 KM）

---

## 7. 武备

### 主炮：15 in/42 BL Mk I（4 × 双联 Mk II 炮塔）
- 型号与门数：「Gun Type **Mk I**」「**8 guns (2 per turret x 4 turrets)**」「Calibre 15"/38.1cm」「Barrel Length **42 cal (630")/16520.2mm**」「Overall 650.4"/16502mm」「76 grooves RH」——https://www.hmshood.org.uk/ship/maingun.htm
- 弹药：「Charge **Cordite MD45**；Full 428 lbs/194.1kg；Reduced 321 lbs/145.6kg；**Shell 1920 lbs/870.9kg**；Pressure 19.5 tons psi/305 MPa；**MV 2462 fs/750 ms**」——同上
- 射速：「Rate of Fire: **2 rounds every 30 seconds** (4 rounds per minute per turret)」——同上；navweaps 交叉：「II mountings used on Hood had a nominal firing cycle of **32 seconds**」——https://www.navweaps.com/Weapons/WNBR_15-42_mk1.php
- 射程：「Max. Range (New Barrel): **30,180 yds / 27,596.6 m (at 30° elev.)**」——maingun.htm
- 俯仰/旋回：「Elevation **30°/-05°**」——maingun.htm；navweaps：「Elevation **Mark II: -5 / +30 degrees**」「Rate of Elevation **5 degrees per second**」「Train -150 / +150 degrees」「Rate of Train **2 degrees per second**」——WNBR_15-42_mk1.php
- 座重：「**Mark II: 880 tons (894 mt)**」；对照 Mk I 为 770 tons (782 mt)——WNBR_15-42_mk1.php
- 装座特征：「The Mark II mount was used only on HMS Hood and had a polygon shaped front plate… All four turrets had **30 foot (9.17 m) MG14 rangefinders**… sighting hoods on gunhouse roof replaced by sighting ports in the turret face… **hydraulic run-out for the guns replaced by pneumatic run-out**.」——同上
- 成本：「Cost of a Mark I mounting was £116,000 for the mounting and an additional **£32,000 for the two guns**.」——同上
- 弹药基数（As built）：「As completed, Hood had an outfit of **289 CPC, 672 APC, 30 Shrapnel**」——同上
- 弹药基数（1939）：「World War II in 1939, Hood carried **80 APC and 20 CPC per gun**」——同上
- 弹药基数（另一口径）：「Courageous 23b and Hood 24b classes: **120 rounds**」——同上
- 弹药基数分歧：120 发/门 vs 100 发/门（80+20）。两处同页并存，疑为「设计基数」与「实际配发」口径。
- 特殊记录：「_Hood_ was the only such ship ever equipped with **Type I guns on a Type II mounting**.」——maingun.htm

### 副炮：5.5 in/50 BL Mk I（12 × 单装 CPII）
- 「**Mk I**，5.5in/13.97cm，**50 cal (275")/698.5cm**，**Cordite MD19**，Full Charge 22 lbs 4 oz/10.1kg，**Shell 82 lbs / 37.2 kg**，**MV 2790 fps / 850 mps**」——https://www.hmshood.org.uk/ship/secondary.htm
- 射速：「8-12 shots per minute」（hmshood）/「**12 rounds per minute (maximum)**」（navweaps https://www.navweaps.com/Weapons/WNBR_55-50_mk1.php）
- 射程：「Max. Range (New Barrel): **18,500 yds / 16,916 m (at 30°)**」——secondary.htm；navweaps：「30 degrees **18,500 yards (16,920 m)**」——WNBR_55-50_mk1.php
- 装座：「Hood (12): **CPII**」「CPII: **18.68 tons (18.89 mt) including shield**」「Elevation **-5 / +30 degrees**」「**Manually operated, only**」——WNBR_55-50_mk1.php
- 布置：「_Twelve 5.5-inch guns_, six on each side… extreme range is 9 miles」——https://www.hmshood.org.uk/ship/pamphlet30s.htm
- 弹药基数：「Outfit for **Hood as built was 1,728 Lyddite, 582 common, 96 shrapnel, 464 practice**. After 1929-1931 refit，**1,368 HE, 624 Shellite, 360 HENT, 50 starshell**（forward shell room only）and 449 practice.」——WNBR_55-50_mk1.php
- **拆除**：「**All 5.5" guns and mounts were completely removed in May 1940.**」——secondary.htm；交叉：「Hood had **two mounts removed in 1938-1939** and the remainder removed in 1940.」——WNBR_55-50_mk1.php

### 高炮：4 in/45 QF Mk XVI（双联 Mk XIX）
- 「**双联 4" Mk XVI**：4"/10.2cm，2 barrels，45 cal，Cordite SC 9 lbs，**Shell HE 35.9 lbs/16.3kg**，**MV 2650 fps/807.7 mps**，**ROF 16-18/min**，**Max Range 21,300 yds at 45°**，Ceiling 40,000 ft at 80°，**Elevation 80°/10°**，Mount **Mk XIX**，HACS **Mk III***」——https://www.hmshood.org.uk/ship/aaa.htm
- navweaps 交叉：「**Rate Of Fire 15 - 20 rounds per minute**」「**MV Standard Charge: 2,660 fps (811 mps)**」「Range @ 45 degrees: **19,850 yards (18,150 m)**」「AA Range @ 80 degrees: **39,000 feet (11,890 m)**」「Mark XIX: **37,072 lbs. (16,816 kg)**」「Elevation **-10 / +80 degrees**」——https://www.navweaps.com/Weapons/WNBR_4-45_mk16.php
- **射程分歧**：21,300 yds（hmshood）vs 19,850 yds（navweaps）。疑为「新增药强装」与「标准装药」口径差。
- 数量与加装：「Four of these were first fitted to the Shelter Deck in **1937**. An additional three were fitted to the Shelter Deck in **1940**.」「three emplacements to port ("P1","P2","P3"), three to starboard ("S1","S2","S3") and one at the very end of the Shelter Deck on the centreline ("Number 4")」「carried these **seven** gun emplacements to the end」——aaa.htm → **7 座 / 14 门**
- 交叉：「HMS Hood had **four twin mountings added in 1937 and three more twin mountings added in 1940**」——WNBR_4-45_mk16.php
- 弹药基数：「**Hood**, Barham, Malaya and Warspite: **250 to 280 rounds plus 250 total star shells**」——同上

### 高炮：4 in Mk V（单管，1939 前）
- 「单管 **4" Mk V**：45 cal，Shell 31.4 lbs/14.25kg，MV 2643 fs，ROF 8-13/min，Max Range 16,300 yds at 45°，Ceiling 28,750 ft at 80°，Mount Mk III/IV，HACS Mk I + 12ft RF」——aaa.htm
- 拆除：「Between 4 and 8 guns were carried on the Shelter Deck until the completion of the **1939 refit**, at which point they were removed entirely.」——同上

### 2-pdr 八联 pom-pom（Mk VIII）
- 「40mm，8 barrels，40 cal，Shell 2 lbs，MV 1920 fps，Max Range 3800 yds，Elevation 80°/10°，Mount Mk V/VI」——aaa.htm
- 加装：「The first two mounts and Mk I series directors were added to the forward Shelter Deck in **1931**… A third and final mount was added… to the rear Shelter Deck in **late 1937**.」→ **3 座**（别称 Sammy / Peter / Auntie）

### 0.5 in 机枪（四联 Vickers Mk III）
- 「12.7mm，4 barrels，600 rpm max/@180 practical，Max Range 1500 yds」——aaa.htm
- 加装：「The first two mounts… were added near the Conning Tower in **late 1933**… Two more were added abreast the Rear Superstructure in **late 1937**.」→ **4 座**（别称 Pip / Squeak / Simon / Paul）

### UP 火箭（Unrotated Projectile Mk I）
- 「UP Mk I：20 管，7in/178mm × 32in 火箭，8oz 弹头，齐射 10 发，最大高度 @1,000 ft」——aaa.htm
- 数量与位置：「_Hood_ was outfitted with **5 UP mounts** which were added in **1940**. One was atop "**B**" turret, and the remaining four on the **Shelter Deck**.」——同上
- 事故：「UP mounting on 'B' turret accidentally fires off 20 charges over harbour; **three ratings badly burnt**.」（1940-07-27）——https://www.hmshood.org.uk/history/timeline4.htm
- 战损相关证词（ADM116/4351）：Tilburn 认为火灾起于舯部 UP 发射器附近并引燃 ready-use 弹药：「My idea was the U.P. ammunition had caught fire because some ammunition exploded.」——https://www.hmshood.org.uk/reference/official/adm116/adm116-4351_Hood.htm

### 鱼雷
- 「Type: **Mk IV and Mk IV***」「**21" / 53.34 cm**」「Torpedo Weight 3,357lbs / 1522.7 kg」「Mk IV, TNT, 515lbs / 233.6 kg」「Range: **5,000 yds (40kts)** or… **13,500yds (25kts)**」——https://www.hmshood.org.uk/ship/torpedo.htm
- 布置与拆除：「**2 submerged tubes** (1 port, 1 starboard, located below waterline just ahead of "A" turret. **Removed in 1937**); **4 above water tubes** (2 per side… parallel with main mast). The above water torpedo tubes remained on the ship until the end.」——同上
- 交叉：「**two submerged and four above-water** 21-inch torpedo tubes」——https://www.hmshood.org.uk/ship/pamphlet30s.htm；navypedia 1937 年 12 月「- 2 - 533 TT」——https://www.navypedia.org/ships/uk/brit_bb1_hood.htm
- 礼炮：「4 × 3pdr Hotchkiss（至 1940）」——https://www.hmshood.org.uk/ship/other.htm

---

## 8. 火控与雷达

### 火控台型号（**重要更正**）
- 「_Hood_ was fitted with the **Mark V Dreyer Table** - the only vessel in the Fleet with that particular unit.」——https://www.hmshood.org.uk/ship/fire_control.htm
- 「**Dreyer Table Mk V:** one in the 15-inch Transmitting Station」——同上
- 「the 15-inch TS was on the Platform Deck, **9 levels below the revolving Director Hood**」——同上
- **AFCT（Admiralty Fire Control Table）未装**。任务书要求的「Admiralty Fire Control Table Mk ?」在本舰不成立，应记为：装 Dreyer Mk V，AFCT 未获取/不适用。

### 主炮指挥仪数量与位置
- 「**15-inch tripod-type director:** one per 15-inch Director Tower」——fire_control.htm
- 位置：「the 15-inch TS was on the Platform Deck, 9 levels below the **revolving Director Hood**」（同上）；「Both antennas were mounted on the **rotating director hood situated above the Spotting Top**」（https://www.hmshood.org.uk/ship/radar.htm）
- **第二座（后部）指挥仪：未获取**（hmshood 各页只描述这一座）

### 测距仪基线
- 「**Rangefinders:** 30-foot – **one in each turret**; one in Director Tower; 15-foot – **one in the aloft Director Tower**」——fire_control.htm
- 「the primary directors were the **15 ft/4.6 m rangefinder above the Spotting Top** and the **30 ft/9.1 m rangefinder atop the Conning Tower**. Additionally, each turret/gun house was fitted with a 30 ft/9.1 m rangefinder」——https://www.hmshood.org.uk/ship/maingun.htm
- 副炮：「two 9-foot (replaced by 12-foot after 1924) rangefinders」——fire_control.htm
- 鱼雷：「15ft rangefinders- in hood on conning tower (removed in 1937), 2 mounted midships (removed in 1940)」——https://www.hmshood.org.uk/ship/torpedo.htm

### 雷达（1941 年只有两套）
- 「_Hood_ was fitted with two radars in early 1941. These were the **Type 284** gunnery radar and **Type 279M** aerial warning radar.」——https://www.hmshood.org.uk/ship/radar.htm
- **Type 284（主炮测距）**：「Wavelength 50 cm，Power 25 kw，~600 MHz，Range 10 nm」；「_Hood_ received her Type 284 during her **16 January - 15 March 1941 refit at Rosyth**」——同上
  - 安装日期分歧：radar.htm 记「16 January - 15 March」；timeline4 记「**16 January–17 March**」（https://www.hmshood.org.uk/history/timeline4.htm）→ 相差 2 天，并列不裁决。
- **Type 279M（对空预警）**：「7.5 m，60 kW ranging/70 kW warning，39-42 MHz，accuracy within 3°，Range 100 nm high altitude」；单收发天线「located high above her main mast」；来源文件 ADM 220/76——同上
- **Type 282 / 285 未装**：「According to C.A.F.O. 509, issued in March 1941… _Hood_ was slated to receive three **Type 282** and three **Type 285**.… it is certain that her Type 282 directors were not fitted. It is unclear however, if the Type 282 sets were fitted. There are also no indications that any part of her Type 285 radar was installed.」——同上
- **雷达型号分歧**：navypedia 记「early 1941: + **type 79B**, type 284 radars」——https://www.navypedia.org/ships/uk/brit_bb1_hood.htm；hmshood 记 **279M**。两说并列。
- 相关：1941 改装中「the removal of the forward topmast (it blocked Type 284 radar aerials from rotating properly)」——timeline4

---

## 9. 航空

- 机型：「Aircraft: **1-2 Fairey "Flycatchers"** (up to 1933) and/or **1 Fairey IIIF** (1929-1933). **Sopwith 1 1/2 Strutter** also seen aboard.」——https://www.hmshood.org.uk/ship/other.htm
- 弹射器与吊车：「A **catapult, crane** and associated equipment were fitted to the quarterdeck aft of "Y" turret during the **1929-1931 refit**. These were **removed in mid 1932**… All aircraft gear was removed by **December 1933**.」——同上
- 弹射器型号（第三方）：「1 catapult **F-IV-H** with 1 seaplane」——https://www.navypedia.org/ships/uk/brit_bb1_hood.htm；拆除：navypedia 记「6/1932: - 1 catapult with seaplane」——同上
- **起飞平台位置分歧**：
  - other.htm：「Launching/Flying-off platforms were fitted to "**B**" and "**X**" turrets.」
  - timeline2（1920-04-15~05-06）：「aircraft flying-off platforms fitted to "**A**" and "**B**" turrets」——https://www.hmshood.org.uk/history/timeline2.htm
  - **分歧记录**：B/X（后期状态）vs A/B（1920 年状态），两处并存，不裁决。
- 损失记录：「1931-06-26 损失 Fairey IIIF」——https://www.hmshood.org.uk/history/timeline3.htm

---

## 10. 编制

### 和平时期 / 战时
- 「The average peacetime crew was roughly **1,200** officers and ratings… During wartime, the number of crew increased to **1,400+**.」——https://www.hmshood.org.uk/ship/hoodspecs6.htm
- 手册口径：「In war time the ship would carry about 1,400 officers and men, but in peace time only 1,200.」——https://www.hmshood.org.uk/ship/pamphlet30s.htm

### 1940 年 6 月核准战时编制（ADM 136/13）
- 「SCHEME OF WAR COMPLEMENT of H.M.S. HOOD as Flagship of the R.A. or V.A. Commanding Battle Cruiser Squadron … Date of issue **4th June, 1940**.」「likely very similar to her final complement」——https://www.hmshood.org.uk/crew/complement/complement40.htm
- 「**1,233** TOTAL COMPLEMENT」→「**1,237 FULL WAR COMPLEMENT**」——同上
- 细项：Captain 1、Commander 1、Commander (N) 1、Lt Cdr/Lt RN 5、Lt Cdr (G) 2、Lt Cdr (T) 1、Lt Cdr (PRT) 1、Sub Lt RN 1、**Midshipman RN 10**、各类 Commissioned Gunner 共 5；Engineer：Engineer Commander 1、Cdr(E) 1、Lt Cdr (E) 3、Lt/Sub Lt (E) 4——同上
- Royal Marines：Major 1、Captain 1、Lieutenant 1、Colour Sergeant 1、Sergeant 7、Corporal 10、Bugler 2、**Marine 110**——同上

### 1941-05-24 实际在舰人数
- 「based on _Hood's_ final complement of **1,418** men on 24 May 1941: **Royal Navy: 89 officers and @1157 ratings/enlisted men; Royal Marines: @4 officers and @161 men; NAAFI: @ 7 civilian men**」——https://www.hmshood.org.uk/ship/hoodspecs6.htm
- 校验：89 + 1,157 + 4 + 161 + 7 = **1,418** ✓
- NAAFI 文职 7 人名单：Canteen Manager William Trevarthen + 6 名助理（Ken Algate、Frank Ayling、Geoffrey Jordan、Cecil Lansdowne、Jack Ovenden、Jack Titheridge）——https://www.hmshood.org.uk/crew/naafimen.htm
- 「a number of crewmen were ashore (leave, hospital, training, deserters, etc.)」——hoodspecs6

### 见习军官（cadet / midshipman）——**关键事实的核实结果**
- 任务前提为「舰上有大量 cadet」。权威名册可核到的数字：
  - 沉没时在舰且阵亡的 **Midshipman：13 人**（含生还的 Dundas，其条目注明「survivor of the sinking」）——https://www.hmshood.org.uk/crew/database/ROHRankRating.php?RankRating=Midshipman
  - **Probationary Temporary Midshipman：1 人**（Kenneth Guy Warden，1940-12-02 上舰）——https://www.hmshood.org.uk/crew/database/ROHRankRating.php?RankRating=Probationary%20Temporary%20Midshipman
  - 合计在舰见习军官级 **14 人**，其中 13 人随舰阵亡
- 1940-06 战时编制表列 **Midshipman RN 10**——complement40.htm
- **关于「大量 cadet」：未获取到任何原句支持「数十/上百名 cadet 在舰」。**可核实的只有上述 10-14 人规模。建议站点不要沿用「大量 cadet」的表述。
- 旁证（舰员普遍年轻）：「Hood's ship's company was remarkably young with **78 men aged less than 18 years**. **900 (63.6%) were under 25**, the oldest casualties were aged 53.」——https://www.hmshood.org.uk/crew/database/roh.php

### 阵亡人数（**三说并存**）
- Association 核证：「**the actual number of men lost in the sinking was 1,415**」，并解释 1,418 是「在舰人数」、1,416 为误含一名 PoW 舰员——https://www.hmshood.org.uk/admin/faq.htm
- 「The links below give access to **1,415** individual memorial pages」——https://www.hmshood.org.uk/crew/database/roh.php
- 1,418：「Out of a crew of **1,418** only three … survived」——https://www.hmshood.org.uk/history/timeline4.htm
- navypedia：「**1419 men lost**」——https://www.navypedia.org/ships/uk/brit_bb1_hood.htm
- **分歧记录**：1,415（核证阵亡）/ 1,418（在舰）/ 1,419（navypedia，疑为笔误或含文职统计差）。三者并存，不裁决。

### 幸存者
- 「only three (Ordinary Signalman **Ted Briggs**, Midshipman **William Dundas**, Able Seaman **Robert Tilburn**) survived」——https://www.hmshood.org.uk/history/timeline4.htm
- 「There was absolutely no trace of the other **1,415 crewmen** alive or dead.」——https://www.hmshood.org.uk/history/denmarkstrait/bismarck2.htm
- 救起与遣返：「H.M.S. _Electra_（H27）救起，当日深夜送抵 Reykjavik」——同上；「The three survivors of _Hood_ were disembarked at **Greenock on 29 May**.」——https://www.hmshood.org.uk/history/denmarkstrait/bismarck3.htm

---

## 11. 涂装

> 来源：https://www.hmshood.org.uk/hoodtoday/models/tips/hoodpaint.htm（Updated 26-Jun-2025；Dave Weldon / Alan Raven / Bruce Taylor / David Mearns）

### 1920–1936（Home Fleet 深灰）
- 「During the first few years of her career, this was a **pure dark grey**. The formula was changed in the **mid 1920s to include a tinge of blue**.」——同上
- 「_Hood_ wore the contemporary versions of the **Home Fleet dark grey colour for her entire career except for her 1936-1939 assignment with the Mediterranean Fleet**.」——同上

### 1936–1939（海外站浅灰 507C）
- 「This was the standard colour for Royal Navy ships assigned to foreign stations, including the Mediterranean Fleet. This colour was a **light grey with a very slight blue tinge**.」「The hull and superstructure were painted in this shade」——同上

### 1939–1941（回到 Home Fleet 灰）
- 1939 年战争爆发起：「A matte variation of the colour (known as **Pattern 507A**) was introduced around the start of the Second World War.」——同上

### 1941 年初的短暂双色调试验
- 1941 年 1–5 月曾出现 A 炮塔偏浅、B 炮塔与 Spotting Top 偏深的试验涂装，但「**no longer in use** when the ship sailed to find _Bismarck_」——同上

### 1941-05 丹麦海峡时的实际涂装（**常见误画点**）
- 「**The last documented painting of Hood took place on 12 May 1941** (per the journal of Midshipman Philip Bucket).」「the previous two toned look was abandoned in favour of a **uniform grey**.」——同上
- 具体色号：「_Hood_ en route to fight _Bismarck_, May 1941. She's shown here wearing **AP507B** paint.」；推荐漆号「Sovereign Hobbies Colourcoats **NARN20 - 1936-1943 Home Fleet Grey 507A / 507B 13% RF**」「Lifecolor **UA631 Admiralty Dark Grey 507A**」——同上
- 炮口与炮衣：「The ends of the 15" barrels were finally **painted over** (for camouflage purposes). Blast bags were the same grey as the hull. They were **NOT plain canvas nor white**!」——同上
- 舰名：「the ship's name was **painted over in a dark grey or possibly black**」——同上
- 战斗旗：「be sure to use **one Battle Ensign**… extremely large version of the White Ensign (@24ft in length)… flown from the large lower flag gaff on the mainmast starfish… **she flew just one ensign**」（Ted Briggs 证言）——同上
- 水线下（**常见误画点**）：「_Hood_ **NEVER had a red bottom**.」「everything under the waterline, to include the propeller shafts and rudder, was coated in **Peacock & Buchan's anti-fouling paint**（only supplied in **grey or black**）」「anti-fouling **grey** (an unspecified shade of grey over a slate undercoating)」；依据 D495 Reports in ADM 136/13——同上
- 水线漆带：「boot topping … generally **glossy black** (and about **8ft tall**)」——同上
- 甲板与桅杆：teak 本色不打漆、corticene 棕色、semtex 灰/棕/绿；foremast 上部黑、桅顶白；mainmast 三脚汇合处以上黑 + 白环带、桅顶白——同上
- FAQ 交叉确认：「**Hood never had a red bottom.**」——https://www.hmshood.org.uk/admin/faq.htm

---

## 12. 生涯时间线（精确到日；重大事件到分钟）

### 1916
- **04-21** 下单三艘：「**21 April:** The Admiralty Board placed orders for three Admiral-class battlecruisers: _Hood_ (John Brown), _Howe_ (Cammell Laird), _Rodney_ (Fairfield).」——https://www.hmshood.org.uk/history/timeline1.htm
- **04（同月）** 日德兰海战 1916-05-31 后重新设计：主装甲带 9" → 12"，「The reworked design was approved on **4 August 1916**.」——https://www.hmshood.org.uk/history/construct/construction.htm
- **05-31（存疑）** 首次铺龙骨（Association 判为不可信，见 §2）——timeline1
- **07（月内）** 第四艘 _Anson_ 下单——timeline1
- **07-14** 命名通知：「**14 July:** Admiralty informed John Brown that their ship is to be named _Hood._」——timeline1
- **09-01** 确认铺龙骨：「**01 September:** Confirmed date _Hood's_ keel was laid… She was ship number 460.」——timeline1

### 1917
- **03-09** 三舰停工：「**09 March 1917:** The Admiralty suspended construction of _Howe_, _Rodney_ and _Anson_」——timeline1
- **08-30** 设计最终批准：「the design was approved by Admiralty only **30.8.1917**」——https://www.navypedia.org/ships/uk/brit_bb1_hood.htm

### 1918
- **08-22** 下水：「_Hood_ was launched at **1305 hours** by Lady Hood」——timeline1
- **10（月内）** 三艘同级取消：「**October 1918:** The Admiralty cancels the other three Admiral-class battlecruisers.」——timeline1

### 1919
- **05-19** 舱内爆炸事故，2 名船厂工人死亡——timeline1
- **12-09/10** 系泊试验（Basin trials）——timeline1

### 1920
- **01-01** Captain Wilfred Tomkinson 接任——https://www.hmshood.org.uk/history/timeline2.htm
- **01-09** 自行驶离 Clydebank：「_Hood_ departs Clydebank under her own power… working up to over 130,000-horse power」——construction.htm
- **03-05** 建成/弹库上方甲板装甲加厚获准——timeline2 与 pamphlet30s
- **03-18** Arran 全功率试航：32.07 kn / 151,000 shp——construction.htm
- **03-22/23** 深载试航——timeline2
- **03-29** 服役（Association 认定）：「commissioned by Captain Tomkinson and **967 crew**」——timeline2
- **04-15~05-06** 倾斜试验、Spotting Top 装 15 ft 测距仪、拆除主上桅、A/B 炮塔装起飞平台——timeline2
- **05-15** 出坞离 Rosyth 赴 Plymouth（**非**服役日）——timeline2
- **05-18** 成为大西洋舰队战列巡洋舰分队旗舰（Keyes 中将）——timeline2
- **06/07** 春季巡航北欧（Køge Bugt / Kalmar / Nynäshamn / Åbenrå / Copenhagen / Christiana）——timeline2
- **08-05** 派兵接收投降德舰 Helgoland / Westfalen / Rügen——timeline2
- **11-11** 无名战士葬礼仪仗——timeline2

### 1923–1924（帝国巡游 Empire Cruise）
- **1923-11-27** 启航：「**27 November 1923–29 September:** The "Cruise of the Special Service Squadron" (AKA "**Empire Cruise**" or "World Cruise"). _Hood_ was the **centrepiece** of the famous public relations cruise around the world.」——timeline2
- 编队：Delhi / Dragon / Repulse / Danae / Dauntless；07:00 离 Devonport——https://www.naval-history.net/OWShips-WW1-02-HMS_Hood.htm
- **1924-09-28** 在 Lizard Point 与 1st LCS 会合返抵——timeline2
- 意义（成为「Mighty Hood」的直接原因）：这次巡游是「the famous public relations cruise around the world」，_Hood_ 为其核心。——timeline2

### 1929–1931 大改装
- 起止：「**01 May–31 December 1929:** … _Hood_ was paid off and taken in hand for a **2 year long major refit (03 June 1929-10 March 1931)**.」——timeline2 → **1929-06-03 至 1931-03-10**，Portsmouth
- **改装清单：hmshood 的 refits.htm 三节全部为「Pending research/under construction」，站内没有该项目清单**——https://www.hmshood.org.uk/history/construct/refits.htm
- 可核实的改装内容（分散来源，逐条列出）：
  - 加装 2 座八联 pom-pom（1931）：「The first two mounts and Mk I series directors were added to the forward Shelter Deck in **1931**」——aaa.htm
  - 装弹射器 F-IV-H + 水上飞机 + 吊车（Y 炮塔后方甲板）：「A catapult, crane and associated equipment were fitted to the quarterdeck aft of "Y" turret during the **1929-1931 refit**」——other.htm
  - 油舱容量增至 4,615 t、排水量变为 45,693（normal）/ 48,000 t——navypedia「1931: … fuel tanks capacity increased to **4615t** of oil, displacement: 45693 (normal) / 48000ts」
  - 拆除鱼雷火控台：「Dreyer Table: one in Torpedo TS (**removed 1929-31 refit**)」——fire_control.htm
  - 5.5" 弹药基数换代（HE / Shellite / HENT 体系）——WNBR_55-50_mk1.php
  - **换锅炉、加防雷鼓包**：**未获取**（本次抓取未找到明确原句）
- 完工后状态：「**10 March 1931:** Commissioned for trials at Portsmouth as tender to H.M.S. _Victory_」「**12 May:** Completed with a full crew of Portsmouth ratings」「**16–17 June:** En route to Portland」——https://www.hmshood.org.uk/history/timeline3.htm

### 1931–1939（小改装与中立巡逻）
- **1931-09-11~16** Invergordon，部分舰员卷入 Invergordon Mutiny——timeline3
- **1931-06-26** 损失一架 Fairey IIIF——timeline3
- **1932 年中** 拆除弹射器与水上飞机：「These were **removed in mid 1932**」——other.htm；navypedia「6/1932: - 1 catapult with seaplane」
- **1933 年末** 0.5 in 四联机枪前两座（Conning Tower 附近）——aaa.htm
- **1933-12（前）** 全部航空设备拆除：「All aircraft gear was removed by **December 1933**.」——other.htm
- **1935-01-23** 与 _Renown_ 相撞：「Collided with _Renown_ off Arousa Bay in position **42° 06'N, 09° 23'W**」（右舷舰尾受损）——timeline3
- **1935-09-17~12-05** 因意大利入侵阿比西尼亚驻 Gibraltar（海尔·塞拉西来访）——timeline3
- **1936-05-30** 海尔·塞拉西再访——timeline3
- **1936–1939** 编入地中海舰队，涂装换 507C 浅灰——hoodpaint.htm
- **1937 年** 4 座双联 4 in Mk XVI 装上 shelter deck——aaa.htm
- **1937-04-23** Thorpehall 事件（西班牙内战中立巡逻实证）：「_Hood_ trained her main guns at _Almirante Cervera_ and forced the Nationalist vessel to immediately stand down.」——timeline3
- **1937-05-07** Spithead 乔治六世加冕观舰式；**05-20** 国王登舰——timeline3
- **1937 年末** 第三座八联 pom-pom + 后部两座 0.5 in 四联——aaa.htm
- **1937 年** 2 具水下鱼雷管拆除——torpedo.htm
- **1938-09-20** 出港搁浅，轻损——timeline3
- **1939-01-23~08-12** Portsmouth 大修（更换高炮、修涡轮、修外底）——timeline3
- **1939-06-02** 重新服役，任本土舰队战列巡洋舰分队旗舰——timeline3

### 1939（二战爆发后）
- **08-31** 动员——https://www.hmshood.org.uk/history/timeline4.htm
- **09-03 11:00** 开战——同上
- **09-26** 被 Ju-88 的 500 lb 炸弹擦伤：「_Hood_ was struck by one **500 lb bomb** from a Ju-88 bomber; glancing hit of her port side… sprung rivets, port bulge amidships flooded slightly, condensers damaged」——同上
- **11-25** 追击 Deutschland（实为 Scharnhorst / Gneisenau），与法国舰队（Dunkerque 等，VAdm Gensoul）联合，未遇敌——同上

### 1940
- **04-13** 挪威战役：「Landing party of **250 Marines and Seamen** from _Hood_ (together with ship's howitzer) depart by train for Rosyth to participate in **Operation PRIMROSE**- the occupation of Ålesund, Norway.」——timeline4
- **04-17/18** 该分队在 Åndalsnes 登陆；**05-06** 归舰——timeline4
- **05（月内）** 5.5" 副炮全部拆除——secondary.htm / WNBR_55-50_mk1.php
- **07-03 17:55–18:04** **米尔斯克比尔（Operation CATAPULT）**——_Hood_ 是开火方之一：「Force H shells French fleet in harbour resulting in destruction of _Bretagne_ and serious damage to _Dunkerque_ and _Provence_」；18:09–18:12 与岸炮交战；追击 _Strasbourg_ 至 **20:22**；法方「@1,300 men dead」；_Hood_ 自身「no serious casualties (**2 lightly wounded men**)」——timeline4
- **07-27** UP 发射器事故：「UP mounting on 'B' turret accidentally fires off 20 charges over harbour; **three ratings badly burnt**.」——timeline4
- **08-31** 追击 Strasbourg 时右舷涡轮叶片剥离——timeline4
- **1940 年内** 加装 5 座 UP 发射器 + 3 座双联 4 in——aaa.htm

### 1941
- **01-13~03-18** Rosyth 改装：「De-ammunitioned, 14–15 January. Taken in hand for a refit, **16 January–17 March**. Modifications included the addition of **Type 284** gunnery radar and the removal of the forward topmast… A **Type 279M** aerial surveillance radar was also fitted… The blades of the starboard turbine… were replaced. Bottom was recoated.」——timeline4
- **02-15** Captain Ralph Kerr 接任——timeline4
- **03-16** 乔治六世检阅舰员——timeline4
- **05-08** Whitworth 将旗降下——timeline4
- **05-12** Holland 中将在舰设指挥部；**05-12** 最后一次记录涂装（单色灰）——timeline4 / hoodpaint.htm
- **05-13** 与 KGV 做距离/倾角演练——timeline4
- **05-22 23:56** 起锚：「_Hood_, _Prince of Wales_ and their destroyer escorts, weighed anchor at **2356 hours**… cleared Scapa's Hoxa Gate at **0050 hours**」——https://www.hmshood.org.uk/history/denmarkstrait/bismarck1.htm
- **05-23 19:15** 首个目视接触（Suffolk/Newell）：「Able Seaman Newell… saw Bismarck, and then Prinz Eugen roughly 7 miles away… _'two ships bearing green one four oh'_」——bismarck1.htm
- **05-23 20:04** 收到 Suffolk 报告；两军相距约 300 英里——bismarck2.htm

### 1941-05-24 丹麦海峡（分秒）
> 来源：https://www.hmshood.org.uk/history/denmarkstrait/bismarck2.htm 与 ADM116/4351

- **00:15** 全员进入战位、升战斗旗（_Hood_ 只升一面）——bismarck2.htm
- **00:30** Holland 信号「_If enemy is not in sight by 0210, I will probably alter course 180º until cruisers regain touch_」；「_Intend both ships to engage Bismarck and to leave [Prinz Eugen] to Norfolk and Suffolk_」——同上
- **01:47** 信号「_If battlecruisers turn 200º at 0205 destroyers continue to search to the northward_」——同上
- **02:03** 拦截部署（任务所问「03:00 前后」的原句在此）：「At **0203 hours**, just before dawn (approximately **0300 hours** in those latitudes at that time of year), _Hood_ and _Prince of Wales_ assumed a more southerly course of **200º** at a speed of 25 knots. The destroyers then parted… to screen at 15 mile intervals to the north.」——同上
- **02:47** Suffolk 恢复雷达接触，距 _Hood_ 约 35 英里；改向 **220°**，提速至 28 kn（PoW 日志记 **28.8 kn**）——同上
- **03:41** 改向 240°——同上
- **05:00–05:10** Holland 令「_Prepare for instant action_」——同上
- **05:35–05:36 目视**：「At roughly **0535-0536 hours**, lookouts in _Prince of Wales_ visually sighted smoke and mast tops of the enemy vessels at a range of at least **38,000 yards** (18.75 nm / 34.7 km).」——同上
- **05:37 距离与电报**：「_Prince of Wales_ transmitted an enemy report at **0537 hours**… _'One battleship and one heavy cruiser, bearing 335, distance 17 miles. My position **63-20 North, 31-50 West**. My course 240. Speed 28 knots'_」；「_Hood_ … did not transmit her enemy report until **0543 hours**」——同上
- **05:37 转向**：「VADM Holland had ordered his vessels to turn **40º to starboard** together… heading **280º**」；PoW 在 _Hood_ 右后方约 **800 yards**——同上
- **05:49** 再转 20°，航向 300°——同上
- **05:50** 目标指示「**G.S.B. 337 L1**」，指定打方位 337° 的**左侧**德舰（误认为 Bismarck）：「**In reality, it was _Prinz Eugen_.**」——同上
- **05:52½ 开火（打的是欧根亲王号）**：「Action commenced at **0552 1/2 hours**, as _Hood's_ two forward turrets fired the first salvoes.」；「_Hood's_ first salvo fell near _Prinz Eugen_ but did not actually hit.」——同上
  - 换靶令存在但未生效：「he ordered _'GOB1'_ … Despite this, Hood's target remained the left hand ship, _Prinz Eugen_.」；「_Hood_ survivors were sure that _Hood_ shot at least two salvoes **before** VADM Holland ordered the target switch.」——同上
  - **开火时间分歧**：bismarck2「0552 1/2」/ PoW 证词「0552」/ 调查委员会「**approximately 0553**」——https://www.hmshood.org.uk/reference/official/adm116/adm116-4351_89to144.htm
- **05:55 俾斯麦开火**：「At **0555 hours**, after two minutes of British shelling, Captain Lindemann had finally had enough… _Prinz Eugen_ shot first, followed shortly by _Bismarck_. Both vessels concentrated their fire on the lead British vessel, _Hood_.」——bismarck2.htm
- **05:55 转向**：「VADM Holland ordered the flag signal 'Blue 2' (**20° turn to port**)… to 'open A arcs'」——同上
- **05:55 起火**：「At **0555** … a fire was observed somewhere on the port after end of the boat deck of HOOD. We consider it established that this fire was caused by a hit from BISMARCK's **third salvo**.」——ADM116/4351
  - 火因争议：「either one 15inch shell from _Bismarck_ or one or more **8inch high explosive** shells from _Prinz Eugen_ struck _Hood_ near the base of the main mast… **It is widely believed that the hit was from _Prinz Eugen_ rather than _Bismarck_.**」——bismarck2.htm
- **05:59–06:00 致命齐射**：「This turn was executed sometime between **0559-0600**… _Hood_ was dealt her death blow- **_Bismarck's 5th salvo_** had straddled, with one or two shells likely striking Hood somewhere around the main mast, or possibly through a narrow weak zone in her side (possibly even underwater).」——bismarck2.htm
- **06:00 沉没（权威口径）**：「Just before 0600 … **at 0600 HOOD blew up and sank in just under 3 minutes**.」——ADM116/4351；「Hood sank at approximately **0600**」——bismarck2.htm；「At **0600**, _Hood_ sank」——timeline4
  - **时间分歧记录**：任务书给的「06:01 沉没」**未在本次抓到的正文中找到原句**。可核到的只有 0600（三处一致）与「0559-0600」区间。PoW 导航官证词说明这些时刻可能有多达 2 分钟误差：「these times may be in error up to as much as two minutes but I am satisfied that relative to each other they are correct」——https://www.hmshood.org.uk/reference/official/adm116/adm116-4351_POW.htm
- **坐标**：**未获取沉没点独立坐标**。文中唯一坐标为 PoW 0537 电报位置「**63-20 North, 31-50 West**」（战斗发生海域）。沉没深度见下。
- **06:02–06:03** PoW 施放烟幕退出；德方海战结束 **06:09**；防空炮停 **0620**——bismarck2.htm
- **生还 3 人**：见 §10

### 沉没后的调查（**Board of Enquiry 结论与争议**）
- **第一次委员会**（1941 年 6 月初）：「concluded that one or more shells from _Bismarck_ had managed to penetrate _Hood's_ armour/protective plating and detonate her aft magazines」；争议点：「**very few witnesses were called, and of the _Hood_ survivors, only William Dundas gave evidence. Verbatim records of the evidence were not made** and … the appropriate experts (on explosives, etc.) had not been called.」——https://www.hmshood.org.uk/history/denmarkstrait/bismarck3.htm
- **第二次委员会**（1941-08-27 起，主席 Rear-Admiral H.T.C. "Hooky" Walker，本人曾任 _Hood_ 舰长）：「The second Board convened on **27th August 1941**」；结论同上「A salvo from _Bismarck_ penetrated _Hood's_ vitals and detonated the aft magazines.」——同上
- 取证规模：「We have taken evidence from a total of **176 eyewitnesses** … **71** from H.M.S. PRINCE OF WALES, **89** from H.M.S. NORFOLK, **14** from H.M.S. SUFFOLK and **2** from H.M.S. HOOD.」——https://www.hmshood.org.uk/reference/official/adm116/adm116-4351_89to144.htm
- 报告日期与签署：「12TH September, 1941」；「L.D. Macintosh CAPTAIN / R.D.Duke CAPTAIN / **H.T.C.Walker REAR ADMIRAL**」——同上
- **免责结论**：「I do not think that there is much doubt that the HOOD was lost as the result of the **explosion of the after magazines** and that **no blame attaches** to the Vice-Admiral Commanding the Squadron, the Captain or anyone else.」「It was known that **HOOD's protection was poor by modern standards** and had it not been for the war she would by now have been undergoing complete reconstruction.」——同上
- **击穿路径的技术结论**（委员会采纳的专家意见，第 (11)-(14) 条）：
  - 「_Bismarck's_ shells probably had a muzzle velocity between **2721 and 3150 feet per second**」
  - 「If the muzzle velocity was more than about **3050 fps** a shell could have penetrated _Hood's_ **12-inch belt** and have got at a vital area」
  - 「If it was as low as 2721 … there is a strip on the ship's side about **18 inches deep and 42 feet long** where the shell could enter and pass over the top of the 12-inch belt and yet get under the flat portion of the protective main deck. With a fuse delay of about **55 feet** it could explode in a vital part.」
  - 「There is a zone a few feet wide the length of the magazine group where a shell could fall short of the ship and enter the ship **below the armoured belt**.」
  - 来源同上
- **DNC 附录结论**（第 112 页）：「The principal lesson of the loss of H.M.S. "HOOD" is that the **magazines of a warship should be so situated and protected** … It was intended to **reconstruct "HOOD" in this way after "QUEEN ELIZABETH" was completed, but the outbreak of war prevented this.**」——同上
- **德方（战俘 von Müllenheim-Rechberg）**：「"HOOD" blew up on **"BISMARCK'S" fifth salvo** and cost Germany **forty shells** in all.」「"BISMARCK" hit with her second salvo and again with her third」「The gunnery of "HOOD" has been described … as **exceptionally good**.」——同上
- **幸存者证词要点**：
  - Tilburn：第一火源起于舯部 UP 附近，「My idea was the U.P. ammunition had caught fire」；「Only "A" and "B" turrets」开火（委员会注记为「it is doubtful if he is correct」）——https://www.hmshood.org.uk/reference/official/adm116/adm116-4351_Hood.htm
  - Briggs：SGO 报「She has hit us on the boat deck and there is a fire in the ready use lockers」，Holland 答「leave it until the ammunition had gone」；「we were doing **29 knots**」——同上
  - PoW 舰长 Leach：「There was a very fierce upward rush of flame the shape of a funnel」——https://www.hmshood.org.uk/reference/official/adm116/adm116-4351_POW.htm
  - PoW 导航官 Rowell：命中后「the Vice-Admiral hoisted a second signal for another turn of 20 deg. away but before it could be executed the "Hood" was hit by another salvo」——同上

### 残骸
- 「In **July 2001**, a team led by **David L Mearns** located _Hood's_ wreck approximately **9,200 feet** below the surface of the Denmark Strait.」——https://www.hmshood.org.uk/history/denmarkstrait/bismarck3.htm
- 状态：「not only was the stern detached, but the bow … was separated from the main hull as well.」——同上
- 舰钟：2012 年首次尝试失败，**2015 年 8 月**成功，现藏 National Museum of the Royal Navy——同上

---

## 13. 与俾斯麦号的数据对照

> 两舰数据均取自各自权威站，口径已在备注列标出。

| 项目 | HMS Hood（胡德） | 来源 | Bismarck（俾斯麦） | 来源 | 备注 |
|---|---|---|---|---|---|
| 主炮口径 | 15 in / 38.1 cm（381 mm），42 倍径 | maingun.htm | 38 cm / 380 mm，L/52 | kb-armament | — |
| 主炮门数 | 8 门（4 × 双联 Mk II） | maingun.htm | 8 门（4 × 双联 SK C/34） | kb-armament | 同为 8 门 |
| 弹重 | 1,920 lbs / 870.9 kg | maingun.htm | 800 kg / 1,764 lbs | kb-armament | 德弹略轻 |
| 初速 | 2,462 fps / 750 m/s | maingun.htm | 820 m/s / 2,690 fps | kb-armament | — |
| 最大射程 | 30,180 yds / 27,596 m（30°） | maingun.htm | 35,550 m / 38,880 yds（30°） | kb-armament | 德炮远约 8 km |
| 射速 | 每门 4 发/分（每座） | maingun.htm | 2.4+ 发/分/门 | kb-armament | — |
| 炮塔座重 | 880 t（Mark II） | NWBR_15-42 | 1,056 t | kb-armament | — |
| 排水量 | 1920：41,125 t（light）/ 46,680 t（deep）；1939：42,752 / 48,650 t | displacement.gif | 40,250 / 43,978 / 47,870 / 51,760 / 53,486 t（空/标准/建造/满载/最大） | kb-genedata | 口径不同，勿直接比 |
| 全长 | 262.3 m | dimensions.gif | 250.50 m | kb-genedata | — |
| 舰宽 | 32 m（含护舷）/ 31.7 m（鼓包） | dimensions.gif | 36.00 m | kb-genedata | — |
| 吃水 | 8.6 m（light）～10.1 m（deep, 1939） | displacement.gif | 9.33 m（标准）/ 10.55 m（最大） | kb-genedata | — |
| 动力 | 144,000 shp 设计 / 151,000 shp 实测 | construction.htm | 150,170 hp（实测最大） | kb-genedata | — |
| 航速 | 32.07 kn（1920 实测）；28.8 kn（1941） | hoodspecs4 | 30.12 kn（实测最大） | kb-genedata | 1941 年胡德已落后 |
| 主装甲带 | 305 mm（12 in），倾角 12° | hoodspecs2 / navypedia | 320 mm KC，倾角 17°/10°/7°/8-10° | kb-proteccioni | 厚度接近，倾角德舰更优 |
| 装甲甲板 | 主甲板 76 mm（弹库上方）+ 51 mm 斜面 | navypedia | 装甲甲板 80-100 mm + 斜面 110-120 mm | kb-proteccioni | — |
| 装甲总重 | 13,800 t（约 30.9%，本报告换算） | pamphlet30s | 19,082 t（约 40%） | kb-proteccioni | 占比差约 9 个点 |
| 水密段 | 未获取 | — | 22 段（17 段在 citadel 内） | kb-proteccioni | 胡德关键缺项 |
| 续航 | 4,500 nm @20 kn | hoodspecs4 | 9,280 nm @16 kn | kb-genedata | — |
| 编制 | 1,418（1941-05-24） | hoodspecs6 | 2,200+ | kb-genedata | — |
| 服役年份 | 1920-03-29 | timeline2 | 1940-08-24 | kb-genedata | 相差 20 年 |
| 造价 | £6,025,000（币值年份未获取） | hoodspecs7 | RM 196.8 million（1938 年币值） | kb-genedata | 不可直接折算 |
| 结局 | 1941-05-24 06:00 爆炸沉没，3 人生还 | timeline4 / ADM116 | 1941-05-27 约 10:39 沉没，115 人生还 | bismarck3 | — |

**定性引语（可直接用于战役条目）**：
- 「Although listed as 35,000 tons to ensure that she fell within the limits of the London Naval Treaty, _Bismarck_ did, in fact, displace well over that.」「_Bismarck_ was a modern battleship in the truest sense. Her critical spaces were well protected by excellent internal compartmentalisation and high quality heavy armour.」——https://www.hmshood.org.uk/history/denmarkstrait/bismarck1.htm
- 「_Hood_ was well-built for her day (1920)… at 29 knots, she was still fast for her size.」「Hood, though old and in need of update, was hardly the "weak" and "totally outdated" ship with "thin deck armour" that legend has made her out to be.」——同上
- 「She still had mostly adequate protection, but also had a great deal of open spaces and a lack of compartmentilzation」——同上

---

## 14. 抓取失败清单

| URL | HTTP / 状态 | 失败原因 | 是否已放弃 |
|---|---|---|---|
| 全部 `https://www.hmshood.org.uk/*`（curl 直连或经 127.0.0.1:7897 代理） | 403 | Cloudflare「Sorry, you have been blocked」拦截页；含图片 `dimensions.gif` 同样 403 | 是（改用 web_fetch 成功） |
| `https://www.hmshood.org.uk/ship/dimensions.gif`、`displacement.gif`（curl 带 Referer） | 000 / 4575 B HTML | 返回拦截页而非图片 | 是（改用 Wayback `id_` 接口 200 成功） |
| `https://www.hmshood.org.uk/ship/displacement2.jpg`（Wayback） | 404（4624 B 404 页） | Wayback 无该文件快照 | 是 |
| `https://www.hmshood.org.uk/history/construct/index.htm` | 200 | 页面内容为站内「Access Forbidden」+ `/images/noaccess.jpg`，无正文 | 是 |
| `https://www.hmshood.org.uk/history/construct/name.htm` | 404 | 页面不存在 | 是 |
| `https://www.hmshood.org.uk/crew/complement/complement.htm` | 404 | 页面不存在（正确路径为 `/crew/complement/index.htm`） | 是 |
| `https://www.hmshood.org.uk/history/construct/refits.htm` | 200 | 三节正文均为「Pending research/under construction」，无改装清单 | 是（已改用分散来源逐条拼） |
| `https://www.kbismarck.com/techn.html` | 200（自定义 404 页） | 站点自带「PAGE CAN NOT BE FOUND」页 | 是 |
| `https://www.kbismarck.com/denmark-strait.html` | 200（自定义 404 页） | 同上 | 是 |
| `https://www.kbismarck.com/genedata.html`、`/armament.html`（web_fetch） | 200 但正文被丢弃 | 工具返回「[HTML content omitted: unable to convert safely.]」 | 是（改用 curl -x 7897 + python 去标签） |
| `https://dreadnoughtproject.org/tfs/index.php/H.M.S._Hood_(1918)` | 200 | Cloudflare 人机验证页（「请稍候…正在进行安全验证」），无内容 | 是 |
| `http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.202.317&rep=rep1&type=pdf`（SNAME 残骸取证报告 PDF） | 200 / 31 B | 返回 31 字节，非 PDF | 是 |
| navweaps 直连（无代理） | 000 | 连接超时/被阻断 | 是（必须 `curl -x http://127.0.0.1:7897 -sL`） |
| web_search（exa 引擎）检索「Hood cadets 1941」「Hood crew boys 1941」 | — | 返回词典/股票/无关结果，未获得任何 cadet 相关原文 | 是（改用本站 Roll of Honour 名册逐级核实） |

---

## 15. 来源 → URL 对照表

| 缩写 | 完整 URL | 需代理 |
|---|---|---|
| FAQ | https://www.hmshood.org.uk/admin/faq.htm | 是（curl 403；web_fetch 可用） |
| HS1 | https://www.hmshood.org.uk/ship/hoodspecs1.htm | 是 |
| HS2 | https://www.hmshood.org.uk/ship/hoodspecs2.htm | 是 |
| HS3 | https://www.hmshood.org.uk/ship/hoodspecs3.htm | 是 |
| HS4 | https://www.hmshood.org.uk/ship/hoodspecs4.htm | 是 |
| HS5 | https://www.hmshood.org.uk/ship/hoodspecs5.htm | 是 |
| HS6 | https://www.hmshood.org.uk/ship/hoodspecs6.htm | 是 |
| HS7 | https://www.hmshood.org.uk/ship/hoodspecs7.htm | 是 |
| HMG | https://www.hmshood.org.uk/ship/maingun.htm | 是 |
| HSEC | https://www.hmshood.org.uk/ship/secondary.htm | 是 |
| HAAA | https://www.hmshood.org.uk/ship/aaa.htm | 是 |
| HTORP | https://www.hmshood.org.uk/ship/torpedo.htm | 是 |
| HFC | https://www.hmshood.org.uk/ship/fire_control.htm | 是 |
| HRAD | https://www.hmshood.org.uk/ship/radar.htm | 是 |
| HOTH | https://www.hmshood.org.uk/ship/other.htm | 是 |
| HPAM | https://www.hmshood.org.uk/ship/pamphlet30s.htm | 是 |
| WB-DIM | https://www.hmshood.org.uk/ship/dimensions.gif（Wayback：http://web.archive.org/web/2010id_/http://www.hmshood.org.uk/ship/dimensions.gif） | 是（Wayback 亦需代理） |
| WB-DISP | https://www.hmshood.org.uk/ship/displacement.gif（Wayback：http://web.archive.org/web/2010id_/…/displacement.gif） | 是 |
| CON | https://www.hmshood.org.uk/history/construct/construction.htm | 是 |
| DES | https://www.hmshood.org.uk/history/construct/design.htm | 是 |
| LAU | https://www.hmshood.org.uk/history/construct/launch.htm | 是 |
| REF | https://www.hmshood.org.uk/history/construct/refits.htm | 是 |
| HT1 | https://www.hmshood.org.uk/history/timeline1.htm | 是 |
| HT2 | https://www.hmshood.org.uk/history/timeline2.htm | 是 |
| HT3 | https://www.hmshood.org.uk/history/timeline3.htm | 是 |
| HT4 | https://www.hmshood.org.uk/history/timeline4.htm | 是 |
| DC1 | https://www.hmshood.org.uk/history/denmarkstrait/bismarck1.htm | 是 |
| DC2 | https://www.hmshood.org.uk/history/denmarkstrait/bismarck2.htm | 是 |
| DC3 | https://www.hmshood.org.uk/history/denmarkstrait/bismarck3.htm | 是 |
| ADM89 | https://www.hmshood.org.uk/reference/official/adm116/adm116-4351_89to144.htm | 是 |
| ADMHOOD | https://www.hmshood.org.uk/reference/official/adm116/adm116-4351_Hood.htm | 是 |
| ADMPOW | https://www.hmshood.org.uk/reference/official/adm116/adm116-4351_POW.htm | 是 |
| PAINT | https://www.hmshood.org.uk/hoodtoday/models/tips/hoodpaint.htm | 是 |
| COMP40 | https://www.hmshood.org.uk/crew/complement/complement40.htm | 是 |
| ROH | https://www.hmshood.org.uk/crew/database/roh.php | 是 |
| ROHRANK | https://www.hmshood.org.uk/crew/database/ROHRankList.php | 是 |
| ROHMID | https://www.hmshood.org.uk/crew/database/ROHRankRating.php?RankRating=Midshipman | 是 |
| ROHPTM | https://www.hmshood.org.uk/crew/database/ROHRankRating.php?RankRating=Probationary%20Temporary%20Midshipman | 是 |
| NAAFI | https://www.hmshood.org.uk/crew/naafimen.htm | 是 |
| NP | https://www.navypedia.org/ships/uk/brit_bb1_hood.htm | 否（https 版 web_fetch 可直取） |
| NW15 | https://www.navweaps.com/Weapons/WNBR_15-42_mk1.php | 是（必须代理 + `-L`） |
| NW4 | https://www.navweaps.com/Weapons/WNBR_4-45_mk16.php | 是 |
| NW55 | https://www.navweaps.com/Weapons/WNBR_55-50_mk1.php | 是 |
| KBG | https://www.kbismarck.com/genedata.html | 是（web_fetch 会丢正文，需 curl + python 去标签） |
| KBP | https://www.kbismarck.com/proteccioni.html | 是 |
| KBA | https://www.kbismarck.com/armament.html | 是 |
| NAVHIST | https://www.naval-history.net/OWShips-WW1-02-HMS_Hood.htm | 否 |

---

## 16. 未获取字段汇总（便于后续补）

- 方形系数、水线面积、水密段数
- 标准排水量 / 满载排水量的**数值**（来源只给 Light / Deep）
- 蒸汽温度、汽轮机厂家、发电机总功率、电动机总功率
- Hood 装甲钢型号
- 装甲总重的官方占比（仅有 13,800 t 与 44,600 t 两个可算式）
- 第二座主炮指挥仪的存在与位置
- 沉没点的独立坐标（只有战斗海域 63-20 N / 31-50 W）
- 造价所对应的币值年份
- 1929–1931 大改装中的「换锅炉」「加防雷鼓包」原始出处（Association 该页未建成）
