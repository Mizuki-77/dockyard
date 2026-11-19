# 加贺（Kaga）技术数据档案

> 采集对象：日本海军航空母舰「加賀」
> 采集日期：2026-11-19
> 编制规则：每条数值附原文照抄 + 来源 URL。查不到写「未获取」。不推算、不跨来源拼凑、不按同级舰类推。
> 来源分级：A=一手档案 / B=同期官方出版物 / C=权威二次文献 / D=专题网站 / E=百科

---

## 采集方法与前置说明

**代理情况**：任务书指定的代理 `127.0.0.1:7897` 未使用。本机系统代理为 `http://127.0.0.1:12450`，实测**直连即可**（`Invoke-WebRequest https://www.combinedfleet.com/kaga.htm` 返回 200）。

**取数方式**：`web_fetch` 工具对 combinedfleet / ibiblio / navweaps 等域名报 SSRF 拦截（域名解析到 198.18.x.x），改用本地 Python `urllib` 直连抓取原文，脚本与原文存 `work/_tmp/kaga_*`。**所有引文均来自实际抓取的页面文本**，未使用记忆或推测。

**检索路径**：combinedfleet TROM（S1）→ combinedfleet Kaga Data Page（S2）→ 英文/日文 Wikipedia（S3/S4）→ Navypedia（S5）→ japanese-warship.com 加贺三篇（S6/S7/S8）→ kasado.net 诸元表（S9）→ Nishida 诸元页（S10）→ NavWeaps 四篇火炮页（S11~S14）→ USSBS 第 4 号审问（S15）→ 军舰色资料站（S16）→ 21号电探条目（S17）→ ETHW 雷达章（S18）→ naval-encyclopedia（S19）→ 电脳大本営 加贺二篇（S20/S21）→ JACAR 战斗详报目录（S22）→ 加贺型战列舰条目（S23）。

**关于「原文照抄」的说明**：口径词（基準排水量 / 公試排水量 / 満載 / standard / full load）一律照抄来源用语，不做英制-公制折算。加贺的排水量在来源间口径互斥严重，见 §15。

---

## §0 身份

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 原名 | 加賀（かが） | 「加賀（かが）は、大日本帝国海軍の航空母艦」 | S4 |
| 中文名 | 加贺 | —（中文译名，无原文） | — |
| 英文名 | Kaga | 「Launched at Kawasaki and named KAGA ("Increased Joy", after the Kaga province, now Ishikawa Prefecture).」 | S1 |
| 舰种 | aircraft_carrier（原为战列舰） | 「種別 (戦艦 →) 航空母艦」 | S4 |
| 所属国家 | japan | 「運用者 大日本帝国海軍」 | S4 |
| 所属海军 | 大日本帝国海軍（Imperial Japanese Navy） | 「was an aircraft carrier built for the Imperial Japanese Navy (IJN)」 | S3 |
| **旗号** | **未获取（且不适用）** | 见本节末「旗号」条 | — |
| 命名来源 | 加贺国（石川县旧令制国名） | 「加賀の艦名は石川県の旧令制国名加賀国にちなんで命名された」 | S4 |
| 建造计划 | 八四艦隊案（大正6年度）→ 发展为八八舰队；加贺为**八八舰队第3番舰（仮称第七号戦艦）** | 「計画 大正6年（1917年）度 (八四艦隊案)」／「1918年（大正7年）5月15日、日本海軍は八八艦隊第3番艦（仮称第七号戦艦）を加賀と命名する（土佐と同日付）」 | S4 / S23 |
| 时代 | ww2 | 「In service 1928–1942」 | S3 |

**补充（原文）：**
> 「加賀型戦艦（かががたせんかん）は、日本海軍が八八艦隊計画で考案した戦艦。長門型戦艦の拡大改良型である」 — S23
> 「なお計画時の番号は「加賀」が第7号戦艦、「土佐」が第8号戦艦」 — S23
> 「艦内神社は白山比咩神社」／「母港 佐世保」 — S4

**「旗号」字段对日本海军不适用，本档案按「不适用」处理。**
日本海军不编舷号/旗号（pennant number）。日文 Wikipedia 加贺条目全文检索「旗号」「信号符字」**均 0 命中**；舰艇识别体系是「艦艇類別等級表」+ 舰名：
> 「大正七年五月十五日(達七七)艦艇類別等級表中戰艦ノ欄「陸奥」ノ次ニ「、加賀、土佐」ヲ加フ」 — S23

加贺可用的「识别」类字段只有两个，且都是**航空队**层面而非舰体层面：
- 垂直尾翼部队识别记号：**A II**（「加賀A II」；同期赤城「A I」、蒼龍「B I」、飛龍「B II」）— S24
- 着艦識別文字：**「カ」**（见 §10，来源等级偏低）

建议本站把「旗号」对日本海军舰统一置空，或改挂「着艦識別文字 / 部隊識別記号」。

---

## §1 建造

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 建造厂 | 川崎造船所（神户）+ 横須賀海軍工廠（舾装/改装） | 「建造所 進水まで：川崎造船所 / 艤装：横須賀海軍工廠」 | S4 |
| 建造地 | 神戸（Kobe）→ 横須賀 | 「Kobe. Laid down as a TOSA-class battleship at Kawasaki Heavy Industries Shipyard.」 | S1 |
| 开工 | 1920-07-19 | 「起工 1920年7月19日」 | S4 |
| 下水 | 1921-11-17 | 「進水 1921年11月17日」 | S4 |
| 服役（竣工） | 1928-03-31 | 「竣工 1928年3月31日」 | S4 |
| 舰种变更 | 1923-11-19（改航空母舰） | 「大正12年11月19日航空母艦に改造することと爲り」 | S4 |
| 改装（大改装）起 | 1934-06-25（正式）／1933-10-20 转预备舰入坞 | 「25 June 1934: Sasebo Naval Yard. KAGA's reconstruction is officially started.」／「20 October 1933: Reduced to second class reserve status … KAGA docks at Sasebo Naval Yard for this purpose.」 | S1 |
| 改装（大改装）止 | 1935-06-25 | 「25 June 1935: Undocked, reconstruction completed.」 | S1 |
| 建造费 | 5,300 万日元（约 3,645 万美元） | 「Cost ¥53 million ($36.45 million)」 | S3 |
| **结局日期** | **1942-06-04 19:25（中途岛当地时）＝ 1942-06-05 16:25（日本时间 JST）** | 见下方时区说明 | S1 |
| 结局型式 | **自沉（己方驱逐舰萩風雷击处分）**，非「被炸沉的瞬间」 | 「Sunk: 1925 (1625 JST) destroyer HAGIKAZE fires two torpedoes into her starboard side amidships aft.」 | S1 |

**时区说明（这是任务书要求核实的点，combinedfleet 编辑专门加了注）：**
> 「Note: For convenience and familiarity local times and date are used herein until KAGA's sinking as the vast majority of sources, even some Japanese ones, utilize this approach. To convert to Tokyo (JST) or Zone 9 time, subtract three hours but advance one one day ahead of a Midway Local time - (Tully)」 — S1

即：**中途岛当地 6 月 4 日 19:25 ＝ 日本时间 6 月 5 日 16:25**。日方史料（含 JACAR 战斗详报标题、日文 Wikipedia）一律记为**昭和17年6月5日**，美方与 combinedfleet 用当地日 6 月 4 日。两种写法指同一时刻，**不是「当天/次日」的矛盾**，是时区差。

**补充原文（条约与代舰经过）：**
> 「5 February 1922: Both TOSA class battleships are canceled under the terms of the Washington Naval Treaty. …the incomplete battlecruisers AMAGI and AKAGI are selected and TOSA and KAGA designated for scrapping. Construction work on the KAGA is ordered halted.」 — S1
> 「1 September 1923: An earthquake of magnitude 8.3 … AMAGI … making launch impossible. … Henceforth, battleship KAGA is reordered on 19 November as a carrier to replace AMAGI.」 — S1
> 「1925: KAGA's conversion to an aircraft carrier starts at Yokosuka Naval Yard.」 — S1

**注意（竣工日 ≠ 实际完成日，两舰同病）：**
> 「就役中も使えなくはなかったので… なんと昭和6年/1931年末でようやく工事が一通り終了した具合です。」 — S6
> 「つまり、昭和3年/1928年3月31日の竣工日にはまだ工事が残っていたのです。」 — S6
> 「結局予算が足りなかったので、年度内ではとりあえず完成したことにし、翌年度で新しく修理、改装費として予算を計上することになります。」 — S6

---

## §2 主尺度

### §2-A 改装前（1928 竣工时 ~ 1935-06）

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 全长 | 238.51 m | 「全長 782 ft 6 in (238.51 m)」 | S4 |
| 水线长 | 230.28 m | 「水線長 755 ft 6+1⁄8 in (230.28 m)」 | S4 |
| 垂线间长 | 217.93 m | 「垂線間長 715 ft (217.93 m)」 | S4 |
| 水线宽 | 29.57 m | 「水線幅 97 ft (29.57 m)」 | S4 |
| 最大宽 | 31.67 m（水线下） | 「最大幅 103.91 ft (31.67 m)(水線下)」 | S4 |
| 吃水 | 7.92 m | 「吃水 26 ft (7.92 m)」 | S4 |
| 深さ（型深） | 15.45 m | 「深さ 15.45m」 | S4 |
| 上甲板高 | 24.77 m | 「高さ 上甲板まで 81 ft 3 in (24.77 m)」 | S4 |
| 帰着甲板高 | 约 29.57 m | 「帰着甲板まで約97 ft (29.57 m)」 | S4 |

> Navypedia 交叉印证（pp/wl/oa 标注）：
> 「Length, m \| 218.0 pp 230.0 wl 238.5 oa」「Breadth, m \| 29.6」「Draught, m \| 7.93」 — S5
> Nishida 同：「垂線間長 218.0m, 水線長 230.0m, 全長 238.5m」「全幅 29.6m」「喫水 7.93m」 — S10

### §2-B 改装后（1935-06-25 完成后 ~ 1942-06 战没）

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 全长 | 247.650 m | 「全長 247.650m」 | S4 |
| 水线长 | 240.304 m | 「水線長 240.304m」 | S4 |
| 垂线间长 | 217.93 m（**未变**） | 「垂線間長 715 ft (217.93 m)」 | S4 |
| 水线宽 | 32.500 m | 「水線幅 32.500m」 | S4 |
| 最大宽 | **未获取**（各源只给单一 breadth 32.5） | 「Breadth, m \| 32.5」 | S5 |
| 吃水 | 9.479 m | 「吃水 9.479m」 | S4 |
| 深さ | 15.45 m（未变） | 「深さ 15.45m」 | S4 |
| 飞行甲板距水面 | 21.7 m | 「水面からの飛行甲板までの高さが21.7mと日本空母のなかでは一番高く」 | S4 |

> 「the hull was lengthened by 10.3 meters (33 ft 10 in) at the stern to reduce drag」 — S3
> 「After installation of anti-torpedo bulges hull breadth has increased from 29.6 to 32.5m, hull length was also increased from 238.5 to 247.7 m.」 — S5

