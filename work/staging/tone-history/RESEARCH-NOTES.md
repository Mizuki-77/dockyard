# 利根型重巡洋舰（利根 / 筑摩）战历与航空运用史 — 调研底稿

> 调研员：`tone-history`（subagent）· 2026-11-23
> 工作目录：`work/staging/tone-history/`　原始页面：`work/staging/tone-history/_raw/`
> 用途：供主会话撰写 `data/articles/tone.yaml`、`data/articles/chikuma.yaml` 正文。
> **本轮不写正文、不写 fact 文件**，只交付调研笔记 + 来源分片。

---

## 0. 采集方式与时间基准（写正文前必读）

### 0.1 抓取方式

`web_fetch` / `research` 在本机对几乎所有域名返回 SSRF 拦截（见 SCHEMA §9.1），本轮全程用
Python `urllib.request` + Chrome UA 直连，原始 HTML/PDF 存 `_raw/`，再用自写 `html2txt.py`
转纯文本后核读。

**能直连的**：`combinedfleet.com`、`navypedia.org`、`ibiblio.org`（HyperWar）、
`en.wikipedia.org`、`ja.wikipedia.org`、`archive.org`（Wayback）。

**不能直连的**：

| 域名 | 症状 | 处置 |
|---|---|---|
| `history.navy.mil`（NHHC） | TLS 握手失败 `UNEXPECTED_EOF_WHILE_READING`，curl/schannel 亦失败 | 走 Wayback 存档，取到全文。引用时给 NHHC 原始 URL + 存档 URL 两条 |
| `usni.org` / `ww2db.com` / `wikiwand.com` / `imodeler.com` 直连 | 403 | imodeler 走 Wayback 取到；USNI 的 Tully《Solving some Mysteries of Leyte Gulf》**未获取** |

### 0.2 时间基准（关键，写错就全错）

三个来源用两套时间，**必须换算**：

- **ONI《The Japanese Story of the Battle of Midway》** 明确声明用东京时间（+9）：
  > "It should be noted that all dates in this report and all times are in Tokyo time, Plus 9."
  > —— <https://www.history.navy.mil/research/library/online-reading-room/title-list-alphabetically/j/japanese-story-of-the-battle-of-midway.html>（存档 <http://web.archive.org/web/20251208125755/https://www.history.navy.mil/research/library/online-reading-room/title-list-alphabetically/j/japanese-story-of-the-battle-of-midway.html>）

- **combinedfleet 的 Tone / Chikuma TROM** 中途岛段用**中途岛当地时**（个别条目标了 `(local)`，
  如达尔文空袭条 "At 0530 (local)…"）。

- **两者相差 21 小时**（即 1942-06 中途岛当地为 UTC−12）。这个换算是我的推断，但有两组
  互不相关的锚点同时对上，可信：

  | 事件 | ONI（东京时） | TROM（当地时间） | 差值 |
  |---|---|---|---|
  | 利根 4 号机发现敌舰 | 0428（5 日） | 0728（4 日） | 21 h |
  | 利根 3 号机起飞 | 0142（5 日） | 0435–0500 区间内 | 21 h |
  | 利根 4 号机起飞 | 0200（5 日） | 0500（区间末） | 21 h |

  → **换算规则：东京时 − 21 h = 中途岛当地时。**

- **JM-93《Midway Operations》** 用东京时（"Between 0130 and 0200 hours … were dispatched"）。

- **莱特湾**：TROM 的 1944-10 各条时间未标基准，与日方战报口径一致，**按日方时间处理**，
  正文凡引用时刻都写「日方记载」而不换算。

---

## 1. 建造与服役

| 项 | 利根 | 筑摩 |
|---|---|---|
| 起工 | 1934-12-01 三菱长崎 | 1935-10-01 三菱长崎 |
| 进水 | 1937-11-21 | 1938-03-19 |
| 竣工 | 1938-11-20 | 1939-05-20 |

**利根**
> "1 December 1934: Nagasaki. Laid down at Mitsubishi's Shipyard."
> "21 November 1937: Launched and named TONE. Captain Ryuzaki Tomekichi (40)(former CO of CHOGEI) is appointed the Chief Equipping Officer (CEO)."
> "20 November 1938: Completed and registered in the IJN. Attached to Yokosuka Naval District. Captain Hara Teizo is the Commanding Officer."
> —— <https://www.combinedfleet.com/tone_t.htm>

**筑摩**
> "1 October 1935: Nagasaki. Laid down at Mitsubishi's shipyard."
> "19 March 1938: Launched and named CHIKUMA."
> "20 May 1939: Completed and registered in the IJN. Attached to Yokosuka Naval District. Captain Nishio Hidehiko is the Commanding Officer."
> —— <https://www.combinedfleet.com/chikuma_t.htm>

navypedia 同口径（`1.12.1934 / 21.11.1937 / 20.11.1938`；`1.10.1935 / 19.3.1938 / 20.5.1939`），
并给两舰船厂序列号 600 / 670，均为三菱长崎：
<https://www.navypedia.org/ships/japan/jap_cr_tone.htm>

> **编成沿革**（两舰同）：1939-05-20 编成第六战队 → 1939-11-15 改称第八战队（CruDiv 8）→
> 1944-01-01 第八战队解队，两舰转入第七战队（CruDiv 7）。
> TROM：`"1 January 1944: CruDiv 8 is disbanded. TONE and CHIKUMA are assigned to Rear Admiral … Nishimura Shoji's … CruDiv 7 with KUMANO and SUZUYA."`（tone_t / chikuma_t 两页同文）

---

## 2. 逐日战历（TROM）

> 每条格式：**日期 ｜ 一句话 ｜ 英文原句 ｜ URL**。
> 全部原句照抄 combinedfleet TROM（Tone: `tone_t.htm`；Chikuma: `chikuma_t.htm`），仅按原文换行重排。
> 时刻一律为该 TROM 自述基准（见 §0.2）。

### 2.1 利根（IJN TONE）

