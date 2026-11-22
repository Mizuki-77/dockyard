# 调研底稿 —— g7-weapons（4 型英国海军武器正文）

> 调研日期 2026-11-22 · 执行 subagent：g7-weapons
> 产出目录：`work/staging/g7-weapons/`
> 未改动 `data/` / `src/` / `public/` / `docs/` 下的任何文件。

---

## 0. 抓取清单

| 来源 id | 实际抓取 URL | HTTP | 字节 | 落盘 | 状态 |
|---|---|---|---|---|---|
| `navweaps-8in-50-mk8` | `http://www.navweaps.com/Weapons/WNBR_8-50_mk8.php` | 200 | 40,544 | `_raw/8in-50-mk8.html` | 直连成功 |
| `navweaps-6in-50-mk23` | `http://www.navweaps.com/Weapons/WNBR_6-50_mk23.php` | 200 | 55,145 | `_raw/6in-50-mk23.html` | 直连成功 |
| `navweaps-45in-45-mk1` | `http://www.navweaps.com/Weapons/WNBR_45-45_mk1.php` | 200 | 60,868 | `_raw/45in-45-mk1.html` | **直连成功，未加 `-L`、未走代理** |
| `navweaps-4-7in-45-mk12` | `http://www.navweaps.com/Weapons/WNBR_47-45_mk12.php` | **404** | — | — | 换页，见 §2.1 |
| `navweaps-4-7in-45-mk12` | `http://www.navweaps.com/Weapons/WNBR_47-45_mk9.php` | 200 | 56,440 | `_raw/4-7in-45-mk12.html` | 实际数据页 |

HTML→文本用 `_raw/h2t.py`（自写，剥标签 + 反转义 + 压空行），产物为同名 `.txt`。

---

## 1. 逐条结论（英文原句 + URL）

### 1.1 `8in-50-mk8` — 8"/50 (20.3 cm) Mark VIII
来源页：https://www.navweaps.com/Weapons/WNBR_8-50_mk8.php

**装舰 / 服役年份**
> "Ship Class Used On | Kent, London, Norfolk and York classes / RAN Australia class (modified Kent)"
> "Date Of Design | 1923" / "Date In Service | 1927"

**设计缘由与高射角**
> "This weapon was designed for Britain's Treaty Cruisers of the 1920s. Similar to other cruisers of that era, the mountings for these weapons were given a high maximum elevation in order to provide an anti-aircraft capability. However, the training and elevation gear was inefficient and both the elevation and training rates were too slow to allow these mountings to be useful in that role."

**早期炮座的问题与处理**
> "The complex nature of the early versions of these mountings, the Mark I and Mark I\*, gave trouble for a number of years. Considerable attention was paid to these faults, especially in 1927 and 1928, before these ships were accepted into service. After the initial trials, the training and elevation rates were reduced prior to commissioning and reduced still further during the 1930s..."

**1938 年伦敦号的抱怨（开战前一年）**
> "HMS London reported as late as June 1938 that 'one would wish that the 8in mountings and torpedoes would behave as they should. The prolonged firing of 20 rounds per gun from London was a disappointment on the material side.'"

**Mark II 的可靠性 / 约克号试验**
> "The later Mark II mountings appear to have been much more reliable, with the first gun trials for HMS York in February 1930 being so successful that they took only four hours to complete."

**诺福克号对俾斯麦的 527 发，以及「X」炮塔右炮只打 8 发**
> "The Mark II was also successful in the battle with Bismarck in May 1941. During this battle, HMS Norfolk in about 90 minutes fired 527 rounds with minor problems, although the right gun in 'X' turret only fired eight rounds (compared to 103 rounds from the right gun in 'B' turret), probably because of double ramming of the cordite charges."
> "Her Commander, Capt. A.J.L. Phillips reported: 'For 8in Mark II mountings, the final state of affairs and the percentage output are considered most satisfactory.'"

**1929-07-26 德文郡号爆炸**
> "On 26 July 1929, HMS Devonshire suffered a misfire with the left gun in 'X' turret. A crewman, unaware of the issue, opened the breech too soon and the inrush of oxygen set off the charges. One shell and a number of cordite bags were ignited, blowing off the turret roof and killing one officer and seventeen crewmen. The investigation into the accident found that the 'interlock' (salvo latch) for this gun had been incorrectly assembled... Fortunately, the flash protection of the mounting had prevented the explosion from penetrating down into the magazine. The burned-out turret was removed and replaced with a spare and Devonshire was back in commission by January 1930."

**诺福克号「X」炮塔 1943-12 受损 / 1944-08 装回**
> "'X' turret on HMS Norfolk was also removed for repairs after being badly damaged in her fight with Scharnhorst in December 1943. It was reinstalled in August 1944, although her other repairs took until November to complete."

**炮座重量（预估 vs 完工）**
> "Original Estimate — Mark I: 155 tons (157 mt) ... Mark II: 168.8 tons (172 mt)"
> "As Completed — Mark I: 205 tons (226 mt) ... Mark II: 220.3 tons (242 mt)"

**超重的后果（条约舰）**
> "The estimated versus actual weights of these mountings show the difficulties involved during the design phase in correctly computing weight. As these were Treaty-limited warships, these overruns for the main armament had to be compensated for by taking weight out of other areas, such as reducing the number of hull scantlings. It was originally hoped that the Mark II mounting would be much lighter than the Mark I, but the reverse turned out to be the case."

