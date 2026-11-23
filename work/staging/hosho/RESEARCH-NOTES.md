# 凤翔（Hōshō / 鳳翔）调研底稿

> 组名：`hosho` · 采集日期：2026-11-23 · 采集人：jp-cvl
> 工作目录：`work/staging/hosho/`
> 原始页面：`work/staging/hosho/_raw/`（HTML/PDF 与转出的 .txt 都在里面）

## 0. 抓取记录（可复现）

用 Python `urllib.request` + 自定义 UA 抓取，全部成功，**未使用 web_fetch / research**。

| 文件 | URL | 结果 |
|---|---|---|
| `combinedfleet-hosho2.htm` | https://www.combinedfleet.com/Hosho.htm | OK 33,072 B |
| `combinedfleet-hosho.htm` | https://www.combinedfleet.com/ships/hosho | OK 4,915 B |
| `navypedia-hosho.htm` | http://www.navypedia.org/ships/japan/jap_cv_hosho.htm | OK 36,197 B |
| `kasado-hosho.htm` | https://www.kasado.net/AircraftCarriers/Japan/Hosho_1922.html | OK 12,922 B |
| `naval-encyclopedia-hosho.htm` | https://naval-encyclopedia.com/ww2/japan/hosho.php | OK 557,810 B |
| `jw-hosho.htm` | https://japanese-warship.com/carrier/hosho/ | OK 44,102 B |
| `ikaduchi-hosho.htm` | https://nihonkaigun.ikaduchi.com/kuubo/houshou.html | OK 16,624 B |
| `hazegray-cv.htm` | https://web.archive.org/web/20061027174235/http://www.hazegray.org/navhist/carriers/ijn_cv.htm | OK 79,643 B |
| `jm93.htm` | https://www.ibiblio.org/hyperwar/Japan/Monos/pdfs/JM-93_MidwayOperations,May-June42/JM-93.htm | OK 224,139 B |
| `kojinsha6.pdf` | https://www.combinedfleet.com/kojinshavolume6.pdf | OK 235,214 B（73 页，pymupdf 抽文） |
| `navweaps-14cm.htm` | https://www.navweaps.com/Weapons/WNJAP_55-50_3ns.php | OK 36,103 B |
| `nw-8cm-40.htm` | https://www.navweaps.com/Weapons/WNJAP_3-40_3ns.php | OK 19,698 B |
| `nw-25mm.htm` | https://www.navweaps.com/Weapons/WNJAP_25mm-60_mg.php | OK 32,042 B |
| `cf-b4y.htm` | http://www.combinedfleet.com/ijna/b4y.htm | OK 6,278 B |
| `cf-a5m.htm` | http://www.combinedfleet.com/ijna/a5m.htm | OK 12,836 B |
| `jawiki-hosho.htm` | https://ja.wikipedia.org/wiki/鳳翔_(空母) | OK 604,768 B（**tier E，只作线索/交叉核对，不作 fact 来源**） |

失败记录（不硬试）：
- `https://www.combinedfleet.com/hosho.htm`、`hosho_t.htm`、`hosyo.htm` → 均 404。真实 TROM 地址是 `/Hosho.htm`（大写 H），由 combinedfleet `/cv.htm` 航空母舰索引页反查得到。
- `https://www.history.navy.mil/.../car-7.pdf`（NHHC《Evolution of Aircraft Carriers》CAR-7 分册）→ 连续两次 `SSL: UNEXPECTED_EOF_WHILE_READING`，`Invoke-WebRequest` 亦报「基础连接已经关闭」。**放弃**。该 PDF 摘要里那句 "…'s original armament consisted of from 14cm single mount guns and two 8cm single mount high angle guns. At the ... angle guns were replaced by four 25mm twin mount machine guns." 只在搜索结果摘要里见到，**未见原文，本轮不引用**。

---

## 1. 「世界第一艘专门设计建造的航空母舰」——原句支撑

> **combinedfleet-hosho-trom**（1922-12-27 条）：
> "Commissioned in the IJN. **HOSHO is the first purpose-built carrier commissioned in the world, 13 months before Royal Navy's HERMES.** However much of her aviation equipment is still lacking."
> URL: https://www.combinedfleet.com/Hosho.htm

> **kojinsha-vol6-carriers**（Kojinsha No.6 英译，p.2 前后）：
> "Similarly, the **world's first dedicated aircraft carrier HOSHO was commissioned by IJN in December 1922.** Thus in the field of naval aviation Japan was ahead of such major naval powers as the United States and Great Britain…"
> URL: https://www.combinedfleet.com/kojinshavolume6.pdf

两条独立来源（D 级专题站 + C 级光人社英译）都给「世界第一艘 purpose-built / dedicated 航母」，可以立住。
措辞要点：是「**专门设计建造（purpose-built）**」的第一，**不是**「第一艘航母」（改装航母 Argus 更早），也不是「第一艘开工」——见 §7 分歧 1。

---

## 2. 建造与结局

| 项 | 值 | 原句 / URL |
|---|---|---|
| 起工 | 1920-12-16 | "16 December 1920: Tsurumi-Ku, Yokohama. **Laid down by Asano Steel Shipyard** as a 7,590-tons (Standard Displacement) aircraft carrier for the Imperial Japanese Navy." — combinedfleet-hosho-trom |
| 下水 | 1921-11-13 | "13 November 1921: Launched and named HOSHO (Flying Phoenix). **Later that same day, towed to the Yokosuka Naval Yard for completion.**" — combinedfleet-hosho-trom |
| 服役 | 1922-12-27 | "27 December 1922: Commissioned in the IJN." — combinedfleet-hosho-trom |
| 船厂 | 浅野造船所（横浜鶴見）+ 横須賀海軍工廠（艤装） | navypedia: "Builder **Asano, Tsurumi / Yokosuka K K**"；日文维基：建造訓令上は横須賀海軍工廠…浅野造船所に請負の形で建造が委託された |
| 除籍 | 1945-10-05 | "5 October 1945: **Removed from IJN list, but remains in Allied service.**" — combinedfleet-hosho-trom |
| 解体 | 1946-08-31 开始 → 1947-05-01 完成，日立造船桜島 | "31 August 1946: Transferred to Home Ministry. Subsequently removed from service and **broken up till 1 May 1947 at Hitachi Zosen, Sakurajima.**" — combinedfleet-hosho-trom |