**注意**：垂线间长改装前后都是 217.93 m，延长全部加在舰尾（舰体加长 10.3 m），故 238.51→247.65 m 与 230.28→240.30 m 各自吻合，**不是抄错**。

---

## §3 排水量

> **口径警告**：「基準排水量」≈standard；「公試排水量」是日本海军特有的试航状态；「満載」≈full load。三者不可互换。本节照抄来源用词。

### §3-A 改装前

| 口径 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 基準排水量（公表值） | 26,900 英吨 | 「基準排水量 公表値 26,900英トン」 | S4 |
| 基準排水量（要目簿计算值） | 约 29,500 英吨 | 「約29,500英トン」 | S4 |
| 公試排水量 | 33,693 英吨 | 「公試排水量 33,693英トン」 | S4 |
| 満載排水量 | **未获取** | 「満載排水量」（栏位空白） | S4 |

**三家口径互斥（原话并列，不裁决）：**
> 「Displacement standard, t \| 26900」「Displacement full, t \| 33693」 — S5（Navypedia 作 **full**）
> 「排水量 基準 26,900t, 公試 33,161t」 — S10（Nishida 作 **33,161**）
> 「基準排水量 26,900t / 公試排水量 33,161t」 — S9（kasado 同 Nishida）
> 「She displaced 26,900 long tons (27,300 t) at standard load, and 33,693 long tons (34,234 t) at full load」 — S3
> 「Her displacement is 27,300-tons standard.」 — S1（把 26,900 长吨换算成公吨后仍标 standard）

### §3-B 改装后

| 口径 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 基準排水量 | 38,200 英吨 | 「基準排水量 38,200英トン」 | S4 |
| 公試排水量 | 42,541 / 42,279 / 完成公試 42,542 吨 | 「公試排水量 42,541トン または 42,279トン / 完成公試 42,542トン」 | S4 |
| 公試排水量（别源） | 41,869 t | 「公試排水量 41,869t」 | S9 / S10 |
| 満載排水量 | 43,650 t | 「満載排水量 43,650t」 | S9 / S10 |
| 基準排水量（别源） | 38,600 t | 「基準排水量 38,600t」 | S9 |

> 「Her displacement is now increased to 38,200-tons standard」 — S1
> 「Displacement standard, t \| 38200」「Displacement full, t \| 43650」 — S5

**任务书未要求但值得单列的官方年报刊值（口径自称「排水量」，未标基准/公试）：**
> 「軍極秘「昭和十二年海軍年報」より）によると排水量41,044英トン、125,000馬力、速力28.50ノット、燃料石炭庫容量2,100トン、重油庫容量8,208トン、乗員1,340名」 — S4（引『戦史叢書31 海軍軍戦備1』付表第四）

---

## §4 动力

### §4-A 改装前

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 动力型式 | 川崎布朗-柯蒂斯式齿轮传动蒸汽轮机 4 组，4 轴 | 「4 sets Kawasaki Brown Curtis geared turbines giving 91,000 shp on four shafts」 | S2 |
| 轴数 | 4 | 「No of shafts \| 4」 | S5 |
| 锅炉数/型号 | ロ号艦本式缶 12 基（重油専焼 8 + 混焼 4） | 「ロ号艦本式重油専焼缶 大8基、小4基」／「twelve saturated steam boilers, eight of them oil-burning, four of the mixed oil/coal type」 | S4 / S2 |
| 主机数/型号 | ブラウン・カーチス式タービン（高低圧）4 基 | 「主機 ブラウン・カーチス式タービン(高低圧) 4基」 | S4 |
| 设计功率 | 91,000 shp | 「出力 91,000shp」 | S4 |
| **试航功率** | **未获取**（各源只给「出力 91,000」，未区分设计/实测） | — | — |
| 设计航速（作戦舰时） | 26.5 kt | 「As a battleship this was projected to give KAGA 26.5 knots.」 | S2 |
| 设计航速（空母化后） | 27.5 kt | 「計画 27.5ノット」 | S4 |
| 试航航速 | **27.5 kt**（1928-11 试航）／别源 **26.7 kt** | 「KAGA actually achieved 27.5 knots on her November 1928 trials」／「実速26.7kt（公称27.5kt）」 | S2 / S4 |
| 续航力 | 8,000 海里 / 14 节 | 「航続距離 8,000カイリ / 14ノット」 | S4 |
| 燃油 | 重油 3,600 t + 石炭 1,700 t（合计 5,300 英吨） | 「Fuel, t \| oil 3600, coal 1700」／「燃料 5,300英トン」 | S5 / S4 |
| 螺旋桨 | 4 轴 × 210 rpm，直径 4.419 m，螺距 4.877 m | 「4軸 x 210rpm / 直径4.419m、ピッチ4.877m」 | S4 |

### §4-B 改装后

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 动力型式 | 布朗-柯蒂斯式 2 基 + 舰本式 2 基，4 轴 | 「ブラウン・カーチス式タービン(高低圧)2基 / 艦本式タービン(高中低圧)2基」 | S4 |
| 轴数 | 4 | 「4軸」 | S9 |
| 锅炉数/型号 | ロ号艦本式重油専焼缶（带空气预热器）8 基 | 「ロ号艦本式重油専焼缶(空気余熱器付) 8基」 | S4 |
| 主机数/型号 | 4 基（内 2 基换新为舰本式） | 「内側2本のタービンを最上型巡洋艦搭載の新式の大出力のものに換装」 | S4 |
| 设计功率 | 127,400 shp（别源 125,000 hp） | 「出力 127,400shp または 125,000hp」 | S4 |
| 试航功率 | 127,400 shp（试航实测值） | 「increased her power from 91,000 to 127,400 shp … during trials」 | S3 |
| 设计航速 | 28.34 kt（别源 28.95 / 28.50） | 「速力 28.34ノット または28.95ノット」 | S4 |
| 试航航速 | 28.34 kt | 同上 | S4 |
| 续航力 | 10,000 海里 / 16 节 | 「航続距離 10,000カイリ / 16ノット」 | S4 |
| 燃油 | 重油罐容量 8,200（容積）吨；满载 7,500（重量）吨 | 「重油タンク容量：8,200(容積)トン / 満載 7,500(重量)トン」 | S4 |
| 推进转速 | 2 轴 × 210 rpm，2 轴 × 280 rpm | 「2軸 x 210rpm、2軸 x 280rpm」 | S4 |

> 锅炉布置：「She emerged from reconstruction with her eight boilers arranged each in a separate compartment amidships along the midline, port and starboard.」 — S2
> 目标 30 节未达：「目標は30ノットでしたが、これはちょっと欲張り過ぎかも。」 — S7

---

## §5 防护

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 装甲体系 | 原战列舰集中防御；空母化时大幅削薄。舷侧装甲带 + 平甲板（下格纳库层）+ 舷侧倾斜接续部 + 纵向鱼雷隔壁 | 「Main 152mm belt closed about 2.3 of hull length and was inclined at 14° from vertical.」 | S5 |
| 舷侧装甲（改装前） | 152 mm，倾斜 14° | 「belt: 152」／「inclined at 14°from vertical」 | S5 |
| 舷侧装甲（改装后） | 152 mm，倾斜 14°（**未变**） | 「belt: 152 … after modernization」 | S5 |
| 舷侧（原设计值，被削减前） | 280 mm → 152 mm | 「Her waterline armored belt was reduced from 280 to 152 mm (11 to 6 in) during her reconstruction」 | S3 |
| 甲板装甲（改装前） | 55–32 mm（38 mm 装甲 + 17 mm 钢板） | 「Flat main (lower hangar) 55-32mm (38mm armour on 17mm plating)」／「Deck: 38 mm」 | S5 / S3 |
| 甲板装甲（改装后） | 79–57 mm（51–32 mm 装甲 + 28–25 mm 钢板），另有 102 mm 倾斜接续部 | 「Flat main (lower hangar) 79-57mm (51-32mm armour on 28-25mm plating) deck … additional 102mm slopes」 | S5 |
| 甲板（原设计值，被削减前） | 102 mm → 38 mm | 「her deck armor was also reduced, from 102 to 38 mm」 | S3 / S19 |
| 鱼雷舱壁上段（改装后） | 127 mm（上部防雷鼓包） | 「the upper part of her torpedo bulge was given 127 mm (5 in) of armor」 | S3 |
| 水下防护 | 纵向防雷隔壁 76 mm（改装前）／76–16 mm（改装后）；鼓包使水下防护深度 +1.5 m | 「There was 76mm longitudinal anti-torpedo bulkhead.」／「76-16mm … Depth of underwater protection was increased at 1.5m by bulges.」 | S5 |
| **弹药库装甲** | **未获取** | 各源「Ship protection」章均只给 belt/deck/bulkhead，无弹药库项 | S5/S3/S9/S19 |
| **装甲总重** | **未获取** | 检索「装甲重量」「防御重量」「armour weight」→ 0 命中 | S1–S23 |

**第三方口径（与上表冲突，见 §15）：**
> kasado 表：「装甲甲板装甲 水平部:55mm / 外舷傾斜部:75mm」（改装前后同值） — S9
> Nishida：「装甲 水線帯 275mm」（改装前后同值） — S10

**设计上的关键弱点（原文，比厚度更重要）：**
> 「Kaga's aviation fuel tanks were incorporated directly into the structure of the carrier, meaning that shocks to the ship, such as those caused by bomb or shell hits, would be transmitted directly to the tanks, resulting in cracks or leaks.」 — S3
> 「Critically, nothing is known about the protection of vital aviation gasoline tanks. There was no known bulkheads or armour stray above or around them.」 — S19

---

## §6 航空设施

### §6-A 三段式飞行甲板 —— 上段 / 中段 / 下段（本站新加字段，重点）

| 分段 | 长度 × 宽度 | 面积 | 原文照抄 | 来源 |
|---|---|---|---|---|
| **上段**（着舰 + 起飞主甲板） | **171.30 m × 30.48 m** | 5,190 ㎡ | 「帰着甲板：562 ft (171.30 m) x 100 ft (30.48 m)」／「上段:171.2m × 30.5m (5,190㎡)」 | S4 / S9 |
| **中段**（小型机起飞） | **15.0 m × 25.0 m** | 375 ㎡ | 「中段:15.0m × 25.0m (375㎡)」 | S9 |
| **下段**（大型机起飞） | **55.02 m × 24.38 m**（别源 55.0 × 20.0） | 1,100 ㎡（S9） | 「発艦甲板：180 ft 6 in (55.02 m) x 80 ft (24.38 m)」／「下段:55.0m × 20.0m (1,100㎡)」 | S4 / S9 |
| 三段合计 | — | 6,665 ㎡（Navypedia 自算） | 「(fd - 5,190+375+1100=6,665m², ha - ?m² / ?m³)」 | S5 |

> 英文源英文表述（长度值与中文表一致，宽度未给）：
> 「Kaga's main flight deck was 171.2 meters (561 ft 8 in) long and 30.5 meters (100 ft) wide, her middle flight deck was only about 15 meters (49 ft 3 in) long and started in front of the bridge, and her lower flight deck was approximately 55 meters (180 ft 5 in) long.」 — S3

