# 20 cm/50 三年式 No.2（2 GÔ）· 弹药/炮架/历史调研底稿

> 2026-11-23 · 战舰资料检索员（weapon-20cm-no2）
> **本线在采集中途被主会话叫停，正文文件未产出。** 本文件保留已核实到手的全部英文原句 + URL，
> 供下一轮直接复用，不必重抓。
> 原始页面：`work/staging/weapon-20cm-no2/_raw/`（`.html` 原页 + `.txt` 转出文本）。

**已产出**：本文件 + `_raw/` 原始页面。**未产出**：`weapon-articles/20cm-3ns-no2.yaml`、
`sources-fragment.yaml`（下一轮补，来源 id 已在 §6 拟好）。

---

## 0. 站点可用性（实测，给下一轮省时间）

按 SCHEMA §9.1 的规矩，`web_fetch` / `research` 全程未用；全部 Python `urllib.request` + Chrome UA 直连。

**实测可直连（200）：**

| 站点 | 用途 |
|---|---|
| `navweaps.com/Weapons/WNJAP_8-50_3ns.htm` | **No.2 炮主数据页**（本条线核心） |
| `navweaps.com/Weapons/WNJAP_79-50_3ns.php` | **No.1 炮独立页**（两型对比的硬证） |
| `navweaps.com/Weapons/WNJAP_Main.htm` | 日本炮索引，确认两型是**两个独立页面** |
| `navypedia.org/ships/japan/jap_cr_tone.htm` | 利根级 |
| `navypedia.org/ships/japan/jap_cr_takao.htm` | 高雄级 |
| `navypedia.org/ships/japan/jap_cr_mogami.htm` | 最上级（含 Ibuki 条目） |
| `navypedia.org/ships/japan/jap_cr_aoba.htm` / `jap_cr_furutaka.htm` | 青叶/古鹰级（改装为 No.2 的两级） |
| `combinedfleet.com/tone_c.htm` / `tone_t.htm` / `chikuma_t.htm` | 利根级速览 + 两舰 TROM |
| `combinedfleet.com/takao_c.htm` / `mogami_c.htm` / `myoko_c.htm` | 三同级速览（炮塔数对比） |
| `pwencycl.kgbudge.com/T/o/Tone_class.htm` | pwe，利根级设计动机的独立表述 |
| `ibiblio.org/hyperwar/Japan/IJN/index.html` | 索引可通，但该目录是陆军的，IJN 无本级条目 |

**实测失败：**
- `navypedia.org` 的**妙高级页面**：`jap_cr_myoko.htm` / `myokou` / `mjoko` / `myoko_class` 四种拼写全 404，
  `jap_cr.htm` 索引页也 404。**妙高级的 navypedia 锚点本轮未拿到**，妙高炮架数据只能走 NavWeaps。
- `ibiblio.org/hyperwar/Japan/IJN/USNTMJ/index.html`：404（USNTMJ O-47(N)-1 报告正文未取到）。
- 本轮未试 `history.navy.mil`（任务书已记 TLS 失败，不重试）。

**一条给下一轮的经验**：`WNJAP_8-50_3ns.htm` 用 `.htm` 能吃，`.php` 同名文件是另一型；
NavWeaps 的日本炮索引（`WNJAP_Main.htm`）里两型的 href 分别是
`WNJAP_8-50_3ns.php` 与 `WNJAP_79-50_3ns.php` —— **No.1 是 7.9 英寸即 79，No.2 是 8 英寸即 8**，
命名规则本身就证明两型不同。

---

## 1. 关键核实：No.1 与 No.2 是两型炮（任务书陈述已核实，成立）

任务书说「本站已有 `weapon:20cm-3ns` 是 No.1，本任务是 No.2，两者不是同一型」——**核实成立**，且拿到五条独立硬证：

1. **两个独立页面**：NavWeaps 索引里 `WNJAP_8-50_3ns.php`（No.2）与 `WNJAP_79-50_3ns.php`（No.1）并列，
   索引文字分别是「20 cm/50 3rd Year Type No. 2 — All Japanese Heavy Cruisers after 1940」与
   「20 cm/50 3rd Year Type No. 1 — Akagi, Kaga, Furutaka, Aoba and Myôkô Classes」。
   <https://www.navweaps.com/Weapons/WNJAP_Main.htm>