navypedia 时间表另有说法：起工 **16.12.1919**、竣工 **16.12.1922**、结局 "surrendered 9.1945, BU 4.1947"。→ 见 §7 分歧 2、3。

---

## 3. 主尺度与排水量

> **navypedia-hosho**：
> "Displacement standard, t **7470**
> Displacement full, t **9630**
> Length, m **155.5 pp 165.0 wl 168.1 oa**
> Breadth, m **18.0 wl 22.7 fd**
> Draught, m **6.17**
> No of shafts **2**
> Machinery **2 Parsons steam turbines, 8 Kampon boilers**
> Power, h. p. **30000**
> Max speed, kts **25**
> Fuel, t **oil 2700, coal 940**
> Endurance, nm(kts) **8000(15)**
> Complement **550**"
> URL: http://www.navypedia.org/ships/japan/jap_cv_hosho.htm

> **kasado-hosho**（「寸法・排水量」表，左列竣工時／右列 1945 年 8 月頃）：
> 全長 **168.1m** / 180.8m；水線長 165.0m；垂線間長 155.5m；**最大幅 18.0m**；**水線幅 14.7m**；吃水 6.17m；
> 基準排水量 **7,470t**；公試排水量 **9,330t**；満載排水量 **10,000t** / 約 10,500t
> 主罐「**ロ号艦本式重油専焼水管罐:4基 / ロ号艦本式炭油混焼水管罐:4基**」
> 主機「パーソンズ式オールギヤードタービンエンジン:2基」、出力 30,000shp、**航続距離 14.0kt / 10,000nm**、速力 25.0kt
> 燃料「重油:2,695t / 石炭:940t」
> URL: https://www.kasado.net/AircraftCarriers/Japan/Hosho_1922.html

> **combinedfleet-hosho-trom**（1922-01-10 条）：
> "HOSHO's **flight deck is 168.25-meters (552.0') long and 22.62-meters (74.3') wide**. The forward end slops down at an angle of **-5°** to help aircraft accelerate during take-off."
> 同条：「She was laid down … as a **7,590-tons (Standard Displacement)** aircraft carrier」→ 7,470 英吨换算成公吨正是 7,590 t 量级，但**这是换算式子，不当事实写**，只在 note 里说明口径。

「标排 7,470」的口径问题：日文维基要目栏写的是「基準排水量 **7,470英トン**」，即**长吨**；本站存储层公制，沿用 `data/ships/soryu.yaml` 的既有做法（苍龙 15,900 英吨直接记 15,900 t + note 说明非公吨）。

---

## 4. 动力：混烧还是重油专烧？

**结论：竣工时是煤油混烧（4 座重油专烧 + 4 座煤油混烧），后来改成全重油专烧；但「何时改」两说。**

竣工时状态（三个来源一致）：
- kasado：「ロ号艦本式**重油専焼**水管罐:4基／ロ号艦本式**炭油混焼**水管罐:4基」
- 日文维基要目：「ロ号艦本式専焼缶4基、同**混焼**缶4基」
- naval-encyclopedia： "Hōshō two Parsons geared turbine fed by eight Type B water-tube Kampon boilers, **four oil-fired and the other coal/fuel mixed-fired**." + "2,700 long tons (2,700 t) of fuel oil were carried **plus 940 long tons (960 t) of coal**."
- navypedia 燃料栏： "**oil 2700, coal 940**"

改装时间两说（不裁决）：
- **navypedia**：「In 1934-1936 … **boilers were converted to oil-firing.**」
- **日文维基**（tier E，只作线索）：「機関関係では、**1926年から1928年にかけて混焼缶を重油専焼缶に換装した**。」
- navypedia 的 "Modernizations" 栏又写 "**1936**: - 2 x 1 - 7.7/80; + 6 x 2 - 13.2/76, full displacement increased to 10797 t, funnels were fixed in vertical position."（未提锅炉）；而 project history 里说 1934-1936 改烧重油。两处 navypedia 内部也不完全对齐。

所以 fact 只写「竣工时混烧」这一点（有 3 条来源），**改烧重油的时间写进 note 并列两说**。

---

## 5. 防护：有没有装甲？飞行甲板有装甲吗？

> **hazegray-ijn-carriers**（World Aircraft Carriers List: Japanese Aircraft Carriers，archive 快照）：
> "Hosho experimental aircraft carrier … **Armor: none**"
> URL: https://web.archive.org/web/20061027174235/http://www.hazegray.org/navhist/carriers/ijn_cv.htm

> **naval-encyclopedia-hosho**：
> "The Hōshō was armed like a light cruiser … and **received no protection or armor**. She already relied on an escort to operate safely."
> URL: https://naval-encyclopedia.com/ww2/japan/hosho.php

> **kasado-hosho** 装甲防御表（竣工時／1945 年 8 月頃两列）：
> 水線部舷側装甲 **N/A／N/A**；格納庫部舷側装甲 **-／-**；前後主隔壁 N/A；水雷隔壁 N/A；
> **飛行甲板装甲 -／-**；**格納庫甲板装甲 -／-**；装甲甲板装甲 N/A／N/A
> URL: https://www.kasado.net/AircraftCarriers/Japan/Hosho_1922.html

