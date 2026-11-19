# 蒼龍 / 飛龍 技术数据采集

> 采集对象：日本海军航空母舰「蒼龍」Sōryū、「飛龍」Hiryū
> 采集日期：2026-11-19
> 采集规则：每条数值附原文照抄（英/日文原句）+ 来源 URL；查不到写【未获取】；不推算、不按同级舰类推；分歧单列不裁决；任务书前提有误直接反驳。
> 全部来源直连抓取（无代理）。抓取原文归档于 `work/raw/txt/`。

---

## §A 先纠错：任务书前提有四条不成立

### A-1【重大错误】「飞龙：右舷舰岛但位置更靠后」 → 错。飞龙的舰岛在**左舷**，位于舰体中央。

原文（日文维基·飛龍）：

> 「特徴としては改装後の赤城同様、**左舷中央に島型艦橋**を配置していることである。」

来源：https://ja.wikipedia.org/wiki/飛龍_(空母)

原文（英文维基·Hiryū）：

> "Hiryū was one of only two carriers ever built whose island was on the **port side** of the ship (Akagi was the other). It was also positioned **further to the rear** and encroached on the width of the flight deck, unlike Sōryū."

来源：https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Hiry%C5%AB

原文（海軍造船技術者向け解説書 Kojinsha Vol.6，第 91 页图注）：

> "The main difference in comparison with SORYU was the **port amidships location of the island**, proposed by Koku Hombu to simplify the supervision of flight operations."

来源：https://www.combinedfleet.com/kojinshavolume6.pdf

结论：飞龙是**左舷中央**舰岛；「更靠后」成立（中央 vs 苍龙的前部），「右舷」不成立。这是两舰最容易搞错的识别特征。

### A-2【无法证实】「飞龙的舰岛与赤城的设计曾经互换过」 → 未获取到任何支持此说的原文；现有证据指向「同一份通達分别适用」，不是「互换」。

我按 `赤城 飛龍 艦橋 交換`、`設計 入れ替え`、`swapped design` 等多组关键词检索（Bing/Exa），**没有任何一条来源支持「互换」**。与之相反，能查到的三条原文都描述为「同一指令 + 时间差」：

原文（日文维基·飛龍，引 1935 年海軍航空本部長→艦政本部長《航空母艦艤装に関する件照会》）：

> 「『赤城の大改装および、**飛龍以後の新造艦からは**できるかぎり艦橋と煙突はそれぞれ両舷に分けて設置し、煙突は艦後方、艦橋は艦の中央付近に設置する』に従っている。」

原文（日文维基·飛龍，说明飞龙为何没改成右舷）：

> 「しかし左舷艦橋は、プロペラの回転方向の関係から左へ流れやすいレシプロ機の着艦時に障害となることが赤城の運用で判明し、のちの日本空母はすべて右舷艦橋とされ、建造中の翔鶴型も左舷中央から右舷前方に変更された。しかし**すでに竣工間近だった飛龍だけが左舷艦橋のままとされた**のである。」

原文（Kojinsha Vol.6，说明赤城是先做木模型验证、再与飞龙同步采用）：

> "Accordingly, AKAGI was fitted with a portside island mock-up prior to her refit. The new configuration was thoroughly tested during her subsequent voyage from Yokosuka to Sasebo and as far as take-off and landing procedures were concerned, no problems with turbulence were detected. **Immediately thereafter portside amidships location was incorporated into AKAGI and HIRYU**, resulting in distinctive-looking warships."

判定：这是「同一设计指令下的并行采用，赤城先试用、飞龙因已接近完工而来不及改」，不是「两舰设计互换」。**「互换」一说未获取任何原始依据，本表不采信，也不列为分歧（因为无对方原文可引）**。

### A-3「苍龙与飞龙名义同级、实际差异很大」 → 成立，但措辞要更准：**两舰是同一造舰计划下的「同型计划舰」，实际按两个不同的基本计划编号（G9 / G10）建造，属两型。**

原文（日文维基·飛龍）：

> 「昭和9年度海軍軍備補充計画（通称・②計画）で建造された中型空母である。**当初は蒼龍の同型艦として計画・建造されていた**。だが軍縮条約破棄により設計の自由度が増したため、飛行甲板幅を1m広げ艦幅を若干太くし、さらに第四艦隊事件による船体構造溶接化の破棄、凌波性向上のため艦首1m・艦尾40cm乾舷を高めるなど**蒼龍とは違う図面で建造された空母**となった。**基本計画番号G10**。」

原文（日文维基·蒼龍）：

> 「基本計画番号は**G9**となった。」

原文（英文维基·Sōryū）：

> "A sister ship, Hiryū, was intended to follow Sōryū, but Hiryū's design was heavily modified and she is often considered to be a separate class."

原文（英文维基·Hiryū）：

> "Generally regarded as the only ship of her class, she was built to a **modified Sōryū design**."

判定：任务书「名义同级」可接受；「请给出两套数据」正确且必要。

### A-4「苍龙常被称为『飞龙的前型』」 → 不准确。原文用语是「準同型艦 / near sister / 蒼龍型の二番艦」，方向是**飞龙是苍龙的后续改进型**，不是「苍龙是飞龙的前型」（语序反了）。

原文（日文维基·蒼龍）：

> 「同年11月15日、**準同型艦飛龍**の編入にともない、二航戦は空母2隻（蒼龍、飛龍）および第11駆逐隊（初雪、白雪、吹雪）という戦力になる。」

原文（Kojinsha Vol.6，第 88 页图注）：

> "While usually listed as the '**near sister**' of the SORYU, HIRYU's appearance and hull layout were rather different."

---

## §0 身份

### §0.1 蒼龍 Sōryū

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 原名（日文） | 蒼龍（そうりゅう / さうりう） | 「蒼龍（そうりゅう / さうりう）は、大日本帝国海軍の航空母艦」 | https://ja.wikipedia.org/wiki/蒼龍_(空母) |
| 中文名 | 苍龙 | —（中文名为译名，无原文） | — |
| 英文名 | Sōryū | "Sōryū (Japanese: 蒼龍; meaning "Blue (or Green) Dragon")" | https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB |
| 舰种 | 航空母艦（正规空母） | 「大日本帝国が海軍休日時代末期に建造した**正規空母**である」 | https://ja.wikipedia.org/wiki/蒼龍_(空母) |
| 国家 | 大日本帝国 | "Japan"（信息框 `Country`） | https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB |
| 海军 | 大日本帝国海軍 | "operated by the Imperial Japanese Navy (IJN)" | 同上 |
| 命名来源 | 「蒼龍」＝深蓝色/青色之龙；帝国海军史上第 2 艘用此名（前有御召艦蒼龍） | 「蒼龍の名前は、帝国海軍の艦船としては**御召艦蒼龍に続いて2隻目**」 / "'Soryu' means '**Deep Blue Dragon**'" | https://ja.wikipedia.org/wiki/蒼龍_(空母) ; https://www.combinedfleet.com/kojinshavolume6.pdf |
| 命名规则依据 | 空母用「特殊名」，须天皇治定 | 「1933年（昭和8年）12月19日、航空母艦の命名に際しては戦艦等と同様に天皇の治定を仰ぎ、命名標準を「**特殊名**」とすることが定められる。」 | https://ja.wikipedia.org/wiki/艦名 |
| 建造计划 | 昭和9年度（1934年）②計画 | 「計画 昭和9年度（1934年）、②計画」 | https://ja.wikipedia.org/wiki/蒼龍_(空母) |
| 建造费 | 予算 40,200,000 円 | 「建造費 予算 40,200,000円」 | 同上 |
| 时代 | 1930 年代（昭和 9–17 年） | — | — |
| 母港 | 横須賀 | 「母港 横須賀」 | 同上 |

> **命名来源纠错**：任务书写「苍龙=天龙？」。查到的原文只说「蒼龍」意为深蓝之龙，且为御召艦蒼龍之后第 2 艘同名舰，**没有任何来源把「蒼龍」同「天龍」联系起来**。「天龍」是另一艘轻巡洋舰（1919 年）的舰名。此处按原文写，不采「天龙」说。

### §0.2 飛龍 Hiryū

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 原名（日文） | 飛龍（ひりゅう / ひりう） | 「飛龍（ひりゅう/ひりう）は、大日本帝国海軍の航空母艦」 | https://ja.wikipedia.org/wiki/飛龍_(空母) |
| 中文名 | 飞龙 | —（译名） | — |
| 英文名 | Hiryū | "Hiryū (Japanese: 飛龍; meaning "Flying Dragon")" | https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Hiry%C5%AB |
| 舰种 | 航空母艦（中型正规空母） | 「昭和9年度海軍軍備補充計画（通称・②計画）で建造された**中型空母**である」 | https://ja.wikipedia.org/wiki/飛龍_(空母) |
| 国家 | 大日本帝国 | `運用者：{{navy|Empire of Japan}}` | 同上 |
| 海军 | 大日本帝国海軍 | 同上 | 同上 |
| 命名来源 | 「飛龍」＝高飞之龙；1935-11-22 正式命名 | 「1935年（昭和10年）11月22日、横須賀海軍工廠で建造予定の空母に**飛龍の艦名が正式に与えられた**」 / "'Hiryu' means '**High-Flying Dragon**'" | https://ja.wikipedia.org/wiki/飛龍_(空母) ; https://www.combinedfleet.com/kojinshavolume6.pdf |
| 建造计划 | 昭和9年度（1934年）②計画；基本计划番号 **G10**；名义为「蒼龍型二番艦」 | 「②計画」 / 「基本計画番号G10」 / 「当初は蒼龍の同型艦として計画・建造されていた」 | https://ja.wikipedia.org/wiki/飛龍_(空母) |
| 时代 | 1930 年代（昭和 11–17 年） | — | — |

---

## §1 建造

### §1.1 蒼龍

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 建造厂 | 呉海軍工廠（吳海军工厂） | 「建造所**呉海軍工廠**」 / "Builder **Kure Naval Arsenal**" | https://ja.wikipedia.org/wiki/蒼龍_(空母) ; https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB |
| 开工 | 1934-11-20 | 「1934年11月20日、軍艦「蒼龍」は**呉海軍工廠で起工**された」 | https://ja.wikipedia.org/wiki/蒼龍_(空母) |
| 下水 | 1935-12-23（书面上记 1935-01-23） | 「書類上では1935年（昭和10年）1月23日に進水したことになっているが、**実際には12月23日に進水した**」 | 同上 |
| 服役（竣工/引渡） | 1937-12-29 | 「1937年（昭和12年）…12月29日、**引渡し**」 / "Commissioned 29 December 1937" | 同上 ; https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB |
| 结局日期（**日本时间 JST**） | 1942-06-05 16:12–16:15 自沉 | 「日本時間6月5日午後4時13-15分（**現地時間6月4日19時13分**）、蒼龍は日没と共に沈没した」 | https://ja.wikipedia.org/wiki/蒼龍_(空母) |
| 结局日期（**中途岛当地时**） | 1942-06-04 19:12 被磯風雷击处置，3 分钟后沉 | "Sunk: 1912 (1612 JST) Destroyer ISOKAZE fired three torpedoes at SORYU… and the carrier began to sink by the stern and three minutes later upended." | https://www.combinedfleet.com/soryu.htm |
| 结局型式 | **自沉**（护卫驱逐舰磯風发射 3 条鱼雷处置）；亦有「未被雷击、自行沉没」异说 | 「随伴駆逐艦（磯風）の魚雷により処分されたという異説もあり、南雲の戦闘詳報は事実を隠して「沈没」としか書いていないという意見もある」 | https://ja.wikipedia.org/wiki/蒼龍_(空母) |
| 除籍 | 1942-08-10 | 「除籍 1942年8月10日」 / "Stricken 10 August 1942" | 同上 |
| 沉没位置 | 30°38′N 179°13′W（Tully）；日文维基另给 30°43′N 178°38′W 与战斗详报 30°42′5″N 178°37′5″W | "Position 30 - 38' N, 179 - 13 W'" | https://www.combinedfleet.com/soryu.htm ; https://ja.wikipedia.org/wiki/蒼龍_(空母) |

