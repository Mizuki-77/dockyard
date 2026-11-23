# 中途岛 · 深度素材补强（缺口 A/B/C/D）

> 采集：2026-11-23 · 采集员 `midway-deep`
> 只管四块缺口：**航空队编制与损失 / 机载武器 / 雷达与发现顺序 / 战役后续影响**
> 战斗逐时事件流已在 `work/raw/midway-battle.md`（下称 **[旧稿]**），本文件**不重复**，只补它没覆盖的部分。
> 只写 `work/staging/midway-deep/`。未改动 `data/` `src/` `public/` `docs/` 任何文件。
>
> **硬规矩执行情况**：每条结论带英文（或日文）原句 + URL；查不到写「未获取」；有分歧两边并列不裁决；
> 任务书里的史实陈述一律当「待核实」，与之不符的以来源为准并在 §0 指出。

---

## 0. 任务书前提纠错（硬规矩 4：先说前提错在哪）

任务书四块缺口的设定里，有 **6 处**与来源不符。先说清楚，正文按核实后的事实写。

### 纠错 ①「日方飞行员阵亡数是重点争议」——说得对，但**不是查不到**，且已有精确分解

任务书说这是「各来源口径差异大」的重点争议，隐含「查不到」的意思。实际上 NHHC 官方史学已经给出**精确分解**：

> "Over 3,000 Japanese sailors were killed in the battle, most while valiantly trying to save their ships, including over 700 aircraft technicians/maintainers (a very limited skill in the Japanese navy). All 248 carrier aircraft were lost, most going down with their ships, along with several cruiser- and battleship-launched float planes. **However, most Japanese pilots were rescued; only 36 were lost on the carriers and 74 in the air, mostly from Hiryu.**"
> —— [S2] https://www.history.navy.mil/about-us/leadership/director/directors-corner/h-grams/h-gram-006/h-006-1.html

36 + 74 = 110。这就是 Parshall & Tully 那个常被引用的「110 名」。加上四份 USSBS 一手访谈的分舰数字（§A.4），
这一项**从「未获取」升级为「多口径并列，可写」**。

### 纠错 ②「熟练飞行员不可替代 → 日本海军航空兵力长期损失」——因果链**被 NHHC 明确反驳**

这是 D 块最要紧的一处。任务书写「熟练飞行员不可替代」，暗示中途岛飞行员损失是长期衰退的主因。
NHHC 官方史学把这话**反过来说**，而且说得非常直白：

> "**It was not the loss of pilots at Midway that crippled Japan's ability to wage offensive naval operations, but rather the loss of the most important Japanese strategic asset, the irreplaceable aircraft carriers.** Only one new Japanese fleet carrier would make it into a major fleet action during the war, only to be sunk by a U.S. submarine in her first battle."
> —— [S2] 同上

USSBS 一手访谈给出了同一方向的旁证（飞行员损耗率的修订主因是瓜岛，不是中途岛）：

> "I believe the **Battle of GUADALCANAL and the actions at RABAUL had more to do with the revision than the Battle of MIDWAY**."
> —— [S13] https://www.ibiblio.org/hyperwar/AAF/USSBS/IJO/IJO-31.html

《Shattered Sword》导言更把「精英飞行员全灭」直接列为**谬见**：

> "• Japan's elite carrier aviators were all but wiped out during the battle.
>  All of these are **fallacious**. All are either untrue, or at least require careful clarification."
> —— [S31] https://www.shatteredswordbook.com/ShatteredSwordIntroduction.pdf

**写法建议**：D 块「飞行员不可替代」这一条要改成「飞行员的损失被多数来源认定**不是**中途岛的决定性后果；
决定性后果是四艘航母本身 + 约 700 名航空机务人员」。争议两边都引，别只写传统的「飞行员说」。

### 纠错 ③「美方 CXAM 雷达在中途岛的作用（谁先发现谁）」——CXAM **没发现日舰**

任务书把「发现顺序」笼统挂在 CXAM 名下。核实结果：**CXAM 在中途岛是纯防御性装备**，
它发现的全是「来袭机」和「日方侦察机」；发现日方**舰队**的是 PBY 的机载雷达与目视。

> "At 0815 Enterprise CXAM operators found a contact at thirty miles on bearing 185 degrees. **It was Tone's Number 4 float plane** still looking for the task force."
> —— [S11] https://ethw.org/Midway_-_Chapter_7_of_Radar_and_the_Fighter_Directors

CXAM 一共四次有效接触，**四次都不是日方主力舰队**：利根 4 号机（侦察机）、飞龙第一波 18 架舰爆、
飞龙第二波 10 架舰攻、以及追击筑摩 5 号机。真正「先发现日舰」的是 PBY：
舰载 ASV 雷达 + 目视，第一次是 6 月 3 日 09:04 的水面接触（[S1] ch4）。
**CXAM 的战场价值是「给了美军约 45–50 分钟的预警窗口」，不是「发现了敌人」。**

### 纠错 ④「TBD 几乎全灭」——成立，但任务书给的「41 架出击、35 架被击落」需要注明口径

`data/battles/midway.yaml` 现有 losses 注释写「41 架出击、35 架被击落」。核实：
41 = 15(VT-8) + 14(VT-6) + 12(VT-3)，三艘航母的 TBD 编制数（[S3] NavWeaps）。
35 = 41 − 6，与 NHHC「只有 6 架返回航母」的说法自洽：

> "One TBF and two B-26s crash-landed on Midway afterward, and **only six of the TBDs made it back to the carriers; only three of the aircraft were flyable**. Of the 99 men in the 42 torpedo planes that were lost, only three survived the battle."
> —— [S2]

**但**：这 6 架里含「返回但已不可用」的，「被击落」与「损失」不是同一个词。
建议改写为「41 架出击，仅 6 架返回航母、其中 3 架仍可用；损失 35 架」。
另注意 [S2] 那句「42 torpedo planes」是把中途岛的 6 架 TBF + 4 架 B-26 算进去的另一种口径，与 41 架不是一回事。

### 纠错 ⑤ 时间基准**不止两套，是四套**

任务书警告「日方两套时间（JST / 中途岛当地）」。实测发现美方行动报告也各用各的：

| 来源 | 明示的时间基准 | 原句 |
|---|---|---|
| ONI 战斗叙述 [S1] | **Zone +12**（中途岛当地） | "All times given in this narrative are zone plus 12." |
| 企业号行动报告 [S5] | **Zone +10** | "On the afternoon and evening of June 3, 1942, the general situation prior to the battle was as follows (**times throughout are Zone plus 10**)" |
| 大黄蜂号行动报告 [S6] | **Zone +10** | "At 090 (**all times given hereafter are zone plus 10**) commenced launching the Air Group for attack" |
| 约克城号行动报告 [S7] | **未声明**，但内部时刻与 +10 自洽 | 6/6 潜艇攻击记 "At about 1536"，ONI(+12) 记 13:35 → 差值正好 2 小时 |
| 南云战斗详报 [S4] | **JST +9，5 日制** | "It should be noted that all dates in this report and all times are in Tokyo time, Plus 9." |
| combinedfleet TROM | **中途岛当地**（自述换算规则） | "To convert to Tokyo (JST) or Zone 9 time, subtract three hours but advance one one day ahead of a Midway Local time - (Tully)" |

**引用美方行动报告时必须把 +10 换算成 +12 再和 [S1] 对表**，否则整体差 2 小时——这比任务书担心的 21 小时差更容易踩，
因为它只差 2 小时，不容易被察觉。
另：约克城号行动报告记鱼雷命中「At about 1620」，换算后应为 1420，与 ONI 的 1445 差 25 分钟。
该报告自己用了「about」，属原始记录精度问题，**两说并列不裁决**。

### 纠错 ⑥「日方四航母飞行员数量」——**未获取**

任务书要求「各搭载多少架、什么机型、飞行员数量」。前两项全部拿到（§A.1、§A.2）；
**各舰飞行员编制数在所有已检索来源中都没有**。南云战斗详报的编制表（Table 1）只列飞机数，
USSBS 四份访谈只给损失数，NHHC 战斗序列只列舰长与飞行队长姓名。
按规矩写「未获取」，**不推算**（比如拿飞机数除以 2 或用「每机 1 名飞行员」倒推，都不做）。

---

## A. 双方航空队编制与损失

### A.1 日方四航母航空队编制（NavWeaps 逐队明细，最细的一份）

主来源 [S3] NavWeaps《Orders of Battle - Battle of Midway and Aleutians》
<https://www.navweaps.com/index_oob/OOB_WWII_Pacific/OOB_WWII_Midway.php>
这一页的价值在于**按 Buntai（分队）逐个列**，且把各航空队指挥官与「机种 × 架数」挂在一起。

**赤城 Air Unit**（指挥官 Cdr. 渊田美津雄，飞行观察员）

> "Unit commander / Commanding officer: Cdr. Fuchida Mitsuo (Notes: Air observer.) / **Notes: 1 x Type 97 B5N2 carrier attack plane.**"
> "Kansen Buntai / Commanding officer: Lt. Itaya Shigeru (Notes: Pilot.) / **Notes: 18 x Type 00 A6M2 carrier fighters.**"
> "Kanbaku Buntai / Commanding officer: Lt. Chihaya Takehiro (Notes: Air observer.) / **Notes: 18 x Type 99 D3A1 carrier bombers.**"
> "Kanko Buntai / Commanding officer: Lt.Cdr. Murata Shigeharu (Notes: Pilot.) / **Notes: 17 x Type 97 B5N2 carrier attack planes.**"
> "6th Kokutai / Commanding officer: Lt.Cdr. Kaneko Tadashi (Notes: Pilot.) / **Notes: 6 x Type 00 A6M2 carrier fighters.**"

**加贺 Air Unit**（指挥官 Lt.Cdr. 楠美正，阵亡；舰长冈田次作阵亡）