| 日期 | 事件 | 英文原句 | 来源 |
|---|---|---|---|
| 1934-12-01 | 三菱长崎起工 | "1 December 1934: Nagasaki. Laid down at Mitsubishi's Shipyard." | tone_t |
| 1937-11-21 | 进水命名 | "21 November 1937: Launched and named TONE." | tone_t |
| 1938-11-20 | 竣工、入横须贺镇守府籍 | "20 November 1938: Completed and registered in the IJN. Attached to Yokosuka Naval District. Captain Hara Teizo is the Commanding Officer." | tone_t |
| 1941-11-26 | 作为第八战队随南云机动部队自单冠湾出击 | "26 November 1941: Operation "Z": CruDiv 8's TONE and CHIKUMA depart Hitokappu Bay, Etorofu Island, Kuriles with Vice Admiral Mikawa Gunichi's … Support Force's BatDiv 3/Section 1's HIEI and KIRISHIMA …" | tone_t |
| 1941-12-07 0500 | 弹射 1 架零式水侦（E13A1）侦察拉海纳锚地，未发现美舰 | "At 0500, TONE and CHIKUMA each launch one Aichi E13A1 Type 0 "Jake" floatplane for a pre-strike reconnaissance flight. TONE's "Jake" No. 1 (coded JI-1), piloted by WO Narukawa Ryozo, reconnoiters Lahaina Roads anchorage, but finds no American fleet units present there." | tone_t |
| 1941-12-07 0630 | 再弹射 1 架九五式水侦（E8N2）担任哨戒 | "At 0630, CHIKUMA and TONE each launch a short range Nakajima E8N2 "Dave" two-seat floatplane to act as pickets and patrol south of the Striking Force." | tone_t |
| 1941-12-07 约0730 | 该零式水侦返航着水时翻覆损失 | "About 0730, lookouts aboard … submarine I-1 observe TONE's "Jake" returning from the Lahaina area. During the landing attempt in heavy seas the E13A1 capsizes and is lost." | tone_t |
| 1941-12-16 | 第八战队等脱离机动部队参加威克岛第二次攻略 | "CruDiv 8, CarDiv 2 and destroyers URAKAZE and TANIKAZE are detached from the Striking Force to participate in the second invasion." | tone_t |
| 1941-12-23 | 利根水侦最先报告岛上战斗结束 | "TONE's floatplane is the first to report that fighting on the island has ceased." | tone_t |
| 1941-12-29 | 返吴入坞检修 | "Arrives at Kure and enters overhaul." | tone_t |
| 1942-01-14 | 抵特鲁克 | "Arrives at Truk." | tone_t |
| 1942-01-20 | 支援拉包尔空袭、莱城/萨拉马瓦空袭 | "Supports air attacks on Rabaul. Supported CarDiv 5 attacks on Lae and Salamaua, New Guinea." | tone_t |
| 1942-01-23 | 2 架零式水侦 + 1 架九五式水侦轰炸布卡岛 | "Two E13A1 floatplanes and one E8N2 from TONE attack and bomb Buka Island." | tone_t |
| 1942-01-25 | 水侦攻击阿德默勒尔蒂群岛 | "The TONE's floatplanes attack the Admiralties." | tone_t |
| 1942-02-19 0530(local) | 达尔文空袭前弹射水侦侦察克拉伦斯海峡天气，电台故障 | "At 0530 (local), TONE catapults an E13A1 "Jake" reconnaissance floatplane to report on the weather over the Clarence Strait 18 miles N of Darwin, but the plane's radio fails and it returns to TONE at 0955 (local)." | tone_t |
| 1942-03-01 0700 | 两舰各弹射 1 架零式水侦搜索圣诞岛以西 | "At 0700 TONE and CHIKUMA each launch one E13A1 "Jake" floatplane to search the waters around Christmas Island and to the west." | tone_t |
| 1942-03-01 1603–1731 | 追击并击沉美军驱逐舰 EDSALL；第八战队耗 844 发 8 英寸弹 | "At 1655, HIEI and the heavy cruisers check fire without having scored a single direct hit." / "At 1731, the battered old "four-piper" sinks by the stern at 13-45S, 106-47E. In all, CruDiv 8 expends 844 8-inch and 62 5-inch rounds." | tone_t |
| 1942-04-05 | 利根 1 架九四式水侦（E7K）发现英军 Cornwall / Dorsetshire | "A Kawanishi E7K "Alf" floatplane from TONE locates Vice Admiral (later Admiral of the Fleet Sir) James Somerville's British Eastern Fleet's cruisers HMS CORNWALL and HMS DORSETSHIRE at sea - without air cover." | tone_t |
| 1942-04-18 | 随机动部队出击追捕杜立特编队，未果 | "TONE and CHIKUMA depart Mako with the Striking Force in an unsuccessful pursuit of of Halsey's ships."（原文 "of of" 重复，照抄） | tone_t |
| 1942-04-25 | 入舞鹤检修入坞 | "Arrives at Maizuru. Refit and drydocked." | tone_t |
| 1942-05-27 | 自柱岛出击参加 MI 作战 | "27 May 1942: Operation "MI" - The Battle of Midway: Departs Hashirajima with Vice Admiral … Nagumo's Carrier Striking Force: CarDivs 1 and 2 …" | tone_t |
| 1942-06-04 0435–0500 | 两舰各弹射 2 架零式水侦做 300 海里远程搜索 | "Between 0435-0500, CruDiv 8's TONE and CHIKUMA each launch two E13A1 Jake long-range reconnaissance floatplanes to search out 300 miles for American carriers from NNE thru S." | tone_t |
| 1942-06-04 0728 | 利根 4 号机发现敌舰，未识别出航母 | "At 0728, TONE's E13A1 No. 4 discovers the enemy ships, which later materialize as a carrier group. The observer does not identify the carriers at the outset, which proves to be a crucial mistake." | tone_t |
| 1942-06-04 | 遭美军舰载机攻击无伤；损失 1 架九五式水侦及机组 | "TONE is attacked by enemy carrier aircraft but sustains no damage. During the battle, TONE's E8N2 No. 3 is lost with her crew." | tone_t |
| 1942-06-06 | 转隶北方部队支援阿留申攻略 | "TONE and CHIKUMA are ordered to support Vice Admiral Hosogawa Boshiro's … Fifth Fleet for the Aleutians invasion." | tone_t |
| 1942-06-24 | 返大凑 | "Arrives at Ominato." | tone_t |
| 1942-07-14 | 舰长更替（神戸祐治）；原忠一任第八战队司令 | "Captain (later Rear Admiral) Kobe Yuji (45)(former CO of YAKUMO) is appointed the CO. Captain Okada is reassigned as the CO of carrier JUNYO." | tone_t |
| 1942-08-16 1800 | 随第三舰队出击参加 KA 作战（瓜岛） | "At 1800 CruDiv 8's TONE and CHIKUMA depart Hashirajima with Nagumo's Third Fleet, Carrier Strike Force …" | tone_t |
| 1942-08-24 1100 | 第二次所罗门海战：两舰放出 7 架水侦；筑摩 2 号机 1400 发现美舰队但被击落 | "At 1100, TONE and CHIKUMA of the Vanguard Force launch seven floatplanes on a late morning search for American ships." / "At 1400, CHIKUMA's Aichi E13A1 No. 2 discovers the American task force, but is shot down by USN fighters." | tone_t |
| 1942-10-19 | 单独与照月号脱离本队搜敌 | "TONE in company with destroyer TERUZUKI is detached to scout for American ships." | tone_t |
| 1942-10-26 | 南太平洋海战：利根 4 架水侦担任美舰观测，损失 2 架 | "TONE's four floatplanes provide spotting duties over the American ships. Two are lost during the battle." | tone_t |
| 1942-11-13 | 第三次所罗门海战（瓜岛第一夜战）：利根水侦搜索无果 | "The Eastern Reconnaissance Unit's TONE, light cruiser SENDAI and destroyer AYANAMI's mission is to reach the waters E of Tanaka's convoy. TONE floatplanes search the area S of Guadalcanal but find nothing." | tone_t |
| 1942-11-18 | 返特鲁克，其后约两个月仅作例行巡逻 | "TONE arrives at Truk. Remains there for the next two months. Performs routine patrol duties." | tone_t |
| 1943-02-21 | 入舞鹤改装：加装 2 座双联 25mm、装 21 号电探 | "Arrives at Maizuru for a refit. Two additional 25-mm twin AA guns are installed and a Type 21 air-search radar is fitted." | tone_t |
| 1943-05-17 | 与筑摩护送武藏运山本五十六骨灰回东京 | "CruDiv 8's TONE and CHIKUMA depart Truk for Yokosuka in response to the invasion of Attu with BatDiv 1's MUSASHI … MUSASHI carries Admiral Yamamoto's ashes to Tokyo for a state funeral." | tone_t |
| 1943-07-19→21 | 往拉包尔运送陆军部队 | "Departs Truk on a troop transport run with the CHIKUMA, MOGAMI, seaplane tender NISSHIN, light cruisers OYODO and AGANO …" / "21 July 1943: Arrives at Rabaul. Disembarks troops." | tone_t |
| 1943-10-31 | 离特鲁克时把全部水侦留在特鲁克 | "Reportedly, TONE leaves all her floatplanes at Truk before departing."（**原文带 "Reportedly"，转写正文时不可去掉这个限定**） | tone_t |
| 1943-11-05 | 隼鹰在本土近海被美潜艇雷击受损、需拖回吴（**利根当时不在拉包尔**；TROM 此处未点名拖带者，拖带一说的出处见 §6） | "5 November 1943: The task group is attacked by USS HALIBUT (SS-232) near Bungo Suido. YAMASHIRO is hit by a dud torpedo, but JUNYO is damaged and has to be towed to Kure." | tone_t |
| 1943-11-06 | 入吴改装：前部 25mm 双联改四座三联，总数 20 门 | "Arrives at Kure Navy Yard. Begins a refit. The forward 25-mm twin AA mounts are replaced by four triple mounts, bringing the total number of 25-mm guns to 20 (4 x 3 and 4 x 2)." | tone_t |
| 1943-12-23 | BO-2-GO：载 525 名陆军与 175 吨物资急送卡维恩 | "TONE and CruDiv 5 (MYOKO and HAGURO) depart Kure for a fast supply run to Kavieng via Truk. TONE is carrying 525 IJA troops and 175 tons of cargo including ammunition, water purification plants and 555 bamboo poles." | tone_t |
| 1944-01-01 | 第八战队解队，转第七战队 | "CruDiv 8 is disbanded. TONE and CHIKUMA are assigned to Rear Admiral … Nishimura Shoji's … CruDiv 7 with KUMANO and SUZUYA." | tone_t |
| 1944-03-09 | 印度洋通商破坏：击沉英货船 BEHAR，收容 108 名俘虏 | "TONE sinks British freighter SS BEHAR. She takes aboard 108 captives, but four die." | tone_t |
| 1944-03-18 | 青叶号上第十六战队司令左近允下令斩首余下 72 名俘虏 | "Departs Batavia. Aboard AOBA en route to Singapore, ComCruDiv 16, Rear Admiral Sakonjo Naomasa … orders the remaining 72 captives beheaded." | tone_t |
| 1944-06-13→20 | 参加 A-GO（马里亚纳海战） | "The Mobile Fleet departs Tawi Tawi for Guimaras near Panay, Philippines …" / "At about 2030, carrier HIYO explodes and sinks …" | tone_t |
| 1944-06-26→07-08 | 吴入坞：25mm 增至 57 门（8×3、4×2、25×1），装 13 号电探 | "26 June-8 July 1944: In drydock at Kure. Four 25-mm triple mounts are added … bringing the TONE's total 25-mm AA suite to 57 barrels (8x3, 4x2, 25x1). New antennas are installed for the two Type 22 surface-search radars and a Type 13 air-search radar is fitted." | tone_t |
| 1944-10-22 | 参加 SHO-1-GO，随栗田第一游击部队自文莱出击 | "Vice Admiral Kurita Takao's … First Mobile Striking Force (Center Force) sorties from Brunei. Vice Admiral Shiraishi's CruDiv 7's TONE, CHIKUMA, KUMANO and SUZUYA are in Force "A"'s Second Section …" | tone_t |
| 1944-10-23 | 巴拉望水道：爱宕、摩耶被潜艇击沉，利根收容爱宕幸存者 | "At 0633, Force A is attacked by … USS DARTER (SS-227) and … USS DACE (SS-247). Vice Admiral Kurita's flagship ATAGO and MAYA are sunk and TAKAO damaged." / "TONE embarks some survivors from ATAGO." | tone_t |
| 1944-10-24 | 锡布延海：利根、筑摩各放出最后 2 架水侦飞往民都洛圣何塞 | "24 October 1944: The Battle of the Sibuyan Sea: Tablas Strait. After 1024, TONE and CHIKUMA both launch their two remaining floatplanes, heading for San Jose, Mindoro Island." | tone_t |
| 1944-10-24 1445–1530 | 利根主动建议集中防空护卫武藏，被派去掩护，遭近失弹与命中弹轻伤 | "At 1445, after the fourth attack, the CO of TONE contacts Vice Admiral Suzuki Yoshio … suggesting to concentrate the entire unit around the heavily damaged MUSASHI to provide additional AA support for her. At 1507 Admiral Suzuki detaches TONE to defend MUSASHI against torpedo bomber attacks." / "At 1517, TONE is attacked by dive-bombers and receives two near misses … At 1518 she receives a small caliber bomb hit, causing a minor fire …" | tone_t |
| 1944-10-25 | 萨马岛海战：对 JOHNSTON、GAMBIER BAY 等射击，全天耗主炮弹 408 发 | "After 0713 TONE fires 18 8-in rounds at the attacking JOHNSTON." / "Between 0818 and 0832 TONE targets a "RANGER class" carrier (USS GAMBIER BAY), firing 90 main caliber rounds; several hits are observed." / "Between 1030 and 1320, CHOKAI, CHIKUMA and SUZUYA are disabled by battle damage and subsequently lost. TONE fires a total of 408 main battery rounds during the battle." | tone_t |
| 1944-10-25 0853 | 利根舰桥目睹筑摩被雷击失速 | "At 0853, the lookouts on TONE witness the torpedo hit crippling CHIKUMA." | tone_t |
| 1944-10-25 1249 | 撤退途中被俯冲轰炸机命中右舷后部，舵机失灵，一度只能 15 节 | "At 1249 Kurita's retiring force is attacked by carrier aircraft. TONE is attacked by four dive-bombers and receives one hit to starboard aft, opening a large hole in the hull and disabling her steering. Her speed is temporarily limited to 15 kts." | tone_t |
| 1944-10-28 | 残部返文莱湾 | "The remnants of Force "A" arrive at Brunei Bay, Borneo and refuel." | tone_t |
| 1944-11-17 | 入舞鹤：加装 4 座三联 25mm，总数 62 门；21 号电探换 22 号 | "Arrives at Maizuru. Drydocked. Four 25-mm triple mounts are installed aft, removing seven single mounts and bringing TONE's total 25-mm AA suite to 62 barrels (12x3, 4x2, 18x1). Her Type 21 radar is replaced with a Type 22." | tone_t |
| 1945-01-01 | 改为练习舰，编入吴练习舰队 | "Redesignated as a training vessel. Reassigned to Kure Training Flotilla with IWATE, IZUMO and YAKUMO." | tone_t |
| 1945-03-19 | 吴军港空袭：被直击弹 1 发，3 号炮塔转向卡死 | "Vice Admiral … Marc A. Mitscher's … Task Force 58 raids Kure. TONE, caught in the middle of Kure Bay, receives one direct hit, jamming her No. 3 turret in train, and several near misses." | tone_t |
| 1945-07-24 | 被 TF38 舰载机命中 3 发 | "TONE is attacked by aircraft of Vice Admiral … John S. McCain's … TF 38 from USS SHANGRI-LA (CV-38), COWPENS (CVL-25) and MONTEREY (CVL-26). TONE receives three direct hits and several near misses." | tone_t |
| 1945-07-28 | 再次空袭：左舷 2 发直击（含 1 发 1000 磅）＋6 近失，左倾 21 度 | "TONE receives two direct hits to port side (one of them a 1,000-lb aft) and six near misses. Near misses cause serious flooding and TONE develops a 21-degree list to port." | tone_t |
| 1945-07-29 | 在浅水坐沉 | "Settles on the bottom in shallow water." | tone_t |
| 1945-11-20 | 除籍 | "Removed from the Navy List." | tone_t |
| 1947-04-07→1948-09-30 | 播磨造船拆解：1948-05-04 浮起，1948-09-30 拆完 | "7 April 1947: Harima Shipyard starts the removal of superstructure and turrets." / "4 May 1948: The hull is refloated." / "30 September 1948: The scrapping of the hull is completed." | tone_t |

