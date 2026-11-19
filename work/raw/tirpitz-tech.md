# Tirpitz（提尔皮茨号）技术数据 — 相对 Bismarck 的差异汇总

> 采集目标：只记录 Tirpitz 与 Bismarck **不同**的值。凡标注「与 Bismarck 相同」的，直接继承 `data/classes/bismarck.yaml` + `data/ships/bismarck.yaml`，本文不重复抄写。
>
> 体例说明：
> - 每个数值后 `[缩写]` = 来源，末尾有缩写 → URL 对照表。
> - `【分歧】` 开头的是多来源互相冲突的值，**全部列出，不做裁决、不取平均**。
> - `【推断】` 是我从多个来源推算/换算出来的，不是任何单一来源直接写的。
> - 口径一律写清：mt = 公吨（metric ton），lt/tn.l. = 长吨（2240 lb），st = 短吨（2000 lb）。
> - 查不到的写「未获取」，并在第 11 节列出试过的 URL 与返回码。

---

## 0. 一句话总览

Tirpitz 相对 Bismarck 的**实体差异**只有七处可确证：更长（+1.1~3.1 m，取决于信哪家）、更重（+1,200 lt 上下）、多了**巡航汽轮机**、10.5cm 炮座**全部统一为 C/37**、加装**两座四联 533mm 鱼雷管**、2cm 高炮从 12 门一路加到 **58~78 门**、雷达换成 FuMO 27 → FuMO 26 + FuMO 213。装甲基本没动，动力装置标称值没动。

---

## 1. 排水量（Displacement）

| 口径 | Tirpitz 值 | 来源 | 备注 |
|---|---|---|---|
| 空载（empty） | **未获取** | — | 没有任何来源单独给 Tirpitz 的空载值；`data/classes/bismarck.yaml` 的 40,250 mt 是 **Bismarck** 的，不能直接套 |
| 标准（standard） | **43,900 mt** | [kb-tirpitz] | 该站 Tirpitz 专页技术数据块原文「standard 43,900 mt」 |
| 标准 | **43,978 mt** | [kb-genedata] | 注意：这是 Bismarck 的值，该站对比表里 Tirpitz 栏原样抄了 Bismarck 的数，**与本站 tirpitz.html 的 43,900 自相矛盾** |
| 标准 | **42,900 t** | [navypedia-bb] | 与 Bismarck（41,700 t）并列给出，差 +1,200 t |
| 标准 | **42,900 t = 42,200 lt** | [enwiki] | 明确标注 42,200 长吨 |
| 标准 | **41,700 tn.l.** | [dewiki] | 德文维基 Infobox 写的是 **tn.l.（长吨）**，不是公吨；41,700 lt ≈ 42,370 mt。dewiki 正文同时说「Bismarck 41.700 tn.l.，Tirpitz 42.900 tn.l.」——**Infobox 的 41,700 与正文的 42,900 在同一篇文章里对不上**，Infobox 疑似漏改 |
| 建造排水量（construction） | **45,950 t** | [dewiki] | 只有德文维基给这个数；Bismarck 的 construction 是 47,870 mt [kb-genedata]，**方向反了（Tirpitz 应更重）**，存疑 |
| 满载（full load） | **52,600 t** | [navypedia-bb]、[enwiki]（=51,800 lt）、[gn-tirpitz]（写成 "Maximum displacement 52600 t"） | 三家一致 |
| 满载 | **51,700 mt** | [kb-genedata] | 又是 Bismarck 值的翻版（Bismarck full 51,760），与本站另一页冲突 |
| 最大（maximum） | **53,500 mt** | [kb-tirpitz]、[dewiki]（Maximal 53.500 t）、[dma-tirpitz]（「53.500 t max. 1944」） | 三家一致 |
| 最大（1941-02 状态） | **50,425 t** | [dma-tirpitz] | **独有口径**：德国海军档案站把 1941 年 2 月的最大排水量记为 50,425 t，1944 年才是 53,500 t |
| 沉没当日实际排水量 | **42,000 tons（st，≈37,600 mt）** | [kb-report-222-45] | **极易误引**：这是 1944-11-12 当天燃油+淡水只剩约 3,000 t（≈满载 30%）时的实载，**不是标准排水量**。报告附录 A-3 称满载液舱约 10,000 t |

**要点**
- 「Tirpitz 比 Bismarck 重约 1,200 lt / 1,200 t」这一说法在 [dewiki]（1.200 tn.l.）、[navypedia-bb]（41,700→42,900）、[enwiki] 三处独立出现，可视为**收敛结论**；但具体数值本身分歧很大（标准排水量从 42,900 到 43,978 都有人写）。
- **【推断】** dewiki 给出的增重原因（见 §2）是「Bismarck 开工后才改的燃油舱分隔设计被用在了 Tirpitz 上，Tirpitz 载油更多」——这条有实物佐证：燃油量 Bismarck 7,900 mt [kb-genedata] vs Tirpitz 7,780 mt [navypedia-bb] / 8,297 mt [kb-tirpitz]，**方向互相矛盾**，说明「载油更多」这个说法本身也不牢靠。

---

## 2. 尺寸（Dimensions）

| 项目 | Tirpitz | 来源 | Bismarck（对照） |
|---|---|---|---|
| length.oa（全长） | **253.6 m** | [navypedia-bb]、[dewiki]、[dma-tirpitz] | 250.50 m [kb-genedata] |
| length.oa | **251.0 m** | [gn-tirpitz]（"Length (Total) 251,0 m"） | — |
| length.oa | **250.5 m** | [kb-tirpitz] | — |
| length.oa | **251 m** | [enwiki] | — |
| length.oa | **821.5 ft = 250.4 m** | [kb-report-222-45]（1945 美方实测报告） | — |
| length.wl（水线长） | **241.55 m** | [kb-tirpitz] | 241.55 m |
| length.wl | **241.6 m** | [gn-tirpitz]、[dewiki]（KWL 241,6 m） | — |
| length.wl | **241.7 m** | [navypedia-bb]、[dma-tirpitz] | — |
| length.wl（L.B.P.） | **790 ft = 240.8 m** | [kb-report-222-45]【推断：ft→m 换算】 | — |
| beam（宽） | **36.0 m** | 全部来源一致（[kb-tirpitz][gn-tirpitz][navypedia-bb][dewiki][dma-tirpitz]）；[kb-report-222-45] 记 118.0 ft = 36.0 m | **相同** |
| draught.max（最大吃水） | **10.61 m** | [kb-tirpitz]、[dma-tirpitz] | 10.55 m [kb-genedata] |
| draught.max | **10.6 m** | [gn-tirpitz]、[navypedia-bb]、[enwiki]（full load） | — |
| draught.max | **9.9 m** | [dewiki]（Tiefgang max. 9,9 m） | — |
| 建造吃水（Konstruktionstiefgang） | **9.9 m** | [dma-tirpitz] | — |
| 平均吃水 | **8.70 m** | [navypedia-bb] | — |
| 标准吃水 | **9.30 m** | [enwiki] | — |
| 型深 / depth | **15 m** | [kb-tirpitz] | 15.00 m，**相同** |
| 干舷 | **未获取**（Tirpitz 专属值） | — | Bismarck 4.45–5.67 m [kb-genedata] |
| 水线面积 | **未获取** | — | Bismarck 5,740 m² |