> "Unit commander / Commanding officer: Lt.Cdr. Kusumi Tadashi †(killed) (Notes: Pilot.) / **Notes: 1 x Type 97 B5N2 carrier attack plane.**"
> "Kansen Buntai / Commanding officer: Lt. Sato Masao (Notes: Pilot.) / **Notes: 18 x Type 00 A6M2 carrier fighters.**"
> "Kanbaku Buntai / Commanding officer: Lt. Ogawa Sho-ichi †(killed) (Notes: Pilot.) / **Notes: 18 x Type 99 D3A1 carrier bombers.**"
> "Kanko Buntai / Commanding officer: Lt. Kazuraki Masuhiko †(killed) (Notes: Pilot.) / **Notes: 26 x Type 97 B5N2 carrier attack planes.**"
> "6th Kokutai / **Notes: 9 x Type 00 A6M2 carrier fighters.**"
> "Soryu Kanbaku Buntai (spares) / **Notes: 2 x Type 99 D3A1 carrier bombers.**"

**飞龙 Air Unit**（指挥官 Lt. 友永丈市，阵亡；舰长加来止男阵亡）

> "Unit commander / Commanding officer: Lt. Tomanga Jo-ichi †(killed) (Notes: Pilot.) / **Notes: 1 x Type 97 B5N2 carrier attack plane.**"
> "Kansen Buntai / Commanding officer: Lt. Mori Shigeru †(killed) (Notes: Pilot.) / **Notes: 18 x Type 00 A6M2 carrier fighters.**"
> "Kanbaku Buntai / Commanding officer: Lt. Kobayashi Michio †(killed) (Notes: Pilot.) / **Notes: 18 x Type 99 D3A1 carrier bombers.**"
> "Kanko Buntai / Commanding officer: Lt. Kikuchi Rokuro †(killed) (Notes: Pilot.) / **Notes: 17 x Type 97 B5N2 carrier attack planes .**"
> "6th Kokutai / **Notes: 3 x Type 00 A6M2 carrier fighters.**"

**苍龙 Air Unit**（指挥官 Lt.Cdr. 江草隆繁；舰长柳本柳作阵亡）

> "Unit commander / Commanding officer: Lt.Cdr. Egusa (Notes: Pilot.) / **Notes: 1 x Type 99 D3A1 carrier bomber.**"
> "Kansen Buntai / Commanding officer: Lt. Suganami Masaji (Notes: Pilot.) / **Notes: 18 x Type 00 A6M2 carrier fighters.**"
> "Kanbaku Buntai / Commanding officer: Lt. Ikeda Masatake (Notes: Pilot.) / **Notes: 15 x Type 99 D3A1 carrier bombers.**"
> "Reconnaissance aircraft / **Notes: 1 x Type 02 D4Y1-C reconnaissance plane; 1 other lost.**"
> "Kanko Buntai / Commanding officer: Lt. Abe Heijiro (Notes: Air observer.) / **Notes: 18 x Type 97 B5N2 carrier attack planes.**"
> "6th Kokutai / **Notes: 3 x Type 00 A6M2 carrier fighters.**"

**结构解读（重要，供主会话避免误判「来源打架」）**：
NavWeaps 每个航空队都单列一行「Unit commander … 1 x B5N2（或 D3A1）」。
把它加回去，就和 combinedfleet TROM 的数字完全对齐：

| 舰 | NavWeaps 分队合计 | combinedfleet TROM 原句数 | 是否冲突 |
|---|---|---|---|
| 赤城 舰攻 | 17 + 1（队长机）= **18** | 18 | 不冲突 |
| 加贺 舰攻 | 26 + 1 = **27** | 27 | 不冲突 |
| 飞龙 舰攻 | 17 + 1 = **18** | 18（第一波派 18、其中 1 架故障返航） | 不冲突 |
| 苍龙 舰爆 | 15 + 1（队长机为舰爆）= **16** | 16 | 不冲突 |

> ⚠️ 这个「加回去」是**结构解读**，不是来源断言。NavWeaps 没有明说队长机是否计入 Buntai 数。
> 主会话若要写进正文，请写明「按 NavWeaps 分队表结构相加后与 TROM 一致」，不要写成「来源明确说 18 架」。

**combinedfleet TROM 侧的原句（用词更直接，可作正文引语）**

> "AKAGI's air group consists of **18 A6M2 "Zeke", 18 D3A1 "Val" and 18 B5N2 "Kate"**. Additionally, **six A6M2 "Zeke" from the 6th Air Group**, destined to Midway's future garrison, are embarked."
> —— [S8] http://www.combinedfleet.com/Akagi.htm

> "KAGA's air group consists of **18 A6M2 "Zeke", 18 D3A1 "Val" and 27 B5N2 "Kate"**. Additionally, **nine A6M2 "Zeke from the 6th Air Group**, destined to Midway's future garrison, **and two spare D3A1 "Val"** are embarked."
> —— [S9] http://www.combinedfleet.com/kaga.htm

> "SORYU's air principal air group consists of **eighteen A6M2 "Zeke" fighters, sixteen D3A1 "Val" dive-bombers, eighteen B5N2 "Kate" attack planes**. Also aboard for the voyage were **three A6M2 "Zeke" fighters assigned to the 6th Air Group** to base at Midway. **One, possibly two, experimental D4Y1 carrier bombers** was aboard to serve as high speed recon aircraft."
> —— [S10] http://www.combinedfleet.com/soryu.htm

> **飞龙编制：combinedfleet 飞龙 TROM 未列航空队编制**（该 TROM 是 2000 年早期版，篇幅短，只写行动）。
> 飞龙的机数只能由 [S3] NavWeaps（18 零战 / 18 舰爆 / 17+1 舰攻 / 3 架第六航空队零战）给出。
> `work/raw/ijn-weapons.md` §8-A 里飞龙那一行的来源标的是 E 级（维基），**按本站规矩不能作 fact 来源**，
> 本次已用 [S3] 替代，主会话请勿回退到维基那一条。

**四舰合计（本报告算术，非来源结论）**：约 54+63+52+54 架主编制 + 21 架第六航空队零战 + 2 架备用舰爆 + 1~2 架彗星 ≈ **248 架**。
与 NHHC 的「248 aircraft」吻合，但这 248 是 [S2] 的独立口径，**别把我的加法当成它的出处**。

### A.2 美方三航母各中队飞机数（含 operational 数）

来源同 [S3] NavWeaps（**这一份是全站唯一标了 operational 数的**，NHHC 战斗序列只给编制数）。

**约克城号 USS Yorktown (CV-5)** — 舰长 Capt. Elliott Buckmaster；航空团指挥官 Lt.Cdr. Oscar Pederson

> "VS-5 / Commanding officer: Lt. Wallace Clark Short, Jr. / **Notes: 19 (17 operational) x SBD-3.**"
> "VF-3 / Commanding officer: Lt.Cdr. John Smith Thach / **Notes: 27 (25 operational) x F4F-4.**"
> "VB-3 / Commanding officer: Lt.Cdr. Maxwell Franklin Leslie / **Notes: 18 (17 operational) x SBD-3.**"
> "VT-3 / Commanding officer: Lt.Cdr. Lance Edward Massey †(killed) / **Notes: 15 (12 operational) x TBD-1.**"

**企业号 USS Enterprise (CV-6)** — 舰长 Capt. George D. Murray；航空团指挥官 Lt.Cdr. C. Wade McClusky Jr.

> "Air Group Commander / Commanding officer: Lt.Cdr. McClusky, Jr. / **Notes: 1 (1 operational) x SBD-3.**"
> "VF-6 / Commanding officer: Lt. James Seton Gray, Jr. / **Notes: 27 (27 operational) x F4F-4.**"
> "VS-6 / Commanding officer: Lt. Wilmer Earl Gallaher / **Notes: 18 (18 operational) x SBD-3.**"
> "VB-6 / Commanding officer: Lt. Richard Halsey Best / **Notes: 18 (18 operational) x SBD-2, -3.**"
> "VT-6 / Commanding officer: Lt.Cdr. Eugene Elbert Lindsey †(killed) / **Notes: 14 (14 operational) x TBD-1.**"

**大黄蜂号 USS Hornet (CV-8)** — 舰长 RA Marc A. Mitscher；航空团指挥官 Cdr. Stanhope C. Ring

> "Air Group Commander / Commanding officer: Cdr. Ring / **Notes: 1 (1 operational) x SBD-3.**"
> "VF-8 / Commanding officer: Lt.Cdr. Samuel Gavid Mitchell / **Notes: 27 (27 operational) x F4F-4.**"
> "VS-8 / Commanding officer: Lt.Cdr. Walter Fred Rodee / **Notes: 16 (15 operational) x SBD-3.**"
> "VB-8 / Commanding officer: Lt.Cdr. Robert Ruffin Johnson / **Notes: 18 (18 operational) x SBD-3.**"
> "VT-8 / Commanding officer: Lt.Cdr. John Charles Waldron †(killed) / **Notes: 15 (15 operational) x TBD-1.**"

**三舰合计（算术）**：F4F-4 81 架（25+27+27 编制；79 operational）、SBD 109 架（19+18+18+1+16+18+1）、TBD 41 架（12+14+15 operational = 41，恰好全部可用）。

> ⚠️ **约克城号的 SBD 数有内部口径差**：NavWeaps 与 NHHC 战斗序列都写 VS-5 19 / VB-3 18，
> 而约克城号行动报告自己写 "**VS-5 - 18 SBD's** / **VB-3 - 18 SBD's**"，出击时又写 "17 VSB, 12 VTB and 6 VF"。
> 三套数字（编制 19+18 / 报告编成 18+18 / 出击 17+12）并存，`work/raw/usn-weapons.md` §7.9 已记过同一处矛盾。
> **不要裁决**，写「编制 19/18，报告列 18/18，当日实际出击 17 架 SBD」。

**中途岛岸基航空兵（对照用，[S3] 原句）**