### §1.2 飛龍

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 建造厂 | 横須賀海軍工廠 | 「建造所**横須賀海軍工廠**」 / "Builder **Yokosuka Naval Arsenal**" | https://ja.wikipedia.org/wiki/飛龍_(空母) ; https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Hiry%C5%AB |
| 开工 | 1936-07-08 | 「1936年（昭和11年）**7月8日に起工**」 | https://ja.wikipedia.org/wiki/飛龍_(空母) |
| 下水 | 1937-11-16 | 「1937年（昭和12年）**11月16日に進水**」 | 同上 |
| 服役（竣工） | 1939-07-05 | 「7月5日、飛龍は**伏見宮博恭王臨席の元で竣工**」 | 同上 |
| 结局日期（**中途岛当地时**） | 6/4 17:03 被 4 发 1000 磅炸弹命中；6/5 05:10 由巻雲雷击处置；6/5 09:12 翻覆沉没 | "Sunk: At **1703** while preparing to launch strike against enemy carrier, attacked by thirteen enemy dive bombers. Four direct bomb hits received…" / "at **0510** scuttled by MAKIGUMO with one torpedo in the starboard side opposite the bridge" / "before she arrives, the carrier at **0912** upended and sank by the bow" | https://www.combinedfleet.com/hiryu.htm |
| 结局日期（**日本时间 JST**） | 沉没时刻有分歧，见 §D-3 | 「日本時間6月6日午前6時6-15分、飛龍は左舷に傾きつつ艦首から沈んでいった」 | https://ja.wikipedia.org/wiki/飛龍_(空母) |
| 结局型式 | **自沉**（巻雲发射鱼雷；另一条未命中） | "One torpedo missed and the other struck near the bow without the typical plume of water, although the detonation was quite visible." | https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Hiry%C5%AB |
| 除籍 | 1942-09-25 | 「除籍 1942年9月25日」 | https://ja.wikipedia.org/wiki/飛龍_(空母) |
| 沉没位置 | 31°38′N 178°51′W（Tully 自沉点）；另有 31°27′N 179°23′W | "(Scuttling position 31-38'N, 178-51'W)" | https://www.combinedfleet.com/hiryu.htm |

---

## §2 主尺度（**两舰不同，分别给**）

### §2.1 蒼龍

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 全长（o/a） | 227.500 m | 「全長 227.500m」 | https://ja.wikipedia.org/wiki/蒼龍_(空母) |
| 水线长（wl） | 222.00 m（或 222.420 m） | 「水線長 222.00m または222.420m」 / "Length, m 210.0 pp **222.0 wl 227.5 oa**" | https://ja.wikipedia.org/wiki/蒼龍_(空母) ; https://www.navypedia.org/ships/japan/jap_cv_soryu.htm |
| 垂线间长（pp） | 206.52 m | 「垂線間長 206.52m」 | https://ja.wikipedia.org/wiki/蒼龍_(空母) |
| 水线宽 | 21.30 m（或 21.318 m） | 「水線幅 21.30m または21.318m」 | 同上 |
| 最大宽 | 21.30 m（舰体）；**飞行甲板宽 26.0 m** | "Breadth, m 21.3 wl **26.0 fd**" | https://www.navypedia.org/ships/japan/jap_cv_soryu.htm |
| 平均吃水 | 7.475 m；竣工时公试 7.62 m | 「吃水 7.475m / 竣工時公試 7.62m」 / "Draught, m 7.62" | https://ja.wikipedia.org/wiki/蒼龍_(空母) ; https://www.navypedia.org/ships/japan/jap_cv_soryu.htm |
| 最大吃水（满载） | 8.03 m | 「竣工時**満載 8.03m**」 | https://ja.wikipedia.org/wiki/蒼龍_(空母) |
| 型深 | 15.70 m（至飞行甲板 20.400 m） | 「深さ 15.70m / 20.400m(飛行甲板まで)」 | 同上 |

### §2.2 飛龍

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 全长（o/a） | 227.35 m | 「全長 227.35m」 / "Length 227.4 m (746 ft 1 in) (o/a)" | https://ja.wikipedia.org/wiki/飛龍_(空母) ; https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Hiry%C5%AB |
| 水线长（wl） | 222.00 m（另本 222.930 m） | 「水線長 222.00m」+ 注「#軍艦基本計画資料Sheet8には、全長227m、水線長**222.930m**、垂線間長206.52m、水線幅22.324mの数値もある」 | https://ja.wikipedia.org/wiki/飛龍_(空母) |
| 垂线间长（pp） | 209.52 m（另本 206.52 m） | 「垂線間長 209.52m」 | 同上 |
| 水线宽 | 22.00 m（另本 22.32 / 22.324 m） | 「水線幅 22.00m」+ 注「#海軍造船技術概要p.295でも**22.32m**としているが…次頁では水線幅22.00mとされている」 | 同上 |
| 最大宽 | 22.3 m（舰体）；**飞行甲板宽 27.0 m** | "Breadth, m 22.3 wl **27.0 fd**" | https://www.navypedia.org/ships/japan/jap_cv_hiryu.htm |
| 平均吃水 | 公试平均 7.84 m | 「吃水 公試平均 **7.84m**」 | https://ja.wikipedia.org/wiki/飛龍_(空母) |
| 最大吃水（满载） | 满载平均 8.21 m | 「満載平均 **8.21m**」 | 同上 |
| 型深 | 15.70 m（至飞行甲板 20.50 m） | 「深さ 15.70m / 飛行甲板まで 20.50m」 | 同上 |

> **两舰尺寸差**：全长差 0.15 m（苍龙更长）、水线宽差 0.70 m（飞龙更宽）、垂线间长差 3.00 m、满载吃水差 0.18 m。

---

## §3 排水量（日本口径词照抄）

### §3.1 蒼龍

| 口径 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 基準排水量 | 15,900 英吨 | 「基準排水量 15,900英トン」 / 「基準排水量15,900t」 | https://ja.wikipedia.org/wiki/蒼龍_(空母) ; https://japanese-warship.com/carrier/soryu/ |
| 公試排水量 | 18,448 t（另一说竣工时 18,800 t；公试实测 18,871 t） | 「公試排水量 18,448トン / 竣工時 18,800トン」+「11月11日の公試では排水量**18871トン**、機関出力15万2483馬力で34.898ノットを発揮した」 | https://ja.wikipedia.org/wiki/蒼龍_(空母) |
| 満載排水量 | 19,500 t（竣工时 20,295 t） | 「満載排水量 19,500トン / 竣工時 20,295トン」 | 同上 |
| （对照）英文维基口径 | 16,200 t normal | "She displaced 16,200 tonnes… at standard load and 19,100 tonnes… at normal load" | https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB |

### §3.2 飛龍

| 口径 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 基準排水量 | 17,300 英吨 | 「基準排水量 17,300英トン」 | https://ja.wikipedia.org/wiki/飛龍_(空母) |
| 公試排水量 | 計画 20,250 t（或 20,165 t） | 「公試排水量 計画 20,250トン または 20,165トン」 | 同上 |
| 満載排水量 | 計画 21,887.30 t；1937-07 实测 21,882.6 t | 「満載排水量 計画 21,887.30トン / 1937年7月 21,882.6トン」 | 同上 |
| （对照）Navypedia | full 21,900 t | "Displacement full, t 21900" | https://www.navypedia.org/ships/japan/jap_cv_hiryu.htm |

---

## §4 动力

### §4.1 蒼龍

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 动力型式 | 4 组舰本式齿轮传动蒸汽轮机（高/中/低压），8 座舰本式锅炉，4 轴 | 「艦本式タービン(高中低圧)4基」 / 「推進 4軸 x 340rpm、直径3.800m」 | https://ja.wikipedia.org/wiki/蒼龍_(空母) |
| 轴数 | 4 | 「4軸 x 340rpm」 | 同上 |
| 锅炉数/型号 | ロ号艦本式ボイラー（附空气预热器）8 座 | 「ボイラー ロ号艦本式ボイラー(空気過熱器附)**8基**」 | 同上 |
| 主机型号 | 艦本式タービン 4 基（与最上级巡洋舰同型） | "The turbines and boilers were the same as those used in the Mogami-class cruisers." | https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB |
| 设计功率 | 152,000 hp | 「出力 計画 **152,000hp**」 | https://ja.wikipedia.org/wiki/蒼龍_(空母) |
| 试航功率 | 公试全力 152,483 hp；过负荷 160,326 hp | 「公試全力 152,483hp」/ 表「過負荷全力 18,621t 35.217kt **160,326**SHP」 | 同上 |
| 设计航速 | 34.5 kt | 「速力 計画 **34.5ノット**」 | 同上 |
| 试航航速 | 公试全力 34.898 kt（排水量 18,871 t） | 「公試全力 34.898ノット」 | 同上 |
| 续航力 | 7,680 海里 / 18 kt | 「航続距離 **7,680カイリ / 18ノット**」 | 同上 |
| 燃油 | 3,400 t（重油） | 「燃料 3,400トン」 | 同上 |
| 航空汽油 | 360 t | 「搭載能力 ガソリン360トン」 | 同上 |

### §4.2 飛龍

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 动力型式 | 舰本式轮机 4 基（高/中/低压），舰本式锅炉 8 座，4 轴 | 「艦本式タービン(高中低圧)4基」 / 「推進 4軸 x 340rpm」 | https://ja.wikipedia.org/wiki/飛龍_(空母) |
| 轴数 | 4 | 同上 | 同上 |
| 锅炉数/型号 | 舰本式缶（附空气余热器）8 座 | 「ボイラー 艦本式缶(空気余熱器付)**8基**」 | 同上 |
| 主机型号 | 艦本式タービン（与最上级同型） | "The turbines and boilers were the same as those used in the Mogami-class cruisers." | https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Hiry%C5%AB |
| 设计功率 | 152,000 shp（計画）；终末全力 153,000 shp | 「出力 計画 **152,000shp** / 終末全力 153,000shp」 | https://ja.wikipedia.org/wiki/飛龍_(空母) |
| 试航功率 | 公试全力 152,733 shp（326 rpm） | 「公試全力 **152,733shp**」 / "During the trials the carrier made 34.28kts with **152,733shp** at 326rpm and a displacement of 20,346ts" | https://ja.wikipedia.org/wiki/飛龍_(空母) ; https://www.combinedfleet.com/kojinshavolume6.pdf |
| 设计航速 | 34.3 kt | 「速力 計画 **34.3ノット**」 | https://ja.wikipedia.org/wiki/飛龍_(空母) |
| 试航航速 | 公试全力 34.28 kt（20,346 t）；终末全力 34.59 kt（20,165 t） | 「公試全力 34.28ノット(20,346トンで) / 終末全力 34.59ノット(20,165トンで)」 | 同上 |
| 续航力 | 计划 7,670 海里 / 18 kt；公试成绩 10,250 海里 / 18.142 kt | 「計画 **7,670カイリ / 18ノット**」+「公試成績 10,250カイリ / 18.142ノット」 | 同上 |
| 燃油 | 重油 3,750 t | 「燃料 重油：**3,750トン**」 | 同上 |
| 航空汽油 / 鱼雷 | 汽油 360 t、鱼雷 27 条 | 「搭載能力 ガソリン360トン、**魚雷27本**」 | 同上 |