**要点**
- **【分歧】全长三说**：253.6 / 251.0 / 250.5。这三组不是「谁抄错」那么简单——[kb-report-222-45] 1945 年美方实测 821.5 ft（250.4 m）意味着战时实测**接近 250.5**，而 253.6 可能包含了某些突出物（如防雷网撑杆/舰艏附件）。**本文不裁决**，但把美方实测值单列，它是唯一有"测量"性质的数据。
- **【分歧】吃水**：[dma-tirpitz]「10.61 max / 9.9 建造吃水」与 [dewiki]「9.9 max」直接矛盾——后者很可能把建造吃水当成了最大吃水。
- ua 与 wl 的关系：如果 wl 取 241.55，oa 取 253.6，则艏艉悬伸合计 12.05 m；若 oa 取 250.5，悬伸 8.95 m。**Bismarck 级的设计悬伸约 9 m**，所以 250.5 一组在几何上更自洽（**【推断】**，非任何来源的原话）。

---

## 3. 动力（Machinery）

### 3.1 主机与功率

| 项目 | Tirpitz | 来源 | Bismarck（对照） |
|---|---|---|---|
| 锅炉 | **12 台 Wagner 高压过热蒸汽水管锅炉** | [kb-tirpitz][gn-tirpitz][navypedia-bb][dewiki][dma-tirpitz] | **相同**（数量与型号都同） |
| 锅炉压力/温度 | **55–56 atm（58 kg/cm²）/ 450 °C** | [kb-propulsioni]（该页标注数据来自 Tirpitz 上的 Brown Boveri 轮机） | 同 |
| 锅炉压力/温度 | **58 atm / 475 °C** | [navypedia-bb] | **【分歧】** 与上一行冲突，navypedia 未说明依据 |
| 锅炉蒸汽参数（德文站） | **55 atü** | [dma-tirpitz] | 第三种写法 |
| 汽轮机 | **3 组 Brown, Boveri & Cie 齿轮传动汽轮机** | [kb-tirpitz][gn-tirpitz][navypedia-bb][dewiki]（BBC-Getriebeturbinen）[dma-tirpitz] | **不同**：Bismarck 是 3 组 Blohm & Voss |
| **巡航汽轮机（Marschturbine）** | **有，1 组**，4,220 rpm / 轴 170 rpm | [kb-propulsioni]、[dewiki] | **Bismarck 没有**——[kb-propulsioni] 原文明确「No cruising turbine was fitted on Bismarck.」；[dewiki] 记「Im Unterschied zur Bismarck erhielt die Tirpitz einen Satz Marschturbinen, die den Brennstoffverbrauch bei Teillast optimierten」 |
| 轴 / 螺旋桨 | **3 轴，3 具三叶桨 ⌀4.70 m** | [kb-propulsioni][dewiki]（dreiflügelig ⌀ 4,7 m） | **相同** |
| 舵 | **2 具，各 24.21 m²，向中线内倾 8°** | [kb-propulsioni] | **相同** |
| 设计功率 | **138,000 hp / 29 kn** | [navypedia-bb] | **相同** |
| 实测最大功率 | **163,026 hp（WPS/shp）** | [kb-tirpitz][gn-tirpitz][dewiki][dma-tirpitz] | 150,170 hp（Bismarck） |
| 实测最大功率 | **163,024 hp** | [kb-genedata] 对比表 | **【分歧】** 与 163,026 差 2 hp，属抄写噪声 |
| 实测最大功率 | **163,023 PS（160,793 shp / 119,903 kW）** | [enwiki] | **【分歧】** 又一说 |
| 实测最大航速 | **30.8 kn** | [kb-tirpitz][gn-tirpitz][navypedia-bb][dewiki][dma-tirpitz] | Bismarck 30.12 kn [kb-genedata] |
| 实测航速（写法不同） | **30–31 knots** | [kb-genedata] 对比表 | 区间写法，无单值 |
| 电功率 | **7,910 kW / 220 V（8×500 kW 柴油 + 5×690 + 1×460 kW 汽轮，4 个电站）** | [kb-propulsioni] | **数值与 Bismarck 相同**，但设备件号不同：柴油机 MWM RS 38 S 编号 170093 → **Tirpitz 170094**；发电机 Garbe-Lahmeyer P23 FA925 10 Spez. B2 编号 377071 → **Tirpitz P23 FA925/10+RP 91 sp.，编号 376848** |

### 3.2 航程与燃油

| 项目 | Tirpitz | 来源 | Bismarck（对照） |
|---|---|---|---|
| 续航 | **8,870 nm @ 19 kn** | [kb-tirpitz][gn-tirpitz][navypedia-bb][dma-tirpitz] | 8,525 nm @19kn [kb-genedata] |
| 续航（完整曲线） | **9,280 @16；8,870 @19；6,693 @24；4,728 @28** | [kb-tirpitz] | 9,280 @16；8,900 @17；8,525 @19；6,640 @24；4,500 @28 |
| 燃油 | **8,297 mt** | [kb-tirpitz] | 7,900 mt [kb-genedata] / 8,294 mt [kb-propulsioni] |
| 燃油 | **7,780 t** | [navypedia-bb] | **【分歧】** 与上一行冲突；navypedia 同时给 Bismarck 7,400 t |
| 续航（德文站） | **8,870 sm @19kn；9,280 sm @16kn** | [dma-tirpitz] | — |

**要点**
- 动力这块的**实质性差异只有一条：巡航汽轮机**。它降低了部分负荷油耗，[dewiki] 认为这也是 Tirpitz 续航数据（8,870 vs 8,525 nm）好于 Bismarck 的原因之一——但这是解释，不是数据。
- 注意 [kb-propulsioni] 页里的轮机性能表**本身就是 Tirpitz 的 Brown Boveri 数据**，而同一页的 Bismarck 总功率 150,170 hp 是 Bismarck 的。混着用会出错。

---

## 4. 编制（Complement）

| 口径 | Tirpitz | 来源 | 备注 |
|---|---|---|---|
| 标准 / 平时 | **2,608 人（108 军官 + 2,500 士兵）** | [kb-tirpitz]、[dma-tirpitz]（「2.608 Mann, davon 108 Offiziere (1943)」）、[gn-tirpitz]、[navypedia-bb] | 四家一致 |
| 标准（拆分数） | **103 军官 + 1,962 士兵** | [enwiki] | **【分歧】** enwiki 把这个当"as built 标准编制"，战时才增到 108 + 2,500。与上面 2,608 的拆法（108 + 2,500）冲突：一个是 2,065 人、一个是 2,608 人 |
| 战时 / 1943 | **2,608 人** | [dma-tirpitz] 明确标 1943 年 | — |
| 1944 年（沉没前） | **约 1,600 人** | [enwiki] | 沉没前减员到约 1,600，用于当浮动炮台；这是**最接近沉没当日**的编制数 |
| 编制（另一说） | **2,500 Mann** | [dewiki] | 只给总数，未拆军官 |
| 编制（对比表） | **2,600** | [kb-genedata] | 概数 |
| 1944-04-03 空袭伤亡 | **122 死（8 军官 + 22 士官 + 90 兵 + 2 船厂人员）、316 伤** | [kb-3444]（舰长呈报原文 B.Nr. Gkdos 395） | 一手德方战报 |

