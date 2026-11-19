# 赤城（Akagi）技术数据档案

> 采集对象：日本海军航空母舰「赤城」
> 采集日期：2026-11-19
> 编制规则：每条数值附原文照抄 + 来源 URL。查不到写「未获取」。不推算、不跨来源拼凑、不按同级舰类推。
> 来源分级：A=一手档案 / B=同期官方出版物 / C=权威二次文献 / D=专题网站 / E=百科

---

## 采集方法与前置说明

**代理情况**：任务书指定的代理 `http://127.0.0.1:7897` **不通**（`无法连接到远程服务器`），全程直连。

**检索路径**：`combinedfleet.com/Akagi.htm`（TROM）→ 日文 Wikipedia → Navypedia → NavWeaps（20cm/12cm/25mm）→ japanese-warship.com（日文专题，引光人社/潮書房一手文献）→ JACAR 目录 → USSBS 第 4 号审问记录（青木泰二郎舰长，A 级一手证言）→ kasado.net / rikukaigun.org(Nishida) / ikaduchi.com / waterline.fanweb.jp。

**关于「原文照抄」的说明**：本档案的「口径词」（基準排水量 / 公試排水量 / 満載排水量 / standard / full / deep load）**一律照抄来源用语，不做英制-公制口径折算**。赤城的排水量数据在来源间存在口径互斥，见 §15。

---

## §0 身份

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 原名 | 赤城（あかぎ） | 「赤城（あかぎ）は、大日本帝国海軍の航空母艦」 | S3 |
| 中文名 | 赤城 | —（中文译名，无原文） | — |
| 英文名 | Akagi | 「Named AKAGI ("Red Castle" - after AKAGI-yama, a mountain in Gunma Prefecture)」 | S1 |
| 舰种 | aircraft_carrier | 「種別 航空母艦」 | S3 |
| 所属国家 | japan | 「運用者 大日本帝国海軍」 | S3 |
| 所属海军 | 大日本帝国海軍（Imperial Japanese Navy） | 「was an aircraft carrier built for the Imperial Japanese Navy (IJN)」 | S2 |
| **旗号** | **未获取（且疑为不适用）** | 见下方纠错说明 | — |
| 命名来源 | 群马县赤城山 | 「赤城の艦名は群馬県前橋市の赤城山にちなんで命名された」 | S3 |
| 建造计划 | 八八舰队计划（八四舰队计划起案） | 「軍艦赤城は、八八艦隊計画により天城型巡洋戦艦の2番艦として呉海軍工廠で建造が始まった」 | S3 |
| 时代 | ww2 | 「In service 1927–1942」 | S2 |

**纠错 ①：「旗号」字段对日本海军不适用。**
日本海军不像英美海军那样给军舰编舷号/旗号（pennant number）。日文 Wikipedia 全条目检索「旗号」「信号符字」**均 0 命中**，各来源的舰船识别栏位是「艦艇類別等級」而不是旗号：

> 「艦艇類別等級別表中巡洋戰艦ノ欄「霧島」ノ次ニ「、天城、赤城」ヲ…加フ」（大正八年七月十七日 海軍大臣加藤友三郎）
> — 出处转引自日文 Wikipedia 脚注引「達大正8年7月 p.6」，URL: https://ja.wikipedia.org/wiki/赤城_(空母)

赤城在日方档案里的识别是**舰名 + 舰艇类别等级**，中途岛期的航空队识别是**着艦識別文字「ア」**（见 §10）。建议本站把「旗号」字段对日本海军舰统一置空或改为「着艦識別文字」。

---

## §1 建造

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 建造厂 | 呉海軍工廠（Kure Naval Arsenal） | 「建造所 呉海軍工廠」 | S3 |
| 建造地 | 広島県呉（Kure, Hiroshima） | 「Kure. Laid down as a battlecruiser - as second warship of AMAGI class - in Kure Naval Yard.」 | S1 |
| **船台号** | **未获取** | 各来源均只写「呉海軍工廠」，无船台编号 | — |
| 订货日期 | 1920 年（八八舰队计划下） | 「Ordered 1920」 | S2 |
| 开工 | 1920-12-06 | 「起工 1920年12月6日」 | S3 |
| 下水 | 1925-04-22 | 「進水 1925年4月22日」 | S3 |
| 服役（竣工） | 1927-03-25 | 「竣工 1927年3月25日」 | S3 |
| 结局日期 | 1942-06-05（当地日期；日本时间 6 月 6 日） | 「0520 AKAGI lay over to starboard and sank tail first after two or three torpedo hits out of four fired into her starboard side…」（5 June 1942 local West Longitude date） | S1 |
| 结局型式 | scuttled（己方驱逐舰雷击处分） | 「1942年6月6日雷撃処分」／「She was sunk by a Japanese destroyer's torpedoes during the next morning.」 | S3 / S7 |

**补充原文（改装开工与竣工）：**
> 「1923年11月19日 航空母艦に改造することと爲り、昭和2年3月25日竣工」 — S3
> 「Construction of Akagi as an aircraft carrier began on 19 November 1923.」 — S2
> 「1938年8月31日 - 改装工事終了。12月15日 - 現役艦に復帰。」 — S3

**纠错 ②：竣工日期与「实际完成」有 4 个月差。**
> 「ただし紙の上では竣工した【赤城】も、実際は予算不足で残工事が多くあり、公試開始が5月、試験終了が7月末だったことから、実際に完成したのはさらに4ヶ月後でした。」 — S6

---

## §2 主尺度

### §2-A 改装前（1927 竣工时 ~ 1935-10 进坞前）

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 全长 | 261.21 m | 「857 ft 0 in (261.21 m)」 | S3 |
| 水线长 | 248.95 m | 「816 ft 9 in (248.95 m)」 | S3 |
| 垂线间长 | 234.70 m | 「770 ft 0 in (234.70 m)」 | S3 |
| 水线宽 | 28.96 m | 「95 ft 0 in (28.96 m)」 | S3 |
| 最大宽 | 33.53 m（另一说水下最大宽 31.10 m） | 「最大幅 110 ft 0 in (33.53 m)または水線下最大幅 102.05 ft 0 in (31.10 m)」 | S3 |
| 平均吃水 | 8.08 m | 「吃水 26 ft 6 in (8.08 m)」 | S3 |
| 最大吃水 | **未获取** | 各来源只给单一吃水值，无平均/最大之分 | — |

> Navypedia（S4）同口径但用 pp/wl/oa 标注，可交叉印证：
> 「Length, m \| 235.0 pp 249.0 wl 260.7 oa」「Breadth, m \| 29.0」「Draught, m \| 8.07」

### §2-B 改装后（1938-08-31 完成后 ~ 1942-06 战没）

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 全长 | 260.67 m | 「全長 260.67m」 | S3 |
| 水线长 | 250.36 m | 「水線長 250.36m」 | S3 |
| 垂线间长 | 234.70 m（Navypedia 记 235.0） | 「235.0 pp 250.4 wl 260.7 oa」 | S4 |
| 水线宽 | 31.32 m | 「水線幅 31.32m」 | S3 |
| 最大宽 | 33.5 m（另一说 31.32 m） | 「最大幅 33.5m」（S5）／「水線幅 31.32m」（S3） | S5 / S3 |
| 平均吃水 | 8.71 m | 「吃水 8.71m」 | S3 |
| 最大吃水 | **未获取** | — | — |

> 「bulges were fitted, which have raised a hull breadth from 29 to 31.3m」 — S4（鼓包改装是宽度的来源）

**注意**：日文 Wikipedia 给改装后的「深さ 28.65m(飛行甲板まで)」，Navypedia 无对应项。这两项**不是**吃水，不可混用。

---

## §3 排水量

> **口径警告**：本节所有数字照抄来源用的是哪个词。「基準排水量」对应英文 standard displacement，「公試排水量」是日本海军特有的试航状态排水量（约相当于满载减一部分），「満載」对应 full load。三个口径**不可互相换算**。

### §3-A 改装前

| 口径 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 基准/标准排水量 | 26,900 英吨 | 「基準排水量 26,900英トン」 | S3 |
| 满载排水量 | 34,364 英吨 | 「公試排水量 34,364英トン」→ 见下注 | S3 |
| 公试排水量 | 34,364 英吨 | 「公試排水量 34,364英トン」 | S3 |
| 深载排水量 | **未获取** | — | — |

**口径分歧**：Navypedia 把 34,364 标为 **full**：
> 「Displacement full, t \| 34364」 — S4

而日文 Wikipedia 与 japanese-warship 都标为 **公試排水量**：
> 「公試排水量① 　34,364t」 — S5

