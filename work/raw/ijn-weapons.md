# 中途岛日本海军 舰炮与舰载机 武器档案

> 采集对象：1942 年 6 月中途岛参战日本海军（机动部队四空母 + 护卫舰队）的舰炮 4 型、舰载机 3 型
> 采集日期：2026-11-19
> 编制规则：每条数值附**英文原文照抄** + 来源 URL。查不到写「未获取」，不推算、不跨来源拼凑、不按同级舰类推。
> 来源分级：A=一手档案 / B=同期官方出版物 / C=权威二次文献（NavWeaps、Francillon、Campbell）/ D=专题网站 / E=百科

---

## 采集方法与前置说明

**代理情况**：任务书指定 `127.0.0.1:7897` **不通**，全程**直连**。实测 `http://www.navweaps.com`、`http://www.combinedfleet.com`、`https://en.wikipedia.org`、`https://ja.wikipedia.org`、`https://www.aviation-history.com` 均返回 200。

**取数方式**：`web_fetch` 工具对上述域名会报 SSRF 拦截（域名解析到 198.18.x.x），改用本地 Python `urllib` 直连抓取原文。脚本 `work/ijn-weapons/fetch.py`，原文存 `work/ijn-weapons/raw/`。**所有引文均来自实际抓取并落盘的页面文本**，未使用记忆或推测。

**关于「原文照抄」**：英制 + 公制双列一律照抄来源原样（含来源自身的换算），不做二次折算。口径词（standard / deep load / loaded / gross）照抄来源用语。

**引文格式约定**（为免歧义，先说明三条）：

1. **脚注上标一律略去**。NavWeaps 与日文维基在数值后挂有上标编号（如 `APC Type 5 ²ᵃ`、`Hiryû (1) ¹⁰ᵇ`、`A2 ⁴ᵇ`），本档案引文只留正文，不复制上标。
   例外：日文维基的正文脚注形如 `[35]`（与上标等价），若落在引文中间则原样保留，不删。
2. **本档案中的「」有双重用途**：除引用来源原句外，也用于强调本站自己的术语与标签（如「未获取」「装备舰」「D3A1 列」）。**只有带来源编号（— S1 … — S26）的「」才是原文照抄**；用于强调处不是引文。
2. **表格类引文按「行名 | 值」给出**：`|` 表示原表格的单元格边界。原表并列多个型号时（A6M2/A6M3/A6M5/A6M8、D3A1/D3A2、B5N1/B5N2），**行名与被引的该列数值均逐字照抄，其余型号列省略**；本节各表的「（D3A1 列）」「（B5N2 列）」等标题即指明所取列。原表格一格跨多行时以 `／` 分隔各行，跨行拆分处用 `＋` 标示。
3. **省字以「…」标记**，省略处必不影响数值本身；`／` 用于并列引两段不相连的原文。

---

## §0 纠错：任务书三处前提问题

### 纠错 ①：赤城、加贺装的是 20cm/50 三年式 **No.1（7.9 吋）**，不是 No.2（8 吋）

任务书只写「20cm/50 三年式」，并给出 NavWeaps 链接 `WNJAP_8-50_3ns.htm` —— 那是 **No.2（2 GÔ）** 炮的页面，而 **No.2 的「使用舰」名单里没有赤城、加贺**。

> 「Takao and Tone classes … Furutaka, Aoba, Myôkô and Mogami classes … Ibuki」 — S2（No.2 的使用舰，四空母一艘不在列）

正确的页面是 `WNJAP_79-50_3ns.php`（No.1）：

> 「Designed for a new generation of scout cruisers shortly after World War I, this weapon was also used by the Myôkô class heavy cruisers and on **the aircraft carriers Akagi and Kaga**.」 — S1

> 「By the start of the Pacific War, **these two carriers were the only Japanese ships still armed with these weapons** and they carried them until they were sunk at the Battle of Midway.」 — S1

命名区分（NavWeaps 原文）：