**要点**
- 编制是 Tirpitz 明显高于 Bismarck 的一项（Bismarck 2,092 / Rheinübung 时 2,221）。**最可靠的是 [kb-3444] 这类原始呈文里出现的实数**，但该文件只给伤亡不给编制。
- **[dma-tirpitz]** 的「2.608 Mann, davon 108 Offiziere (1943)」是唯一把 2,608 绑定到具体年份的写法、且与 [kb-tirpitz] 完全吻合，采信度较高。

---

## 5. 武备（Armament）

### 5.1 主炮 38cm（8 门 / 4 座双联）

| 项目 | Tirpitz | 来源 | 与 Bismarck 对比 |
|---|---|---|---|
| 数量 / 布局 | **8 门 38cm SK C/34，4 座双联 Drh LC/34**，Anton/Bruno 前背射、Caesar/Dora 后 | [kb-tirpitz][gn-tirpitz][navypedia-bb][dewiki][dma-tirpitz] | **完全相同**，炮塔名称也一样 |
| 炮塔命名 | **Anton / Bruno / Caesar / Dora** | [enwiki] | 相同 |
| 身管倍径 | **L/52（德制算法）；navypedia 写 380/48** | [dewiki]（L/52）[navypedia-bb]（380/48） | 相同，属算法口径差异（德制按膛线长/英制按整管） |
| 座重 | **1,052,000 kg** | [nw-38] | 相同 |
| 俯仰 / 旋回 | **-5.5°/+30°，6°/s；旋回 ±145°，5°/s** | [nw-38] | 相同 |
| 弹药基数 | **960 发（120 发/炮）** | [dewiki] | 相同 |
| 弹药基数 | **108 发/炮（设计值）**，德国舰实际 112–120，「German Capital Ships of WWII」记 130 | [nw-38] | **【分歧】** 108 / 120 / 125 / 130 四说并存 |
| 是否有改进 | **有：1944 年起配发改装引信的对空弹** | [nw-38] | **Tirpitz 独有** |
| 炮塔差异 | 无 | — | — |

**Tirpitz 独有：38cm 对空弹（barrage AA）**
- 1944-04-03 被英舰载机击伤后，补给了一批**改装引信（Z.Z. S/60 nA 时间引信）的 38cm 榴弹**：去掉风帽、换时间引信，最大对空射程 20,100 m [nw-38]。
- 1944 年 8–10 月的空袭中使用过；11-12 在 11,200 m 对 Lancaster 开火，打散了编队但未击落 [nw-38]。
- [enwiki] 从另一侧印证：「specially fuzed 38 cm shells for barrage anti-aircraft fire were supplied」。
- 效果评价：[enwiki] 明确写「Tirpitz's 38 cm fragmentation shells proved ineffective in countering the high-level bombers」。

### 5.2 副炮 15cm（12 门 / 6 座双联）

| 项目 | Tirpitz | 来源 | 对比 |
|---|---|---|---|
| 数量 / 型号 | **12 门 15cm SK C/28（L/55），6 座双联** | [kb-tirpitz][gn-tirpitz][navypedia-bb][dewiki][dma-tirpitz] | **完全相同** |
| 弹药基数 | **1,800 发** | [dewiki] | 相同 |
| 对空改装 | **1944 年修复期间，15cm 炮被改装为可对空射击** | [enwiki] | **Tirpitz 独有**（Bismarck 没有这个改装机会） |

### 5.3 重型高炮 10.5cm（16 门 / 8 座）— **这段是重点**

| 项目 | 值 | 来源 |
|---|---|---|
| 数量 | **16 门 10.5cm SK C/33（L/65），8 座双联** | [kb-tirpitz][gn-tirpitz][navypedia-bb][dewiki][dma-tirpitz] 全部一致 |
| 炮座型号（Tirpitz 初始） | **前 6 座 Dop. L. C/37 + 后 2 座 Dop. L. C/31d** | [navypedia-bb]（「Tirpitz had all 105mm guns in LC/37 mounts」，但同页改装表与 navweaps 表给出更细的分法） |
| 炮座型号（Bismarck 对照） | **前 4 座 Dop. L. C/31d + 后 4 座 Dop. L. C/37** | [nw-105] |
| **1941 年底以后** | **全部 8 座统一为 Dop. L. C/37** | [nw-105] 脚注原文：「Tirpitz was originally fitted with two Dop. L. C/31d mounts but these were replaced in late 1941 giving her a uniform battery of eight Dop. L. C/37 mounts.」 |

**C/31d 与 C/37 的量化差别（[nw-105]）**

| 项目 | C/31 / C/31gE | C/31d | C/37 |
|---|---|---|---|
| 座重 | 27,805 kg | 27,350 kg | **26,425 kg** |
| 俯仰范围 | -8°/+80° | -8°/+80° | **-10°/+80°** |
| 俯仰速率 | 10°/s | 10°/s | **12°/s** |
| 旋回速率 | 8.0°/s | 8.0°/s | **8.5°/s** |
| 横倾补偿速率 | 5°/s | 5°/s | **8°/s** |
| 后座行程 | 41 cm | 41 cm | **38 cm** |

- **要点**：[nw-105] 还专门说了为什么统一炮座重要——「this mixing of mounting types may not have accounted for in her AA fire control systems, so changing to a uniform battery would have improved her AA defense capabilities.」即混装会让火控解算对不上，统一后防空效率提高。
- 炮本身（10.5cm SK C/33）两舰相同：射速 15–18 发/分、弹重 AP 15.8 kg / HE L/4,4 15.1 kg、45° 射程 17,700 m、80° 升限 12,500 m [nw-105]。
- 两舰都在 C、D 炮塔之间装一门**练习炮**（完整炮闩 + 短身管）[nw-105]。
- **[enwiki]** 补充：1942 年 1 月挪威部署前的改装中，「the 10.5 cm guns on the superstructure next to the catapult were moved outboard to increase their field of fire」——弹射器旁边的 10.5cm 座被外移以扩大射界。

### 5.4 轻型高炮 3.7cm（16 门 / 8 座）

| 项目 | Tirpitz | 来源 | 对比 |
|---|---|---|---|
| 数量 / 型号 | **16 门 3.7cm SK C/30（L/83），8 座双联 Dopp. L. C/30** | [kb-tirpitz][gn-tirpitz][navypedia-bb][dewiki][dma-tirpitz] | **与 Bismarck 完全相同，且全程未变** |
| 弹药基数 | **32,000 发** | [dewiki] | — |
| 射速 | **约 30 发/分** | [nw-37]（navweaps 明确否掉常见的「80 理论/40 实用」说） | 相同 |