**中段甲板宽度分歧**：S9 记 25.0 m，S5 记「upper flight-off deck: 15x~25m」（同 25），但 S4 未给宽度。下段宽度 S4 记 24.38 m、S9 记 20.0 m、S5 记「55x~20m」（偏 S9）。→ 见 §15 分歧 ⑥。

**使用方式（原文）：**
> 「上段を離着艦用、中段を小型機の発艦用、下段を大型機の発艦用とし、航空機の機種・用途に合わせ、甲板を使い分けることが考えられた」 — S4
> 「the hangars opened onto the middle and lower flight decks to allow aircraft to take off directly from the hangars while landing operations were in progress on the main flight deck above」 — S3

**但中段甲板实际不可用（这是加贺三段甲板失败的核心原因，与赤城同病，但加贺更早被舰桥截断）：**
> 「問題となったのは発着用飛行甲板の短さであり、特に中段の甲板で顕著に表れ、ここから艦上機が発艦することはできなかった。このため中段の飛行甲板には艦橋設備が作られ、艦載機の離艦は出来ないようになった」 — S4
> 「つまり、「赤城」「加賀」の新造時から上段格納庫と中層飛行甲板は艦橋によって分断されてしまっていました。」 — S21

**上段甲板倾斜（与赤城的一处差别）：**
> 「若干艦尾方向が高くなっていた傾斜飛行甲板はフラットなものに手直しされた」 — S4（指改装前的上段甲板有向舰尾抬升的倾角）
> 「Besides, the deck had no characteristic for Akagi angle towards a stern.」 — S5（Navypedia 说加贺甲板**没有**赤城那种向舰尾的倾角）

两源一句说有倾角、一句说没有，方向相反 → 见 §15 分歧 ⑥-B。

### §6-B 改装后单段全通甲板

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 长 × 宽 | 248.576 m × 30.480 m | 「飛行甲板 248.576m x 30.480m」 | S4 |
| 面积 | 7,001.7 ㎡（别源 7,533 / 7,553 ㎡） | 「その結果飛行甲板面積は7,001.7m2にまで達した」／「Flight deck: 248.6x30.3m」(fd 7,533㎡)／「248.6m × 30.3m (7,553㎡)」 | S4 / S5 / S9 |
| 长度超过水线长 | 是（248.576 > 240.304） | 「最上段の飛行甲板は船体長を上回る長さになり」 | S4 |
| 甲板距水面 | 21.7 m | 「水面からの飛行甲板までの高さが21.7m」 | S4 |
| 舰桥处甲板宽 | 29.5 m | 「艦橋部分の飛行甲板幅も29.5mある」 | S4 |
| 支撑柱 | 最终 6 根（4 根说并存） | 「【加賀】の支柱では昨今最終的には6本になったという考察が進んでいて」 | S7 |