> 「Nomenclature note: Even though these guns were developed in 1930 to 1931, they were still designated as 3rd Year Type (Model 1914). **The No. 2 (2 GÔ) designation was used to distinguish these guns from the older 20 cm (7.9") 3rd Year Type No. 1 (1 GÔ) guns.**」 — S2

两者实弹径也不同：No.1 为 20.0 cm，No.2 为 20.32 cm。

> 「Actual bore diameter was **20.0 cm (7.87")**.」 — S1
> 「Actual bore diameter was **20.32 cm (8.0")**.」 — S2

**后果**：若按 No.2 取数，炮身重（18.7 t vs 17.6 t）、弹重（125.85 kg vs 110 kg）、初速（840 vs 870 mps）、射程（29,400 m vs 28,000 m）**全部会填错**。本档案按 **No.1** 采集。

### 纠错 ②：加贺的 12cm 十年式在 1930 年代已换装为 12.7cm 八九式，赤城则从未换装

任务书写「12cm/45 十年式 —— 赤城的高角炮」「12.7cm/40 八九式 —— 加贺、苍龙、飞龙的高角炮」。**前半对、后半对，但理由要说清**：加贺**竣工时装的也是 12cm 十年式**，是 1935 年改装时才换掉的；赤城则是申请换装被驳回、至死保留 12cm。

> 「The carrier Kaga and those cruisers modernized during the late 1930s had these weapons replaced by the 12.7 cm/40 (5") Type 89 AA gun. **However, Akagi carried them to her end at Midway.**」 — S3

加贺竣工时装备（日文维基要目表原文，分行照抄）：

> 「3年式20cm連装砲2基4門」／「3年式20cm単装砲6門」／「**45口径10年式12cm連装高角砲6基12門**」／「13mm連装機銃4基」／「留式機銃2挺（1931年）」 — S23

改装后：

> 「3年式20cm単装砲 10基10門」／「**89式12.7cm連装高角砲 8基16門**」／「96式25mm連装機銃 11基 または14基」 — S23

赤城未换装的原因（日文维基）：

> 「武装面では、加賀と違って**旧式の十年式45口径12cm高角砲を、新式の八九式40口径12.7cm高角砲に換装・増強できなかった**。設置位置も低い位置のままだったので、依然として反対舷方向は撃てなかった。」 — S22

> 「The ship's 12 cm 10th Year Type guns were scheduled to be replaced by more modern 12.7 cm (5 in) Type 89 mounts in 1942. … However, the ship was lost in combat before the upgrade could take place.」 — S18

### 纠错 ③：NavWeaps 八九式页面的「使用舰」表**漏了苍龙**

任务书把 12.7cm 八九式列为「加贺、苍龙、飞龙」的高角炮。苍龙确实装了 6 基 12 门，但 **NavWeaps 使用舰表里没有 Sôryû**（"Sôryû" 在该页只出现在参考文献书目里）。

> 「Kaga (8), Ryûjô (4), Hiryû (1) 10b, Shôkaku (2) 11b, Hiyo (6), Ryûhô (ex-Taigei) (4) 12b and Shoho (ex-Tsurugizaki) (4) 12b: A1 Mod 2」 — S4（无苍龙）

苍龙的装备须另引舰级来源：

> 「40口径12.7cm連装高角砲」6基12門／「九六式二十五粍高角機銃」連装14基28挺 — S24
> 「6 × twin 12.7 cm (5 in) DP guns」／「14 × twin 25 mm (1 in) AA guns」 — S20

**因此 §3 的「装备舰」栏对苍龙标注为「NavWeaps 未列，据舰级来源补」**，不作同级类推。

---

## §1 20cm/50 三年式 No.1（50口径三年式二〇糎砲 / 20 cm/50 3rd Year Type No. 1）

### §1-A 身份

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 日文原名 | 50口径三年式二〇糎砲（1号） | 「五十口径三年式二〇糎砲」 — S23（加贺要目表链接词） | S23 |
| 英文全称 | 20 cm/50 (7.9") 3rd Year Type (Model 1914) No. 1 | 「20 cm/50 (7.9") 3rd Year Type (Model 1914) No. 1」 | S1 |
| 官方制式名 | 50 caliber 3rd Year Type No. 1 20 cm Gun | 「Official Designation: 50 caliber 3rd Year Type No. 1 20 cm Gun」 | S1 |
| 原制式名 | 20 cm/50 (7.9") 3rd Year Type (Model 1914) | 「Original Designation: 20 cm/50 (7.9") 3rd Year Type (Model 1914)」 | S1 |
| 改称时点 | 1931-04 | 「Redesignation April 1931: 20 cm/50 (7.9") 3rd Year Type (Model 1914) No. 1」 | S1 |
| 常见简称 | 三年式 20cm 炮 / 3rd Year Type / 1 GÔ | 「The No. 1 (1 GÔ) designation was added … after the more powerful 20 cm/50 (8") 3rd Year Type No. 2 (2 GÔ) Gun was adopted on 6 April 1931.」 | S1 |

### §1-B 炮身

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 口径 | 200 mm（实弹径 20.0 cm / 7.87"） | 「Actual bore diameter was 20.0 cm (7.87")」 | S1 |
| 倍径 | L/50 | 「20 cm/50 (7.9")」 | S1 |
| 炮身全长 | 10.000 m（393.7 in） | 「Gun Length oa \| 393.7 in (10.000 m)」 | S1 |
| 膛线部长（bore length） | 9.144 m（381.5 in） | 「Bore Length \| 381.5 in (9.144 m)」 | S1 |
| 膛线长（rifling length） | **未获取** | 「Rifling Length \| N/A」 | S1 |
| 阴线数 | 48 | 「Grooves \| 48」 | S1 |
| 药室容积 | **未获取** | 「Chamber Volume \| N/A」 | S1 |
| 炮身重 | 17.6 吨（17.9 mt） | 「Gun Weight \| 17.6 tons (17.9 mt)」 | S1 |
| 炮身构造 | 部分长度线绕（wire wound），Welin 螺式炮闩、三动作开闭 | 「These guns were wire wound for part of their length and had Welin screw breech blocks with a three-motion breech mechanism.」 | S1 |
| 设计年份 | 1920（1916 在吴海军工厂起步，1921 试制炮验收） | 「Date Of Design \| 1920」／「Design was started in 1916 at the Kure Navy Yard … The prototype gun was proved in 1921.」 | S1 |
| 服役起始 | 1923 | 「Date In Service \| 1923」 | S1 |

### §1-C 弹药（分弹种）

| 弹种 | 弹重 | 原文照抄 | 来源 |
|---|---|---|---|
| APC 五式（穿甲通常弹） | 110 kg（242.5 lbs） | 「APC Type 5 2a: 242.5 lbs. (110 kg)」（2a 为脚注上标） | S1 |
| APC 六号 / 八八式 | 110 kg（242.5 lbs） | 「APC No. 6 / Type 88 3a: 242.5 lbs. (110 kg)」（3a 为脚注上标） | S1 |
| 通常弹 四式（高爆） | 110 kg（242.5 lbs） | 「Common Type 4 HE 4a: 242.5 lbs. (110 kg)」（4a 为脚注上标） | S1 |

| 弹种 | 装药重 | 原文照抄 | 来源 |
|---|---|---|---|
| APC 五式 | 2.9 kg（6.4 lbs） | 「APC Type 5: 6.4 lbs. (2.9 kg)」 | S1 |
| APC 六号 / 八八式 | 2.84 kg（6.3 lbs） | 「APC No. 6 / Type 88: 6.3 lbs. (2.84 kg)」 | S1 |
| 通常弹 四式 | 7.3 kg（16.1 lbs） | 「Common Type 4: 16.1 lbs. (7.3 kg)」 | S1 |

| 装药 | 重量 | 原文照抄 | 来源 |
|---|---|---|---|
| 穿甲弹用 60 DC | 32.55 kg（71.76 lbs） | 「APC Projectiles \| 71.76 lbs (32.55 kg) 60 DC」 | S1 |
| 穿甲弹用 70 C2 | 32.55 kg | 「71.76 lbs (32.55 kg) 70 C2」 | S1 |
| 穿甲弹用 80 C2 | 32.55 kg | 「71.76 lbs (32.55 kg) 80 C2」 | S1 |
| 穿甲弹用 53 DC | 32.55 kg | 「71.76 lbs. (32.55 kg) 53 DC」 | S1 |
| 通常弹用 C2 | 25.40 kg（56.0 lbs） | 「Common Projectiles \| 56.0 lbs. (25.40 kg) C2」 | S1 |

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 初速 | 870 mps（2,854 fps，单值，未分弹种） | 「Muzzle Velocity \| 2,854 fps (870 mps)」 | S1 |
| 膛压 | 3,000 kg/cm²（19 tons/in²） | 「Working Pressure \| 19 tons/in2 (3,000 kg/cm2)」 | S1 |
| 炮身寿命 | 约 300 发 | 「Approximate Barrel Life \| 300 rounds」 | S1 |
| 弹长 | 76.2 cm（30 in） | 「Projectile Length \| 30 in (76.2 cm)」 | S1 |

### §1-D 弹道

| 仰角 | 射程 | 原文照抄 | 来源 |
|---|---|---|---|
| 25° | 24,000 m | 「25 degrees \| 26,250 yards (24,000 m)」 | S1 |
| 40° | 26,700 m | 「40 degrees \| 29,200 yards (26,700 m)」 | S1 |
| 45° | 28,000 m | 「45 degrees \| 30,620 yards (28,000 m)」 | S1 |
| **最大射程 / 对应仰角** | **28,000 m @ 45°** | 同上 | S1 |
| **最大射高** | **不适用**（非高射炮） | 页面无 AA ceiling 项；仅列仰角-射程表 | S1 |

> 口径分歧提示（来源内部）：「These figures are from "Japanese Cruisers of the Pacific War" but "Naval Weapons of World War Two" says that the range @ 25 degrees was **24,700 yards (22,600 m)** during World War II. This may be the result of different propellants being used during World War II.」 — S1

### §1-E 射速与炮架

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 理论射速 | 3–5 发/分（古鹰级除外） | 「Others: 3 to 5 rounds per minute」 | S1 |
| 古鹰级实战射速 | 低于 2 发/分 | 「Furutaka class 3: Less than 2 rounds per minute」（上标 `3` 为脚注编号） | S1 |
| **赤城/加贺适用值** | **3–5 发/分（理论）；实战射速未获取** | 赤城、加贺属「Others」栏；来源未单列其实战射速 | S1 |
| 弹药基数（每门） | 120 发 | 「Ammunition stowage per gun \| 120 rounds」 | S1 |

| 炮架型号 | 装舰 | 重量 | 俯仰 | 原文照抄 | 来源 |
|---|---|---|---|---|---|
| 单装 Model A1（炮廓式） | 赤城 6、加贺 10（1930 年代改装后） | 56.6 吨（57.5 mt，Model A 值） | −5 / +25° | 「Akagi (6) and Kaga (10) (after modernization during 1930s): Model A1」／「Model A Single Mount: 56.6 tons (57.5 mt)」／「Model A and Model A1 Single Mounts: -5 / +25 degrees」 | S1 |
| 连装 Model B（炮塔式） | 赤城 2、加贺 2（竣工时，1930 年代拆除） | N/A，估约 172 吨 | −5 / +70° | 「Akagi (2) and Kaga (2) (as built - all were removed during 1930s modernizations): Model B」／「Model B Twin Turret: N/A, but probably about 172 tons (175 mt)」／「Model B Twin Turrets: -5 / +70 degrees」 | S1 |

**赤城/加贺实际配置（口径差异见 §1-A）**：

| 舰 | 竣工时 | 1930 年代改装后 | 原文照抄 | 来源 |
|---|---|---|---|---|
| 赤城 | 单装 6 + 连装 2 基（4 门）= 10 门 | 单装 6 门（炮廓） | 「Akagi (6) and Kaga (6) (as built): Model A1」／「Akagi (6) and Kaga (10) (after modernization during 1930s): Model A1」／「Akagi (2) and Kaga (2) (as built - all were removed during 1930s modernizations): Model B」 | S1 |
| 加贺 | 单装 6 + 连装 2 基（4 门）= 10 门 | 单装 10 门（炮廓） | 「3年式20cm連装砲2基4門」／「3年式20cm単装砲6門」／「3年式20cm単装砲 10基10門」（改装后） | S23 |

**回转性能**：

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 俯仰速度 Model A1 | **未获取** | 「Model A Single Mounts: N/A」 | S1 |
| 俯仰速度 Model B | **未获取**（来源推测 12°/s） | 「Model B Twin Turrets: N/A (probably the same 12 degrees per second achieved by the Model E)」 | S1 |
| 回转速度 Model B | **未获取**（来源推测 4°/s） | 「Model B Twin Turrets: N/A (probably the same 4 degrees per second achieved by the Model E)」 | S1 |
| 回转范围（空母炮座） | 约 +20 / +160°（不能跨甲板射击） | 「Carrier Single and Twin Mounts: About +20 / +160 degrees」／「Neither the Model A1 single mountings nor the Model B twin mountings used on carriers could fire cross-deck.」 | S1 |
| 装填角 | Model A/A1：+5 ~ +9°；Model B：+5° | 「Model A, Model A1 and Model C: +5 to +9 degrees」「Model B and Model D: +5 degrees」 | S1 |

**两条空母专属限制（关键）**：

> 「The maximum elevation of the Model B was +70 degrees, but the elevating and recoil mechanisms proved to be fragile and it was found that **+55 degrees was the maximum practical elevation**.」 — S1

> 「The elevation of **the single guns used on Akagi and Kaga was restricted to 20-23 degrees** for much of their training arc in order to avoid blast damage. These guns were mounted low in the ships and were of limited use.」 — S1

**实战记录（赤城）**：

> 「ミッドウェー海戦で赤城は20cm砲を最低54発発射しているが[35]、飛行甲板への影響については不明である。」 — S22

### §1-F 装备舰（中途岛相关）

| 舰 | 数量 | 原文照抄 | 来源 |
|---|---|---|---|
| 赤城 | 6 门单装（炮廓） | 「Akagi (6) and Kaga (10) (after modernization during 1930s): Model A1」 | S1 |
| 加贺 | 10 门单装（炮廓） | 「Kaga (10) (after modernization during 1930s): Model A1」 | S1 |
| — | **太平洋战争爆发时全日本仅此二舰仍装此炮** | 「these two carriers were the only Japanese ships still armed with these weapons」 | S1 |
| 利根 / 筑摩 | **不适用**（装 No.2，见 §0 纠错①） | 「Takao and Tone classes」为 No.2 使用舰 | S2 |
| 榛名 / 雾岛 | **不适用**（战列舰，主炮为 36cm） | — | — |

---

## §2 12cm/45 十年式（四五口径十年式十二糎高角砲 / 12 cm/45 10th Year Type）

### §2-A 身份

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 日文原名 | 四五口径十年式十二糎高角砲 | 「四五口径十年式十二糎高角砲」 | S23 |
| 英文全称 | 12 cm/45 (4.7") 10th Year Type (Model 1921) | 「12 cm/45 (4.7") 10th Year Type (Model 1921)」 | S3 |
| 官方制式名 | 45 caliber 10th Year Type 12 cm | 「Official Designation: 45 caliber 10th Year Type 12 cm」 | S3 |
| 常见简称 | 十年式 12cm 高角炮 / 12cm 10th Year | 「12 cm/45 (4.7") 10th Year Type」 | S3 |
| 设计谱系 | 由单用 12cm/45 三年式 派生 | 「This was an AAA weapon derived from the single-purpose 12 cm/45 (4.7") 3rd Year Type.」 | S3 |

### §2-B 炮身

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 口径 | 120 mm（4.7"） | 「12 cm/45 (4.7")」 | S3 |
| 倍径 | L/45 | 同上 | S3 |
| 炮身全长 | 5.604 m（220.6 in） | 「Gun Length oa \| 220.6 in (5.604 m)」 | S3 |
| 膛线部长 | 5.400 m（212.6 in） | 「Bore Length \| 212.6 in (5.400 m)」 | S3 |
| 膛线长 | 4.649 m（183 in） | 「Rifling Length \| 183 in (4.649 m)」 | S3 |
| 阴线 | 34 条（部分炮 36 条） | 「(34) 0.057 in deep x 0.263 in (1.45 mm x 6.688 mm)」／「Some guns had 36 rather than 34 grooves.」 | S3 |
| 药室容积 | 10.774 dm³（657.5 in³） | 「Chamber Volume \| 657.5 in3 (10.774 dm3)」 | S3 |
| 炮身重 | 2.95 mt（2.9 吨） | 「Gun Weight \| 2.9 tons (2.95 mt)」 | S3 |
| 炮身构造 | 早期 built-up，后期 monobloc；半自动滑动炮闩 | 「The earlier guns were of built-up construction but the later ones were of monobloc construction. All used a semi-automatic sliding breech-block mechanism.」 | S3 |
| 设计年份 | 1921 | 「Date Of Design \| 1921」 | S3 |
| 服役起始 | 1926 | 「Date In Service \| 1926」 | S3 |
| 总产量 | 约 3,000 门 | 「A total of about 3,000 guns were manufactured」 | S3 |

### §2-C 弹药

| 弹种 | 全弹重 | 弹重 | 原文照抄 | 来源 |
|---|---|---|---|---|
| 通常弹 零式（高爆） | 34 kg | 20.3 kg | 「Common Type 0 HE 2a: 44.9 lbs. (20.3 kg)」（2a 为脚注上标）／「Weight of Complete Round … Common Type 0 HE: 75 lbs. (34 kg)」 | S3 |
| 通常弹 一式（高爆） | 34 kg | 20.3 kg | 「Common Type 1 HE: 44.9 lbs. (20.3 kg)」 | S3 |
| 通常弹 四式（三式弹/焼霰弹） | **未获取** | **未获取** | 「Common Type 4 IS 3a: N/A」（3a 为脚注上标） | S3 |
| 对潜弹（ASW） | — | 16.4 kg | 「ASW: 36.3 lbs. (16.4 kg)」 | S3 |
| 照明弹 | — | 约 20.3 kg | 「Illum: about 44.9 lbs. (20.3 kg)」 | S3 |
| 新型弹 | — | 22.5 kg | 「New Type Projectile: 49.6 lbs. (22.5 kg)」 | S3 |

| 弹种 | 装药重 | 原文照抄 | 来源 |
|---|---|---|---|
| 通常弹 零式 | 1.7 kg | 「Common Type 0 HE: 3.75 lbs. (1.7 kg)」 | S3 |
| 通常弹 一式 | 1.9 kg | 「Common Type 1 HE: 4.07 lbs. (1.9 kg)」 | S3 |
| 对潜弹 | 3.8 kg | 「ASW: 7.19 lbs. (3.8 kg)」 | S3 |
| 新型弹 | 1.9 kg | 「New Type Projectile: 4.07 lbs. (1.9 kg)」 | S3 |

| 装药 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 1929 年前常装药 | 5.06 kg 36 C2 | 「Common charge (prior to 1929): 11.2 lbs. (5.06 kg) 36 C2」 | S3 |
| 1929 年后常装药 | 5.5 kg 30 DC | 「Common charge (after 1929): 12.1 lbs. (5.5 kg) 30 DC」 | S3 |
| 减装药 | 重量未获取 | 「Reduced charge: [Weight N/A] 36 C2 or 30 DC or 20 T2」 | S3 |
| 轻装药 | 重量未获取 | 「Light charge: [Weight N/A] 20 C2 or 20 C3」 | S3 |
| 药筒 | 黄铜 120 × 708R，空重 14.4 kg | 「Brass, 120 x 708R, 30 lbs. (14.4 kg)」 | S3 |
| 弹药类型 | 定装式 | 「Type \| Fixed」 | S3 |

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 初速（通常弹） | 825–830 mps | 「Common HE: 2,707 to 2,723 fps (825 to 830 mps)」 | S3 |
| 初速（照明弹） | 700 mps | 「Illum: 2,297 fps (700 fps)」 | S3 |
| 初速（对潜弹） | 250 mps | 「ASW: 820 fps (250 mps)」 | S3 |
| 膛压 | 2,650 kg/cm² | 「Working Pressure \| 16.8 tons/in2 (2,650 kg/cm2)」 | S3 |
| 炮身寿命 | 700–1,000 发 | 「Approximate Barrel Life \| 700 - 1,000 rounds」 | S3 |
| 弹药基数（每门） | 200–250 发 | 「Ammunition stowage per gun \| 200 - 250 rounds」 | S3 |

### §2-D 弹道

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| **最大射程** | **16,000 m @ 45°** | 「Range with 45.0 lbs. (20.4 kg) HE Shell and 30 DC propellant … 45 degrees \| 17,500 yards (16,000 m)」 | S3 |
| **最大射高** | **10,000 m @ 75°** | 「75 degrees \| 32,800 feet (10,000 m)」 | S3 |
| 对潜弹射程 | 4,000 m @ 40° | 「40 degrees \| 4,375 yards (4,000 m)」 | S3 |
| 对潜弹最小射程 | 820 m | 「Minimum range of ASW shell is given as 750 yards (820 m). Ranges less than this tended to ricochet.」 | S3 |
| 照明弹最大射程 | 14,000 m | 「Illumination rounds were rated at 600,000 candle power and had a maximum range of 15,310 yards (14,000 m).」 | S3 |
| 新型弹 | 20,500 m @ 45°；13,000 m @ 75° | 「a maximum surface range of 22,430 yards (20,500 m) and a maximum AA Ceiling of 42,660 feet (13,000 m) at 75 degrees elevation」 | S3 |

### §2-E 射速与炮架

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 理论射速 | 10–11 发/分 | 「Rate Of Fire \| Maximum: 10 - 11 rounds per minute」 | S3 |
| 实战射速 | 6–8 发/分 | 「Effective: 6 - 8 rounds per minute」 | S3 |
| 实弹演练数据 | 6.4 发/分（妙高级 1931 年对空射击） | 「Firing was at an average of 6.4 rounds per minute at ranges between 2,000 and 5,500 m」 | S3 |

| 炮架 | 装舰 | 重量 | 原文照抄 | 来源 |
|---|---|---|---|---|
| 连装 A2 | **赤城 6 基（12 门）**、加贺 6 基（竣工时） | 20 吨（20.3 mt） | 「Akagi (6), Kaga (6) …: A2」／「Twin Mounts A2 4b: 20 tons (20.3 mt)」 | S3 |
| 单装 B / B2 / C | 妙高、青叶、古鹰、高雄、大鹰级等（非四空母） | B 7.8 mt；B2 10.0 mt；C N/A | 「B: 7.7 tons (7.8 mt)」「B2: 9.8 tons (10.0 mt)」「C: N/A」 | S3 |

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 俯仰范围 | −10 / +75° | 「Elevation \| -10 / +75 degrees」 | S3 |
| 俯仰速度（A2） | 6.5°/s | 「B2 and A2: 6.5 degrees per second」 | S3 |
| 回转范围（大型舰） | 约 ±70° | 「Larger ships: About +/- 70 degrees」 | S3 |
| 回转速度（A2） | 10°/s | 「B2 and A2: 10 degrees per second」 | S3 |
| 后座行程 | 49.0 cm（19.3 in） | 「Gun recoil \| 19.3 in (49.0 cm)」 | S3 |
| 装填角 | 任意角 | 「Loading Angle \| Any」 | S3 |
| 驱动方式 | 电动-液压 | 「Type C, B2 and A2 mounts were electro-hydraulically powered.」 | S3 |
| 装填 | 全人力装填、人力定引信 | 「All mountings were hand loaded and fuze setting was by hand.」 | S3 |

### §2-F 装备舰（中途岛相关）

| 舰 | 状态 | 原文照抄 | 来源 |
|---|---|---|---|
| **赤城** | 6 基 12 门，至沉没未换装 | 「World War II Carriers: **Akagi**, Taiyo and Unyo classes」／「However, Akagi carried them to her end at Midway.」 | S3 |
| 加贺 | 竣工时 6 基 12 门，1935 改装时撤除换 12.7cm | 「The carrier Kaga … had these weapons replaced by the 12.7 cm/40 (5") Type 89 AA gun.」 | S3 |
| 苍龙 / 飞龙 | **不适用**（建成即装 12.7cm） | 使用舰表未列 | S3 |
| 利根 / 筑摩 / 榛名 / 雾岛 | **不适用** | 使用舰表未列 | S3 |

---

## §3 12.7cm/40 八九式（四十口径八九式十二糎七高角砲 / 12.7 cm/40 Type 89）

### §3-A 身份

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 日文原名 | 四十口径八九式十二糎七高角砲 | 「四十口径八九式十二糎七高角砲」 | S24 |
| 英文全称 | 12.7 cm/40 (5") Type 89 (Model 1929) | 「12.7 cm/40 (5") Type 89 (Model 1929)」 | S4 |
| 官方制式名 | 40 caliber Type 89 12.7 cm Gun | 「Official Designation: 40 caliber Type 89 12.7 cm Gun」 | S4 |
| 常见简称 | 八九式 12.7cm 高角炮 / Type 89 | 「12.7 cm/40 (5") Type 89」 | S4 |
| 易混型号 | Type 88（潜艇用，非本型） | 「The Type 88 was a submarine weapon which was not widely used. The very similar Type 89 was the first Japanese AAA weapon designed for the purpose」 | S4 |

### §3-B 炮身

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 口径 | 127 mm（5"） | 「12.7 cm/40 (5")」 | S4 |
| 倍径 | L/40 | 同上 | S4 |
| 炮身全长 | 5.284 m（208 in） | 「Gun Length oa \| 208 in (5.284 m)」 | S4 |
| 膛线部长 | 5.080 m（200 in） | 「Bore Length \| 200 in (5.080 m)」 | S4 |
| 膛线长 | 4.450 m（175 in） | 「Rifling Length \| 175 in (4.450 m)」 | S4 |
| 阴线 | 36 条 | 「(36) 0.060 in deep x 0.261 in (1.52 mm x 6.63 mm)」 | S4 |
| 药室容积 | 9.0 dm³（549 in³） | 「Chamber Volume \| 549 in3 (9.0 dm3)」 | S4 |
| 炮身重 | 3.1 mt（3.05 吨） | 「Gun Weight \| 3.05 tons (3.1 mt)」 | S4 |
| 炮身构造 | 自紧 monobloc 身管 + 炮尾环，横动式炮闩 | 「These weapons were of simple construction with autofretted monobloc barrels and breech rings and used horizontal sliding breech-blocks.」 | S4 |
| 设计年份 | 1928（Type 88）/ 1929（Type 89） | 「Date Of Design \| 1928 / 1929」 | S4 |
| 试制炮验收 | 1931 | 「The Type 89 prototype was proved in 1931」 | S4 |
| 服役起始 | 1932-02-06 制式采用 | 「Date In Service \| 1932」／「adopted for service use on 6 February 1932」 | S4 |
| 总产量 | 1,306 门（其中 1941–45 造 836 门） | 「Total production of Type 89 guns amounted to 1,306 guns, with 836 being manufactured between 1941 and 1945.」 | S4 |

### §3-C 弹药

| 弹种 | 全弹重 | 弹重 | 原文照抄 | 来源 |
|---|---|---|---|---|
| 通常弹 零式（高爆） | 34.32 kg | 23.45 kg | 「Common Type 0 HE 1a: 51.7 lbs. (23.45 kg)」／「Weight of Complete Round … Common Type 0 HE: 75.7 lbs. (34.32 kg)」 | S4 |
| 通常弹 三式（焼霰弹/三式弹） | 35 kg | 23.0 kg | 「Common Type 3 IS 2a: 50.7 lbs. (23.0 kg)」（2a 为脚注上标）／「Common Type 3 IS: 77.2 lbs. (35 kg)」 | S4 |
| 对潜弹（ASW） | — | 20.9 kg | 「ASW 3a: 46.2 lbs. (20.9 kg)」 | S4 |
| 照明弹 | 34.32 kg | 23.45 kg | 「Illum 4a: 51.7 lbs. (23.45 kg)」 | S4 |

| 弹种 | 装药 | 原文照抄 | 来源 |
|---|---|---|---|
| 通常弹 零式 | 1.88 kg 下濑火药 | 「Common Type 0 HE: 4.2 lbs. (1.88 kg) Shimose」 | S4 |
| 通常弹 三式 | 43 根烧霰管 + 23 根支柱 | 「Common Type 3 IS: Contained 43 incendiary tubes and 23 stays」 | S4 |
| 对潜弹 | 4.0 kg | 「ASW: 8.78 lbs. (4.0 kg)」 | S4 |

| 装药 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 发射药 | 3.98 kg 21 DC | 「Propellant Charge \| 8.77 lbs. (3.98 kg) 21 DC」 | S4 |
| 药筒 | 黄铜 127 × 583 mm，空重 6.9 kg | 「Brass, 127 x 583 mm, about 15.23 lbs. (6.9 kg)」 | S4 |
| 弹药类型 | 定装式 | 「Type \| Fixed」 | S4 |
| 全弹长 | 97.1 cm（38.2 in） | 「Complete Round Length \| 38.2 in (97.1 cm)」 | S4 |

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 初速（通常弹/三式弹） | 700–725 mps | 「Common Type 0 HE: 2,360 - 2,379 fps (700 - 725 mps)」 | S4 |
| 初速（对潜弹） | 250 mps | 「ASW: 820 fps (250 mps)」 | S4 |
| 初速（照明弹） | 720 mps | 「Illum: 2,362 fps (720 mps)」 | S4 |
| 膛压 | 2,500 kg/cm² | 「Working Pressure \| 16 tons/in2 (2,500 kg/cm2)」 | S4 |
| 炮身寿命 | 800–1,500 发 | 「Approximate Barrel Life \| 800 - 1500 rounds」 | S4 |
| 弹药基数（每门） | 翔鹤 250 发；其他 **未获取** | 「Shôkaku: 250 rounds」／「Others: N/A」 | S4 |

### §3-D 弹道

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| **最大射程（三式弹）** | **14,800 m @ 45°** | 「Range of IS projectiles … 45 degrees \| 16,185 yards (14,800 m)」 | S4 |
| **最大射高** | **9,400 m @ 75°** | 「AA Ceiling @ 75 degrees \| 30,840 feet (9,400 m)」 | S4 |
| 对潜弹射程 | 4,300 m @ 40° | 「40 degrees \| 4,700 yards (4,300 m)」 | S4 |
| 对潜弹最小射程 | 800 m | 「Minimum range of ASW shell is given as 875 yards (800 m).」 | S4 |
| 照明弹最大射程 | 14,550 m | 「Illumination rounds were rated at 680,000 candle power and had a maximum range of 15,910 yards (14,550 m)」 | S4 |
| 通常弹（零式）射程 | **未获取**（该页仅给三式弹射程） | 页面 Range 节标题为「Range of IS projectiles」 | S4 |

### §3-E 射速与炮架

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| **理论射速** | 14 发/分（初期） | 「Type 89: 14 rounds per minute initially」 | S4 |
| **持续射速** | 8 发/分 | 「8 rounds per minute sustained」 | S4 |
| Type 88 射速 | 8 发/分 | 「Type 88: 8 rounds per minute」 | S4 |

| 炮架型号 | 装舰 | 重量 | 原文照抄 | 来源 |
|---|---|---|---|---|
| A1（无防盾） | 榛名/雾岛（金刚级）4 基、飞龙 5 基 | 20 吨（20.3 mt） | 「Kongô (4) …: A1」／「Hiryû (5) …: A1」／「A1: 20 tons (20.3 mt)」 | S4 |
| A1 Mod 1（加防盾） | 妙高、最上、利根 4 基、筑摩 | 24 吨（24.5 mt） | 「Myôkô (4), Mogami (4) … Tone (4) and Ibuki (4): A1 Mod 1」／「A1 Mod 1: 24 tons (24.5 mt)」 | S4 |
| A1 Mod 2（防盾气密） | **加贺 8 基**、飞龙 1 基、翔鹤 2 基 | 约 24 吨 | 「Kaga (8) … Hiryû (1) …: A1 Mod 2」／「A1 Mod 2: about 24 tons (24.5 mt)」 | S4 |
| A1 Mod 3（厚防盾，抗 46cm 爆风） | 大和 6 基 | 29 mt | 「Yamato (6) 5b: A1 Mod 3」／「A1 Mod 3: 28.5 tons (29 mt)」 | S4 |

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 俯仰范围 | −7 / +90°（一说 −8 / +85°） | 「Type 89: -7 / +90 degrees (one source says -8 / +85 degrees)」 | S4 |
| 俯仰速度（A1 全型） | 12°/s | 「A1 (all): 12 degrees per second」 | S4 |
| 回转速度（A1 全型） | 6–7°/s | 「A1 (all): 6 to 7 degrees per second」 | S4 |
| 回转范围（舷侧炮座） | 约 ±70° | 「Amidships Mounts: About -70 / +70 degrees」 | S4 |
| 回转范围（首尾炮座） | 约 ±150° | 「Bow and Stern Mounts: About -150 / +150 degrees」 | S4 |
| 后座行程 | 45.0 cm（17.75 in） | 「Gun recoil \| 17.75 in (45.0 cm)」 | S4 |
| 装填角 | 任意角 | 「Loading Angle \| Any」 | S4 |
| 驱动方式 | 电动油压（回转+俯仰） | 「All twin mountings were to a generally similar design and used electrically driven oil hydraulic gear for both training and elevation.」 | S4 |
| 遂发方式 | 弹簧撞锤，由后座待发 | 「Used a spring rammer cocked by the recoil, similar to other Japanese AAA weapons.」 | S4 |

### §3-F 装备舰（中途岛相关）

| 舰 | 数量/型号 | 原文照抄 | 来源 |
|---|---|---|---|
| **加贺** | 8 基 16 门，A1 Mod 2 | 「Kaga (8) …: A1 Mod 2」 | S4 |
| **飞龙** | 5 基 A1 + 1 基 A1 Mod 2（共 6 基 12 门） | 「Hiryû (5) 10b …: A1」／「Hiryû (1) 10b …: A1 Mod 2」 | S4 |
| **苍龙** | 6 基 12 门 —— **NavWeaps 未列，据舰级来源** | 「40口径12.7cm連装高角砲：6基12門」（S24）／「6 × twin 12.7 cm (5 in) DP guns」（S20） | S24 / S20 |

---

## §4 25mm 九六式（九六式二十五粍高角機銃 / 25 mm/60 Type 96）

### §4-A 身份

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 日文原名 | 九六式二十五粍高角機銃 | 「九六式二十五粍高角機銃」 | S24 |
| 英文全称 | 25 mm/60 (1") Type 96 (Model 1936) | 「25 mm/60 (1") Type 96 (Model 1936)」 | S5 |
| 官方制式名 | 96 Type 25 mm Machine Gun | 「Official Designation: 96 Type 25 mm Machine Gun」 | S5 |
| 常见简称 | 九六式机铳 / Type 96 25mm | 「The 25 mm Type 96」 | S5 |
| 原型 | 法国哈奇开斯（Hotchkiss）；法造样炮称 Type 94/95「Type J」 | 「A design based upon the French Hotchkiss machine gun was selected as the replacement. French built twin mounts, designated as 25 mm Type 94 and Type 95, were tested at the Yokosuka Navy Yard in 1935.」 | S5 |

### §4-B 炮身

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 口径 | 25 mm（1"） | 「25 mm/60 (1")」 | S5 |
| 倍径 | L/60 | 同上 | S5 |
| 炮身全长 | 2.296 m（90.4 in） | 「Gun Length oa \| 90.4 in. (2.296 m)」 | S5 |
| 身管长（barrel） | 1.500 m（59.1 in） | 「Barrel Length \| 59.1 in (1.500 m)」 | S5 |
| 膛线长 | 1.350 m（53.2 in） | 「Rifling Length \| 53.2 in. (1.350 m)」 | S5 |
| 阴线 | 12 条 | 「(12) 0.0098 in deep x 0.141 in (0.25 mm x 3.58 mm)」 | S5 |
| 炮身重 | 115 kg（不含弹匣） | 「Gun Weight \| 253.5 lbs. (115 kg) not including magazine」 | S5 |
| 炮身构造 | 锻造单块身管，导气式自动 | 「This weapon had a forged monobloc barrel and the automatics were gas-operated.」 | S5 |
| 设计年份 | 1935（日本国产化） | 「Date Of Design \| 1935 (In Japan)」 | S5 |
| 服役起始 | 1936-08-06 | 「Date In Service \| 1936」／「adopted for service use on 6 August 1936」 | S5 |
| 总产量 | 约 33,000 门 | 「a total of about 33,000 guns being manufactured」 | S5 |

### §4-C 弹药

| 弹种 | 弹重 | 原文照抄 | 来源 |
|---|---|---|---|
| 穿甲弹（AP） | 0.26 kg | 「AP: 0.57 lbs. (0.26 kg)」 | S5 |
| 通常弹（Common） | 0.24 kg | 「Common: 0.55 lbs. (0.24 kg)」 | S5 |
| 烧夷通常弹 | 0.25 kg | 「Incendiary Common: 0.55 lbs. (0.25 kg)」 | S5 |
| 曳光弹 | 0.25 kg | 「Tracer: 0.55 lbs. (0.25 kg)」 | S5 |

| 弹种 | 装药 | 原文照抄 | 来源 |
|---|---|---|---|
| 穿甲弹 / 曳光弹 | 无装药 | 「AP and Tracer: None」 | S5 |
| 通常弹 | 0.01 kg | 「Common: 0.02 lbs. (0.01 kg)」 | S5 |
| 烧夷通常弹 | 0.01 kg | 「Incendiary Common: 0.02 lbs. (0.01 kg)」 | S5 |

| 装药 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 发射药 | 102–110 g，Type 1 No. 2（K3） | 「Propellant Charge \| 3.60 - 3.88 oz. (102 - 110 gm) Type 1 No. 2 (K3)」 | S5 |
| 全弹重 | 约 0.68 kg | 「Weight of Complete Round \| All types about 1.5 lbs. (0.68 kg)」 | S5 |
| 弹种识别色 | AP 白 / Common 褐红 / 烧夷 橙 / 曳光 黄 | 「AP \| White」「Common \| Maroon」「Incendiary Common \| Orange」「Tracer \| Yellow」 | S5 |
| 弹匣容量 | **15 发** | 「The magazines for the Type 96 held only 15 rounds」 | S5 |

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 初速 | 900 mps（2,953 fps） | 「Muzzle Velocity \| 2,953 fps (900 mps)」 | S5 |
| 膛压 | 2,700 kg/cm² | 「Working Pressure \| 17.1 tons/in2 (2,700 kg/cm2)」 | S5 |
| 炮身寿命 | 12,000 发 | 「Approximate Barrel Life \| 12,000 rounds」 | S5 |
| 弹药基数（每门） | 2,000 发 | 「Ammunition stowage per gun \| 2,000 rounds」 | S5 |
| 混装比例 | 每 5 发 1 发曳光 | 「Normal allocation was one tracer in every five rounds.」 | S5 |

### §4-D 弹道

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 射程 @ 45° | 6,800 m | 「45 degrees \| 7,439 yards (6,800 m)」 | S5 |
| **最大射程** | **7,500 m @ 50°** | 「50 degrees \| 8,200 yards (7,500 m)」 | S5 |
| **有效射高** | **3,000 m @ 85°** | 「AA Ceiling @ 85 degrees \| Effective: 9,843 feet (3,000 m)」 | S5 |
| **最大射高** | **5,500 m @ 85°** | 「Maximum: 18,040 feet (5,500 m)」 | S5 |
| 来源分歧提示 | 来源间射程/射高不一致，NavWeaps 取 Campbell/Lacroix | 「The sources listed below disagree as to the ranges and AA ceiling for this weapon. I have chosen to use those given in "Japanese Cruisers of the Pacific War."」 | S5 |

### §4-E 射速与炮架

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| **理论（循环）射速** | 200–260 发/分，标准 220 | 「Cyclic: 200 - 260 rounds per minute, 220 standard」 | S5 |
| **实战（有效）射速** | 110–120 发/分 | 「Effective: 110 - 120 rounds per minute」 | S5 |
| 影响射速的缺陷 | 高仰角抛壳不良、频繁卡壳 | 「Cartridge ejection was a problem at high elevations and stoppages were frequent.」 | S5 |

| 炮架型号 | 重量 | 原文照抄 | 来源 |
|---|---|---|---|
| 单装（Model 1/3/10） | 785 kg | 「Single: 1,731 lbs. (785 kg)」 | S5 |
| 连装（Model 1/2） | 1,100 kg | 「Twin: 2,425 lbs. (1,100 kg)」 | S5 |
| 三连装（Model 1/2） | 1,800 kg | 「Triple: 3,970 lbs. (1,800 kg)」 | S5 |
| 炮架总数 | 约 20,000 基 | 「About 20,000 mountings of all types were produced.」 | S5 |

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 俯仰范围 | −10 / +85° | 「Elevation \| -10 / +85 degrees」 | S5 |
| 俯仰速度 | 多数人力；部分三连装 Ward-Leonard 随动 12°/s | 「Most were manually operated」／「Some triples had Ward-Leonard RPC: 12 degrees per second」 | S5 |
| 回转范围 | 360° | 「Train \| 360 degrees」 | S5 |
| 回转速度 | 多数人力；部分三连装随动 18°/s | 「Some triples had Ward-Leonard RPC: 18 degrees per second」 | S5 |
| 后座行程 | 11 cm（4.33 in） | 「Gun recoil \| 4.33 in (11 cm)」 | S5 |
| 人力操作方式 | 连装/三连装均齿轮手轮驱动 | 「Twin Models 1 and 2 were trained and elevated by geared handwheels.」／「Triple Models 1 and 2 were trained and elevated by geared handwheels.」 | S5 |
| 炮班人数 | 三连装 9 人、连装 7 人、单装 3 人 | 「Manually controlled Triple mountings had nine crewmembers … Twin mountings were similarly manned (seven crewmembers total). Single mountings had three crewmembers」 | S5 |
| 装填 | 全人力，无专用装填装置 | 「Apparently, all magazines had to be loaded by hand as no specialized loading equipment was ever developed.」 | S5 |
| 三连装出现时点 | 1941 | 「Originally issued in twin mountings, triple mounts were introduced in 1941 and single mounts in 1943.」 | S5 |

**日方自评五大缺陷（USNTMJ O-47(N)-2）**：

> 「The multiple mounts could not be trained and elevated rapidly enough, either by power or manual drive. / The gunsights were inadequate against high speed aircraft. / The guns had excessive vibration, making them difficult to keep on target. / The capacity of the ammunition supply equipment was inadequate, causing interrupted fire and a greatly reduced operating routine. / The muzzle blast caused problems for both the guncrew and equipment.」 — S5

### §4-F 装备舰（中途岛四空母）

| 舰 | 座数与管数 | 原文照抄 | 来源 |
|---|---|---|---|
| 赤城 | 连装 14 基 28 门 | 「25mm連装機銃 14基28門」 | S22 |
| 加贺 | 连装 11 基（22 挺）**或** 14 基（28 挺）—— 两说并存 | 「96式25mm連装機銃 11基 または14基」／「11式軽機銃6挺（1938年）」 | S23 |
| 苍龙 | 连装 14 基 28 挺 | 「九六式二十五粍高角機銃」連装14基28挺 — S24 |
| 飞龙 | 三连装 7 基（21 挺）+ 连装 5 基（10 挺）= **31 挺** | 「九六式二十五粍高角機銃：3連装7基、連装5基 計31挺」 | S25 |
| 利根 / 筑摩 | 一等巡洋舰标准 18 基三连装 + 16 单装 | 「First class (Heavy) cruisers \| 18 \| - \| 16」（O-47(N)-2 标准配置，非逐舰实数） | S5 |
| 榛名 / 雾岛 | 金刚级 20 三连装 + 6 连装 + 30 单装 | 「Ise, Fuso and Kongô classes \| 20 \| 6 \| 30」（同上，标准配置） | S5 |

---

## §5 零式舰战二一型（A6M2 Model 21 / 零式艦上戦闘機二一型）

### §5-A 身份

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 日文原名 | 零式艦上戦闘機二一型 | 「零式艦上戦闘機」 | S22 |
| 英文全称 | Mitsubishi A6M2 Model 21 Carrier Fighter | 「Mitsubishi A6M Reisen (Zero Fighter)」 | S10 |
| 盟军代号 | **Zeke** | 「Allied Code Name: "Zeke"」 | S10 |
| 海军制式名 | 零式一号艦上戦闘機二型 | 「designated as the Mitsubishi Navy Type 0 carrier fighter」 | S15 |
| 设计者 | 堀越二郎 | 「Designer \| Jiro Horikoshi」 | S15 |
| 乘员 | 1 | 「Accommodation: Pilot in enclosed cockpit.」／「Crew: 1」 | S10 / S15 |

### §5-B 几何

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 翼展 | 12.00 m | 「Span \| 12.00 m」 | S10 |
| 机长 | 9.06 m | 「Length \| 9.06 m」 | S10 |
| 机高 | 3.05 m | 「Height \| 3.05 m」 | S10 |
| 翼面积 | 22.4 m²（另源 22.44 m²） | 「Wing area \| 22.4 m2」／「Wing area: 22.44 m2 (241.5 sq ft)」 | S10 / S15 |

### §5-C 重量

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 空重 | 1,680 kg | 「Empty \| 1,680 kg」 | S10 |
| 全重（loaded） | 2,410 kg | 「Loaded \| 2,410 kg」 | S10 |
| 最大重量 | 2,796 kg | 「Maximum \| 2,796 kg」 | S10 |
| 燃油 | 内部 518 L + 330 L 副油箱 | 「Fuel capacity: 518 L (137 US gal; 114 imp gal) internal + 1 × 330 L (87 US gal; 73 imp gal) drop tank」 | S15 |

### §5-D 动力

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 发动机 | 中岛 荣一二型（NK1C Sakae 12），14 缸空冷星型 | 「One Nakajima NK1C Sakae 12 fourteen-cylinder air-cooled radial」 | S10 |
| 起飞功率 | 940 hp | 「rated at 940 hp for take-off」 | S10 |
| 4,200 m 功率 | 950 hp | 「and 950 hp at 4,200 m」 | S10 |
| 螺旋桨 | 三叶金属恒速桨 | 「driving a three-blade metal propeller」／「3-bladed Sumitomo-Hamilton constant-speed propeller」 | S10 / S15 |

### §5-E 性能

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| **最大速度** | 288 kt @ 4,550 m（533 km/h） | 「Maximum speed \| 288 kt at 4,550 m」／「Maximum speed: 533 km/h (331 mph, 288 kn) at 4,550 m」 | S10 / S15 |
| **巡航速度** | 180 kt（333 km/h） | 「Cruising speed \| 180 kt」 | S10 |
| 实用升限 | 10,000 m | 「Service ceiling \| 10,000 m」 | S10 |
| 爬升 6,000 m | 7 分 27 秒 | 「Climb to \| 6,000 m」＋「in \| 7 min 27sec」 | S10 |
| **航程（正常）** | 1,010 海里（1,870 km） | 「Normal range \| 1,010 naut miles」 | S10 |
| **航程（最大/转场）** | 1,675 海里（3,100 km） | 「Maximum range \| 1,675 naut miles」 | S10 |
| 极限速度 | 600 km/h（不得超越） | 「Never exceed speed: 600 km/h (370 mph, 320 kn)」 | S15 |

### §5-F 武备与载弹

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 机枪 | 7.7mm 九七式 × 2（机头上方），**每挺 500 发** | 「2 × 7.7 mm (0.303 in) Type 97 aircraft machine guns in the engine cowling, with 500 rounds per gun.」 | S15 |
| 机炮 | 20mm 九九式一号 Mk.3 × 2（机翼），**每门 60 发** | 「2 × 20 mm (0.787 in) Type 99-1 Mk.3 cannon in the wings, with 60 rounds per gun.」 | S15 |
| 20mm 备弹（另一口径） | 未获取（A6M2 单门备弹数源间未统一） | 同上仅给 60 发/门 | S15 |
| 常规炸弹 | 60 kg × 2 | 「Normal \| two 60 kg bombs」 | S10 |
| 特攻炸弹 | 250 kg × 1 | 「Suicide missions \| one 250 bomb」 | S10 |
| 副油箱 | 330 L × 1 | 「Drop tanks \| one 330 litre (all versions except A6M7 and A6M8)」 | S10 |

### §5-G 服役与产量

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 首飞 | 1939-04-01 | 「First flight \| 1 April 1939」 | S15 |
| **服役起始** | 1940-07-01 | 「Introduction date \| 1 July 1940」 | S15 |
| 总产量（全型） | 10,449（三菱 3,879 + 中岛 6,570） | 「Mitsubishi Jukogyo K.K.」列合计「3,879」／「Nakajima Hikoki K.K.」列合计「6,570」／「Total」列合计「10,449」 | S10 |
| 总产量（维基口径） | 10,939 | 「Number built \| 10,939」 | S15 |

### §5-H 中途岛参战

见 §8 搭载矩阵。

---

## §6 九九式舰爆一一型（D3A1 Model 11 / 九九式艦上爆撃機一一型）

### §6-A 身份

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 日文原名 | 九九式艦上爆撃機一一型 | 「九九式艦上爆撃機」 | S22 |
| 英文全称 | Aichi D3A1 Model 11 Carrier Bomber | 「Aichi D3A」 | S16 |
| 海军制式名 | 九九式艦上爆撃機一一型（Navy Type 99 Carrier Bomber Model 11） | 「designation Navy Type 99 Carrier Bomber Model 11」 | S13 |
| 盟军代号 | **Val** | 「Allied reporting name "Val"」 | S16 |
| 代号时效性 | 1943 年中后期才启用；此前盟军多称「九九式舰爆」 | 「This code name was applied mid-to-late 1943; more often the D3A was referred to as the "Type 99 navy dive bomber" by Allied forces.」 | S16 |
| 乘员 | 2 | 「Accommodation: Crew of two in tandem enclosed cockpits.」 | S11 |

### §6-B 几何

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 翼展 | 14.37 m（14.365） | 「Span \| 14.37 m」／「Wingspan: 14.365 m (47 ft 2 in)」 | S11 / S16 |
| 机长 | 10.20 m（10.195） | 「Length \| 10.20 m」／「Length: 10.195 m (33 ft 5 in)」 | S11 / S16 |
| 机高 | 3.85 m（3.847） | 「Height \| 3.85 m」 | S11 |
| 翼面积 | 34.9 m² | 「Wing area \| 34.9 m2」 | S11 |

### §6-C 重量（D3A1 列）

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 空重 | 2,408 kg | 「Empty \| 2,408 kg」（D3A1 列） | S11 |
| 全重 | 3,650 kg | 「Loaded \| 3,650 kg」（D3A1 列） | S11 |
| 翼载 | 104.6 kg/m² | 「Wing loading \| 104.6 kg/m2」 | S11 |

### §6-D 动力

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 发动机（早期批） | 金星四三型（Kinsei 43），14 缸空冷星型 | 「One Mitsubishi Kinsei 43 fourteen-cylinder air-cooled radial」 | S11 |
| 早期批功率 | 起飞 1,000 hp；2,800 m 时 990 hp | 「rated at 1,000 hp for take-off and 990 hp at 2,800 m」 | S11 |
| 发动机（后期批） | 金星四四型（Kinsei 44） | 「One Mitsubishi Kinsei 44 fourteen-cylinder air-cooled radial」 | S11 |
| 后期批功率 | 起飞 1,070 hp；2,000 m 时 1,080 hp | 「rated at 1,070 hp for take-off and 1,080 hp at 2,000 m」 | S11 |
| 螺旋桨 | 三叶金属恒速桨 | 「driving a three-blade metal propeller」 | S11 |

### §6-E 性能（D3A1 列）

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| **最大速度** | 209 kt @ 3,000 m（240 mph） | 「Maximum speed \| 209 kt at 3,000 m」 | S11 |
| **巡航速度** | 160 kt @ 3,000 m | 「Cruising speed \| 160 kt at 3,000 m」 | S11 |
| 实用升限 | 9,300 m | 「Service ceiling \| 9,300 m」 | S11 |
| 爬升 3,000 m | 6 分 27 秒 | 「Climb to \| 3,000 m」＋「in \| 6 min 27 sec」 | S11 |
| **航程** | 795 海里（1,472 km，见 §10 分歧） | 「Range \| 795 naut miles」 | S11 |

### §6-F 武备与载弹

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 固定机枪 | 7.7mm 九七式 × 2（机头上方） | 「Two forward-firing 7.7 mm Type 97 machine-guns in the engine cowling」 | S11 |
| 后座机枪 | 7.7mm 九二式 × 1（柔性枪架，向后） | 「and one flexible rear-firing 7.7 mm Type 92 machine gun」 | S11 |
| 机身下挂弹 | 250 kg × 1 | 「Bomb-load: one 250 kg bomb under the fuselage」 | S11 |
| 机翼挂弹 | 60 kg × 2 | 「and two 60 kg bombs under the wings」 | S11 |
| 投弹方式 | 250kg 弹由挂臂下摆前送后投放 | 「which swung down and forward on arms before it was released」 | S13 |
| 鱼雷 | **不适用**（舰爆不挂鱼雷） | 载弹栏无鱼雷项 | S11 |

### §6-G 服役与产量

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 首飞 | 1938-01（Aichi 原型） | 「First flight \| January 1938」 | S16 |
| 制式采用 | 1939-12（九九式舰爆） | 「one month prior to its official acceptance as the Navy Type 99 dive bomber」 | S16 |
| **服役起始** | 1940 | 「Introduction date \| 1940」 | S16 |
| 空母适应试验 | 1940 年在赤城、加贺上试飞 | 「The D3A1 commenced carrier qualification trials aboard the aircraft carriers Akagi and Kaga during 1940」 | S16 |
| 总产量 | 1,495 架（D3A1 479 + D3A2 1,016） | 「Number built \| 1,495 (479 D3A1) (1016 D3A2)」 | S16 |
| 一一型产量 | 470 架（1939-12 ~ 1942-08） | 「470 D3A1 Model 11 production aircraft (Dec 1939-Aug 1942)」 | S11 |

### §6-H 中途岛参战

见 §8 搭载矩阵。

---

## §7 九七式舰攻一二型（B5N2 Model 12 / 九七式艦上攻撃機一二型）

### §7-A 身份

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 日文原名 | 九七式艦上攻撃機一二型 | 「九七式艦上攻撃機」 | S22 |
| 英文全称 | Nakajima B5N2 Model 12 Carrier Attack Bomber | 「Nakajima B5N」 | S17 |
| 海军制式名 | 九七式艦上攻撃機（Type 97 Carrier Attack Bomber） | 「leading to the B5N's service introduction as the Type 97 Carrier Attack Bomber in 1938」 | S17 |
| 盟军代号 | **Kate** | 「Allied reporting name "Kate"」 | S17 |
| 乘员 | 3（驾驶 / 侦察-轰炸-领航 / 电信-射手） | 「Crew of three comprising pilot, observer/navigator/bomb-aimer and radio operator/gunner, in enclosed cockpit.」 | S12 |

### §7-B 几何

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 翼展 | 15.52 m（15.518） | 「Span \| 15.52 m \| 15.52 m」（左 B5N1／右 B5N2，两列同值）／「Wingspan: 15.518 m (50 ft 11 in)」 | S12 / S17 |
| 机长 | 10.30 m | 「Length \| 10.30 m \| 10.30 m」（B5N1／B5N2 同值） | S12 |
| 机高 | 3.70 m | 「Height \| 3.70 m \| 3.70 m」（B5N1／B5N2 同值） | S12 |
| 翼面积 | 37.7 m² | 「Wing area \| 37.7 m2 \| 37.7 m2」（B5N1／B5N2 同值） | S12 |

### §7-C 重量（B5N2 列）

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 空重 | 2,279 kg | 「Empty \| 2,106 kg \| 2,279 kg」（左 B5N1／右 B5N2，取右） | S12 |
| 全重 | 3,800 kg | 「Loaded \| 3,700 kg \| 3,800 kg」（左 B5N1／右 B5N2，取右） | S12 |
| 最大全重 | 4,100 kg | 「Maximum \| 4,015 kg \| 4,100 kg」（左 B5N1／右 B5N2，取右） | S12 |
| 翼载 | 100.8 kg/m² | 「Wing loading \| 98.1 kg/m2 \| 100.8 kg/m2」（左 B5N1／右 B5N2，取右） | S12 |

### §7-D 动力

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 发动机 | 中岛 荣一一型（NK1B Sakae 11），14 缸空冷星型 | 「One Nakajima NK1B Sakae 11 fourteen-cylinder air-cooled radial」 | S12 |
| 起飞功率 | 1,000 hp | 「rated at 1,000 hp for take-off」 | S12 |
| 3,000 m 功率 | 970 hp | 「and 970 hp at 3,000 m」 | S12 |
| 螺旋桨 | 三叶恒速金属桨 | 「driving a three-blade constant-speed metal propeller」 | S12 |

### §7-E 性能（B5N2 列）

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| **最大速度** | 204 kt @ 3,600 m（378 km/h） | 「Maximum speed \| 199 kt at 2,000 m \| 204 kt at 3,600 m」（左 B5N1／右 B5N2，取右） | S12 |
| **巡航速度** | 140 kt @ 3,000 m（259 km/h） | 「Cruising speed \| 138 kt at 2,000 m \| 140 kt at 3,000 m」（左 B5N1／右 B5N2，取右） | S12 |
| 实用升限 | 8,260 m | 「Service ceiling \| 7,400 m \| 8,260 m」（左 B5N1／右 B5N2，取右） | S12 |
| 爬升 3,000 m | 7 分 40 秒 | 「Climb to \| 3,000 m」＋「in \| 7 min 50 sec \| 7 min 40 sec」（左 B5N1／右 B5N2，取右） | S12 |
| **航程（正常）** | 528 海里（978 km） | 「Normal range \| 590 naut miles \| 528 naut miles」（左 B5N1／右 B5N2，取右） | S12 |
| **航程（最大）** | 1,075 海里（1,991 km） | 「Maximum range \| 1,220 naut miles \| 1,075 naut miles」（左 B5N1／右 B5N2，取右） | S12 |

### §7-F 武备与载弹

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 后座机枪 | 7.7mm 九二式 × 1（背侧柔性，弹鼓 97 发） | 「1 × 7.7 mm Type 92 machine gun 'Ru' (Lewis) in rear dorsal position, fed by hand loaded drum magazines of 97 rounds.」 | S17 |
| 固定前射机枪 | **一一型部分机装 2 × 7.7mm 九七式**（一二型无） | 「A number of B5N1s were equipped with 2 × 7.7 Type 97 machine guns in the wings.」 | S17 |
| 鱼雷 | 九一式 800 kg × 1 | 「1 × 800 kg (1,760 lb) Type 91 torpedo」 | S17 |
| 炸弹（最大单发） | 800 kg × 1 | 「or 1 × 800 kg (1,760 lb) bomb」 | S17 |
| 炸弹（分挂） | 250 kg × 2 或 60 kg × 6 | 「or 2 × 250 kg (550 lb) bombs or 6 × 60 kg (132 lb) bombs」 | S17 |
| 载弹总重（另一口径） | 800 kg 炸弹 或 800 kg 鱼雷 | 「Bomb-load: 800 kg of bombs or one 800 kg torpedo.」 | S12 |
| 后座机枪备弹 | **未获取**（仅知弹鼓 97 发，鼓数未载） | 同上 | S17 |

### §7-G 服役与产量

| 字段 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 首飞 | 1937-01 | 「First flight \| January 1937」／「The first prototype made its maiden flight in January 1937」 | S17 |
| 九七式舰攻服役 | 1938 | 「service introduction as the Type 97 Carrier Attack Bomber in 1938」 | S17 |
| **B5N2 出现年份** | 1939 | 「In 1939, the improved B5N2 appeared with a more powerful Sakae 11 engine in a smaller cowling.」 | S14 |
| 开战时装备状况 | 一线部队已全部换装 B5N2 | 「When Japan attacked the USA, the B5N2 had wholly replaced the B5N1 with operational units.」 | S14 |
| 总产量 | 1,149 架 | 「Production of all B5Ns reached 1,149.」／「Number built \| 1,149」 | S14 / S17 |

### §7-H 中途岛参战

见 §8 搭载矩阵。

---

## §8 中途岛四空母 舰载机搭载矩阵

### §8-A 各舰搭载数

| 舰 | A6M2 | D3A1 | B5N2 | 其他 | 原文照抄 | 来源 |
|---|---|---|---|---|---|---|
| **赤城** | **18** | 18 | 18 | 第六航空队 A6M2 6 架 | 「AKAGI's air group consists of 18 A6M2 "Zeke", 18 D3A1 "Val" and 18 B5N2 "Kate". Additionally, six A6M2 "Zeke" from the 6th Air Group, destined to Midway's future garrison, are embarked.」 | S6 |
| **赤城**（另一说） | **24** | 18 | 18 | — | 「Akagi's aircraft complement consisted of **24 Zeros**, 18 D3As, and 18 B5Ns.」 | S18 |
| **加贺** | **18** | 18 | **27** | 第六航空队 A6M2 9 架 + 备用 D3A1 2 架 | 「KAGA's air group consists of 18 A6M2 "Zeke", 18 D3A1 "Val" and 27 B5N2 "Kate". Additionally, nine A6M2 "Zeke from the 6th Air Group, destined to Midway's future garrison, and two spare D3A1 "Val" are embarked.」 | S7 |
| **苍龙** | **18** | **16** | 18 | 第六航空队 A6M2 3 架 + 试验型 D4Y1 1~2 架 | 「SORYU's air principal air group consists of eighteen A6M2 "Zeke" fighters, **sixteen D3A1 "Val"** dive-bombers, eighteen B5N2 "Kate" attack planes. Also aboard for the voyage were three A6M2 "Zeke" fighters assigned to the 6th Air Group to base at Midway. One, possibly two, experimental D4Y1 carrier bombers was aboard」 | S8 |
| **飞龙** | **18** | 18 | 18 | 第六航空队 A6M2 3 架 | 「Her aircraft complement consisted of 18 Zeros, 18 D3As, and 18 B5Ns. Also aboard were three A6Ms of the 6th Kōkūtai intended as the aerial garrison for Midway.」 | S21 |

### §8-B 中途岛当日（1942-06-04）出击编成

| 舰 | 第一波（对中途岛） | 原文照抄 | 来源 |
|---|---|---|---|
| 四舰合计 | 108 机（36 B5N2 + 36 D3A1 + 36 A6M2） | 「the air strike led by Lt. (later KIA, Cdr posthumously) Tomonaga Joichi (59) is launched against Midway Island with 36 B5N2 "Kate", 36 D3A1 "Val" and 36 A6M2 "Zeke"」 | S7 |
| 赤城 | 18 D3A1 + 9 A6M2 | 「AKAGA contributes 18 "Val" and 9 "Zeke". 1 "Val", badly damaged is put out of commission and 1 "Zeke" is lost.」 | S6 |
| 加贺 | 18 D3A1 + 9 A6M2（另 1 B5N2 参加搜索、2 机 CAP） | 「KAGA contributes 18 D3A1 "Val" and 9 A6M2 "Zeke". 1 D3A1 "Val" and 2 A6M2 "Zeke" are lost. In addition, KAGA launched one B5N2 to participate in the morning long-range search」 | S7 |
| 苍龙 | 18 D3A1（挂八〇番陆用爆弹）+ 9 A6M2 | 「SORYU contributes eighteen D3A1 "Val" armed with Type # 80 land bombs and nine A6M2 "Zekes."」 | S8 |
| 飞龙 | 18 B5N2（1 架因故障返航）+ 9 A6M2 | 「Hiryū's portion of the 108-plane airstrike was an attack on the facilities on Sand Island with 18 torpedo bombers, one of which aborted with mechanical problems, escorted by nine Zeros.」 | S21 |

### §8-C 当日反击（飞龙单舰）

| 波次 | 编成 | 原文照抄 | 来源 |
|---|---|---|---|
| 第一波反击（10:54） | 18 D3A + 6 A6M，攻约克城 | 「Launched two strikes at 1050 and 1245 against USS YORKTOWN.」 | S9 |
| 返航残存 | 仅 2 架零战 + 3 架轰炸机可飞 | 「Of the four Zeros and five B5Ns that returned to Hiryū, only two Zeros and three bombers were still airworthy.」 | S21 |

---

## §9 未获取字段汇总（**单列，不得以「0」代替**）

| # | 武器 | 字段 | 状态 | 说明 |
|---|---|---|---|---|
| 1 | 20cm/50 No.1 | 膛线长（rifling length） | **未获取** | 「Rifling Length \| N/A」 |
| 2 | 20cm/50 No.1 | 药室容积 | **未获取** | 「Chamber Volume \| N/A」 |
| 3 | 20cm/50 No.1 | 阴线深度 / 阳线宽 / 缠度 | **未获取** | 「Lands \| N/A」「Twist \| N/A」 |
| 4 | 20cm/50 No.1 | Model A1 单装炮座俯仰速度 | **未获取** | 「Model A Single Mounts: N/A」 |
| 5 | 20cm/50 No.1 | Model B 连装炮塔回转/俯仰速度 | **未获取**（来源仅推测 4°/s、12°/s） | 「Model B Twin Turrets: N/A (probably …)」 |
| 6 | 20cm/50 No.1 | Model B 炮塔重量 | **未获取**（来源估 ~172 吨） | 「Model B Twin Turret: N/A, but probably about 172 tons」 |
| 7 | 20cm/50 No.1 | 三式弹 / 照明弹 | **该炮未列此弹种**（≠ 0） | 弹种表仅 3 项 |
| 8 | 20cm/50 No.1 | 赤城/加贺实战射速 | **未获取** | 仅给通用 3–5 发/分 |
| 9 | 20cm/50 No.1 | 最大射高 | **不适用**（非高炮） | 页面无此项 |
| 10 | 12cm/45 十年式 | 四式焼霰弹（三式弹）弹重 | **未获取** | 「Common Type 4 IS 3a: N/A」（3a 为脚注上标） |
| 11 | 12cm/45 十年式 | 减装药 / 轻装药重量 | **未获取** | 「[Weight N/A]」 |
| 12 | 12cm/45 十年式 | 单装 C 型炮座重量 | **未获取** | 「C: N/A」 |
| 13 | 12.7cm/40 八九式 | 赤城/加贺/苍龙/飞龙 每门弹药基数 | **未获取** | 「Shôkaku: 250 rounds」／「Others: N/A」 |
| 14 | 12.7cm/40 八九式 | 通常弹（零式）射程 | **未获取**（该页仅给三式弹射程） | Range 节标题为「Range of IS projectiles」 |
| 15 | 12.7cm/40 八九式 | 苍龙的炮座型号 | **未获取** | NavWeaps 使用舰表无苍龙；舰级来源只给「6 基 12 门」 |
| 16 | 25mm 九六式 | 加贺确切座数（11 基 / 14 基） | **未获取（两说并存）** | 日文维基两说并列 |
| 17 | 25mm 九六式 | 各空母每门实际携弹量 | **未获取** | 仅给通用 2,000 发/门 |
| 18 | A6M2 | 20mm 机炮单门备弹的权威口径 | 部分获取（60 发/门，单源） | 仅维基给出 |
| 19 | D3A1 | 250 kg 弹具体型号（通常弹/陆用弹配比） | **未获取** | 来源只写「250 kg bomb」 |
| 20 | B5N2 | 后座机枪弹鼓携带数 | **未获取** | 仅知单鼓 97 发 |

---

## §10 分歧清单（两边原话都引，不裁决）

### 分歧 ①：赤城 20cm 炮，竣工时 6 门还是 10 门

- **A 说（NavWeaps）**：「Akagi (6) and Kaga (6) (as built): Model A1」+「Akagi (2) and Kaga (2) (as built - all were removed during 1930s modernizations): Model B」 —— 即单装 6 + 连装 2 基（4 门）= **10 门**。
- **B 说（japanese-warship.com，日文专题站，引光人社/潮書房一手文献）**：1927-03 竣工时只有 6 门单装，连装炮是 1928 年末工事才加装。
- **B 说原句**：「**連装砲が搭載されたのは昭和3年/1928年末の工事で**、それまではここには何もありませんでした。」 — S26
- **同站技术数据表（并列两栏，支持 A 方向）**：竣工时栏记「50口径20cm単装砲　6基6門」＋「50口径20cm連装砲2基4門（昭和3年/1928年末の工事で搭載」 — S26
- **日文维基要目表（支持 A 方向）**：竣工栏记「50口径20cm連装砲 2基4門」＋「同単装砲 6門」 — S22

差别在「竣工」与「1928 年末工事」的时点界定：NavWeaps 与日文维基把连装炮算进「as built」，japanese-warship.com 明确否认并给出照片证据（公试照片上无连装炮）。**不裁决**，本站若要精确，建议按「1927-03 竣工：单装 6 门；1928 年末：增连装 2 基 4 门，共 10 门；1930 年代改装：连装撤除、单装 6 门」表述。

### 分歧 ②：赤城中途岛搭载零战 18 架还是 24 架

- **A 说（combinedfleet TROM，Tully）**：「AKAGI's air group consists of **18 A6M2 "Zeke"**, 18 D3A1 "Val" and 18 B5N2 "Kate". Additionally, six A6M2 "Zeke" from the 6th Air Group … are embarked.」 — S6（18 + 6 = 24，但 6 架属第六航空队、非本舰编制）
- **B 说（英文维基，引 Parshall & Tully《Shattered Sword》pp. 90, 149）**：「Akagi's aircraft complement consisted of **24 Zeros**, 18 D3As, and 18 B5Ns.」 — S18

**差别实质**：是否把第六航空队的 6 架零战计入「本舰搭载」。A 说分列、B 说合并。数字 18 与 24 的差正好是 6。**不裁决**，建议本站用「本舰编制 18 + 搭运第六航空队 6」的双栏表述。

### 分歧 ③：苍龙九九舰爆 16 架还是 18 架（同一来源内部冲突）

- **同一页面 A 处**：「SORYU's air principal air group consists of eighteen A6M2 "Zeke" fighters, **sixteen D3A1 "Val"** dive-bombers, eighteen B5N2 "Kate" attack planes.」 — S8
- **同一页面 B 处（当日 04:30 记录）**：「SORYU contributes **eighteen D3A1 "Val"** armed with Type # 80 land bombs and nine A6M2 "Zekes."」 — S8

同为 combinedfleet TROM 的苍龙页，搭载表记 16、出击记录记 18。**不裁决**。

### 分歧 ④：20cm/50 No.1 在 25° 的射程

- **A**：「25 degrees \| 26,250 yards (**24,000 m**)」（引自《Japanese Cruisers of the Pacific War》） — S1
- **B**：「"Naval Weapons of World War Two" says that the range @ 25 degrees was 24,700 yards (**22,600 m**) during World War II. This may be the result of different propellants being used during World War II.」 — S1

NavWeaps 自身并列两说并给出解释（发射药不同）。**不裁决**。

### 分歧 ⑤：D3A1 航程 795 海里 vs 840 法定英里

- **A（combinedfleet，Francillon 口径）**：「Range \| 795 naut miles」= 1,472 km — S11
- **B（aviation-history）**：「Range: **840 miles (1,351 km)**」（D3A1 列，上下文为 statute miles） — S13

795 nmi = 1,472 km；840 statute mi = 1,351 km。两者换算是自洽的，但**基准单位不同**，不是同一物理量。**不裁决**，本站须标注单位。

### 分歧 ⑥：加贺 25mm 座数 11 基 vs 14 基

- **A**：「96式25mm連装機銃」11基 — S23（要目表）
- **B**：同句续「または14基」 — S23（同页并列第二说）
- **日文维基解释**：「25mm連装機銃も同時に増強されたがその位置・数は公式図面が残されていないこともあって不明である（11基とする説と14基とする説あり）。」 — 既有采集引日文维基同句

官方图纸已失，两说并存。**不裁决**。

### 分歧 ⑦：25mm 九六式射程/射高源间不一致

- NavWeaps 明言：「The sources listed below disagree as to the ranges and AA ceiling for this weapon. I have chosen to use those given in "Japanese Cruisers of the Pacific War."」 — S5（本档案采 7,500 m @ 50° / 有效 3,000 m / 最大 5,500 m）
- 该页同时给出另一组：45° 时 7,439 yards（6,800 m）。

**引用时须标注「采 Lacroix & Wells 口径」**。

---

## 来源清单

| 编号 | 来源 | 分级 | 用于 |
|---|---|---|---|
| S1 | NavWeaps — Japan 20 cm/50 (7.9") 3rd Year Type No. 1<br>https://www.navweaps.com/Weapons/WNJAP_79-50_3ns.php | C | §1 全部炮术数据、赤城/加贺炮座型号 |
| S2 | NavWeaps — Japan 20 cm/50 (8") 3rd Year Type No. 2<br>https://www.navweaps.com/Weapons/WNJAP_8-50_3ns.htm | C | §0 纠错①（证明 No.2 未装赤城/加贺）、命名区分 |
| S3 | NavWeaps — Japan 12 cm/45 (4.7") 10th Year Type<br>https://www.navweaps.com/Weapons/WNJAP_47-45_10ns.htm | C | §2 全部、赤城至死未换装的直接证据 |
| S4 | NavWeaps — Japan 12.7 cm/40 (5") Types 88 and 89<br>https://www.navweaps.com/Weapons/WNJAP_5-40_t89.htm | C | §3 全部、加贺/飞龙炮座型号 |
| S5 | NavWeaps — Japan 25 mm/60 (1") Type 96<br>https://www.navweaps.com/Weapons/WNJAP_25mm-60_mg.php | C | §4 全部 |
| S6 | combinedfleet — IJN Akagi TROM（Anthony P. Tully）<br>http://www.combinedfleet.com/Akagi.htm | D | 赤城中途岛搭载 18+18+18+6 |
| S7 | combinedfleet — IJN Kaga TROM<br>http://www.combinedfleet.com/kaga.htm | D | 加贺中途岛搭载 18+18+27+9 |
| S8 | combinedfleet — IJN Soryu TROM<br>http://www.combinedfleet.com/soryu.htm | D | 苍龙搭载 18+16+18+3、当日出击 18 D3A |
| S9 | combinedfleet — IJN Hiryu TROM<br>http://www.combinedfleet.com/hiryu.htm | D | 飞龙当日两波反击时序 |
| S10 | combinedfleet — Mitsubishi A6M Reisen<br>http://www.combinedfleet.com/ijna/a6m.htm | D（数据源 Francillon 1979） | §5 几何/重量/性能/产量 |
| S11 | combinedfleet — Aichi D3A<br>http://www.combinedfleet.com/ijna/d3a.htm | D（同上） | §6 全部 |
| S12 | combinedfleet — Nakajima B5N<br>http://www.combinedfleet.com/ijna/b5n.htm | D（同上） | §7 全部 |
| S13 | aviation-history.com — Aichi D3A<br>https://www.aviation-history.com/aichi/d3a.html | D | §6 航程互校、250kg 挂弹方式 |
| S14 | aviation-history.com — Nakajima B5N<br>https://www.aviation-history.com/nakajima/b5n.html | D | §7 B5N2 1939 出现年份 |
| S15 | Wikipedia (en) — Mitsubishi A6M Zero<br>https://en.wikipedia.org/wiki/Mitsubishi_A6M_Zero | E | §5 服役日期、备弹数、转场航程 |
| S16 | Wikipedia (en) — Aichi D3A<br>https://en.wikipedia.org/wiki/Aichi_D3A | E | §6 服役年份、代号时效性、产量分解 |
| S17 | Wikipedia (en) — Nakajima B5N<br>https://en.wikipedia.org/wiki/Nakajima_B5N | E | §7 载弹组合、弹鼓容量、服役年份 |
| S18 | Wikipedia (en) — Japanese aircraft carrier Akagi<br>https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Akagi | E | §0 纠错②、§10 分歧②（24 架零战） |
| S19 | Wikipedia (en) — Japanese aircraft carrier Kaga<br>https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Kaga | E | 加贺装备栏互校 |
| S20 | Wikipedia (en) — Japanese aircraft carrier Sōryū<br>https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB | E | §0 纠错③（苍龙 12.7cm） |
| S21 | Wikipedia (en) — Japanese aircraft carrier Hiryū<br>https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Hiry%C5%AB | E | 飞龙搭载 18+18+18+3、当日编成 |
| S22 | Wikipedia (ja) — 赤城 (空母)<br>https://ja.wikipedia.org/wiki/赤城_(空母) | E | 赤城要目表、20cm 炮 54 发、12cm 未换装原句 |
| S23 | Wikipedia (ja) — 加賀 (空母)<br>https://ja.wikipedia.org/wiki/加賀_(空母) | E | 加贺竣工/改装后要目表、25mm 两说 |
| S24 | Wikipedia (ja) — 蒼龍 (空母)<br>https://ja.wikipedia.org/wiki/蒼龍_(空母) | E | 苍龙 12.7cm 6 基 12 门、25mm 14 基 |
| S25 | Wikipedia (ja) — 飛龍 (空母)<br>https://ja.wikipedia.org/wiki/飛龍_(空母) | E | 飞龙 25mm 三连 7 + 连装 5 = 31 挺 |
| S26 | japanese-warship.com — 航空母艦「赤城」其ノ二（引光人社/潮書房一手文献）<br>https://japanese-warship.com/carrier/akagi-2/ | D | §10 分歧①「1928 年末工事」原句、连装炮炮座为 B 型大仰角 75° |

**原始抓取文本**：`work/ijn-weapons/raw/*.txt`（每份首行为 SOURCE URL），HTML 原文同目录 `*.html`。

---

## 附：任务书字段覆盖自检（7 型 × 全字段）

| 字段 | 20cm No.1 | 12cm 十年 | 12.7cm 八九 | 25mm 九六 | A6M2 | D3A1 | B5N2 |
|---|---|---|---|---|---|---|---|
| 全称（日/英/简称） | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 盟军代号 | 不适用 | 不适用 | 不适用 | 不适用 | ✅ Zeke | ✅ Val | ✅ Kate |
| 口径 | ✅ 200mm | ✅ 120mm | ✅ 127mm | ✅ 25mm | — | — | — |
| 倍径 | ✅ L/50 | ✅ L/45 | ✅ L/40 | ✅ L/60 | — | — | — |
| 炮身长 | ✅ 10.000m | ✅ 5.604m | ✅ 5.284m | ✅ 2.296m | — | — | — |
| 炮身重 | ✅ 17.6t | ✅ 2.95mt | ✅ 3.1mt | ✅ 115kg | — | — | — |
| 弹重（分弹种） | ✅ 3 种 | ✅ 6 种 | ✅ 4 种 | ✅ 4 种 | — | — | — |
| 装药重量/类型 | ✅ | ✅ | ✅ | ✅ | — | — | — |
| 初速（分弹种） | ✅ 870 | ✅ 825-830 / 700 / 250 | ✅ 700-725 / 250 / 720 | ✅ 900 | — | — | — |
| 最大射程+仰角 | ✅ 28,000@45° | ✅ 16,000@45° | ✅ 14,800@45° | ✅ 7,500@50° | — | — | — |
| 最大射高 | 不适用 | ✅ 10,000@75° | ✅ 9,400@75° | ✅ 5,500@85° | — | — | — |
| 射速（理论/实战） | ✅ 3-5 / 未获取 | ✅ 10-11 / 6-8 | ✅ 14 / 8 | ✅ 220 / 110-120 | — | — | — |
| 俯仰范围 | ✅ -5/+25、-5/+70 | ✅ -10/+75 | ✅ -7/+90 | ✅ -10/+85 | — | — | — |
| 回转速度 | 部分未获取 | ✅ 10°/s | ✅ 6-7°/s | ✅ 18°/s(随动) | — | — | — |
| 炮架型号+重量 | ✅ A1/B | ✅ A2 20t | ✅ A1/A1M1/A1M2 | ✅ 单/双/三连 | — | — | — |
| 弹药基数 | ✅ 120 | ✅ 200-250 | 部分未获取 | ✅ 2,000 | — | — | — |
| 服役起始 | ✅ 1923 | ✅ 1926 | ✅ 1932 | ✅ 1936 | ✅ 1940 | ✅ 1940 | ✅ 1939 |
| 装过哪些舰 | ✅ 赤城/加贺 | ✅ 赤城 | ✅ 加贺/飞龙/苍龙+榛名/雾岛/利根/筑摩 | ✅ 四舰 | — | — | — |
| 翼展/机长/机高 | — | — | — | — | ✅ | ✅ | ✅ |
| 空重/全重 | — | — | — | — | ✅ | ✅ | ✅ |
| 发动机+功率 | — | — | — | — | ✅ | ✅ | ✅ |
| 最大/巡航速度 | — | — | — | — | ✅ | ✅ | ✅ |
| 航程 | — | — | — | — | ✅ | ✅ 有分歧 | ✅ |
| 武备 | — | — | — | — | ✅ 含备弹 | ✅ | ✅ |
| 载弹 | — | — | — | — | ✅ | ✅ | ✅ 含鱼雷 |
| 乘员 | — | — | — | — | ✅ 1 | ✅ 2 | ✅ 3 |
| 中途岛搭载数 | — | — | — | — | ✅ 四舰 | ✅ 四舰 | ✅ 四舰 |