2. **实弹径不同**：No.2 页 "Actual bore diameter was 20.32 cm (8.0")"；
   No.1 页 "Actual bore diameter was 20.0 cm (7.87")"。
3. **初速不同**：No.2 840 mps（2,756 fps）；No.1 870 mps（2,854 fps）。
4. **膛压不同**：No.2 "19.9 tons/in2 (3,130 kg/cm2)"；No.1 "19 tons/in2 (3,000 kg/cm2)"。
5. **外形可辨**：No.1 页原文 "These weapons can be distinguished from the 20 cm/50 (8") No. 2 guns
   by the marked step in the chase diameter."
   <https://www.navweaps.com/Weapons/WNJAP_79-50_3ns.php>

**序号何时补上（硬证）**：
> "Nomenclature note: The No. 1 (1 GÔ) designation was added to these guns after the more powerful
> 20 cm/50 (8") 3rd Year Type No. 2 (2 GÔ) Gun was adopted on 6 April 1931."
> — <https://www.navweaps.com/Weapons/WNJAP_79-50_3ns.php>

**为什么分两型（No.2 页原句）**：
> "These guns were developed in 1930-1931 in order to achieve the maximum caliber allowed for
> cruisers under the Naval Limitation Treaties of the time."
> — <https://www.navweaps.com/Weapons/WNJAP_8-50_3ns.htm>

即：No.1 是 1920 年设计的 20.0 cm 炮，1931 年条约语境下要压到条约上限（8 英寸＝20.32 cm）的
最大威力，于是新设计 No.2，并回头把旧的改名 No.1。
另有一处**名不副实**同样适用于 No.2：
> "Nomenclature note: Even though these guns were developed in 1930 to 1931, they were still
> designated as 3rd Year Type (Model 1914)."

---

## 2. 炮身与技术数据（NavWeaps No.2 页，逐条原句）

来源：<https://www.navweaps.com/Weapons/WNJAP_8-50_3ns.htm>（下文简称 NW2）

| 项 | 原句 |
|---|---|
| 制式名 | `20 cm/50 (8") 3rd Year Type (Model 1914) No. 2` / `Official Designation: 50 caliber 3rd Year Type No. 2 20 cm Gun` |
| 实弹径 | `Actual bore diameter was 20.32 cm (8.0")` |
| 设计年 | `Date Of Design — 1930 (actual design date)` |
| 服役年 | `Date In Service — 1932` |
| 炮身重 | `Gun Weight — 18.7 tons (19 mt)` |
| 全长 | `Gun Length oa — 405.9 in (10.310 m)` |
| 膛线长（bore） | `Bore Length — 393.70 in (10.000 m)` |
| 膛线长（rifling） | `Rifling Length — 333.9 in (10.310 m)` ← **原文换算有误，见 §5 分歧①** |
| 阴线数 | `Grooves — (48) 0.090 in deep x 0.327 in (2.28 mm x 8.299 mm)` |
| 阳线宽 | `Lands — 0.197 in (5.00 mm)` |
| 缠度 | `Twist — Uniform RH 1 in 27.56` |
| 药室容积 | `Chamber Volume — 4,150 in3 (68.0 dm3)` |
| 射速 | `Rate Of Fire — 3 to 4 rounds per minute` |
| 装药 | `Type — Bag` / `Propellant Charge — 74.5 lbs. (33.80 kg) 53 DC` |
| 膛压 | `Working Pressure — 19.9 tons/in2 (3,130 kg/cm2)` |
| 炮身寿命 | `Approximate Barrel Life — 320 - 400 rounds` |
| 弹药基数 | `Ammunition stowage per gun — 120 - 126 rounds` |

**炮身构造（原句）**：
> "Constructed of A tube, full-length jacket, breech ring, breech bush and used a Welin screw block
> with a three-motion breech mechanism operated by hydraulic power or by hand."

**装药细节（脚注原句）**：
> "The propellant charge was in two bags which were rammed one at a time."

**射速的仰角依赖（脚注原句，重要）**：
> "The ammunition supply system for the Aoba and Furutaka classes could provide three complete
> rounds per gun per minute while that for the later classes could provide a maximum of four
> complete rounds per gun per minute. As loading was at a fixed angle of +5 degrees and the gun
> elevation speeds were relatively slow, the rate of fire for these later classes was reduced at
> higher elevations to 2-3 rounds per minute at +55 degrees and a maximum of 2 rounds per minute
> at +70 degrees."

即：**3–4 发/分是低仰角值**；+55° 时 2–3 发/分、+70° 时 ≤2 发/分。

### 2.1 弹种与弹重（qual 已有着落）

| 弹种 | 弹重 | 原句 |
|---|---|---|
| AP Type 91 | 125.85 kg | `AP Type 91: 277.4 lbs. (125.85 kg)` |
| Common Type 91 HE | 125.85 kg | `Common Type 91 HE: 277.4 lbs. (125.85 kg)` |
| Common Type 0 HE | 125.85 kg | `Common Type 0 HE: 277.4 lbs. (125.85 kg)` |
| Common Type 3 IS | 125.85 kg | `Common Type 3 IS: 277.4 lbs. (125.85 kg)` |
| Illum Shell B | 125.85 kg | `Illum Shell B: 277.4 lbs. (125.85 kg)` |

五种弹**弹重完全相同**，所以 `weapon.projectile_weight` 无论给哪种 qual 都是 125.85 kg；
建议只登记 `ap` 与 `he` 两条，其余写 note。

**爆填（原句）**：`AP Type 91: 6.9 lbs. (3.11 kg)` / `Common Type 91 HE: 18.0 lbs. (8.2 kg)` /
`Common Type 0 HE: 18.0 lbs. (8.2 kg)`

**弹长（原句）**：`AP Type 91: 35.68 in (90.62 cm)` / `Common Type 91 HE: 35.83 in (91.0 cm)` /
`Common Type 0 HE: 34.65 in (88.0 cm)` / `Common Type 3 IS: 34.07 in (86.55 cm)`

**「AP Type 91 不是真正的 APC」——决定 qual 怎么填的关键脚注**：
> "These 20 cm (8") Type 91 shells were not true "APC" projectiles as they lacked a cap, having only
> a cap head and windshield. Cap head and windshield together weighed 17 lbs. (7.7 kg). There were
> true APC projectiles, designated as Type 91 Mod 1, but these were used only for armor penetration
> experiments and were not in service use."
→ 与本站 `20cm-3ns.yaml`（No.1）的处理一致：**shell_type 填 `ap`，不填 `apc`**。