> 注意：[navypedia-bb] 的 Tirpitz 改装时间线里 **1941–1944 年没有任何一条涉及 3.7cm**，说明这 8 座是从服役到沉没都没动过的。这是与 2cm 形成鲜明对比的一点。

### 5.5 轻型高炮 2cm（**数量变化最大**）

**各家给的终值（全部并列，不裁决）：**

| 终值 | 来源 | 写法 |
|---|---|---|
| **78 门（1944）** | [kb-tirpitz] | 「20 x 2cm guns (78 in 1944)」 |
| **最多 78 门** | [dma-tirpitz] | 「bis zu 78 x 2,0 cm-Flak」；[kb-genedata] 对比表也记 78 |
| **58 门** | [enwiki] | 「The number of 2 cm guns was eventually increased to 58」 |
| **16–58 门** | [gn-tirpitz]、[dewiki]（12–58） | 区间写法，德文维基下限记 12 |

**改装时间线（[navypedia-bb] 逐条原文，唯一给出完整过程的来源）：**

| 时间 | 变化 | 累计（本文按原文推算【推断】） |
|---|---|---|
| 服役时（1941-02） | 12 × 1 20/65 C/38 | 12 门（单装） |
| 1941-07 | **+4 × 1** 20/65 C/38 | 16 门（单装） |
| 1941-09 | **-4 × 1**；**+6 × 4** 20/65 C/38（六座四联） | 6×4 = 24 门 |
| 1942-06 | **+2 × 4** 20/65 C/38 | 8×4 = 32 门 |
| 1943-03 | **+2 × 4** 20/65 C/38 | 10×4 = 40 门 |
| 1944-06 | **-6 × 1**（清掉剩余单装）；**+8 × 4** 20/65 C/38 | 18×4 = **72 门** |

- **【推断】** 上表累计列是我按 navypedia 的「+/-」逐条加减算的，navypedia 原文**没有给累计值**。若「-6 × 1」实际清掉的是全部剩余单装，则 1941-09 之后单装应已清零，此处 1944-06 的「-6 × 1」在时间线上对不上，**navypedia 自身存在内部矛盾**。
- 三种独立来源的终值 72（推算）/ 78 / 58 互不相等，说明**没有一家把最后一年的账算准**。
- [kb-tirpitz] 提供了独立的装置形态证据，可交叉验证「四联为主」这一趋势：
  - 1941-10（Gotenhafen）：「the antiaircraft battery is increased」
  - 1944-04-03 空袭弹药消耗：**8,260 发 2cm** [kb-3444]（对照 10.5cm 506 发、3.7cm 400 发）——2cm 是唯一打了上万发的口径
- **[kb-3444]（1944-04-03 德方原始战报）里的装置细节**，能看出 1944 年的实际布局：
  - 「Brücken-Vierling」= 舰桥四联（照片说明里出现）
  - 「Schornstein-Vierling」= 烟囱四联，被命中后「kippt vom Pivot」（从基座翻倒）
  - 舰桥/上层建筑前部（"forward part of her main superstructure"）与 **Bruno 炮塔顶部**各有一组四联 [ww2color-blog]（1942 年 6 月照片说明）+ [dewiki]（「eine markante, auf dem Schwesterschiff ebenfalls nicht vorhandene 2-cm-Flak-Vierling 38 auf dem überhöhten 38 cm-Turm „Bruno"」——**Bismarck 上没有这台 Bruno 顶四联**）
- **[dewiki]** 的「12–58 × 2 cm Flak C/38（L/65），90,000 发」把型号统一写成 C/38，与 [navypedia-bb] 的「20/65 C/38」一致；Bismarck 早期用的是 C/30。

### 5.6 鱼雷管 — **Tirpitz 独有武装**

| 项目 | 值 | 来源 |
|---|---|---|
| 数量 / 布局 | **8 具 533mm（53.3cm）鱼雷发射管，2 座四联装，甲板安装** | [kb-tirpitz][gn-tirpitz][navypedia-bb][dewiki][dma-tirpitz] 全部一致 |
| 位置 | **上甲板舯部（section X）两舷各一座** | [kb-tirpitz] 原文「on the upper deck to each side of the ship amidships (section X)」 |
| 位置（另一描述） | **两座后部 15cm 炮塔之间加高上层建筑的后方** | [dewiki] 原文「Hinter diesem Vorsprung wurden im Herbst 1941 noch zusätzlich Torpedo-Vierlingssätze installiert」 |
| 鱼雷型号 | **G7a T1（53.3cm，湿式热机）**【推断：navweaps 的 G7a 页面配了「Battleship Tirpitz firing a torpedo」照片，且 G7a 是德水面舰标准 53.3cm 鱼雷】 | [nw-torp] |
| 鱼雷参数 | 重 1,528 kg，长 7.186 m，装药 280 kg Hexanite；6,000 m/44kn、8,000 m/40kn、14,000 m/30kn | [nw-torp] |
| 备雷数 | **24 发** | [dewiki]（「zwei Vierersätze, 24 Schuss」） |
| 加装时间 | **1941 年 9 月** | [navypedia-bb]（「9/1941: ... 2 x 4 - 533 TT」） |
| 加装时间 | **1941 年 10 月（Gotenhafen）** | [kb-tirpitz] 原文「October 1941: While in Gotenhafen, the antiaircraft battery is increased. In addition two quadruple torpedo mounts are installed...」 |
| 加装时间 | **1941 年秋** | [dewiki]（「im Herbst 1941」）——与上面两条相容 |
| 加装时间 | **1941-12 ~ 1942-01 的挪威部署改装期间** | [enwiki] 原文「The two quadruple 53.3 cm torpedo tube mounts were also installed during this refit」 |
| 发射管型号 | **未获取**（德方型号如「Vierlingssatz / TR-Vierling」为驱逐舰用；战舰用甲板四联的正式型号未在任何已查来源出现） | 见 §11 |

**要点**
- **【分歧】加装时间三说**：1941-09 [navypedia-bb] / 1941-10 [kb-tirpitz] / 1941-12～1942-01 [enwiki]。kbismarck 论坛相关讨论（403，未取得）标题本身就是「Background of Tirpitz's additional torpedo armament」，说明这争了几十年。
- **德文维基还给了原因**：这两座四联之所以能装在「后部两座 15cm 炮塔之间」的位置，是因为 Tirpitz 把那里的一段上层建筑**延伸到了上甲板边缘**（Bismarck 没有），主吊车因此不得不装在更高的一层甲板上 [dewiki]。这是 Tirpitz 与 Bismarck **肉眼可见的结构差异**之一。

### 5.7 其他武装

| 项目 | Tirpitz | 来源 |
|---|---|---|
| 深水炸弹 | **未获取**（Bismarck 记 9 枚 [kb-genedata]） | — |
| 练习炮 | **1 门，位于 C、D 炮塔之间** | [nw-105]（与 Bismarck 相同） |