即同一数字在英文源被称作 full load、在日文源被称作公试排水量。**不裁决，见 §15。**

### §3-B 改装后

| 口径 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 基准/标准排水量 | 36,500 英吨 | 「基準排水量 36,500英トン」 | S3 |
| 公试排水量 | 41,300 吨 | 「公試排水量 41,300トン」 | S3 |
| 满载排水量 | 42,750 t | 「満載 42,750t」 | S10（Nishida）／S5 |
| 深载排水量 | 41,300 long tons（英文源如此标注） | 「41,300 long tons (42,000 t) (deep load)」 | S2 |

**口径分歧（重要）**：同一个 41,300 —
- 日文源叫 **公試排水量**：「公試排水量 41,300トン」 — S3 / S5 / S10
- 英文源叫 **deep load**：「41,300 long tons (42,000 t) (deep load)」 — S2

**另见 §15 纠错 ③：Combinedfleet 的 37,100 标准排水量。**

---

## §4 动力

| 字段 | 值（改装前） | 值（改装后） | 原文照抄 | 来源 |
|---|---|---|---|---|
| 动力型式 | 技本式齿轮传动蒸汽轮机 | 同左 | 「4 sets Gihon geared steam turbines」 | S4 |
| 轴数 | 4 轴 | 4 轴 | 「推進 4軸」 | S3 |
| 锅炉数与型号 | ロ号艦本式専焼缶 11 基 + 混焼缶 8 基 | ロ号艦本式専焼缶 大型 11 基 + 小型 8 基 | 「主缶 ロ号艦本式専焼缶11基／同混焼缶8基」→「ロ号艦本式専焼缶 大型11基／同小型8基」 | S3 |
| 主机数与型号 | 技本式汽轮机（高低压 2 组）4 基 | 同左 | 「主機 技本式タービン(高低圧 2組)4基」 | S3 |
| 设计功率 | 131,200 hp | 133,000 hp | 「出力 131,200hp」／「133,000hp」 | S3 |
| **试航实测功率** | **未获取** | **未获取** | 各来源只给 131,200 / 133,000 的「出力」，未标明是否为实测 | — |
| 设计航速 | 计划 31.0 节 | 31.2 节 | 「速力 計画 31.0ノット」／「31.2ノット」 | S3 |
| 试航实测航速 | 32.5 节（1927-06-17） | 31.2 节（公试） | 「Achieves a speed record of 32.5-knots during her trials.」 | S1 / S3 |
| 续航力 | 8,000 海里 / 14 节 | 8,200 海里 / 16 节 | 「航続距離 8,000カイリ / 14ノット」→「8,200カイリ / 16ノット」 | S3 |
| 燃油装载量 | 重油 3,900 英吨 + 石炭 2,100 英吨 | 重油 5,770 t（或 5,775 t，1938-03） | 「燃料 重油 3,900英トン／石炭 2,100英トン」→「重油 5,770トン または5,775トン(1938年3月)」 | S3 |

> 「She carried 3,900 long tons (4,000 t) of fuel oil and 2,100 long tons (2,100 t) of coal that gave her a range of 8,000 nautical miles (15,000 km; 9,200 mi) at 14 knots」 — S2
> 「Her bunkerage was increased to 7,500 long tons (7,600 t) of fuel oil which increased her endurance to 10,000 nautical miles (18,520 km; 11,510 mi) at 16 knots」 — S2

**续航力分歧**：改装后英文源说 10,000 海里/16 节、燃油 7,500 长吨；日文源说 8,200 海里/16 节、燃油 5,770 吨。见 §15。

---

## §5 防护

**结论：赤城作为战巡改装航母，防护是明确的弱项，且改装后几乎没有加强。**

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 装甲体系 | 非 all-or-nothing，沿用战巡的「舷侧装甲带 + 装甲甲板 + 倾斜连接」局部防御 | 「Main 152mm belt closed about 2.3 of hull length and was inclined at 14°from vertical. Flat main (lower hangar) 79-57mm (51-32mm armor on 28-25mm plating) deck connected with its upper edge but had additional 102mm slopes connected with lower edge of main belt.」 | S4 |
| 舷侧装甲厚度 | 152 mm（倾斜 14°）；日文源记「5インチVC鋼(傾斜12度)」 | 「Amour, mm \| belt: 152」／「舷側：5インチVC鋼(傾斜12度)」 | S4 / S3 |
| 甲板装甲厚度 | 79 mm 水平部 + 102 mm 舷侧倾斜部 | 「装甲甲板装甲 水平部:79mm 外舷傾斜部:102mm」 | S10 |
| 弹药库装甲 | **未获取**（无任何来源单独给弹药库装甲值） | — | — |
| 水下防护纵深 | 有纵向防雷纵壁 76–16 mm；改装加鼓包使水下防护深度增加 1.2 m | 「There was 76-16mm longitudinal anti-torpedo bulkhead.」／「Depth of underwater protection was increased at 1.2m by bulges」 | S4 |
| **装甲总重** | **未获取** | 检索日文 Wikipedia「装甲」「重量」、japanese-warship 防御章、Navypedia 防护章，均无装甲总吨位 | — |

**防护设计原委（原文）**：
> 「防御に関する内容はかなり薄いですが、基準となったのは重巡の砲撃、すなわち20cm砲弾です。戦艦の防御力をそのまま維持するとあまりに過剰なので、254mmあった戦艦用のVC甲鈑を150mmまで再圧縮。」 — S6
> 「Akagi's waterline armored belt was reduced from 254 to 152 mm (10 to 6 in) and placed lower on the ship than originally designed. … Her deck armor was also reduced from 96 to 79 mm (3.8 to 3.1 in).」 — S2

**航空防御（真正的死因）**：
> 「Akagi's aviation fuel tanks were incorporated directly into the structure of the carrier, meaning that shocks to the ship, such as those caused by bomb or shell hits, would be transmitted directly to the tanks, resulting in cracks or leaks.」 — S2
> 「Futhermore, the carrier's hangar and flight decks carried little armor protection, and there was no redundancy in the ship's fire-extinguishing systems.」（原文拼写如此） — S2

> 飞行甲板装甲 / 格纳库甲板装甲：来源明确标「-」（无装甲）
> 「飛行甲板装甲 - ／格納庫甲板装甲 -」 — S10

**纠错 ④：赤城改装后没装海水灭火装置。**
> 「弯曲煙突を搭載した空母は、構造上海水を汲み上げる装置が必須となっています。…が、なんと【赤城】にはこの装置が搭載されていません。原因はよくわかっていませんが、恐らくこれも予算の関係でしょう。」 — S6

---

## §6 航空设施

### §6-A 飞行甲板（改装前，1927–1935，三段式）

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 上段（着舰+大型机起飞） | 190.20 m × 30.48 m | 「624 ft 0 in (190.20 m) x 100 ft 0 in (30.48 m) (上段)」 | S3 |
| 中段（小型机起飞） | 15 m × 约 25 m | 「中段:15.0m × 25.0m (375㎡)」／「her middle flight deck (beginning right in front of the bridge) was only 15 meters (49 ft 3 in) long」 | S10 / S2 |
| 下段（大型机起飞） | 55.02 m × 22.86 m | 「180 ft 6 in (55.02 m) x 75 ft 0 in (22.86 m) (下段)」 | S3 |
| 三段合计面积 | 7,276 m² | 「fd - 5,801+375+1100=7,276m²」 | S4 |

**注**：Navypedia（S4）把中段记为「18x~25m」，与日文源 15.0 m 不符。见 §15。

### §6-B 飞行甲板（改装后，1938–1942，单段全通）

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 长 | 249.17 m | 「Flight deck: 249.2x30.5m」／「飛行甲板 249.17m×30.48m」 | S4 / S3 |
| 宽 | 30.48 m | 同上 | S4 / S3 |
| 面积 | 7,601 m² | 「after modernization(fd - 7,601m²…)」 | S4 |
| 倾斜 | 舰首 0.5°、舰尾 1.5° | 「飛行甲板は中央部が水平で、艦首方向へ0.5度、艦尾方向へ1.5度の傾斜が付けられていた。」 | S3 |
| 到飞行甲板的高度 | 28.65 m | 「深さ 28.65m(飛行甲板まで)」 | S3 |