### 2.2 筑摩（IJN CHIKUMA）

| 日期 | 事件 | 英文原句 | 来源 |
|---|---|---|---|
| 1935-10-01 | 三菱长崎起工 | "1 October 1935: Nagasaki. Laid down at Mitsubishi's shipyard." | chikuma_t |
| 1938-03-19 | 进水命名 | "19 March 1938: Launched and named CHIKUMA." | chikuma_t |
| 1939-05-20 | 竣工、入横须贺镇守府籍 | "20 May 1939: Completed and registered in the IJN. Attached to Yokosuka Naval District. Captain Nishio Hidehiko is the Commanding Officer." | chikuma_t |
| 1941-11-26 | 随第八战队自单冠湾出击 | "26 November 1941: CruDiv 8's CHIKUMA and TONE depart Hitokappu Bay, Etorofu Island, Kuriles with Vice Admiral Mikawa Gunichi's Support Force …" | chikuma_t |
| 1941-12-07 0500 | 弹射零式水侦侦察珍珠港本港（利根机去拉海纳） | "At 0500, CHIKUMA and TONE each launch one Aichi E13A1 "Jake" Type 0 floatplanes for a pre-strike reconnaissance flight. The E13A1 from CHIKUMA reconnoiters Pearl Harbor." | chikuma_t |
| 1941-12-23 | 筑摩水侦被高炮击伤迫降，机组获救 | "TONE's floatplane reports that fighting on Wake Island has ceased. CHIKUMA's plane, damaged by AA fire, ditches, but the crew is rescued." | chikuma_t |
| 1942-01-24 | 筑摩水侦攻击阿德默勒尔蒂群岛 | "CHIKUMA's floatplanes attack the Admiralties." | chikuma_t |
| 1942-03-01 0700 | 与利根各弹射 1 架零式水侦搜索 | "At 0700 TONE and CHIKUMA each launch one E13A1 "Jake" floatplane to search the waters around Christmas Island and to the west." | chikuma_t |
| 1942-03-01 | 筑摩水侦发现荷兰商船 MODJOKERTO 并报位 | "CHIKUMA's "Jake" locates the Dutch armed motor vessel MODJOKERTO, attempting to escape from Tjilatjap to Australia and reports its location." | chikuma_t |
| —— | 尾注 [1] 更正「筑摩击沉 MODJOKERTO」的流传说法：战果其实是驱逐舰的 | "[1] Although several Western sources credit CHIKUMA with the sinking of MODJOKERTO, DesRon 1's War Diary (1-31 March 1942 including DesRon 1 Secret Messages Nos. 14-2-6), filed on 27 April 1942, confirms that MODJOKERTO, identified by her name, was indeed intercepted and sunk by ISOKAZE and other destroyers." | chikuma_t |
| 1942-03-01 1603 | 筑摩以 8 英寸炮超远距离开火射击 EDSALL | "At 1603, CHIKUMA opens fire with her 8-inch guns at extremely long range. EDSALL lays down a smokescreen and begins evasive maneuvers." | chikuma_t |
| 1942-03-01 1731 | EDSALL 沉没；筑摩救起 7–8 名幸存者 | "At 1731, the battered old "four-piper" sinks by the stern at 13-45S, 106-47E. In all, CruDiv 8 expends 844 8-inch and 62 5-inch rounds. CHIKUMA picks up seven or eight survivors." | chikuma_t |
| 1942-03-04 | 与浦风共同击沉荷兰商船 ENGGANO | "CHIKUMA and destroyer URAKAZE sink Dutch merchant ENGGANO, bombed and set afire by a floatplane from CruDiv 4's TAKAO on 1 March." | chikuma_t |
| 1942-05-18 | 入柱岛后转吴海军工厂修理 | "18 May 1942: Arrives at Hashirajima, then transfers to Kure Naval Yard for repairs." | chikuma_t |
| 1942-05-27 | 自柱岛出击参加中途岛 | "27 May 1942: Operation "MI" - The Battle of Midway: Abe's CruDiv 8 departs Hashirajima with Vice Admiral (later Admiral, posthumously) Nagumo's Carrier Striking Force: CarDivs 1 and 2 …" | chikuma_t |
| 1942-06-04 0435–0500 | 与利根各弹射 2 架零式水侦 | "Between 0435-0500, CruDiv 8's CHIKUMA and TONE each launch two E13A1 "Jake" long-range reconnaissance floatplanes to search out 300 miles for American carriers from NNE thru S." | chikuma_t |
| 1942-06-04 1045 | 筑摩 5 号机（原久志三等兵曹）发现约克城，跟踪 3 小时并引导攻击 | "At 1045, CHIKUMA's No. 5 floatplane, an E13A1 piloted by PO3c Hara Hisashi, finds USS YORKTOWN, discovered earlier by TONE's floatplane. Hara shadows the carrier for the next three hours and guides the carrier bombers that attacking YORKTOWN."（原文 "that attacking" 语法错误，照抄） | chikuma_t |
| 1942-06-04 1409 | 该 5 号机被 VF-6 击落 | "During the battle, CHIKUMA loses her E13A1 No. 5, piloted by PO Hara, evidently downed by VF-6's MM William H. Warden and Lt(jg) Ronald J. Hoyle at 1409." | chikuma_t |
| 1942-06-06 0652 | 筑摩 2 号机发现重创的约克城并报位，使 I-168 得以找到目标 | "At 0652, CHIKUMA's floatplane No. 2 discovers damaged YORKTOWN and signals its position. With this information submarine I-168 is able to find and sink the carrier." | chikuma_t |
| 1942-08-24 1400 | 第二次所罗门海战：筑摩 2 号机（福山特務少尉）发现美舰队，被击落，报未送达 | "At 1400, CHIKUMA's No. 2 Jake, piloted by Special Duty Ensign Fukuyama … Its report and subsequent messages sent by HIEI's F1M2 Pete as well as CHIKUMA's No. 5 floatplane are not picked up by the leader of carrier bomber group." | chikuma_t |
| 1942-10-23 | 与照月号向东方突出侦察 | "CHIKUMA and destroyer TERUZUKI thrust eastward of the Vanguard Force and the cruiser's planes canvass the ocean." | chikuma_t |
| 1942-10-26 | 南太平洋海战：投弃鱼雷后被 500 磅弹命中右舷前部鱼雷室，另中 2 弹， catapult 上 1 架零式水侦损毁，死 190 伤 154（含舰长古村） | "CHIKUMA jettisons her torpedoes before a 500-lb bomb dropped by a Douglas SBD-3 "Dauntless" dive-bomber from HORNET hits her starboard forward torpedo room. She is also hit by two other bombs. She loses one E13A1 "Jake" on the catapult. Her crew suffers 190 killed and 154 wounded including Captain Komura." | chikuma_t |
| 1942-10-26 | 以 23 节撤离 | "CHIKUMA proceeds to Truk with the maximum available speed of 23 knots escorted by URAKAZE and TANIKAZE." | chikuma_t |
| 1942-11-10 | 在吴修理并改装：加 2 座双联 25mm、装 21 号电探 | "CHIKUMA is repaired and undergoes a refit. Two additional 25-mm twin mounts are installed and a Type 21 air-search radar is fitted." | chikuma_t |
| 1943-02-27 | 改装完了，内海训练 | "The refit is completed. Training in Inland Sea." | chikuma_t |
| 1943-05-17 | 与利根护送武藏运骨灰 | "CruDiv 8's CHIKUMA and TONE depart Truk for Yokosuka with Admiral Koga embarked on MUSASHI … MUSASHI carries Admiral Yamamoto's ashes to Tokyo for a state funeral." | chikuma_t |
| 1943-07-19→21 | 陆军运输任务至拉包尔 | "CHIKUMA, TONE and MOGAMI depart Truk on a troop transport run …" / "21 July 1943: Arrives at Rabaul. Disembarks troops." | chikuma_t |
| 1943-11-05 0931 | 拉包尔空袭：右舷弹射器附近近失弹，3 号鱼雷发射管失灵，伤 3 人 | "Around 0931 CHIKUMA is attacked by an SDB dive-bomber from SARATOGA. She receives a near miss off the starboard catapult, which disables No. 3 torpedo mount and causes slight flooding; 3 crewmen are wounded." | chikuma_t |
| 1943-12-12 | 入吴改装：前部 25mm 双联改四座三联，总数 20 门 | "Arrives at Kure. Begins refit. The forward 25-mm twin AA mounts are replaced by four triple mounts, bringing the total number of 25-mm AA guns to 20 (4 x 3 and 4 x 2)." | chikuma_t |
| 1944-01-01 | 第八战队解队，转第七战队 | "CruDiv 8 is disbanded. CHIKUMA and TONE are assigned to Rear Admiral … Nishimura Shoji's … CruDiv 7 with KUMANO and SUZUYA." | chikuma_t |
| 1944-03-01→20 | 印度洋通商破坏；3-20 起任第七战队旗舰 | "1 March 1944: Operation "SA No. 1" Arrives at Bangka then departs for commerce raiding in the Indian Ocean." / "24 March-7 April 1944: Flagship of CruDiv 7." | chikuma_t |
| 1944-06-18/19 | 马里亚纳海战：除 13 架 B5N2 外，另放 1 架零式水侦参与搜索 | "CHIKUMA launches one E13A1 floatplane in addition to 13 B5N2 that are in CarDiv 3's second wave of morning searches." | chikuma_t |
| 1944-06-26 | 入吴入坞 | "Arrives at Kure. Drydocked." | chikuma_t |
| 1944-10-22 0820 | 随栗田部队自文莱出击 | "At 0820, CruDiv 7's KUMANO, SUZUYA, TONE and CHIKUMA sortie from Brunei towards Philippines with Vice Admiral Kurita's First Mobile Striking Force …" | chikuma_t |
| 1944-10-24 | 锡布延海：与利根各放出最后 2 架水侦 | "Tablas Strait. After 1024, CHIKUMA and TONE both launch their two remaining floatplanes, heading for San Jose, Mindoro Island." | chikuma_t |
| 1944-10-25 0724 | 熊野被雷击后，筑摩临时代理第七战队旗舰 | "After 0724, when KUMANO is damaged by a torpedo, CHIKUMA is designated the ad hoc flagship of CruDiv 7." | chikuma_t |
| 1944-10-25 0853 | 被 Taffy 2 的 4 架 TBM 雷击，Mk.13 命中，左螺旋桨与舵失效 | "At 0853, CHIKUMA is attacked by four TBM "Avenger" torpedo-bombers from "Taffy Two". She is hit by a Mk.13 torpedo that disables her port screw and rudder; two minutes later she goes dead in the water." | chikuma_t |
| 1944-10-25 0907→0930 | 连续向大和报告失去航行能力；最后报位 11-25N, 126-48E，9 节 | "At 0907, CHIKUMA reports to YAMATO that she has been torpedoed and is unnnavigable. Then at 0920, CHIKUMA reports that she has lost a shaft, is making 18 knots, but is unsteerable. At 0930, CHIKUMA reports she is at 11-25N, 126-48E and making nine knots."（原文 "unnnavigable" 三 n，照抄） | chikuma_t |
| 1944-10-25 1105 | 被 KITKUN BAY 的 VC-5 5 架 TBM 命中左舷中部 2 雷，机舱进水、失电、停船、左倾 | "At 1105, CHIKUMA is attacked by five VC-5 TBM-1Cs from KITKUN BAY. By that time her AA ammunition is mostly exhausted; in fact, during the previous attack some gunners had resorted to using exercise rounds. CHIKUMA is hit port side amidships by two torpedoes and her engine rooms flood. Power is lost." | chikuma_t |
| 1944-10-25 1110 | 派野分号前往救助 | "At 1110, destroyer NOWAKI is dispatched to assist her." | chikuma_t |
| 1944-10-25 1415→1430 | 再被 OMMANEY BAY 的 3 架 TBM 命中左舷中部 3 雷，约 1430 向左翻覆、尾部下沉于 11-52N 126-36E；野分救起约 120 人 | "After 1415, CHIKUMA is attacked by three TBM-1Cs from OMANNEY BAY (CVE-79), led by VC-75's CO, Lt Allen W. Smith, Jr. Three torpedoes hit her port side amidships. Around 1430, CHIKUMA capsizes and sinks by the stern at 11-52N, 126-36E. NOWAKI rescues some 120 survivors." | chikuma_t |
| 1944-10-26 0054→0149 | 野分号被美军水面舰艇击沉，筑摩幸存者随之全灭 | "At 0054, NOWAKI is crippled and set afire by gunfire from TG 34.5's VINCENNES (CL-64), BILOXI (CL-80) and MIAMI (CL-89) …" / "At 0149, NOWAKI, dead in the water, is sunk by gunfire and torpedoes from the destroyers at 13N, 124-54E. NOWAKI goes down with all hands, including CHIKUMA's survivors." | chikuma_t |
| 1945-04-20 | 除籍 | "Removed from the Navy List." | chikuma_t |