**Mark II\*（仅埃克塞特号）降仰角**
> "As a weight saving measure, the Mark II\* version of this mounting, used only on HMS Exeter, had a significantly reduced maximum elevation." → 数值：`Mark I, I* and II: -3 / +70 degrees / Mark II*: -3 / +50 degrees`

**主要参数（正文用了这些）**
| 项 | 值 |
|---|---|
| 炮重 | Mk VIII/VIII\*: 38,528 lbs (17,476 kg)；Mk VIII\*\*: 38,640 lbs (17,527 kg) |
| 身管全长 | 413.1 in (10.493 m) |
| 膛线长 | 346.3 in (8.796 m) |
| 药室 | 3,646 in³ (59.75 dm³) |
| 射速 | 3 - 6 rounds per minute（脚注：最初参谋部要求 12 发/分，「impossibly high」；降到 6；Raven & Roberts 说战时实际持续 3-4 发/分；肯特号试验中短暂达到 5 发/分） |
| 弹重 | SAPC Mk Ib 256 lbs (116.1 kg)；HE Mk IIIb 255 lbs (115.7 kg) |
| 发射药 | 66.0 lbs (29.94 kg) SC 205，分两半装 |
| 初速 | 2,805 fps (855 mps)（注：原始为 2,900 fps / 884 mps 配 72.25 lbs 药，为减小散布与延长身管寿命而下调） |
| 身管寿命 | 550 发 |
| 备弹/门 | Kent 130 / London 150 / Dorsetshire 150 / York 172.5 |
| 最大射程 | 45 度 30,650 码 (28,030 m)（range table 按 MV=2,725 fps / 831 mps） |
| 装甲 | 各面与顶盖 0.98 in (2.5 cm) |
| 炮轴间距 | 84 in (213 cm) |

> 射速矛盾原文（`^The original Naval Staff requirement for these weapons was 12 rounds per minute, an impossibly high figure for the time. The requirement was ultimately reduced to six rounds per minute. However, "British Cruisers of World War Two" states that this rate was never reached during wartime service and that the maximum sustained ROF in action was actually 3 to 4 rounds per minute. During trials, HMS Kent did achieve a ROF of 5 rounds per minute for a brief time.`）已在正文并列，未合并。

**华盛顿条约原文**（来源 id `washington-treaty-1922`，Tier A，https://www.ibiblio.org/pha/pre-war/1922/nav_lim.html）
> Article XII: "No vessel of war of any of the Contracting Powers, hereafter laid down, other than a capital ship, shall carry a gun with a calibre in excess of 8 inches (203 millimetres)."
> Article XI: "No vessel of war exceeding 10,000 tons (10,160 metric tons) standard displacement, other than a capital ship or aircraft carrier, shall be acquired by, or constructed by, for, or within the jurisdiction of, any of the Contracting Powers."
> 签署日：`"Treaty Between the United States of America, the British Empire, France, Italy, and Japan, Signed at Washington, February 6, 1922."` → 正文事件日期用 `1922-02-06`。

---

### 1.2 `6in-50-mk23` — 6"/50 (15.2 cm) BL Mark XXIII
来源页：https://www.navweaps.com/Weapons/WNBR_6-50_mk23.php

**设计缘由（伦敦会议直接产物）**
> "This weapon was developed as a result of the London Cruiser Conference of January 1929 which restricted cruiser gun size to 6" (15.2 cm)."

**对炮本体的评价 + 改进都在炮座上**
> "A reliable weapon, although somewhat obsolescent in its use of bag ammunition, manual ramming and manually-operated breech mechanism. Mountings had improved ammunition supply compared to earlier cruisers, with power operated hoists and gravity assisted loading trays to increase the rate of fire. These improvements plus the use of enclosed mountings also reduced crew fatigue, meaning that the higher rate of fire could be maintained over a longer period."

**原拟用于防空，未成**
> "Like many contemporary mid-caliber designs, it was originally planned to use this gun in the AA role. However, again like many contemporary designs, the slow rates of train, elevation and firing made it ineffective in that role. For this reason, later mounting designs dropped the high angle requirement, a decision which also reduced their mounting weights."

**散布问题的根因与解法**
> "The early Southampton ('Town') class cruisers experienced dispersion problems with spreads up to 700 yards (640 m) being recorded. It was thought that air currents set up by the wing shells were affecting the flight of the center projectile, even though the center gun was set back to reduce the problems. However, a Professor Hay, who was in charge of the gunnery trials of HMS Newcastle at Shoeburyness in October 1937, theorized that as the cordite charge was much smaller than the chamber, that its burning caused more pressure at the top of the chamber than at the bottom and sides and thus produced an uneven vibration along the gun barrel. Special high speed cameras were mounted in the turret and these showed that some shells were indeed canted at the muzzle which increased the dispersion. As a result, a timing circuit was introduced to delay the firing of the center gun. This increased the shell separation and thus reduced dispersion."

**产量与制造商**
> "A total of 469 guns of all types were manufactured by Elswick, the Royal Gun Factory at Woolwich Arsenal and at William Beardmore & Co. Parkhead Forge works in Glasgow."

**Mark XXIV 的历史（两个不同的 Mark XXIV）**
> "There was a proposed variation tentatively designated as the Mark XXIV which was for the quadruple mounting originally intended for HMS Edinburgh and HMS Belfast. This gun would have used a power-worked breech mechanism, but it was cancelled along with the quadruple mounting. The Mark XXIV designation was ultimately given to an Army coastal defense gun having the same performance as the Mark VII\*, but constructed with a loose barrel. About 140 of these guns were built during World War II."