→ `protection.scheme: none`。飞行甲板与机库甲板均无装甲（kasado 用「-」表示无；两个英文来源说全舰无装甲）。
**注意**：按 `data/fields.yaml` 的规矩，scheme=none 时**不写**厚度字段，更不填 0。

---

## 6. 武备分期（本舰最容易被写乱的一项）

### 6.1 竣工时（1922-12）

> **combinedfleet-hosho-trom**：「Her armament consists of **four 14-cm/50 3rd Year Type guns, two on each side for surface action** and **a pair of 8-cm/40 3rd Year Type AA guns on disappearing mounts positioned on the flight deck, just forward of the rear elevator.**」

> **naval-encyclopedia-hosho**：「It was limited to six guns: **Four single 14 cm/50 3rd Year Type guns and two single 8 cm/40 3rd Year Type AA guns.**」「Their mounts were **fixed on elevator so they can be lowered** and not obstruct the deck operations. Placed just forward of the rear elevator…」

> **kasado-hosho**（竣工時列）：「三年式 50口径14.0cm単装砲:**4基**」「三年式 40口径7.6cm単装高角砲:**4基**」「留式(ルイス) 87口径7.7mm単装機銃:**2基**」
> ⚠️ kasado 把竣工时 8cm 高炮写成 **4 基**，与 combinedfleet / naval-encyclopedia 的 2 门冲突 → 见 §7 分歧 4。

> **navypedia-hosho** 武备栏：「**4 x 1 - 140/50 3-shiki, 4 x 1 - 76/40 3-shiki, 2 x 1 - 7.7/80**, 26 aircraft」——同样写 4 门 76mm；但同页 Modernizations 又写「**10/1940: - 2 x 1 - 76/40**」（只减 2 门），内部不自洽。

### 6.2 1936-03-31 改装后

> **combinedfleet-hosho-trom**（1936-03-31 条）：「Undocked. HOSHO's forward flight deck's supports are reinforced and increased in number; **the ship's AA guns, aircraft crane and upper aviation fuel tanks are removed**; the funnels are fixed in the horizontal position with their mouths angled slightly downwards; the front sides of the forward hanger and bridge are reinforced and the ship's hull reinforced in the vicinity of her rear hanger to increase her longitudinal strength. **Six Type 93 twin 13.2mm AA MGs are also fitted.**」

→ 本条说 8cm 高炮**在 1936 年就拆了**；navypedia 与日文维基都说 **1940-10** 才拆（"10/1940: - 2 x 1 - 76/40; + 4 x 2 - 25/60 96-shiki"；「1940年10月に…8cm高角砲を2門とも撤去し、代わりに九六式 25mm（60口径）連装機銃6基に更新」）。见 §7 分歧 5。

### 6.3 1940-10：换装 25mm

- navypedia：「**10/1940: - 2 x 1 - 76/40; + 4 x 2 - 25/60 96-shiki**」→ 4 座双联 = 8 挺
- 日文维基：「1940年10月に…九六式 25mm（60口径）連装機銃**6基**に更新され、舷側に張り出し（スポンソン）を片舷2か所ずつ計4か所に配置した」→ 6 座双联 = 12 挺
- **combinedfleet-hosho**（简表）：「4 x 5.5in guns, **8 x 25mm guns**, 12 x 13.2mm guns (1941)」→ 8 挺（= 4 座双联），与 navypedia 一致

→ 取 8 挺（combinedfleet + navypedia 一致），6 座 12 挺的异说进 note。见 §7 分歧 6。

### 6.4 1942 / 1944：14cm 撤去时间两说（**最大的一处分歧**）

- **combinedfleet-hosho-trom**（"Late June 1944" 条）：「Following the disastrous carrier losses at the Battle of the Marianas, **four 140 mm guns are removed** and the HOSHO's flight deck is lengthened as long as possible in an effort to improve her utility by accommodating newer plane needs. It is likely this was done at this time before she left drydock on 24 June 1944」
- **navypedia**：「**late 1942: - 4 x 1 - 140/50; + 4 x 2 - 25/60 96-shiki**」
- **日文维基**（tier E）：「**1942年に**対空火器の強化のため14cm単装砲4基を撤去し、25mm連装機銃2基を追加したため、更にスポンソン2か所を新設して計6箇所となった」

→ 1942（navypedia + 日文维基）vs 1944-06（combinedfleet TROM）。不裁决，两边原句并列。fact 里按 1942 切窗口，note 里点名 combinedfleet 的 1944 说法。

### 6.5 1944 年防空

- **combinedfleet-hosho**（简表）：「**30 x 25mm guns (1944)**」
- navypedia（1944 改装）：「flight deck was lengthened to 180.8 m, new lifts were fitted …, funnels were inclined down; **- 2 x 1 - 76/40**」（1944 又减 76mm —— 与 1940 已拆的说法重复，可能是 navypedia 的年代错位）
- navypedia（6/1945）：「**- 5 x 2 - 25/60**」→ 1945-06 减 10 挺
- 日文维基：1945-07-30 吴镇守府命在凤翔、龙鳯周边陆上配置 25mm 机枪阵地，并从利根、大淀抽调单装机枪与乘员（引「昭和20年7月龍鳳日誌」原文）

### 6.6 7.7mm / 13.2mm

- 竣工时：kasado「留式(ルイス) 87口径7.7mm単装機銃:2基」；navypedia「2 x 1 - 7.7/80」
- 1936 换成：「Six Type 93 twin 13.2mm AA MGs」（combinedfleet）；日文维基 1938-03 要目「13mm連装機銃6基12挺」（一致）

---

## 7. 航空设施