**筑摩唯一的例外幸存者**（TROM 尾注 [3]）：
> "[3] A single survivor from CHIKUMA was picked up by an American warship three days later."
> —— <https://www.combinedfleet.com/chikuma_t.htm>

---

## 3. 航空运用史（利根级的核心设计特色）

### 3.1 为什么后甲板这么设计

**设计动因（日方视角）**：日本海军没有「攻击/侦察兼用」舰载机，也不给航母配侦察队，
侦察全部推给巡洋舰的水侦。利根级的任务就是补上这个缺口。

> "Unlike the U.S. Navy, the Japanese did not have a dual role attack/scout aircraft, nor did they assign any of their carrier aircraft to a reconnaissance role. Little emphasis was placed on this aspect of carrier warfare. Instead the Japanese reserved all of their carrier aircraft for attack roles. Reconnaissance then was relegated to the float planes carried by cruisers. The Tone and the Chikuma were intended to provide the long range reconnaissance needed for Japan's carrier Air Fleets."
> —— <https://en.wikipedia.org/wiki/Tone-class_cruiser>（**tier E，只能当线索**）

同类表述见 combinedfleet 的舰级页（tier D，可作来源）：
> "Their main gun layout was sort of bizarre, with four dual turrets forward (some of which suffered from very poor firing arcs), and none aft. Their aft decks were totally devoted to AAA and float plane operations (they carried 5, as compared to the 3 carried by most other Japanese CAs), which made them very useful as scouting ships for carrier battlegroups, and consequently they spent much of the war hanging out with the carriers of Combined Fleet, rather than fighting in rat-holes like the Solomons."
> —— <https://www.combinedfleet.com/tone_c.htm>

**「为什么主炮全前置 → 后部全给航空」的因果链**（navypedia 讲得最清楚，一段话把稳性、
装甲带长度、干舷、航空甲板四件事串起来）：

> "However experience of designing of first 155mm cruisers, and also tragedy of overturned torpedo boat Tomozuru and mass newest ships damages during a typhoon have compelled to redesign cruisers. Number of main turrets had shrunk to four, having grouped them in a fore end. Machinery, in comparison with prototype, was displaced in a stern. As result it was possible to shrink a length of an armored belt, to moderate upper weight, to make ship ends lighter, that, in turn, has improved seaworthiness. Exempted aft end allowed to place large air group of six seaplanes."
> —— <https://www.navypedia.org/ships/japan/jap_cr_tone.htm>

**日文一侧的补充**（tier E，仅作线索）：主炮全前置使舰载机不受主炮爆风破坏，从而「随时可
全主炮齐射」；并举例说妙高、高雄都曾在射击时用爆风毁掉正在等待弹射的舰载机。

> 「利根型の特徴は、前部に20.3 cm連装砲塔4基を集中配置し、後部（後檣より後ろすべて）が航空兵装となっていることにある。この配置によって、艦載機が主砲の爆風で破損する危険性がなくなり、常時全主砲を発射できるようにもなった。（妙高型重巡洋艦、妙高はスラバヤ沖海戦で、高雄型重巡洋艦、高雄は敵駆逐艦を撃沈した際にそれぞれ射出を待っていた艦載機を4番主砲の爆風で破壊している）」
> —— <https://ja.wikipedia.org/wiki/利根型重巡洋艦>

### 3.2 弹射器与水侦布置

- **弹射器 2 基，位于后桅之后的两舷**：
  > "The Tone class had no aircraft hangar, but there was a comprehensive arrangement of transport rails and turntables on the aircraft catapult and quarterdecks. Two gunpowder-propelled catapults were located on the beam abaft the mainmast."
  > —— <https://en.wikipedia.org/wiki/Tone-class_cruiser>（tier E）

- **弹射器型号：吴式 2 号射出机 2 基**（日文维基，tier E，待主会话另找 C/D 级来源复核）：
  > 「呉式2号射出機2基」 —— <https://ja.wikipedia.org/wiki/利根型重巡洋艦>

- **无机库，露天系止；弹射甲板比系止甲板高一级，靠斜坡推上去；低处系止甲板易上浪，
  维护性差 —— 这也是后来大淀改设机库的原因**（日文维基，tier E）：
  > 「艦載機は露天繋止で格納庫はない。カタパルトの設けられた甲板は艦載機繋止甲板より一段高くなっており、艦載機はスロープであがる。この低い繋止甲板は波浪に洗われやすく搭載機のメンテナンス性に問題があった。そのため、後の軽巡洋艦大淀は格納庫を持つに至っている。」
  > —— <https://ja.wikipedia.org/wiki/利根型重巡洋艦>

> **注意**：combinedfleet 舰级页写 "they carried 5"；navypedia 写 "6 seaplanes (3 E7K1, 3 E8N1)… 2 catapults"；
> NHHC 写 "had been built to carry five longer-range floatplanes"。三处数字不一致，见 §7「有争议」。

### 3.3 各时期搭载机型与数量

**能拿到的最硬的一段（日文维基信息框，逐期给数列，标注来源为「#5」）**：

> 「搭載機
> 　計画:水上機6機
> 　定数(-1942年6月25日):零式水偵3機、九五式水偵2機
> 　定数(1942年6月25日-):零式水偵5機
> 　（カタパルト2基）」
> —— <https://ja.wikipedia.org/wiki/利根_(重巡洋艦)>

即：**计划 6 机 → 1942-06-25 前 = 零式水侦 3 + 九五式水侦 2 → 1942-06-25 起 = 零式水侦 5**。
日文维基正文另给了战前与莱特湾两个时点：

> 「計画では6機の航空機を搭載可能だったが、通常5機ないし4機で運用されていた。戦前は三座水偵2機、二座水偵4機、1940年（昭和15年）に三座水偵1機、二座水偵3機、レイテ沖海戦時には零式水上偵察機5機だった」
> —— <https://ja.wikipedia.org/wiki/利根型重巡洋艦>

**TROM 里可以逐条核到的实际出动记录（这些是可引的 D 级一手转述）**：