---

## §5 防护

### §5.1 蒼龍

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 装甲体系 | 极轻防御，仅机舱与弹药库设防；舷侧 41 mm Ducol 钢 + 内侧防破片纵壁 | "To save weight Sōryū was minimally armored; her waterline belt of 41 millimeters (1.6 in) of Ducol steel only protected the machinery spaces and the magazines… backed by an internal anti-splinter bulkhead." | https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB |
| 舷侧 | 40 mm（机舱段）；日文维基记 140〜35 mm NVNC | "belt: 40" / 「舷側：**140〜35mmNVNC鋼**」 | https://www.navypedia.org/ships/japan/jap_cv_soryu.htm ; https://ja.wikipedia.org/wiki/蒼龍_(空母) |
| 甲板 | 机舱上方 25 mm；弹药库与航空汽油库上方 55 mm | "Her deck was only 25 mm thick over the machinery spaces and 55 millimeters… over the magazines and aviation gasoline storage tanks." | https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB |
| 弹药库 | 垂直 140 mm、水平 55 mm | "Magazines had **140mm vertical and 55mm horizontal** protection." | https://www.navypedia.org/ships/japan/jap_cv_soryu.htm |
| 水下防护 | 45 mm 纵向防雷纵壁 | "There was a **45mm longitudinal anti-torpedo bulkhead**." / "There was 45mm longitudinal anti-torpedo bulkhead."（飞龙页同句） | https://www.navypedia.org/ships/japan/jap_cv_soryu.htm |
| 装甲总重 | 【未获取】 | — | — |

### §5.2 飛龍

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 装甲体系 | 机舱段舷侧加强，弹药库段加厚；飞行甲板**不考虑防御** | 「機関室と舵取機室は駆逐艦の5インチ砲にガソリンタンクと弾薬庫は巡洋艦の8インチ砲に耐える装甲を施しているが、**飛行甲板の防御は考慮されていない**」 | https://ja.wikipedia.org/wiki/飛龍_(空母) |
| 舷侧 | 机舱段 90 mm，弹药库与航空汽油库段 150 mm（英文维基）；另本：机舱段 48 mm、弹药库段 150 mm（Navypedia）；日文维基：機関部舷側 25 mm CNC | "her waterline belt with a maximum thickness of **150 millimeters**… over the magazines that reduced to **90 millimeters** over the machinery spaces and the avgas storage tanks" / "belt: 48 (150 abreast magazines)" / 「機関部舷側 **25mmCNC鋼板**」 | https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Hiry%C5%AB ; https://www.navypedia.org/ships/japan/jap_cv_hiryu.htm ; https://ja.wikipedia.org/wiki/飛龍_(空母) |
| 甲板 | 机舱上方 25 mm，弹药库/汽油库上方 55 mm；日文维基另记 140〜50 mm NVNC | "The ship's deck was 25 millimeters… over the machinery spaces and 55 millimeters… over the magazines and avgas storage tanks." / 「甲板**140〜50mmNVNC鋼板**」 | https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Hiry%C5%AB ; https://ja.wikipedia.org/wiki/飛龍_(空母) |
| 弹药库 | 舷侧 56 mm 或 65 mm CNC | 「弾薬庫舷側 **56mm[24]または65mmCNC鋼板**」 | https://ja.wikipedia.org/wiki/飛龍_(空母) |
| 水下防护 | 45 mm 纵向防雷纵壁 | "There was a 45mm longitudinal anti-torpedo bulkhead." | https://www.navypedia.org/ships/japan/jap_cv_hiryu.htm |
| 装甲总重 | 【未获取】 | — | — |

---

## §6 航空设施

### §6.1 蒼龍

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 飞行甲板 | **216.9 m × 26.0 m**；高出水线 12.8 m；木铺板（首尾端与两舷为钢板） | 「飛行甲板 **216.9m x 26.0m**」 / "The carrier's 216.9-meter flight deck was **26 meters** wide and overhung her superstructure at both ends… The flight deck was only **12.8 meters** above the waterline" | https://ja.wikipedia.org/wiki/蒼龍_(空母) ; https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB |
| 机库层数与尺寸 | 2 层（各 3 区划，共 6 区划）。上层 171.3 × 18.3 × 高约 4.6 m；下层 142.3 × 18.3 × 高约 4.3 m；合计约 5,736 m² | "The upper hangar was **171.3 by 18.3 metres** and had an approximate height of **4.6 meters**; the lower was **142.3 by 18.3 metres** and had an approximate height of **4.3 meters**. Together they had an approximate total area of 5,736 square metres" / 「格納庫：上下2段（各段3区画・計6区画）」 | 同上 ; https://japanese-warship.com/carrier/soryu/ |
| 升降机数量/位置 | 3 基；前部在舰岛旁中线，中/后两部偏向右舷 | "three elevators, the forward one abreast the island on the centerline and the other two offset to starboard" | https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB |
| 升降机尺寸 | 前 16 × 11.5 m；中 11.5 × 12 m；后 11.8 × 10 m（英文维基）/ 前 16×11.5、中 12×11.5、后 10×11.5 m（Kojinsha） | "The forward platform measured **16 by 11.5 meters**, the middle one **11.5 by 12 meters**, and the rear **11.8 by 10 meters**." / "SORYU's forward elevator measured **16m by 11.5m, middle 12m by 11.5m, and aft 10m by 11.5m**." | https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB ; https://www.combinedfleet.com/kojinshavolume6.pdf |
| 升降机能力 | 5,000 kg | "They were capable of transferring aircraft weighing up to **5,000 kilograms**" | 同上 |
| 拦阻索 | 9 组横向（呉式4型），可拦停 6,000 kg 飞机；钢索高出甲板 100–150 mm；电动吸收动能，40 m 内停住 4 t / 30 mps 飞机，12 秒收回 | "Nine transverse arrestor wires were installed on the flight deck and could stop a 6,000 kg aircraft." / "SORYU and HIRYU were fitted with **Kure Type 4** arrester wires… Type 4 could stop a 4-ton aircraft traveling at a speed of 30mps (acceleration 2,0 G's) in less than 40 meters. The released wire was electrically retrieved in 12 seconds." | 同上 ; Kojinsha 同上 |
| 拦阻索分布 | 苍龙：防冲网前 2 组、后 7 组 | "two located forward of the crash barriers and **seven aft (three and six on HIRYU)**" | https://www.combinedfleet.com/kojinshavolume6.pdf |
| 防冲网（crash barrier） | 苍龙：2 部固定式（前/中部升降机之间）+ 2 部移动式；久式3型，可 7 m 内拦停 4 t / 15 mps 飞机 | "Both carriers had two fixed crash barriers installed between the foremost and middle elevators. In addition, SORYU carried **two** and HIRYU **three** mobile crash barriers." | 同上 |
| 弹射器 | 【未获取（单舰原文）】；见下方「旁证」 | 旁证①：「艦載機はできるだけ甲板上に並べ、**カタパルトで一気に発艦させることも求められています**」（这是原始设计要求，不是实装记录） 旁证②：「上述の通り『**日本海軍は空母用カタパルトを実用化できなかった**』とあるが」 旁证③："The IJN began the development of domestic carrier catapults at the time of KAGA's refit. Nevertheless, **a usable model was not ready until the end of the war**." | https://japanese-warship.com/carrier/soryu/ ; https://ja.wikipedia.org/wiki/カタパルト ; https://www.combinedfleet.com/kojinshavolume6.pdf |
| 着舰识别文字 | **存疑**：一说「サ」，一说无记入 | 「従来艦上機からの個艦識別用として飛行甲板後端に「**サ**」の文字が書かれていたという説がある。一方で**無記入だったとする説もある**。ミッドウェー作戦時の空撮写真にそれらしいものがまったく写っておらず」 | https://ja.wikipedia.org/wiki/蒼龍_(空母) |
| 其他 | 后升降机旁有 4 t 折叠吊车；取消了加贺/龙骧式机库后端门；舰尾着舰标识与滑走静止装置为日本空母首次自建成即装备 | 「後部エレベーター脇には揚収用クレーンを備え、加賀や龍驤に見られた**格納庫後端の扉は廃止**されている」 / 「後に日本空母の標準装備となる**艦尾の着艦標識、滑走静止装置**が建造当初から設置されたのは蒼龍が初めてであった」 | https://ja.wikipedia.org/wiki/蒼龍_(空母) |