### §6-C 机库

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 层数（前） | 3 层（上/中/下，开放式为主） | 「Upper and medium hangars, each: ~100x22x5 m, small lower hangar: ~20x20x?m」 | S4 |
| 层数（后） | 3 层（上/中为全密闭，下为小型） | 「Upper and medium hangars, each: ~130x22x5m, small lower hangar: ~20x20x?m」 | S4 |
| 上/中格纳库（前） | 100 m × 22 m × 5 m | 「上段:100.0m × 22.0m × 5.0m／中段:100.0m × 22.0m × 5.0m」 | S10 |
| 上/中格纳库（后） | 130 m × 22 m × 5 m | 「上段:130.0m × 22.0m × 5.0m／中段:130.0m × 22.0m × 5.0m」 | S10 |
| 下格纳库 | 20 m × 20 m × 高度未获取 | 「下段:20.0m × 20.0m × N/A」 | S10 |

> 「As completed, the ship had two main hangar decks and a third auxiliary hangar, giving a total capacity of 60 aircraft. The third and lowest hangar deck was used only for storing disassembled aircraft.」 — S2
> 「The upper and middle hangar areas totaled about 80,375 square feet (7,467.1 m2), the lower hangar about 8,515 square feet (791.1 m2).」 — S2

### §6-D 升降机

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 数量（前） | 2 基 | 「エレベーター2基」 | S3 |
| 数量（后） | 3 基 | 「エレベーター3基」 | S3 |
| 前部（改装前） | 11.8 × 13.0 m，偏右舷 | 「Her forward aircraft lift was offset to starboard and 11.8 by 13 meters (38 ft 9 in × 42 ft 8 in)」 | S2 |
| 后部（全程） | 12.8 × 8.4 m，中线 | 「Her aft lift was on the centerline and 12.8 by 8.4 meters (42 ft 0 in × 27 ft 7 in).」 | S2 |
| 前部（改装后） | 11.8 × 16.0 m | 「Lifts: fore (11.8x16.0m)」 | S4 |
| 中部（改装后新增） | 11.8 × 13.0 m | 「medium (11.8x13.0m)」 | S4 |

> 「元の前方エレベーターとほぼ同じ場所から、中央に寄せた箇所に1番エレベーターが、甲板のほぼ中央に2番エレベーターが搭載されました。新設されたエレベーターは幅16m、縦11.8mと横長になったので運用面では楽になりました。」 — S6

### §6-E 拦阻索

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 数量（改装前初期） | 英制纵索式（Furious 同型），索数未获取 | 「Her arresting gear was an unsatisfactory British longitudinal system used on the carrier Furious that relied on friction between the arrester hook and the cables.」 | S2 |
| 数量（1931 改装后） | 横索式，6 索 | 「It was replaced during the ship's refit in 1931 with a Japanese-designed transverse cable system with six wires」 | S2 |
| 数量（改装后 1938） | 9 索（英文源）／10 索（日文源） | 「hydraulic Type 1 system with 9 wires」（S2）／「呉式四型 (4.0t / N/A):10索」（S10） | S2 / S10 |

### §6-F 弹射器

**无。** 本条属于「0」性质，来源明确。
> 「No catapults were fitted.」 — S2
> 「日本は結局空母にカタパルトを搭載することはできず、大型機の短距離発艦という夢は叶いませんでした。」 — S6

（另：改装时曾为安装 2 基弹射器做过配套工程，但未完成。见 §15 纠错 ⑤）

### §6-G 着舰标识与助降设备

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 着舰识别文字 | 「ア」 | 「着艦識別文字: ア」 | S3 |
| 着舰指导灯 | 有 | 「着艦指導燈というものが装備されました。…正しい着艦高度、着艦姿勢を取るための目印です。」 | S6 |
| 滑走制止装置（拦阻网） | 空技廠式三型，固定 3 基 + 移动式 2 基 + 应急 1 基 | 「【赤城】の滑走制止装置は、【加賀】が大改装後に換装したものと同じ空技廠式三型です。滑走装置は固定された3基のほか、移動式2基と応急用1基が備わっていたようです。」 | S6 |
| 甲板识别标识（中途岛时） | 飞行甲板前部画巨大日章旗 | 「珊瑚海海戦の戦訓から敵味方識別のため、日本空母の飛行甲板前部には巨大な日の丸が描かれていたが、これはアメリカ軍急降下爆撃隊にとって絶好の的となった」 | S3 |
| 遮风栅 | 前部升降机两侧各 1 处 | 「機体が飛ばされないように遮風柵が前部エレベーターを挟む形で2箇所設置されています」 | S6 |

---

## §7 武备

### §7-A 主炮：20cm/50 三年式

| 时期 | 配置 | 原文照抄 | 来源 |
|---|---|---|---|
| 设计时 | 连装 2 基 4 门 + 单装 6 基 6 门 = 10 门 | 「50口径20cm連装砲 2基4門／同単装砲 6門」 | S3 |
| **1927-03 竣工时** | **只有单装 6 门**（连装炮 1928 年末才装） | 「連装砲2基ですが、実は竣工時には搭載されていません。…連装砲が搭載されたのは昭和3年/1928年末の工事で」 | S6 |
| 1928 末 – 1935 | 10 门（连装 2 基在中段甲板两舷 + 单装 6 门在舰尾两舷炮廓） | 「中段甲板には両脇に連装砲が1基ずつ設置されました。…上限の残り6門は、戦艦の副砲のように片舷3門ずつ艦後部にケースメートに装備されました。」 | S6 |
| 1938 – 1942 | 单装 6 门（连装 2 基撤除） | 「20cm単装砲 6門」／「The two 20 cm gun turrets on the middle flight deck were removed」 | S3 / S2 |

**性能（NavWeaps，武器本体数据，非赤城专有）：**
> 「Muzzle Velocity \| All except Illum: 2,756 fps (840 mps)」「Ammunition stowage per gun \| 120 - 126 rounds」 — S8

**纠错 ⑥：1927 年竣工时只有 6 门 20cm 单装炮，不是单装 + 连装 10 门。** 任务书此处若按 10 门记则与原文冲突。

**主炮在实战中的问题（原文）：**
> 「甲板のほぼ真下にある主砲は、発射時の衝撃が甲板の裏側から突き上げてきます。…このため撃っているうちに甲板がめくれ上がる始末で、存在意義をかき消すものでした。」 — S6
> 「ミッドウェー海戦で赤城は20cm砲を最低54発発射しているが、飛行甲板への影響については不明である。」 — S3

### §7-B 高角炮：12cm/45 十年式

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 型号 | 45口径 12cm 十年式連装高角砲 | 「12cm連装高角砲 6基12門」 | S3 |
| 数量 | 6 基 12 门（改装前后不变） | 「45口径12cm連装高角砲 6基12門」（改装前后两栏相同） | S3 |
| 换装 12.7cm？ | **从未换装** | 「Akagi carried them to her end at Midway.」（NavWeaps 论 12cm 十年式） | S8b |