> "VMF-221 / **21 (20 operational) x F2A-3** … **7 (6 operational) x F4F-3**"
> "VMSB-241 / **19 (18 operational) x SBD-2** … **21 (14 operational) x SB2U-3** / Notes: **Only 12 crews.**"
> "VT-8 Detachment / Commanding officer: Lt. Langdon Kellogg Fieberling †(killed) / **Notes: 6 x TBF-1.**"
> "VP-23 / **Notes: 14 (13 operational) (11 search) x PBY-5**"
> "VP-44 / Notes: **8 (7 operational) (7 search) x PBY-5A.**"
> "VP-24 / Notes: **6 (6 operational) (3 strike, 2 search) x PBY-5A.**"
> "VP-51 / Notes: **3 (3 operational) (1 strike, 2 search) x PBY-5A.**"

> **VMSB-241 的 SB2U-3「21 (14 operational)」而「Only 12 crews」**——这是全表最值得写进正文的细节：
> 飞机比机组多。任务书旧稿 §1.7 写「SB2U-3 ×11」，与 [S3] 的 21 架/14 可用/12 机组冲突，
> 而 ONI [S1] ch6 写「a second under Maj. Benjamin W. Norris with **12 SB2U-3's**」。
> **三说并列**：21 架编制（[S3]）/ 14 架可用（[S3]）/ 12 架出击（[S1]）。

### A.3 双方飞机损失明细

#### A.3.1 日方：官方战斗详报的「空中损失」只有 44 架——这是理解口径分歧的钥匙

南云战斗详报的 Table 8「Damage Sustained — Aircraft」逐舰逐波次列出，**Grand total: 44**。
原表结构（[S4] https://www.ibiblio.org/hyperwar/Japan/IJN/rep/Midway/Nagumo/Table8.html）：

| 波次 | 零战（赤/加/飞/苍） | 舰爆（赤/加/飞/苍） | 舰攻（赤/加/飞/苍） | 合计 |
|---|---|---|---|---|
| 对中途岛攻击 Attack on Midway | 1 / 1 / – / – | – / 1 / – / – | – / – / 4 / 1 | **8** |
| 战斗巡逻 Air cover | 2 / 4 / 4 / – | – | – | **10** |
| 对敌航母第一次攻击 First attack | – / – / 3 / – | – / – / 13 / – | – | **16** |
| 对敌航母第二次攻击 Second attack | – / 1 / 2 / – | – | – / – / 5 / – | **8** |
| **总计** | | | | **44** |

> 原句（表脚）："**Grand total: 44.**"

**这个 44 是「飞出去没回来」的机数，不含随舰沉没的飞机。**
而 [S2] NHHC 说 "All 248 carrier aircraft were lost, most going down with their ships"。
**两个数不矛盾，统计对象不同**：44 = 空中战损；248 = 编制总数（其中约 200 架随舰沉没）。
主会话写损失时必须把这两个词分开，否则读者会以为来源打架。
（44 与 248 之差 = 204，**这是我的算术，不是任何来源的结论**，只用于说明两个数不冲突。）

#### A.3.2 日方：逐舰阵亡数——四套口径并列

**口径一：南云战斗详报本人（JST，5 日制）**

> "Personnel (killed in action):
> **Akagi:** Warrant officers and above 8 / Petty officers and men 213 / **Total 221**
> **Kaga:** Captain, officers, and men ¹800
> **Hiryu:** ComDiv, captain, warrant officers, and above 29 / Petty officers and men 387 / **Total 416**
> **Soryu:** Captain, warrant officers, and above 35 / Petty officers and men 683 / **Total 718**"
> —— [S4] https://www.ibiblio.org/hyperwar/Japan/IJN/rep/Midway/Nagumo/Table8.html （同页 Part V）

**口径二：combinedfleet TROM（Tully）**

| 舰 | 阵亡 | 原句 |
|---|---|---|
| 赤城 | 263 | "while only **263** petty officers and men are lost" [S8] |
| 加贺 | 814 | "She suffers a loss of **814** officers, petty officers, and men." [S9] |
| 苍龙 | 713 | [S10]（[旧稿] §4.1 已录） |
| 飞龙 | 418（Tully 注：扣除战俘后实为 383） | "A total of **418** officers, petty officers and men are listed as lost with the carrier, but this does not appear to exclude the POWs, so the actual figure would be **383** lost." [S12] |

**逐项对照**：赤城 221（详报）vs 263（Tully）；加贺 800（详报）vs 814（Tully）；
飞龙 416（详报）vs 418/383（Tully）；苍龙 718（详报）vs 713（Tully）。
**四舰全部不一致，但每舰差距都不大**——说明详报的数字是原始上报数，Tully 的是核对后的修正数。**不裁决。**

**口径三：USSBS 一手访谈（分舰口语估计）**

> 加贺：「A. **About 800 lost.** About 1000 saved.」—— [S14] IJO-1（天城孝久，加贺飞行长）
> 赤城：「A. **200 were lost, 100 were wounded** out of 1400 on board.」—— [S16] IJO-4（青木泰二郎，赤城舰长）
> 苍龙：「A. Two or three destroyers rescued about 600 men. **About 700 were lost** including about 30 pilots.」—— [S17] IJO-39（小原久，苍龙副长）
> 飞龙：「A. About 60 pilots and **a total of 500 men of crew of 1500**.」—— [S18] IJO-2（川口进，飞龙航空参谋）

**口径四：尼米兹报告转引（ONI 1943 年叙述）**

> "Estimated total number of personnel lost: **4,800**." —— [S1] ch13
> 另有山本幕僚（渡边安次）的估计：「**The total lost was about 4,500.**」—— [S32] IJO-13

**四个总数并列**：2,208（Tully 四舰相加，[旧稿] 已算）/ 约 3,000+（[S2] "Over 3,000 Japanese sailors"）/
4,500（IJO-13）/ 4,800（ONI [S1]）。**差距近一倍，主因是「是否含三隈号与巡洋舰部队」，本文不裁决。**

#### A.3.3 日方飞行员阵亡：**重点分歧，五说并列**

| # | 说法 | 原句 | 来源 |
|---|---|---|---|
| 1 | **110 名（36 舰上 + 74 空中）** | "most Japanese pilots were rescued; **only 36 were lost on the carriers and 74 in the air, mostly from Hiryu**." | [S2] NHHC H-006-1 |
| 2 | **over 100** | "the Japanese lost **over 100 trained pilots**, who could not be replaced." | [S19] NHHC Midway overview |
| 3 | **赤城 6 名** | "Q. How many pilots were saved; how many were lost? A. **Six pilots were lost.** Others landed and were picked up by destroyers." | [S16] IJO-4 |
| 4 | **加贺约 40 名阵亡（50% 生还）** | "Q. How many pilots saved? A. **About 40 pilots. About 50% pilots saved.**" | [S14] IJO-1 |
| 5 | **苍龙约 30 名** | "About 700 were lost **including about 30 pilots**." | [S17] IJO-39 |
| 6 | **飞龙约 60 名** | "Q. How many men and pilots were lost on the Hiryu? A. **About 60 pilots** and a total of 500 men of crew of 1500." | [S18] IJO-2 |
| 7 | **30% 阵亡、40% 负伤** | "A. **30% of the pilots were killed and 40% were injured.**" | [S15] IJO-64（高田利种，第三舰队参谋） |

**并列结论（不裁决）**：
- 逐舰相加 6+40+30+60 = **136**（本报告算术），与 [S2] 的 110 差 26 名；
- [S2] 的 110 是「舰上 36 + 空中 74」，即按**死亡地点**分；逐舰访谈是**按所属舰**分，两种切法不能直接比。
- 第 7 条的「30%」是**生还飞行员总数**的百分比，而中途岛后飞行员总基数未获取，所以**无法换算成绝对数**——不要硬算。

#### A.3.4 美方：飞机损失与阵亡

**总口径（尼米兹报告，经 ONI 转引）**

> "Ships: **Yorktown and Hammann sunk.** Planes: **About 150 lost in action or damaged beyond repair.** Personnel: **92 officers and 215 men.**"
> —— [S1] ch13（用户口径：307 人）

**逐舰逐中队（行动报告原始清单，A 级）**

**企业号**（[S5] https://www.history.navy.mil/research/archives/digital-exhibits-highlights/action-reports/wwii-battle-of-midway/uss-enterprise-action-report.html）

> "3. Aircraft losses as the result of 3 days action: **Torpedo SIX (Ten (10))** … **Bombing SIX (Eleven (11))** … **Scouting SIX (Nine (9))** … **Fighting SIX (One (1))**"

企业号报告**逐架列了 Bureau No.**（如 "6T1 - TBD-1 / 0289"、"6B3 - SBD-3 / 4682"），
这是全战役唯一能查到单机机号的损失清单，武器页/战史页要做「逐机」叙事时用这一份。
合计 **31 架**（10+11+9+1）。**注意这 31 架里有相当一部分是「油尽迫降/降落损毁」而非被击落**，
报告自己在 [S1] ch7 里说："Of the 33 SBD's, 18 failed to return, but **it is thought that most of these were forced down on the water when they ran out of fuel**."

同时，企业号报告人员损失清单也逐名列了（飞行员 + 后座机枪手的姓名、军衔、服役号），
例：`6T1 | LtCdr. E.E. Lindsey, USN. | GRENAT, C.T., 279 45 11, ACRM, USN.`
—— **本站要写「人名级」伤亡表，这份是唯一 A 级来源。**

**大黄蜂号**（[S6]）

> "Own losses: **15 TBD on 4 June (1 pilot rescued).** / **12 F4F-4 on 4 June (6 pilots rescued).** / **5 SBDs 4-6 June (4 pilots and 4 RM rescued).**"

**约克城号**（[S7]）

> "(b) Planes lost by Air Group. / **9 VF lost (5 shot down, 2 crashed on deck and two lost on Yorktown pilots missing two.** / **8 VSB lost on Yorktown, no pilots missing.** / **10 VT lost in vicinity of enemy fleet, Pilots missing 10; rear seat men 10, killed one.**"
> 另一处：「2 VSB landed in water, no pilots missing.」

（原文 `9 VF lost` 那句标点混乱，是原始转录问题，照抄不改。）

**美方飞行员/空勤阵亡**：

> "**Well over 150 U.S. aviators**, most of them Navy, made the ultimate sacrifice in winning one of the greatest battles of all time."
> —— [S2]