**装舰栏（原文，含「planned for Tiger class」）**
> "Ship Class Used On | Leander, Perth, Arethusa, Southampton ('Town'), Edinburgh ('Modified Town'), Fiji ('Colony'), Ceylon ('Improved Colony') and Swiftsure classes / Planned for Tiger class / Australian Perth class ('Modified Leander')"

**射速：8 发/分的来源与 6 发/分的实战值**
> "Rate Of Fire | 6 - 8 rounds per minute"
> 脚注引 Peter Cannon《The Twin 6in Mark XXI Turret》："While nominally capable of eight rounds per minute, a relatively high rate of fire for hand-worked guns, this was achieved in local control with guns laid to loading elevations; the local sight layer pulling the trigger as soon as his two 'Gun Ready' lamps illuminated following the 'loading interval,' the bare time it took gun crews to reload the guns. Reality in action was different, particularly under director control. This needed to account for the 'control interval,' the time taken by the director layer to steady his aim (around three seconds on average) as well as the need to depress and elevate the gun to facilitate loading angles while firing at longer ranges. ... six rounds per minute, relying on a good fire control solution while firing rapid broadsides, was considered the practical rate of fire of the mounting. However, during most actions such opportunities were rare."

**10 发/分的河床海战说法（原文即转述语气）**
> "'The twin 'Y' turret on HMNZS Achilles is said to have been able to fire at 10 rounds per minute for a few minutes at the Battle of the River Plate before the gun crews tired. The rate of fire was then about six rounds per minute. 'B' turret fired at an average of five rounds per minute during this battle.' British Cruisers of World War Two says that the rate of fire in action for the triple mountings was about five to six rounds per gun per minute."

**主要参数**
| 项 | 值 |
|---|---|
| 炮重 | 6.906 tons (7.017 mt) |
| 身管全长 | 309.8 in (7.869 m) |
| 膛线长 | 255.4 in (6.486 m) |
| 药室 | 1,750 in³ (28.7 dm³) |
| 射速 | 6 - 8 发/分（见上） |
| 弹重 | CPBC 112 lbs (50.8 kg)；HE 112 lbs (50.8 kg)；Leander only: CPBC Mark XXVB / HE 100 lbs (45.36 kg) |
| 发射药 | 30 lbs (13.6 kg) SC 150；32 lbs (14.5 kg) NQFP 128 |
| 初速 | 2,758 fps (841 mps) new gun |
| 身管寿命 | 1,100 发（另有一说 1,020 发） |
| 备弹/门 | 200 发（Town 级为条约按 150 登记，实际可容 200） |
| 最大射程 | 45 度 25,480 码 (23,300 m)，range table 按 MV=2,700 fps / 823 mps |
| 穿甲 | 12,500 码 穿 3" (76 mm) 舷侧；22,000 码 穿 2.0" (51 mm) 甲板 |
| 后坐 | 16.5 in (42 cm) |
| 装填角 | 界限 -5 ~ +12.5 度；优选 +5 ~ +7 度 |
| 炮轴间距 | Mark XXI 84 in (213 cm)；Mark XXII / XXIII 78 in (198 cm) |

**炮座分档（原文，极易与炮号混淆）**
> 双联 Mark XXI：Leander (4)、Arethusa (3)
> 三联 Mark XXII：Southampton ["Town"] (4)、Gloucester ["Later Town"] (4)
> 三联 Mark XXIII：Edinburgh ["Modified Town"] (4)、Fiji ["Colony"] (4)、Ceylon ["Improved Colony"] (3)、Swiftsure (3)
> 四联：Edinburgh (4) Mark XXIII（not in service）；Tiger (4) RP 10 Mark XXIV（not in service）
> 重量：Mark XXI 91 t / Southampton Mark XXII 146 t / Gloucester Mark XXII 约 182 t / Edinburgh Mark XXIII 182 t / Ceylon Mark XXIII 161 t

**四联装取消的试验依据**
> "The Edinburgh class were originally planned to carry four quadruple mountings. Tests at Shoeburyness in early 1936 with a mockup where all four guns were equally spaced at 42 inches (106.7 cm) apart showed considerable shell interference and collision problems, with the resultant large dispersal patterns. A later design had the guns mounted as two pairs... This design did not produce acceptable results and the quad mounting was cancelled in favor of an improved triple mounting."

**「X」炮塔的拆除**
> "Most surviving cruisers had 'X' turret removed as weight compensation for added electronic equipment and light AA. ... HMS Belfast, of the larger 'Modified Town' class, was unique in keeping all four of her 6" (15.2 cm) mountings throughout the war and beyond, although she did lose two of her twin 4"/45 (10.2 cm) Mark XIX mountings in their place."

**1948 年贝尔法斯特号备弹**
> "After the end of the war, in 1948 HMS Belfast had an outfit of 1,384 CPC, 960 HE, 474 Practice and 44 Drill for a total of 2,862 projectiles."
> 备弹构成变化："The outfits per gun were originally made up of 180 rounds of CPBC and 20 rounds of HE along with 31 practice rounds. In 1940 this was changed to 170 rounds of CPBC and 30 rounds of HE, showing the increased threat of air attack."

**两条「易混点」的原文依据**
- 炮号 vs 炮座号：城级的**炮**是 Mark XXIII、**炮座**是 Mark XXII（见上装舰栏与炮座栏）——这在标题 "6"/50 (15.2 cm) BL Mark XXIII" 与炮座栏 "Southampton ["Town"] (4) and Gloucester ["Later Town"] (4): Mark XXII" 之间直接可见。
- Mark XXII 炮（纳尔逊级副炮）与本页的 Mark XXII **炮座**是两个不同的东西，编号巧合。已在正文用一句明确区分。