### §6.2 飛龍

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 飞行甲板 | **216.9 m × 27.0 m**（日文维基信息框另记 27.4 m，见 §D-4）；甲板高 12.57 m | 「飛行甲板 **216.9m x 27.4m**」 / 「飛行甲板幅 27.0（最大）・飛行甲板高さ **12.57**」 / "The carrier's 216.9-meter flight deck was **27 meters** wide" | https://ja.wikipedia.org/wiki/飛龍_(空母) ; http://vanguard.my.coocan.jp/700contents/hiryu1.htm ; https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Hiry%C5%AB |
| 机库层数与尺寸 | 2 层（各 3 区划，共 6 区划）。上层 171.3 × 18.3 × 4.6 m；下层 142.3 × 18.3 × 4.3 m | "The upper hangar was 171.3 by 18.3 metres… 4.6 meters; the lower was 142.3 by 18.3 metres… 4.3 meters" | https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Hiry%C5%AB |
| 升降机数量/位置 | 3 基；前部在中线（舰岛旁），中/后偏右舷 | "three elevators, the forward one abreast the island on the centerline and the other two offset to starboard" | 同上 |
| 升降机尺寸 | 前 16 × 13 m；中 13 × 12 m；后 11.8 × 13.0 m（英文维基）/ 前 16×13、中 12×13、后 13×11.8 m（Kojinsha）/ 前 16×12、中 12×11.5、后 10×11.8 m（日文维基） | "The forward platform measured **16 by 13 meters**, the middle one **13 by 12 meters**, and the rear **11.8 by 13.0 meters**." / 「前方から**16×12m、12×11.5m、10×11.8m**」 / "HIRYU's elevators were somewhat larger: the forward one measured **16m by 13m, middle 12m by 13m, and aft 13m by 11.8m**." | 同上 ; https://ja.wikipedia.org/wiki/飛龍_(空母) ; https://www.combinedfleet.com/kojinshavolume6.pdf |
| 升降机能力 | 5,000 kg | "They were capable of transferring aircraft weighing up to 5,000 kilograms" | https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Hiry%C5%AB |
| 拦阻索 | 9 组横向（呉式4型），可拦停 6,000 kg；其中 3 组前移，可「向舰首方向着舰」（实战未用） | "Nine transverse arrestor wires… could stop a 6,000-kilogram aircraft. **One group of three wires was positioned further forward to allow the ship to land aircraft over the bow**, although this was never done in practice." | 同上 |
| 拦阻索分布 | 飞龙：防冲网前 3 组、后 6 组 | "two located forward of the crash barriers and seven aft (**three and six on HIRYU**)" | https://www.combinedfleet.com/kojinshavolume6.pdf |
| 防冲网 | 2 部固定式 + 3 部移动式 | "Both carriers had two fixed crash barriers… SORYU carried two and HIRYU **three** mobile crash barriers." | 同上 |
| 弹射器 | 【未获取（单舰原文）】；旁证同苍龙（见 §6.1 及 §13） | 同上三条旁证 | 同上 |
| 着舰识别文字 | **「ヒ」**（片假名） | 「飛行甲板後端には、上空からの識別のために片仮名で「**ヒ**」の文字が記入された」 / 信息框「着艦識別文字 ヒ」 / 图注「ミッドウェー海戦で、敵機の爆撃を回避する飛龍。飛行甲板後部に“ヒ”の字が確認出来る」 | https://ja.wikipedia.org/wiki/飛龍_(空母) |
| 其他 | 舵为半平衡式单舵（苍龙为全平衡双舵）；前部有螺旋桨乱流防护网（可 30 秒内于 35 m/s 风中升起）；飞行甲板中央有风向标示（6 条白色放射线，间隔 10°） | "In contrast with SORYU's fully balanced twin rudder, **HIRYU featured a semi-balanced single rudder**." | https://www.combinedfleet.com/kojinshavolume6.pdf |

---

## §7 武备

### §7.1 蒼龍

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 主炮（高角炮） | **40 口径 12.7 cm 连装高角炮 6 基 12 门**（八九式） | 「40口径12.7cm連装高角砲6基12門」 / "6 × twin 12.7 cm (5 in) DP guns" | https://ja.wikipedia.org/wiki/蒼龍_(空母) ; https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB |
| 主炮布置 | 舷侧突出炮座，左右各 3 基 | "six twin-gun mounts equipped with 50-caliber 12.7-centimeter Type 89 dual-purpose guns mounted on **projecting sponsons, three on either side** of the carrier's hull" | 同上 |
| 主炮性能（炮本身） | 最大射程 14,700 m；最大射高 9,440 m（+90°）；射速 14 发/分（持续约 8 发/分）；初速 700–725 m/s；弹重 23.45 kg | "The guns had a range of 14,700 meters, and a ceiling of 9,440 meters at an elevation of +90 degrees. Their maximum rate of fire was fourteen rounds a minute, but their sustained rate of fire was around eight rounds per minute." / "Muzzle Velocity Common Type 0 HE: 2,360 - 2,379 fps (700 - 725 mps)" | 同上 ; https://www.navweaps.com/Weapons/WNJAP_5-40_t89.htm |
| 25 mm 高炮 | **连装 14 基 = 28 挺**（九六式 25 mm） | 「九六式二十五粍高角機銃**連装14基28挺**」 / "fourteen twin-gun mounts for license-built Hotchkiss 25 mm (1 in) Type 96 AA guns" | https://ja.wikipedia.org/wiki/蒼龍_(空母) ; https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB |
| 25 mm 布置 | 其中 3 基设于飞行甲板前端下方平台，另 3 基在舰首（日本空母首次在舰首装炮） | "Three of these were sited on a platform just below the forward end of the flight deck." / 「蒼龍には25ミリ機銃は14基あったが、うち3基は**艦首**に搭載。艦首に兵器搭載は本艦が初である」 | 同上 |
| 机枪 | 11 mm 轻机枪 6 挺 | 「11mm軽機銃6挺」 | https://ja.wikipedia.org/wiki/蒼龍_(空母) |
| 弹药基数 | 【未获取】（NavWeaps 对八九式列「Shôkaku: 250 rounds / Others: N/A」，未给苍龙数值） | "Ammunition stowage per gun … **Others: N/A**" | https://www.navweaps.com/Weapons/WNJAP_5-40_t89.htm |

> **任务书前提核实（主炮）**：✔ 成立。苍龙/飞龙用 12.7 cm，不是 20 cm。但必须补一句：**20 cm 炮原本在计划里**——G6 案「20.3cm連装砲3基6門」，G8 案「15.5cm三連装砲と20cm連装砲を1基ずつ」，最后因友鹤事件全部取消。
> 原文：「最初の【蒼龍】案である「G6」案は…艦首側に**20.3cm連装砲**を3基搭載しているのがはっきりわかります」 / 「まず**主砲が全部取り払われ**、12.7cm連装高角砲も6基へと微減」
> 来源：https://japanese-warship.com/carrier/soryu/

### §7.2 飛龍

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 主炮（高角炮） | **40 口径 12.7 cm 连装高角炮 6 基 12 门** | 「40口径12.7cm連装高角砲：6基12門」 / "6 × twin 12.7 cm (5 in) DP guns" | https://ja.wikipedia.org/wiki/飛龍_(空母) ; https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Hiry%C5%AB |
| 主炮布置（与苍龙不同） | 前部右舷 2、左舷 2；后部右舷 1、左舷 1（苍龙为前 2-1、后 1-2） | 「高角砲位置 前方右舷２、左舷２ / 後方右舷１、左舷１」+ 对照栏苍龙「前方右舷２、左舷１ / 後方右舷１、左舷２」 | http://vanguard.my.coocan.jp/700contents/hiryu1.htm |
| 25 mm 高炮 | **三连装 7 基（21 挺）+ 连装 5 基（10 挺）= 31 挺** | 「九六式二十五粍高角機銃：**3連装7基、連装5基 計31挺**」 / "seven triple and five twin-gun mounts" | https://ja.wikipedia.org/wiki/飛龍_(空母) ; https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Hiry%C5%AB |
| 25 mm 布置 | 其中 2 基三连装设于飞行甲板前端下方平台 | "Two of the triple mounts were sited on a platform just below the forward end of the flight deck." | 同上 |
| 机枪 | 【未获取】（日文维基飞龙条目未列轻机枪；苍龙条目列 11 mm 6 挺，不可类推） | — | — |
| 其他武备 | 九一式爆雷 6 个 | 「九一式爆雷6個」 | https://ja.wikipedia.org/wiki/飛龍_(空母) |
| 弹药基数 | 【未获取】 | — | — |

> **管数对比**：苍龙 28 挺（14×2），飞龙 31 挺（7×3 + 5×2）。飞龙管数更多，是两舰防空火力最直观的差别之一。

---

## §8 雷达与火控

### §8.1 蒼龍

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 雷达（中途岛时是否已装） | **未装**。日本海军开战时舰载雷达尚属空白，1942-05-27 才首次装到战列舰伊势、日向 | "At the outbreak of the war, the Navy did not have ship radar… the Navy finally completed the installation of radar equipment on the battleships, ISE and HYUGA, on **27 May**, just prior to the beginning of this operation." | https://www.ibiblio.org/hyperwar/Japan/Monos/pdfs/JM-93_MidwayOperations,May-June42/JM-93.htm |
| 雷达型号 | 无（21 号电探为「ミッドウェー海戦後」才装重要舰艇） | 「ミッドウェー海戦後に重要艦艇から搭載され（最も早い搭載は1942年（昭和17年）6月ころの空母「翔鶴」や隼鷹型航空母艦と言われる）」 | https://ja.wikipedia.org/wiki/二式二号電波探信儀一型 |
| 射击指挥仪 | **九四式高射指揮装置 2 基**（左右各 1）；舰岛上的右舷指挥仪可统控全部八九式炮 | "The ship was equipped with two Type 94 fire-control directors to control the 12.7-centimeter (5.0 in) guns, one for each side of the ship, although the starboard director on the island could control all of the Type 89 guns." | https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB |
| 25 mm 指挥仪 | 九五式机枪指挥装置 5 基（左右各 2、舰首 1） | "The Type 96 guns were controlled by **five Type 95 directors**, two on each side and one in the bow." | 同上 |
| 测距仪 | 【未获取】 | — | — |

### §8.2 飛龍

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 雷达（中途岛时是否已装） | **未装**（同上 JM-93 原文；无任何来源称飞龙中途岛时带雷达） | 同上 | 同上 |
| 射击指挥仪 | **九四式高射指揮装置 2 基**；右舷的在舰岛顶上，左舷的在飞行甲板下 | "two Type 94 fire-control directors… one for each side of the ship; **the starboard-side director was on top of the island** and the other director was positioned below flight deck level on the port side." | https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Hiry%C5%AB |
| 25 mm 指挥仪 | 九五式 5 基（左右各 2、舰首 1） | "The Type 96 guns were controlled by five Type 95 directors, two on each side and one in the bow." | 同上 |
| 测距仪 | 【未获取】 | — | — |

---

## §9 编制

### §9.1 蒼龍

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 计划乘员 | 1,100 名 | 「計画乗員 **1,100名**」 | https://ja.wikipedia.org/wiki/蒼龍_(空母) |
| 竣工时定员 | 1,101 名 | 「竣工時定員 **1,101名**」 | 同上 |
| 定员细分（军官数） | 士官 53、特務士官 29、准士官 43、下士官 285、兵 691（合计 1,101） | 「航空母艦定員表 其ノ四 蒼龍、**士官53人、特務士官29人、准士官43人、下士官285人、兵691人**」 | https://ja.wikipedia.org/wiki/蒼龍_(空母) |
| 战时编制 | 【未获取】（仅有定员表，无战时编制原文） | — | — |
| 中途岛实载人数 | 1,103 名（乘员）；战死 711 名（英文维基）/ 718 名（日文维基） | 「最終時 **1,103名**」 / "Losses were **711** crew of her complement of 1,103" / 「柳本艦長以下准士官以上35名、下士官兵683名、**計718名**が戦死」 | 同上 ; https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB ; https://ja.wikipedia.org/wiki/蒼龍_(空母) |

### §9.2 飛龍

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 计划乘员 | 1,100 名 | "Her crew consisted of 1,100 officers and enlisted men." | https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Hiry%C5%AB |
| 竣工时定员 | 1,101 名 | 「計画乗員、竣工時定員 **1,101名**」 | https://ja.wikipedia.org/wiki/飛龍_(空母) |
| 定员细分（军官数） | 准士官以上（军官）**95 名**、下士官兵 1,315 名、傭人 6 名，合计 **1,416 名** | 「飛龍の定員は**准士官以上95名、下士官兵1315名、傭人6名、計1,416名**である」 | 同上 |
| 旗舰队部人员 | 另加第二航空戦隊司令部員 23 名 | 「これに第二航空戦隊司令部員**23名**と航空機搭乗員…が乗艦していた」 | 同上 |
| 战时编制 | 【未获取】 | — | — |
| 中途岛实载人数 | **不明**（日文维基明确写「不明」；信息框另给「最終時 1,103名」） | 「ミッドウェー海戦時の飛龍に乗り組んでいた**実員は不明**だが…」 / 「最終時 **1,103名**」 | 同上 |