---

## 6. 航空（Aviation）

| 项目 | 值 | 来源 |
|---|---|---|
| Ar 196 搭载数 | **4 架** | [kb-tirpitz][gn-tirpitz][navypedia-bb][dewiki][dma-tirpitz][enwiki] 全部一致 |
| **最大搭载能力** | **6 架**（4 架在 3 个机库，2 架停在弹射器上） | [luft-196]（一手德文技术说明） |
| 机库 | **3 个**：Halle 1（上甲板中部 Spant 94–106，2 架）、Halle 2（左舷烟囱旁 Spant 122–134，1 架）、Halle 3（右舷同位，1 架） | [luft-196] |
| 修理间 | Deckhausdecke 内侧，Spant 82–87.5 | [luft-196] |
| 弹射器类型 | **Doppel-Teleskop-Katapult（双联伸缩式），Deutsche Werke 制造，左右舷各一，位于舯部** | [luft-196] |
| 弹射器尺寸 | **每具 16 m，可伸出舷外至 24 m** | [luft-196] |
| 弹射器尺寸 | **32 m，伸出至 48 m** | [dewiki] — **【分歧】** 与上一行相差整整一倍 |
| 弹射器数量表述 | **1 座 double-ended catapult（双端弹射器）** | [enwiki]（与「左右各一」的说法不同，可能是指同一套背靠背装置） |
| 起重设备 | 2 台固定 12 t 旋转吊（Spant 121 左右），2 台 4 t 移机吊（烟囱处 Spant 114.950），1 个转盘 | [luft-196] |
| 航空燃油 | 2 套系统共 4 个油罐、4 个加注点；3 个 70 L 滑油罐；2 台 Junkers 空压机供弹射器 | [luft-196] |
| 航空部队 | **Bordfliegerkommando 1./196**（陆基海军航空兵编入） | [luft-196]、[dewiki] |
| **弹射器何时拆除** | **未获取** | 见 §11 |

**航空活动时间线（[luft-196] 一手记录）**

| 日期 | 事件 |
|---|---|
| 1941-09-03 | E-Stelle Travemünde 验收弹射装置（首两架 B BY F / B BY L，Ar 196 A3） |
| 1941-09-17 ~ 10-30 | 波罗的海试飞（Unternehmen Aalandsee「BALTENFLOTTE」） |
| 1941-10-31 | **因舰只进坞，Bordfliegerabschnitt 解散**，飞机全部飞回 Wilhelmshaven |
| 1941-11-30 ~ 1942-04-21 | 再度上舰，含挪威航渡（T 3 L H / C K / F K / B L / B H / D L / E L / H H 轮换，部分从 Prinz Eugen 转来） |
| 1942-04-21 | **全部飞机与人员转移至 Drontheim 水上机场**，此后 Tirpitz 只当起降平台 |
| 1942-07-02 ~ 10-24 | Rösselsprung 行动期间；T 3 G H「Katapult unklar」（弹射器故障），T 3 B H 移交 Admiral Scheer |
| 1943-02-04 ~ 11-26 | Sizilien 等行动；**1943-09-22 X 艇爆炸**中 T 3 G H、T 3 F H 两机「flugunklar」（不可飞），09-25 移交 BERNHARD v. TSCHIRSCHKY |
| 1943-11-26 之后 | **[luft-196] 的记录到此为止**，1944 年无飞机上舰记录 |

- 【推断】结合 [luft-196] 记录止于 1943-11-26、以及 1944 年 4 月空袭中「Tirpitz's two Arado Ar 196 floatplanes were completely destroyed」[enwiki]，可推知 1944 年舰上仍有 2 架（非 4 架）。但**弹射器是否、何时拆除，所有已查来源均无记载**。

---

## 7. 装甲（Armour）

**结论：与 Bismarck 基本相同。** 这是本文中唯一可以明确写「相同」的大项，且多来源支持。

| 项目 | Tirpitz | 来源 | 对比 |
|---|---|---|---|
| 舷侧装甲带（main belt） | **320 mm（最大）** | [kb-tirpitz][gn-tirpitz][dewiki]（Gürtel 170–320） | 相同（Bismarck 320） |
| 舷侧装甲带 | **300 mm** | [dma-tirpitz] | **【分歧】** 德文站写 300 而非 320 |
| 舷侧装甲带（下缘） | **320–270 mm** | [navypedia-bb] | 与 Bismarck 同 |
| 上装（upper belt / Zitadelle） | **145 mm**（Zitadelle 120–145） | [kb-tirpitz]（upper deck 表述不同）[navypedia-bb][dewiki][dma-tirpitz] | 相同（Bismarck 145） |
| 上甲板（upper deck） | **50–80 mm** | [kb-tirpitz][dewiki]（Oberdeck 50–80） | 相同 |
| 装甲甲板（armour deck / Panzerdeck） | **80–120 mm** | [kb-tirpitz][gn-tirpitz][dewiki][dma-tirpitz]（80 mm，弹药库/舵机处 100 mm） | 相同（Bismarck 80–120） |
| 装甲甲板（斜面） | **100 mm** | [navypedia-bb] | 与 Bismarck 同 |
| 横向装甲隔壁 | **45–220 mm** | [dewiki] | 相同 |
| 防雷舱壁 | **45 mm** | [kb-tirpitz][dewiki][navypedia-bb] | 相同 |
| 主炮塔 | **360 mm（正面）/ 130–360** | [kb-tirpitz][gn-tirpitz][navypedia-bb][dewiki][dma-tirpitz] | 相同 |
| 主炮座（barbette） | **220–340 mm**（正面 340） | [dewiki][dma-tirpitz][navypedia-bb] | 相同 |
| 副炮塔 | **100 mm（正面）/ 20–100** | [dewiki][dma-tirpitz][navypedia-bb] | 相同 |
| 前司令塔 | **350 mm（200–350）** | [kb-tirpitz][dewiki][dma-tirpitz][navypedia-bb]（CT 355–50） | 相同 |
| 后司令塔 | **150 mm** | [dewiki] | — |
| 火炮指挥所（Vormars） | **20–60 mm** | [dewiki] | — |
| 装甲总重 | **19,082 mt** | [kb-genedata]（对比表 Tirpitz 栏） | 与 Bismarck 同数 |
| 装甲总重 | **18,700 t（占排水量 44%）** | [navypedia-bb] | **【分歧】** 与 19,082 冲突 |
| 防雷系统设计指标 | **可承受约 660 lb（300 kg）德国 hexanite** | [kb-report-222-45] | 一手印证；[kb-report-222-45] 同时给出德方对 Bismarck 的 250 kg TNT 说法 |
| 防护长度 | **未获取**（Tirpitz 专属） | — | Bismarck 70%（170.7 m）/ 22 段中 17 段在装甲盒内 |
| 水密段数 | **未获取**（Tirpitz 专属） | — | Bismarck 22 段 |