**图片说明里的两个可用事实**
> "'Y' Turret from INS Delhi (formerly HMNZS Achilles) now on display at the Devonport Naval Base, New Zealand."
> "HMS Southampton 'Y' Mark XXII turret being lowered into place 3 July 1936."
> "A Mark XXIII Turret being fitted to HMS Bermuda in May 1942."
> "Guncrew of HMCS Uganda setting HE nose fuzes prior to bombarding Truk in June 1945."
> "Stern Mark XXII turrets on HMS Sheffield after she had sunk the German tanker Friederich Breme in the North Atlantic on 12 June 1941."

---

### 1.3 `45in-45-mk1` — 4.5"/45 (11.4 cm) QF Mark I
来源页：https://www.navweaps.com/Weapons/WNBR_45-45_mk1.php（页标题为 "QF Marks I, III and IV"）

**设计缘由**
> "These weapons were originally designed to arm the new carriers being built in the 1930s. They were also used on auxiliary vessels and to rearm a few capital ships and then late in the war they became the standard weapon for fleet destroyers."
> "Following the failure of the 5.1"/50 (13 cm) QF Mark I program, the 4.5" (11.4 cm) caliber was selected in the middle 1930s as the new DP weapon for carriers. It was believed that this was the largest caliber that could be used for a manually-handled fixed round and the complete round for this weapon weighed 85 lbs. (38.6 kg) versus 108 lbs. (49 kg) for the 5.1" (13 cm) gun."

**定装弹过重的结论（与 Mark III 篇共用的原句）**
> "...this fixed round proved to be too heavy in service use and there was a tendency for the projectiles to separate from the cartridge cases during normal handling. These problems resulted in a rapidly decreasing rate of fire during prolonged firing periods."

**Mark I 与 Mark III 的关系 / 装舰混杂**
> "The Mark I and Mark III guns were used only in twin mountings and were interchangeable with each other, the only difference being in details of the firing mechanism. Several ships actually carried both gun types, depending upon what was available when the ships were being built or modernized."
> "Mark I had both percussion and electric firing while the Mark III was designed for all-electric firing. The Mark I was later modified to permit electric only firing."

**产量**
> "Five experimental, 46 Mark I, 524 Mark III and at least 199 Mark IV guns were manufactured."

**皇家方舟号（1937）的装舰栏（原文）**
> "Mark I — Ark Royal (1937), Forth, Maidstone and Illustrious class / Queen Elizabeth (3 guns), Valiant (5 guns), Renown (4 guns), Scylla, Charybdis, Tyne, Hecla and Adamant"
> 炮座栏："Ark Royal (1937) (8), Forth (4), Maidstone (4), Tyne (4), Hecla (4) and Adamant (4): Mark III UD"
> 备弹栏："Ark Royal (1937), Illustrious and Implacable classes: 400 rounds"

> ⚠️ 注意一处原文内部张力：装舰栏把 Illustrious class 列在 **Mark I** 名下，而炮座栏写 Illustrious (8) 用的是 **Mark II BD** 炮座。本站在 `4_5in-qf-mk3.yaml` 里记的是光辉级装 Mark III。两说并存，本轮**不在 Mark I 篇里就光辉级下结论**，正文只写皇家方舟号与 Mark III UD 这个组合（两栏一致）。

**Mark III UD 与 Mark II BD 的区别**
> "Mark III UD (Upper Deck) mounting was similar to Mark II but had open-backed shields and a smaller roller path diameter of 93 inches (2.36 m) versus 113 inches (2.87 m) for the Mark II."
> 重量："Mark III UD: 29.738 tons (30.215 mt)" / "Mark II BD: 37.95 tons (38.56 mt)"

**皇家方舟号的弹药供应**
> "The ammunition supply in Ark Royal (1937) was by two-stage electrically driven chain hoists, with the first stage running from the handling rooms to the upper deck and the second stage running from the upper deck to the gun positions."

**主要参数**
| 项 | 值 |
|---|---|
| 实际膛径 | "All British 4.5" naval guns have an actual bore diameter of 4.45" (11.3 cm)." |
| 炮重 | Marks I and III: 6,304 lbs (2,859 kg)；Mark IV: 6,179 lbs (2,803 kg)（含炮闩） |
| 身管全长 | 202 in (5.131 m) |
| 膛线长 | 170.9 in (4.341 m) |
| 药室 | 600 in³ (9.83 dm³) |
| 射速 | 战时双联座（除 RP10 Mark IV\*）：12 发/分/门 |
| 弹重 | HE 55 lbs (24.95 kg)；SAP 58.25 lbs (26.4 kg) |
| 整发弹重 | HE 87 lbs (39.5 kg)；SAP 91.75 lbs (41.6 kg)（含 SC 发射药） |
| 发射药 | 11.04 lbs (5.0 kg) SC 122；13.63 lbs (6.18 kg) NF/S 198-054 |
| 药筒 | 定装：黄铜 114 × 695 mm R，约 28 lbs；分装：114 × 645 mm R，约 27.0 lbs |
| 初速 | 新炮 2,449 fps (746 mps)；平均 2,350 fps (716 mps) |
| 身管寿命 | 650 发 |
| 最大射程 | 43 度 19,900 码 (18,200 m)；45 度 20,750 码 (18,970 m) |
| 射高 | 50 度 29,910 ft (9,120 m)；80 度 41,000 ft (12,500 m) |
| 后坐 | 18 in (46 cm)（全部） |
| 炮轴间距 | 双联座一律 38 in (96.5 cm) |