---

## §10 涂装与外形

| 项 | 蒼龍 | 飛龍 | 原文照抄 | 来源 |
|---|---|---|---|---|
| 涂装方案与时间窗 | 【未获取】 | 【未获取】 | 仅获得到「外舷塗装」这一动作描述，无方案/色号/时间窗原文：「蒼龍（1937年秋）で、**外舷塗装のために足場が組まれている**」 | https://ja.wikipedia.org/wiki/蒼龍_(空母) |
| 舰岛位置 | **右舷前部**，体积小，与驱逐舰舰桥同规模；建在向右舷外伸的平台上，不占用飞行甲板宽度 | **左舷中央**，比苍龙多一层（4 层 5 甲板），前后长度也更长，能设作战室 | 苍龙：「艦橋は**右舷前部**にあり」 / 「右舷に設置された艦橋は**駆逐艦の艦橋とほぼ同規模**の大きさである」 / "Sōryū's island was built on a starboard-side extension that protruded beyond the side of the hull so that it did not encroach on the width of the flight deck." 飞龙：「**左舷中央**に島型艦橋を配置」 / 「形状は赤城同様…**蒼龍より1層多い4層5甲板**となっている」 | https://ja.wikipedia.org/wiki/蒼龍_(空母) ; https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB ; https://ja.wikipedia.org/wiki/飛龍_(空母) |
| 舰岛位置的实战后果 | 飞行员习惯右舷舰岛，着舰时无意识左偏 | 接收苍龙舰载机时发生**撞上左舷舰岛坠毁**事故 | 「ドック入りした蒼龍の航空機を受け入れた際には、右舷に艦橋のある蒼龍での着艦に慣れたパイロット達が無意識に飛行甲板左に寄って着艦し、**左舷にある飛龍艦橋に接触して墜落する事故**も起きた」 | https://ja.wikipedia.org/wiki/飛龍_(空母) |
| 烟囱 | 右舷中部，2 座向下排气式弯曲烟囱；锅炉进气/机舱排气走中部舷侧外挂箱型通风筒（两舰共同外观特征） | 右舷中央 1 座大型弯曲烟囱（排气强烈，后加防烟罩） | 苍龙：「**右舷中部に下方排出式の煙突を2つ**持つ」 / "exhausted just below flight deck level through two funnels curved downwards" 飞龙：「**右舷中央部に大きな煙突**があるので、排煙の影響を考慮して艦橋は左舷中央部に置かれた」 | https://ja.wikipedia.org/wiki/蒼龍_(空母) ; https://ja.wikipedia.org/wiki/飛龍_(空母) ; http://vanguard.my.coocan.jp/700contents/hiryu1.htm |
| 识别标识 | 「サ」说 vs 无记入说，**存疑** | 飞行甲板后端片假名**「ヒ」**，中途岛空拍可辨 | 见 §6 | https://ja.wikipedia.org/wiki/蒼龍_(空母) ; https://ja.wikipedia.org/wiki/飛龍_(空母) |

---

## §11 生涯时间线

### §11.1 蒼龍

| 日期 | 事件 | 原文/来源 |
|---|---|---|
| 1934-11-20 | 呉海軍工廠起工 | 「1934年 - 11月20日 呉海軍工廠にて起工」 |
| 1935-12-23 | 进水（书面上记 1935-01-23） | 「1935年 - 12月23日 進水」 |
| 1937-12-29 | 竣工，编入第 2 航空戦隊 | 「1937年 - 12月29日 竣工。第2航空戦隊に編入される」 |
| 1938 | 参加广东攻略作战（中日战争） | 「1938年 - **広東攻略作戦に参加**」 |
| 1938-12-15 | 编入第二航空戦隊（司令官鮫島具重少将） | 「1938年12月15日、蒼龍は第二航空戦隊…に編入される」 |
| 1939-11-15 | 飞龙编入，二航戦成为苍龙+飞龙+第 11 駆逐隊 | 「準同型艦飛龍の編入にともない、二航戦は空母2隻（蒼龍、飛龍）および第11駆逐隊…という戦力になる」 |
| 1940-10-11 | 参加横滨港外纪元二千六百年特别观舰式 | 「横浜港沖で行われた**紀元二千六百年特別観艦式**に、二航戦の僚艦とともに参加」 |
| 1941-03 | 南下调解仏印-泰国边境纠纷途中，与驱逐舰「夕月」碰撞，舰首撞入夕月左舷中部，回佐世保入坞 | 「蒼龍艦首が**夕月左舷中央部に乗り上げ、破口が生じた**…蒼龍は搭載機をうつしたのち佐世保に戻ってドックに入った」 |
| 1941-04-10 | 二航戦编入新设第一航空艦隊 | 「1941年4月10日、第二航空戦隊（蒼龍、飛龍）は、新設された第一航空艦隊に編入される」 |
| 1941-07 | 支援第二次仏印进驻（FU 作戦） | 「太平洋戦争開戦前の7月には**南部仏印進駐作戦の支援**を行った」 ; TROM「Assigned to "FU-GO" Escort Fleet, participated in "FU" Operations from 10 - 30 July」 |
| 1941-09-12 | 赤城舰长长谷川喜一兼任苍龙舰长（一时） | 「赤城と蒼龍の艦長を兼務することになった」 |
| 1941-10-06 | 柳本柳作大佐就任苍龙舰长 | 「柳本柳作大佐が蒼龍の艦長に補職された」 ; TROM「Captain Kosaka relieved by Captain (Rear-Admiral posthumously) Yanigimoto Ryusaku」 |
| 1941-11-22 | 与飞龙同抵单冠湾 | 「Arrive Hitokappu Bay with HIRYU」 |
| 1941-11-26 | 机动部队从单冠湾出击 | 「departs Hittokapu Wan in the "Hawaii Operation"」 |
| 1941-12-07（当地） | 珍珠港：第一波 8 架 B5N 鱼雷 + 10 架 B5N（800 kg 九九式五号弹）+ 8 架 A6M；第二波 18 架 D3A + 9 架 A6M | 「SORYU contributes **eight B5N2 "Kate" torpedo armed bombers and ten B5N2 "Kate" each equipped with one 800-kg Type 99 model 5 bomb**… and eight A6M2 "Zeke" fighters」；「SORYU contributes **eighteen D3A1 "Val"** dive bombers」 |
| 1941-12-07 | 损失 3 架 A6M + 2 架 D3A，共 5 架（全在第二波） | 「Losses sustained by SORYU's aircraft are three A6M2 "Zeke", and two D3A1 "Val", totaling five aircraft. All having been lost from the second wave」 |
| 1941-12-16 16:30 | 与飞龙一起从机动部队分遣，转攻威克岛 | 「Detached from Striking Force Main Body with HIRYU… to participate in strikes against Wake Island」 |
| 1941-12-21/22/23 | 威克岛三轮空袭；22 日苍龙 2 架 B5N 被 F4F 击落 | 「they encountered opposition from the last two remaining "Wildcat" fighters, which **shot down two of SORYU's "Kates"**」 |
| 1941-12-29 | 返回呉 | 「Return to Kure」 |
| 1942-01-08 | 编入南方部队第二航空攻击部队 | 「Assigned to 2nd Air Attack Force, Southern Force」 |
| 1942-01-23/24 | 安汶攻击（23 日天候不良中止，24 日实施） | 「Launched strike against Ambon. However the attack had to be aborted and returned due to bad weather」 |
| 1942-02-19 | 达尔文空袭：苍龙出零战 9、舰爆 18、舰攻 18；损 1 架舰爆迫降 | 「2月19日、ダーウィン空襲に「蒼龍」からは**零戦9機、艦爆18機、艦攻18機**が参加し、艦爆1機が不時着水（乗員は救助された）」 |
| 1942-03-01 | 与加贺共同攻击美油船 Pecos；苍龙 6 架 Vals（TROM）/9 架（日文维基） | 「SORYU launched six "Vals" to attack the oiler」 / 「蒼龍も13時9分に九九式艦爆**9機**からなる攻撃隊…を発進させてペコスに向かわせた」 |
| 1942-03-07 | 圣诞岛空袭；苍龙 9 架舰爆击沉荷兰货船 POELAU BRAS | 「nine dive-bombers of SORYU sink Dutch freighter POELAU BRAS (9,278 tons)」 |
| 1942-04-05 | 科伦坡空袭：苍龙出 18 架 B5N + 9 架 A6M；当日午后 18 架 D3A 参与击沉 CORNWALL/DORSETSHIRE | 「SORYU contributed 18 B5N and 9 A6M to that total」 / 「SORYU's contributes **18 of the dive-bombers**」 |
| 1942-04-09 | 亭可马里空袭；苍龙出 18 架 D3A + 3 架 A6M，参与击沉 HERMES | 「SORYU contributed **18 D3A and three A6M** to the strike」 |
| 1942-04-18 | 追击杜立特空袭编队（未遇） | 「attempted pursuit of the "Doolittle Raiders"」 |
| 1942-04-22 | 返柱岛泊地 | 「Return to Hashirajima with HIRYU」 |
| 1942-05-15 | 在佐世保小修；二航戦旗舰旗移至飞龙 | 「At Sasebo undergoing minor maintenance. Flag of ComCardiv 2 is transferred to HIRYU」 |
| 1942-05-27 06:00 | 从柱岛出击参加 MI 作战 | 「SORYU departs Hashirajima for the MI Operation」 |
| **1942-06-04 中途岛（当地时）** | 见下节逐时 | — |
| 1942-06-05 16:12（JST） | 磯風雷击处置，3 分钟后翻覆沉没 | 「Sunk: 1912 (1612 JST) Destroyer ISOKAZE fired three torpedoes at SORYU」 |
| 1942-08-10 | 除籍 | 「Removed from the Navy list」 |

#### 中途岛逐时（苍龙，当地时；JST = 当地 −3h、日期 +1）