> 「The carrier Kaga and those cruisers modernized during the late 1930s had these weapons replaced by the 12.7 cm/40 (5") Type 89 AA gun. However, Akagi carried them to her end at Midway.」 — S8b
> 「高角砲は、これもまた金がねぇってことで、最新の八九式40口径12.7cm高角砲に換装されることはなく、十年式45口径12cm高角砲のままでした。」 — S6

**火力死角（原文）：**
> 「シールドのない裸の高角砲も同様の配置なのは無策が過ぎます。…逆側に対しては全く砲撃ができないため、これでは対空火力が常に最大スペックの半分しか出せないのと同じです。」 — S6

### §7-C 25mm 高炮（九六式 60口径）

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| **总管数** | **28 门** | 「25mm連装機銃 14基28門」 | S3 |
| **联装座数** | **14 座，全部为连装（双联）** | 「14 × twin 25 mm (1 in) AA guns」 | S2 |
| 单装座数 | 0（战时未加装 25mm 单装） | 「改装後に増備された単装機銃はなんと7.7mm」 | S6 |
| 三联装座数 | 0 | 无来源给出三联装，日文/英文源均只列连装 14 基 | — |
| 装备时点 | 1938 改装完成时，替换原有的 13mm 连装机枪 | 「機銃はさすがに海軍おなじみの25mm連装機銃が14基搭載され（竣工後搭載された13mm連装機銃からの換装）」 | S6 |

**武器本体数据（NavWeaps，非赤城专有）：**
> 「Rate Of Fire 2 \| Cyclic: 200 - 260 rounds per minute, 220 standard 3」「Effective: 110 - 120 rounds per minute」 — S9
> 「Ammunition stowage per gun \| 2,000 rounds」 — S9
> 「Originally issued in twin mountings, triple mounts were introduced in 1941 and single mounts in 1943.」 — S9

### §7-D 机枪

| 时期 | 型号与数量 | 原文照抄 | 来源 |
|---|---|---|---|
| 竣工时 | 无（另有 Navypedia 记 22 挺 6.5mm，存疑） | 「22 x 1 - 6.5/115」 | S4 |
| 1931-03 | 留式 7.7mm 机枪 2 挺 | 「竣工時には機銃は搭載されておらず、昭和6年/1931年3月の段階では留式7.7mm機銃が2挺だけ追加されています」 | S6 |
| 竣工后某期 | 13mm 连装机枪（后被 25mm 换装） | 「竣工後搭載された13mm連装機銃」 | S6 |
| 1938 后 | 7.7mm 单装机枪（新增） | 「大改装後も25mmの他に未だに7.7mmが増備されており、対空火力は貧弱そのものです」 | S6 |

**13mm 机枪的精确数量：未获取。** 来源只说「13mm連装機銃」曾存在并被换装，未给座数。

### §7-E 弹药基数

| 层级 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 20cm 炮（每门） | 120–126 发 | 「Ammunition stowage per gun \| 120 - 126 rounds」 | S8 |
| 12cm 高角炮（每门） | 200–250 发 | 「Ammunition stowage per gun \| 200 - 250 rounds」 | S8b |
| 25mm 机炮（每门） | 2,000 发 | 「Ammunition stowage per gun \| 2,000 rounds」 | S9 |
| **全舰弹药基数（各口径总携行量）** | **未获取** | 无任何来源给出赤城全舰弹药总基数 | — |

> 上述为**火炮本身的弹药架容量（per gun）**，不是赤城全舰基数，二者不可混用。

---

## §8 雷达与火控

### §8-A 雷达

**结论：赤城在中途岛时没有雷达。这是「0」，不是「未获取」，有一手证言。**

> 「Q. Did you have radar on the Akagi?
> A. **No.**
> Q. Did any ships at MIDWAY have radar?
> A. Yamato, Mutsu and Nagato in the Grand Fleet may have had it. There was no ship at MIDWAY or carrier which had it.」
> — 青木泰二郎大佐（赤城舰长）USSBS 第 4 号审问，1945-10-09 — S7（A 级一手证言）

佐证（二手）：
> 「Although the Japanese battleships were fitted with radar, their carriers had none」 — S11（ETHW, Radar and the Fighter Directors 第 7 章）

日文 Wikipedia 全文检索「電探」**0 命中**，与上述一致。

| 字段 | 值 | 说明 |
|---|---|---|
| 雷达型号 | 无（0 部） | S7 一手证言 |
| 雷达数量 | 0 部 | 同上 |
| 雷达装舰时点 | 未装（赤城 1942-06 战没前从未装雷达） | S7 |

### §8-B 射击指挥仪

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 20cm 炮用 | 一四式方位盘 2 组 | 「一四式方位盤 (20.0cm砲用):2組」 | S10 |
| 12cm 高角炮用 | 九一式高射装置 2 组（一说 3 基） | 「九一式高射装置 (12.0cm砲用):2組」（S10）／「九一式高射装置が両舷と艦橋トップに計3基」（S6） | S10 / S6 |
| 25mm 用 | 九五式机铳射击装置 4 组（英文源作 6 组） | 「九五式機銃射撃装置 (25mm機銃用):4組」（S10）／「Six Type 95 directors were fitted」（S2） | S10 / S2 |
| 20cm 用（英文源口径） | Type 89 director 1 部 | 「Akagi carried one Type 89 director for the 20 cm (7.9 in) guns; it is uncertain how many were carried before then.」 | S2 |

### §8-C 测距仪

**未获取。**
检索路径：日文 Wikipedia 全文检索「測距」「測距儀」「方位盤」「射撃指揮」「九四式」「九一式」→ 除要目表外 **0 命中**；英文 Wikipedia 无测距仪条目；kasado.net 的「測距儀 / レーダー」栏只列射击指挥装置，测距仪栏未单列；Navypedia 无。**结论：赤城舰载测距仪型号与数量未获取。**

---

## §9 编制

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 平时编制（竣工时定员） | 1,400 名 | 「竣工時定員 1,400名」 | S3 |
| 平时编制（1931-03） | 1,297 名 | 「1931年3月 1,297名」／「定数乗員1,297人」 | S3 / S5 |
| 平时编制（1934-04） | 1,299 名 | 「1934年4月定員 1,299名」 | S3 |
| 平时编制（1937-04） | 1,627 名 | 「1937年4月定員 1,627名」 | S3 |
| 平时编制（1938-03） | 1,340 名 | 「1938年3月 1,340名」 | S3 |
| 最终时定员 | 1,630 名 | 「最終時 1,630名」 | S3 |
| **军官数** | **未获取** | 无来源给出赤城军官定员数 | — |
| **中途岛出击时实际搭载人数** | **未获取（来源明确说「不明」）** | 见下引 | S3 |

**关键原文（这是「未获取」而非「查漏」的铁证）：**
> 「ミッドウェー海戦時の赤城に乗り組んでいた実員は**不明**である。これはミッドウェー基地占領時、同島基地に進出するための基地要員や兵員が便乗していた為である。赤城の定員は1,630名、第一航空艦隊司令部員が64名で、准士官以上8名、下士官兵213名の計221名が戦死した」 — S3

即：定员 1,630 + 一航舰司令部 64，但**实际搭载数因有搭便船的基地要员而不可考**。战死者 221 名（准士官以上 8 + 下士官兵 213）。

**注意**：USSBS 青木证言说「out of a total complement of 1400」——这与日文源 1,630 冲突，且是战后回忆的约数。见 §15。

---

## §10 涂装与外形

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 涂装方案（全期） | 无迷彩；单色工厂灰（軍艦色），仅舰首局部有重新涂装记录 | 「セイロン沖海戦後の『海鷲武勲の蔭に』では、艦前部の塗装塗り替え…が記録されている」／「真珠湾攻撃に出撃する直前に赤城の外舷を塗装している模様を撮影したものがある」 | S3 |
| 舰体色（改装前 1927–1938） | 呉海軍工廠グレイ（建造厂为吴，归类为吴厂灰） | 「航空母艦 赤城[三段甲板以前]・蒼龍…」（列于「呉」工厂栏下） | S12 |
| 舰体色（改装后 1938–1942） | 佐世保海軍工廠グレイ（改装在佐世保实施） | 「航空母艦 赤城[近代化改装後]・加賀[近代化改装後]・天城…」（列于「佐世保」栏下） | S12 |
| 上层建筑色 | 同舰体色（无单独记录） | — | — |
| **甲板色** | **未获取** | 无来源给出飞行甲板具体色号/色名 | — |
| **舰岛位置** | **左舷（port side）** —— 全程唯一，见下 | 「An island superstructure is added on the ship's port side, an unusual arrangement which will be later shared by carrier HIRYU.」 | S1 |
| 识别标识（烟囱） | 改装前：右舷双烟囱（大者下弯向海面，小者向上）；改装后：右舷单一大弯烟囱向后下方 | 「Akagi was given two funnels on the starboard side. The larger, forward funnel was angled 30° below horizontal with its mouth facing the sea, and the smaller one exhausted vertically」 | S2 |
| 着舰识别文字 | 「ア」 | 「着艦識別文字: ア」 | S3 |
| 甲板识别标识 | 中途岛时飞行甲板前部巨大日章旗 | 见 §6-G | S3 |

### §10-A 舰岛位置 —— 重点确认

**改装前（1927–1938）：无岛式舰桥。**
> 「There was no island superstructure when the carrier was completed; the carrier was commanded from a space below the forward end of the upper flight deck.」 — S2
> 「No island is fitted, the ship being commanded from a space below the forward end of the upper flight deck.」 — S1

（注：完成数年后在飞行甲板**右舷**加装过小型航海舰桥，非岛式。见下引）

**改装后（1938–1942）：左舷岛式舰桥，且位置在舰体中央略前。**

> 「An island superstructure is added on the ship's port side, an unusual arrangement which will be later shared by carrier HIRYU. However, this experiment will not be continued on other future carriers.」 — S1
> 「The modernization added an island superstructure on the port side of the ship, which was an unusual arrangement; the only other carrier to share this feature was a contemporary, the Hiryū. The port side was chosen as an experiment to see if that side was better for flight operations by moving the island away from the ship's exhaust outlets.」 — S2
> 「左舷側艦橋を設けた日本空母は本艦と飛龍のみ。」 — S3
> 「赤城は左舷中央やや前方のレイアウトとなった。」 — S13

**为什么放左舷（原文，注意这与英美惯例相反）：**
> 「元巡洋戦艦の【赤城】は細長く、大きな煙突の近くに艦橋を置くと、流石に右舷側に重量が偏る危険がありました。艦橋を左舷に移せば煙突とのバランスが取りやすいですから、【赤城】ではこのような判断に至るのもやむを得ません。」 — S6

**实验结论（1938 年 10–11 月实测，451 架次）：**
> 「・風向正首ヨリナル場合ハ着艦ニ差支ナシ
> ・風向左舷5度迄ハ着艦容易ナリ
> ・風向右舷ノ場合ハ艦首ヨリ二度以上外ルレバ気流乱レ着艦困難トナル
> ・…夜間ノ着艦困難ナリ
> ・艦橋ハ極力舷外ニ張リ出スヲ要ス
> ・艦橋及煙突ハ極力同一舷トシ艦橋ノ位置ハ煙突ノ前方適当ノ位置ヲ可トス」 — S6（引自『日本空母物語』p.411）

即：左舷舰桥的实测结论是**负面**的，但改装已成事实，赤城至死未改。

**纠错 ⑦：任务书说「舰岛在左舷，与加贺（右舷）相反」—— 这句对的，但补一个细节：赤城三段甲板时代曾在飞行甲板右舷装过小型航海舰桥，来源是加贺移来的。**
> 「完成後数年で飛行甲板右舷に航海用の小型艦橋が設置された。これは、先に近代化改装工事に入った加賀で改装前に使用されていたものを移設したものである」 — S3

---

## §11 生涯时间线

| 日期 | 事件 | 原文照抄 | 来源 |
|---|---|---|---|
| 1920-12-06 | 作为天城型战巡 2 号舰在吴工厂开工 | 「Kure. Laid down as a battlecruiser - as second warship of AMAGI class - in Kure Naval Yard.」 | S1 |
| 1922-02-05 | 华盛顿条约，天城型两舰取消，选定改装为航母 | 「Both AMAGI class battlecruisers are canceled under the terms of the Washington Naval Treaty. …the incomplete battlecruisers AMAGI and AKAGI are selected.」 | S1 |
| 1923-09-01 | 关东大地震，天城号损毁，改装中止 | 「AMAGI … is heavily shaken by the quake that causes significant stress damage to her hull. …conversion work is abandoned.」 | S1 |
| 1923-11-19 | 赤城正式改为航空母舰（舰种变更） | 「軍備補充費ヲ以テ建造中ノ戰艦加賀及巡洋戰艦赤城ノ艦種ヲ航空母艦ニ改メラル 大正十二年十一月十九日」 | S3 |
| 1923-11-09 / 19 | 改装工事开始（吴工厂） | 「9 November 1923: Works on conversion to a carrier starts at Kure Naval Yard.」（S1）／「航空母艦に改造することと爲り」（S3，记 11-19） | S1 / S3 |
| 1925-04-22 | 下水，命名「赤城」 | 「Launched. Named AKAGI ("Red Castle" - after AKAGI-yama, a mountain in Gunma Prefecture).」 | S1 |
| 1927-03-25 | 竣工，三段式甲板，无岛式舰桥 | 「AKAGI like KAGA is completed with three superimposed flight decks」 | S1 |
| 1927-06-17 | 试航创 32.5 节纪录 | 「Achieves a speed record of 32.5-knots during her trials.」 | S1 |
| 1927-08-01 | 编入联合舰队，航空队 12 架 1MF3 + 24 架 B1M + 12 架 2MR | 「Her air group consists of 12 Mitsubishi Type 10 1MF3 (+4 spares) fighters, 24 (+4 spares) Mitsubishi Type 13 B1M attack planes and 12 Mitsubishi Type 10 2MR reconnaissance aircraft.」 | S1 |
| 1928-04-01 | 就任一航战旗舰 | 「Attached as flagship of Rear Admiral … Takahashi Sankichi's … newly formed CarDiv 1」 | S1 |
| 1928 末 | 中段甲板加装 20cm 连装炮 2 基 | 「連装砲が搭載されたのは昭和3年/1928年末の工事で」 | S6 |
| 1928-12-10 | 山本五十六就任舰长（至 1929-11-01） | 「山本五十六 大佐：1928年12月10日 - 1929年10月8日」 | S3 |
| 1931-12 / 1932-12 | 预备舰状态下的改装，拦阻索换为横索式 | 「Refit is completed. Her arresting gear is replaced with a transverse cabled system」 | S1 |
| 1934-03 | 友鹤事件，影响后续改装设计 | 「「友鶴事件」が発生したのは昭和9年/1934年3月」 | S6 |
| 1935-10-24 | 入佐世保工厂，开始大改装 | 「Sasebo. Enters docks at Sasebo Naval Yard for a general reconstruction」 | S1 |
| 1937-07 | 中日战争爆发（改装中） | 「この期間中の昭和12年/1937年7月から「日華事変」が始まっています。」 | S6 |
| 1938-08-31 | 改装完成，单段全通甲板 + 左舷岛式舰桥 | 「Modernization is completed; AKAGI emerges with the three flight decks removed.」 | S1 |
| 1938-10~11 | 左舷舰桥实船试验（451 架次） | 「延べ451回の発着艦を行い」 | S6 |
| 1938-12-15 | 复归现役，编入一航战 | 「Resumes active service and joins … CarDiv 1」 | S1 |
| 1939-01~02 | 参加海南岛攻略作战 | 「赤城の航空戦力は艦戦18、艦爆12、艦攻18であった」 | S3 |
| 1940-11-15 | 被列为特设舰（特務艦） | 「Reclassified as special duty ship」（原文作 special purpose ship） | S1 |
| 1941-04-10 | 第一航空舰队（机动部队）编成，赤城任旗舰 | 「1941年（昭和16年）4月、第一航空艦隊（長官は南雲忠一中将）が編制され」 | S3 |
| 1941-11-22 | 单冠湾集结完毕 | 「Arrives at Hittokappu Bay, Etorofu-To (Island)」 | S1 |
| 1941-11-26 | 出击，驶向夏威夷 | 「Departs … for the Kuriles」/「11月26日に単冠湾を出港し」 | S1 / S3 |
| 1941-12-07 | 珍珠港攻击（第一波 27 架舰攻 + 9 架零战；第二波 18 架舰爆 + 9 架零战） | 「AKAGI contributes 12 B5N2 "Kate" torpedo bombers and 15 B5N2 "Kate" each equipped with one 800-kg Type 99 model 5 bomb … and nine A6M2 "Zeke" fighters」 | S1 |
| 1941-12-07 | 珍珠港损失：零战 1、九九舰爆 4 | 「Losses sustained by AKAGI's aircraft are one "Zeke" and four "Val", totaling five aircraft.」 | S1 |
| 1942-01-20~22 | 拉包尔 / 卡维恩攻击 | 「CarDiv 1 attacks Allied positions at Kavieng … of which AKAGI contributes 9 A6M2 "Zeke" and 18 D3A1 "Val"」 | S1 |
| 1942-02-19 | 达尔文空袭 | 「AKAGI contributed 18 B5Ns, 18 D3As, and 9 Zeros to the attack」 | S2 |
| 1942-03-01 | 参与击沉 Pecos / Edsall | 「at 1520 AKAGI also launches nine Vals to participate」 | S1 |
| 1942-03-05 | 芝拉扎（Tjilatjap）空袭 | 「her main contribution appears to have been providing 18 B5Ns and 9 Zeros for the 5 March air strike on Tjilatjap」 | S2 |
| 1942-04-05 | 科伦坡空袭；当日击沉 Cornwall / Dorsetshire | 「AKAGI contributes 17 "Kate" and six "Zeke"」／「17 D3As from AKAGI helped to sink the British heavy cruisers Cornwall and Dorsetshire」 | S1 / S2 |
| 1942-04-09 | 亭可马里空袭；击沉竞技神号 | 「AKAGI contributes 17 "Val" and three "Zeke"」 | S1 |
| 1942-04-09 | 险遭 9 架 Blenheim 轰炸 | 「nine British Bristol Blenheim bombers from Ceylon penetrated the CAP and dropped their bombs … just missing the carrier」 | S2 |
| 1942-04-18~22 | 追击杜立特空袭编队，未果 | 「Akagi, Sōryū, and Hiryū were sent in pursuit of the American carriers Hornet and Enterprise … They found only empty ocean」 | S2 |
| 1942-04-25 | 青木泰二郎接任舰长 | 「Captain Taijiro Aoki relieved Hasegawa as skipper of the carrier.」 | S2 |
| 1942-05-27 | 从柱岛出击参加 MI 作战 | 「AKAGI departs Hashirajima for the Invasion of Midway as flagship of CarDiv 1」 | S1 |
| 1942-06-04 04:30(当地) | 第一波攻击中途岛：18 架舰爆 + 9 架零战 | 「AKAGA contributes 18 "Val" and 9 "Zeke".」 | S1 |
| 1942-06-04 07:10(当地) | 遭 B-26 鱼雷攻击，全部规避 | 「Two torpedoes are evaded by the carrier.」 | S1 |
| 1942-06-04 10:26(当地) | 被 Enterprise VB-6 的 Best 队 3 机俯冲轰炸，1 发直击中部（中部升降机后缘，在机库内爆炸） | 「AKAGI is attacked from 80 degrees port by three VB-6's Douglas SBD-3 "Dauntless" dive-bombers led by LtCdr Richard H. Best」 | S1 |
| 1942-06-04 10:29(当地) | 下令注水弹药库，前部成功、后部因阀件损坏失败 | 「Forward and aft magazines ordered flooded; but at first, only the forward ones can be due to damaged valves aft.」 | S1 |
| 1942-06-04 10:40(当地) | 舵机卡死于右 20–30° | 「rudder stayed locked in 20 degree turn」／「the ship's rudder jammed 30 degrees to starboard」 | S1 / S2 |
| 1942-06-04 10:46(当地) | 南云将旗舰转移至长良号 | 「At 10:46, Nagumo transferred his flag to the light cruiser Nagara.」 | S2 |
| 1942-06-04 19:20(当地) | 青木决定弃舰 | 「Captain Aoki decided to Abandon Ship.」 | S1 |
| 1942-06-04 21:25(当地) | 山本下令推迟处分；舰长被劝离 | 「A direct order from CinC Yamamoto to postpone scuttling is received.」 | S1 |
| 1942-06-05 04:50(当地) | 山本下令处分 | 「AKAGI directed to be scuttled by direct order of CinC-Combined Fleet, Admiral Yamamoto Isoroku.」 | S1 |
| 1942-06-05 05:20(当地) | 被岚、萩风、舞风、野分各射 1 雷，倾覆沉没于 30°30′N 178°40′W | 「AKAGI lay over to starboard and sank tail first after two or three torpedo hits out of four fired into her starboard side」 | S1 |
| 1942-09-25 | 除籍 | 「Removed from the Navy List.」 | S1 |
| 2019-10-20 | 残骸由 Petrel 号在 5,490 m 深处发现 | 「identified the wreck of Akagi using high-frequency sonar … at a depth of 18,011 feet (5,490 m)」 | S2 |
| 2023-09 | EV Nautilus 拍摄残骸 | 「The wreck of Akagi was visited and photographed by the research vessel EV Nautilus in September 2023.」 | S2 |

---

## §12 舰载机编制（中途岛时）

### §12-A 搭载数（三套互斥数据，见 §15）

| 来源 | 零战 | 九九舰爆 | 九七舰攻 | 合计 | 原文照抄 |
|---|---|---|---|---|---|
| Combinedfleet TROM（S1） | 18 | 18 | 18 | 54 + 6 架第六航空队零战 | 「AKAGI's air group consists of 18 A6M2 "Zeke", 18 D3A1 "Val" and 18 B5N2 "Kate". Additionally, six A6M2 "Zeke" from the 6th Air Group … are embarked.」 |
| 英文 Wikipedia（S2） | 24 | 18 | 18 | 60 | 「Akagi's aircraft complement consisted of 24 Zeros, 18 D3As, and 18 B5Ns.」 |
| 日文 Wikipedia（S3） | 21 | 21 | 21 | 63 | 「戦没時保有機 零式艦上戦闘機：21機 九九式艦上爆撃機：21機 九七式艦上攻撃機：21機」（原文标注[要出典]） |

### §12-B 出击情况

| 项目 | 原文照抄 | 来源 |
|---|---|---|
| 第一波（对中途岛） | 「At 0430 (local times), the air strike led by Lt. … Tomonaga Joichi is launched against Midway Island with 36 B5N2 "Kate", 36 D3A1 "Val" and 36 A6M2 "Zeke". AKAGA contributes 18 "Val" and 9 "Zeke".」 | S1 |
| 第一波损失 | 「1 "Val", badly damaged is put out of commission and 1 "Zeke" is lost.」 | S1 |
| 甲板/机库状态（被弹瞬间） | 「当時、赤城の格納庫内には3機の零戦、魚雷装備艦攻18機、第一次攻撃隊として着艦収容したばかりの艦爆18機があった」 | S3 |
| 换装作业进度 | 「その赤城の格納庫では兵装転換を終えていた15～16機の九七艦攻への魚雷再装着作業が始まる」 | S3 |
| 未及出击 | 「There was no second flight from the Akagi.」（青木证言）／「攻撃隊の準備はできておらず、5分で発艦するのは不可能だった」 | S7 / S3 |
| 舰上人员损失 | 「本海戦における赤城搭載機搭乗員の戦死者は機上3名、艦上4名の合わせて7名(戦闘機4名、艦爆1名、艦攻2名）」 | S3 |
| 飞机损失 | **未获取确切总机数**（各源只给片段，无中途岛全战赤城机损总数） | — |

---

## §13 未获取字段汇总

> 本节列出所有查不到的字段，并说明**查过哪些地方**。凡能证明是「0」而非「未获取」的，已在正文标出（弹射器、雷达）。

| 字段 | 状态 | 已检索的位置 |
|---|---|---|
| 旗号（pennant number） | 未获取（疑为不适用） | 日文 Wikipedia 全文（「旗号」「信号符字」0 命中）；英文 Wikipedia infobox（无此栏） |
| 船台号 | 未获取 | Combinedfleet TROM、Navypedia、日文 Wikipedia、japanese-warship 全 4 页 |
| 最大吃水（改装前后） | 未获取 | 所有来源只给单一「吃水」值，无平均/最大之分 |
| 深载排水量（改装前） | 未获取 | 各源只用 full / 公試 二口径 |
| 试航实测功率（改装前后） | 未获取 | 各源只给「出力」131,200 / 133,000，未标实测 |
| 弹药库装甲 | 未获取 | Navypedia Ship protection 章、日文 Wikipedia 要目装甲栏、japanese-warship 防御章、kasado 装甲表 |
| 装甲总重 | 未获取 | 同上 + 检索「装甲重量」「防御重量」 |
| 飞行甲板色 / 上层建筑色 | 未获取 | 日文 Wikipedia「塗装」「迷彩」检索（迷彩 0 命中）；waterline.fanweb.jp 涂装资料 |
| 军官数 | 未获取 | 日文 Wikipedia 要目「乗員」栏只给定员总数 |
| 中途岛出击时实际搭载人数 | 未获取（来源明言「不明」） | 日文 Wikipedia 引『戦史叢書43』；USSBS S7 只给「1400」约数 |
| 测距仪型号与数量 | 未获取 | 日文 Wikipedia「測距」「測距儀」「方位盤」0 命中；kasado「測距儀/レーダー」栏未列；Navypedia 无 |
| 13mm 机枪精确座数 | 未获取 | 只知曾装 13mm 连装机枪并被 25mm 换装，座数无载 |
| 全舰弹药基数（总量） | 未获取 | 只有 NavWeaps 的单门弹药架容量（per gun），非全舰基数 |
| 下格纳库高度 | 未获取 | Navypedia 记「~20x20x?m」，kasado 记「-」 |
| 拦阻索（改装前初期纵索式）索数 | 未获取 | 日英源均只说「British longitudinal system」，索数无载 |
| 中途岛全战赤城机损总数 | 未获取 | 各源只给分段数字 |

---

## §14 来源清单

| ID | URL | 层级 | 说明 |
|---|---|---|---|
| S1 | https://www.combinedfleet.com/Akagi.htm | **D** | Anthony P. Tully / Gilbert Casse 编「IJN AKAGI: Tabular Record of Movement」。逐日记录，引『Shattered Sword』与日方一次史料。**本站价值最高**。 |
| S2 | https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Akagi | **E** | 英文 Wikipedia。脚注引 Gardiner & Gray、Parshall & Tully、Dull、Werneth，可循线索但本身为百科。 |
| S3 | https://ja.wikipedia.org/wiki/赤城_(空母) | **E** | 日文 Wikipedia。引『昭和造船史』『海軍造船技術概要』『戦史叢書43』『写真日本の軍艦』等，**仅作线索**。含 JACAR 档案号 C08051579600 / C08051579700（赤城飛行機隊戦闘行動調書）。 |
| S4 | https://www.navypedia.org/ships/japan/jap_cv_akagi.htm | **D** | Navypedia。主尺度与防护骨架，含改装前后双栏数据。 |
| S5 | https://japanese-warship.com/carrier/akagi/ | **D** | 「大日本帝国軍 主要兵器」赤城 其1（诸元表）。引光人社《航空母艦「赤城」「加賀」》、潮書房《日本海軍艦艇図面全集第三巻解説》。 |
| S6 | https://japanese-warship.com/carrier/akagi-2/ · -3/ · -4/ | **D** | 同站 其2（三段甲板/备炮/防御/烟囱/格纳库/舰桥）、其3（一段甲板/飞行甲板/拦阻/升降机/火控/舰桥论证）、其4（战历）。**本档案日文技术细节的主要依据**。 |
| S7 | https://www.ibiblio.org/hyperwar/AAF/USSBS/IJO/IJO-4.html | **A** | USSBS Interrogation Nav No. 4 / USSBS No. 23，1945-10-09 审问赤城舰长青木泰二郎。**一手证言，雷达=0 即出自此。** |
| S8 | https://www.navweaps.com/Weapons/WNJAP_8-50_3ns.htm | **C** | NavWeaps 日本 20cm/50 三年式。注明 Model B 炮架用于 Akagi 与 Kaga。 |
| S8b | https://www.navweaps.com/Weapons/WNJAP_47-45_10ns.htm | **C** | NavWeaps 日本 12cm/45 十年式。**明言「Akagi carried them to her end at Midway」。** |
| S9 | https://www.navweaps.com/Weapons/WNJAP_25mm-60_mg.php | **C** | NavWeaps 日本 25mm/60 九六式。 |
| S10 | http://www.kasado.net/AircraftCarriers/Japan/Akagi_1927.html | **D** | kasado.net 赤城型诸元表（竣工时/1938改装后/最终时三栏）。升降机、拦阻索、射击指挥装置、格纳库尺寸唯一结构化来源。 |
| S11 | https://ethw.org/Midway_-_Chapter_7_of_Radar_and_the_Fighter_Directors | **C** | ETHW「Radar and the Fighter Directors」第 7 章。佐证日舰有雷达、航母无雷达。 |
| S12 | http://waterline.fanweb.jp/materials/３．軍艦色の使い分け/ | **D** | 舰船模型资料站，按海军工厂分类军舰色。赤城改装前归吴厂灰、改装后归佐世保厂灰。 |
| S13 | https://nihonkaigun.ikaduchi.com/kuubo/akagi.html | **D** | 「日本海軍艦艇入門」赤城/加贺页，含赤城-加贺对照表与左舷舰桥原委。 |
| S14 | https://rikukaigun.org/Nishida/stc0202.html | **D** | Hiroshi Nishida 舰艇诸元页。满载 42,750 t 的来源。 |
| S15 | https://www.jacar.archives.go.jp/das/meta/C08051579600 · C08051579700 | **A** | JACAR（アジア歴史資料センター）「昭和16年12月～昭和17年6月 赤城飛行機隊戦闘行動調書（1）（2）」，防衛省防衛研究所藏。**已确认存在，但图像未数字化读取**，本次未取到内文数值。 |

**未能使用的档案**：JACAR 上述两件为 A 级一手档案，目录页可访问，但需图像浏览（本次仅取到目录元数据，未取到内文）。若需舰载机逐日行动原始记录，此为下一步首选。

---

## §15 分歧与纠错汇总

> 原则：只列两边各说什么、各引哪句原话，**不裁决**。纠错项则明确指出任务书前提与原文的冲突。

### 分歧 ①：改装后标准排水量 36,500 还是 37,100？

- 日文源：**36,500 英吨**
  > 「基準排水量 36,500英トン」 — S3
  > 「基準排水量② 　36,500t」 — S5
- 英文 Wiki 正文也用 36,500，但括注换算成 37,100 t：
  > 「36,500 long tons (37,100 t) (standard)」 — S2
- Combinedfleet TROM 却直接写 37,100：
  > 「Her displacement is now 37,100-tons (standard).」 — S1

即：**36,500 英吨（long ton）= 37,100 公吨（tonne）**，两者是同一质量的两种单位。S1 写作「37,100-tons (standard)」时用了公吨数值却标 standard，容易与日文源的英吨值混读。

### 分歧 ②：41,300 是「公试排水量」还是「deep load / 满载」？

- 日文源：**公試排水量**
  > 「公試排水量 41,300トン」 — S3
  > 「公試排水量（メートルトン）… 41,300」 — S13
- 英文源：**deep load**
  > 「41,300 long tons (42,000 t) (deep load)」 — S2
- Nishida / kasado 则另给 **満載 42,750 t**：
  > 「満載 42,750t」 — S14

三种口径词指同一个数量级的数字，但**「公試」不等于「deep load」，也不等于「満載」**。本站若需单一字段，须先确定采用哪一体系。

### 分歧 ③：改装前 34,364 是 full 还是 公試？

- 英文源：**full**
  > 「Displacement full, t \| 34364」 — S4
- 日文源：**公試**
  > 「公試排水量① 　34,364t」 — S5
  > 「公試排水量 34,364英トン」 — S3

同 ①，是口径词体系冲突，不是数值冲突。

### 分歧 ④：改装后燃油 5,770 t 还是 7,500 长吨？续航 8,200 还是 10,000 海里？

- 日文源：
  > 「燃料 重油 5,770トン または5,775トン(1938年3月)」／「航続距離 8,200カイリ / 16ノット」 — S3
- 英文源：
  > 「Her bunkerage was increased to 7,500 long tons (7,600 t) of fuel oil which increased her endurance to 10,000 nautical miles」 — S2
- Navypedia 第三说：
  > 「Fuel, t \| oil 6000」「Endurance, nm(kts) \| 8200(16)」 — S4

三家互不相同：5,770 / 6,000 / 7,500 吨燃载；8,200 / 10,000 海里续航。

### 分歧 ⑤：装甲厚度与倾角

| 来源 | 舷侧 | 倾角 | 甲板 |
|---|---|---|---|
| S4 Navypedia | 「belt: 152」 | 「inclined at 14°from vertical」 | 「main deck: 51 - 32」 |
| S3 日文 Wiki | 「舷側：5インチVC鋼」 | 「傾斜12度」 | — |
| S6 japanese-warship | 「254mmあった戦艦用のVC甲鈑を150mmまで再圧縮」 | 「傾斜10度で舷側装甲として設置」 | 「55mmのNVNC鋼板と22mmのHT鋼板の張り合わせ」 |
| S10 kasado | 「152mm」 | 「傾斜:14.0°」 | 「水平部:79mm／外舷傾斜部:102mm」 |
| S2 英文 Wiki | 「reduced from 254 to 152 mm」 | — | 「reduced from 96 to 79 mm」 |
| S14 Nishida | 「水線帯 250mm」 | — | — |

注意两处硬冲突：**日文 Wiki 的「5インチ（=127mm）」与其余来源的 152mm 不一致**；**Nishida 的「250mm」与其余全部来源不一致**（250mm 是原战巡设计值，非航母化后实际值）。倾角则有 10°/12°/14° 三说。

### 分歧 ⑥：试航实测航速 32.5 还是 32.1 节？

- 32.5 节：
  > 「Achieves a speed record of 32.5-knots during her trials.」（1927-06-17） — S1
  > 「竣工時 32.5ノット」 — S3
- 32.1 节：
  > 「最大速度① 　公試32.1ノット」 — S5
  > 「32.1ノットと狙い通り計画よりは速くなりました」 — S6

日文 Wiki 另给第三说：「1931年3月 31.75ノット」（S3）。

### 分歧 ⑦：拦阻装置是「一式」还是「呉式四型」？9 索还是 10 索？

- S1：「Her arrester gear is replaced by a Japanese-designed Type 1 system.」
- S2：「hydraulic Type 1 system with 9 wires」
- S10：「呉式四型 (4.0t / N/A):10索」
- S6：「【赤城】と【加賀】は改装の際に呉式四号が搭載されています」

日文文献（S6/S10）一致指向「呉式四型」，英文源的「Type 1」疑为一式/呉式四号的译名混淆，索数 9 vs 10 亦未定。

### 分歧 ⑧：射击指挥装置数量

- S10：一四式方位盘 2 组 / 九一式高射装置 2 组 / 九五式机铳射击装置 4 组
- S6：九一式高射装置「両舷と艦橋トップに計3基」、九五式「各機銃群に計4基」
- S2：Type 95 directors **six** 组；Type 94 高射装置 2 组替换 Type 91；Type 89 director **1** 部管 20cm

九一式：2 组 vs 3 基。九五式：4 组 vs 6 组。20cm 用：一四式方位盘 2 组 vs Type 89 director 1 部。

### 分歧 ⑨：搭载机数（中途岛）

见 §12-A，18/18/18+6、24/18/18、21/21/21 三说并存。

### 分歧 ⑩：战死者数 221 / 263 / 267 / 200

- 221 名：
  > 「准士官以上8名、下士官兵213名の計221名が戦死した」 — S3
  > 「【赤城】の戦死者は221名」 — S6
- 263 名：
  > 「while only 263 petty officers and men are lost」 — S1
- 267 名：
  > 「Two hundred and sixty-seven men of the ship's crew were lost」 — S2
- 200 名（青木证言，1945 年回忆）：
  > 「200 were lost and 100 wounded, out of a total complement of 1400」 — S7

日文源区分了「准士官以上」与「下士官兵」，英文源可能是「兵员损失」口径不同，也可能是把其他舰的数字混入。**不裁决。**

### 分歧 ⑪：沉没有「舰尾先沉」还是「舰首先沉」

- 舰尾先沉（Tully 的结论）：
  > 「AKAGI lay over to starboard and sank tail first」 — S1
- 舰首先沉（英文 Wiki）：
  > 「she sank, bow first, at 05:20」 — S2

Combinedfleet 的 Note 3 专门解释了这条分歧的来源：
> 「It should be mentioned that in "Shattered Sword" the Editor with Jon Parshall described Akagi sinking head first. This had been derived from Gordon Prange's "Miracle at Midway" but proved misleading. …since 2005 translation of the diary of Koga Mogotaro CO of NOWAKI … makes clear Akagi's bow was the last part of the ship to leave the surface.」 — S1

Tully 明确认为「bow was the last part to leave the surface」= 舰尾先沉。英文 Wiki 的「bow first」是未更新的旧说。

### 分歧 ⑫：青木舰长说被弹「两发」，Tully 认为致命伤仅一发

> 「Fore; two bombs by dive bombing about two hours after sunrise」 — S7（青木证言）
> 「Heretofore it has been generally reported that Akagi was struck by two bombs … However, in "Shattered Sword" we … made the case that the available facts indicate the bomb aft did not detonate on the flight deck, but exploded close beside the fantail. For this reason, Akagi was in fact mortally wounded almost certainly by one hit alone」 — S1

---

### 纠错 ①：「旗号」字段对日本海军不适用
详见 §0。日本海军无 pennant number 制度，赤城的识别是舰名 + 舰艇类别等级 + 着舰识别文字「ア」。

### 纠错 ②：命中日期是 1942-06-04（当地时间），不是 6 月 5 日
任务书写「1942 年 6 月 5 日中途岛海战中被美军俯冲轰炸机击中」。按中途岛当地时间，俯冲轰炸发生在 **6 月 4 日 10:26**：
> 「- 1026, AKAGI is attacked from 80 degrees port by three VB-6's Douglas SBD-3 "Dauntless" dive-bombers」 — S1
> 「At approximately 10:26, the three bombers hit her with one 1,000-pound (450 kg) bomb」 — S2

**沉没**才是 6 月 5 日（当地）/ 6 月 6 日（日本时间）。Tully 在 TROM 开头专门说明用当地时间：
> 「Note: For convenience and familiarity local times and date are used herein until AKAGI's sinking as the vast majority of sources, even some Japanese ones, utilize this approach. To convert to Tokyo (JST) or Zone 9 time, subtract three hours but advance one one day ahead of a Midway Local time」 — S1

日文源的「1942年6月6日雷撃処分」用的是日本时间，与当地的 6 月 5 日 05:20 是同一时刻。三种写法都对，但**必须注明时区**，否则会误读成「被弹和沉没隔了一天多」。

### 纠错 ③：1927 年竣工时赤城只有 6 门 20cm 炮，不是 10 门
任务书写「主炮（改装前后不同：1927 年 20cm 单装炮，改装后拆除部分）」——「1927 年 20cm 单装炮」这半句是对的，但很多资料会把 10 门算进竣工状态。实际：
> 「連装砲2基ですが、実は竣工時には搭載されていません。…連装砲が搭載されたのは昭和3年/1928年末の工事で、それまではここには何もありませんでした。」 — S6

即：1927-03-25 竣工 = 单装 6 门；1928 年末起 = 单装 6 + 连装 4 = 10 门；1938 起 = 单装 6 门。**三个状态，不是两个。**

### 纠错 ④：12cm 高角炮从未换装为 12.7cm
任务书写「副炮/高角炮（12cm 或 12.7cm 连装高角炮）」。赤城**至死都是 12cm 十年式**，换装计划存在但未实施：
> 「The carrier Kaga and those cruisers modernized during the late 1930s had these weapons replaced by the 12.7 cm/40 (5") Type 89 AA gun. However, Akagi carried them to her end at Midway.」 — S8b
> 「The ship's 12 cm 10th Year Type guns were scheduled to be replaced by more modern 12.7 cm (5 in) Type 89 mounts in 1942. … However, the ship was lost in combat before the upgrade could take place.」 — S2
> 「高角砲は、これもまた金がねぇってことで、最新の八九式40口径12.7cm高角砲に換装されることはなく」 — S6

### 纠错 ⑤：赤城改装时曾为 2 基弹射器做配套工程，但未完成 —— 「弹射器：0」需要加注
任务书要求「弹射器（有无、型号、数量）」。结论是 **0 基**（S2 明言 No catapults were fitted）。但日文专题给出了一个补充事实：
> 「この予算の問題もあったのでしょうか、【赤城】はカタパルト2基を搭載するための工事が一緒に行われていました。ただこの工事もどの段階まで行われていたのかが分からず、少なくとも実験が可能だった【加賀】レベルには遠く及ばない段階でストップしているのは間違いないでしょう。」 — S6

即「计划 2 基、工程部分实施、最终未装成」。字段值仍应为 **0**，但加注可避免与「从未考虑弹射器」混淆。

### 纠错 ⑥：任务书「赤城与加贺不是同一舰级」是对的，但要注意来源里「赤城级」的用法
日文 Wikipedia infobox 明确：
> 「級名 巡洋艦計画時：天城型巡洋戦艦、空母：未分類」 — S3

即**航母化后的赤城「未分类」（无同级舰）**，战巡时代属**天城型**。但 kasado.net（S10）与部分资料把赤城单列为「赤城型航空母舰」，那是「唯一舰自成一级」的编目习惯，不代表有同级舰。加贺来自**加贺级战列舰**，与赤城不同级 —— 任务书此项无误，仅需在数据模型里把「级」字段处理成「天城型（战巡计划时）/ 无同级舰（航母）」。

### 纠错 ⑦：赤城在珍珠港前**没有**"雷达缺失但靠瞭望"这类常规说法之外的特殊装备
任务书写「中途岛时赤城基本没有雷达，请核实并如实记录」。核实结果：**完全没雷达，且整个机动部队的航母都没雷达**，不只是"基本没有"。见 §8-A 的 USSBS 原话。

---

## §16 字段覆盖率统计

| 类别 | 字段数 | 获取 | 未获取 |
|---|---|---|---|
| §0 身份 | 10 | 9 | 1（旗号） |
| §1 建造 | 9 | 8 | 1（船台号） |
| §2 主尺度（前 7 + 后 7） | 14 | 12 | 2（最大吃水×2） |
| §3 排水量（前 4 + 后 4） | 8 | 7 | 1（深载·改装前） |
| §4 动力 | 10 | 8 | 2（试航实测功率×2；实测航速已得，设计功率已得） |
| §5 防护 | 6 | 4 | 2（弹药库装甲、装甲总重） |
| §6 航空设施 | 14 | 13 | 1（前中期纵索式索数）* |
| §7 武备 | 10 | 9 | 1（全舰弹药基数）* |
| §8 雷达与火控 | 3 | 2 | 1（测距仪）** |
| §9 编制 | 4 | 2 | 2（军官数、中途岛实员） |
| §10 涂装与外形 | 6 | 5 | 1（甲板色） |
| §12 舰载机 | 2 | 1 | 1（机损总数） |
| **合计** | **96** | **80** | **16** |

\* 按"该字段的最小可交付信息"计为已获取（拦阻索给了改装后的 9/10 索；弹药基数给了 per-gun 值），已在正文标注其局限。
\** 雷达字段计为已获取，因为「0 部」是有 A 级一手证言支撑的确证结论，不是查不到。

**覆盖率：80 / 96 ≈ 83.3% 获取，16 / 96 ≈ 16.7% 未获取。**

其中「雷达 = 0」「弹射器 = 0」两条属于**有价值的零值**，不应与「未获取」混计 —— 这是本档案在字段完整性之外的主要收获。