**声望号 1941-05-08 事故**
> "On 8 May 1941 while HMS Renown was engaging Italian torpedo bombers, a fail-safe lockout system malfunctioned and her P3 mounting fired into the back of P2 mounting, killing six and wounding twenty-six crewmembers. Angle iron frameworks were erected by the ship's crew around the mountings to prevent a repeat episode. The fail-safe gear was overhauled during a refit at Rosyth later that same year."

**皇家方舟号沉没**
> 图片说明："HMS Legion rescuing sailors from the sinking HMS Ark Royal on 13 November 1941. 4.5"/45 (11.4 cm) Mark I in Mark III UD mountings."

**1944 年驱逐舰改用 Mark IV 与分装弹药**
> "In 1944, guns of 4.7" (12 cm) caliber, which had been used on nearly every British destroyer built since 1918, gave way to a new destroyer weapon, the 4.5" (11.4 cm) QF Mark IV gun... It had originally been planned that destroyers would also use fixed ammunition, but reports from the cruisers Scylla and Charybdis told of loading problems during rough weather due to the heavy weight of the ammunition. As these were 6,000 ton (6,100 mt) cruisers, it was an obvious conclusion that the much lighter destroyers would have even worse handling problems - a conclusion that the Royal Navy should have been aware of for over a decade."

**战后编号制度改变（1950 年代）**
> "In the 1950s the British weapon designation system changed from being per the gun itself to being per the mounting. At the same time, arabic numerals replaced roman numerals."

---

### 1.4 `47in-45-mk12` — 4.7"/45 (12 cm) QF Mark XII
实际来源页：https://www.navweaps.com/Weapons/WNBR_47-45_mk9.php（页标题 "4.7"/45 (12 cm) QF Mark IX and Mark XII"）

**Mark XII 与 Mark IX 的唯一差别**
> "The 4.7" (12 cm) QF Mark IX was used on most destroyers built in the 1930s and 1940s. The almost identical Mark XII was designed for use in twin mountings and differed from the Mark IX in being slightly heavier and longer. Both Marks fired separate ammunition, otherwise they were similar to the preceding 4.7" (12 cm) BL Mark I."

**装舰栏（Mark XII 部分）**
> "Mark XII — Prototype mounted on Hereward / Tribal, J, K and N destroyer classes / Abdiel class minelayers / Netherlands 3: Van Galen (ii) class (ex-RN 'N' destroyers)"

**没有对空能力（正文直接引用的重句）**
> "The lack of a DP function for these weapons was keenly felt throughout the war as more British destroyers were sunk by air attack than from any other cause. What little AA capability that these weapons did have was hindered by a lack of a tachymetric (predictive) fire control system and the setting of HE time fuzes by hand."

**CPXIX 的地位**
> "The CPXIX twin mounting was the first British power mounting specifically designed for destroyers."

**CPXIX 的细节**
> "These guns had a trunnion height 13" (33 cm) higher than the single mountings. This required raising the wheelhouse to enable to helmsman to see over the gun shields. It also made loading the weapons at low elevations more difficult. The gun axes were 38 in (96.5 cm) apart. Guns shared a cradle and could not elevate independently. Each mounting had two dredger projectile hoists which ran vertically from the shell rooms to the deck below the guns except for 'Y' mounting on the Tribal class where the hoists terminated on the upper deck. The projectiles for 'A', 'B' and 'X' mountings were transferred from the tops of the hoists to the gun deck via hand-operated sliding chutes which ran diagonally between the two decks. Propellant cartridges were passed up from the magazines to the guns by hand."

**动力来源**
> "The Tribal class had their four CPXIX mountings split in two groups, each powered by a 140 HP steam turbine and oil hydraulic pump. The J, K and N classes had a 70 HP electric motor and pump on each individual mounting."

**无 RPC**
> 描述段："The twin mounting had power ramming and used power training and elevation but no RPC gear was installed."

**主要参数（Mark IX / Mark XII 并列，正文已按 Mark XII 取值）**
| 项 | Mark XII | Mark IX |
|---|---|---|
| 炮重 | 3.238 - 3.245 tons (3,290 - 3,297 kg) | 2.963 - 2.984 tons (3,011 - 3,032 kg) |
| 身管全长 | 224.08 in (5.692 m) | 220.62 in (5.604 m) |
| 膛径（实际） | "Actual bore diameter of all British 4.7" guns was 4.724" (12 cm)." | 同 |
| 膛线长 | 179.3 in (4.552 m) | 同 |
| 药室 | 628 in³ (10.29 dm³) | 同 |
| 射速 | CPXIX (twin) 10 - 12 发/分；其他炮座 7 - 10 发/分 | 同 |
| 弹重 | HE 50 lbs (22.68 kg)；SAP 50 lbs (22.68 kg) | 同 |
| 药筒 | 黄铜 4.724 × 30.922 in (120 × 785.42 mm) | 同 |
| 发射药 | 11.58 lbs (5.25 kg) SC 109；13.13 lbs (5.96 kg) NF/S 164-048 | 同 |
| 初速 | 2,650 fps (808 mps) | 同 |
| 膛压 | 20 tons/in² (2,150 kg/cm²) | 同 |
| 身管寿命 | 1,400 发 | 同 |
| 射程 | 30 度 15,800 码 (14,450 m)；40 度 17,000 码 (15,545 m) | 同 |
| 穿甲 | 6,500 码 (5,950 m) 穿 2.5" (63 mm) NC 装甲 | 同 |
| 后坐 | 除 CPXXII 外 26.5 in (67.3 cm) | 同 |
| 产量 | 372 门（含各亚型） | 742 门（含各亚型） |