| 时刻（当地） | 事件 |
|---|---|
| 04:30（01:30 JST） | 第一波发舰：苍龙出 **18 架 D3A（挂八〇番陆用爆弹）+ 9 架 A6M**（TROM 原文如此，与日文维基/英文维基记「18 架九七舰攻」冲突，见 §D-2） |
| 06:34 | 苍龙机攻击 Sand/Eastern 两岛；**1 架被拦截击落** |
| 07:05 | 发 3 架战斗机；发现敌雷击队 |
| 07:30 | 收回第一、第二批直掩（6 架） |
| 07:55 | 最大战速，开火；敌机投弹 9–10 发，**未命中** |
| 08:19 | 敌机在苍龙附近大量投弹，苍龙、飞龙猛烈对空射击，**未命中** |
| 08:30 | 侦察用 D4Y1（十三试舰爆）起飞，接替利根 4 号机 |
| 08:50–09:10 | 收回中途岛攻击队；2 架攻击机迫降，乘员获救 |
| 09:30 | 发现 17 架敌雷击机，2 条鱼雷从右舷掠过 |
| 10:24 | 加贺起火 |
| **10:25–10:26** | 被**约克城 VB-3 的 13 架 SBD** 攻击，**命中 2 弹**（一在前升降机，一在第二升降机后方），引发大火与诱爆 |
| 10:29 | 第 3 发 1,000 磅炸弹命中舷侧烟囱处，穿透至下层机库爆炸，炸断锅炉舱蒸汽管 |
| 10:40 | 失速停船，蒸汽从左舷喷出，开始左倾 |
| 10:45 | 柳本舰长下令非必要人员离舰（本人拒绝离舰，留在右舷信号塔） |
| 11:12–11:40 | 千曲派 2 号艇协助撤离；苍龙侦察机报回「发现敌空母部队」 |
| 11:34 | 苍龙 1 架轰炸机改降飞龙 |
| 13:30 | 苍龙侦察机降落在飞龙 |
| 15:02（日文维基） | 磯風、浜風收容苍龙幸存者 |
| 17:00 | 磯風电：「苍龙已失战斗力，请示处置」 |
| 19:00 | 飞行长楠本几登组织防火队准备再登舰，被制止（接自沉令） |
| **19:12（16:12 JST）** | 磯風发射 3 条鱼雷（至少 2 条命中），苍龙舰尾下沉、3 分钟后翻覆 |
| 19:20 | 沉没处发生水下大爆炸；随后救起随舰沉没的落水者，含少数机舱人员 |
| 1942-06-05 JST 16:13–16:15 | 日文维基口径的沉没时刻（= 当地 6/4 19:13） |

来源：https://www.combinedfleet.com/soryu.htm ；https://ja.wikipedia.org/wiki/蒼龍_(空母)

### §11.2 飛龍

| 日期 | 事件 | 原文/来源 |
|---|---|---|
| 1935-11-22 | 正式命名「飛龍」 | 「横須賀海軍工廠で建造予定の空母に飛龍の艦名が正式に与えられた」 |
| 1936-07-08 | 横須賀海軍工廠起工 | 「1936年（昭和11年）7月8日に起工」 |
| 1937-11-16 | 进水 | 「1937年（昭和12年）11月16日に進水」 |
| 1939-07-05 | 竣工（伏见宫博恭王临席） | 「7月5日、飛龍は**伏見宮博恭王臨席の元で竣工**」 |
| 1939-11-15 | 与苍龙、第 11 駆逐隊编成第二航空戦隊（司令官戸塚道太郎少将） | 「空母2隻（飛龍、蒼龍）は第11駆逐隊…と共に戸塚道太郎少将指揮の第二航空戦隊に配属された」 |
| 1940-04 | 与一航戦一起轰炸中国福建省 | 「飛龍は第一航空戦隊と共に**中国の福建省を爆撃**した」 |
| 1940-09-17 | 出呉，支援北部仏印进驻 | 「3隻（飛龍、初雪、白雪）は呉を出港し…**北部仏印進駐を支援**した」 |
| 1940-10-11 | 参加纪元二千六百年特别观舰式 | 「11日の紀元二千六百年特別観艦式に参加する」 |
| 1940-12-09 | 成为第二航空戦隊旗舰 | 「この時点での第二航空戦隊の旗艦は蒼龍だったが、12月9日より**飛龍が旗艦**となった」 |
| 1941-02 | 苍龙撞夕月后，飞龙在冲绳中城湾待机；参加中国沿海封锁作战 | 「飛龍は沖縄県中城湾で待機した。その後**中国沿岸封鎖作戦**に参加し」 |
| 1941-07-10 | 出日本，支援第二次仏印进驻；期间舰载机轰炸福建省南平 | 「インドシナに対する第二次仏印進駐を支援する。この期間中、艦載機が**福建省南平を爆撃**した」 |
| 1941-09-08 | 加来止男大佐就任舰长 | 「飛龍の艦長は矢野大佐から…**加来止男大佐**に交代する」 |
| 1941-09 起 | 在鹿儿岛湾、有明海进行珍珠港预习训练 | 「鹿児島湾や有明海で真珠湾攻撃の予行演習と訓練を行う」 |
| 1941-11-22 | 抵单冠湾；此时二航戦旗舰为苍龙 | 「この時の第二航空戦隊旗艦は**蒼龍**だった」 |
| 1941-11-26 | 出击 | 「単冠湾を出港し」 |
| 1941-12-07（当地） | 珍珠港：第一波 8 架 B5N 鱼雷 + 10 架 B5N（800 kg 弹）+ 6 架 A6M；其中水平轰炸队（楠美正少佐）投下的八〇番弹引爆亚利桑那前部弹药库 | 「The high-level bomber group under command of Lt.Cdr. Tadashi Kusumi is credited with the fatal bomb hit with a **No.80 bomb dropped from 3,200 meters that exploded USS ARIZONA's (BB-39) forward magazines at about 0806-07**」 |
| 1941-12-16 | 与苍龙分遣攻威克岛 | 「Detached from Striking Force Main Body with HIRYU to participate strikes against Wake Island」 |
| 1941-12-29 | 返呉 | 「Return to Kure」 |
| 1942-01-23/24 | 安汶攻击（两舰合计 54 机） | 「attacking Allied positions on the island on 23 January with 54 aircraft」 |
| 1942-02-19 | 达尔文空袭：飞龙出 44 机（零战 9、舰爆 17、舰攻 18）；1 架零战迫降未归（乗員豊島一成为澳军首个日俘） | 「2月19日にダーウィン空襲に飛龍艦載機**計44機(零戦9、艦爆17、艦攻18)**が参加し、零戦1機が不時着・未帰還となった」 |
| 1942-03-01 | 飞龙舰爆重创美驱逐舰 Edsall；同日击沉油船 Pecos | "On 1 March 1942, the ship's D3As damaged the destroyer USS Edsall badly enough for her to be caught and sunk by Japanese cruisers. Later that day the dive bombers sank the oil tanker USS Pecos." |
| 1942-03-07 | 圣诞岛；飞龙机击沉荷兰货船 Poelau Bras | 「HIRYU's aircraft sank the Dutch freighter Poelau Bras」 |
| 1942-04-05 | 科伦坡空袭：飞龙出 18 架 B5N + 9 架 A6M；后出 18 架 D3A 参与击沉 CORNWALL/DORSETSHIRE | 「飛龍零戦9機、艦攻18機がセイロン島コロンボ空襲を行い」 / 「飛龍からは**18機**である」（D3A） |
| 1942-04-09 | 亭可马里空袭：飞龙出 9 架 A6M + 18 架 B5N；后出 18 架 D3A + 3 架 A6M 攻击 HERMES 群 | 「4月9日にはセイロン島ツマンコリー軍港を空襲、飛龍からの参加機は**零戦9、艦攻18**だった」 / 「飛龍攻撃隊(**零戦3、艦爆18**)は空母ハーミーズ…を共同撃沈した」 |
| 1942-04-15 | 抽调 5 架零战、4 架舰爆给第五航空戦隊 | 「飛龍から零戦5、艦爆4機が第五航空戦隊戦力補強のために移された」 |
| 1942-04-22 | 返佐世保入坞大修；期间机动部队大规模人事异动 | 「4月22日、飛龍は佐世保に帰港した。ドックにてオーバーホール中」 |
| 1942-05-27 | 从柱岛出击 | 「Departed Hashirajima for the Midway Operation」 |
| **1942-06-04 中途岛（当地时）** | 见下节逐时 | — |
| 1942-06-05 05:10（当地） | 巻雲雷击处置 | 「at 0510 scuttled by MAKIGUMO with one torpedo」 |
| 1942-06-05 09:12（当地） | 舰首下沉翻覆，沉没 | 「the carrier at 0912 **upended and sank by the bow**」 |
| 1942-06-06 06:06–06:15（JST） | 日文维基口径的沉没时刻 | 「日本時間6月6日午前6時6-15分、飛龍は左舷に傾きつつ艦首から沈んでいった」 |
| 1942-07-14 | 与赤城一起被列为第三舰队附属（为隐匿损失） | 「7月14日…「飛龍」は「赤城」とともに第三艦隊附属とされた。2隻が第三艦隊に加えられたのは**喪失秘匿のため**であった」 |
| 1942-09-25 | 除籍 | 「除籍 1942年9月25日」 |

#### 中途岛逐时（飞龙，当地时；JST = 当地 −3h、日期 +1）

| 时刻（当地） | 事件 |
|---|---|
| 04:30 | 第一波：飞龙出 18 架 B5N（友永丈市大尉指挥）+ 9 架零战（其中 1 架因发动机故障返航） |
| 06:34 前后 | 攻击 Sand 岛；损失惨重：2 架被战斗机击落、1 架被高炮击落、1 架（菊池六郎机）重伤迫降库雷环礁、1 架返航途中迫降、5 架报废，另 2 架零战不可用 |
| 07:05–07:10 | 直掩 6 架零战；参与击落来袭 TBF 5 架、B-26 2 架；飞龙被 1 架零战击落 |
| 07:40 | 2 架直掩零战弹药耗尽着舰 |
| 09:37 | 追加 4 架零战加强直掩（对 VT-6） |
| 10:13 | 再发 3 架零战（对 VT-3）；被野猫击落 2 架、1 架迫降 |
| 10:25 前后 | 赤城、加贺、苍龙相继起火时，**飞龙未受损**；因左舷舰岛导致的航行序列，飞龙向三舰左舷方向脱离并躲进飑区，避开第一轮俯冲轰炸 |
| **10:54** | 飞龙单舰反击：18 架 D3A（小林道雄大尉指挥；250 kg 通常弹 12、陆用弹 8）+ 6 架零战，攻击约克城 |
| 12:00 前后 | 命中约克城 3 弹（日方记录 6 弹），重创 |
| **13:30** | 第二波：10 架 B5N（含 1 架赤城机）+ 6 架零战（含 2 架加贺机）；14:38 遭野猫突袭，损失 4 架 B5N，2 架命中约克城（炸坏 3 座锅炉、全舰断电） |
| 14:30 前后 | 约克城恢复 19 kt；17 分钟后左倾 23°，弃舰 |
| 16:30 | 山口多闻电告南云，拟黄昏（约 18:00）发第三波；南云令舰队西撤 |
| 16:45 | 企业号俯冲队发现飞龙 |
| 16:56 | 南云令转向 120°（可能为回收侦察机），打乱领先 SBD 瞄准 |
| 17:01 | 日方才发现美机 |
| **17:03** | 企业号 + 约克城 SBD 共 13–24 架俯冲，**命中 4 发 1,000 磅炸弹**：前部飞行甲板 3 发成串、舰桥旁 1 发；首弹掀飞前升降机砸向舰桥（反成防爆墙护住舰桥）；前半个飞行甲板塌入机库 |
| 17:42 起 | 两批 B-17 来袭未命中；1 架扫射飞行甲板打死数名高炮手 |
| 18:00 前后 | 轮机 4 座正常、8 座锅炉中 5 座正常，轮机科报可跑 30 kt |
| 21:23 | 主机停转（舵机马达停、切换电池后舰桥与机舱电话中断） |
| 23:58 | 大爆炸（日文维基记 23:58；Tully 记 01:58） |
| 次日 03:15 | 下令弃舰；幸存者由巻雲、風雲收容；山口多闻、加来止男留舰 |
| **05:10** | 巻雲发射 1 条鱼雷（另 1 条未命中），命中舰首附近 |
| 约 06:30 | 凤翔号九六式舰攻发现飞龙仍漂浮，甲板上有人影挥帽 |
| 约 09:00 | 舰上残存 39 人乘 cutter 离舰 |
| **09:12** | 飞龙舰首下沉、翻覆沉没，带走 389 具遗体 |
| 此后 14 天 | cutter 漂流，被 PBY 发现，由 USS Ballard 救起（漂流中 5 人死亡） |