**要点**
- 除了 [dma-tirpitz] 的「300 mm 舷侧」和 navypedia 的装甲总重（18,700 vs 19,082）之外，**没有任何来源指出 Tirpitz 装甲与 Bismarck 有实质差别**。
- [dewiki] 的 170–320 与 navypedia 的 320–270 是「带的上下缘」不同写法，不是矛盾。

---

## 8. 建造信息（Construction）

| 项目 | 值 | 来源 |
|---|---|---|
| 铺设龙骨 | **1936-11-02** | [kb-tirpitz]（"laid down at the Kriegsmarine Werft, Wilhelmshaven, Slipway 2"）、[gn-tirpitz]（02.11.1936）、[dewiki]（2. November 1936） |
| 铺设龙骨 | **1936-11-01** | [kb-km-bb] — **【分歧】** 同站另一页，差一天 |
| 铺设龙骨 | **1936-10-20** | [navypedia-bb] — **【分歧】** 差 13 天 |
| 铺设龙骨 | **1936-10-24** | [dma-tirpitz]（24.10.36） — **【分歧】** 第四说 |
| 下水 | **1939-04-01** | [kb-tirpitz][gn-tirpitz][navypedia-bb][dewiki][dma-tirpitz] 全部一致 |
| 掷瓶人 | **Frau Ilse von Hassell**（Tirpitz 元帅之女） | [kb-tirpitz][dewiki] |
| 服役 | **1941-02-25** | 全部来源一致 |
| 建造厂 | **Kriegsmarinewerft Wilhelmshaven**（海军船厂，不是私人厂） | [kb-tirpitz][gn-tirpitz][navypedia-bb][dewiki][dma-tirpitz] 一致 |
| 船台 | **Slipway 2（2 号船台）** | [kb-tirpitz][gn-tirpitz] |
| 船台号 / 建造编号 | **S 128 / Yard No 128 / Baunummer 128** | [kb-tirpitz]（"construction number S 128"）、[navypedia-bb]（Yard No 128）、[dewiki]（Baunummer 128） |
| 造价 | **1.81 亿帝国马克（181 Mio RM）** | [gn-tirpitz]（"Cost 181 Mio Reichsmark"） |
| 造价 | **1.816 亿帝国马克（181,6 Mio ℛℳ）** | [dewiki] — **【分歧】** 差 60 万，dewiki 更精确 |
| 下单日期 | **1936-06-14** | [kb-tirpitz] |
| **服役时舰长** | **Karl Topp（Kpt.z.S.），1941-02-25 ~ 1943-02-24** | [kb-tirpitz][dma-tirpitz]（25.02.41–24.02.43） |
| 舰长（后续） | **Hans Meyer** 1943-02-25 ~ 1944-04-30 | [kb-tirpitz][dma-tirpitz]（25.02.43–30.04.44） |
| 舰长 | **Wolf Junge** 1944-05-01 ~ 1944-11-03（带 DKG 字样） | [kb-tirpitz][dma-tirpitz]（01.05.44–04.11.44） |
| 舰长 | **Robert Weber**（i.V.，代理）1944-11-04 ~ 11-12（阵亡） | [kb-tirpitz][dma-tirpitz] |
| 沉没 | **1944-11-12，挪威 Altafjord / Håkøya 附近**（69°38'49"N 18°48'27"E） | [kb-tirpitz][gn-tirpitz][dewiki][dma-tirpitz] |
| 拆解 | **1948–1957，挪威公司就地拆解**（1947 年 Einar Høvding 购得） | [kb-tirpitz][dewiki] |

**要点**
- 龙骨日期四说（10-20 / 10-24 / 11-01 / 11-02）是本文最烂的一块数据。11-02 有三家支持（含德文维基与 kbismarck 主页面），**但我不裁决**。
- 「Tirpitz 是欧洲建成的最大的战列舰」这一说法 [dewiki] 明确写过，依据就是她比 Bismarck 重 1,200 tn.l.。

---

## 9. 雷达与火控（Radar & Fire Control）

### 9.1 雷达演进

| 时期 | 装备 | 来源 |
|---|---|---|
| **1941 年（服役时）** | **3 × FuMO 23** | [kb-tirpitz]、[kb-genedata]（Bismarck 同） |
| **1942 年** | **3 × FuMO 23 + 1 × FuMO 27 + FuMO 4 "Samos"** | [kb-tirpitz] |
| **1942-01（更精确）** | 前桅测距仪塔顶加雷达室，装 **FuMO 27** 天线；其上方小框装 **Timor** 天线（FuMO 4 Samos）；雷达室两侧与后方装 **Sumatra** 天线 | [nw-radar] |
| **1943 年（编号体系变更）** | FMG 39G (gO)/(gP) → **FuMO 23**；FMG 39G (gL) → **FuMO 21** | [nw-radar] |
| **1944 年** | **3 × FuMO 26 + FuMO "Hohentwiel" + FuMO 213 "Würzburg-D"** | [kb-tirpitz] |
| **1944 春夏（更精确）** | 换装加大型 **3 m × 6 m** 天线，判为 **FuMO 26**；前桅小框可能是试验性 **FuMO 30**，或 Palau 偶极子的标准框（配 **FuMB 6**）——「this would be the only appearance of a FuMO 30 on a German surface unit」 | [nw-radar] |
| **1944 春夏（火控）** | 第三座防空指挥仪（主桅后，昵称 'Wackeltopf'）**升高 2 m**，加装炮瞄雷达，判为 **Würzburg-C 或 Würzburg-D**（海军编号分别 FuMO 212 / 213） | [nw-radar] |
| **另一说（静态清单）** | **4 × FuMO 27** | [navypedia-bb] — **【分歧】** 与上表的时间演进描述冲突，navypedia 未给时间点 |
| **另一说（kbismarck 对比表）** | 1944 年列与 Bismarck 同（未列 Tirpitz 专属值） | [kb-genedata] |
| **ECM（电子对抗）** | 1941-09：**FuMB 4 + FuMB 7**；1944-06：**FuMB 6** | [navypedia-bb] |

- [nw-radar] 的总评：「**Tirpitz had the most sophisticated radar equipment of all the larger German surface units.**」
- **[nw-radar] 关于 Bismarck 级共性的一条**：两舰都因雷达塔增重导致测距仪塔轴承临界超载，改装了加大型测距仪塔（容纳 FuMO 23 与光学设备）。Bismarck 舰桥正面是否装第 4 面天线在德国文献中有争议——**Tirpitz 侧无此争议**。

### 9.2 火控

| 项目 | Tirpitz | 来源 | 对比 |
|---|---|---|---|
| 主/副炮指挥仪 | **3 座（含机械计算机）** | [enwiki] | 相同 |
| 测距仪 | **5 × 10.5 m、1 × 7 m、2 × 6.5 m、4 × 4 m（Type SL-8）、2 × 3 m** | [kb-tirpitz] | 与 Bismarck 规格相同 |
| 10.5cm 的 SL-8 指挥仪 | **4 座稳定式** | [enwiki] | 相同 |
| 后部测距仪护罩 | **有（Abdeckhauben），Bismarck 没有** | [dewiki] | **Tirpitz 独有** |
| 防空指挥仪 | **第三座于 1944 春夏升高 2 m 并加雷达** | [nw-radar] | **Tirpitz 独有** |
| Anton 炮塔测距仪 | **1940/41 冬因进水损坏后拆除** | [nw-38] | 属 Bismarck 级共性描述，Tirpitz 适用性**未单独确证** |