**装舰与备弹**
> "Ammunition stowage per gun 2a — Tribals: 200 rounds SAP + 50 rounds HE and 50 rounds star shell per ship"

**炮座仰角**
> "CPXIX: -10 / +40 degrees"（单装各型：CPXIV -10/+30、CPXVII -10/+40、CPXVIII -10/+40、CPXXII -10/+55）

**「X」炮座换 4 英寸高炮**
> "Most of the Tribal class had 'X' mounting removed and a twin 4"/45 (10.2 cm) HA/LA mounting installed in its place in order to increase their anti-aircraft capabilities. For similar reasons, the fast minelayers of the Abdiel class had their three 4.7" (12 cm) twin mountings replaced with three twin 4"/45 (10.2 cm) HA/LA mountings."

**J/K 级「X」炮座中位问题**
> "For reasons not known at this time, 'X' mounting on the 'J' and 'K' classes was originally set up such that the mid-training position was dead ahead. This meant that this stern mounting on these ships could not bear directly astern and that having to train from the port quarter to the starboard quarter meant that the mounting had to slew 'the long way round' to follow a target passing across the stern. Early in the war, the mountings were modified to move the mid-train position to the more normal dead astern position and the 'N' class was completed to this configuration."

**炮口暴风与防浪板**
> "One of the more noticeable features of destroyers with these guns were the large 'sprayshields' forward of 'B' gun platform and aft of 'X' gun platform. Although these structures did reduce spray on the upper decks, their true purpose was to reduce the problem of blast from the upper guns disrupting the crews of the guns on the lower decks. ... By choosing 'lightweight' open mountings for these destroyers, the designers paid a weight penalty in having to add these shield structures. Likewise, the L-M destroyer classes with their 'heavyweight' enclosed 4.7" (12 cm) mounts saved some compensating weight by being able to eliminate these shields."

**荷兰转交**
> "Two 'N' class destroyers (ex-RN Noble (i) and ex-RN Nonpareil) were turned over the the Royal Netherlands Navy in 1942 and became RNN Van Galen (ii) and RNN Tjerk Hiddes, respectively."

**战争末期弹药**
> "Ten per gun special anti-submarine HE shells that had RDX/TNT fillers were supplied to each ship by 1945 and star shell complement was 150-200 per ship. VT fuzes were supplied starting in 1944 and by the end of the war these were about 50% of HE projectiles issued."

**两型可 QF / SA 双模式**
> "Both the Mark IX and the Mark XII guns could be operated in either Quick Firing (QF) or Semi-Automatic (SA) mode. In QF mode, the breech was manually opened after firing by moving a lever which also ejected the spent casing. In SA mode, the breech would open automatically after firing and eject the spent casing."

---

## 2. 卡住的地方

### 2.1 任务下发的 4.7"/45 Mk XII URL 是 404
- 下发地址：`http://www.navweaps.com/Weapons/WNBR_47-45_mk12.php` → HTTP 404。
- 依次试过：`WNBR_47-45_mk12.php`（404）、`WNBR_4-7-45_mk12.php`（404）、
  `WNBR_47-45_mk11.php`（404）、`WNBR_47-45_mk12_and_mk12_star.php`（404）、
  `WNBR_4.7-45_mk12.php`（404）；`WNBR_47-45_mk9.php` → **200**。
- 原因：NavWeaps 把 Mark IX 与 Mark XII **放在同一页**，页标题即
  "4.7"/45 (12 cm) QF Mark IX and Mark XII"。
- 处理：数据全部取自该页，来源 id 仍按任务规定用 `navweaps-4-7in-45-mk12`，
  `url` 字段填**实际抓到的** `WNBR_47-45_mk9.php`，并在来源 note 里写清这一差异。
  **请主会话在合并时不要把这个 url「修正」成下发地址**。

### 2.2 `navweaps-45in-45-mk1` 既有 note 与实际不符
- `data/sources.yaml:2217` 的 note 写「注意：**必须加 -L 并走代理**」。
- 本轮实测：`http://www.navweaps.com/Weapons/WNBR_45-45_mk1.php` **直连即 200**，
  未加 `-L`、未走代理，返回 60,868 字节，Mark I/III/IV 家族页内容完整
  （含 Mark I 装舰栏、Mark III UD 炮座栏、声望号事故、1944 年 Mark IV 段）。
- 判断：这是环境变化（此前需代理、现在可达），**不是内容问题**。
  本文件只作记录，`data/sources.yaml` 的 note 由主会话决定是否更新；本轮不改 `data/`。

### 2.3 光辉级到底装 Mark I 还是 Mark III，NavWeaps 自己两栏不一致
- 装舰栏："Mark I — ... Illustrious class"
- 炮座栏："Illustrious (8) class: Mark II BD"
- 而 `data/weapon-articles/4_5in-qf-mk3.yaml` 记的是光辉级装 **Mark III**。
- 处理：`45in-45-mk1.yaml` 里**不写光辉级**，只写皇家方舟号 + Mark III UD
  （装舰栏与炮座栏两处一致，无争议）。这个矛盾已写进本文件，留主会话裁决是否
  需要回头核 Mark III 篇。