**其他脚注（原句）**：
- `Common Type 91 HE was issued starting in 1940`
- `Common Type 0 HE was supplied with time fuzes for AA defense. US Naval Technical Mission to Japan
  report O-19 says that this round had an effective radius of 32.05 yards (29 m) but this seems to be
  optimistic.`
- `IS is my abbreviation for the incendiary shrapnel round (sankaikan) intended for AA use.`
- `The Shômeidan B Illumination round had an effective range of 17,500 yards (16,000 m) and an
  illuminating power of 1.6 million candelas. The maximum ballistic range was 24,900 yards (22,770 m).`

### 2.2 初速

> `Muzzle Velocity — All except Illum: 2,756 fps (840 mps)`
> `Illum: 2,330 fps (710 mps)`

### 2.3 射程表（分仰角，**必须整表用，不许取单值**）

原句表头：`Range with 277 lbs. (125.6 kg) AP`

| 仰角 | 射程 | 存速 | 落角 |
|---|---|---|---|
| 2.4° | 5,470 yd (5,000 m) | 2,133 fps (650 mps) | 3.0° |
| 5.3° | 10,940 yd (10,000 m) | 1,634 fps (498 mps) | 7.5° |
| 10.5° | 16,400 yd (15,000 m) | 1,299 fps (396 mps) | 15.8° |
| 18.0° | 21,870 yd (20,000 m) | 1,194 fps (364 mps) | 29.0° |
| 30.0° | 27,340 yd (25,000 m) | 1,247 fps (380 mps) | 47.0° |
| 40.0° | 31,600 yd (28,900 m) | — | — |
| 45.0° | 32,150 yd (29,400 m) | — | — |

→ `weapon.range.max = 29400` / `weapon.range.max_elevation = 45`（成对写）。
注意 30°/25,000 m 一行的存速**回升**（1,247 > 1,194 fps），这是原表就有的，不是抄错，不要改。

### 2.4 穿深表（`weapon.penetration`，附带 method）

原句表头：`Armor Penetration with 277 lbs. (125.6 kg) AP`