---

## 10. 涂装（Camouflage）

**这一块是全篇证据最弱的部分。** 没有任何一手德国海军涂装命令被已查来源引用；下述内容来自照片说明、模型参考书目录与论坛二手讨论，全部标注来源性质。

| 时期 | 涂装 | 来源 | 证据强度 |
|---|---|---|---|
| **1941 年波罗的海试航（约 5 月）** | **"Baltic" 迷彩**：舰体与上层建筑上三道黑白条纹（用于航空识别），艏艉另有浅色块 | [nw-camo]（图注「Figure 3. KMS Bismarck in "Baltic" Camouflage, May 1941」——同一页 Figure 4 为 Tirpitz 的 dazzle）、[dewiki]（未提） | 弱：无来源明确说 Tirpitz 在 1941 年也用了 Baltic 条纹；但 [nw-camo] 的 Figure 4 图注为「KMS Tirpitz in a "Dazzle" Disruptive Measure」，**说明她确实用过眩目迷彩** |
| **1942 年（Fættenfjord，特隆赫姆）** | **浅/深灰分裂式（splinter-pattern）破坏迷彩**：「light / dark grey splinter-pattern disruptive camouflage」，舰体与上层建筑呈碎块状 | [ww2color-blog]（1942-06 照片说明） | 中：照片说明，非档案 |
| **1942/43 年** | 有专门的**迷彩标识（camouflage markings）**套装，Snyder & Short 色卡第二张专门收录「camouflage markings for the Tirpitz in 1942/43」 | [modelwarships-bookreview] | 中：说明确有阶段性方案，但未给图案 |
| **1943 年（Kåfjord）** | 「ikledd kamuflasje dekor」（身着迷彩装饰），可见全舰 | [digitaltmuseum-1943]（挪威博物馆藏 1943 年照片记录） | 中：档案照片，但无图案细节 |
| **1943-07 ~ 1944-03（"Scheme J"）** | 德文模型圈称这一段为 **"Paint Scheme J"**；有人据彩照推测配色为 **白 = RAL 9002 / 浅灰 = RAL 7001 / 深灰 = RAL 7024**（建模者自述，非档案） | [forum-marinearchiv]（原帖明确在问「有没有官方 Farbangaben，还是都只是模型圈估计」） | **弱：论坛二手，作者本人声明是估计** |
| **1944 年末（Håkøya / Tromsø）** | **未获取**（据照片通常描述为整体浅灰、图案大幅简化，但已查来源无一条给出确切方案） | — | — |
| 迷彩的欺骗性原理 | 艏艉涂浅色以误导观察者判断舰长与目标角（target angle） | [nw-camo]（原文「He has both the stern and bow a painted in a lighter shade so as to deceive the observer as to ship length and target angle」） | 中：理论描述 |
| 甲板色 | 柚木甲板；作者持有 Tirpitz 甲板样本，记「Burmese teak」色调 | [camobook-v2]（Leon & Asmussen, *German Naval Camouflage Vol. II* 前言） | 中：专业作者的一手样本 |

**关于权威来源的状况**
- 该领域最权威的专著是 **John Asmussen & Eric Leon, *German Naval Camouflage Volume II: 1942–1945***（2014，ISBN 9781526709844），其中 **Tirpitz 独占第 18–35 页**（Battleships 章首篇）[camobook-v2 目录页]。
- 我只拿到了该书的**预览 PDF（17 页）**，其中只含前言、目录、来源与方法论，**不含 Tirpitz 的 18–35 页图版**。全书为付费出版物，未获取正文。
- kbismarck.com **没有涂装专栏**（详见 §11 的 404 记录），navweaps 只有理论文章。

---

## 11. 未获取项与失败记录

### 11.1 未获取的关键数据

| 项目 | 状态 | 已试过的路径 |
|---|---|---|
| Tirpitz 空载排水量（empty） | 未获取 | 所有来源只给 Bismarck 的 40,250 mt；无 Tirpitz 单列值 |
| Tirpitz 建造排水量 | 仅 dewiki 一家（45,950 t），且方向可疑 | 其余来源未给 |
| 干舷、水线面积、水密段数、防护长度 | 未获取 | 均为 Bismarck 值，无 Tirpitz 单列 |
| 533mm 鱼雷**发射管型号** | 未获取 | navweaps 鱼雷页（`WTGER_WWII.php`）只讲鱼雷（G7a）不讲发射管型号；德方型号「Vierlingssatz」是驱逐舰用语 |
| **弹射器拆除时间** | 未获取 | [luft-196] 记录止于 1943-11-26；[kb-tirpitz]/[dewiki]/[enwiki] 均无记载 |
| 1944 年末涂装方案 | 未获取 | 见 §10 |
| 1944-04-03 之后的 2cm 精确最终数量 | 未获取（72 推算 / 78 / 58 三说） | 无一手清点文件 |

### 11.2 抓取失败 / 无效的记录（便于后续复查）

| URL | 返回 | 说明 |
|---|---|---|
| `https://www.navypedia.org/ships/germany/ger_bb_tirpitz.htm` | **404** | Tirpitz 数据与 Bismarck 同页 |
| `https://www.navypedia.org/ships/germany/ger_bb_tirpitz_2.htm` | **404** | 同上 |
| `https://www.navweaps.com/Weapons/Torp_index.php` 等 7 个鱼雷索引猜测 | **404 ×7** | 正确入口是 `Weapons/index_weapons.php` → `WTGER_Main.php` → `WTGER_WWII.php` |
| `https://www.kbismarck.com/camouflage.html`、`camo.html`、`paint.html`、`tirpitz-camouflage.html`、`camouflagei.html`、`tirpitz-1944.html`、`tirpitz-technical.html`、`tirpitzf.html`、`tirpitz-specs.html` | **404 ×9** | kbismarck 站无涂装页、无独立技术页 |
| `https://www.kbismarck.com/sitemap.xml` | **404** | 无站点地图，只能靠首页链接爬 |
| `https://web.archive.org/web/20131203013625/http://www.bismarck-class.dk/technicallayout/generaldetails.html` | **000**（直连与代理均失败） | 该站的 Bismarck/Tirpitz 并列对照表未取得。**注**：bismarck-class.dk 域名现已被抢注为无关博客，原始内容只能走 archive.org，而 archive 该快照不可达 |
| `https://kbismarck.org/forum/viewtopic.php?start=15&t=9640`（Tirpitz 鱼雷武装加装时间讨论） | **403** | Cloudflare 拦截 |
| `https://ww2db.com/ship_spec.php?ship_id=95` | **403**（直连）/ **403**（代理） | 被拦 |
| `https://www.german-navy.de/kriegsmarine/weapons/index.html`、`weapons/`、`weapons/torpedos/` | **404 ×4** | 该站无武器分区 |
| `https://ipmsuk.proboards.com/thread/5187/tirpitz-paint-scheme-july-november` | **202**（内容为空） | 反爬跳转 |