### 2.4 没查到、因此没写的数字
| 武器 | 缺什么 | 页面原状 |
|---|---|---|
| `8in-50-mk8` | HE 弹的弹长 | 页面写 `HE - N/A` |
| `8in-50-mk8` | 各炮座俯仰/回旋的最终值只给了区间 | `Mark I*, Mark II and Mark II*: 4 - 5.5 degrees per second` / `Final design: 5 - 6 degrees per second`，未给每型单值 |
| `8in-50-mk8` | 炮座实际俯仰速率在 Mark I 上被下调后的最终值 | 注 `This elevation rate was found to be impossible to control accurately and was reduced to 4 degrees per second.`（原文未说明是哪一型最终值，正文未采用） |
| `6in-50-mk23` | 100 磅弹在利安得号上的初速 | 原文只说 `would have had a higher MV with the same charges`，未给数值 |
| `6in-50-mk23` | 利安得号是否改装为可打 112 磅弹 | 原文只说改动 "relatively minor"，未记录改装，正文写「未记录改装」 |
| `45in-45-mk1` | 高爆弹/半穿甲弹的炸药装药量 | 页面写 `Bursting Charge | N/A` |
| `45in-45-mk1` | 弹长 | 页面写 `Projectile Length | N/A`（只给整发定装弹 49 in / 124.5 cm） |
| `45in-45-mk1` | Mark I 单装炮座（Mark I UD）参数 | 原文 `None: Mark I UD`，即未服役，无参数 |
| `47in-45-mk12` | 药筒空重 | 页面写 `N/A`（只给连发射药 30.5 lbs / 13.8 kg） |
| `47in-45-mk12` | HE 弹长 | 页面写 `HE: N/A`（只给 SAP 约 15 in / 38 cm） |
| `47in-45-mk12` | 非部族级的备弹量 | 原文 `Others: N/A, but probably similar to Tribals` —— 含 "probably"，**未采用** |
| `47in-45-mk12` | 爆药成分 | 页面写 `N/A - TNT` |

### 2.5 刻意没用的两条
- **`47in-45-mk12` 的「Others: N/A, but probably similar to Tribals」** ——
  原文自己带 "probably"，属于推断，按站规不进正文。
- **`8in-50-mk8` 的 12 发/分** —— 那是 1920 年代参谋部的**要求值**，
  原文自己说 "an impossibly high figure for the time"，不是性能，正文不写。

---

## 3. 有争议的记载（正文怎么并列的）

### 3.1 6"/50 Mark XXIII 的射速：8 / 6 / 5 / 10 四个数
| 数值 | 条件 | 出处 |
|---|---|---|
| 8 发/分 | 局部控制、炮压到装填角、纯装填循环 | NavWeaps 名义值，引 Peter Cannon |
| 6 发/分 | 指挥仪控制，含约 3 秒控制间隔 + 压炮到装填角的时间 | 同上，「considered the practical rate of fire of the mounting」 |
| 5–6 发/分 | 三联装炮座实战 | Raven & Roberts《British Cruisers of World War Two》，NavWeaps 转引 |
| 10 发/分 | 河床海战开局数分钟，阿基里斯号「Y」炮塔 | NavWeaps 用 **"is said to have been able to"**，未给一手依据 |

**并列方式**：
- 8 vs 6 写在同一段，明确标为「理论值 / 实际值」并各自附条件（`6in-50-mk23.yaml` intro 第 5 段）。
- 10 发/分单独一段，**明写来源本身是转述语气、无一手依据**，只作并列不写进论断；
  history 事件里再复述一次同样的限定。这是全篇唯一一处我主动降低证据等级的地方，
  理由写进了正文而不是只写在底稿里。

### 3.2 8"/50 Mark VIII 的射速：6 与 3–4
- NavWeaps 表列 `3 - 6 rounds per minute`。
- 脚注引 Raven & Roberts：`this rate was never reached during wartime service and
  that the maximum sustained ROF in action was actually 3 to 4 rounds per minute`。
- 另：肯特号在试验中曾短暂达到 5 发/分。
- **并列方式**：正文只写 "3 到 6 发/分" 并注明战时实际持续 3–4 发/分（见 `6in-50-mk23.yaml`
  的对比段，那里需要两型放在一起比）。未裁决，也未取中间值。

### 3.3 8"/50 Mark VIII 的「可靠性」：Mark I 差、Mark II 好
- 这是同一页里的两组评价，容易被读成「这炮不可靠」。
- 关键区分：抱怨来自 **Mark I / Mark I\***（肯特、伦敦级），好评来自 **Mark II**
  （诺福克、约克级）。诺福克号属 Mark II。
- **并列方式**：`8in-50-mk8.yaml` intro 第 3 段专门写这一区分，
  并把 1938 年伦敦号的抱怨（Mark I\* 炮座）与 1941 年诺福克号的好评（Mark II）
  分列在 history 的两条事件里，各自带日期，不合并成一句评语。

### 3.4 诺福克号 527 发：「minor problems」与「X 炮塔只打 8 发」
- 同一段原文里同时存在，且原文对原因的措辞是 **"probably"**。
- **处理**：正文并列，明确写出 8 发 vs 103 发的对比；
  原因按原文写「navweaps 归因于……」，并保留 "probably" 的限定，不改写成确定结论。

### 3.5 4.5"/45 的射速：12 发/分 vs 持续射击时下降
- NavWeaps 表列 12 发/分/门（战时双联座）。
- 同页又说定装弹过重导致 "a rapidly decreasing rate of fire during prolonged firing periods"。
- 既有 `4_5in-qf-mk3.yaml` 已用「ADM 3363/0197 的 30 分钟 12 发/分」并列处理过。
- **本篇（Mark I）处理**：不复述那条论证（属 Mark III 篇），只留结论一句，
  并说明「选口径的前提在服役中被推翻」。避免与 Mark III 篇重复长篇论证。