| 时间 | 机型与架数 | 原句 | 来源 |
|---|---|---|---|
| 1941-12-07 0500 | 利根：E13A1（零式水侦）1 架 | "TONE's "Jake" No. 1 (coded JI-1), piloted by WO Narukawa Ryozo, reconnoiters Lahaina Roads anchorage" | tone_t |
| 1941-12-07 0630 | 两舰各：E8N2（九五式水侦）1 架 | "At 0630, CHIKUMA and TONE each launch a short range Nakajima E8N2 "Dave" two-seat floatplane to act as pickets" | tone_t |
| 1942-01-23 | 利根：E13A1 ×2 + E8N2 ×1 | "Two E13A1 floatplanes and one E8N2 from TONE attack and bomb Buka Island." | tone_t |
| 1942-04-05 | 利根：E7K（九四式水侦）1 架 | "A Kawanishi E7K "Alf" floatplane from TONE locates … HMS CORNWALL and HMS DORSETSHIRE" | tone_t |
| 1942-06-04 | 两舰各：E13A1 ×2 远程搜索 + E8N2 ×1 反潜；另各留 1 架 E8N2 备用 | "TONE and CHIKUMA also each launch one E8N2 floatplane on ASW patrol. Each cruiser holds another "Dave" for later use on another ASW mission." | tone_t |
| 1942-08-24 1100 | 两舰合计：7 架水侦 | "At 1100, TONE and CHIKUMA of the Vanguard Force launch seven floatplanes on a late morning search" | tone_t |
| 1942-10-26 | 利根：4 架水侦担任观测，损失 2 架 | "TONE's four floatplanes provide spotting duties over the American ships. Two are lost during the battle." | tone_t |
| 1943-10-31 | 利根：离特鲁克时把全部水侦留下 | "Reportedly, TONE leaves all her floatplanes at Truk before departing." | tone_t |
| 1944-01-02 | 利根：载 2 架水侦 | "TONE is carrying two floatplanes." | tone_t |
| 1944-06-18/19 | 筑摩：另加 1 架 E13A1 参与搜索 | "CHIKUMA launches one E13A1 floatplane in addition to 13 B5N2 that are in CarDiv 3's second wave of morning searches." | chikuma_t |
| 1944-10-24 | 两舰各：剩 2 架，飞往民都洛圣何塞 | "TONE and CHIKUMA both launch their two remaining floatplanes, heading for San Jose, Mindoro Island." | tone_t |

**机型性能（E13A1，combinedfleet 的机型页，数据源自 Francillon 1979）**：
> "Description: Single-engined twin-float reconnaissance seaplane. All-metal construction with fabric-covered control surfaces." / "Accommodation: Crew of three in tandem enclosed cockpits." / "Powerplant: One Mitsubishi Kinsei 43 fourteen-cylinder air-cooled radial rated at 1,060 hp for take-off, and 1,080 hp at 2,000 m" / "Maximum speed 203 kt at 2,180 m" / "Range 1,128 naut miles"
> 配属舰艇一栏明确列有利根、筑摩："Cruisers: Kinugasa, Atago, Takao, Chokai, Maya, Kumano, Chikuma, Tone, Suzuya, etc."
> —— <https://www.combinedfleet.com/ijna/e13a.htm>

**E8N2 配属**：
> "Cruisers: Aoba, Ashigara, Atago, Chokai, … Suzuya, Takao and Tone." / "Crew of two in open cockpits."
> —— <https://www.combinedfleet.com/ijna/e8n.htm>

### 3.4 为什么利根级被选作机动部队的侦察力量

NHHC（S. J. Cox，H-Gram 006-2）把机制说透了：日方宁可用岸基飞机和「战列舰/巡洋舰弹射的
水上飞机」做侦察，也不肯拿航母舰载攻击机去搜索；而中途岛时能用的水侦平台很紧张，
利根、筑摩是仅有的两艘「为搭载 5 架长航程水侦而建造」的舰：

> "Despite this, the Japanese much preferred not to "waste" carrier-based strike aircraft on reconnaissance, preferring to rely instead on long-range land-based aircraft and catapult-launched floatplanes from battleships and cruisers." / "Given the complexity of the Japanese plan, floatplane capable escort ships were spread thin. Within the Japanese carrier force, the two battleships, Haruna and Kirishima, carried three floatplanes (of limited range) and the two cruisers Tone and Chikuma had been built to carry five longer-range floatplanes."
> —— 原始 URL <https://www.history.navy.mil/about-us/leadership/director/directors-corner/h-grams/h-gram-006/h-006-2.html>
> 实际取得（Wayback，NHHC 直连 TLS 失败）<http://web.archive.org/web/20251208121754/https://www.history.navy.mil/about-us/leadership/director/directors-corner/h-grams/h-gram-006/h-006-2.html>

**结果**：两舰整场战争基本都跟着航母走，很少进所罗门那种「耗子洞」（combinedfleet 舰级页
原话，见 §3.1 引文 "they spent much of the war hanging out with the carriers of Combined Fleet,
rather than fighting in rat-holes like the Solomons"）。

**TROM 可核的实际分布**：两舰出动记录里绝大多数日期挂在机动部队名下（珍珠港、威克岛、
拉包尔、达尔文、印度洋、中途岛、第二次所罗门、南太平洋、马里亚纳、莱特湾），
只有在 1943 年下半段才脱离航母去做运输与拉包尔方面任务。

---

## 4. 中途岛侦察专节（重点核实）

### 4.1 搜索计划本身

**六条/七条搜索线怎么分的**（ONI 逐时记录，1942-06-04 东京时）：
> "There will be seven search lines: #1, 181 degrees, Akagi; #2, 158 degrees, Kaga; #3, 123 degrees; #4, 100 degrees; #5, 77 degrees; #6, 54 degrees; all four to be carried out by planes of CruDiv 8. Search distance, 300 miles and 60 miles to the left. #7, to bear 31 degrees, distance 150 miles and 40 miles to left."
> "1640 Message by signal from Comdr. CruDiv 8 to CruDiv 8, info Mobile Force: "CruDiv 8 SigOrd #28. With regards to Mobile Force SigOrd #97. Tone will supply planes for searches on lines 3 and 4 and Chikuma for lines 5 and 6.""
> —— <https://www.history.navy.mil/research/library/online-reading-room/title-list-alphabetically/j/japanese-story-of-the-battle-of-midway.html>（存档同上）

JM-93 的同一段（东京时 0130–0200 出发）：
> "During the time from 0130 to 0200 hours, one carrier-based torpedo-carrying assault plane each from the AKAGI and the KAGA, two Zero-type fleet reconnaissance planes each from the TONE and the CHIKUMA (range of advance, 300 nautical miles, and lateral distance, 40 nautical miles to port), and one type 95 float reconnaissance plane from the HARUNA … were dispatched to search for the enemy to the south and east of the task force. **However, the departure of the TONE, as well as the CHIKUMA was greatly delayed**, and the sixth search plane returned at 0235 hours because of poor weather conditions."
> —— <https://www.ibiblio.org/hyperwar/Japan/Monos/pdfs/JM-93_MidwayOperations,May-June42/JM-93.htm>

> **重要**：JM-93 只说「利根、筑摩都大幅延迟」，**没有说是弹射器故障**，也没区分是哪一架。

### 4.2 出发时间与实际延误

**ONI 的逐机起飞时刻（东京时，5 日）——这是本次能拿到的最细的时刻表**：
> "0135 Chikuma plane takes off on #5 search line."
> "0138 Tone's antisub direct escort plane takes off."
> "0142 Tone's plane takes off on #3 search line."
> "0150 Chikuma's antisub direct escort plane takes off."
> "0200 Tone's plane takes off on #4 search line."
> —— <https://www.history.navy.mil/research/library/online-reading-room/title-list-alphabetically/j/japanese-story-of-the-battle-of-midway.html>

→ 换成本地时（−21 h）：**筑摩 5 号线 0435、利根反潜机 0438、利根 3 号线 0442、
筑摩反潜机 0450、利根 4 号线 0500**。
→ 计划要求「0130–0200 之间出发」，利根 4 号线卡在 0200 上限，**比同舰 3 号线晚 18 分钟**。
combinedfleet TROM 的概括与之吻合：
> "Between 0435-0500, CruDiv 8's TONE and CHIKUMA each launch two E13A1 Jake long-range reconnaissance floatplanes…"
> —— <https://www.combinedfleet.com/tone_t.htm>

combinedfleet 自己的机型/事件页也写「30 分钟延迟」，但那是概数，与 ONI 的 18 分钟不符，见 §7。

### 4.3 延误原因：至少四种说法，均无定论

**（a）弹射器故障 —— 最流行的说法。** 这是「流传」而非「档案」，措辞上就能看出来：
> "Suggestions as to why it didn't take off on time to fly its designated pattern with the other scouts, include a failed catapult (most commonly reported) or engine trouble. Another story, more in keeping with the view that the Japanese commanders were stereotypically self-confident, was that the search for US vessels was done in a perfunctory way, and the commanders of the spotter planes were under-prioritised and left waiting for orders."
> —— <https://imodeler.com/2017/06/scout-4-is-late/>（Wayback 取得：<http://web.archive.org/web/20260517143345/https://imodeler.com/2017/06/scout-4-is-late/>）

**（b）原因不明 —— NHHC 的官方口径，明确拒绝给原因：**
> "Tone's No. 4 scout (an Aichi E13A Type 0 "Jake") launched late, **due to reasons that still remain unclear**, to fly the No. 4 search line."
> —— <https://www.history.navy.mil/about-us/leadership/director/directors-corner/h-grams/h-gram-006/h-006-2.html>（存档同上）

**（c）日文一侧写「利根のカタパルトが故障し」，但同一句里就把「30 分遅れ」标成「とする文献がある」
（有文献如此说），即日文维基也没把它当定论：**
> 「この時、利根のカタパルトが故障し利根4号機（甘利一飛曹、大熊一等飛行兵）の発進が30分遅れ日本海軍敗北の一因となったとする文献がある」
> —— <https://ja.wikipedia.org/wiki/利根_(重巡洋艦)>（tier E）

**（d）罗盘失准（第八战队参谋土井美二中佐的回忆）—— 与「延误」互为因果的另一种解释：**
> 「また土井美二中佐（当時の第八戦隊参謀。利根座乗）は利根4号機のコンパスが狂っており、このためアメリカ艦隊を発見できた可能性を指摘している」
> —— <https://ja.wikipedia.org/wiki/利根_(重巡洋艦)>（tier E，仅记录有这一说，未获原始出处）

→ **结论：延误的「事实」有多份一手材料互证（JM-93 说延迟、ONI 给出逐机时刻、NHHC 说
launched late），但「原因」没有任何一手材料。正文只能写「延误原因至今不明，流传最广的
说法是弹射器故障」。**

### 4.4 发现了什么、什么时候发报