来源：https://www.combinedfleet.com/hiryu.htm ；https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Hiry%C5%AB ；https://ja.wikipedia.org/wiki/飛龍_(空母)

---

## §12 舰载机编制（中途岛时）

### §12.1 蒼龍

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 机型与数量 | 零战 18、九九舰爆 16、九七舰攻 18、十三试舰爆（D4Y1-C）2 架；另搭载第 6 航空隊零战 3 架（预定进驻中途岛） | 「SORYU's air principal air group consists of **eighteen A6M2 "Zeke" fighters, sixteen D3A1 "Val" dive-bombers, eighteen B5N2 "Kate" attack planes**. Also aboard for the voyage were three A6M2 "Zeke" fighters assigned to the 6th Air Group… One, possibly two, experimental D4Y1 carrier bombers」 / "Her aircraft complement consisted of eighteen Zeros, sixteen D3As, eighteen B5Ns, and two preproduction reconnaissance variants (D4Y1-C)… Also aboard were three A6M Zeros of the 6th Kōkūtai" | https://www.combinedfleet.com/soryu.htm ; https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB |
| 出击 | 第一波：18 架攻击机（挂 800 kg 陆用爆弹）+ 9 架零战；当日多次发 3 架直掩零战（07:05、09:45、10:00、10:15）；08:30 发 1 架 D4Y1 侦察 | 「SORYU contributes eighteen D3A1 "Val" armed with Type # 80 land bombs and nine A6M2 "Zekes"」 / "Sōryū launched another trio of CAP Zeros at 10:00 and another three at 10:15" | 同上 |
| 损失 | 攻击队损失舰攻 3 架（含 2 架迫降）；5 架报废（含 1 架改降飞龙）；直掩零战损失若干；搭乗员战死 10 名（机上 6、舰上 4） | 「蒼龍攻撃隊は全機が被弾して**艦攻3機を喪失(不時着2含む)**」 / 「搭乗員戦死者は機上6名、艦上4名の合わせて**10名**」 | https://ja.wikipedia.org/wiki/蒼龍_(空母) |

### §12.2 飛龍

| 项 | 值 | 原文照抄 | 来源 |
|---|---|---|---|
| 机型与数量 | 零战 18、九九舰爆 18、九七舰攻 18；另搭载第 6 航空隊零战 3 架 | "Her aircraft complement consisted of **18 Zeros, 18 D3As, and 18 B5Ns**. Also aboard were three A6Ms of the 6th Kōkūtai intended as the aerial garrison for Midway." | https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Hiry%C5%AB |
| 出击 | 第一波：18 架 B5N（友永丈市大尉）+ 9 架零战；10:54 第一波反击 18 架 D3A + 6 架零战；13:30 第二波 10 架 B5N + 6 架零战 | "Hiryū's portion of the 108-plane airstrike was an attack on the facilities on Sand Island with 18 torpedo bombers, one of which aborted with mechanical problems, escorted by nine Zeros." | 同上 |
| 损失 | 第一波：2 架被战斗机击落、1 架被高炮击落、1 架迫降库雷环礁、1 架迫降、5 架报废、2 架零战不可用。反击：第一波返航时仅 5 架 D3A + 4 架零战可用；第二波仅 4 架零战 + 5 架 B5N 返航且只 2 架零战 3 架轰炸机可用 | "Two B5Ns were shot down by fighters, with a third falling victim to antiaircraft fire… A fifth B5N was forced to ditch… and five more were damaged beyond repair." / "Of the four Zeros and five B5Ns that returned to Hiryū, only two Zeros and three bombers were still airworthy." | 同上 |

---

## §13 未获取字段汇总（**单列，不得以「0」代替**）

| # | 舰 | 字段 | 状态 | 说明 |
|---|---|---|---|---|
| 1 | 蒼龍 | 装甲总重 | **未获取** | 所有查询来源均未给该舰装甲重量 |
| 2 | 飛龍 | 装甲总重 | **未获取** | 同上 |
| 3 | 蒼龍 | 主炮弹药基数 | **未获取** | NavWeaps 八九式条目：`Shôkaku: 250 rounds / Others: N/A` |
| 4 | 飛龍 | 主炮弹药基数 | **未获取** | 同上 |
| 5 | 蒼龍 | 测距仪（型号/基线长） | **未获取** | 仅查到九四式高射指挥装置，未查到主测距仪参数 |
| 6 | 飛龍 | 测距仪（型号/基线长） | **未获取** | 同上 |
| 7 | 蒼龍 | 弹射器（单舰明确记载） | **未获取** | 无「苍龙未装弹射器」的单舰原文。旁证三条指向日本海军至战争结束都未实用化空母弹射器（§6.1） |
| 8 | 飛龍 | 弹射器（单舰明确记载） | **未获取** | 同上 |
| 9 | 蒼龍 | 机枪以外的近防武器 | — | 11 mm 轻机枪 6 挺有原文，不算未获取 |
| 10 | 飛龍 | 轻机枪 | **未获取** | 飞龙条目未列轻机枪；苍龙的 6 挺不可类推 |
| 11 | 蒼龍 | 战时编制 | **未获取** | 只有平时定员表 |
| 12 | 飛龍 | 战时编制 | **未获取** | 同上 |
| 13 | 飛龍 | 中途岛实载人数 | **未获取** | 日文维基原文即「実員は不明」；信息框「最終時 1,103名」与定员 1,416 名并存，两说并列（见 §D-5） |
| 14 | 蒼龍 | 涂装方案（色号/时间窗） | **未获取** | 只查到「外舷塗装」这一动作描述 |
| 15 | 飛龍 | 涂装方案（色号/时间窗） | **未获取** | 同上 |
| 16 | 蒼龍 | 25 mm 机炮单基弹药数 | **未获取** | — |
| 17 | 飛龍 | 25 mm 机炮单基弹药数 | **未获取** | — |
| 18 | 蒼龍 | 升降机单基载重以外的速度参数 | **未获取** | 仅有 5,000 kg 载重 |
| 19 | 飛龍 | 烟囱尺寸/排气口面积 | **未获取** | 只有「2 座向下排气式」的描述 |
| 20 | 蒼龍 | 烟囱尺寸/排气口面积 | **未获取** | 同上 |
| 21 | 两舰 | 锅炉蒸汽参数（压力/温度） | **未获取** | 未查到原文数值 |
| 22 | 两舰 | 舵机/操舵装置细节 | 部分 | 飞龙「半平衡式单舵」有原文；苍龙「全平衡双舵」有原文；具体参数未获取 |

> 说明：**「未获取」≠「0」**。例如「装甲总重」未获取，不等于 0 t；「弹射器」未获取，也不等于确认无（旁证指向无，但缺单舰原文，故不入正表、只列旁证）。

---

## §D 分歧单列（两边原话都引，不裁决）

### D-1 建设计划编号：「②計画（昭和9年度）」 vs 「1931–1932 Supplementary Program」

- 日方：「計画 昭和9年度（1934年）、**②計画**」——https://ja.wikipedia.org/wiki/蒼龍_(空母)
- 英文维基："Sōryū was one of two large carriers approved for construction under the **1931–1932 Supplementary Program**"——https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB
- Navypedia："Both ships were built under **1st Supplementary Programme of 1931**."——https://www.navypedia.org/ships/japan/jap_cv_soryu.htm

（①計画＝昭和6年度/1931，②計画＝昭和9年度/1934。日文维基与日文造舰史用语一致；英方两源指向 1931。）

### D-2 苍龙第一波机种：九七舰攻 18 架 vs 九九舰爆 18 架

- Combined Fleet TROM（Tully）：「SORYU contributes **eighteen D3A1 "Val"** armed with **Type # 80 land bombs** and nine A6M2 "Zekes."」——https://www.combinedfleet.com/soryu.htm
- 日文维基：「攻撃機は第一航空戦隊は九九艦爆の稼働全18機、**第二航空戦隊は逆に九七艦攻の稼働全18機**を出撃させている。九七艦攻は魚雷ではなく、**800kg陸用爆弾**を搭載しての出撃である。」——https://ja.wikipedia.org/wiki/蒼龍_(空母)
- 英文维基：「Sōryū's part in the 108-plane combined air raid was a strike on the airfield on Eastern Island with **eighteen torpedo bombers** escorted by nine Zeros.」——https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB

（另注：Tully 句内自相矛盾——九九舰爆不挂八〇番 800 kg 陆用弹，该弹是九七舰攻的挂载。此点仅陈述，不裁决。）

### D-3 飞龙沉没时刻（时区换算冲突）

- Combined Fleet TROM（Tully）："at **0912** upended and sank by the bow"（当地时）；同页给出的换算法则是 "To convert to Tokyo (JST) or Zone 9 time, **subtract three hours but advance one one day ahead** of a Midway Local time"。按此法则 6/5 09:12 当地 = **6/6 12:12 JST**。——https://www.combinedfleet.com/hiryu.htm
- 日文维基：「**日本時間6月6日午前6時6-15分**、飛龍は左舷に傾きつつ艦首から沈んでいった」——https://ja.wikipedia.org/wiki/飛龍_(空母)
- Kojinsha Vol.6："At **0510 (0210 Tokyo time**--Ed.), HIRYU is scuttled by MAKIGUMO"（未标日期进位）——https://www.combinedfleet.com/kojinshavolume6.pdf

三者对「自沉 05:10 当地」一致（= 6/6 02:10 JST），但对「沉没」的 JST 换算互不一致：Tully 换算得 12:12 JST，日文维基写 06:06–06:15 JST（相当于当地 03:06–03:15，早于自沉）。**此为我无法调和的分歧，按要求不裁决。**

### D-4 飞龙飞行甲板宽：27.0 m vs 27.4 m

- 日文维基信息框：「飛行甲板 **216.9m x 27.4m**」——https://ja.wikipedia.org/wiki/飛龍_(空母)
- 同一维基正文以外的三源均 27.0：「飛行甲板幅 **27.0**（最大）」（http://vanguard.my.coocan.jp/700contents/hiryu1.htm）；"Breadth, m 22.3 wl **27.0 fd**"（https://www.navypedia.org/ships/japan/jap_cv_hiryu.htm）；"flight deck was **27 meters** wide"（https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Hiry%C5%AB）

### D-5 飞龙乘员数：1,101 / 1,103 / 1,416