> "Of the **99 men in the 42 torpedo planes** that were lost, **only three survived** the battle." —— [S2]
> （这一句是「鱼雷机空勤几乎全灭」的最强原句，比「TBD 全灭」更狠：**99 人只活 3 个**。）

**岸基航空兵损失明细（[S1] ch5、ch6 原句，可与 [旧稿] §4.2 对表）**

> "Of the **27 fighter planes** of the Marine air group which intercepted the enemy bombers, **15 were missing and 7 severely damaged**."
> 脚注："Missing in action: **13 F2A-3's and 2 F4F-3's**. Severely damaged: **5 F2A-3's, and 2 F4F-3's**."
> —— [S1] ch5

> "Of the **16 SBD's** which engaged in this attack, **8 returned to the base**, and of these **only 6 remained fit for service**." —— [S1] ch6

> "Of this flight **only one badly shot-up plane returned** to make a landing with one wheel retracted."（6 架 TBF）—— [S1] ch6

> "Of the two B-26's lost, one was seen to launch its torpedo and then to strike the flight deck of the carrier and hurtle into the sea." —— [S1] ch6

> "**Two of our planes were forced to land in the water** before reaching Midway, but two pilots and a gunner were rescued."（SB2U）—— [S1] ch6

NHHC 另给了一个更完整的岸基损失口径（可补 [S1] 未覆盖的空勤数）：

> "Only minutes before the attack by the TBFs and B-26s … Nagumo would not know until the strike recovered aboard just how badly it had been shot up by Midway's defenses: **11 aircraft shot down, 14 severely damaged, 29 hit, (almost half the strike lost or damaged), and 20 aviators killed or missing.**"
> —— [S20] https://www.history.navy.mil/about-us/leadership/director/directors-corner/h-grams/h-gram-006/h-006-3.html

> 这一条是**日方视角的损失**（日军第一波对中途岛的损失），不是美方。放在这里是因为它是唯一给出
> 「日方第一波被岸基火力打掉多少」的精确数字，且 `midway.yaml` 现有 timeline 完全没有这条。

---

## B. 舰载机与武器技术细节

### B.1 日方三型机的中途岛挂弹配置

#### B.1.1 九九式舰爆 D3A1

**中途岛当日实挂：八〇番陆用爆弹（805 kg）**

> "SORYU contributes eighteen D3A1 "Val" **armed with Type # 80 land bombs** and nine A6M2 "Zekes.""
> —— [S10] http://www.combinedfleet.com/soryu.htm

**弹种定义（南云战斗详报脚注，是全战役最权威的日方弹种原句）**

> "Bomb types mentioned on this and succeeding pages are as follows:
> **No. 25 land bomb, total weight 242 kg.**;
> **No. 25 ordinary bomb, total weight 250 kg.; for use against ships**;
> **No. 80 land bomb, total weight 805 kg.**"
> —— [S4] https://www.ibiblio.org/hyperwar/Japan/IJN/rep/Midway/Nagumo/

**这三种弹的分工，直接对应中途岛的核心技术问题**：
- **No. 80 陆用爆弹 805 kg** = 对**陆地目标**（中途岛机场）用 → 第一波舰爆挂的就是这个；
- **No. 25 通常弹 250 kg** = 对**舰船**用 → 换弹命令要换成的就是这一型；
- **No. 25 陆用爆弹 242 kg** = 陆用版，比通常弹轻 8 kg。

> ⚠️ **这里有个此前没被点破的技术细节**：No.25 陆用弹（242 kg）与 No.25 通常弹（250 kg）**几乎同重**，
> 所以「换弹」这个动作在**弹重上几乎没有区别**，区别在**引信与弹体**（陆用弹是薄壳高爆、触发即炸；
> 通常弹是半穿甲、延时引信）。这解释了为什么换弹作业要重来一遍却不能「凑合」——
> 但**「为什么不能凑合」这一点没有任何来源明说，是我从两条弹重数据推的，不作为结论写入**。

**D3A1 的常规挂弹（技术页用）**：机身下 1 × 250 kg、机翼 2 × 60 kg，
投弹方式为「挂臂下摆前送后投放」。这些数据已在 `work/raw/ijn-weapons.md` §6-F 采集完毕（来源 [S21] combinedfleet D3A、[S22] aviation-history），**本次不重复**。

#### B.1.2 九七式舰攻 B5N2

**第一波对中途岛：挂八〇番陆用爆弹**

> "the air strike led by Lt. (later KIA, Cdr posthumously) Tomonaga Joichi (59) is launched against Midway Island with **36 B5N2 "Kate", 36 D3A1 "Val" and 36 A6M2 "Zeke"**"
> —— [S9]（加贺 TROM，四舰共用同一句）

**第二波对舰：换回鱼雷**

> "After the 1 Assault Unit departed, the carrier-based torpedo-carrying assault planes ware equipped with **torpedo armaments** as a precautionary measure against the surface naval craft of the enemy. … It was decided to direct the second attack towards MIDWAY, and **the torpedo armaments of the carrier-based torpedo-carrying assault planes were ordered to be shifted to No 80 land bombers**."
> —— [S4]（JM-93 同一段，注意这段是 JST 记时）

**飞龙反击两波的编成（南云详报 Table 1，最权威）**

> "**First Attack on Enemy Carriers**
> 14th Attack Unit / Hiryu Division Comdr. / **f b x 18** / Notes: 2 planes of the Air Control Unit encountered and destroyed enemy torpedo planes en route, and did not join in the attack.
> 4th Air Control Unit / Hiryu Division Comdr. / **f c x 6**
>
> **Second Attack on Enemy Carriers**
> 4th Attack Unit / Air Officer Hiryu / **f o x 9** / Notes: **Akagi's attack planes failed to use their torpedoes and brought them back.**
> Akagi Attack Planes / Warrant Officer Nishimori / **f o x 1**
> 4th Air Control Unit / Division Comdr. Hiryu / **f c x 4**
> Kaga Air Control Unit / A Yamamoto / **f c x 2 ¹**"
> —— [S4] Table 1（`f o` = attack plane 舰攻；`f b` = bomber 舰爆；`f c` = fighter 战斗机）

> **「Akagi's attack planes failed to use their torpedoes and brought them back.」**
> 这一句极其重要：飞龙第二波里的**那 1 架赤城舰攻（准尉西森）挂了鱼雷但没投，带回来了**。
> 现有 `midway.yaml` 的 timeline 完全没有这条，而它是「赤城飞行队并未全员战死」的直接证据（[S14] 天城说赤城只损失 6 名飞行员，与此自洽）。

**B5N2 鱼雷型号**：九一式 800 kg（Type 91）。
`work/raw/ijn-weapons.md` §7-F 已采（来源 [S23] combinedfleet B5N）；NavWeaps 日本鱼雷页实测含
`45 cm Type 91 (1931) Mod 1 / Mod 2 / Mod 3` 条目及一张图注「Type 91 mod 2 Torpedoes on the carrier Akagi in November 1941」
（[S24] https://www.navweaps.com/Weapons/WTJAP_WWII.php）——**这条图注是「赤城带的就是九一式改二」的旁证，
但 NavWeaps 未给中途岛当日的具体型号，写作时不要断言是 Mod 2 还是 Mod 3。**

#### B.1.3 零战 21 型 A6M2

**中途岛配置：纯制空，无挂弹记录。**

三型机里零战的参战配置最简单：36 架护航第一波、各舰 CAP。所有已查来源**均未记载中途岛零战挂载炸弹**
（对比：1944 年之后才有战斗爆击机改型）。技术要求里若写「零战可挂 60 kg 炸弹」，那是**机型能力**不是**当日配置**，
两者必须分开，否则会误导。

### B.2 美方三型机的中途岛挂弹配置

#### B.2.1 SBD 无畏（SBD-2 / SBD-3）

**企业号当日实挂三档（最细的原句，直接可作正文）**

> "Of the scout bombers, **15 carried one 1,000-pound bomb each, 12 carried one 500- and two 100-pound bombs, and 6 carried one 500-pound bomb each**."
> —— [S1] ch7（ONI 叙述）

企业号行动报告自己的写法（分波次）：

> "**15 VSB armed with one 1000 lb. bomb each.** / **12 VSB armed with one 500 lb. bomb and two 100 lb. bombs each.** / **6 VSB armed with one 500 lb. bomb each.** / **14 VTB armed with torpedoes.**"
> —— [S5]

**约克城号 VB-3 实挂：17 架各 1 × 1,000 lb，引信 Mk 21 / Mk 23**

> "The dive bombing attack group consisted of **17 SBD's of VB-3, each armed with 1-1000 pound bomb, fused with Mk 21 and 23 fuses**."
> —— [S7]

**大黄蜂号**（报告写得较粗，只给量级）：

> "At 090 … commenced launching the Air Group for attack; **VSB loaded with 500-lb. bombs, VTB with torpedoes** and VF with M.G. ammunition only."
> —— [S6]

> **注意这里一个容易被误读的点**：同一场攻击，企业号的 VSB 有 1,000 lb / 500 lb+2×100 lb / 500 lb 三种挂法，
> 约克城号全部 1,000 lb，大黄蜂号一律 500 lb。**三舰挂弹不统一，是中途岛美军协同失调的一部分**，
> 不是记录错误。写「美军 SBD 挂 1,000 磅」这一句时必须限定是哪一舰。

**企业号弹药消耗（可用于「打了多少」的量化）**

> "4. Ammunition expended: Expended **57 1000-lb. bombs / 67 500-lb. bombs / 22 100-lb. bombs / 48,000 .50 caliber / 40,000 .30 caliber**"
> —— [S5]（三日合计）

#### B.2.2 TBD 蹂躏者

> "each torpedo plane carried **one MK13 torpedo**" —— [S1] ch7
> "The torpedo attack group consisted of **12 TBD's of VT-3, each armed with one MK 13 torpedo**." —— [S7]

**MK XIII 对 TBD 的性能致命性（NHHC 原句，武器页的核心引语）**