**利根 4 号机（甘利一飞曹机）的报文序列 —— ONI 版（东京时 → 本地时）**：

| 东京时 | 本地时 | 原句（ONI） |
|---|---|---|
| 0245 | 0545 | "Radio message from Tone's #4 plane to Mobile Force: "#1. Sight two surfaced enemy submarines in position bearing 120 degrees, distance 80 miles from my take-off point. Subs' course, 120 degrees. (0220)."" |
| 0255 | 0555 | "Radio message from Tone's plane on #4 search line to Mobile Force: "15 enemy planes are heading towards you."" |
| 0428（发现时刻） | 0728 | （报文本身于 0500 收到）见下条 |
| 0500（收到） | 0800 | "At about 0500, Tone's #4 plane reported: "Sighted what appears to be the enemy composed of 10 (ships), bearing 10 degrees, distance 240 miles from Midway, on course 150 degrees, speed 20 knots (0428)."" |
| 0455 | 0755 | "Two subsequent reports concerning the weather (0440) and the enemy's course and speed (0455) were received" |
| 0530 | 0830 | "At 0530, Tone's plane reported: "The enemy is accompanied by what appears to be a carrier in a position to the rear of the others (0520)."" |
| 0540 | 0840 | "and again at about 0540: "Sight what appears to be 2 cruisers in position bearing 8 degrees, distance 250 miles from Midway; course, 150 degrees; speed 20 knots (0530)."" |
| 0509 | 0809 | "At 0509 hours, the Tone plane reported that "the enemy power was composed of five cruisers and five destroyers."" |

以上全部：<https://www.history.navy.mil/research/library/online-reading-room/title-list-alphabetically/j/japanese-story-of-the-battle-of-midway.html>

**JM-93 是同一套报文的另一种英译**（措辞不同，可作互校）：
> "At about 0500 hours, the first message in respect to the discovery of the enemy, dispatched by the Tone planes of the fourth search line, which was reported to be greatly delayed, was received: "Ten craft resembling the enemy's were sighted at 0428 hours at a compass point 10 degrees and 240 nautical miles off MIDWAY, on a compass course of 150 degrees, and proceeding at a speed of 20 knots." We received reports twice, at 0440 hours in respect to the weather and at 0455 hours regarding the compass course and speed of the enemy, but we did not receive any other information. Therefore, at 0500 hours, we requested information on the type of naval ship."
> "At 0509 hours, the Tone plane reported that "the enemy power was composed of five cruisers and five destroyers." At 0530 hours, it was reported that the enemy was accompanied by something resembling an aircraft carrier end this was reported again at about 0540 hours."
> —— <https://www.ibiblio.org/hyperwar/Japan/Monos/pdfs/JM-93_MidwayOperations,May-June42/JM-93.htm>

**combinedfleet 的浓缩版（本地时）**：
> "At 0728, TONE's E13A1 No. 4 discovers the enemy ships, which later materialize as a carrier group. **The observer does not identify the carriers at the outset, which proves to be a crucial mistake.**"
> —— <https://www.combinedfleet.com/tone_t.htm>

**iModeler 给的四个时刻（本地时，与 ONI 换算后完全对得上）**：
> "0728: "Sight what appears to be ten enemy surface ships, in position 10 degrees, distance 240 miles from Midway. Course 150 degrees, speed over 20 knots"."
> "0758: "...the enemy is on course 80 degrees, speed 20 knots"."
> "0809: "Enemy ships are five cruisers and five destroyers"."
> "0820: "Enemy force accompanied by what appears to be aircraft carrier bringing up the rear"."
> —— <https://imodeler.com/2017/06/scout-4-is-late/>（存档 URL 同上）

> **可核结论**：发现时刻 0728（本地）/0428（东京），报文 0500（东京）才到南云手上；
> 「似乎是航空母舰」的补充报告要到 0530（东京）/0830（本地）才发出。
> **「4 号机没认出航母」这一条在 ONI、JM-93、combinedfleet 三处一致，可以写。**
> **但「没认出航母 = 关键错误」这个评价是 combinedfleet 的措辞，不是档案本身的话，引用时要标明是评论。**

### 4.5 日方对这个延误的检讨

**① JM-93 只记「greatly delayed」，在检讨段里把延误当成已知事实引用，不追原因：**
> "At about 0500 hours, the first message in respect to the discovery of the enemy, dispatched by the Tone planes of the fourth search line, **which was reported to be greatly delayed**, was received"
> —— <https://www.ibiblio.org/hyperwar/Japan/Monos/pdfs/JM-93_MidwayOperations,May-June42/JM-93.htm>

**② JM-93 同时记了搜索计划本身的缺陷（七条线里第 6 线因天候 0235 就返航）：**
> "However, the departure of the TONE, as well as the CHIKUMA was greatly delayed, and the sixth search plane returned at 0235 hours because of poor weather conditions."
> —— 同上

**③ NHHC（美方对日方检讨的再检讨）明确推翻「延误＝败因」这个流传说法：**
> "Its late launch has been cited by many historians as a key factor in the Japanese defeat since it did not detect the U.S. carriers until it was too late. **Actually, Chikuma's No. 1 scout, launched on time, and flying No. 5 search line, should have seen TF-17 at approximately 0615, but did not due to clouds or other factors that remain unclear.** Even if Chikuma No. 1 had found the U.S. carriers at 0615, it was already too late for Nagumo to launch the reserve strike (107 aircraft, armed with anti-ship weapons) before the U.S. carriers started launching."
> "**If Tone No. 4 had launched on time and flown the prescribed route, she would have missed the U.S. carriers**, and the first indication Nagumo would have had of them was the 15 TBDs of Hornet's Torpedo Squadron EIGHT."
> —— <https://www.history.navy.mil/about-us/leadership/director/directors-corner/h-grams/h-gram-006/h-006-2.html>

**④ 日文一侧近年研究也持同一方向（迟发反而导致发现，准时反而会错过）：**
> 「後年の研究では、筑摩1号機（黒田信大尉）は米軍機動部隊の上空を飛んでいたが、雲量のため発見できなかった（第一次攻撃隊隊長友永丈市大尉が「第二攻撃の要ありと認む」を発信する前）。また利根4号機の発進が遅れたからこそアメリカ艦隊を発見できたのであり、定時に発進していたらかえって発見できなかった可能性が高いと言われている」
> —— <https://ja.wikipedia.org/wiki/利根_(重巡洋艦)>（tier E）

**⑤ iModeler 对 4 号机自身的评价（「搜索质量差」的另一路批评）：**
> "The search by Amari and his crew has been described by some as a poor effort, although his comrades in Chikuma's Scout 5 reportedly missed Task Force 17 (which they should potentially have spotted) due to what has been referred to as 'halfhearted' flying – staying above the clouds and looking through gaps, rather than suffering the weather below to carry out a thorough job. Scout 4 picked up '10 surface ships' on the return leg of its flight, that should have been spotted earlier by Scout 5."
> "The crew of Scout 4's biggest failing was to miss an aircraft carrier in the group, until an hour after its first sighting."
> —— <https://imodeler.com/2017/06/scout-4-is-late/>（存档 URL 同上）

### 4.6 本节结论（供正文取用，逐条标可信度）

| 命题 | 能否写进正文 | 依据 |
|---|---|---|
| 利根 4 号机延误出发 | **能**（一手材料互证） | JM-93 "greatly delayed"；ONI 逐机时刻 0200；NHHC "launched late" |
| 延误约 18 分钟（相对同舰 3 号线 0142） | **能，但必须说明是相对 3 号线** | ONI 0142 / 0200 |
| 「延误 30 分钟」 | **不能直接写**，只能写「部分文献作 30 分钟」 | 日文维基「30分遅れ…とする文献がある」；ONI 实测 18 分钟 |
| 延误原因是弹射器故障 | **不能写成事实**，只能写「流传最广的说法」 | NHHC "reasons that still remain unclear"；imodeler "most commonly reported" |
| 0728（本地）发现「约 10 艘水面舰」 | **能** | ONI、JM-93、combinedfleet 一致 |
| 首报未识别出航母，1 小时后才补报 | **能** | ONI 0509/0530/0540；combinedfleet「crucial mistake」 |
| 「延误是日本战败主因」 | **不能**，必须并列反证 | NHHC 明确推翻；日文维基近年研究同向 |
| 真正「该发现却没发现」的是筑摩 1 号机 | **能，但要标为 NHHC 的判断** | NHHC "Chikuma's No. 1 scout … should have seen TF-17 at approximately 0615" |

---

## 5. 两舰结局

> **任务书里「两舰都在莱特湾损失」这句是错的**。筑摩 1944-10-25 在萨马岛外海沉没；
> 利根**活过了莱特湾**，一直撑到 1945-07-28 在吴港被击沉坐底。详见 §6。

### 5.1 筑摩：1944-10-25 萨马岛外海

不是苏里高海峡。筑摩当天在栗田（Center Force）序列内，位置在萨马岛以东。

**经过（combinedfleet，全部日方时刻）**：
> "At 0724, when KUMANO is damaged by a torpedo, CHIKUMA is designated the ad hoc flagship of CruDiv 7."
> "At 0853, CHIKUMA is attacked by four TBM "Avenger" torpedo-bombers from "Taffy Two". She is hit by a Mk.13 torpedo that disables her port screw and rudder; two minutes later she goes dead in the water."
> "At 0907, CHIKUMA reports to YAMATO that she has been torpedoed and is unnnavigable."
> "At 1105, CHIKUMA is attacked by five VC-5 TBM-1Cs from KITKUN BAY. By that time her AA ammunition is mostly exhausted; in fact, during the previous attack some gunners had resorted to using exercise rounds. CHIKUMA is hit port side amidships by two torpedoes and her engine rooms flood. Power is lost. She comes to a stop and takes on a list to port. At 1110, destroyer NOWAKI is dispatched to assist her."
> "After 1415, CHIKUMA is attacked by three TBM-1Cs from OMANNEY BAY (CVE-79), led by VC-75's CO, Lt Allen W. Smith, Jr. Three torpedoes hit her port side amidships. Around 1430, CHIKUMA capsizes and sinks by the stern at 11-52N, 126-36E. NOWAKI rescues some 120 survivors."
> —— <https://www.combinedfleet.com/chikuma_t.htm>