环境验证：代理 `http://127.0.0.1:7897` 可用，`https://www.navweaps.com/` 返回 **200**；`de.wikipedia.org` 与 `en.wikipedia.org` 走代理 **200**，直连 **000**。

---

## 12. 来源缩写对照表

| 缩写 | 完整 URL | 性质 |
|---|---|---|
| kb-tirpitz | https://www.kbismarck.com/tirpitz.html | 专题站，二手汇编（含德方档案摘录） |
| kb-genedata | https://www.kbismarck.com/genedata.html | 专题站，Bismarck 级通用数据表 |
| kb-bsweights | https://www.kbismarck.com/bsweights.html | 专题站，分项重量表 |
| kb-propulsioni | https://www.kbismarck.com/propulsioni.html | 专题站，动力装置详表（含 Tirpitz/Brown Boveri 数据） |
| kb-armament | https://www.kbismarck.com/armament.html | 专题站，武备页（纯 Bismarck，无 Tirpitz 内容） |
| kb-km-bb | https://www.kbismarck.com/kriegsmarine-battleships.html | 专题站，全战列舰一览表 |
| kb-report-222-45 | https://www.kbismarck.com/tirpitz-technical-report.html | **一手**：US Naval Technical Mission in Europe, Technical Report No. 222-45, 1945-08-29 |
| kb-3444 | https://www.kbismarck.com/tirpitz-luftangriff-3444.html | **一手**：Kommando Schlachtschiff "Tirpitz" B.Nr. Gkdos 395, 1944-04-13 战报 |
| kb-xcraft | https://www.kbismarck.com/tirpitz-midget-submarines.html | 一手/二手混合：1943-09-22 X 艇袭击 |
| gn-tirpitz | https://www.german-navy.de/kriegsmarine/ships/battleships/tirpitz/index.html | 德文海军站（英/德双语） |
| navypedia-bb | https://www.navypedia.org/ships/germany/ger_bb_bismarck.htm | 俄系舰艇数据库，Bismarck/Tirpitz 并列 |
| dma-tirpitz | http://www.deutsches-marinearchiv.de/Archiv/1935-1945/Schiffe/schlachtschiffe/tirpitz.htm | 德国海军档案馆（德文） |
| nw-38 | https://www.navweaps.com/Weapons/WNGER_15-52_skc34.php | **权威技术站**：38cm SK C/34 |
| nw-105 | https://www.navweaps.com/Weapons/WNGER_41-65_skc33.php | **权威技术站**：10.5cm SK C/33（含 C/31 vs C/37 炮座对照表） |
| nw-37 | https://www.navweaps.com/Weapons/WNGER_37mm-83_skc30.php | **权威技术站**：3.7cm SK C/30 |
| nw-20 | https://www.navweaps.com/Weapons/WNGER_20mm-65_c30.php | **权威技术站**：2cm C/30 与 C/38 |
| nw-torp | https://www.navweaps.com/Weapons/WTGER_WWII.php | **权威技术站**：德国二战鱼雷（G7a/G7e） |
| nw-radar | https://www.navweaps.com/Weapons/WNGER_Radar.php | **权威技术站**：德国海军雷达与电子设备 |
| nw-camo | https://www.navweaps.com/index_tech/tech-110.php | 理论文章《Naval Camouflage》（无时期方案） |
| luft-196 | http://www.luftwaffe-zur-see.de/Seeluft/196%20Bordfliegergruppe/Bkdo_Tirpitz.htm | **一手级**：Bordfliegerkommando 1./196 在 Tirpitz 上的完整记录 |
| enwiki | https://en.wikipedia.org/wiki/German_battleship_Tirpitz | 维基（仅作线索交叉，不作最终依据） |
| dewiki | https://de.wikipedia.org/wiki/Tirpitz_(Schiff,_1941) | 德文维基（仅作线索交叉，不作最终依据） |
| camobook-v2 | https://api.pageplace.de/preview/DT0400.9781526709851_A29612660/preview-9781526709851_A29612660.pdf | Leon & Asmussen《German Naval Camouflage Vol. II》预览（17 页，**不含** Tirpitz 图版 pp.18–35） |
| modelwarships-bookreview | https://www.modelwarships.com/reviews/books-plans/snyder-short/dkm-1/dkm-1.html | 色卡评测（含「Tirpitz 1942/43 camouflage markings」一句） |
| ww2color-blog | http://ww2colorfarbe.blogspot.com/2015/09/the-tirpitz-in-fttenfjord-near-trondheim.html | 上色照片博客（1942-06 Fættenfjord 迷彩描述） |
| digitaltmuseum-1943 | https://digitaltmuseum.no/0210114591934/tirpitz-i-kafjord | 挪威博物馆藏 1943 年 Kåfjord 照片档案 |
| forum-marinearchiv | https://forum-marinearchiv.de/smf/index.php?topic=21556.0 | 德文论坛（"Paint Scheme J" 配色讨论，二手估计） |
| smt-torp | http://www.ship-model-today.de/sd026.htm | 模型站，533mm 四联发射管结构复原（驱逐舰用，非战舰） |

---

## 13. 数据可信度自评

| 章节 | 可信度 | 理由 |
|---|---|---|
| §5.3 10.5cm C/37 vs C/31d | **高** | navweaps 有明确的舰名对照表 + 脚注说明更换时间，且与 navypedia 的「all LC/37」结论相容 |
| §5.6 鱼雷管存在与数量 | **高** | 五家一致；但**加装时间**三说并存（低） |
| §3 巡航汽轮机 | **高** | kbismarck 动力专页 + dewiki 独立确认 |
| §9 雷达演进 | **中高** | navweaps 给了月份级时间点，但用「Probably」「possibly」措辞；navypedia 的 4×FuMO 27 无法与之调和 |
| §8 建造信息 | **中** | 服役/下水/厂/船台号高度一致；**龙骨日期四说**（低） |
| §1 排水量 | **中** | 「比 Bismarck 重约 1,200」收敛；但标准/满载的具体数字各家自相矛盾，kbismarck 站内两页打架 |
| §2 尺寸 | **中** | 宽 36.0 一致；全长三说、吃水两说 |
| §5.5 2cm 数量 | **低** | navypedia 时间线内部矛盾，各来源终值 58/72/78 不等 |
| §6 航空 | **中** | luft-196 是一手级；但**弹射器拆除时间全无** |
| §10 涂装 | **低** | 无一手命令，全部二手/照片推断；权威专著正文未获取 |
| §7 装甲 | **高**（「与 Bismarck 相同」这个结论本身） | 多来源一致，仅两处小分歧 |

---

*生成时间：2026-11-17。所有数值均来自上述来源，未做任何编造；换算值已标【推断】。*