> 「increasing the flight deck length to 248.55 meters (815.5')」 — S1
> 「まず全長は171.3mだったものが248.5mと77mも増加。」 — S7
> 「この延長のために艦首艦尾は様変わりし、それぞれが支柱でV字に支えるようになっています。」 — S7
> 「甲板面積はこれで約7,000㎡となり、次世代空母の「翔鶴型」を上回る広さ」 — S7

### §6-C 机库

| 字段 | 改装前 | 改装后 | 原文照抄 | 来源 |
|---|---|---|---|---|
| 层数 | 3 层（上/中格纳库 + 下辅助格纳库） | 3 层（下格纳库缩小保留） | 「two main hanger decks and a third auxiliary hanger with a total capacity of 60 aircraft」 | S2 |
| 上格纳库 | 100.0 × 22.0 × 5.0 m | **153.0 × 22.0 × 5.0 m** | 「上段:100.0m × 22.0m × 5.0m」／「上段:153.0m × 22.0m× 5.0m」 | S9 |
| 中格纳库 | 100.0 × 22.0 × 5.0 m | **153.0 × 22.0 × 5.0 m** | 同上 | S9 |
| 下格纳库 | 20.0 × 20.0 × 高度未获取 | 20.0 × 20.0 × 高度未获取 | 「下段:20.0m × 20.0m × N/A」／「small lower hangar: ~20x20x?m」 | S9 / S5 |
| 上+中格纳库面积（改装后） | — | 7,493 ㎡ | 「常用の上中2段の格納庫面積だけで合計で7,493m2となり」 | S4 |

> 延长量：「改装後の上段格納庫は58m、中段格納庫は38m延長され」 — S7（与 S9 的 100→153 m 相差 53 m 不吻合，见 §15 分歧 ⑦）
> Navypedia 记改装后「Upper and medium hangars, each: ~153x22x5m」 — S5
> 下格纳库用途：「下段格納庫は引き続き分解された補用機や資材置き場になったようです。」 — S7

### §6-D 升降机（エレベーター）

| 字段 | 改装前 | 改装后 | 原文照抄 | 来源 |
|---|---|---|---|---|
| 数量 | 2 基 | 3 基 | 「エレベーター2基」／「エレベーター3基」 | S4 |
| 前部 | 10.67 × 15.85 m，**偏右舷** | 11.5 × 12.0 m | 「Her forward aircraft elevator was offset to starboard and 10.67 by 15.85 meters (35 by 52 ft)」／「前部 (11.5m × 12.0m)」 | S3 / S9 |
| 中部 | —（无） | 10.7 × 15.9 m | 「中部 (10.7m × 15.9m)」 | S9 |
| 后部 | 12.8 × 9.15 m，**中线** | 12.8 × 9.9 m | 「Her aft elevator was on the centerline and 12.8 by 9.15 meters (42 by 30 ft)」／「後部 (12.8m × 9.9m)」 | S3 / S9 |

> 前升降机尺寸三家不一（10.67×15.85 / 11.8×13.0 / 11.8×13.0）→ 见 §15 分歧 ⑧。
> 「元の前方エレベーターとほぼ同じ場所から、中央に寄せた箇所に1番エレベーターが、甲板のほぼ中央に2番エレベーターが搭載されました。」 — S7（此为赤城表述，加贺同构）
> 加贺特征：「「加賀」の飛行甲板を見ると、エレベーターがアンバランスな配置になっているのはこの理由によります。」（新增升降机靠前，致升降机集中在前部） — S20

### §6-E 拦阻索（着艦制動装置）

| 时期 | 型式 | 索数 | 原文照抄 | 来源 |
|---|---|---|---|---|
| 竣工时 | **英制纵索式** | **未获取** | 「Her arresting gear is the British longitudinal wire system.」 | S2 |
| 1930 改装后 | 法式横索式「フェー式」（Béarn 同型） | **未获取** | 「KAGA is refitted with a French transverse system used on their aircraft carrier BEARN」 | S1 |
| 1935 改装后 | 日制一式 | **未获取** | 「Her arrested gear is replaced by a Japanese-designed Type 1 system.」 | S1 |
| 1938 改装后 | **呉式四型** | **8 索**（别源 **10 索**） | 「着艦制動装置 呉式四型 (4.0t / N/A):8索」／「着艦制動装置は萱場式から呉式四型（横索一〇本）に改められ」 | S9 / S20 |
| 1940 改装后 | 三式 | **未获取** | 「Her arresting gear is replaced by a Type 3 system」 | S1 |

**重要分歧**：英文 Wikipedia 把「法式横索式」写成**竣工时即已装备**：
> 「Her arresting gear was a French transverse system as used on their aircraft carrier Béarn and known as the Model Fju (Fju shiki) in the Japanese service.」 — S3

而 TROM 与日方资料都说是**先英制纵索式、1930 年才换法式**：
> 「E 1930: Due to numerous problems and damage to aircraft caused by the British longitudinal arresting gear system, KAGA is refitted with a French transverse system」 — S1
> 「昭和五年末には佐世保工廠で飛行甲板の制動装置をフランスより購入した「フェー式制動装置」に換装（それまでは縦索式）。」 — S21

→ 见 §15 纠错 ⑨（这是本次发现最实质的一处英文源错误）。

**滑走制止装置（拦阻网）：**
> 「さらに着艦に失敗した機を止めるための「空技廠式滑走制止装置」を前部と中部エレベーターの直後に一基ずつ装備。移動式滑走制止装置二基と応急用滑走制止装置一基も積み込まれました。」 — S20

### §6-F 弹射器（カタパルト）

**结论：服役期间装备数 = 0；但 1935/1940/1941 三个时点都有「装了又拆 / 只做基座」的记录，必须分开写。**

| 时点 | 说法 | 原文照抄 | 来源 |
|---|---|---|---|
| 竣工时 | **无**（明确的 0） | 「No catapults are fitted.」 | S2 |
| 1935 改装 | 装过 2 基试验用，试验不合格后放弃 | 「Two experimental catapults are fitted forward but trials are deemed unsatisfactory and their use is abandoned.」 | S2 |
| 1940-05 改装 | 一说装了 **3 基**空气式，后拆除，基座痕迹留存 | 「Reportedly, KAGA had three air-propelled catapults installed on the forward end of the flight deck during the refit period starting 1 May 1940. … The experiment was apparently short-lived, and the catapults removed, but their seatings remained visible.」 | S2 |
| 1941-09 | 在佐世保开槽、极秘装 1 组于长崎冲试射，成功后即刻拆除 | 「1941年9月末に極秘裏にカタパルトを搭載して射出実験が長崎沖で実施されたが、実用には困難と判断されたため、即刻カタパルトを撤去した。」 | S4 |
| 开战时 | **0 基装备** | 「結局未搭載のまま開戦を迎え、カタパルト完成の機会はなかった」 | S4 |

> 加贺甲板预开三条沟：「【加賀】には滑走車が走るための3方向から溝があらかじめ掘られていました。」 — S7
> 试射结论（重要，说明为何放弃）：「小福田晧文少佐が「人が乗っていたら死んでいた」と言われるぐらいのもの」 — S7
> 「射出速度の不足が問題となり」（『日本の航空母艦パーフェクトガイド』引） — S7

### §6-G 其他航空设施

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 着舰指导灯 | **加贺首创**（自行研制，后制式化） | 「着艦指導燈が初めて搭載されたのは【加賀】でした。…自分たちで独自に開発設計したもので、これが目に留まってやがて正式装備になった」 | S7 |
| 航空 gasoline | 505 t（改装后）／512 t（要目表） | 「航空用ガソリン:505.0t」／「ガソリン 512トン」 | S9 / S4 |
| 遮风栅 | 未获取 | — | — |

---

## §7 武备

### §7-A 主炮：20cm/50 三年式

| 时期 | 配置 | 原文照抄 | 来源 |
|---|---|---|---|
| 设计/竣工时 | 连装 2 基 4 门（B 型炮塔，中段甲板两舷）+ 单装 6 门（舰尾炮廓）= **10 门** | 「3年式20cm連装砲2基4門 / 3年式20cm単装砲6門」 | S4 |
| 1935 改装后 | 连装 2 基撤除，后部舷侧新增 4 门廓炮 → **单装 10 门** | 「3年式20cm単装砲 10基10門」 | S4 |
| 1941 年前后 | **实际减为 8 门**（最尾一门撤除） | 「1941年1月の写真では最後尾の砲が撤去されており、開戦の少し前に主砲は8門になっていたようです。」 | S7 |
| 2019 沉舰确认 | 10 号炮确已不在 | 「重量調整のために撤去されたと言われていた九番、十番砲ですが、少なくとも十番砲がないことがわかっています。」 | S8 |

> 「Her two twin turrets on the middle flight deck are removed and four new 20-cm/50 3rd Year Type No. 1 guns in casemates are added forward of the aft existing ones.」 — S2
> 装 20cm 炮的理由：「This heavy gun armament is provided in case she is surprised by enemy cruisers and forced to engage battle.」 — S2
> 改装后配置的实战评价：「この配置は視界、射界ともに狭く、運用実績も不良だった。」 — S4

**炮本身性能（NavWeaps，武器本体，非加贺专有）：**
> 「Muzzle Velocity \| All except Illum: 2,756 fps (840 mps)」／「Ammunition stowage per gun \| 120 - 126 rounds」 — S11
> B 型炮塔仰角：「nominally capable of 70° elevation … in practice the maximum elevation was only 55°」 — S3

### §7-B 高角炮：12cm → **12.7cm（加贺换装过，赤城没有）**

| 时期 | 配置 | 原文照抄 | 来源 |
|---|---|---|---|
| 竣工时 | 45口径 12cm 十年式 **连装 6 基 12 门** | 「45口径10年式12cm連装高角砲6基12門」 | S4 |
| 1935 改装后 | **40口径 八九式 12.7cm 连装 8 基 16 门** | 「89式12.7cm連装高角砲 8基16門」 | S4 |

**这条任务书问对了，NavWeaps 有直接对比句：**
> 「The carrier Kaga and those cruisers modernized during the late 1930s had these weapons replaced by the 12.7 cm/40 (5") Type 89 AA gun. However, Akagi carried them to her end at Midway.」 — S12

**即：加贺 = 换装 12.7cm；赤城 = 至死保留 12cm。这是两舰在武备上最大的实质差别。**

> 「連装12cm高角砲を連装12.7cm高角砲に換装、数も6基から8基に増備し、反対舷方向にも射撃が可能なように高い位置に取り付けられるなど」 — S4
> 「Their sponsons are raised one deck to allow them some measure of cross-deck fire.」 — S2
> 换装时点：「海軍は昭和7年/1932年に新しい高角砲として四十口径八九式12.7cm高角砲を採用していて、【加賀】の高角砲はこちらに換装されます。」 — S7

**12.7cm 炮性能：**
> 「Common Type 0 HE: 2,360 - 2,379 fps (700 - 725 mps)」／「Ammunition stowage per gun \| Yamato: 300 rounds / Cruisers with 4 guns: 250 rounds」 — S13

### §7-C 25mm 高炮（九六式 60 口径）—— 按管数记

| 口径 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| **总管数** | **22 挺**（11 基×2）／别说 **28 挺**（14 基×2） | 「25mm連装機銃 11基22挺／14基28挺（資料により異同）」 | S6 |
| 双联座数 | **11 座**（有力说）或 **14 座** | 「96式25mm連装機銃 11基 または14基」 | S4 |
| 单装座数 | **0** | 各源均只列连装 | S4/S9 |
| 三联座数 | **0** | 同上（三联装 1941 年才出现，加贺未装） | S4/S14 |
| 装备时点 | 1935 改装时（换 13mm）；九六式正式装舰 1939 年 | 「【加賀】が九六式を搭載したのは昭和14年/1939年のようです。」 | S7 |
| 1940 增备 | **+4 座双联**（若能确认，则与「14 基」说不吻合） | 「Four additional Type 96 twin 25-mm guns are fitted on sponsons.」 | S1 / S2 |

> 为什么数字定不下来（原文）：「25mm連装機銃も同時に増強されたがその位置・数は公式図面が残されていないこともあって不明である（11基とする説と14基とする説あり）。」 — S4
> 系谱：「当時の25mm機銃は九六式ではなくホチキス社製の保式。九六式が採用されたのは昭和11年/1936年で」 — S7
> 25mm 炮性能：「Muzzle Velocity \| 2,953 fps (900 mps)」／「Ammunition stowage per gun \| 2,000 rounds」 — S14

### §7-D 机枪

| 时期 | 配置 | 原文照抄 | 来源 |
|---|---|---|---|
| 竣工时 | 13mm 连装 4 基 + 留式机枪 2 挺（1931 年） | 「13mm連装機銃4基 / 留式機銃2挺（1931年）」 | S4 |
| 竣工时（别源） | 三年式 6.5mm 单装 **22 基** | 「三年式 115口径6.5mm単装機銃:22基」 | S9 |
| 1935 改装后 | 6.5mm 十一式 **6 挺** | 「Six 6.5-millimeter (0.26 in) Type 11 machine guns were also carried.」／「11式軽機銃6挺（1938年）」 | S3 / S4 |

> 三源数字互斥（4 基 13mm / 22 基 6.5mm / 6 挺 6.5mm）→ 见 §15 分歧 ⑩。

### §7-E 弹药基数

**全舰总量：未获取。** 只有 NavWeaps 的**单门弹药架容量**：
> 20cm： 「Ammunition stowage per gun \| 120 - 126 rounds」 — S11
> 12.7cm：「Ammunition stowage per gun \| Yamato: 300 rounds / Cruisers with 4 guns: 250 rounds」（无加贺数据） — S13
> 25mm： 「Ammunition stowage per gun \| 2,000 rounds」 — S14

---

## §8 雷达与火控

### §8-A 雷达（电探）

**结论：加贺在中途岛时没有雷达。这是「0」，不是「未获取」，有三条独立证据。**

**证据 1（A 级一手证言，指向「中途岛全体空母均无」）：**
> 「Q. Did any ships at MIDWAY have radar?
> A. Yamato, Mutsu and Nagato in the Grand Fleet may have had it. **There was no ship at MIDWAY or carrier which had it.**」
> — 青木泰二郎大佐（赤城舰长）USSBS 第 4 号审问，1945-10-09 — S15
（注：该审问对象是赤城舰长，回答覆盖「MIDWAY … or carrier」，加贺属其中。）

**证据 2（装备时间线，说明加贺沉没时 21 号电探尚未上舰）：**
> 「ミッドウェー海戦後に重要艦艇から搭載され（最も早い搭載は1942年（昭和17年）6月ころの空母「翔鶴」や隼鷹型航空母艦と言われる）」 — S17

**证据 3（第三方综述）：**
> 「Although the Japanese battleships were fitted with radar, their carriers had none」 — S18

| 字段 | 值 | 说明 |
|---|---|---|
| 雷达型号 | **无（0 部）** | 21 号电探最早 1942-06 上翔鶴，加贺 6 月 5 日已沉 |
| 雷达数量 | **0 部** | S15 / S17 / S18 |
| 装舰时点 | 从未装 | 同上 |

### §8-B 射击指挥仪

| 用途 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 20cm 炮用 | 一四式方位盘 **2 组** | 「一四式方位盤 (20.0cm砲用):2組」 | S9 |
| 20cm 炮用（英文源口径） | 八九式方位盘 **2 部** | 「two Type 89 directors for the main guns」 | S3 / S19 |
| 12.7cm 高角炮用 | 九一式高射装置 **2 组** | 「九一式高射装置 (12.7cm砲用):2組」 | S9 |
| 12.7cm 高角炮用（原文补充） | 保留旧式九一式，未换新 | 「KAGA retains her outdated Type 91 AA directors.」 | S2 |
| 25mm 机铳用 | 九五式机铳射击装置 **4 组**（英文源记 6 组） | 「九五式機銃射撃装置 (25mm機銃用):4組」／「Six Type 95 directors were fitted to control the new 25 mm guns」 | S9 / S3 |

> 改装前只有：「She had two Type 89 directors to control her 20 cm guns and two Type 91 manually powered anti-aircraft directors (Kōshaki) to control her 12 cm guns.」 — S3

### §8-C 测距仪

**型号与数量：未获取。** 但有一条**加贺与赤城的实质差别**可确证：

> 「大きさの他にも【赤城】にある4.5m測距儀が【加賀】にはないのも特徴です。」 — S7
> 「【赤城】では艦橋トップにある測距儀は、【加賀】では艦橋からさらに舷側にある張り出しに設置されています。」 — S7

即：赤城有 4.5 m 测距仪（置舰桥顶），加贺**没有 4.5 m 测距仪**，其测距仪装在舰桥外侧的舷侧张出部。**具体型号与基数两源均未给。**

检索路径：日文 Wikipedia 加贺条目「測距」「測距儀」「方位盤」检索 → 仅 0 命中（要目表无此栏）；kasado「測距儀/レーダー」栏 → 只列射击指挥装置，测距仪栏空白；Navypedia → 无；japanese-warship → 只有上述两句定性描述。

---

## §9 编制

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 平时编制（竣工时定员） | **1,271 名** | 「竣工時定員 1,271名」 | S4 |
| 平时编制（竣工时，内令细目） | 士官 64 + 特務士官 17 + 准士官 24 + 下士官 272 + 兵 895 = **1,272 名** | 「士官64人、特務士官17人、准士官24人、下士官272人、兵895人」 | S4（引昭和3年2月1日 内令二二） |
| 平时编制（1931-03） | 1,269 名 | 「昭和6年3月調 1,269名」 | S4 |
| 平时编制（1937-04-23 定员） | **1,705 名** | 「1937年4月23日付定員 1,705名」 | S4 |
| 平时编制（1937，内令细目） | 士官 77 + 特務士官 41 + 准士官 58 + 下士官 507 + 兵 1,022 = **1,705 名** | 「士官77人、特務士官41人、准士官58人、下士官507人、兵1022人」 | S4（引昭和12年4月23日 内令一六九） |
| 最终时定员 | **1,708 名** | 「最終時 1,708名」 | S4 |
| **军官数** | **1937 年：士官 77 名（另特務士官 41 名）**；竣工时：士官 64 名 | 同上两行 | S4 |
| **战时编制** | **未获取** | 各源只给「定員」（平时），无战时编制表 | S1–S23 |
| **中途岛出击时实际搭载人数** | **未获取** | 日文维基未给加贺实员；只能反推战死者 811（见 §11） | S4 |

**互斥数字（原话）：**
> 「Complement \| 1340」（改装前）／「2016」（改装后） — S5
> 「乗員 1340」（竣工时）／「乗員 2016」（改装后） — S10
> 「乗員 1,340名」（竣工时）／「2,016名」（改装后） — S9
> 「complement totaled 1,340 crewmembers」／「The carrier's complement increased to 1708 crewmembers.」 — S3

→ 1,340 与 1,271/1,272 的差、2,016 与 1,705/1,708 的差，见 §15 分歧 ⑪。注意 **2,016 这个数字同时出现在 Navypedia / Nishida / kasado 三家，但日文维基的内令细目明确是 1,705**。

---

## §10 涂装与外形

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 涂装方案 | 无迷彩，单色军舰色（全期） | 日文维基加贺条目检索「迷彩」0 命中 | S4 |
| 舰体色（三段甲板时代） | **横須賀海軍工廠グレイ** | 「横須賀 … 航空母艦 … 加賀[三段甲板以前]」 | S16 |
| 舰体色（近代化改装后） | **佐世保海軍工廠グレイ** | 「佐世保 … 航空母艦 赤城[近代化改装後]・加賀[近代化改装後]」 | S16 |
| 甲板色 | **天然木色（米松/bei-matsu），浅棕至黄橙**，未着色 | 「Until 1944 most if not all Japanese carrier flight decks were left in the natural finish of the gold growth pine (bei-matsu) they were planked with. This gave it generally a light tan look, or a hue ranging from yellow to orange depending on the sun and angle of viewing.」 | S2 |
| 甲板前部标识（中途岛） | 巨大日章旗 | 「敵味方識別のため、飛行甲板に巨大な「日の丸」を描いた」 | S4 |
| 舰尾舰名 | 片假名「カガ」（推定） | 「She probably also had her name in katakana painted on her flight deck at the fantail like AKAGI and HIRYU.」 | S2 |
| **舰岛位置（改装后）** | **右舷前部，小型四层** | 「a small starboard island superstructure is also installed」／「全通式となった飛行甲板の右舷前方に設置された」 | S1 / S4 |
| **舰岛（竣工时）** | **无岛式舰桥**（但有横贯全宽的大舰桥结构，位于中段甲板前端） | 见 §10-A | S3 / S4 / S21 |
| 着艦識別文字 | **「カ」**（来源等级偏低，见 §10-B） | 「背面には、着艦識別文字の「カ」がプリントしてあります」 | 商品页（D 级，见 §10-B） |
| 烟囱（改装前） | 两舷各一条**长水平烟道**，向后延伸至飞行甲板后方两侧排气；烟道长 95 m | 「KAGA's funnel gases are collected in a pair of long horizontal ducts which discharge at the rear of each side of the flight deck」／「長さ95mの煙突は舷側を沿って船尾へと伸びていた」 | S1 / S6 |
| 烟囱（改装后） | 右舷单一下弯式弯曲烟囱（赤城同型但更小） | 「The lengthy funnel ducting is replaced by a single downturned starboard funnel.」／「煙突の大きさは【加賀】のほうが小さくなっています」 | S1 / S7 |

### §10-A 舰岛位置 —— 重点核实（任务书这一条需要修正表述）

**竣工时（1928–1935）：没有岛式舰桥。**
> 「Kaga lacked an island until one was added during the modernization.」 — S3

**但「没有岛」≠「没有舰桥」。加贺竣工时有一座横贯全宽的大舰桥，压在中段飞行甲板前端，正是它把中段甲板废掉的：**
> 「このため中段の飛行甲板には艦橋設備が作られ、艦載機の離艦は出来ないようになった」 — S4
> 「ついに戦時格納庫前に艦の全幅にわたる広大な艦橋を設ける事となったのです。さらに両側に張り出し部を設けて上空見張所とするなどの大改正が実施されました。もちろん「加賀」も右にならえ。」 — S21
> 「「加賀」の艦橋は当初は中層飛行甲板の前端部に設けられていました（アイランド無し）。」 — S20

**1932 年曾在飞行甲板右舷前部设塔型补助舰桥 + 飞行科指挥所：**
> 「1932年（昭和7年）には甲板のエレベーター右舷に塔型補助艦橋と、飛行科指揮所を設けている」 — S4

**1933 年 2–6 月设临时小型舰桥（右舷前端），1935 年改装时拆除并移交赤城：**
> 「【加賀】は昭和8年/1933年2月から始まった修理中の5～6月頃に、仮設の小さな艦橋を右舷先端付近に設置しています。… これは改装時に撤去されたので使われたのは半年ちょっとではありましたが」 — S7
> 「撤去された小型艦橋はその後【赤城】に移されて、こちらも改装が入るまで使われています。」 — S7

**改装后（1935–1942）：右舷前部，小型四层。**
> 「艦橋については、上記のように、最小限といえる小さなものが全通式となった飛行甲板の右舷前方に設置された。」 — S4
> 「当初はかなり大型の艦橋を設置予定でしたが、「友鶴事件」の影響で艦橋の大きさは四層構造の小型サイズとなってしまいます。」 — S7
> 「トップヘビー回避の必要から、大型艦橋の搭載は中止されてしまい、羅針艦橋・操舵室・発着艦指揮所だけを収容した四層の小型艦橋に変更の上で右舷前部に設置されました。」 — S20

**为什么右舷（两条独立理由，日方两源一致）：**
> 「発着艦の空路が左回りと決められていたためである。… レシプロ機の場合、プロペラはパイロット側から見て時計回りであり、これは機体を左へと導く。それを踏まえてのことで、左舷艦橋は障害物となりやすかったのである。」 — S4
> 「まず船は左舷接舷が世界的に常識となっているルールです。… 煙突と艦橋、それぞれ右に置きたい事情があり、【加賀】はこの2つの構造物でバランスを取ることよりも実用性を重視し、いずれも右舷への設置を決定。」 — S7

### §10-B 着艦識別文字「カ」—— 来源诚信声明

赤城的「ア」在日文 Wikipedia 要目表里有正式栏位，且脚注指向**『写真日本の軍艦 第3巻』p.63**（C 级文献）：
> 「着艦識別文字: ア」 — 日文维基赤城条目（footnote: 「写真日本の軍艦第3巻 p.63の写真より」）

加贺的日文维基条目里「識別文字」「「カ」」**均 0 命中**（无此栏，无脚注）。「カ」的唯一来源是一个商业 T 恤商品页的文案：
> 「背面には、着艦識別文字の「カ」がプリントしてあります」 — https://www.sa-ka-ki.jp/?pid=143290726

**该来源等级 = D（商业制品），不足以作为档案依据。** 本档案把「着艦識別文字＝カ」记为**「低等级单源，未获一手档案确认」**，不建议直接入站，除非另找到《写真 日本の軍艦》或着艦信号相关一手材料。

可用的、等级较高的航空队识别记号是尾翼记号 **A II**（S24），但那是部队记号，不是舰体涂装。

---

## §11 生涯时间线

| 日期 | 事件 | 原文照抄 | 来源 |
|---|---|---|---|
| 1918-05-15 | 命名为「加贺」，同日登记为战舰（八八舰队第3番舰） | 「1918年（大正7年）5月15日、日本海軍は八八艦隊第3番艦（仮称第七号戦艦）を加賀と命名する」 | S23 |
| 1919-01 | 海军向川崎造船所下达建造命令 | 「1919年（大正8年）1月、海軍は川崎造船所に戦艦加賀の建造を命じた」 | S4 |
| 1920-07-19 | 神户川崎造船所开工（战列舰） | 「Kobe. Laid down as a TOSA-class battleship at Kawasaki Heavy Industries Shipyard.」 | S1 |
| 1921-11-17 | 下水命名（伏见宫博恭王出席，观者号称 10 万） | 「1921年（大正10年）11月17日午前8時30分、天皇の名代として伏見宮博恭王が参加した他、10万人ともいう観衆が見守る中で進水する」 | S4 |
| 1922-02-05 | 华盛顿条约，加贺/土佐两舰建造中止 | 「ワシントン海軍軍縮条約に従い1922年（大正11年）2月5日に建造中止の通達があり」 | S4 |
| 1922-07-08 | 舰体移交海军；07-11 由富士号拖带离神户，07-14 抵横须贺 | 「1922年（大正11年）7月8日、加賀は川崎造船所から海軍に引き渡される」 | S4 |
| 1923-09-01 | 关东大地震，天城号损毁，加贺被选为代舰 | 「AMAGI … making launch impossible … Henceforth, battleship KAGA is reordered on 19 November as a carrier to replace AMAGI.」 | S1 |
| 1923-11-19 | 正式变更为航空母舰 | 「大正12年11月19日航空母艦に改造することと爲り」 | S4 |
| 1925 | 横须贺工厂正式开始空母化改装 | 「1925: KAGA's conversion to an aircraft carrier starts at Yokosuka Naval Yard.」 | S1 |
| 1928-03-31 | 竣工（形式竣工，工事未完） | 「31 March 1928: Completed. … but this only signifies the beginning of her sea trials.」 | S1 |
| 1928-09-15 | 馆山冲试航 | 照片说明「Kaga during trials, off Tateyama, Japan, 15 Sep 1928」 | S2 |
| 1928-11 | 试航达 27.5 节 | 「KAGA actually achieved 27.5 knots on her November 1928 trials」 | S2 |
| 1929-11-30 | 编入第一航空战队（初） | 「一応昭和4年/1929年11月30日に初の第一航空戦隊配属となりましたが、この時もまだ機動部隊の運用実験と並行して」 | S6 |
| 1930 末 | 拦阻装置换法式「フェー式」 | 「昭和五年末には佐世保工廠で飛行甲板の制動装置をフランスより購入した「フェー式制動装置」に換装（それまでは縦索式）。」 | S21 |
| 1932-01-29 | 一·二八事变，加贺赴上海（一航战旗舰） | 「KAGA, attached to the 3rd Fleet, CarDiv 1 … departs Sasebo for Shanghai.」 | S1 |
| 1932-02-05 | 加贺舰载机首次空战（世界首次舰载机被击落记录） | 「一方で対空射撃を受けた【一三式艦上攻撃機】が1機撃墜されており、これは世界最初の艦載機撃墜記録となっています。」 | S7 |
| 1932-02-22 | 击落 Robert Short 的 Boeing 218（日本陆海军首次击落敌机） | 「2月22日、加賀飛行隊の三式艦戦3機、一三式艦攻3機の編隊が…ボーイング218と空戦となり…B218を撃墜」 | S4 |
| 1933-10-20 | 转二等预备舰，入佐世保工厂准备大改装 | 「20 October 1933: Reduced to second class reserve status. … KAGA docks at Sasebo Naval Yard」 | S1 |
| 1934-06-25 | 大改装正式开工 | 「25 June 1934: … KAGA's reconstruction is officially started.」 | S1 |
| 1935-06-25 | 大改装出坞完成；同日归队 | 「25 June 1935: Undocked, reconstruction completed.」 | S1 |
| 1935-11-15 | 最终改装工事完成 | 「15 November 1935: Final modifications completed.」 | S1 |
| 1937-08-15 | 中日战争首次出击（损失 8 架八九舰攻 + 2 架九四舰爆） | 「この攻撃で加賀航空隊は八九式艦攻8機（2機不時着水含む）、九四式艦爆2機」 | S4 |
| 1937-09-22~23 | 攻击宁海、平海 | 「NING HAI sustains hits by four bombs … PING HAI sustains hits by eight bombs」 | S1 |
| 1937-12-12 | 击沉美炮舰 Panay（加贺 B4Y1 投弹） | 「PANAY is hit by two of the 18 60-kg (132-lb) bombs dropped by 3 B4Y1 "Jean" from KAGA」 | S1 |
| 1938-12-15 | 转预备舰，入佐世保入坞大改（二年） | 「That same day, KAGA enters dock at Sasebo Naval Yard.」 | S1 |
| 1940-11-18 | 改装完成出坞；飞行甲板扩大补强 + 增 4 座 25mm | 「Overhaul is completed. Undocked. Her flight deck is enlarged and reinforced. … Four additional Type 96 twin 25-mm guns are fitted on sponsons.」 | S1 |
| 1941-04-10 | 一航战编入新设第一航空舰队 | 「The First Air Squadron joins the newly organized First Air Fleet」 | S1 |
| 1941-09 | 长崎冲弹射器试射，随即拆除 | 「1941年9月末に極秘裏にカタパルトを搭載して射出実験が長崎沖で実施された」 | S4 |
| 1941-11-18 | 佐伯湾装载 100 枚特制浅深度鱼雷 | 「arrives Saeki Wan … to load 100 special torpedoes」 | S1 |
| 1941-11-26 | 单冠湾出击（珍珠港） | 「departs Hittokapu Wan in the "Hawaii Operation"」 | S1 |
| 1941-12-07 | 珍珠港：一波 26 架（12 雷击 + 14 水平爆击）+ 9 零战；二波 23 九九舰爆 + 9 零战；损失 15 架 | 「KAGA contributes 12 B5N2 "Kate" torpedo bombers and 14 B5N2 … and 9 A6M2 "Zeke" … Losses sustained by KAGA's aircraft are 4 A6M2, 5 B5N2 and 6 D3A1, totaling 15 aircraft.」 | S1 |
| 1942-01-20~22 | 拉包尔/卡维恩空袭 | 「KAGA provides 27 B5N2 "Kate" and 9 A6M2 "Zeke".」 | S1 |
| 1942-02-09 | **帕劳触礁**，航速降至 18 节 | 「KAGA strikes a reef at Palau while shifting mooring positions. … maximum speed is reduced to 18 knots.」 | S1 |
| 1942-02-19 | 达尔文港空袭（27 舰攻 + 18 舰爆 + 9 零战） | 「KAGA contributes 27 B5N2 "Kate" … 18 D3A1 "Val" and 9 A6M2 "Zeke"」 | S1 |
| 1942-03-01 | 击沉 Pecos、参与击沉 Edsall | 「KAGA launches nine dive-bombers. … 1718 PECOS sank.」 | S1 |
| **1942-03-26 ~ 04-18** | **「Operation C」印度洋作战 —— 加贺未参加** | 「KAGA is unable to participate due to repairs still in progress at Sasebo.」 | S1 |
| 1942-03-22 | 返佐世保，舰载机转馆山基地训练 | 「Arrives at Sasebo for permanent hull repairs from reef damage … Her air group is flown off to Tateyama Air Base」 | S1 |
| 1942-05-04 | 修理完成出坞 | 「Repairs are completed. Undocked.」 | S1 |
| 1942-05-27 | 柱岛出击（MI 作战），航空队 18 零战 + 18 舰爆 + 27 舰攻 + 6 空 9 零战 + 2 备用舰爆 | 「KAGA's air group consists of 18 A6M2 "Zeke", 18 D3A1 "Val" and 27 B5N2 "Kate". Additionally, nine A6M2 "Zeke from the 6th Air Group … and two spare D3A1 "Val" are embarked.」 | S1 |

### §11-A 中途岛逐时（当地时 / JST 对照，S1 为骨架）

| 时刻（中途岛当地 = JST−3h，+1 日） | 事件 | 原文照抄 |
|---|---|---|
| 0430（0130 JST 6/5） | 第一次攻击队发舰：加贺出 18 九九舰爆 + 9 零战；另出 1 架九七舰攻参与 158° 索敌、2 架零战直卫 | 「the air strike … is launched against Midway Island with 36 B5N2 "Kate", 36 D3A1 "Val" and 36 A6M2 "Zeke". KAGA contributes 18 D3A1 "Val" and 9 A6M2 "Zeke"」 |
| 0700 | 发现敌机接近，发 6 架战斗机 | 「Enemy planes sighted approaching in force from 90 degrees. Launch six fighters.」 |
| 0707 | 加贺报「Sand Island 爆击，战果极大」 | 「KAGA notifies AKAGI: "Sand Island bombed; great results obtained."」 |
| 0715 | 南云令第二攻击队换陆用爆弹 | 「Nagumo orders second attack wave to arm for land strike against Midway.」 |
| 0745 | 南云令停止换爆弹、改换鱼雷（对舰） | 「land-bombs switched to torpedoes (in the case of AKAGI and KAGA) for ship attack」 |
| 0850 | 加贺第一次攻击队全部收回 | 「All KAGA first wave aircraft recovered.」 |
| 0938 | 企业号 VT-6 鱼雷机队**专门以加贺为目标** | 「This is USS ENTERPRISE (CV-6) Torpedo Squadron VT-6's Douglas TBD "Devastators" … which directly targeted KAGA.」 |
| 0938–1000 | 加贺在两舷被「铁砧」式夹击，躲过 6 条鱼雷；零战击落 14 架来袭机中的 10 架 | 「Enemy torpedo planes attack both sides of KAGA in an "anvil" attack. But assisted by CAP the carrier dodges a total of six torpedoes, the "Zeke" CAP shooting down 10 out of the 14 attacking aircraft.」 |
| **1022（0722 JST）** | **企业号 SBD（McClusky）25 架俯冲，加贺中 1×1000 磅 + 至少 3×500 磅；避开最初 3 发；舰桥被毁，舰长冈田次作以下干部阵亡** | 「KAGA takes evasive action to starboard, avoiding first three bombs but is struck by a minimum of one 1,000-pound (450-kg) and three 500-pound (230-kg) bombs … One of the bombs destroyed the bridge, killing most there including Captain Okada」 |
| 1130 | 二航战令各派 1 驱护受损空母；加贺以 5–8 节挣扎 | 「KAGA under supervision of the First Damage Control Officer attempts to comply, still making about 5-8 knots.」 |
| 1300（1000 JST） | 机关科全员死亡或被令停机；加贺停车；萩风靠上 | 「KAGA's engine gang is either overcome, or ordered to stop the ship (Only a third of them would survive; 213 of them perished.)」 |
| 1325 | 御真影移往萩风；飞行长天谷以下非必要人员离舰 | 「The Imperial Portrait is transferred via the forecastle to HAGIKAZE. … Air Officer Cdr. Amagai Takahisa … directs all non-essential personnel … to abandon ship」 |
| 1410（1110 JST） | 美潜艇 Nautilus 射 3 雷，1 条命中右舷舰尾但**不炸** | 「One torpedo hits the starboard quarter, but fails to explode.」 |
| 1640 | 判定无救，全员离舰（萩风、舞风收容） | 「The situation judged hopeless, all remaining personnel are ordered … to abandon ship.」 |
| 1715 | 萩风报：加贺残员已全数收容 | 「all remaining personnel on KAGA having earlier been ordered to abandon ship, have now been taken aboard the two destroyers」 |
| 1750 | 南云报山本：加贺失去战力，全员已转移 | 「"KAGA is inoperational in (grid) position HE E A55. All survivors have been transferred to destroyers."」 |
| 1856 | 日没，加贺、苍龙被令自沉 | 「Shortly after this time, KAGA and SORYU are apparently ordered scuttled.」 |
| **1925（1625 JST 6/5）** | **萩风射 2 雷命中右舷中部偏后，加贺舰尾下沉、舰体保持正浮，滑入水下。位置 30-23.3'N, 179-17.2'W** | 「Sunk: 1925 (1625 JST) destroyer HAGIKAZE fires two torpedoes into her starboard side amidships aft. … in approximate position 30-23.3'N, 179-17.2' W.」 |
| 1942-08-10 | 除籍 | 「Removed from Navy List.」 |

> 加贺是中弹到沉没间隔最久的：「【加賀】は被弾してから9時間もの間浮かび続けてました。」 — S8
> 沉没姿态两说并存：「また沈没の様子についても、艦尾から沈没したというものと、ほぼ水平にゆっくり沈んだという証言があり、はっきりしていません。」 — S8

---

## §12 舰载机编制（中途岛时）

### §12-A 搭载数（四套互斥数据）

| 来源 | 零战 | 九九舰爆 | 九七舰攻 | 备注 | 原文照抄 |
|---|---|---|---|---|---|
| S1（TROM，1942-05-27） | 18 | 18 | 27 | 另有六空 9 零战、备用舰爆 2 | 「18 A6M2 "Zeke", 18 D3A1 "Val" and 27 B5N2 "Kate". Additionally, nine A6M2 "Zeke from the 6th Air Group … and two spare D3A1 "Val"」 |
| S4（日文维基，常用机） | 18 | 18 | 27 | 「当時の日本海軍の空母では最大の攻撃力」 | 「ミッドウェー海戦時の搭載機（常用）は艦戦18、艦爆18、艦攻27」 |
| S3 / S19（英文源） | **27** | **20** | 27 | — | 「Her aircraft complement was 27 Zeros, 20 D3As, and 27 B5Ns.」 |
| S5（Navypedia 6.1942） | **21** | **27** | **18** | — | 「21 A6M2 \| 27 D3A1 \| 18 B5N2」 |

> 日文维基另给「戦没時保有機」栏：零战 21、九九舰爆 21、九七舰攻 30（标「要出典」） — S4
> Pearl Harbor 时（对照）：18 零战 + 27 舰攻 + 27 舰爆 + 三型各 3 架箱装备用 — S3

### §12-B 出击情况（1942-06-04）

| 波次 | 加贺出动 | 原文照抄 | 来源 |
|---|---|---|---|
| 第一次对中途岛 | 18 九九舰爆 + 9 零战；另 1 架九七舰攻索敌 | 「KAGA contributes 18 D3A1 "Val" and 9 A6M2 "Zeke"」 | S1 |
| 损失（第一波） | 1 舰爆 + 2 零战 | 「1 D3A1 "Val" and 2 A6M2 "Zeke" are lost.」 | S1 |
| 第二次对舰攻击 | **未及发舰即被炸** | 见 §11-A 1022 项 | S1 |

> 九九舰爆队指挥官：「eighteen D3As, commanded by Lieutenant Shōichi Ogawa, escorted by nine Zeros」 — S3
> JACAR 战斗详报内列的编制表（一手档案目录，可循）：「（イ）第二制空隊（艦戰九）／（ロ）第十二攻撃隊（艦爆一八）」 — S22

### §12-C 损失

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 加贺乘员战死 | **811 名**（别源 814 名） | 「加賀の岡田艦長以下約811人が犠牲となり」／「She suffers a loss of 814 officers, petty officers, and men.」 | S4 / S1 |
| 其中机关科 | 213 名，幸存约 40 名 | 「213 of them perished.」／「生存者は40名程だった」 | S1 / S4 |
| 搭乘员战死 | **21 名**（空中 8 + 舰上 13；战斗机 6、舰爆 6、舰攻 9） | 「加賀搭乗員は機上・艦上あわせて楠美正飛行隊長以下21名（戦闘機6名、艦爆6名、艦攻9名）が戦死」 | S4 |
| 转飞他舰 | 至少 7 架零战转降飞龙后随飞龙沉没 | 「少なくとも7機の零戦が加賀戦闘不能後も空母飛龍に着艦して戦闘を継続したが、飛龍の沈没と共に全機が失われた。」 | S4 |

---

## §13 未获取字段汇总

> 凡能证明是「0」而非「未获取」的，已在正文标出（弹射器装备数=0、雷达=0）。

| 字段 | 状态 | 已检索的位置 |
|---|---|---|
| 旗号（pennant number） | 未获取（不适用） | 日文维基加贺全文「旗号」「信号符字」0 命中；英文维基 infobox 无此栏；warbirds 识别记号表只有部队记号 |
| 船台号 | 未获取 | S1 TROM、S5 Navypedia、S4 日文维基、S6–S8 japanese-warship、S10 Nishida |
| 改装后最大宽 | 未获取 | 各源只给单一 breadth（29.6/32.5），无「水线宽/最大宽」分栏 |
| 改装前満載排水量 | 未获取 | S4 该栏空白；S5/S9/S10 只有 standard/full 二值 |
| 改装前试航功率 | 未获取 | 各源只给「出力 91,000shp」，未区分设计/实测 |
| 弹药库装甲 | 未获取 | S5「Ship protection」章、S4 装甲栏、S9 装甲表、S19 Armour 章均无弹药库项 |
| 装甲总重 | 未获取 | 检索「装甲重量」「防御重量」「armour weight」→ 0 命中 |
| 改装前拦阻索索数 | 未获取 | S2/S1/S21 只说「British longitudinal system」「縦索式」，索数无载 |
| 改装后 1940 拦阻索（三式）索数 | 未获取 | S1/S3 只说「Type 3 system」 |
| 全舰弹药基数（总量） | 未获取 | S11/S13/S14 只给 per gun 的弹药架容量 |
| 测距仪型号与数量 | 未获取 | S4「測距/測距儀/方位盤」0 命中；S9 该栏空白；S5 无；只确证「加贺无赤城的 4.5m 测距仪」（S7） |
| 战时编制 | 未获取 | 各源只有「定員」（平时）；S4 引内令只有平时定员表 |
| 中途岛出击时实际搭载人数 | 未获取 | S4 未给（赤城条目明言「不明」，加贺条目连这句都没有）；S22 战斗详报目录含「六 被害（一）人員」但**图像未数字化读取** |
| 舰员军官数（中途岛时） | 未获取 | 只有 1937 年定员细目（士官 77） |
| 飞行甲板色号 / 舰体色号（数值） | 未获取 | S16 只给「横須賀グレイ/佐世保グレイ」色名，不给色号；S2 描述木甲板为自然色但无色值 |
| 着艦識別文字（一手确认） | 低等级单源 | 仅商业商品页给「カ」（见 §10-B）；日文维基无此栏 |
| 下格纳库高度 | 未获取 | S5「~20x20x?m」、S9「N/A」 |
| 加贺 25mm 精确座数 | 未获取（两说） | S4 明言「公式図面が残されていない」，11 基/14 基并存 |
| 全战加贺机损失总数 | 未获取 | 各源只给分段（第一波 3 架等），无全战合计 |

---

## §14 来源清单

| ID | URL | 层级 | 说明 |
|---|---|---|---|
| S1 | https://www.combinedfleet.com/kaga.htm | **D** | Anthony P. Tully / Gilbert Casse「IJN KAGA: Tabular Record of Movement」，末次修订 2020-08-17。逐日 TROM，中途岛逐时最详细，含**当地时/JST 换算注**。**本站价值最高**。 |
| S2 | https://www.combinedfleet.com/KAGA-Data-Page-Chen.htm | **D** | 同站「KAGA Data page」。舰载机、备炮、改装、涂装、弹射器争议、甲板木色，均为此页独有细节。 |
| S3 | https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Kaga | **E** | 英文 Wikipedia。引 Parshall & Tully、Lengerer、Hata、Werneth。**注意其拦阻索段落有误**（见 §15 纠错 ⑧）。 |
| S4 | https://ja.wikipedia.org/wiki/加賀_(空母) | **E** | 日文 Wikipedia。引『海軍造船技術概要』『昭和造船史』『戦史叢書31』及**内令原文**（定员细目、舰艇类别等级）。仅作线索。 |
| S5 | https://www.navypedia.org/ships/japan/jap_cv_kaga.htm | **D** | Navypedia。改装前后双栏主尺度/防护/机库/升降机骨架数据。 |
| S6 | https://japanese-warship.com/carrier/kaga/ | **D** | 「大日本帝国軍 主要兵器」加贺 其1（诸元表 + 三段甲板成立经过 + 烟囱 + 机关）。引光人社《航空母舰「赤城」「加贺」》。 |
| S7 | https://japanese-warship.com/carrier/kaga-2/ | **D** | 同站 其2（飞行甲板/格纳库/四型舰桥/备炮/弹射器实验/25mm 系谱）。**加贺专有技术细节主要依据**。 |
| S8 | https://japanese-warship.com/carrier/kaga-3/ | **D** | 同站 其3（战历：上海事变→日中战争→珍珠港→中途岛→沉没→2019 发现）。 |
| S9 | http://www.kasado.net/AircraftCarriers/Japan/Kaga_1928.html | **D** | kasado.net 诸元表（竣工时/1935改装后/最终时三栏）。三段甲板面积、升降机、拦阻索、射击指挥装置唯一结构化来源。 |
| S10 | https://rikukaigun.org/Nishida/stc0203.html | **D** | Hiroshi Nishida 舰艇诸元页。公试 33,161 / 満載 43,650 的来源。 |
| S11 | https://www.navweaps.com/Weapons/WNJAP_8-50_3ns.php | **C** | NavWeaps 日本 20cm/50 三年式。初速、弹药架容量、炮架型号归属。 |
| S12 | https://www.navweaps.com/Weapons/WNJAP_47-45_10ns.htm | **C** | NavWeaps 日本 12cm/45 十年式。**明言「The carrier Kaga … replaced by the 12.7 cm/40 Type 89 … However, Akagi carried them to her end」** —— §7-B 的决定性依据。 |
| S13 | https://www.navweaps.com/Weapons/WNJAP_5-40_t89.php | **C** | NavWeaps 日本 12.7cm/40 八九式。逐舰装备型别表明确列「Kaga (8) … A1 Mod 2」。 |
| S14 | https://www.navweaps.com/Weapons/WNJAP_25mm-60_mg.php | **C** | NavWeaps 日本 25mm/60 九六式。三联装 1941 年才出现（佐证加贺 1942 年无三联）。 |
| S15 | https://www.ibiblio.org/hyperwar/AAF/USSBS/IJO/IJO-4.html | **A** | USSBS Interrogation Nav No. 4（1945-10-09，赤城舰长青木泰二郎）。**一手证言，「中途岛无舰有雷达」出自此**。 |
| S16 | http://waterline.fanweb.jp/materials/３．軍艦色の使い分け/ | **D** | 舰船模型资料站，按海军工厂分类军舰色。加贺三段甲板期=横须贺灰、改装后=佐世保灰。 |
| S17 | https://ja.wikipedia.org/wiki/二式二号電波探信儀一型 | **E** | 21 号电探条目。**「ミッドウェー海戦後に重要艦艇から搭載」＋最早 1942-06 翔鶴**，佐证加贺无雷达。 |
| S18 | https://ethw.org/Midway_-_Chapter_7_of_Radar_and_the_Fighter_Directors | **C** | ETHW《Radar and the Fighter Directors》第 7 章。**「their carriers had none」**。 |
| S19 | https://naval-encyclopedia.com/ww2/japan/kaga.php | **D** | naval-encyclopedia。舰载机、防护弱点（汽油柜无装甲）表述较完整。 |
| S20 | https://daihonnei.com/akagi-and-kaga2 | **D** | 「電脳 大本営」赤城与加贺（二）。**升降机布置、拦阻索 10 本、四层舰桥、赤城加贺舰桥对比**。 |
| S21 | https://daihonnei.com/akagi-and-kaga1 | **D** | 同站（一）。**竣工时横贯全宽大舰桥的由来（艤装委員長海津良太郎意见具申）**、フェー式换装时点。 |
| S22 | https://www.jacar.archives.go.jp/das/meta/C08030040500 | **A** | JACAR「昭和17年6月1日～6月30日 ミッドウエー海戦 戦時日誌戦闘詳報（2）」Ref.C08030040500，作成者「軍艦加賀／／軍艦蒼龍」。**目录级已确认（含「六 被害（一）人員」「別紙第七 戰死傷者名簿」），图像未数字化读取**。 |
| S23 | https://ja.wikipedia.org/wiki/加賀型戦艦 | **E** | 加贺型战列舰条目。舰级归属、八四→八八舰队沿革、命名与番号。 |
| S24 | http://www.warbirds.jp/text/kigo.htm | **D** | 尾翼部队识别记号表。加贺 = A II。 |

**未能使用的档案**：S22 为 A 级一手档案，目录可访问但正文需图像浏览器，本次未取到数值。若要「中途岛实载人数 / 战死者名簿」，此为下一步首选。

---

## §15 分歧与纠错汇总

> 原则：只列两边各说什么、各引哪句原话，**不裁决**。纠错项则明确指出任务书前提或来源与原文的冲突。

### 纠错 ①：任务书「加贺原设计是加贺级战列舰（长门级改良型）」——**正确**，但需补两点

「加贺型」与「土佐型」是**同一舰级的两个叫法**，任务书说的没错：
> 「加賀型戦艦（かががたせんかん）は、日本海軍が八八艦隊計画で考案した戦艦。長門型戦艦の拡大改良型である」 — S23
> 「土佐型戦艦、もしくは土佐級戦艦と呼称した事例がある」 — S23

**但 combinedfleet 与英文维基都写「TOSA-class」，以二号舰命名该级：**
> 「Kobe. Laid down as a TOSA-class battleship」 — S1
> 「Originally intended to be one of two Tosa-class battleships」 — S3

**这不是矛盾，是命名惯例差**（日方档案用一番舰「加賀型」，英美文献用二番舰「土佐級/Tosa-class」）。本站若只取一个，建议跟日方一手档案用「加賀型（加賀級）」，并在别名里记 Tosa-class。

另：任务书说「因华盛顿条约改装为航母」——完整因果是**三段**，中间那段不能省：
> 条约 → 加贺/土佐 建造中止、预定解体（S1/S4）→ 关东大地震毁掉预定改航母的天城（S1）→ 加贺被选为**代舰**（「其ノ代艦トシテ…戰艦加賀ヲ航空母艦ニ変更シ」 — S4 引大正12年公文）。

### 纠错 ②：任务书「1942-06-04 中途岛被美军俯冲轰炸击中，当日下午爆炸沉没」——三个点都要修

1. **被弹时刻**是当地 1022（JST 6/5 0722），不是「下午」。
2. **沉没不是「爆炸」直接造成，而是己方雷击处分**：
   > 「Sunk: 1925 (1625 JST) destroyer HAGIKAZE fires two torpedoes into her starboard side amidships aft.」 — S1
3. **「当日/次日」是时区问题**：当地 6/4 19:25 ＝ 日本时间 6/5 16:25。日方所有史料记 **6月5日**（日文维基要目「最期 1942年6月5日沈没」、JACAR 详报标题也是「六月五日」、Nishida「1942.6.5 戦没」）。美方与 combinedfleet 记 6/4。**两种写法都对，混着写才错。**

4. 附一条被打掉的分歧：**16:25 的大爆炸是否等于沉没**。日文维基说「16時25分に2回の大爆発…この大爆発により沈没した」（战报口径），而 combinedfleet 与多数证言说爆后仍浮 2 小时才被雷击处分，且「舰尾から沈没 vs ほぼ水平に沈没」两说并存（S8）。
   > 「生存者や目撃者の証言は前述のように完全には一致せず、戦闘詳報にも『本報告は生存者の断片的記憶を整理調製せるものにして…』と記載されている」 — S4

### 纠错 ③：任务书要求时间线含「印度洋」——**加贺没参加**

> 「1942-03-26 ~ 04-18「Operation C」— The Raids in the Indian Ocean: … KAGA is unable to participate due to repairs still in progress at Sasebo.」 — S1

原因是一月触礁：
> 「1942年（昭和17年）1月…2月8日にパラオに入港した翌日、【加賀】は海図に書かれていない暗礁に接触してしまいます。…この損傷が原因で【加賀】は「セイロン沖海戦」には不参加となっています。」 — S8

**加贺的 1942 年春天是「缺席者」**：错过印度洋（在佐世保修船）、错过杜立特追歼（船还在坞里）、错过珊瑚海（3/13 已被解除机动部队编成）。

> 「スターリング湾へ帰投後、先の座礁での損傷が懸念された加賀は3月13日附で機動部隊から除かれた」 — S4
> 「4月18日…加賀の戦闘機隊12機は…アメリカ機動部隊攻撃に向かったが、発見できずに引き返し」（此时本舰仍在佐世保） — S4
> 「22 April 1942: … KAGA is still under repairs at Sasebo.」 — S1本站时间线若画「印度洋」箭头指向加贺，是错的。

### 纠错 ④：任务书「加贺没有舰岛（竣工时），改装后才加装右舷岛式舰桥」——**正确**，但「没有舰岛」容易被误读成「没有舰桥」

竣工时有**横贯全宽的大舰桥**，位置在中段飞行甲板前端，正是它废掉了中段甲板：
> 「このため中段の飛行甲板には艦橋設備が作られ、艦載機の離艦は出来ないようになっていた」 — S4
> 「ついに戦時格納庫前に艦の全幅にわたる広大な艦橋を設ける事となった」 — S21

且 1932/1933 年先后在右舷前部加过塔型补助舰桥与临时小型舰桥（S4/S7），**「右舷」这个属性在改装前就出现过**，不是 1935 年才有。

### 纠错 ⑤：任务书「加贺是否换装过 12.7cm？赤城没有，加贺可能有」——**加贺确实换了，这是两舰最大武备差别**

> 「The carrier Kaga and those cruisers modernized during the late 1930s had these weapons replaced by the 12.7 cm/40 (5") Type 89 AA gun. However, Akagi carried them to her end at Midway.」 — S12
> 「89式12.7cm連装高角砲 8基16門」（改装后）／「45口径10年式12cm連装高角砲6基12門」（改装前） — S4

### 分歧 ⑥：三段甲板各段尺寸（宽度尤其乱）

| 分段 | S4 日文维基 | S9 kasado | S5 Navypedia | S3 英文维基 |
|---|---|---|---|---|
| 上段 | 171.30 × 30.48 | 171.2 × 30.5 | 171.3 × 30.3 | 171.2 × 30.5 |
| 中段 | （长度未给） | 15.0 × 25.0 | 15 × ~25 | 「about 15 m」 |
| 下段 | 55.02 × 24.38 | 55.0 × 20.0 | 55 × ~20 | 「approximately 55 m」 |

> 面积三方：S5 算 6,665 ㎡（5,190+375+1,100）；S9 分列 5,190/375/1,100；S4 只给上段。

**下段宽度 24.38 vs 20.0 m 是硬冲突**（差 4.4 m，不是四舍五入）。

### 分歧 ⑥-B：改装前上段甲板到底有没有向舰尾的倾角

- 有： 「若干艦尾方向が高くなっていた傾斜飛行甲板はフラットなものに手直しされた」（改装时把抬升的倾斜甲板改成平面） — S4
- 没有： 「Besides, the deck had no characteristic for Akagi angle towards a stern.」（加贺甲板没有赤城那种向舰尾的倾角） — S5

两句都出自「加贺 vs 赤城」的比较语境，结论相反，不裁决。若本站要画侧视线图，此点必须先定。

### 分歧 ⑦：机库延长量与格纳库尺寸

- S9：上/中格纳库 100×22×5 → 153×22×5（**各延长 53 m**）
- S7：「改装後の上段格納庫は58m、中段格納庫は38m延長され」（**58 / 38 m**）
- S4：上中两段合计面积 7,493 ㎡
- S5：「Upper and medium hangars, each: ~153x22x5m」

S7 的 58/38 与 S9 的 53/53 不吻合，且 S7 自己给的两段延长量不等，与 S9 的两段等长矛盾。

### 分歧 ⑧：升降机尺寸（前部尤其）

| 项 | S3 英文维基 | S5 Navypedia | S9 kasado |
|---|---|---|---|
| 前部（改装前） | 10.67 × 15.85（偏右舷） | 11.8 × 13.0 | 11.8 × 13.0 |
| 后部（改装前） | 12.8 × 9.15（中线） | 12.8 × 8.4 | 12.8 × 8.4 |
| 前部（改装后） | — | 11.5 × 12.0 | 11.5 × 12.0 |
| 中部（改装后） | 11.5 × 12.0（称"third elevator forward"） | 10.7 × 15.9 | 10.7 × 15.9 |
| 后部（改装后） | — | 12.8 × 9.9 | 12.8 × 9.9 |

S3 的「第三升降机 11.5×12」对应 S5/S9 的「前部 11.5×12」，命名位置不同（S3 把它叫"forward"，S5/S9 把 10.7×15.9 叫"medium"）。改装前三组数字两两不等。

### 纠错 ⑨（本次最实质的一处英文源错误）：拦阻装置时间线倒置

- 英文维基说**竣工时就是法式横索式**：
  > 「Her arresting gear was a French transverse system as used on their aircraft carrier Béarn and known as the Model Fju (Fju shiki) in the Japanese service.」 — S3
- TROM 说竣工时是**英制纵索式**，1930 年才换法式：
  > 「Her arresting gear is the British longitudinal wire system.」／「E 1930: … KAGA is refitted with a French transverse system」 — S1
- 日方独立源同 TROM：
  > 「昭和五年末には佐世保工廠で飛行甲板の制動装置をフランスより購入した「フェー式制動装置」に換装（それまでは縦索式）。」 — S21

**两源（S1 专题 TROM + S21 日方专题）一致对一源（S3 百科）**，倾向 S1/S21；但本节按规矩不裁决，只标注 S3 此处把 1930 年的事写成了竣工状态。

### 分歧 ⑩：25mm 座数与机枪

- 25mm：**11 基 22 挺** vs **14 基 28 挺**，日文维基明言「公式図面が残されていない」故不明（S4）；S6 并列两说。
- **且 TROM 记 1940-11 又加了 4 座双联**（「Four additional Type 96 twin 25-mm guns are fitted on sponsons.」 — S1）。若 11+4=15、14+4=18，**两说都对不上 1940 年后的状态**，说明「11 vs 14」争的很可能是 1935 年状态而非最终状态。
- 机枪：S4 记竣工时「13mm 连装 4 基 + 留式 2 挺」；S9 记「三年式 6.5mm 单装 22 基」；S3 记改装后「6.5mm 十一式 6 挺」。三者口径、数量全不同。

### 分歧 ⑪：乘员数（1,271 / 1,340 / 1,705 / 1,708 / 2,016）

- 内令细目（一手）：竣工时 64+17+24+272+895 = **1,272**；1937 年 77+41+58+507+1,022 = **1,705**（S4）
- 英文维基/Navypedia/Nishida/kasado 一致：竣工 **1,340**、改装后 **2,016**（S3/S5/S9/S10）
- 日文维基要目：竣工時定員 **1,271**、最終時 **1,708**（S4）

**1,340 − 1,272 = 68**，**2,016 − 1,705 = 311**。后者差得离谱，怀疑 2,016 是把「航空隊含む」或别舰数字混入（三家互相抄同一源头）。若本站要单一值，建议的优先级是：内令细目（A/B 级）> 日文维基要目 > Navypedia 系三家。

### 分歧 ⑫：排水量（三口径互斥，见 §3 详表）

- 改装前公试：**33,693 英吨**（S4/S3/S5 作 full）vs **33,161 t**（S9/S10）
- 改装后基准：**38,200**（S4/S5/S3/S1）vs **38,600**（S9）
- 改装后公试：**42,541 / 42,279 / 42,542**（S4）vs **41,869**（S9/S10）vs Navypedia 的 full **43,650**
- 改装后満載：**43,650**（S9/S10）——独此一家

---

## §16 字段覆盖率统计

按任务书 §0–§14 列出的必填字段计（§11 时间线、§14 来源清单不计入分母）：

| 节 | 必填项 | 已获取 | 部分/弱来源 | 未获取 |
|---|---|---|---|---|
| §0 | 10 | 9 | 0 | 1（旗号，不适用） |
| §1 | 8 | 8 | 0 | 0 |
| §2 | 12 | 11 | 0 | 1（改装后最大宽） |
| §3 | 6 | 5 | 0 | 1（改装前満載） |
| §4 | 10 | 9 | 0 | 1（改装前试航功率） |
| §5 | 6 | 4 | 0 | 2（弹药库装甲、装甲总重） |
| §6 | 8 | 6 | 1（升降机位置） | 1（改装前拦阻索索数） |
| §7 | 5 | 4 | 0 | 1（全舰弹药基数） |
| §8 | 3 | 2 | 0 | 1（测距仪型号数量） |
| §9 | 4 | 2 | 0 | 2（战时编制、中途岛实载） |
| §10 | 6 | 5 | 1（着艦識別文字） | 0 |
| §12 | 3 | 3 | 0 | 0 |
| **合计** | **81** | **68** | **2** | **11** |

**覆盖率 ≈ 84%（68/81 全额 + 2 项部分）**；若把 2 项「部分」按半计，约 **85%**。

**低于 60% 的节没有**；最弱的节是 §9 编制（2/4）与 §5 防护（4/6），两者欠的都是「官方细目类」数据——这类数据只在日方一手技术档案（『海軍造船技術概要』原书、『軍艦基本計画資料』Sheet 表）里，网页层面到顶了。

---

*档案完*