**Tully（Ed Low 图证分析，收在 combinedfleet 的沉舰调查页）给了几乎一致的时刻链**：
> "At 0853 CHIKUMA was hit by a torpedo that smashed the fantail and destroyed her rudder, leaving only the inboard port propeller working and the cruiser left making clockwise circles. At 1105 VC-5 stopped her with two torpedoes in the port side that left her unavigable and listing to port. By 1130 the NOWAKI had joined her off her port side when photographed by a VC-76 plane. There may have been more attack damage before the last blow that came after 2pm. Finally it appears that three torpedoes from VC-75 (USS OMMANEY BAY CVE-79) in the port side at 1415 caused her to capsize to port and sink by the stern."
> —— <https://www.combinedfleet.com/atully08.htm>

**位置**：11-52N, 126-36E（combinedfleet）；11°25′N 126°36′E（en-wiki）。
两处纬度不同（11-52 vs 11-25），见 §7。

**幸存者**：野分救起约 120 人 → 野分当晚被击沉，这批人全灭；只有 1 名未被野分救起的
军官漂了 3 天后被美舰捞起，战后回日本。
> "[3] A single survivor from CHIKUMA was picked up by an American warship three days later."
> —— <https://www.combinedfleet.com/chikuma_t.htm>

**除籍**：1945-04-20。

### 5.2 利根：1945-07-24 / 07-28 吴港，7-29 坐底

**不是莱特湾损失的。** 莱特湾中利根只是受损（舵机失灵），撤出后一直用到战争结束。

**1944-10-25 的损伤**：
> "At 1249 Kurita's retiring force is attacked by carrier aircraft. TONE is attacked by four dive-bombers and receives one hit to starboard aft, opening a large hole in the hull and disabling her steering. Her speed is temporarily limited to 15 kts."
> "At 1330 TONE, now using manual steering, is again attacked by dive-bombers, receiving a "250-kg" bomb hit (a dud)."
> "By 1341 TONE can make 30 knots again."
> —— <https://www.combinedfleet.com/tone_t.htm>

**结局三段**：
> "19 March 1945: Vice Admiral … Marc A. Mitscher's … Task Force 58 raids Kure. TONE, caught in the middle of Kure Bay, receives one direct hit, jamming her No. 3 turret in train, and several near misses."
> "24 July 1945: TONE is attacked by aircraft of … TF 38 from USS SHANGRI-LA (CV-38), COWPENS (CVL-25) and MONTEREY (CVL-26). TONE receives three direct hits and several near misses."
> "28 July 1945: After 1000 TONE is attacked by aircraft from USS BATAAN (CVL-29), TICONDEROGA (CV-14) and MONTEREY (CVL-26). Her AA gunners put up a steady volume of heavy flak which is rapidly reduced after the first bomb hits. TONE receives two direct hits to port side (one of them a 1,000-lb aft) and six near misses. Near misses cause serious flooding and TONE develops a 21-degree list to port. After additional damage control parties arrive from ashore, counterflooding manages to reduce the list, but the flooding cannot be stopped."
> "A second strike against TONE is launched that afternoon from USS ESSEX (CV-9), BATAAN, MONTEREY and RANDOLPH (CV-15), but redirected against targets of opportunity in the Inland Sea after a report is received that TONE had been sunk."
> "29 July 1945: Settles on the bottom in shallow water."
> "20 November 1945: Removed from the Navy List."
> "4 May 1948: The hull is refloated."
> "30 September 1948: The scrapping of the hull is completed."
> —— <https://www.combinedfleet.com/tone_t.htm>

**日文一侧对 7-28 的补充（损伤细节，tier E，可当线索）**：
> 「7月28日にも再度空襲を受け、アメリカ軍艦載機の空襲により左舷後部に直撃弾2発と至近弾6発を受けた…左舷後部の直撃弾は1000ポンド爆弾で、地上施設破壊用の瞬発信管であり、利根の水平装甲板を貫通せずに爆発したが被害は甚大であり、至近弾もあいまって大浸水をきたした。一時は左舷に20度以上傾斜したが…7月29日に着底」
> —— <https://ja.wikipedia.org/wiki/利根_(重巡洋艦)>

**「以哪一天为 fate_date」**：combinedfleet 把 7-24 记作「Final Destruction」、7-29 记作坐底；
navypedia 写 "sunk 24.7.1945"；en-wiki 写 "Sunk 24 July 1945"；日文维基写「1945年7月28日
艦載機の攻撃で大破着底」。→ **四说并存，见 §7。**

---

## 6. 与任务书不符之处（主会话请注意）

> 按 SCHEMA §9.3 的规矩，任务书里的史实陈述一律当「待核实」处理。以下是我查到与任务书
> 表述不符的条目。

| # | 任务书原文 | 查到的情况 | 依据 |
|---|---|---|---|
| **1** | 「1944 年莱特湾（**两舰都在此役损失**）」 | **错。只有筑摩在莱特湾（萨马岛外海）沉没。利根在莱特湾只是被炸弹命中右舷后部、舵机失灵，1944-10-28 还随残部回到文莱，一直活到 1945-07-28 在吴港被击沉坐底、1948 年拆解。** | tone_t：`"At 1249 … one hit to starboard aft … disabling her steering"`、`"The remnants of Force "A" arrive at Brunei Bay"`、`"28 July 1945 … TONE receives two direct hits to port side"`、`"29 July 1945: Settles on the bottom in shallow water."` |
| **2** | 「两舰在莱特湾（**苏里高海峡？**）的损失经过」 | **苏里高海峡是错的。** 筑摩当天属栗田的 Center Force（Force "A"），在**萨马岛以东**被舰载机雷击沉没。苏里高海峡那是西村祥治的第二游击部队（山城、扶桑、最上），利根型两舰都不在其中。 | chikuma_t：`"22 October 1944: Operation "SHO-1-GO" … CruDiv 7's KUMANO, SUZUYA, TONE and CHIKUMA sortie from Brunei … with Vice Admiral Kurita's First Mobile Striking Force"`；沉没条 `"Around 1430, CHIKUMA capsizes and sinks by the stern at 11-52N, 126-36E."` |
| **3** | 「利根 4 号侦察机…**延误原因（弹射器故障？）**」 | 延误是事实（一手材料互证），**但原因至今不明**。NHHC 原文 `"due to reasons that still remain unclear"`。弹射器故障只是「most commonly reported」的流传说法。**正文不能把它写成事实。** | NHHC H-Gram 006-2；imodeler |
| **4** | （隐含）「延误约 30 分钟」 | ONI 逐机时刻显示：利根 3 号线 0142（东京时）、4 号线 0200，**相差 18 分钟**。「30 分钟」出自部分文献而非档案。 | ONI 逐时记录；ja-wiki `"30分遅れ…とする文献がある"` |
| **5** | （隐含）「发现航母＝4 号机的功劳」 | 4 号机**首报没认出航母**，1 小时后才补报「后面似乎跟着一艘航母」。这一条三源一致，可以写，且比「发现航母」更准确。 | ONI 0509/0530/0540；JM-93；combinedfleet `"does not identify the carriers at the outset, which proves to be a crucial mistake"` |

**另外两处易错点（不是任务书的问题，但正文容易写错）**：

- **1943-11-05 拉包尔空袭中受损的是筑摩，不是利根。** 英文维基的 Tone-class 条目把这件事
  写在利根身上（"In 1943, Tone patrolled in Solomon Islands theatre where she was damaged by an
  air raid on the base at Rabaul on 5 November."），与 TROM 冲突。TROM 显示利根当时正在
  本土近海拖带被 USS HALIBUT 雷击的隼鹰，11-06 入吴：
  > TROM：「5 November 1943: The task group is attacked by USS HALIBUT (SS-232) near Bungo
  > Suido … JUNYO is damaged and has to be towed to Kure.」「6 November 1943: Arrives at Kure
  > Navy Yard. Begins a refit.」
  > 日文维基点明拖带者是利根：「11月5日朝、隼鷹が日本近海でアメリカの潜水艦ハリバットから
  > 雷撃され…このため、利根は隼鷹を曳航、11月6日呉に到着した」
  > 筑摩受损条：「Around 0931 CHIKUMA is attacked by an SDB dive-bomber from SARATOGA. She
  > receives a near miss off the starboard catapult, which disables No. 3 torpedo mount and
  > causes slight flooding; 3 crewmen were wounded.」
  → **正文写「1943-11-05 拉包尔空袭，筑摩受近失弹轻伤；利根不在场」。**

- **利根水侦在珍珠港当天损失的编号，两页 TROM 说法不同**（利根页：`"TONE's E8N2 No. 3 is
  lost with her crew"` 是中途岛；珍珠港那条是 `"the E13A1 capsizes and is lost"`）。这个已经
  对上了，不算矛盾，仅提示别把两件事混在一起。

---

## 7. 有争议的记载（并列，不裁决）

### 7.1 筑摩是「被野分雷击处分」还是「因空袭自行沉没」

四种说法并存，全部列出：

| 说法 | 原句 | 出处 |
|---|---|---|
| **A. 野分以鱼雷处分** | "In Battle off Samar on 25 October took part in torpedo attack on U.S. escort carriers …; later **removed survivors from CHIKUMA and scuttled with torpedoes**." | <https://www.combinedfleet.com/nowaki_t.htm> |
| **B. 被野分击沉** | "In battle at Samar 25.10.1944 she was heavy damaged by American carrier aircraft and **sunk by destroyer Nowaki**." | <https://www.navypedia.org/ships/japan/jap_cr_tone.htm> |
| **C. 空袭致翻覆沉没（野分只来得及救幸存者）** | "Around 1430, CHIKUMA capsizes and sinks by the stern at 11-52N, 126-36E. NOWAKI rescues some 120 survivors." | <https://www.combinedfleet.com/chikuma_t.htm> |
| **D. 旧说 A/B，新研究支持 C** | "It is generally thought Nowaki took off survivors from Chikuma, and then scuttled her … but **a more recent study suggests Chikuma sank from the effect of the air attack, and Nowaki only arrived in time to pick up survivors from the water**." | <https://en.wikipedia.org/wiki/Japanese_cruiser_Chikuma_(1938)>（tier E，但此处正是转述 Tully 的研究） |
| **E. 日文一侧（支持「处分」）** | 「筑摩はその後、駆逐艦野分により雷撃処分された」 | <https://ja.wikipedia.org/wiki/筑摩_(重巡洋艦)>（tier E） |

Tully 本人在沉舰调查页的表述最谨慎，把「翻覆」当定论、把「野分处分」留白：
> "Finally it appears that three torpedoes from VC-75 (USS OMMANEY BAY CVE-79) in the port side at 1415 caused her to capsize to port and sink by the stern. **All the evidence roughly agrees with NOWAKI commencing rescue operations about now.**"
> —— <https://www.combinedfleet.com/atully08.htm>