> "The slow TBDs (the aircraft had been "state-of-the-art" only four years previously), were **limited even further by the speed and altitude restriction of the Mk. 13 torpedo (100 knots, 100 feet)**, and they began to go down one after the other."
> —— [S20]

> 这条是本轮**最有价值的单句**：它把「TBD 为什么被打得这么惨」从「飞机老」推进到
> **「鱼雷的投放包线（100 节 / 100 英尺）把飞机锁死在低空低速」**——这是技术因果，不是勇气问题。

#### B.2.3 F4F 野猫

中途岛三航母全部 F4F-4（VF-3 25 / VF-6 27 / VF-8 27，[S3]）；岸基 VMF-221 另有 7 架 F4F-3
（[S3]："7 (6 operational) x F4F-3"）。**F4F-4 的 6 挺 .50 与 240 发/挺的取舍问题**，
`work/raw/usn-weapons.md` §4.6 已引约克城号行动报告的原句，本次不重复。

**中途岛新增的一条：野猫的数量劣势是算术问题，不是性能问题**

> "The Brewster Buffalos were no match for the protecting Zeros and there were not enough Wildcats. **Seventeen of the twenty-eight American fighters were shot down** and seven damaged for the loss of a few Japanese bombers."
> —— [S11]

> "**All VMF pilots** of various degrees of experience and capability **were awed by the performance of the Zero** I Sento K1 fighter, claiming that it has **20 percent more speed, climb, and maneuverability** than does the F2A-3 or F4F-3."
> —— [S1] ch5（引麦考尔少校报告）

> "**No local pilot has yet observed a fighter type aircraft with such versatility**.... The only way our pilots could shake them off was to dive at speeds better than 400 knots, or to use cloud cover."
> —— [S1] ch5（引凯姆斯中校报告）

### B.3 TBD 几乎全灭：三队各自结局的原句（本块核心）

**VT-8（大黄蜂，15 架，Waldron）——全灭，1 人生还**

> "As Torpedo EIGHT drove in toward the target it encountered overwhelming fighter opposition. … One by one our planes fell, but those that were left pressed home the attack. … **Of the 15 planes, not one returned from the attack. Only one pilot, Ensign George H. Gay, survived.**"
> —— [S1] ch7

> "**Torpedo 8, led by Lieutenant Commander John C. Waldron, U.S.N., was lost in its entirety.**" —— [S6]（大黄蜂号行动报告，舰长 Mitscher 亲笔）

> "**15 TBD on 4 June (1 pilot rescued).**" —— [S6]（同一份报告的统计行）

**VT-6（企业号，14 架，Lindsey）——14 架出击，4 架返回**

> "Of the **14 planes in the Enterprise squadron (VT-6) only 4 returned**" —— [S1] ch7

> "the enemy fighter opposition was so strong and effective that **ten torpedo planes out of fourteen of Torpedo Squadron SIX did not return**." —— [S5]

> "By the time VT-6's attack was over around 1000, **nine TBDs had been shot down, and five torpedoes had failed to hit Kaga**" —— [S20]

> ⚠️ **10 架未返 vs 9 架被击落：差 1 架**。企业号报告说 10 架没回来（含迫降/失踪），NHHC 说 9 架被击落。
> 两者统计对象不同（未返 vs 被击落），**并列不裁决**。

**VT-3（约克城，12 架，Massey）——12 架出击，2 架确知脱离战场**

> "of the Yorktown's **12 planes constituting VT-3 only 2 survived the attack**." —— [S1] ch7

> "Only 5 VT dropped their torpedoes, as **7 were shot down during the approach and 3 more after the attack**." —— [S7]

> "**out of 12 TBD's sent into attack, only two are known to have left the vicinity of the battle. It is recommended that remaining TBD's be immediately replaced by TBF's.**"
> —— [S7]（**这句是「TBD 就此退役」的直接决策依据，武器页必引**）

> "It is believed that this engagement showed clearly **the vulnerability of TBD's**" —— [S7]

**三队合计与「全灭」的准确表述**

> "Four waves of U.S. torpedo bombers (six new TBF Avengers and four USAAF B-26 Marauders from Midway, and 41 older TBD Devastators in three squadrons from the carriers) suffered grievous losses likened to the Charge of the Light Brigade, each wave encountering between 15 and 30 Zero fighters, **but not one torpedo bomber turned away**."
> —— [S2]

> "**only six of the TBDs made it back to the carriers; only three of the aircraft were flyable.** **Of the 99 men in the 42 torpedo planes that were lost, only three survived the battle.**"
> —— [S2]

> **写作警示**：「TBD 全灭」是**错的**——6 架返回了。准确说法是
> 「41 架出击、35 架损失、6 架返回（3 架仍可用）」。
> 而「**42 架鱼雷机 99 名空勤只活 3 人**」才是真正接近「全灭」的那一句，且它把中途岛的 6 架 TBF 也算进去了。
> 两句都要引，别只引一句。

**另一方视角的交叉验证（日方对美军鱼雷机攻击的记录）**

> "0310? … Enemy torpedo planes attacked both sides of KAGA in an "anvil" attack. But assisted by CAP the carrier **dodges a total of six torpedoes**, the "Zeke" CAP **shooting down 10 out of the 14 attacking aircraft**."
> —— [S9]

> 日方记「打下 14 架中的 10 架」，美方记「14 架中 4 架返回」。**两边数字对上了**——这是本轮少见的两源完全吻合的一处。

---

## C. 雷达与发现顺序

### C.1 美方 CXAM：四次接触，全部是防御性

来源 [S11] Engineering and Technology History Wiki《Midway — Chapter 7 of Radar and the Fighter Directors》
<https://ethw.org/Midway_-_Chapter_7_of_Radar_and_the_Fighter_Directors>（C 级，二手，但逐条给了页码级引用 [15][33]）

**接触一：06-04 0815，企业号 CXAM 发现利根 4 号机（距 30 英里，方位 185°）**

> "At **0815 Enterprise CXAM operators found a contact at thirty miles on bearing 185 degrees. It was Tone's Number 4 float plane** still looking for the task force."
> 后文："Because of low altitude cloud cover, **Red 17 did not spot the float plane, and Tone No. 4 was able to get off another report saying the formation did indeed include one carrier**."

> 这一条极重要：**美军雷达发现了日方侦察机，但战斗机没拦到，侦察机把「这里有航母」发出去了**。
> 中途岛的第一个「谁先发现谁」的答案在这里——**日方侦察机先看到了美方航母，美方雷达先看到了日方侦察机，但没能阻止它发报**。

**接触二 & 三：约克城号 CXAM 两次预警飞龙反击**

> "At **1159 radar picked up a large number of planes, estimated at 30 or 40, on bearing 250° at a distance of 46 miles**."（[S1] ch8 同句）
> "**Yorktown's CXAM operator picked up the attackers at thirty-two miles, bearing 225 degrees; following the returning strike force.**"

> "Again they found Yorktown, whose **CXAM radar at about 1430 detected them at forty-five miles range**."

**接触四：彭萨科拉号接替雷达警戒（约克城失去电力后）**

> "the **Pensacola, which had assumed radar guard after the Yorktown was damaged, picked up enemy planes bearing 340°, distance 33 miles**." —— [S1] ch8

> 这一条说明**美军雷达警戒是「舰—舰移交」的**：约克城被打瘫后，雷达警戒交给巡洋舰。
> 这是写「雷达在战役中的作用」时最容易被漏掉的一环——**雷达的价值不在单舰，在编队的接力**。

**CXAM 的物理边界（一句话给技术页）**：ethw 引用的原句把 CXAM 与中途岛的岸基雷达并列：

> "a Midway-based **SCR-270 radar, a close cousin of the CXAM**, detected the raid."

NavWeaps 雷达页对 CXAM 的定位（型号学层面，非战役数据）：

> "The prefixes 'X' and 'CX' were reserved for the Navy (NRL) and commercially produced experimental or preproduction sets, eg **CXAM, the first US naval radar**."
> —— [S25] https://www.navweaps.com/Weapons/WNUS_Radar_WWII.php

### C.2 中途岛岸基雷达：0593/0553 的第一道警报

> "Five minutes later the **Midway radar picked up the planes at a distance of 93 miles, altitude about 10,000 feet**." —— [S1] ch5（时标 0545 之后五分钟 ≈ 0550）

> "At 0545 'the most important contact of the battle' was made. A patrol plane reported **in plain English (the first use of it in the battle): "Many planes heading Midway, bearing 320, distance 150."**"
> —— [S1] ch5

NHHC 给的时刻略有不同（0553 vs 0550），并有「谁先谁后」的完整链条：

> "At **0530**, a PBY flown by Lieutenant **Howard P. Ady** sighted Japanese ships northwest of Midway and issued a sighting report at **0534**. At **0545** another PBY, flown by Lieutenant **William Chase** sighted the inbound Japanese air strike and reported "many aircraft heading Midway." Several minutes later, at **0552**, Chase sighted two of the Japanese carriers. **Midway radar detected the incoming strike at 0553.**"
> —— [S33] https://www.history.navy.mil/about-us/leadership/director/directors-corner/h-grams/h-gram-006/h-006-2.html

> ⚠️ **ONI 说雷达 0550（"five minutes later"），NHHC 说 0553，两说并列。**
> 更关键的是**顺序**：NHHC 的版本是「PBY 目视 0545 → PBY 目视航母 0552 → 岸基雷达 0553」，
> 即**雷达比目视晚了 8 分钟**。这与「雷达是先发现者」的通行印象相反，主会话写的时候要照实写。

**中途岛防御阵地的雷达原始记录（香农中校的战斗日志，逐条时刻）**

> "**0629** Radar to Bn: "Many unidentified planes 8 miles, 330° and 29 miles, 265°".
> **0630** Radar to Bn: "Many unidentified planes 27 miles, 250°".
> **0637** Radar to Bn: "Few unidentified planes 20 miles, 245° and 21 miles, 235°. Also 9 miles, 330°".
> **0653** Radar to Bn: "Many planes 9 miles, 235° and 27 miles, 315°. Many planes 33 miles, 310°"."
> —— [S1] ch5（引 Lt. Col. Harold D. Shannon 战斗日志）