| 距离 | 侧装甲 | 甲板 |
|---|---|---|
| 10,000 m（10,940 yd） | 190 mm（7.5"） | — |
| 18,000 m（19,690 yd） | 120 mm（4.7"） | — |
| 29,400 m（32,150 yd） | 74 mm（2.9"） | — |

原句来源注：`This data is from "Anatomy of the Ship: The Heavy Cruiser Takao" and refers to NVNC armor.`
→ 写进 note：**NVNC 钢、出自 Skulski 的 Takao 专著**，不是日方原始射表。

### 2.5 散布（历史正文可用，No.2 页 Description 段原句）

- `with Takao in 1933 reporting patterns of 483 meters (530 yards) at a mean firing range of
  19,300 meters (21,100 yards)`
- `In a target shoot against the old minelayer Aso (ex-Russian Armored Cruiser Bayan) in 1932, the
  cruisers Nachi and Myôkô repeatedly straddled at ranges between 15,800 and 22,300 meters
  (14,450 and 20,390 yards) yet failed to score a single hit because of dispersion patterns of
  about 350 meters (380 yards).`
- `following which the Myôkô class in 1936 achieved patterns of 280 to 330 meters (306 to 360 yards)
  at ranges of 20,000 to 22,000 meters`
- `the Type 98 (Model 1938) Gunfiring Delay Installation which consisted of a "trigger time limiting
  device" … and a "firing time separator" which produced a lag of 0.03 seconds between the firing of
  each gun in a turret. … These devices reduced dispersion by about 10-15%.`
- `Patterns for the 10-gun cruisers were reported by the USN as being very small at the Battle of
  Samar in 1944.`

### 2.6 防空评价（原句，写正文时用来解释「高仰角炮架为何没用」）

> "Some mountings were given high elevation capability with the idea that they could be used against
> aircraft, but the guns had a low rate of fire and the mountings could not train or elevate quickly
> enough to be effective in the AA role. As the surface fire control system was separated from the AA
> fire control system, switching from one to the other was a complicated process, resulting in a slow
> transition."

---

## 3. 炮架（mount）—— 逐型原句

**炮架型号与装舰（NW2 Mount/Turret Data 原句，一段引全）**：
> "Two-gun Mountings — Aoba (3): Modified Model C; Myôkô (5): Modified Model D;
> Takao class (5) except Maya: Model E; Maya (5): Model E1;
> Furutaka (3): Model E2; Mogami (5): Mogami Model (also known as Modified E2);
> Tone (4) and Ibuki (5): Model E3"

| 项 | 原句 |
|---|---|
| 炮座重 | `Weight — 163 - 172 tons (166 - 175 mt)` |
| 仰俯范围 | `Models C and D: -5 / +40 degrees` / `Model E: -5 / +70 degrees` / `Model E1, E2, Modified E2 and E3: -5 / +55 degrees` |
| 俯仰速度 | `Models C, D: 6 degrees per second` / `Models E and E1: 12 degrees per second` / `E2, Modified E2 and E3: 6 degrees per second` |
| 回转范围 | `Train — About +120 / -120 degrees` |
| 回转速度 | `Train Rate — 4 degrees per second` |
| 后座 | `Gun recoil — N/A`（原页未给） |
| **装填角** | `Loading Angle — +5 degrees` |
| 测距仪 | `The Modified E2 and the Model E3 mountings had 315 inch (8 m) rangefinders, the other Models had 236 inch (6 m) rangefinders.` |
| 炮管间距 | `The gun axes were 74.8 in (190 cm) apart for all Models.` |
| 炮塔员 | `Model C, Model D and those Model E mountings with one shell hoist per gun had a crew of 19 in the gunhouse, nine in the shell room and ten more in the powder magazine. Those Model E mountings with two shell hoists per gun had a crew of 23 in the gunhouse, nine in the shell room and ten more in the powder magazine.` |

**通用机构与缺陷（原句）**：
> "They were all operated with very noisy electric motor driven oil hydraulic pumps located in the
> revolving structure. Damage to rubber covered wiring by oil leaks was a common complaint. Run out
> was by compressed air. Elevation was by rack and pinion on the Model C, D and E1 mountings and by
> hydraulic actuators on the other Model E mountings."