| 项 | 值 | 原句 |
|---|---|---|
| 飞行甲板（竣工） | 168.25 × 22.62 m，前部 -5° 下倾 | combinedfleet：「HOSHO's flight deck is 168.25-meters (552.0') long and 22.62-meters (74.3') wide. The forward end slops down at an angle of -5°…」 |
| 飞行甲板（1944） | 180.8 × 22.7 m | navypedia：「1944: flight deck was lengthened to **180.8 m**」；kasado 1945 列「180.8m × 22.7m」；jw「② 飛行甲板長180.80m」 |
| 机库 | **2 处**（前部战斗机库 + 后部上/下两段攻击机库），互不相通 | combinedfleet：「The carrier is fitted with **two hangers, each served by an aircraft elevator.**」日文维基：「格納庫を艦の前後で完全に分離している…前部は戦闘機用として、後部は攻撃機用…格納庫同士の行き来が全くできない配置でした。高さも違った」 |
| 机库总长 | **92 m** | navypedia：「Fore hangar, upper aft hangar and lower aft hangar (**Length summary: 92m**)」 |
| 机库净高 | **未获取** | 检索 navypedia / kasado / combinedfleet / 光人社 均无逐舱净高数值。kasado 格納庫栏直接 N/A。**不写**。 |
| 升降机 | **2 部** | combinedfleet / navypedia / kasado / jw 一致 |
| 升降机尺寸（竣工） | 前 9.0 × 9.0 m，后 12.5 × 7.0 m | navypedia：「There were **fore (9.0x9.0m) and aft (12.5x7.0m) lifts**」；kasado 竣工時列同值 |
| 升降机尺寸（1939 扩大） | 前 12.8 × 8.5 m，后 13.7 × 7.0 m | combinedfleet（E 1939）：「Her aircraft elevators are enlarged: **the forward elevator to 12.8 by 8.5 meters (42 by 28 ft) and the rear elevator to 13.7 by 7 meters (45 by 23 ft).**」 |
| 升降机尺寸（1944） | 前 8.5 × 12.8 m，后 13.7 × 11.0 m | navypedia：「1944: … **new lifts were fitted (fore: 8.5 x 12.8 m and aft: 13.7 x 11.0 m)**」；kasado 1945 列同值 |
| 拦阻装置（竣工） | **纵索式**（英国式 longitudinal wire），约 100 m 制动索、9 处駒立 | 日文维基：「竣工時の飛行機拘束装置は英国より導入した**縦索式**制動装置であった、これは約100mの長さの制動索を約15cm間隔に張り渡し…高さ約45cmの駒立（ハードル）を**9ヶ所**設置し」；jw：「【鳳翔】もイギリスも、索道索はこの縦索式を使っています」 |
| 拦阻装置（后期） | 横索式；三式一〇型，6 索 | kasado 1945 列「着艦制動装置 **三式一〇型 (6.0t / N/A):6索**」；日文维基：1942 年空技廠开发三式一〇型，一装置管 4 条制动索 |
| 弹射器 | **无（0）** | naval-encyclopedia 两处：「**She had no catapult**, and the narrow deck served as a runway for only a few planes.」「**There was no catapult**, but for arresting landing planes, no satisfying solution either.」；kasado カタパルト 栏 竣工時／1945 均「-」 |
| 防冲网 | 1925-07-02 加装，液压、3 秒立起 | combinedfleet：「Fitted with a net used as a crash barrier aft of the forward elevator. **This barrier, hydraulically operated and being able to be erected in three seconds**…」 |
| 航空燃油 | **未获取**（体积/重量都无） | kasado「航空用ガソリン:N/A」；navypedia「Aircraft fuel stowage: ?」 |

---

## 8. 舰载机编制（含水道）

| 时点 | 编制 | 原句 |
|---|---|---|
| 1923-03/04 | 9 × 三菱一〇式 1MF 战斗机 + 3~6 × 三菱一三式 B1M3 舰攻 | combinedfleet：「HOSHO's air group consists of **nine Mitsubishi Type 10 1MF fighters and three to six Mitsubishi Type 13 B1M3 torpedo bombers.**」 |
| 1923（navypedia 表） | 7 × 1MF / 4 × 2MR / 6 × 1MT | navypedia「1923 7 1MF / 4 2MR / 6 1MT」 |
| 1928 | 一〇式换中岛三式 A1N1 | combinedfleet：「HOSHO's nine Mitsubishi Type 10 1MF fighters are replaced by Nakajima Type 3 A1N1.」 |
| 1931 | 9 × A1N + 三菱八九式 B2M | combinedfleet |
| 1932-02 | 9 × A1N + 3 × B1M + 3 × 一〇式 C1M（2MR）侦察机 | combinedfleet（1932-02-01 条） |
| 1937-07 | 9 × 中岛九五式 A4N1 + 6 × 横须贺九二式 B3Y | combinedfleet（11 July 1937 条） |
| 1941-09-28 | **11 × 三菱九六式 A5M4 + 8 × 横须贺九六式 B4Y1** | combinedfleet：「HOSHO's air group consists of **eleven Mitsubishi Type 96 A5M4 "Claude" fighters and eight Yokosuka Type 96 B4Y1 "Jeans" torpedo bombers.**」 |
| **1942-06 中途岛** | 8 × 九六式舰攻 B4Y1（combinedfleet 明写 "eight Type-96 Yokosuka B4Y"） | 「Admiral Yamamoto orders HOSHO to launch a few of her meager complement of **eight Type-96 Yokosuka B4Y "Jeans" aircraft** to search for Nagumo.」（1942-06-05 条） |
| 1942-05-29（日文维基，E） | 九六舰战 9（补用 2）+ 九六舰攻 6（补用 2）= 19 | 「鳳翔は九六式艦上戦闘機9機（補用2機）、九六式艦上攻撃機6機（補用2機）、計19機を搭載する」 |
| 1942-06（navypedia 表） | 8 × **B5N2** | navypedia Air group 表「6.1942 — — 8 B5N2」 ← **与「凤翔无法运用 B5N」直接矛盾，见 §9** |
| 1942-08 起 | 定数 0（练习舰） | 日文维基要目「1942年8月以降 定数0」；combinedfleet（20 June 1942）「All Type-96 planes are disembarked and offloaded.」 |

**任务书说「1942-06 中途岛载 8 架九六式舰攻 B4Y1」——与 combinedfleet 一致，这条成立。** 但要补一句：8 架只是舰攻数；同时期是否另有战斗机在舰，两说有分歧（见 §9）。

B4Y1 是否真能上凤翔：combinedfleet B4Y 页 "UNITS ALLOCATED — Aircraft carriers: Akagi, Hosho, Kaga, Ryujo and Soryu"；A5M 页 "Carriers: Akagi, Hosho, Kaga, Ryujo and Zuiho"。

---

## 9. 战历要点（combinedfleet TROM 为主轴）

- 1922-12-27 服役（世界第一艘 purpose-built 航母）。
- 1923-02 着舰试验：先由英国合同飞行员（William Jordan），后由日本飞行员（吉良俊一大尉 3 月成功，日本人首次）。
- 1924-06-06~08-20 首次改装：撤岛、撤三脚桅、撤吊车、前部甲板改水平、8cm 高炮前移。→ 平甲板（flush deck）外形确立。
- 1925-07-02 加装液压防冲网。1925-1928 大量试验（拦阻装置、光学助降）。
- 1928-04-01 编入第一航空战队（与赤城）。
- 1932-01/02 第一次上海事变：与加贺同赴长江口；1932-02-05 日本海军首次空战（3 架战斗机护航 2 架攻击机对 9 架中国战斗机）。
- 1935-09-25 第四舰队事件：遭遇台风，飞行甲板与前部结构受损（combinedfleet：「Light carriers HOSHO and RYUJO, several cruisers and destroyers **suffer damage to their flight decks and superstructure**」；naval-encyclopedia：「the aircraft carrier was badly damaged, as **the forward flight deck collapsed**」）。
- 1935-11-22~1936-03-31 大改装（见 §6.2）。
- 1937 日中战争：上海、广东方面作战；1937-09-21 六架战斗机护航轰炸天生、白云机场，宣称击落 6 架，但 5 架因航程耗尽迫降海面。
- 1937-12-01 转预备。
- 1939 升降机扩大。
- 1940-12-23 海军结论：凤翔无法运用 A6M / D3A / B5N 等新机。
- 1941-12-07/08 珍珠港：编入主力部队航空部队，与瑞凤同行动；12-10 夜放飞后与主力失去联络，12-11 于小笠原以东 500 海里被找回。
- 1942-05-29 中途岛出击：位于山本主力部队战列舰纵队之间，护航为川内 + 第 11、19 驱逐队。JM-93 战斗序列明列「Aircraft Carrier Unit — Captain of HOSHO — HOSHO — One destroyer of the 1 Destroyer Sqn」。
- 1942-06-03 派 B4Y 搜索失踪的川内、矶波（1315 于前方 43 海里找到）。
- 1942-06-05 0420 一架 B4Y 发现漂流中的飞龙，拍照；据此田中角荣…（无关）— 驱逐舰谷风奉命前往未果。1300 南云机动部队与山本、近藤会合。
- 1942-06-14 返泊柱岛；06-20 全部九六式机下舰。
- 1942-07-14 转第三舰队附属，成为着舰练习舰。
- 1943-01-15 第五十航空战队（凤翔、龙鳯、鹿屋空、筑城空、夕风）。
- 1944-06 下旬 撤 14cm、甲板延至 180.8 m、升降机扩大（本项两说，见 §6.4）。
- 1945-03-19 吴军港空袭：0532 遭 7 机攻击，后部飞行甲板 3 弹，弹重不超过 50 kg，轻伤，**战死 6 名**，甲板 4 个小洞（最大约 1 m）。→ 这是全战历唯一确认的被弹。
- 1945-04-20 定为三等舰；1945-06-01 定为四级预备舰、附吴港防备队、乘员减半。
- 1945-07-24 吴空袭：据报 0930-1030 中 1 弹，损伤轻微；但 TROM 注 3 明言「unlike 19 March, there is no record of damage to Hosho today」。
- 1945-08-15 终战。日文维基：终战时能航行的航母仅凤翔、龙鳯、葛城，其中几乎无伤的只有凤翔。
- 1945-10-05 除籍，转复员运输：与鹿岛同行至 Wotje、Eniwetok、Jaluit；1945-11-03 载 700（Wotje）+ 311（Jaluit）返浦贺。日文维基：9 个往返、约 4 万人。
- 1945-12-05 入日立造船因岛船厂坞，拆除覆盖舰首的前部飞行甲板以改善舰桥视野。
- 1946-08-31 移交内务省，解体开始；1947-05-01 于日立造船桜島工场解体完毕。

---

## 7'/9'. 分歧清单（不裁决，两边原话并列）

**分歧 1｜「世界第一」的准确边界**
combinedfleet 与光人社都说 "first purpose-built / dedicated carrier commissioned in the world"。日文维基则补一层：「全通式飛行甲板をもつ世界最初の空母はイギリス海軍の貨客船改造空母アーガス、最初から空母として設計された艦はイギリス海軍のハーミーズ（1918年1月）であった」。即：**最早「按航母设计」开工的是 Hermes（1918-01），最早「按航母设计」建成服役的是凤翔（1922-12）**。正文必须写清是「建成服役」的第一，不能含混成「设计第一」。

**分歧 2｜起工年：1919 还是 1920**
- combinedfleet：「16 December **1920**: … Laid down by Asano Steel Shipyard」
- navypedia 表：「Laid down **16.12.1919**」
- kasado：「起工:**1919年12月16日**」
- 日文维基要目写 1920-12-16，注释引原始档案《軍艦鳳鵬翔製造一件》：「大正九年十二月十六日午後三時半 右報告ス」（=1920-12-16），并注明「ただし『艦船要目公表範囲(昭和12年12月1日)』画像2では『大正8-12-16』となっている」（=1919-12-16）。
→ 站内取 1920-12-16（combinedfleet，与原始档案一致），1919-12-16（navypedia / kasado / 要目表）原句并列，不裁决。

**分歧 3｜竣工/服役日：1922-12-27 还是 1922-12-16**
- combinedfleet：「**27 December 1922**: Commissioned in the IJN.」
- 日文维基：竣工 1922-12-27（引《軍艦鳳鵬翔製造一件》画像44）
- navypedia：Comp **16.12.1922**
- kasado：竣工 **1922年12月16日**
- hazegray 无日期。
→ 取 1922-12-27，16 日一说并列。

**分歧 4｜竣工时 8cm 高炮：2 门还是 4 门**
- 2 门：combinedfleet「a pair of 8-cm/40 3rd Year Type AA guns」；naval-encyclopedia「Four single 14 cm/50 … and two single 8 cm/40」；日文维基要目「8cm単装高角砲2門」
- 4 门：kasado「三年式 40口径7.6cm単装高角砲:4基」；navypedia 武备栏「4 x 1 - 76/40 3-shiki」
→ 站内不写 8cm 的门数进数值字段（注册表里也没有 8cm 高炮计数栏），只写进 `armament.mount.summary` 的叙述，并在 note 里并列 2 门/4 门两说。

**分歧 5｜8cm 高炮何时拆除：1936 还是 1940-10**
- 1936：combinedfleet（1936-03-31 条）「the ship's AA guns, aircraft crane and upper aviation fuel tanks are removed」
- 1940-10：navypedia「10/1940: - 2 x 1 - 76/40」；日文维基「1940年10月に…8cm高角砲を2門とも撤去」
→ 不裁决；summary 的 1936 段不写 8cm，1940 段写「8cm 撤去（combinedfleet 记 1936 已撤，两说并列）」。

**分歧 6｜1940-10 换装的 25mm 是 4 座还是 6 座**
- 4 座双联（8 挺）：navypedia「+ 4 x 2 - 25/60 96-shiki」；combinedfleet 简表「8 x 25mm guns (1941)」
- 6 座双联（12 挺）：日文维基「連装機銃6基に更新」
→ 取 8 挺，异说进 note。

**分歧 7｜14cm 主炮撤去时间：1942 还是 1944-06（本舰最大分歧）**
- 1942：navypedia「late 1942: - 4 x 1 - 140/50」；日文维基「1942年に…14cm単装砲4基を撤去」
- 1944-06：combinedfleet「Late June 1944: … four 140 mm guns are removed」
→ 不裁决。fact 窗口按 1942 切（两条来源），note 里引 combinedfleet 原文。

**分歧 8｜1942-06 舰载机总数与构成**
- combinedfleet：8 架九六式舰攻 B4Y1（未提战斗机）
- 日文维基：九六舰战 9（补用 2）+ 九六舰攻 6（补用 2）= 19
- navypedia：8 架 **B5N2（九七式舰攻）**
→ 前两条可并存（舰攻 6 或 8）；navypedia 的 B5N2 明显与「凤翔不能运用 B5N」的记载冲突（combinedfleet 1940-12-23 条），**倾向为 navypedia 笔误，但不裁决**，照原样记录并加注。

**分歧 9｜排水量口径**
- 基准 7,470（navypedia / kasado；日文维基明写「英トン」）
- 常備 9,494 英吨（竣工时，日文维基引『海軍造船技術概要』）/ 9,449（ikaduchi 公試）
- 公試 9,330（kasado）/ 9,449（ikaduchi）
- 満載 9,630（navypedia full）/ 10,000（kasado 竣工時）/ 約 10,500（kasado 1945、jawiki 公試 最終時）
- 1938-03 10,797（日文维基 常備；navypedia 归到 1936 改装「full displacement increased to 10797 t」）
→ 分条记录：standard 7470、full 9630（1922-1936）、full 10797（1936 起）、trial 9330、maximum 10500（1945）。

**分歧 10｜续航**
- navypedia「8000(15)」= 8,000 nm @ 15 kn
- kasado「14.0kt / 10,000nm」；日文维基同
- naval-encyclopedia「8,680 nautical miles at 12 knots」
→ 取 10,000 nm @ 14 kn（kasado，D 级专题表），另两说原句并列。

**分歧 11｜雷达**
- kasado 测距仪/雷达表两列均「-」（含捜索レーダー、ソナー、電子戦装置全为「-」）
- 日文维基（E）最终时「電探1基、逆探1基」「零式水中聴音機1基」
→ kasado 同一张表里连它有记载的声呐也写「-」，说明该栏不是可靠的「无」，而是「未列」。**故本轮不写雷达 fact**，写「未获取」，两说进 note。

**分歧 12｜建造时的船名 / 原始舰种**
- navypedia：「鳳翔 [Hosho] (ex-飛龍 [Hiryu])」「She was laid down as **naval tanker**, originally named Hiryu.」
- hazegray：「ex-Hiryu」「was initially laid down as a **tanker** and redesigned during construction」
- 日文维基：计划时是「特務船（仮称船名第七号特務船）」，预定舰名「**竜飛（龍飛）**」，1919-10 改名凤翔
- japanese-warship：「建造当初は「龍飛」」
→ 「ex-飛龍」与「龍飛」是两个不同的名字，并列，不裁决。同时注意：hazegray 那句"Often considered the first ship built from the keel up as a carrier, but was initially laid down as a tanker" 是**自我保留**的说法，与「laid down as a tanker」并存于同一段。

---

## 10. 未获取清单（明确没查到，不写进 fact）

| 项 | 试过哪 | 结论 |
|---|---|---|
| 机库净高（m） | navypedia / kasado / combinedfleet / 光人社英译 / naval-encyclopedia | 全部无逐舱净高数值 → **未获取**（`aviation.hangar.height` 整条不写，只留注释） |
| 航空汽油容量（体积或重量） | 同上 | kasado「N/A」、navypedia「?」 → **未获取**（两个字段都是 number 型，整条不写，只留注释） |
| 鱼雷发射管 | navypedia 武备栏（只列炮与机枪）/ kasado「水雷兵装 -／-」 | 无来源正面说「无」→ **未获取**（integer 字段，不填 0、不塞「未获取」，整条不写） |
| 装甲重量（t） | 同上 | 无，且全舰无装甲，该字段本身不适用 |
| 水下防护纵深（m） | 同上 | 无记载 → **未获取** |
| 雷达型号 / 有无 | kasado（"-"，不可靠）/ 日文维基（E） | 两说互斥且都不可作 fact 源 → **未获取**（`sensors.radar.installed` 值写「未获取」并解释） |
| 声呐型号 | kasado「-」/ 日文维基「零式水中聴音機1基」（E） | **未获取** |
| 弹射器型号 | — | 无弹射器，不适用（`aviation.catapult.count: 0` 有原文支撑） |
| 建造费 | 日文维基「建造費：空」 | **未获取** |
| 详细涂装色号 | 只找到 1944-45 年「extensively camouflaged」一句 | 色号 **未获取** |
| 螺旋桨直径 / 舵数 | navypedia / kasado / 光人社 | 无 → **未获取** |
| 1942-05-29 的 19 机定数 | 只有日文维基（E） | **不入库**（已写进 `aviation.aircraft.capacity=8` 的 note 作并列口径） |
| 1944 年后全長 179.5 m、吃水 5.3 m | 只有日文维基（E，标一手档案『鳳翔引渡目録』但本轮未获该档案） | **不入库**（`ships/hosho.yaml` 内留注释说明） |
| 改名日期（1919-10）与「大正 7 年度／八六艦隊案」 | 只有日文维基（E） | **不入库**（`identity.name_original` / `identity.building_program` 的 note 里说明） |
| 详细的舰长名单 | combinedfleet TROM 逐年给 20 余任，但只有姓名与就任日 | **本轮不入库**（`service.commander` 每条一人一窗口，20+ 条 fact 属主会话决定要不要拆） |

---

## 11. E 级来源的使用边界（本轮自查重点）

日文维基（`ja.wikipedia.org/wiki/鳳翔_(空母)`）虽然信息最全，但按 SCHEMA §2.1 与 §9.2 **tier E 不能作 fact 来源**。
本轮的处置：

- 它给出的、与其他 D/C 级来源**一致**的信息 → 用来交叉核对，fact 的 `src` 只挂 D/C 级来源。
- 它**独有**的信息（改名日期、八六艦隊案、19 机定数、179.5 m、5.3 m、雷达、声呐、
  电影拍摄、1945-07-30 的防空机枪调配令、舰长名单）→ **一律不进 fact**，
  写在 `note` 里当线索，或列进上面的「未获取」表。
- 它的**统计口径**（例如「終戦時点で航行可能な海軍の空母は鳳翔、龍鳳、葛城の3隻」）→
  正文里若要用，必须能追到 D/C 级来源；追不到就不用。

---

## 交付摘要

| 项 | 数量 |
|---|---|
| 舰级文件 | 1（`classes/hosho.yaml`，90 条 fact） |
| 单舰文件 | 1（`ships/hosho.yaml`，45 条 fact） |
| 切片文件 | 1（`slices/hosho.yaml`，9 片 P0–P8） |
| 正文文件 | 1（`articles/hosho.yaml`，intro 4 段 + history 4 节 38 条事件） |
| 新登记来源 | 10（复用 3：`jm93-midway-operations`、`kojinsha-vol6-carriers`、`navweaps-25mm-96`） |

自检结果：`scripts/validate.py` 的 `check_ship` / `check_article` 在三个 yaml 上 **0 error / 0 warning**；
另按 SCHEMA §10 清单逐项跑自定义自检，同样 **0 fail**（字段注册、单位一致、qual 齐备、
无 confidence D、无 tier E 作 src、正文无「据说/有人认为/据信/或许/大概/应该是」、切片边界单调）。
另加一项跨文件检查：`classes` 与 `ships` 之间**同 field + 同 about + 同时间窗**的重复登记已清零
（此前有 `identity.name_note` 与 `propulsion.boiler.type` 两处会在合并后显示成「两说打架」，
已各归一处；剩下的 6 条同值重复是身份类字段，值完全一致，不会产生假分歧）。

复现命令：
```powershell
python work/staging/hosho/_raw/scripts/_check.py      # 同源 validator
python work/staging/hosho/_raw/scripts/_selfcheck.py  # SCHEMA §10 清单
python work/staging/hosho/_raw/scripts/_cross.py      # 跨文件重复值
```

### 卡住的地方
1. **机库净高、航空汽油容量、鱼雷发射管**：navypedia 只给「格納庫長さ合計 92m」，kasado 该栏直接 N/A，五个来源全部无值。这三个字段分别是 number / number / integer 型，写不了「未获取」字符串，按红线**整条不写**，只在该位置留注释说明查过——这是本轮唯一「留白」的三处，不是漏采。
2. **雷达**：唯一给型号的是 tier E 的日文维基（電探1基、逆探1基），唯一说「无」的是 kasado，但 kasado 同一张表把有记载的声呐也写成「-」，不能作为「无」的证据。故写「未获取」。
3. **NHHC CAR-7 PDF**（`https://www.history.navy.mil/.../car-7.pdf`）：SSL 层失败，Python 放宽 cipher 与 PowerShell 两条路都不通，三次即止，**未引用**。搜索引擎摘要里那句 8cm 高炮换 25mm 双联的话因此没有原文支撑，没用。
4. **combinedfleet TROM 自身有一处日期不可用**：写成 "10 January 1922: Completed."，但同页紧接着又说 "Commissioning is delayed … March~December 1922"，随后 "27 December 1922: Commissioned"，内部矛盾（完成早于服役近一年）。故 `construction` 的「完成」一律用 1922-12-27，不用这个 1 月 10 日。
5. **combinedfleet 的 TROM 有若干条自身前后不一致**（1945-07-24「中 1 弹」vs 注 3「no record of damage」；
   1944-06 撤 14cm 炮 vs navypedia 的 1942）。这类不合并、不挑选，两说都进 note。

### 有争议的记载（详见 §7'/9' 的 12 条 + 补充）
最要紧的三条：
1. **14cm 主炮撤去时间**：navypedia + 日文维基 = 1942；combinedfleet TROM = 1944-06 下旬。两说并列，`ships/hosho.yaml` 里按两段时间窗各写一条 `armament.mount.summary`，互不覆盖。
2. **8cm 高炮何时拆**：combinedfleet = 1936-03-31 改装；navypedia + 日文维基 = 1940-10。
3. **1942-06 舰载机**：combinedfleet = 8 架 B4Y1 舰攻；日文维基 = 9 架九六舰战 + 6 架九六舰攻（各带 2 架补用）= 19 架定数；navypedia = 8 架 **B5N2**（与「凤翔不能运用 B5N」矛盾，疑为笔误，不裁决）。

补充三条（写作过程中新发现）：
4. **改烧重油的时间**：navypedia = 1934-1936；日文维基 = 1926-1928；**kasado 的 1945-08 栏仍写混烧 4 座**（与两说都冲突）。三说并列。
5. **飞行甲板竣工长度**：168.25 / 168.5 m（combinedfleet / 日文维基 / kasado）vs **158.2 m**（japanese-warship、ikaduchi，都放在「竣工時」列）。差 10 m，像是另一种量法（扣掉前部下倾段？），但无来源说明，不裁决。
6. **升降机 1939 vs 1944 的尺寸横纵颠倒**：1939 记「前 12.8 × 8.5」，1944 记「前 8.5 × 12.8」，数值相同只是颠倒，两来源都没说是换了新机还是记法不同。
7. **1944 年 25mm 总数**：combinedfleet 记 30 挺（1944）；kasado 的 1945-08 栏只写「連装機銃 3 基」（= 6 挺），差一个量级；navypedia 记 1945-06 减 10 挺但没给减后总数。三说并列，无 1945-08 的确定值。

### 任务书史实核对结果
| 任务书说法 | 核对 |
|---|---|
| 世界第一艘专门设计建造的航母 | ✅ 成立，两条独立来源原句（combinedfleet、光人社英译）。**但需精确到「建成服役」**：最早按航母设计开工的是 Hermes（1918-01），凤翔 1922-12-27 服役，比 Hermes 早 13 个月建成。 |
| 1922 年服役 | ✅ 1922-12-27。另有 1922-12-16 一说（navypedia、kasado）。 |
| 1942-06 中途岛属主力部队（山本）的 Carrier Group | ✅ 成立。JM-93 战斗序列原文：「**Aircraft Carrier Unit — Captain of HOSHO — HOSHO — One destroyer of the 1 Destroyer Sqn**」，编在山本主力部队内。combinedfleet 补充：位于战列舰纵队之间、大和号左后方，主力部队在南云前方 300 英里之后。 |
| 载 8 架九六式舰攻 B4Y1 | ✅ 与 combinedfleet 一致（"eight Type-96 Yokosuka B4Y 'Jeans'"）。⚠️ 但只是**舰攻**数，同时期战斗机有无/多少有三说，见分歧 8。 |
| 混烧（煤+重油）还是重油专烧「待核实」 | ✅ 已核实：**竣工时混烧**（4 座重油专烧 + 4 座煤油混烧），燃料 2,700 t 重油 + 940 t 石炭。后改全重油专烧——但改烧时间两说，且 kasado 的 1945 栏仍写混烧，故 `propulsion.boiler.type` 不给 valid.to，三说进 note。 |
| 武备在改装中大幅削减 | ⚠️ **措辞需修正**：不是单纯「削减」，是**换装**——14cm×4 与 8cm×2 全撤，25mm 从 0 → 8（1940-10）→ 30（1944）；另 7.7mm 路易斯×2 → 13.2mm×12（1936）。**「改装后只剩高炮与机枪」这句成立**，但高炮与机枪的数量本身各期也都在变。 |
| 1945 年投降后用于运回人员，1946-1947 拆解 | ✅ 成立。复员运输 1945-10-05 起至 1946-08（9 个往返、约 4 万人，japanese-warship 语）；解体 1946-08-31 开始、1947-05-01 完成，日立造船桜島工场。**补充**：1945-12-05 入坞拆掉了覆盖舰首的前部飞行甲板以改善舰桥视野，所以复员期的外形与战时不同——这一点任务书没提。 |
| 1942-06 时是「属主力部队的 Carrier Group」 | ✅ 但需注意舰种归属：本舰当时编为「主力部隊航空部隊」下的**航空母艦隊（Aircraft Carrier Unit）**，指挥官即凤翔舰长（上谷薰 Kaorou Umetani，1941-09-05 上任）。JM-93 与 combinedfleet 都支持「凤翔自身就是一个单舰航母单位」。 |