> 这份日志是**全战役唯一按分钟记录的雷达操作实录**，写「雷达怎么用」时的第一手材料。

### C.3 日方几乎没有雷达：四份一手证言 + 三份官方文件

**这是本轮找到的「对比原句」最齐的一块，四份 USSBS 一手访谈 + 一份日方官方战史 + 两份 NHHC 综述，互相印证。**

**（1）日方官方战史（战后美方编译，JM-93）——最权威的一段**

> "At the outbreak of the war, **the Navy did not have ship radar**. As a result of earnest study and progress in preparations, the Navy finally completed the installation of radar equipment **on the battleships, ISE and HYUGA, on 27 May**, just prior to the beginning of this operation. **The radar range was about 60 to 100 km at that time.**"
> —— [S26] https://www.ibiblio.org/hyperwar/Japan/Monos/pdfs/JM-93_MidwayOperations,May-June42/JM-93.htm

> 注意：27 May 装的是**战列舰伊势、日向**，两舰都不在中途岛战场（在阿留申方向的北方部队）。
> 所以这句话的实际含义是：**中途岛战场上，日方主力（机动部队）一艘雷达都没有。**

**（2）赤城舰长青木泰二郎（最直接的一句）**

> "Q. Did you have radar on the Akagi? **A. No.**
> Q. Did any ships at MIDWAY have radar? A. **Yamato, Mutsu and Nagato in the Grand Fleet may have had it. There was no ship at MIDWAY or carrier which had it.**"
> —— [S16] https://www.ibiblio.org/hyperwar/AAF/USSBS/IJO/IJO-4.html

**（3）飞龙航空参谋川口进（给了「什么时候才装上」）**

> "Q. Did the Hiryu of any of the other carriers or ships have radar? **A. No, not any. As soon as we got back they put them on the carriers. July 1942 both battleships and carriers received them.**"
> —— [S18] https://www.ibiblio.org/hyperwar/AAF/USSBS/IJO/IJO-2.html

**（4）加贺飞行长天城孝久（说清了「有雷达也用不好」）**

> "Q. How did the control officer know where to send the fighters? A. **By radar. It was an experiment at MIDWAY. Not too good.**
> Q. Did the Kaga have it? **A. No, island too small.**
> …
> Q. What did the radar look like? A. **It was a big wire grid. Kept rotating. Didn't work very well. Destroyers act as pickets and advise by voice radio if planes are coming.**"
> —— [S14] https://www.ibiblio.org/hyperwar/AAF/USSBS/IJO/IJO-1.html

> ⚠️ **天城这一条内部有矛盾**：他先说「用雷达指挥战斗机」，又说「加贺没有雷达」「中途岛时是实验、不太好」。
> 合理解读是「整个机动部队有极少量实验性雷达、加贺本舰没有」，但**他的原话没这么说**。
> **不裁决**，两句都引，让读者自己看这个矛盾——这本身就是「日方雷达状况混乱」的证据。

**（5）山本幕僚渡边安次**

> "Q. Did you have radar installed on your ships at the Battle of MIDWAY? **A. No, about August 1942 it was installed.**"
> —— [S32] https://www.ibiblio.org/hyperwar/AAF/USSBS/IJO/IJO-13.html

**（6）NHHC 综述的两句对比（可直接作正文对句）**

> "**Although the Japanese battleships were fitted with radar, their carriers had none, and they had no advance warning of the incoming dive bombers, and no time to prepare.**"
> —— [S11]

> "**With no radar, unreliable radios, and no real shipboard fighter direction of any kind, the Japanese fighters were pretty much on their own once they left the deck**"
> —— [S20]

> 这一句把「无雷达」的**战术后果**说透了：不是「看不见」，是「**没有战斗机引导体系**」。
> 美方的 CXAM + FDO（战斗机引导官）是一套**人和机器绑定的系统**，日方缺的是整个系统，不是一台机器。

**（7）反事实判断（ethw 的战果评估，C 级，标清层级再用）**

> "Battle analysts have concluded that the critical element in the sinking of the four Japanese carriers was **surprise by the U.S. dive bombers**. **If the Japanese carriers had radar equivalent to the American CXAM they most likely would not have been surprised**, and the battle probably could have come out much differently."
> —— [S11]

### C.4 PBY 卡特琳娜的侦察发现（6-03 与 6-04）

**6 月 3 日：三次水面接触 + 人类史上第一次夜间巡逻机鱼雷攻击**

> "At **0904** the first surface contact of the battle was reported by a patrol plane: "**Two Japanese cargo vessels sighted bearing 247° from Midway, distance 470 miles. Fired upon by antiaircraft.**"
> Shortly afterward, at **0925**, another plane reported: "**Main body bearing 261°, distance 700 miles, six large ships in column.**"
> At **1100** the same plane reported that this force consisted of **11 ships, course 090°, speed 19**. Actually, as it later proved, this was not the enemy's "main body," but probably only a portion of his occupation force."
> —— [S1] ch4

> "a flight of four PBY-5A's, each carrying one MK XIII Mod. I torpedo took off on an historic mission, "**the first night torpedo attack by our patrol planes on surface ships**." The pilots were volunteers, led by **Lt. William L. Richards**, Executive Officer of Patrol Squadron FORTY-FOUR."
> —— [S1] ch4

**PBY 上也有雷达（这是任务书没提到的）**

> "At about **0115** on June 4th, **radar indicated a group of about 10 ships 10 or 12 miles to the port of this group**. As our planes approached, the silhouettes of the enemy ships became visible in the moonlight."
> —— [S1] ch4

> **中途岛最早的雷达接触不是舰载 CXAM，是 PBY 的机载雷达**，时标 06-04 0115。
> 这一条 `midway.yaml` 的 timeline 里完全没有，且它比舰载雷达的第一次接触（0815）早了 7 小时。

**6 月 4 日：发现日方机动部队（三条报告、三个人名，NHHC 版本最完整）**

> "At 0530, a PBY flown by Lieutenant **Howard P. Ady** sighted Japanese ships northwest of Midway and issued a sighting report at **0534**. At 0545 another PBY, flown by Lieutenant **William Chase** sighted the inbound Japanese air strike and reported "many aircraft heading Midway." Several minutes later, at **0552**, Chase sighted two of the Japanese carriers."
> —— [S33]

**PBY 的搜索半径与战前部署（写「为什么能发现」用）**

> "By early June 1942, the **127 aircraft based on Midway Island included 31 PBY Catalina flying boats**, a few rigged to carry a torpedo. … **The PBYs began to fly missions out to 700 miles from Midway**"
> —— [S33]

> "They were ordered to **search to 425 miles unless four enemy carriers were discovered earlier**, and to report all contacts fully. They were ordered to **return to Laysan and Lisianski**, as keeping them on the scene of action would be to expose them unnecessarily."
> —— [S1] ch5

> ⚠️ **700 英里 vs 425 英里**：NHHC 说 PBY 飞 700 英里，ONI 说当天的命令是搜 425 英里。
> 两者不冲突（700 是极限能力，425 是当日命令），但**不能混写**。任务书旧稿若只引一个会失真。

**日方对 PBY 的记载（另一方视角，交叉验证）**

> "From about **0230** hours, **two or three flying boats of the enemy came into contact with our task force**." —— [S4] JM-93

> "**At 0430 hours** … one carrier-based torpedo-carrying assault plane each from the AKAGI and the KAGA, two Zero-type fleet reconnaissance planes each from the TONE and the CHIKUMA … **However, the departure of the TONE, as well as the CHIKUMA was greatly delayed, and the sixth search plane returned at 0235 hours because of poor weather conditions.**"
> —— [S4] JM-93（**JST**，换算成当地时要 −3h +1d）

---

## D. 战役后续影响

### D.1 日本海军航空兵力的长期损失

**（1）决定性损失不是飞行员，是航母 + 机务**

> "including **over 700 aircraft technicians/maintainers** (a very limited skill in the Japanese navy)" —— [S2]

> "It was **not the loss of pilots at Midway** that crippled Japan's ability to wage offensive naval operations, but rather **the loss of the most important Japanese strategic asset, the irreplaceable aircraft carriers**."
> —— [S2]

> "**Only one new Japanese fleet carrier would make it into a major fleet action during the war, only to be sunk by a U.S. submarine in her first battle.**" —— [S2]
> （指信浓号，1944-11-29 被射水鱼号击沉。）

**（2）飞行员：生还者被投入瓜岛消耗战（这是真正的长期损失路径）**

> "**Most of Japan's Pearl Harbor–veteran pilots would survive Midway only to perish in the meat-grinder battle of attrition in the skies around Guadalcanal and the Solomon Islands later in the year, where over 1,000 Japanese aircraft would be lost.**"
> —— [S2]

**（3）USSBS 第三舰队参谋高田利种的亲历（重建过程）**

> "After this Battle of MIDWAY they put **more emphasis on search training**." —— [S15] IJO-64
> "**30% of the pilots came back to JAPAN to convalesce, and 40% were shifted to the Third Fleet, at KYUSHU, to go into further training.**" —— [S15]
> "The Third Fleet was organized on 15 July and they figured two months were needed for their next operation; **but before they had enough time to reorganize, the GUADALCANAL picture came up and they were forced to send these pilots prematurely to RABAUL.**" —— [S15]
> "When they went down south, part of this original number of pilots were sent to RABAUL carriers; but after the battle of SANTA CRUZ they were brought back to JAPAN … **However, most of them were killed in action at PORT MORESBY, BUNA and SANTA CRUZ.**" —— [S15]

**（4）训练体系的崩坏路径（招魂式的因果链，一手）**

> "In 1943 we operated on the assumption that **50 percent of our flight personnel would be necessarily expended**. Before 1943, our estimate of the attrition rate had been **20 to 30 percent**. … **I believe the Battle of GUADALCANAL and the actions at RABAUL had more to do with the revision than the Battle of MIDWAY.**"
> —— [S13] IJO-31（胜又清三少将，航空教育系统）