### 3.6 爱丁堡级四联装：为什么取消
- 有试验依据（1936 年 Shoeburyness 等间距 42 英寸模型散布过大），
  也有「改为两两成对仍不可接受」的后续，然后取消。
- 页面另有一句 `Delay coils were under consideration at the time of the cancellation.`
  —— 这是「取消时正在考虑延时线圈」，不是「用了延时线圈」，正文未写成已采用。

---

## 4. 与 `47in-40-mk8.yaml` 的篇幅对照

| | 47in-40-mk8（范例） | 8in-50-mk8 | 6in-50-mk23 | 45in-45-mk1 | 47in-45-mk12 |
|---|---|---|---|---|---|
| intro 段数 | 3 | 6 | 8 | 6 | 6 |
| history 节数 | 1 | 2 | 2 | 3 | 2 |
| history 事件数 | 3 | 8 | 11 | 8 | 6 |

说明：范例只有 3 段 / 1 节 3 事件，但它自己在文件头注明「六门炮一发未放」
这种单点事故值得独占一段。这 4 型都是**新船要用的主力武器**，参数与装舰面都比
范例宽（范例只是一型高炮），所以按 SCHEMA §7「有特殊意义的舰：intro 3~4 段 +
history 3~4 节、共 15~25 条事件」的上限区间的**下限一侧**取，
实际落在 6 段 / 2 节 / 6–11 事件。段数偏多的主因是每型都额外加了一段
「主要参数」——这是任务要求第 3 条（口径、身长、弹重、初速、射速、最大射程都要写），
而范例里没有这一段。若主会话认为超出，建议**先删各篇的「主要参数」段**
（该段信息可由武器实体的 fact 承载），而不是删掉争议段。

---

## 交付摘要

| 项 | 数量 |
|---|---|
| 舰级文件 | 0（本任务只写武器正文） |
| 单舰文件 | 0 |
| 切片文件 | 0 |
| 武器正文文件 | 4 |
| 新登记来源 | 1（`navweaps-4-7in-45-mk12`） |

产出清单：

| 文件 | 内容 |
|---|---|
| `weapon-articles/8in-50-mk8.yaml` | intro 6 段 / history 2 节 8 事件 |
| `weapon-articles/6in-50-mk23.yaml` | intro 8 段 / history 2 节 11 事件 |
| `weapon-articles/45in-45-mk1.yaml` | intro 6 段 / history 3 节 8 事件 |
| `weapon-articles/47in-45-mk12.yaml` | intro 6 段 / history 2 节 6 事件 |
| `sources-fragment.yaml` | 1 条新来源 + 引用到的既有来源清单 |
| `_raw/` | 4 份抓取 HTML + 转出的 txt + `h2t.py` |
| `_selfcheck.py` | 结构自检脚本（自写，不是项目校验器） |

自检结果（`python -c "import yaml,glob;..."`）：`yaml ok`。
另跑了 `_selfcheck.py`，逐文件核对：顶层 `weapon` 键存在、文件名与 `weapon` 值一致、
每段/每事件有 `src`、`src` 全部能在 `data/sources.yaml`（3929 行版）或本分片里找到、
无 tier E 来源、无「据说/有人认为/有人称/据信/或许/大概/应该是」、
日期格式全部 `YYYY` / `YYYY-MM` / `YYYY-MM-DD` —— **4 个文件 0 问题**。

### 卡住的地方
- **下发 URL 404**：`WNBR_47-45_mk12.php` 不存在，实际页是 `WNBR_47-45_mk9.php`
  （Mark IX 与 Mark XII 同页）。见 §2.1，合并时 **不要改 url**。
- **既有来源 note 过时**：`navweaps-45in-45-mk1` 的 note 说「必须加 -L 并走代理」，
  本轮直连即 200。见 §2.2。
- **NavWeaps 自相矛盾**：光辉级在装舰栏归 Mark I、在炮座栏归 Mark II BD，
  与既有 Mark III 篇也不一致。本篇绕开光辉级，见 §2.3。
- **11 项数值页面本身未给**，逐项列在 §2.4，全部按「来源未给」处理，未用姊妹型填充。

### 有争议的记载
- **6"/50 Mk XXIII 射速 8 / 6 / 5 / 10 四个数**：8 是局部控制理论值、6 是指挥仪控制
  实际值、5–6 是 Raven & Roberts 的实战值、10 是河床海战流传说法且 NavWeaps 自身
  用 "is said to" 转述。前三个并列并附条件，10 单列且**明写无一手依据**。见 §3.1。
- **8"/50 Mk VIII 射速 6 vs 3–4**：表值 vs 战时实际持续值，并列不裁决。见 §3.2。
- **8"/50 Mk VIII 的可靠性名声**：差评属 Mark I/I\*（肯特、伦敦），好评属 Mark II
  （诺福克、约克）。正文按炮座型号分开写，不合并。见 §3.3。
- **诺福克号 527 发**：「minor problems」与「X 炮塔右炮只打 8 发（对 103 发）」同时成立，
  原因原文用 "probably"。并列，保留限定语。见 §3.4。
- **4.5"/45 射速 12 发/分 vs 持续射击衰减**：结论保留，详细论证留在既有 Mark III 篇，
  本篇不重复。见 §3.5。