- 「計画乗員、**竣工時定員 1,101名**」+「**最終時 1,103名**」——https://ja.wikipedia.org/wiki/飛龍_(空母)
- 「飛龍の定員は准士官以上95名、下士官兵1315名、傭人6名、**計1,416名**である」——同上
- "Her crew consisted of **1,100** officers and enlisted men."——https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Hiry%C5%AB
- 「ミッドウェー海戦時の飛龍に乗り組んでいた**実員は不明**」——同上（日文维基）

（1,101 是竣工定员；1,416 是含傭人与增员的定员表数；中途岛实员不明。三个数不是同一口径，但常被混用，故并列。）

### D-6 飞龙燃油：3,750 t vs 4,400/4,500 t

- 「燃料 重油：**3,750トン**」——https://ja.wikipedia.org/wiki/飛龍_(空母)
- "oil **4400**"——https://www.navypedia.org/ships/japan/jap_cv_hiryu.htm
- "Hiryū carried **4,500 metric tons** (4,400 long tons) of fuel oil"——https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Hiry%C5%AB

### D-7 苍龙燃油：3,400 t vs 3,670/3,730 t

- 「燃料 **3,400トン**」——https://ja.wikipedia.org/wiki/蒼龍_(空母)
- "oil **3670**"——https://www.navypedia.org/ships/japan/jap_cv_soryu.htm
- "Sōryū carried **3,730 metric tons** (3,670 long tons) of fuel oil"——https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB

### D-8 苍龙续航：7,680 vs 7,750 海里

- 「航続距離 **7,680カイリ / 18ノット**」——https://ja.wikipedia.org/wiki/蒼龍_(空母)
- "Endurance, nm(kts) **7750(18)**"——https://www.navypedia.org/ships/japan/jap_cv_soryu.htm
- "a range of **7,750 nautical miles**… at 18 knots"——https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB

### D-9 苍龙装甲口径：40 mm Ducol vs 140〜35 mm NVNC

- "waterline belt of **41 millimeters** of Ducol steel" / "belt: **40**"——https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB ; https://www.navypedia.org/ships/japan/jap_cv_soryu.htm
- 「装甲 舷側：**140〜35mmNVNC鋼**、甲板：**40mmNVNC鋼**」——https://ja.wikipedia.org/wiki/蒼龍_(空母)

（日文维基的 140 mm 应指弹药库段局部，但原文未分段说明。）

### D-10 飞龙舷侧装甲：90 mm vs 48 mm vs 25 mm CNC

- "waterline belt with a maximum thickness of 150 millimeters… that reduced to **90 millimeters** over the machinery spaces and the avgas storage tanks"——https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Hiry%C5%AB
- "belt: **48** (150 abreast magazines)"——https://www.navypedia.org/ships/japan/jap_cv_hiryu.htm
- 「装甲 **機関部舷側 25mmCNC鋼板**」——https://ja.wikipedia.org/wiki/飛龍_(空母)

### D-11 苍龙沉没时刻的记载方式

- Tully：「Sunk: **1912 (1612 JST)** Destroyer ISOKAZE fired three torpedoes」——https://www.combinedfleet.com/soryu.htm
- 日文维基：「日本時間6月5日午後4時13-15分（**現地時間6月4日19時13分**）」——https://ja.wikipedia.org/wiki/蒼龍_(空母)
- 英文维基：「The destroyer reported at **19:15** that Sōryū had sunk」——https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB

三者其实相容（19:12 雷击 / 19:13–19:15 沉没 / 19:15 报告），只是粗细不同，列出备查。

### D-12 苍龙战死人数：711 vs 718 vs 713

- "Losses were **711** crew of her complement of 1,103"——https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB
- 「准士官以上35名、下士官兵683名、**計718名**が戦死」——https://ja.wikipedia.org/wiki/蒼龍_(空母)
- 「plunged to the bottom taking down **713** officers and men」——https://www.combinedfleet.com/soryu.htm

---

## §14 来源清单

| # | 来源 | URL | 用途 | 可信度备注 |
|---|---|---|---|---|
| 1 | Combined Fleet — IJN SORYU: Tabular Record of Movement（Anthony P. Tully, ©2000，Enhanced Edition Nov 2015） | https://www.combinedfleet.com/soryu.htm | 苍龙逐时行动、珍珠港/印度洋/中途岛机数、沉没时刻 | 一手档案整理，价值最高；个别条目有内部矛盾（见 D-2） |
| 2 | Combined Fleet — IJN HIRYU: Tabular Record of Movement（Tully） | https://www.combinedfleet.com/hiryu.htm | 飞龙逐时行动、被弹、自沉、沉没 | 同上 |
| 3 | Warship Profile / Kojinsha Vol.6 "SHOKAKU CLASS, SORYU, HIRYU, UNRYU CLASS, TAIHO"（英译，Takao Ishibashi 等） | https://www.combinedfleet.com/kojinshavolume6.pdf | 舰岛设计决策、拦阻索/防冲网/升降机尺寸、试航数据、命名含义 | 日方技术史译文，工程细节最扎实 |
| 4 | 日文维基 — 蒼龍 (空母) | https://ja.wikipedia.org/wiki/蒼龍_(空母) | 日本口径要目表、定员表、试航成绩、装甲、识别文字存疑 | 二手汇编，逐项标了出处页码，可回溯 |
| 5 | 日文维基 — 飛龍 (空母) | https://ja.wikipedia.org/wiki/飛龍_(空母) | 同上；舰岛设计缘由、G10、定员 1,416 | 同上 |
| 6 | 日文维基 — 赤城 (空母) | https://ja.wikipedia.org/wiki/赤城_(空母) | 赤城左舷舰岛决策链，用于核对「互换」说 | 同上 |
| 7 | 英文维基 — Japanese aircraft carrier Sōryū | https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_S%C5%8Dry%C5%AB | 英制换算值、珍珠港/中途岛机数、战死数 | 二手，引用 Chesneau/Parshall & Tully |
| 8 | 英文维基 — Japanese aircraft carrier Hiryū | https://en.wikipedia.org/wiki/Japanese_aircraft_carrier_Hiry%C5%AB | 同上；左舷舰岛明文、升降机尺寸 | 同上 |
| 9 | japanese-warship.com（大日本帝国軍 主要兵器）— 蒼龍 | https://japanese-warship.com/carrier/soryu/ | 日文技术要目、G6/G8→G9 设计演变、25 mm 布置 | 日文二次整理，注明引用书刊 |
| 10 | japanese-warship.com — 飛龍 | https://japanese-warship.com/carrier/hiryu/ | 飞龙要目、25 mm 3 连 7 基+连 2 5 基、飞行甲板 216.9×27.0 | 同上 |
| 11 | Navypedia — SORYU aircraft carrier (1937) | https://www.navypedia.org/ships/japan/jap_cv_soryu.htm | 主尺度三档、装甲 mm、航空设施面积 | 二手数据库，数值与日方常有出入（已列分歧） |
| 12 | Navypedia — HIRYU aircraft carrier (1939) | https://www.navypedia.org/ships/japan/jap_cv_hiryu.htm | 同上；舰载机年度编制表 | 同上 |
| 13 | NavWeaps — Japan 12.7 cm/40 (5") Types 88 and 89 | https://www.navweaps.com/Weapons/WNJAP_5-40_t89.htm | 八九式高角炮弹道/射速/弹药 | 武器口径权威；明确写「Others: N/A」故弹药基数记未获取 |
| 14 | 日本海軍艦艇入門（PeraOyaji）— 蒼龍、飛龍 | http://nihonkaigun.ikaduchi.com/kuubo/souryuu.html | 两舰对照要目表、原案要求 | 个人站，数值与日文维基/日舰档案一致 |
| 15 | 1/700 作例解説 — 飛龍（開戦時仕様） | http://vanguard.my.coocan.jp/700contents/hiryu1.htm | 两舰差异对照表（舰桥/信号桅/高角炮位/乾舷）、飞行甲板高 12.57 m | 模型考证站，差异表逐项对照实物照片 |
| 16 | 日文维基 — カタパルト | https://ja.wikipedia.org/wiki/カタパルト | 「日本海軍は空母用カタパルトを実用化できなかった」 | 用于弹射器旁证 |
| 17 | 日文维基 — 二式二号電波探信儀一型（21 号电探） | https://ja.wikipedia.org/wiki/二式二号電波探信儀一型 | 雷达装舰时间（中途岛之后）、最早装舰为翔鹤/隼鹰 | 用于雷达时间线 |
| 18 | 日文维基 — 艦名 | https://ja.wikipedia.org/wiki/艦名 | 空母命名规则「特殊名」 | 制度性依据 |
| 19 | JACAR / 戦史叢書 JM-93 "Midway Operations, May–June 1942"（US 战略轰炸调查团日方战史） | https://www.ibiblio.org/hyperwar/Japan/Monos/pdfs/JM-93_MidwayOperations,May-June42/JM-93.htm | 开战时日本海军无舰载雷达；苍龙载 2 架十三试舰爆作侦察 | 日方战后官方战史，雷达时间线的最硬证据 |

### 抓取失败/不可用来源

| 来源 | 状态 |
|---|---|
| japanese-warship.com 图片页、记录写真页 | 未抓取（非数值源） |
| warbirds.jp BBS 问答（赤城/飞龙左舷舰桥讨论） | 论坛贴，仅作线索，未入正表 |
| 各模型厂商/游戏 wiki | 未采用 |

### 附录：本地归档

已抓取的原文 HTML/纯文本存于 `work/raw/txt/`，关键文件：

- `cf-soryu.txt` / `cf-soryu.html` — 苍龙 TROM
- `cf-hiryu.txt` — 飞龙 TROM
- `kojinsha6.pdf` / `kojinsha6.txt` — Kojinsha Vol.6（73 页，241k 字符）
- `wiki-ja-soryu.txt` / `wiki-ja-hiryu.txt` / `wiki-ja-akagi.txt` / `wiki-ja-kanmei.txt` / `wiki-ja-21radar.txt` / `wiki-ja-catapult.txt`
- `wiki-en-soryu.txt` / `wiki-en-hiryu.txt`
- `jws-soryu.txt` / `jws-hiryu.txt` — japanese-warship.com
- `navypedia-soryu.txt` / `navypedia-hiryu.txt`
- `nw-127-89.txt` / `nw-127-89.html` — NavWeaps 12.7 cm
- `nk-soryu-hiryu.txt` — 日本海軍艦艇入門
- `vg-hiryu1.txt` — 1/700 作例对照表
- `jm93-midway.txt` — JM-93 全文

---

## 附：覆盖率统计

统计口径：按任务书 §0–§12 列明的必需字段逐项计数（每舰 70 项），凡正表给了带原文的数值即计「已覆盖」；标【未获取】或「存疑/分歧无定值」计「未覆盖」。

| 舰 | 已覆盖 | 未获取/存疑 | 覆盖率 |
|---|---|---|---|
| 蒼龍 | 62 | 8 | **约 88.6%** |
| 飛龍 | 61 | 9 | **约 87.1%** |

未覆盖项集中在：装甲总重、弹药基数、测距仪、弹射器单舰原文、涂装方案、战时编制、飞龙轻机枪、飞龙中途岛实员（详见 §13）。

分歧条目 12 项（§D-1 ~ §D-12），全部两边原文并列，未做取舍。