> "Gasoline shortages necessitated **abandoning the intermediate phase of the pilot training program late in 1943. This increased operational losses.**"
> —— [S13]（该访谈的 SUMMARY 第 3 条，原句）

> "As the war progressed the quality of pilots deteriorated due to **insufficient training facilities, great attrition and a shortage of fuel for training** with the consequent necessity of using inadequately trained replacements."
> —— [S18] IJO-2

**（5）飞机损失的年度统计（IJO-50，唯一给出逐月「生产 vs 损耗」的一手数据）**

> "Commander FUKAMIZU had prepared a graph on which were plotted: (1) **Annual overall naval aircraft production and wastage totals from December 1941 to August 1945.** (2) Annual naval aircraft production and wastage totals by plane type …"
> —— [S27] https://www.ibiblio.org/hyperwar/AAF/USSBS/IJO/IJO-50.html

该页 Annex B 的表**逐月给出「生产/损耗」两列**（格式如 `137/70` = 该月生产 137 / 损耗 70），
且脚注 7 明确把 **1942 年 6 月标记为「Midway, Aleutians」**。

> **可直接引用的关键行**（Fiscal 1942 段，1942 年 6 月列）：
> Fighters `137/70`；Torpedo & Dive Bombers `189/12`；Medium Bombers `9/18`；Total `350/139`
> —— [S27] Annex B（**注意：这是「生产/损耗」，前者是产量不是存量，引用时别读反**）

> ⚠️ 这张表的 `a/b` 格式在该页正文中**没有图例说明**，我是从表头 "Number of Planes Expended = Combat Losses/Operational Losses"
> 与列位关系推断为「生产/损耗」的。**这是推断，不是来源断言**。主会话若要引用这张表，
> 建议只引「1942 年 6 月被标注为 Midway/Aleutians」这个事实，不要引具体数字，除非先去核对原表图例。

### D.2 美军的战略转折

> "Historical Importance of Midway: Most important battle in the Pacific War in terms of short and long-term effects / **Permanently wrecked IJN's elite carrier force** / **Restored parity of forces in Pacific** / **Allowed U.S. to undertake offensive actions—Guadalcanal, Solomons**"
> —— [S28] https://www.admiraltytrilogy.com/pdf/Hist2006_Parshall_Midway_Brief.pdf （Parshall 讲义第 4 页，四项要点）

> **这四条是 Parshall 的学术判断（C 级），不是一手档案**。但那句「Restored parity」有硬数据支撑：
> 中途岛后日方只剩 2 艘舰队航母（翔鹤、瑞鹤），美方剩 3 艘（企业、大黄蜂、萨拉托加），
> 这个「3 比 2」的算术不在本次采集范围内（未查航母存量表），**列未获取**。

**日方自己的判断（一手，比美方说法更有说服力）**

> "The loss of the carriers meant **loss of control of the air**. We did not think that we could capture MIDWAY after we lost air control, so we returned to JAPAN. The loss of the carriers and planes **also slowed up the occupation of the SOLOMONS**. If we had been stronger in the air, maybe we could have stopped some of your convoys to the SOLOMONS."
> —— [S17] IJO-39（苍龙副长小原久）

> "**I think failure of the MIDWAY Campaign was the beginning of total failure.**" —— [S15] IJO-64
> "the chief reason I can give is in the beginning of the war everything went on successfully until right before the MIDWAY Campaign, **which marked the end of the successful operation. They should have stopped to think of defense, to consolidate.**" —— [S15]

> "Q. What effect did the loss of the carriers have on your later plans? A. **Many planes and a number of pilots were lost in the action, which, weakened the Navy Air Force, requiring training to replace them.** The Army refused to take their pilots from MANCHURIA and CHINA during the SOLOMONS Campaign, therefore the Navy was required to furnish pilots in that area."
> —— [S32] IJO-13

**组织层面的后果：第一航空舰队被解散重组**

> "After the MIDWAY Campaign, as you know, **the First Air Fleet was very heavily damaged and we had to reorganize the Third Fleet.** I had the mission to reorganize the Third.Fleet." —— [S15] IJO-64

**作战层面的直接后果：中途岛攻略计划正式取消**

> "C. Operational Objectives Abandoned: In the battle on 4 Jun 42 all four carriers of the 1 and 2 Air Squadrons were lost, so the difficulty in continuing the operation was recognized. **On 11 Jul 42, the mission of the Commander-in-Chief of the Combined Fleet to capture MIDWAY, which had been based on Imperial General Headquarters Order No 18, was canceled.**"
> —— [S26] JM-93

### D.3 日方官方战报口径 vs 实际损失（宣传与事实的差异，原句）

这一块是本轮**最值得写进正文**的部分，因为三层「口径造假」都找到了原句，
而且**第三层最狠：日方自己的战斗详报里就把己方损失栏直接删掉了**。

#### 第一层：大本营公开发表（1942-06-10 15:30）

**日文原句（京都新聞引 1942-06-11《京都戦時新聞》第 4 号）**

> 「■ミッドウェー大戦果　**米空母２隻撃沈　１２０機撃墜**
> 【大本営発表（６月１０日午後３時３０分）】…
> 主な戦果
> （１）ミッドウェー方面　**米航空母艦エンタープライズ型１隻とホーネット型１隻撃沈**▽**飛行機約１２０機撃墜**▽重要軍事施設爆砕」
> —— [S29] https://www.kyoto-np.co.jp/articles/-/1734498

同一报道的编者按（现代表述，标明这是「虚構の戦果」）：

> 「開戦半年後のミッドウェー海戦では、日本海軍が米国海軍に大敗し、３千人以上の犠牲者を出しました。しかし、**大本営は虚構の戦果を発表し、京都新聞など全国の新聞は追従して「大戦果」と報道しました**。」
> —— [S29]

**事实对照**：美方实际损失 = 约克城号 1 艘（+ 哈曼号驱逐舰），被击落飞机约 150 架（含报废）。
日方损失 = 4 艘航母 + 1 艘重巡 + 248 架舰载机。
**「击沉 2 艘航母、击落 120 机」这个战报，等于把美方损失夸大一倍、把自己的 4 艘航母全部抹掉。**

#### 第二层：分阶段释放（先认 2 艘，再含糊认 2 艘）

> "On **11 June**, the Japan Times and Advertiser lied to the Japanese public by publishing "**Navy Scores Another Epochal Victory**," claiming to have sunk two U.S. carriers. **In this initial article, the Japanese admitted to losing two carriers. Then, on 21 June, the state revealed that the other two carriers could no longer operate due to vaguely defined damage.**"
> —— [S30] https://www.usni.org/magazines/naval-history/2025/june/timeless-lessons-messaging-after-midway

**这一条的叙事价值**：日方不是一次性撒谎，是**分两次、隔 10 天、逐级加码**地把 4 艘航母的损失摊开。
写「宣传与事实」时这是最好的细节——它证明**高层知道真相，且有计划地控制披露节奏**。

#### 第三层：日方战斗详报**自己**的造假（最有力的一层）

南云机动部队战斗详报（即 [S4]）的「战果」栏：

> "Recapitulation of Results Obtained During Midway Operations
> Surface Vessels:
> **2 Carriers of the Enterprise class sunk.**
> **1 Cruiser of the San Francisco class seriously damaged.**"
> —— [S4] https://www.ibiblio.org/hyperwar/Japan/IJN/rep/Midway/Nagumo/

而同一份报告的「损失」栏只有一个词：

> "Damage Sustained:
> **Surface Vessels (Omitted).**
> Aircraft ("self-exploded"):
> Personnel (killed in action): …"
> —— [S4] 同上

> **「Surface Vessels (Omitted).」——己方四艘航母的损失，在自己的绝密战斗详报里被「省略」了。**
> 这是全案最有力的一句原话。它不是对外宣传，是**对内归档的战斗详报**。
> 主会话写「日方官方口径 vs 实际损失」时，这一句应当放在最前面。

同报告还有一句自我安慰式的战略判断：

> "The enemy, however, having lost two of their powerful carriers and many of his air personnel, would undoubtedly be unable to effect any large-scale operation in the near future. It is believed that the enemy will surely strike back at some time, and every precaution should be taken against this."
> —— [S4]

以及「有功者表彰」里对「战果」的重复（注意括号里的犹豫）：

> "The action of the men of CarDiv 2 (less the Soryu), in succeeding to **sink (or severely damage) two of the new and powerful enemy carriers** in spite of the fact that the enemy had gained control of the air, must be commended highly."
> —— [S4]

#### 第四层：对盟友也说谎，反噬自身战略

> "**To save face to their Axis allies, the Japanese fabricated their naval capabilities and lied about the outcome of Midway.** This lie only served to confuse their allies, as after the Axis defeat at El Alamein in the fall of 1942, **Italy explicitly blamed the IJN for the loss**, questioning why they had failed to halt the backdoor British supply route."
> —— [S30]

#### 第五层：对内的隔离措施（把生还者关起来）

> "In addition to the immediate battlefield losses, **the IJN's decision to conceal surviving crew members in remote outposts had far-reaching consequences. By isolating the wounded and forbidding them any outside contact for more than a year, the IJN inadvertently deprived itself of desperately needed experience.**"
> —— [S30]

#### 美方的对照（同一篇文章，可作对照句）

> "The first explosive Midway headline electrified the United States on **7 July 1942** … "The resounding victory scored by American warships, submarines, planes and guns in decisively repulsing a major enemy seaborne thrust at strategic Midway Island was **hailed as possibly an important turning point in the war of the Pacific**.""
> —— [S30]

> ⚠️ **[S30] 的日期与史实有内部矛盾**：文中说 US 头条「7 July 1942, hitting the stands **three days after the battle**」——
> 但中途岛是 6 月 4-7 日，7 月 7 日距战斗已一个月，不是三天。**这是该文自身的错误**。
> 主会话不要引「三天后」这个说法。同文的 [S29]（京都新闻）日期链条（6/10 大本营发表 → 6/11 见报）是自洽的，可以引。