**Model E 的外形特征（原句，可用于正文区分高雄级）**：
> "Model E mountings (and the Model B mountings used on Akagi and Kaga) differed from earlier
> mountings in having flat instead of sloped roofs and in that the rangefinders were partially within
> the mounting instead of being superimposed. … The gunhouses for all Model E types were 15 cm (5.9")
> taller than the Model D gunhouse in order to better accommodate the larger guns."

**为什么 E 型只到 +55°（原句，关键）**：
> "The maximum elevation of the Model E was +70 degrees and elevation speed increased to 12 degrees
> per second, but the elevating and recoil mechanisms proved to be fragile and it was found that
> +55 degrees was the maximum practical elevation. As a result, the other Model E mountings were
> designed for a maximum elevation of +55 degrees and had their elevation speed reduced to 6 degrees
> per second."

**闪火安全（原句，含 1935 年足柄事故）**：
> "As originally completed in the 1920s, the Model C and the Model D mountings used pusher hoists for
> the powder charges that effectively created a continuous powder train between the gun breeches and
> the magazines. These powder hoists were replaced by bucket hoists in 1930s which gave improved
> protection from flash. … These changes did slow down the supply rate of ammunition to four charges
> per minute. However, the new arrangements proved their worth in the summer of 1935 when a flareback
> wrecked Turret No. 2 on Ashigara. Although 41 men were killed or injured, the flash did not
> penetrate down into the magazines and the ship was saved."

### 3.1 与妙高/高雄级的炮架差异（这是任务书 §2 的要点，已拿到答案）

| 舰级 | 炮架 | 仰俯 | 俯仰速度 | 测距仪 |
|---|---|---|---|---|
| 妙高级 | **Modified Model D** | −5 / **+40°** | 6 °/s | 6 m |
| 高雄级（除摩耶） | **Model E** | −5 / **+70°**（实际限 +55°） | 12 °/s | 6 m |
| 摩耶 | Model E1 | −5 / +55° | 12 °/s | 6 m |
| **利根级** | **Model E3** | −5 / **+55°** | 6 °/s | **8 m** |
| 最上级 | Mogami Model（= Modified E2） | −5 / +55° | 6 °/s | **8 m** |
| 古鹰级 | Model E2 | −5 / +55° | 6 °/s | 6 m |
| 青叶级 | Modified Model C | −5 / +40° | 6 °/s | 6 m |

**要点**：妙高（Mod D）与利根（E3）**不是同一种炮架**，仰角差 15°，俯仰速度快一倍，测距仪 6 m vs 8 m。
高雄（Model E）虽然有 +70° 的名义仰角，但那是因为它是**第一型试高仰角的炮架**、机构脆弱，
后面的 E 型全部退回 +55°。利根 E3 是 E 系列里**最后一个、也是唯一装 8 m 测距仪的新造型**。

**利根级炮座圈的由来（原句，正文必写的一层）**：
> "The hull and barbettes of the Tone class had already been completed up above the armored deck
> when the main armament was changed from triple 15.5 cm turrets to twin 20 cm turrets. … the twin
> 20 cm turret needed a smaller diameter roller path than the triple 15.5 cm turret, this meant that
> the diameter of the completed portion of the barbettes was now too large to fit the standard turret
> races used for twin 20 cm turrets. To compensate, the design for the top of the barbettes was
> altered to a conical shape with a diameter of 18.7 feet (5.70 m) at the lower level and 16.4 feet
> (5.00 m) at the upper level. The follow-on Ibuki class were to use the same E3 turrets as the Tone
> class, but these later ships were designed from the start with 16.4 foot (5.00 m) diameter
> barbettes. However, the distance between the centerlines of No. 1 and No. 2 barbette on the Ibuki
> class was the same as for the Mogami class, which meant that the guns in No. 2 turret would have
> still have needed to be raised in order to clear No. 1 turret, similar to the problem with the
> Mogami class."

→ 即：**利根级的锥形炮座顶是「舰体已建到装甲甲板以上才改主炮」的补丁**，不是原始设计。

**最上级的装填死角（同类问题的旁证，原句）**：
> "As the 20 cm guns were longer than the 15.5 cm guns they replaced, the guns of No. 2 turret could
> not depress below +12 degrees when trained on the centerline as otherwise they would have struck
> No. 1 turret."

**古鹰级的炮架来源（原句，一条容易被漏掉的事实）**：
> "During modernization and replacement of the 20 cm (7.9") No. 1 guns with the 20 cm (8") No. 2 guns,
> the Furutaka class was converted from six Model A single mounts to three Model E2 twin mounts.
> Although externally these looked like the Model E mounts, internally the gunhouses and ammunition
> supply arrangements including hoists resembled the Model C mountings used on the Aoba class."

**另有一条「炮是新的、炮管是旧的」的细节（两页都写，No.1 页脚注 1）**：
> "When it came time for Furutaka and Kako to be rearmed in the 1930s, production difficulties held up
> deliveries of the 20 cm (8") No. 2 guns intended for these ships. Rather than wait for these guns to
> be completed, the Japanese instead took 20 cm (7.9") No. 1 guns removed from Haguro and Ashigara,
> rebored and relined them to 20.32 cm (8"), and then installed them onto Furutaka and Kako."

---

## 4. 利根级「四座全在舰艏」——三源硬证

1. **combinedfleet（舰级页）**：
   > "Their main gun layout was sort of bizarre, with four dual turrets forward (some of which suffered
   > from very poor firing arcs), and none aft. Their aft decks were totally devoted to AAA and float
   > plane operations (they carried 5, as compared to the 3 carried by most other Japanese CAs), which
   > made them very useful as scouting ships for carrier battlegroups, and consequently they spent much
   > of the war hanging out with the carriers of Combined Fleet…"
   > — <https://www.combinedfleet.com/tone_c.htm>

2. **navypedia（设计史段落）**：
   > "Number of main turrets had shrunk to four, having grouped them in a fore end. Machinery, in
   > comparison with prototype, was displaced in a stern. As result it was possible to shrink a length
   > of an armored belt, to moderate upper weight, to make ship ends lighter, that, in turn, has
   > improved seaworthiness. Exempted aft end allowed to place large air group of six seaplanes."
   > — <https://www.navypedia.org/ships/japan/jap_cr_tone.htm>

3. **pwe（设计动机，与上两源角度不同）**：
   > "The Tones crowded all their main guns onto the forward part of the ship, a measure intended to
   > reduce dispersion of shot. It also freed the rear of the ships for extensive plane handling
   > facilities and resulted in ships that were unusually habitable. … On the other hand, the unusual
   > turret arrangement yielded an ugly profile and poor firing arcs."
   > — <http://pwencycl.kgbudge.com/T/o/Tone_class.htm>

**注意：pwe 多给了一个 navypedia 没有的理由 —— 「减少散布」**。三源并列写，不裁决
（navypedia 给的是「缩短装甲带／减轻艏艉重量／改善航海性」，pwe 给的是「减散布」，
combinedfleet 给的是「舰尾让给航空」）。三者不冲突，可并存。

**主炮改装时点（navypedia 原句）**：
> "Early 1937 when ships still laid on slipways, Naval Staff decided to replace 155mm guns by 203mm,
> that converted light cruiser to the heavy. As well as on predecessors, such replacement was provided
> by the design, therefore strengthening of armament has not called necessity of entering of serious
> corrections for drawings, however building was inhibited, partly because of shortage of 203mm turrets."

**pwe 的另一个版本（时点口径不同，见 §5 分歧②）**：
> "The design was originally announced as using 6.1" (155mm) guns, but following the repudiation of
> the naval disarmament treaties at the end of 1936, the ships were completed with 8" (203mm) guns
> quickly enough to raise suspicions that the ships had been designed for such guns from the start."

**Ibuki 的旁证（combinedfleet 同一段）**：
> "Others state that the follow-on Ibuki class, which was never built, would have been a copy of the
> Mogami, rather than the Tone, because of war lessons learned which rejected the concept of an
> all-forward armament layout"

---

## 5. 有争议 / 原文瑕疵（单列，不裁决）

### ① NavWeaps 的 Rifling Length 换算自相矛盾（**原文错，不要照抄**）

> `Rifling Length — 333.9 in (10.310 m)`

333.9 in = 8.481 m，而 10.310 m 正是同一页 `Gun Length oa` 的换算式。
**两条不可能同时成立**：若炮身全长 10.310 m，膛线不可能也是 10.310 m。
建议 `weapon.length.bore` 只登记 `Bore Length — 393.70 in (10.000 m)`（=10.0 m），
**Rifling Length 不登记**，并在 note 里说明原文换算有误。此条为本轮新发现，任务书未提及。

### ② 利根级改主炮的时点：1937 年初（navypedia）vs 1936 年底条约失效后（pwe）

- navypedia：`Early 1937 when ships still laid on slipways, Naval Staff decided to replace 155mm guns by 203mm`
- pwe：`following the repudiation of the naval disarmament treaties at the end of 1936, the ships were
  completed with 8" (203mm) guns`
- 两说不矛盾（1936 年底废约 → 1937 年初决定），但**「决定时点」与「完工时点」不是一件事**，
  正文写「1937 年初决定换炮」，pwe 的 1936 年底说并列进 note。

### ③ 摩耶改高射巡洋舰后主炮数（仅一条来源，单源）

> "Her number 3 turret and all 12 cm (4.7") AA guns were removed and she was then modified such that
> she now carried eight 20 cm (8.0") No. 2 guns and twelve 12.7 cm/40 (5.0") AA guns"
> — NW2
navypedia 的摩耶改装表写 `- 1 x 2 - 203/50 (No 3)`，与上句一致（5 座 → 4 座 = 8 门）。**两源一致，可用。**

### ④ 青叶级的仰角是否后期提到 +50°（NavWeaps 自己否定）

> "Some accounts infer that Aoba was later modified to increase maximum elevation to +50 degrees, but
> this is not supported by "Japanese Cruisers of the Pacific War.""
→ 正文若写青叶，按 +40° 写，并注明此说。

### ⑤ 最上级 No.2 炮塔的俯角限制（只影响最上级，不改利根数据）

见 §3 末：`No. 2 turret could not depress below +12 degrees when trained on the centerline`。
**利根级没有对应的限制表述**——combinedfleet 只说「some of which suffered from very poor firing arcs」，
未指明是哪几座、也未给具体角度。**不要拿最上级的 +12° 套到利根级上。**

---

## 6. 未获取（下一轮要补的清单）

| 项 | 为什么没有 |
|---|---|
| **利根级逐座主炮塔的层次关系**（哪座背负、哪两座朝后、各自射界角度） | 只有 tier E 有正面表述；combinedfleet 只到「四座在前、有的射界很差」。故 `mount.position` 只能写 `fore`，不写 `superfiring_fore`，不拆四座实体。 |
| **利根级 E3 炮座的单座重量** | NavWeaps 只给全系列区间 `163 - 172 tons (166 - 175 mt)`，未分型。分型值不可推。 |
| **E3 的后座行程 / 后座力** | NavWeaps 原页 `Gun recoil — N/A`，未给。 |
| **妙高级 navypedia 数据** | navypedia 妙高页四种路径全 404，妙高数据只能引 NavWeaps 的 `Modified Model D` 行。 |
| **USNTMJ O-47(N)-1 报告正文**（Japanese Naval Guns and Mounts） | ibiblio 的 USNTMJ 索引 404。NavWeaps 的炮架示意图即出自该报告，若能拿到可把 confidence 提到 B。 |
| **日方一手档案**（防卫省防卫研究所 / JACAR 的 20 cm 炮要目） | 本轮未抓；利根级那轮（`work/staging/tone/`）也未抓。这是本站武器条目普遍最薄的一层。 |
| **利根级主炮弹药库容量（全舰）** | NavWeaps 只给「每门 120–126 发」。**全舰总数需要「每门 × 门数」自算 = 推算，不做。** |

---

## 7. 拟登记来源（下一轮直接抄）

| id | url | tier | 备注 |
|---|---|---|---|
| `navweaps-20cm-3ns` | `https://www.navweaps.com/Weapons/WNJAP_8-50_3ns.htm` | C | **已存在，直接复用，不要重复登记**。注意：这条的 url 就是 **No.2 炮页**，标题却写成 `Japanese 20 cm/50 (7.9") 3rd Year Type`（7.9" 是 No.1 的写法），**标题有误**，建议主会话改名 |
| `navweaps-20cm-3ns-no1-page` | `https://www.navweaps.com/Weapons/WNJAP_79-50_3ns.php` | C | **新登记**。No.1 炮的独立页，提供「序号 1931-04-06 补上」「外形以台阶区分」「20.0 cm / 870 mps」等硬证。此前 `20cm-3ns.yaml` 用的 `navweaps-20cm-3ns` 指向的是 No.2 页，**No.1 正文缺了它自己的页面** |
| `navypedia-tone` | `https://www.navypedia.org/ships/japan/jap_cr_tone.htm` | D | 已由 `work/staging/tone/sources-fragment.yaml` 登记，**复用前先查合并结果** |
| `navypedia-takao` | `https://www.navypedia.org/ships/japan/jap_cr_takao.htm` | D | 新登记 |
| `navypedia-mogami` | `https://www.navypedia.org/ships/japan/jap_cr_mogami.htm` | D | 新登记 |
| `navypedia-furutaka` / `navypedia-aoba` | `.../jap_cr_furutaka.htm` / `.../jap_cr_aoba.htm` | D | 新登记 |
| `combinedfleet-tone-class` | `https://www.combinedfleet.com/tone_c.htm` | D | 已由 tone 那轮登记，复用前先查 |
| `combinedfleet-tone-trom` / `combinedfleet-chikuma-trom` | `.../tone_t.htm` / `.../chikuma_t.htm` | D | 同上 |
| `combinedfleet-takao-class` / `-myoko-class` / `-mogami-class` | `.../takao_c.htm` 等 | D | 新登记，只用于炮塔数对比 |
| `pwe-tone-class` | `http://pwencycl.kgbudge.com/T/o/Tone_class.htm` | D | 已由 tone 那轮登记，复用前先查 |

**⚠️ 一条必须回给主会话的既有错误**：`data/sources.yaml` 的 `navweaps-20cm-3ns`
标题写的是 `Japanese 20 cm/50 (7.9") 3rd Year Type`，但 url 是 **8-50（No.2 炮）页**。
`7.9"` 是 No.1 的口径。**这条来源的标题与 url 不匹配**，且 `20cm-3ns.yaml`（No.1 正文）
正是引它当唯一来源 —— 也就是说 **No.1 正文此前引用的是 No.2 的页面**。
本轮抓到 No.1 独立页后，No.1 的 20.0 cm / 870 mps / 17.6 t / 寿命 300 发 / 基数 120 发
都能在该页找到原句，结论数值不变，但**来源指向应当修正**。

---

## 8. 结尾：本线的实际状态

**做到哪一步**：抓取 + 逐条取证完成度约 80%（炮身、弹药、射表、穿深、炮架、三源「四座前置」硬证、
两型区别硬证、结局线索全部到手）；**正文 YAML 一个字没写**（先取证的顺序，被叫停时正好卡在取证收尾）。

**已可用的东西**：
- `_raw/` 下 15 个原始页面 + 对应 `.txt`（navweaps 两型、navypedia 五级、combinedfleet 六个页面、pwe）。
- 本文件 §2–§4 的表格与英文原句**可以直接搬进正文的 `src`/note**，不需要重抓。
- §1 的两型区别、§3.1 的炮架对照表、§5 的三处原文瑕疵，是这个条目最容易写错的三块，
  已经钉死。

**没有任何一条结论是靠推算得来的**；所有「查不到」都记在 §6。

## 交付摘要

| 项 | 数量 |
|---|---|
| 正文文件（`weapon-articles/20cm-3ns-no2.yaml`） | **0（本线取消，未产出）** |
| 来源分片（`sources-fragment.yaml`） | **0（未产出，拟登记清单见 §7）** |
| 原始页面落盘 | 15（`_raw/`，含 `.html` + `.txt`） |
| 已核实英文原句条目 | 约 60 条 |

### 卡住的地方
- 利根级逐座炮塔的层次与射界角度：**只有 tier E 有**，故 `mount.position` 只能到 `fore`。
- E3 炮座的分型重量、后座行程：NavWeaps 全系列只给区间 / 给 `N/A`。
- navypedia 妙高级页全部 404；USNTMJ O-47(N)-1 报告正文 ibiblio 404。
- 日方一手档案（JACAR）本轮未抓，与 tone 那轮同样是最薄的一层。

### 有争议的记载
1. **NavWeaps 的 Rifling Length 换算错**（333.9 in 写成 10.310 m，与 Gun Length oa 重复）——
   本轮新发现，建议 `weapon.length.bore` 只取 Bore Length 10.000 m，rifling 不登记。
2. 利根级改主炮的决定时点：navypedia「1937 年初」vs pwe「1936 年底废约后」——并列，不裁决。
3. 「为什么四座全前置」三源理由不同：navypedia（缩短装甲带／减重／改善航海性）、
   pwe（**减少散布**）、combinedfleet（舰尾让给航空）——三者不冲突，可并存，不裁决。