> **建议正文写法**：写「筑摩于 1430 前后向左翻覆、尾部下沉于 11-52N 126-36E；野分号随即
> 救起约 120 名幸存者。长期流传的说法是野分以鱼雷将其处分，但近年研究认为她在空袭中
> 已经倾覆沉没，野分赶到时只来得及救人。**两说并列，不裁决。**」

### 7.2 筑摩沉没位置的纬度

- combinedfleet：`11-52N, 126-36E`
- en-wiki：`11°25′N 126°36′E`

差 27 分纬度（约 50 km）。经度一致。**两说并列**。日文维基未给坐标。

### 7.3 利根级的航空搭载数

| 数值 | 原句 | 出处 |
|---|---|---|
| 计划 6 机，常用 4–5 机 | "计划:水上機6機 / 定数(-1942年6月25日):零式水偵3機、九五式水偵2機 / 定数(1942年6月25日-):零式水偵5機"；正文「計画では6機…通常5機ないし4機で運用」 | <https://ja.wikipedia.org/wiki/利根_(重巡洋艦)>（tier E） |
| 6 架（3 架 E7K1 + 3 架 E8N1） | "…4 x 3 - 610 TT (24), **6 seaplanes (3 E7K1, 3 E8N1), 2 catapults**" | <https://www.navypedia.org/ships/japan/jap_cr_tone.htm> |
| 5 架 | "they carried 5, as compared to the 3 carried by most other Japanese CAs" | <https://www.combinedfleet.com/tone_c.htm> |
| 5 架（长航程） | "the two cruisers Tone and Chikuma had been built to carry five longer-range floatplanes" | NHHC H-Gram 006-2 |
| 最多 4 架 E7K2 + 4 架 E8N1，正常 6 架（其中 4 架 E8N1），实战从未超过 5 架 | "A maximum of four Kawanishi E7K2 "Alf" three-seat floatplanes and four Nakajima E8N1 "Dave" floatplanes could be carried, the normal complement being six, of which four were to be E8N1s. In practice, no more than five were ever embarked." | <https://en.wikipedia.org/wiki/Tone-class_cruiser>（tier E） |

→ **正文写「设计搭载 6 架，实战通常 4–5 架」是安全的；具体机型分年表用日文维基那组
（1942-06-25 前 零式 3 + 九五式 2；之后 零式 5），但须注明是单一来源的定数表，未得第二源互证。**

### 7.4 利根 4 号机延误的时长

- ONI 逐机时刻：3 号线 0142 → 4 号线 0200，差 **18 分钟**（东京时）。
- 日文维基：「発進が**30分**遅れ…**とする文献がある**」——即标注为某些文献的说法。
- combinedfleet 全篇未给具体分钟数。

→ **两说并列；正文若写分钟数，须写明「据 ONI 逐机时刻为 18 分钟；另有文献作 30 分钟」。**

### 7.5 利根 fate_date 取哪一天

| 日期 | 说法 | 出处 |
|---|---|---|
| 1945-07-24 | "sunk 24.7.1945" / "Sunk 24 July 1945" | navypedia；en-wiki |
| 1945-07-28 | 「1945年7月28日艦載機の攻撃で大破着底」 | ja-wiki |
| 1945-07-29 | "Settles on the bottom in shallow water." | combinedfleet |
| 1945-11-20 | "Removed from the Navy List."（除籍日，非沉没日） | combinedfleet；navypedia/ja-wiki 同 |

→ **7-24 是致命空袭开始、7-28 是决定性打击、7-29 是坐底。三个日期指向三个不同事件，
正文应写清事件链而不是挑一个当「沉没日」。**

### 7.6 中途岛搜索是否「七条线」还是「六条线」

- ONI：`"There will be seven search lines: #1 … #7"`，但其中 #1/#2 由赤城、加贺的舰攻担任，
  #3–#6 由第八战队（利根/筑摩）担任，#7 由榛名担任。
- JM-93：只数了 7 架飞机（`"one carrier-based torpedo-carrying assault plane each from the AKAGI and the KAGA, two … from the TONE and the CHIKUMA …, and one type 95 float reconnaissance plane from the HARUNA"`）。
- NHHC：`"the Japanese launched seven aircraft to conduct a search of about a 200-degree sector"`。

→ **「7 架飞机 / 7 条搜索线」一致，不矛盾。** 只有表述颗粒度不同。

---

## 8. 未获取 / 卡住的地方

1. **Tully《Fate of CHIKUMA and CHOKAI》(TullyLeyte.pdf, 3.1 MB) 是纯扫描图，无文字层。**
   已下载到 `_raw/tully-leyte-chikuma.pdf`，pypdf 抽出 11 页全空。→ **无法提供英文原句，故不引。**
   所幸同一作者同结论的 HTML 页 `atully08.htm` 有全文，本笔记改引那一页并注明。

2. **USNI《Solving some Mysteries of Leyte Gulf: Fate of the "Chikuma" and "Chokai"》**
   （*Warship International* 37(3), 2000, pp. 248–258）—— `usni.org` 403、`jstor.org` 需订阅，
   **未获取原文**。en-wiki 引它作 [9][10][11] 之一，即 §7.1 的 D 说。本笔记只转述
   en-wiki 的转述，未触原文。

3. **利根型的原厂设计图/官方计划书未获取。** 主尺度、装甲分部位值全部来自 navypedia（D 级）
   与二战文献的二次汇总，未触一手图纸。→ 若正文要写 `protection.armor.*` 的 `qual` 明细值，
   建议主会话另行核实；本笔记只给 navypedia 与 ja-wiki 的两套数字（两者在弹药库装甲上口径不同：
   navypedia "belt 100 (machinery) – 145 (magazines), deck 65 – 31"；ja-wiki「舷側：145mm 甲板：35mm」）。

4. **「呉式2号射出機」这个型号未得第二源。** 只有日文维基一处（tier E），
   不能写进 fact。正文若要写弹射器型号，需另找 C/D 级来源。

5. **1943-11-05 拉包尔空袭中利根的具体位置，TROM 未直说。** TROM 只写利根 10-31 离特鲁克、
   11-05 护航队在本土近海遭 USS HALIBUT 攻击、11-06 入吴。**「利根拖带隼鹰」这一细节仅
   日文维基一处（tier E）**，TROM 未点名拖带者。→ 正文可写「利根当时不在拉包尔」，
   但「拖带隼鹰」要标为单一来源。

6. **日方战报原件（「軍艦利根戦闘詳報」Ref. C08030568500 等）全部在 JACAR，需登录且为图像。**
   未尝试。→ 本笔记所有日方时刻全部转引自 combinedfleet / ONI / JM-93 三者的英译，
   未核日文原件。

7. **中途岛当天利根、筑摩各机的水侦乘员全名**，TROM 只给了 3 人：
   利根 1 号机 `WO Narukawa Ryozo`（珍珠港）、筑摩 5 号机 `PO3c Hara Hisashi`（中途岛）、
   筑摩 2 号机 `Special Duty Ensign Fukuyama`（第二次所罗门）、利根 4 号机 `甘利一飛曹`（仅日文维基给，
   且只给姓）。→ **利根 4 号机乘员的英文拼写未获**；日文维基给「甘利一飛曹、大熊一等飛行兵」。

---

## 9. 交付摘要

### 9.1 数量统计

| 项 | 数量 |
|---|---|
| 舰级文件 | 0（本轮不写 fact） |
| 单舰文件 | 0 |
| 切片文件 | 0 |
| 正文文件 | 0（按任务书要求，正文由主会话统一写） |
| 新登记来源 | **10** 条（见 `sources-fragment.yaml`；其中 7 条 D 级可作数据/叙述来源，3 条 tier E 仅作线索：`tone-class-design-ja` / `tone-ca-ja` / `chikuma-ca-ja`） |
| 复用已登记来源 | **3**（`oni-japanese-story-midway`、`jm93-midway-operations`、`nhhc-h006-2-isr-midway`） |
| TROM 事件行（利根，§2.1 表内实计） | 61 |
| TROM 事件行（筑摩，§2.2 表内实计） | 43 |
| 英文引文块合计（全文以 `>` 起首的行） | 128 |
| 抓取原始文件 | **50** 个存 `_raw/`（21 .htm + 24 .html + 2 .pdf + 3 .json），另 36 个 `.txt` 是脚本转出的纯文本副本 |

### 9.2 卡住的地方（一句话版）

- Tully 的 Chikuma 沉没分析 PDF 是**纯扫描图无文字层**，抽不出原句 → 改引同一作者同结论的
  HTML 页 `atully08.htm`。
- USNI / JSTOR 上 Tully 2000 年那篇原文**拿不到**（403 / 订阅墙），只能引 en-wiki 的转述。
- **NHHC 全站 TLS 握手失败**（`history.navy.mil`），改走 Wayback 取到全文；
  引用时给了 NHHC 原 URL + 存档 URL 两条。
- 日方战报原件全在 JACAR（需登录、图像格式），**未核**；所有日方时刻为英译转引。

### 9.3 有争议的记载（并列，未裁决）

1. **筑摩是「被野分雷击处分」还是「空袭中已倾覆、野分只救人不处分」** —— 五说并存，§7.1。
2. **筑摩沉没纬度**：`11-52N` vs `11°25′N`，差约 50 km，§7.2。
3. **利根级搭载机数**：5 架 / 6 架 / 「最多 8 架但实战从未超 5」——四处数字不同，§7.3。
4. **利根 4 号机延误时长**：ONI 逐机时刻 18 分钟 vs 部分文献 30 分钟，§7.4。
5. **利根 fate_date 取 7-24 / 7-28 / 7-29** —— 三个日期对应三个不同事件，§7.5。
6. **利根 4 号机延误原因**：弹射器故障 / 发动机故障 / 指挥文化轻慢侦察 / 罗盘失准，
   **四说皆无一手材料**，§4.3。

### 9.4 给主会话的三条硬提醒

1. **「两舰都在莱特湾损失」是错的。** 只有筑摩在 1944-10-25 萨马岛外海沉没；利根活到
   1945-07-28 吴港被击沉、1948 年拆解。**且不在苏里高海峡**——两舰都在栗田的 Center Force。
2. **中途岛那段「延误导致战败」的流行叙事已被 NHHC 明确推翻**，正文若沿用必须同时给出
   反证（`nhhc-h006-2-isr-midway` 已登记，可直接引）。
3. **延误原因不能写成事实。** NHHC 原话是 `"due to reasons that still remain unclear"`。