### D.4 需要补一句的边界（诚实标注）

- **「中途岛后日美航母存量对比」未获取**：本次没有查双方航母在 1942-06 的存量表，
  所以 D.2 里「Restored parity of forces in Pacific」只能引 Parshall 的判断句，**不能自己算成 3:2**。
- **「日本飞行员训练时长的具体数字」未获取**：只查到「30% 阵亡 / 40% 负伤」「损耗率假设 20-30% → 50%」这类比例，
  没有「战前 XX 小时 / 战后 XX 小时」的绝对数。若武器页/战史页要写训练时长，需另找来源。
- **「日方四航母各舰飞行员编制数」未获取**（见 §0 纠错⑥）。

---

## 来源编号对照表（S 号 → 实际来源）

> 正文用 `[S#]` 简写，此处给全表，方便主会话并回 `data/sources.yaml`。
> 「已登记」= 已在 `data/sources.yaml` 里，**本组不重复登记**，直接复用其 id。
> 「新登记」= 见本组 `sources-fragment.yaml`。

| 号 | 来源 | 对应 id | 状态 |
|---|---|---|---|
| S1 | ONI 战斗叙述《The Battle of Midway》(1943) | `oni-midway-combat-narrative` | 已登记（本轮补抓 ch4–13 全文） |
| S2 | NHHC H-gram 006-1《The Battle of Midway》 | `nhhc-h006-1-battle-of-midway` | **新登记** |
| S3 | NavWeaps 中途岛双方战斗序列 | `navweaps-midway-oob` | **新登记** |
| S4 | 南云机动部队战斗详报（含 7 张附表） | `hw-japanese-story-midway-nagumo` | **新登记** |
| S5 | 企业号行动报告（Zone +10） | `nhhc-enterprise-midway-report` | 已登记 |
| S6 | 大黄蜂号行动报告（Zone +10） | `nhhc-hornet-midway-report` | 已登记 |
| S7 | 约克城号行动报告（未声明基准） | `nhhc-yorktown-midway-report` | 已登记 |
| S8 | combinedfleet 赤城 TROM | `combinedfleet-akagi` | 已登记 |
| S9 | combinedfleet 加贺 TROM | `combinedfleet-kaga` | 已登记 |
| S10 | combinedfleet 苍龙 TROM | `combinedfleet-soryu` | 已登记 |
| S11 | ETHW《Midway — Radar and the Fighter Directors》ch.7 | `ethw-radar-fighter-directors-midway` | **新登记** |
| S12 | combinedfleet 飞龙 TROM | `combinedfleet-hiryu` | 已登记 |
| S13 | USSBS IJO-31 胜又（飞行员损耗率） | `ussbs-ijo-31-katsumata-attrition` | **新登记** |
| S14 | USSBS IJO-1 天城（加贺飞行长） | `ussbs-ijo-1-amagi-kaga` | **新登记** |
| S15 | USSBS IJO-64 高田（中途岛后重建） | `ussbs-ijo-64-takata-planning` | **新登记** |
| S16 | USSBS IJO-4 青木（赤城舰长） | `ussbs-aoki-akagi` | 已登记 |
| S17 | USSBS IJO-39 小原（苍龙副长） | `ussbs-ijo-39-ohara-soryu` | **新登记** |
| S18 | USSBS IJO-2 川口（飞龙航空参谋） | `ussbs-ijo-2-kawaguchi-hiryu` | **新登记** |
| S19 | NHHC 中途岛专题总览 | `nhhc-midway-overview` | 已登记 |
| S20 | NHHC H-gram 006-3《The Victory — Barely》 | `nhhc-h006-3-victory-barely` | 已登记 |
| S21 | combinedfleet Aichi D3A | `combinedfleet-d3a` | 已登记 |
| S22 | The Aviation History On-Line Museum — Aichi D3A | `avh-d3a` | 已登记 |
| S23 | combinedfleet Nakajima B5N | `combinedfleet-b5n` | 已登记 |
| S24 | NavWeaps 日本二战鱼雷 | `nw-japanese-torpedoes-wwii` | **新登记** |
| S25 | NavWeaps 美国二战雷达 | `nw-us-radar-wwii` | **新登记** |
| S26 | JM-93《Midway Operations, May–June 1942》 | `jm93-midway-operations` | 已登记 |
| S27 | USSBS IJO-50 深水（飞机生产/损耗表） | `ussbs-ijo-50-aircraft-wastage` | **新登记** |
| S28 | Parshall 2006 Historicon 讲义 | `parshall-midway-brief` | 已登记 |
| S29 | 京都新聞《京都戦時新聞》第 4 号转引大本营发表 | `kyoto-shimbun-midway-daiseika` | **新登记** |
| S30 | USNI《Timeless Lessons From the Messaging After Midway》(2025) | `usni-messaging-after-midway` | **新登记** |
| S31 | 《Shattered Sword》导言（免费样本 PDF） | `ss-introduction-shattered-sword` | **新登记** |
| S32 | USSBS IJO-13 渡边（山本幕僚） | `ussbs-ijo-13-watanabe` | **新登记** |
| S33 | NHHC H-gram 006-2《ISR at Midway》 | `nhhc-h006-2-isr-midway` | 已登记 |

> S15 在正文中曾与 S32 混用（同一批 IJO-13 引文），已统一为 **S32 = IJO-13**、**S15 = IJO-64**。
> 另有 `ussbs-ijo-66-midway-solomons`（IJO-66）与 `nhhc-h006-4-flight-to-nowhere`（H-006-4）
> 已登记于 sources-fragment.yaml 但正文未逐句引用，登记备用。

---

## 交付摘要

| 项 | 数量 |
|---|---|
| 交付文件 | 3（`RESEARCH-NOTES.md` / `sources-fragment.yaml` / `timeline-candidates.yaml`） |
| 新登记来源 | 17 |
| 复用已登记来源 | 14 |
| 缺口 A 覆盖 | 编制 100%（四舰逐分队 + 美方三舰 operational 数）；损失 90%（日方 44 架空中损失 + 逐舰阵亡 4 口径 + 飞行员 7 说；美方逐中队逐机号）；**飞行员编制数未获取** |
| 缺口 B 覆盖 | 85%（三型日机挂弹 + 三型美机挂弹 + 弹药消耗 + TBD 三队结局原句齐）；**零战当日挂弹「无记载」需按无挂弹写** |
| 缺口 C 覆盖 | 95%（CXAM 四次接触 + 岸基雷达 + 日方 6 份证言 + PBY 6-03/6-04 全链） |
| 缺口 D 覆盖 | 90%（技术/机务损失 + 飞行员路径 + 战略转折 + 五层宣传造假原句）；**航母存量对比未获取** |
| 时间线候选 | 21 条 |
| 抓取原始页 | 30 份，存 `_raw/` |

### 卡住的地方

- **日方四航母各舰飞行员编制数**：查了南云详报 Table 1（只有飞机数）、USSBS 四份访谈（只有损失数）、
  NHHC 战斗序列（只有姓名）、combinedfleet 四份 TROM（只有飞机数），**四处都没有**。不推算。
- **中途岛后日美航母存量对比**：本次未查，不写。
- **「换弹作业为什么不能在陆用弹/通常弹之间凑合」**：No.25 陆用 242 kg 与通常 250 kg 几乎同重，
  但没有任何来源解释引信/弹体差异，**我推的机制不作为结论**。
- **IJO-50 Annex B 的 `a/b` 列含义**：该页未给图例，我按表头推断为「生产/损耗」，**标注为推断**，建议主会话只引「6 月标注 Midway/Aleutians」这一事实。

### 有争议的记载（均并列，未裁决）

| # | 争点 | 各方说法 |
|---|---|---|
| 1 | 日方飞行员阵亡总数 | 110（NHHC 36+74）/ over 100（NHHC 综述）/ 30% 阵亡（IJO-64）/ 逐舰相加 136（本文件算术） |
| 2 | 四舰逐舰阵亡 | 详报 221/800/416/718 vs Tully 263/814/713/418(383)；USSBS 访谈另给 200/800/700/500 |
| 3 | 日方总阵亡 | 2,208（Tully 相加）/ 3,000+（NHHC）/ 4,500（IJO-13）/ 4,800（ONI） |
| 4 | 日方飞机损失 | 44 架（南云详报，仅空中战损）/ 248 架（NHHC，含随舰沉没）/ 约 250（IJO-39）/ 275（ONI 尼米兹） |
| 5 | 赤城舰载机数 | NavWeaps 17+1 vs TROM 18（结构解读后一致，但来源未明说） |
| 6 | 苍龙舰爆数 | NavWeaps 15+1 vs TROM 16 |
| 7 | 约克城 SBD 数 | 编制 19+18（NavWeaps/NHHC）/ 报告编成 18+18（CV-5 AR）/ 出击 17+12（CV-5 AR） |
| 8 | VMSB-241 SB2U 数 | 21 架编制 / 14 可用（NavWeaps）/ 12 架出击（ONI） |
| 9 | 中途岛雷达首发时刻 | ONI「0545 后五分钟」≈0550 vs NHHC 0553；且 NHHC 说雷达比 PBY 目视晚 8 分钟 |
| 10 | 加贺有无雷达 | 天城先说「用雷达指挥」→ 又说「加贺没有」「中途岛是实验、不太好」，本人自相矛盾 |
| 11 | VT-6 损失 | 10 架未返（CV-6 AR）vs 9 架被击落（NHHC） |
| 12 | 飞龙被弹数与 1020 时刻 | 南云详报 1403(JST) / 4 弹（Table 3）vs TROM 1703 当地 / 4 弹；IJO-2 川口说「hit six times」 |
| 13 | 美方鱼雷机总数 | 41 TBD + 6 TBF + 4 B-26 =「42 torpedo planes」（NHHC）vs 41 架 TBD（三舰合计） |
| 14 | 约克城鱼雷命中时刻 | ONI 1445（+12）vs 约克城 AR「about 1620」（+10）→ 换算后差 25 分钟 |
