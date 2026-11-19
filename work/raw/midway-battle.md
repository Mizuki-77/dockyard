# 中途岛海战 逐时战斗细节（1942-06-03 ～ 06-07）

> 采集对象：为 `website-warships` 项目提供可溯源的战斗时间线。
> 采集日期：2026-11-19。全程直连，未使用代理。

---

## 0. 时间口径与记账规则

**统一使用中途岛当地时间（Midway local / Zone +12）。**

所有日方 TROM（combinedfleet.com）在叙述中途岛段时**已改用当地时间**，其自述换算规则原句：

> "Note: For convenience and familiarity local times and date are used herein until AKAGI's sinking as the vast majority of sources, even some Japanese ones, utilize this approach. To convert to Tokyo (JST) or Zone 9 time, subtract three hours but advance one one day ahead of a Midway Local time - (Tully)"
> —— [S1] http://www.combinedfleet.com/Akagi.htm

即 **JST = 当地 − 3 小时 + 1 天**，反推 **当地 = JST + 3 小时 − 1 天**。

《The Japanese Story of the Battle of Midway》（ONI 译自南云一手战斗详报）的「Outline of Events」段落**全部使用 JST**，因此本文凡引该件，均标注「原记为 JST xx:xx」并给出换算值。交叉校验示例：该件记飞龙被俯冲轰炸「at 1403」，1303+3h → 当地 1703，与 [S4] 飞龙 TROM 的 1703 完全吻合；该件记苍龙沉没「at 1613」，→ 当地 1913，与 [S3] 的 1912 吻合。换算链自洽。

**三条记账纪律**（对应任务书硬规矩 2、3、4）：

- `未获取` = 已检索的 A/B 级源里确实没有该数据，**不做任何推算或常识补全**。
- `0` 只用于来源明确写出「无 / 没有」的情形，并引原句。
- 凡两源冲突，**两边原话并列，不裁决**。

---

## 0b. 任务书前提纠错（规矩 5：先说前提错在哪）

采集过程中发现任务书有 6 处与原始材料不符，先列出，正文按核实后的事实写：

**（1）「10:22-10:26 麦克拉斯基队俯冲，加贺、赤城、苍龙相继中弹」——错在归因。**
加贺、赤城确由麦克拉斯基（Cdr. C. Wade McClusky）率领的企业号 VS-6 / VB-6 命中；**苍龙是企业号以外的约克城号 VB-3（Lt. Cdr. Maxwell F. Leslie）打的**，与麦克拉斯基无关：

> "This squadron (VB-3) consisted of 17 scout bombers, each with one 1,000-pound bomb. … At 1025 VB-3 was ordered to attack."
> "Three direct hits were scored on her at 0725, 0726, and 0728."（苍龙自记，JST）
> —— [S17-cn7] https://www.ibiblio.org/hyperwar/USN/USN-CN-Midway/USN-CN-Midway-7.html ；[S21] japanese-story 页

**（2）「美军岸基鱼雷机（TBF、B-26、SB2U、SBD 各队），几乎全灭」——对一半，错一半。**
「几乎全灭」只适用于 TBF 与 B-26；VMSB-241 的 SBD/SB2U 是**重大损失但远非全灭**：

> "Of the 16 SBD's which engaged in this attack, 8 returned to the base, and of these only 6 remained fit for service."
> —— [S17-cn6] https://www.ibiblio.org/hyperwar/USN/USN-CN-Midway/USN-CN-Midway-6.html
> "Two of our planes were forced to land in the water before reaching Midway"（SB2U，11 架中）
> —— 同上

**（3）「美军岸基飞机的战果是否为零」——前提本身设错了：不是零。**
全战役美军**唯一一发命中日舰的鱼雷**就是中途岛岸基 PBY 打的：

> "At 0153 one of the PBYs, flown by Ensign Gaylord Probst, hit a Japanese tanker, Akebono Maru, the only U.S. torpedo to damage a Japanese ship in the entire battle"
> —— [S24] https://www.history.navy.mil/about-us/leadership/director/directors-corner/h-grams/h-gram-006/h-006-3.html

**（4）「利根 4 号机延迟起飞的影响」——不能当作既定的失败原因。**
NHHC 官方 H-gram 明确反过来说：

> "Actually, Chikuma's No. 1 scout, launched on time, and flying No. 5 search line, should have seen TF-17 at approximately 0615, but did not due to clouds… If Tone No. 4 had launched on time and flown the prescribed route, she would have missed the U.S. carriers"
> —— [S23] https://www.history.navy.mil/about-us/leadership/director/directors-corner/h-grams/h-gram-006/h-006-2.html

**（5）「约克城号被伊-168 击沉（6 月 7 日）」——命中在 6 日，沉没在 7 日，二者不能混。**
伊-168 是 6 月 6 日 1331/1332 命中；约克城 7 日清晨才翻转沉没（见 §2、§3）。

**（6）「04:30 各舰出动数」——飞龙的单项数字未获取。**
可查到赤城/加贺/苍龙各「18 舰爆 + 9 零战」，飞龙的分项数字在所查 A/B 级源里**没有单独列出**；只能确认第一波总计 108 机（36 舰攻 / 36 舰爆 / 36 零战）。飞龙那 36 机里的分项按规矩不做减法倒推，列 `未获取`。

---

## §1 参战兵力全表

### 1.1 日方 · 第一航空舰队机动部队（南云忠一，旗舰赤城）

出处：[S1] http://www.combinedfleet.com/Akagi.htm ；[S20] https://www.history.navy.mil/research/library/online-reading-room/title-list-alphabetically/c/composition-of-japanese-forces.html

> "AKAGI departs Hashirajima for the Invasion of Midway as flagship of CarDiv 1 of Vice Admiral Nagumo's First Mobile Force, Carrier Strike Force also consisting of CarDiv 2's HIRYU and SORYU, BatDiv 3/2's HARUNA and KIRISHIMA, CruDiv 8's TONE and CHIKUMA, DesRon 10's light cruiser NAGARA with DesDiv 4's NOWAKI, ARASHI, HAGIKAZE and MAIKAZE, DesDiv 10's KAZAGUMO, YUGUMO and MAKIGUMO and DesDiv 17's URAKAZE, ISOKAZE, TANIKAZE and HAMAKAZE." —— [S1]

| 舰 | 舰长 | 航空队指挥官 / 编制 | 原句出处 |
|---|---|---|---|
| 赤城 Akagi（CarDiv 1 旗舰） | 舰长 青木泰二郎 Capt. Aoki Taijirō | 航空队指挥官 Cdr. Fuchida Mitsuo；零战 18（Lt.Cdr. Itaya Shigeru）、舰爆 18（Lt.Cdr. Chihaya Takehiko）、舰攻 18（Lt.Cdr. Murata Shigeharu）+ 第六航空队零战 6 | "Akagi, Capt. Aoki Taijirō" / "Akagi Air Unit, Comdr. Fuchida Mitsuo 18 Mitsubishi A6M2 … Lt. Comdr. Itaya Shigeru" —— [S20] |
| 加贺 Kaga | 舰长 冈田次作 Capt. Okada Jisaku（KIA） | 飞行队长 Lt.Cdr. Kusumi Tadashi（KIA）；零战 18（Lt. Satō Masao）、舰爆 18（Lt. Ogawa Shōichi, KIA）、舰攻 27（Lt. Kitajima Ichirō）+ 第六航空队零战 9 + 备用舰爆 2 | "Kaga, Capt. Okada Jisaku (KIA)" / "Kaga Air Unit, Lt. Comdr. Kusumi Tadashi (KIA)" —— [S20] |
| 飞龙 Hiryu（CarDiv 2 旗舰） | 舰长 加来止男 Capt. Kaku Tomeo（KIA） | 飞行队长 Lt.Cdr. Tomonaga Jōichi（KIA）；零战 18（Lt. Mori Shigeru, KIA）、舰爆 18（Lt. Kobayashi Michio, KIA）、舰攻 18（Lt. Kikuchi Rokurō, KIA）+ 第六航空队零战 3 | "Hiryu, Capt. Kaku Tomeo (KIA)" / "Hiryu Air Unit, (aircraft numbers approximate) Lt. Comdr. Tomonaga Jōichi (KIA)" —— [S20] |
| 苍龙 Soryu | 舰长 柳本柳作 Capt. Yanagimoto Ryūsaku（KIA） | 飞行队长 Lt.Cdr. Egusa Takashige；零战 18（Lt. Suganami Masaharu）、舰爆 16（Lt. Ikeda Masahiro）、舰攻 18（Lt. Abe Heijirō）+ 第六航空队零战 3 + 彗星 D4Y1 舰爆 2 | "Soryu, Capt. Yanagimoto Ryūsaku (KIA)" / "Soryu Air Unit, Lt. Comdr. Egusa Takashige" —— [S20] |

**航空兵力总数（分歧，两说并列）**

> "First Mobile Force/Carrier Strike Force, which comprised the four large carriers Akagi, Kaga, Soryu, and Hiryu with a total of 229 embarked aircraft."
> —— [S18] https://www.history.navy.mil/browse-by-topic/wars-conflicts-and-operations/world-war-ii/1942/midway.html

> "Organization #5 composed of 36 ship-based fighters, 36 ship-based bombers, and 36 ship-based torpedo planes, took off to attack Midway."（即第一波 108 机）
> —— [S21] https://www.history.navy.mil/research/library/online-reading-room/title-list-alphabetically/j/japanese-story-of-the-battle-of-midway.html

**护航舰艇**

| 队 | 指挥官 | 舰 | 原句 |
|---|---|---|---|
| 第八战队 CruDiv 8 | 阿部弘毅 Rear Adm. Abe Hiroaki | 利根 Tone、筑摩 Chikuma（各携 E13A1 水侦 3、E8N2 水侦 2） | "Cruiser Division 8 / Rear Adm. Abe Hiroaki / Tone / 3 Aichi E13A1 … 2 Nakajima E8N2" —— [S20] |
| 第三战队第二小队 BatDiv 3/2 | 高间完 Rear Adm. Takama Tamotsu（座舰榛名） | 榛名 Haruna、雾岛 Kirishima（各携 E8N2 3） | "Battleship Division 3, (Section 2) / Rear Adm. Takama Tamotsu, in Haruna" —— [S20] |
| 第十水雷战队 DesRon 10 | 木村进 Rear Adm. Kimura Susumu（座舰长良） | 长良 Nagara（E11A1 夜侦 1） | "Rear Adm. Kimura Susumu, Commander Destroyer Squadron 10 / in light cruiser Nagara" —— [S20] |
| 第十驱逐队 DesDiv 10 | 阿部俊雄 Capt. Abe Toshio | 风云 Kazagumo、夕云 Yūgumo、卷云 Makigumo | "Destroyer Division 10 / Capt. Abe Toshio / Kazagumo / Yūgumo / Makigumo" —— [S20] |
| 第十七驱逐队 DesDiv 17 | 北村昌幸 Capt. Kitamura Masayuki | 矶风 Isokaze、浦风 Urakaze、滨风 Hamakaze、谷风 Tanikaze | "Destroyer Division 17 / Capt. Kitamura Masayuki" —— [S20] |
| 第四驱逐队 DesDiv 4 | 有贺幸作 Capt. Ariga Kosaku | 岚 Arashi、野分 Nowake、萩风 Hagikaze、舞风 Maikaze | "Destroyer Division 4 / Capt. Ariga Kosaku / Arashi / Nowake / Hagikaze / Maikaze" —— [S20] |
| 补给部队 Supply Group | 太田正尚 Capt. Ota Masanao | 极东丸、神国丸、东邦丸、日本丸、国洋丸；驱逐舰秋云（6 月 3 日自 DesDiv 10 调入） | "Supply Group / Oilers / Capt. Ota Masanao / Kyokutō Maru / Shinkoku Maru / Tōhō Maru / Nippon Maru / Kokuyō Maru / Destroyer Akigumo – from Destroyer Division 10 (3 June 1942)" —— [S20] |

**各驱逐舰舰长（TROM 可查者）**

> "Ship's captain: Commander Watanabe Yasumasa [49] (prev. C.O. OSHIO). Assigned to Desdiv 4 (ARASHI, HAGIKAZE, NOWAKI, MAIKAZE)"
> —— [S12] http://www.combinedfleet.com/arashi_t.htm
> "Ship's captain: Commander Koga Mogotaro [49]."
> —— [S14] http://www.combinedfleet.com/nowaki_t.htm
> "Ship's captain: Commander Tomura Kiyoshi [49] (prev. C.O. SHIRAYUKI)."
> —— [S15] http://www.combinedfleet.com/kasumi_t.htm
> "Commanding Officer: Cdr Semba Shigeo (50)"
> —— [S16] http://www.combinedfleet.com/yugumo_t.htm

| 舰 | 舰长 | 状态 |
|---|---|---|
| 岚 Arashi | Cdr. 渡边保正 Watanabe Yasumasa | 已获取 |
| 野分 Nowaki | Cdr. 古贺茂太郎 Koga Mogotaro | 已获取 |
| 霞 Kasumi（属运输船团护卫） | Cdr. 户村清 Tomura Kiyoshi | 已获取 |
| 夕云 Yugumo | Cdr. 仙波繁雄 Semba Shigeo | 已获取 |
| 荒潮 Arare | Cdr. 小原利道 Ohara Toshimichi | 已获取（TROM 原句 "Commanding Officer: Cdr Ohara Toshimichi (49)"） |
| 萩风 Hagikaze / 舞风 Maikaze / 矶风 Isokaze / 谷风 Tanikaze / 浦风 Urakaze / 滨风 Hamakaze / 风云 Kazagumo / 卷云 Makigumo / 朝潮 Asashio / 荒潮 Arashio | **未获取** | combinedfleet 相应 TROM 页 404（已试 `_t.htm`、`.htm`、`_tr.htm` 三种命名均失败） |

**巡洋舰舰长（TROM 可查者）**

| 舰 | 舰长 | 原句 |
|---|---|---|
| 利根 Tone | 冈田为次 Capt. Okada Tametsugu（1941-09-10 就任，1942-07-14 去职） | "10 September 1941: Captain (later Rear Admiral) Okada Tametsugu (45)… is appointed the CO." —— [S5] http://www.combinedfleet.com/tone_t.htm |
| 筑摩 Chikuma | 小村敬三 Capt. Komura Keizo（1941-08-11 就任，1942-11 去职） | "11 August 1941: Captain (later Rear Admiral) Komura Keizo (45)… is appointed the CO." —— [S6] http://www.combinedfleet.com/chikuma_t.htm |
| 三隈 Mikuma | 崎山释夫 Capt. Sakiyama Shakao（1940-11-01 就任） | "1 November 1940: Captain (Rear Admiral, posthumously) Sakiyama Shakao (42)… is appointed the CO." —— [S7] http://www.combinedfleet.com/mikuma_t.htm |
| 最上 Mogami | 曾祢章 Capt. Sone Akira（1941-09-10 就任） | "10 September 1941: Captain (later Rear Admiral) Sone Akira (44)(former CO of NAGARA) is appointed the CO." —— [S8] http://www.combinedfleet.com/mogami_t.htm |
| 榛名 Haruna | 高间完 Capt. Takama Tamotsu（1941-08-20 就任；1942-05-01 晋升少将，仍兼舰长至 1942-06-20） | "20 August 1941: Captain (promoted Rear Admiral 1 May 1942; later Vice Admiral) Takama Tamotsu (41)… is appointed the CO." —— [S9] http://www.combinedfleet.com/haruna.htm |
| 雾岛 Kirishima | 岩渊三次 Capt. Iwabuchi Sanji（1942-04-20 就任） | "20 April 1942: Early naval aviator Captain (Vice Admiral, posthumously) Iwabuchi Sanji (43)… is appointed CO." —— [S10] http://www.combinedfleet.com/Kirishima.htm |
| 长良 Nagara | 直井俊夫 Capt. Naoi Toshio（1941-09-10 就任，1942-07-10 去职） | "10 September 1941: Captain Naoi Toshio (47)… is appointed the CO." —— [S11] http://www.combinedfleet.com/nagara_t.htm |

### 1.2 日方 · 主力部队（山本五十六，旗舰大和）

> "Main Body (First Fleet) / Adm. Yamamoto / Battleship Division 1 / Rear Adm. Takayanagi Gihachi / Yamato / Mutsu / Nagato / Small Carrier / Hōshō / Destroyer / Yūkaze / Seaplane Carriers / Chiyōda / Nisshin - carrying 2 motor torpedo boats and 6 midget submarines. / Screen / Destroyer Squadron 3 / Rear Adm. Hashimoto Shintaro in light cruiser Sendai"
> —— [S20]

| 队 | 指挥官 | 兵力 | 舰长 |
|---|---|---|---|
| 第一战队 BatDiv 1 | 高柳仪八 Rear Adm. Takayanagi Gihachi | 大和 Yamato（联合舰队旗舰）、陆奥 Mutsu、长门 Nagato | **未获取** |
| 凤翔 Hōshō | — | 八九式舰攻 8（Lt. Irikiin Yoshiaki） | **未获取** |
| 驱逐舰夕风 Yūkaze | — | — | **未获取** |
| 水上机母舰 | — | 千代田 Chiyōda、日进 Nisshin（载鱼雷艇 2、袖珍潜艇 6） | **未获取** |
| 第三水雷战队 DesRon 3 | 桥本信太郎 Rear Adm. Hashimoto Shintaro（座舰川内 Sendai） | 第十一、十九、二十驱逐队 | 川内舰长 **未获取** |

### 1.3 日方 · 北方部队（阿留申方向）

NHHC 的日方战斗序列页只列到「Aleutian Screening (Support) Force」（高须四郎：伊势、日向、扶桑、山城；第九战队轻巡北上、大井），**第二机动部队（角田觉治，龙骧、隼鹰）在该页未单列**；其存在可由利根 TROM 佐证：

> "CruDiv 8 joins BatDiv 3/1, carrier ZUIHO, seaplane carrier KAMIKAWA MARU escorted by DesDiv 4's MAIKAZE, HAGIKAZE and NOWAKI that are also detached to join Rear Admiral (later Vice Admiral) Kakuta Kakuji's (former CO of YAMASHIRO) Second Mobile Force."
> —— [S5]

| 队 | 指挥官 | 兵力 |
|---|---|---|
| 阿留申警戒（支援）部队 | 高须四郎 Vice Adm. Takasu Shiro | 第二战队：伊势、日向、扶桑、山城；第九战队（轻巡）：北上、大井（Rear Adm. Kishi Fukuhara） |
| 第二机动部队 | 角田觉治 Rear Adm. Kakuta Kakuji | 龙骧 Ryujo、隼鹰 Junyo（编成细节 **未获取**） |

> "Detachment from Main Body as Aleutian Screening (Support) Force / Vice Adm. Takasu Shiro Battleship Division 2 / Ise / Hyūga / Fuso / Yamashiro / Cruiser Division (Light) 9 / Rear Adm. Kishi Fukuhara / Kitakami / Ōi"
> —— [S20]

### 1.4 日方 · 运输船团与登陆部队（近藤信竹）

> "Midway Occupation Force / Vice Adm. Kondō Nobutake (Commander in Chief, Second Fleet) / Chief of Staff, Rear Adm. Shiraishi Kazutaka"
> "Transport Group / Approximately 5,000 troops embarked, Capt. Ota Minoru (Navy) … and Col. Ichiki Kiyonao (Army) / Rear Adm. Tanaka Raizō, Commander Destroyer Squadron 2 / in light cruiser Jintsu"
> —— [S20]

| 队 | 指挥官 | 主要舰船 |
|---|---|---|
| 掩护部队 Covering Group | 近藤信竹 Vice Adm. Kondō | 第四战队第一小队 爱宕 Atago、鸟海 Chōkai；第五战队 妙高 Myōkō、羽黑 Haguro（高木武雄）；第三战队第一小队 金刚 Kongō、比叡 Hiei（三川军一）；第四水雷战队（西村祥治，座舰由良 Yura）第三、第九驱逐队 |
| 航母部队 Carrier Group | 小林末男 Capt. Obayashi Sueo（瑞凤舰长） | 瑞凤 Zuiho（零战 6、九六舰战 6、舰攻 12）+ 驱逐舰三日月 Mikazuki |
| 近距离支援部队 Close Support Group | 栗田健男 Rear Adm. Kurita Takeo | 第七战队 铃谷 Suzuya、熊野 Kumano、最上 Mogami、三隈 Mikuma；第八驱逐队 朝潮、荒潮；油船 日荣丸 Nichiei Maru |
| 运输船团 Transport Group | 田中赖三 Rear Adm. Tanaka Raizō（座舰神通 Jintsu） | 清澄丸、庆洋丸、全洋丸、五洲丸二号、东亚丸、加纳丸、阿根廷丸、北陆丸、巴西丸、雾岛丸、东亚丸、南海丸；特设巡洋（哨戒艇）第 1、2、34 号；油船 曙丸 Akebono Maru（护卫：黑潮、亲潮、初风、雪风、天津风、时津风、霞、霰、阳炎、不知火） |
| 水上机母舰部队 | 藤田类太郎 Rear Adm. Fujita Ryūtarō | 千岁 Chitose（F1M 16、E13A1 4）、神川丸 Kamikawa Maru（F1M 8、E13A1 4）；驱逐舰 早潮 Hayashio |
| 扫雷部队 | 宫本定知 Capt. Miyamoto Sadatomo | 第 3、5 玉丸，第 7、8 昭南丸；驱潜艇 16、17、18 号；补助舰 宗谷；货物船 明洋丸、山福丸 |

### 1.5 美方 · TF 16（斯普鲁恩斯）

> "Task Force 16 (TF 16) / Rear Adm. Raymond A. Spruance, USN / Chief of Staff, Capt. Miles R. Browning, USN"
> —— [S19] https://www.history.navy.mil/research/library/online-reading-room/title-list-alphabetically/c/composition-of-us-forces.html

| 舰 | 舰长 | 航空队指挥官 / 编制 | 原句 |
|---|---|---|---|
| 企业号 USS Enterprise (CV-6) | Capt. George D. Murray | 航空团指挥官 CEAG Lt.Cdr. C. Wade McClusky；VF-6 Lt. James S. Gray Jr.（F4F-4 ×27）、VB-6 Lt. Richard H. Best（SBD ×15）、VS-6 Lt. W. Earl Gallaher（SBD-3 ×17）、VT-6 Lt.Cdr. Eugene E. Lindsey（KIA，TBD-1 ×14） | "USS Enterprise (CV-6) / Capt. George D. Murray, USN / Commander Enterprise Air Group (CEAG) - Lt. Comdr. C. Wade McClusky, USN" —— [S19] |
| 大黄蜂号 USS Hornet (CV-8) | Capt. Marc A. Mitscher | 航空团指挥官 CHAG Lt.Cdr. Stanhope C. Ring；VF-8 Lt.Cdr. Samuel G. Mitchell（F4F-4 ×27）、VB-8 Lt.Cdr. Robert R. Johnson（SBD-3 ×19）、VS-8 Lt.Cdr. Walter F. Rodee（SBD ×15）、VT-8 Lt.Cdr. John C. Waldron（KIA，TBD-1 ×15） | "USS Hornet (CV-8) / Capt. Marc A. Mitscher, USN / Commander Hornet Air Group (CHAG) - Lt. Comdr. Stanhope C. Ring, USN" —— [S19] |
| 巡洋舰群 TG 16.2 | Rear Adm. Thomas C. Kinkaid | 新奥尔良、明尼阿波利斯、文森斯、北安普敦、彭萨科拉、亚特兰大（CL-51） | "Task Group 16.2 (TG 16.2) / Cruiser Group / Rear Adm. Thomas C. Kinkaid, USN" —— [S19] |
| 驱逐舰群 TG 16.4 | Capt. Alexander R. Early（DesRon 1）/ Capt. Edward P. Sauer（DesRon 6） | 菲尔普斯、沃登、莫纳汉、艾尔文；巴尔奇、康宁汉、本汉姆、埃利特、莫里 | "Destroyer Screen / Capt. Alexander R. Early, USN" —— [S19] |

### 1.6 美方 · TF 17（弗莱彻）

| 舰 | 舰长 | 航空队指挥官 / 编制 | 原句 |
|---|---|---|---|
| 约克城号 USS Yorktown (CV-5) | Capt. Elliot Buckmaster | 航空团指挥官 CYAG Lt.Cdr. Oscar Pederson；VF-3（含 VF-42 人员）Lt.Cdr. John S. Thach（F4F-4 ×25）、VB-3 Lt.Cdr. Maxwell F. Leslie（SBD-3 ×17）、VS-5 Lt. Wallace C. Short Jr.（SBD-3 ×16）、VT-3 Lt.Cdr. Lance E. Massey（KIA，TBD-1 ×12） | "USS Yorktown (CV-5) -Capt. Elliot Buckmaster, USN" / "Commander Yorktown Air Group (CYAG) - Lt. Comdr. Oscar Pederson, USN" —— [S19] |
| 巡洋舰群 TG 17.2 | Rear Adm. William W. Smith | 阿斯托里亚、波特兰；VCS-4/VCS-6 各型 SOC/SON ×8 | "Task Group 17.2 (TG 17.2) / Cruiser Group / Rear Adm. William W. Smith, USN" —— [S19] |
| 驱逐舰群 TG 17.4 | Capt. Gilbert C. Hoover（ComDesRon 2） | 哈曼 Hammann、休斯 Hughes、莫里斯 Morris、安德森 Anderson、拉塞尔 Russell、格温 Gwin | "USS Hammann (DD-412) - torpedoed and sunk by Japanese submarine I-168 on 6 June 1942." —— [S19] |

指挥关系：

> "When TF 17 and TF 16 joined about 350 miles northeast of Midway on 2 June, Fletcher became officer in tactical command."
> —— [S18]

### 1.7 美方 · 中途岛岸基航空兵（TF 9 / 岸基航空）

> "Patrol Wings, Task Force 9 (TF 9) / Rear Adm. Patrick N. L. Bellinger, USN / Shore-Based Air, Midway / Capt. Cyril T. Simard, USN"
> —— [S19]

| 单位 | 指挥官 | 装备 | 原句 |
|---|---|---|---|
| 中途岛岸基航空总指挥 | Capt. Cyril T. Simard, USN | — | "Shore-Based Air, Midway / Capt. Cyril T. Simard, USN" —— [S19] |
| 第一巡逻航空队分遣队 PatWing 1 Det | Cdr. F. Massie Hughes | PBY-5/5A ×32（与 PatWing 2 Det 合计） | "Patrol Wing 1 Detachment (PatWing 1 Det) / Comdr. F. Massie Hughes, USN" —— [S19] |
| 第二巡逻航空队分遣队 PatWing 2 Det | Lt.Cdr. Robert C. Brixner | 同上 | "Patrol Wing 2 Detachment (PatWing 2 Det) / Lt. Comdr. Robert C. Brixner, USN / 32 Consolidated PBY-5 and PBY-5A (Catalina)" —— [S19] |
| VT-8 分遣队（TBF 队） | Lt. Langdon K. Fieberling（KIA） | TBF-1 ×6 | "Torpedo Squadron 8 Detachment (VT-8 Det) / Lt. Langdon K. Fieberling, USN (KIA) / 6 Grumman TBF-1 (Avenger)" —— [S19] |
| 海军陆战队第 22 航空大队 MAG-22 | Lt.Col. Ira L. Kimes, USMC | 见下两行 | "Marine Aircraft Group 22 (MAG 22) / Second Marine Aircraft Wing / Lt. Col. Ira L. Kimes, USMC" —— [S19] |
| VMF-221 | Maj. Floyd B. Parks（6/4 KIA），后 Capt. Kirk Armistead | F2A-3 ×20、F4F-3 ×7 | "Marine Fighting Squadron 221 (VMF-221) / Maj. Floyd B. Parks, USMC (4 June 1942) (KIA)" —— [S19] |
| VMSB-241 | Maj. Lofton R. Henderson（6/4 KIA）→ Maj. Benjamin W. Norris（KIA）→ Capt. Marshall A. Tyler | SB2U-3 ×11、SBD-2 ×16 | "Marine Scout Bombing Squadron 241 (VMSB-241) / Maj. Lofton R. Henderson, USMC (4 June 1942) (KIA)" —— [S19] |
| 陆军第七航空队分遣队 | Maj.Gen. Willis P. Hale, USAAF | B-26/B-26B ×4（Capt. William F. Collins Jr.）；B-17 ×13（Lt.Col. Walter C. Sweeney Jr.）+ ×6（Maj. George A. Blakey） | "Seventh Army Air Force Detachment / Maj. Gen. Willis P. Hale, USAAF" —— [S19] |
| 第六陆战防御营（加强） | Col. Harold D. Shannon, USMC | 高炮、岸防 | "Sixth Marine Defense Battalion (reinforced), Fleet Marine Force / Col. Harold D. Shannon, USMC" —— [S19] |
| 第一鱼雷艇中队 MTBRon 1 | Lt. Clinton McKellar Jr., USN | PT-20/21/22/24/25/26/27/28（中途岛），PT-29/30（库雷环礁） | "Motor Torpedo Boat Squadron 1 (MTBRon 1) / Lt. Clinton McKellar Jr., USN" —— [S19] |

---

## §2 逐时事件流

格式：`MM-DD HH:MM（当地）`。每条附英文原句 + URL。

### 6 月 3 日

**06-03 04:30（当地）** 中途岛全部可用飞机升空（例行搜索开始）。

> "By 0430 all planes fit for service were in the air."
> —— [S17-cn4] https://www.ibiblio.org/hyperwar/USN/USN-CN-Midway/USN-CN-Midway-4.html

**06-03 09:04（当地）** 全战役第一次水面接触：PBY 发现两艘日军货船。**机号未获取**（原报告只给方位距离，未给机号或 Bureau Number）。

> "At 0904 the first surface contact of the battle was reported by a patrol plane: 'Two Japanese cargo vessels sighted bearing 247° from Midway, distance 470 miles. Fired upon by antiaircraft.'"
> —— [S17-cn4]

**06-03 09:25（当地）** 另一架巡逻机报告「主力」六艘大船成纵队。

> "Shortly afterward, at 0925, another plane reported: 'Main body bearing 261°, distance 700 miles, six large ships in column.'"
> —— [S17-cn4]

**06-03 11:00（当地）** 同一机修正为 11 艘，航向 090、航速 19 节（后证为占领部队一部，非主力）。

> "At 1100 the same plane reported that this force consisted of 11 ships, course 090°, speed 19. Actually, as it later proved, this was not the enemy's 'main body,' but probably only a portion of his occupation force."
> —— [S17-cn4]

**06-03 12:30（当地）** 9 架 B-17E（Lt.Col. Walter C. Sweeney Jr.）自中途岛起飞。

> "This squadron, piloted by the most experienced of the B-17 pilots, was commanded by Lt. Col. Walter C. Sweeney, Jr., U.S.A. Air Corps. Taking off about 1230, our planes found the enemy at 1623 at a distance of about 570 miles."
> —— [S17-cn4]

**06-03 16:23（当地）** B-17 对运输船团投弹 36 枚 600 磅，战果存疑（见 §5 争议 3）。

> "Preliminaries to the Battle of Midway opened on the afternoon of 3 June, when at 1623, nine B-17E's led by Lt. Col. Walter C. Sweeney, Jr., of the 431st Bombardment Squadron surprised the transport force with its supporting craft some 570 miles west of Midway, dropping 36 x 600-lb. demolition bombs from 8,000 feet."
> —— [S25] https://www.history.navy.mil/research/library/online-reading-room/title-list-alphabetically/b/battle-of-midway-army-air-forces.html

**06-03 16:40（当地）** 长程 B-17 报告 261° 方向 700 英里处有 2 艘运输船与驱逐舰。

> "at 1640 reported 2 transports and destroyers, on bearing 261°, distance 700."
> —— [S17-cn4]

**06-03 21:15（当地）** 4 架 PBY-5A 各挂一条 MK XIII 鱼雷起飞，执行美军巡逻机首次夜间鱼雷攻击（Lt. William L. Richards 带队）。

> "Before the B-17's returned, a flight of four PBY-5A's, each carrying one MK XIII Mod. I torpedo took off on an historic mission, 'the first night torpedo attack by our patrol planes on surface ships.'"
> —— [S17-cn4]

**06-03 全天（当地）** 日方当日无逐时战斗记录（仅航行数据）：0030 航向 70、航速 9；1030 电令航向 125；1200 第十水雷战队开始加油；1330 航向 130；2350 雾散。

> "3 June / 0000 Course, 70; speed, 9. / 1030 Despatch from Comdr. Mobile Force to Mobile Force (radio) : 'Course, 125.' / 1200 Refuelling of DesRon 10 begun. / 1250 Fog gradually lifts. / 1330 Course, 130. Position: 37-1.5N, 171-7.0E. / 2350 Fog clears."
> —— [S21]（该件全段为 JST，各条 +3h −1d 即为当地同日同时刻附近；本条不参与 §2 的事件计数）

### 6 月 4 日 · 凌晨

**06-04 01:15（当地）** 4 架 PBY 在月夜接近运输船团，雷达先于目视发现约 10 艘船、6 艘驱逐舰。

> "At about 0115 on June 4th, radar indicated a group of about 10 ships 10 or 12 miles to the port of this group. … There were 10 or more large ones in 2 columns, escorted by 6 destroyers."
> —— [S17-cn4]

**06-04 01:30（当地）** PBY 发起鱼雷攻击（ONI 叙述：领队 800 码投雷，「以为」有爆炸；未确认战果）。

> "The planes glided down to 100 feet and the leader dropped his torpedo at 800 yards, then climbed in a turn over the target. It was thought that an explosion followed."
> —— [S17-cn4]

**06-04 01:53（当地）** **（与上条冲突）** NHHC 记 Ensign Gaylord Probst 命中油船曙丸 Akebono Maru，且为全战役美军唯一命中日舰的鱼雷。

> "At 0153 one of the PBYs, flown by Ensign Gaylord Probst, hit a Japanese tanker, Akebono Maru, the only U.S. torpedo to damage a Japanese ship in the entire battle"
> —— [S24]

**06-04 04:15（当地）** 中途岛搜索机群起飞。

> "At 0415 Search planes take off."
> —— [S17-cn5] https://www.ibiblio.org/hyperwar/USN/USN-CN-Midway/USN-CN-Midway-5.html

**06-04 04:30（当地）** 日军第一波 108 机（36 舰攻 + 36 舰爆 + 36 零战）起飞攻击中途岛，总指挥为飞龙飞行队长友永丈市海军大尉。

> "At 0430 (local times), the air strike led by Lt. (later KIA, Cdr posthumously) Tomonaga Joichi (59) is launched against Midway Island with 36 B5N2 'Kate', 36 D3A1 'Val' and 36 A6M2 'Zeke'. AKAGA contributes 18 'Val' and 9 'Zeke'."
> —— [S1]

**同一时刻的日方原始记录（原记为 JST 6 月 5 日 01:30）：**

> "At 0130 on the 5th, under command of flight officer of the Hiryu, Lieut. Tomonaga, Organization #5 composed of 36 ship-based fighters, 36 ship-based bombers, and 36 ship-based torpedo planes, took off to attack Midway."
> —— [S21]

（换算校验：0130 JST + 3h − 1d = 当地 6 月 4 日 04:30，与 [S1] 完全吻合。）

各舰出动数（分项）：

> "KAGA contributes 18 D3A1 'Val' and 9 A6M2 'Zeke'."
> —— [S2] http://www.combinedfleet.com/kaga.htm
> "SORYU contributes eighteen D3A1 'Val' armed with Type # 80 land bombs and nine A6M2 'Zekes.'"
> —— [S3] http://www.combinedfleet.com/soryu.htm

飞龙分项：**未获取**（见 §0b（6））。

**06-04 05:00（当地）**（原记为 JST 02:00）利根 4 号搜索机起飞，比预定晚约 30 分钟。

> "0200 Tone's plane takes off on #4 search line."
> —— [S21]（该件全段为 JST。0200 JST + 3h − 1d = 当地 0500）

对照 Tully 的概述（未给单机时刻，只说区间）：

> "Between 0435-0500, CruDiv 8's TONE and CHIKUMA each launch two E13A1 Jake long-range reconnaissance floatplanes to search out 300 miles for American carriers from NNE thru S."
> —— [S5]

**06-04 05:30（当地）** PBY（Lt. Howard P. Ady）发现日舰，05:34 发出报告。

> "At 0530, a PBY flown by Lieutenant Howard P. Ady sighted Japanese ships northwest of Midway and issued a sighting report at 0534."
> —— [S23]

**06-04 05:45（当地）** PBY（Lt. William Chase）报告「大量飞机飞向中途岛」——用明语，为全战役首次。

> "At 0545 'the most important contact of the battle' was made. A patrol plane reported in plain English (the first use of it in the battle): 'Many planes heading Midway, bearing 320, distance 150.'"
> —— [S17-cn5]

**06-04 05:52（当地）** 报告发现两艘航母及主力，航向 135、航速 25，方位 320、距离 180 英里。

> "At 0552 came the news which our attack forces had impatiently awaited. A PBY reported two carriers and the main body of ships, carriers in front, course 135°, speed 25, on bearing from Midway 320°, distance 180 miles."
> —— [S17-cn5]

**06-04 05:55（当地）** 中途岛空袭警报；06:00 前除一架 J2F 外全部飞机升空。

> "At 0555 the air-raid alarm was sounded, and by 0600 or shortly after, every plane able to leave the ground, except for one J2F, was in the air."
> —— [S17-cn5]

**06-04 06:16（当地）** 陆战队战斗机（VMF-221）在 12,000 英尺、距岛 30 英里处与日机群接触。

> "At 0616 the first three fighter sections encountered the enemy planes 30 miles out at 12,000 feet."
> —— [S17-cn5]

**06-04 06:30（当地）** 第一枚炸弹落于中途岛；东岛机库、沙岛油罐被毁。

> "The first bomb fell on Midway at 0630."
> —— [S17-cn5]

**06-04 07:05（当地）** 4 架 B-26（Capt. James F. Collins Jr.）与 6 架 TBF（Lt. Langdon K. Fieberling）同时发现日航母编队并进入攻击。

> "The four B-26's and the six TBF's found the enemy force simultaneously on the morning of June 4th."
> —— [S17-cn6]

**06-04 07:10（当地）** 赤城瞭望发现低空来袭的 6 架 TBF 与 4 架 B-26；2 条鱼雷被规避。

> "0710, AKAGI's lookouts spot enemy planes coming low. The aircraft are six Grumann TBFs 'Avenger' torpedo-bombers, on their first combat mission, and four twin-engined Martin B-26 'Marauder' medium bombers, the latter targeting AKAGI. Two 'Marauders' are shot down by CAP fighters and AA fire for the loss of one 'Zeke'. Two torpedoes are evaded by the carrier."
> —— [S1]

**06-04 07:15（当地）** 南云下令第二波改挂陆用炸弹（第一次换弹）。

> "0715 Nagumo orders second attack wave to arm for land strike against Midway."
> —— [S2]

**06-04 07:20（当地）** TBF 队扑向飞龙；Earnest 机重创后返航。

> "Fieberling led his strike against the Japanese carrier Hiryu, flagship of Rear Admiral Tamon Yamaguchi, commander of Carrier Division Two"
> —— [S24]

**06-04 07:28（当地）** 利根 4 号机发现敌舰——观察员**未立即识别出航母**，日后被视为关键失误。

> "At 0728, TONE's E13A1 No. 4 discovers the enemy ships, which later materialize as a carrier group. The observer does not identify the carriers at the outset, which proves to be a crucial mistake."
> —— [S5]

**06-04 07:40（当地）** 该报告送达南云（另一说为 07:40 报告、07:45 处置，见 §5 争议 2）。

> "At 0740, the No. 4 scout floatplane from the Japanese cruiser Tone, flown by Petty Officer First Class Hiroshi Amari, reported sighting ten U.S. surface ships northeast of Midway."
> —— [S24]

**06-04 07:45（当地）** 南云下令停止换装陆用炸弹，改回鱼雷（第二次换弹）。

> "0745 Nagumo directs that the preparations for the second wave to attack Midway be halted, and land-bombs switched to torpedoes (in the case of AKAGI and KAGA) for ship attack."
> —— [S2]

**06-04 07:55（当地）** VMSB-241 的 16 架 SBD-2（Maj. Lofton R. Henderson）开始滑翔轰炸。

> "At 0755 VMSB-241 began its attack. This squadron was divided into two attack groups: one commanded by Maj. Lofton R. Henderson, with 18 SBD-2 planes"
> —— [S17-cn6]

**06-04 07:55–08:15（当地）** B-17 高空轰炸机动部队，无命中。

> "0755-0815 In this time frame B-17s are bombing the carrier force (no hits)."
> —— [S2]

**06-04 08:10（当地）** B-17 群（15 架，Sweeney）找到航母并分三队攻击。

> "The enemy force was located at 0732, but the carriers, circling under a cloud formation, were not found till 0810."
> —— [S17-cn6]

**06-04 08:20（当地）** VMSB-241 的 11 架 SB2U-3（Maj. Benjamin W. Norris）转向攻击战列舰（实为榛名）。

> "At 0820 VMSB-241's six Douglas SBD-2 'Dauntless' dive-bombers and six Vought-Sikorsky SB2U-3 'Vindicators' from Midway, led by Captain Marshall A. Tyler, attack MIKUMA and MOGAMI"（此处为 6 月 5 日条目，另行引用）
> —— [S7]
> "At 0820 the second unit of the Marine group arrived, the 11 SB2U-3's under the command of Major Norris. These sighted the enemy at 0820"
> —— [S17-cn6]

**06-04 08:20（当地）** 利根 4 号机报告「敌似有航母随行」，南云处境逆转。

> "Tone No. 4 scout plane reported sighting a carrier at 0820. Nagumo and his staff immediately grasped the grave implications of this, and he promptly ordered that the re-arming of the torpedo bombers in his reserve strike be halted, and those that had already been re-armed with bombs, be re-armed with torpedoes."
> —— [S24]

**06-04 08:30（当地）** 苍龙起飞 1 架 D4Y1「彗星」接替利根 4 号机保持接触。

> "0830 Reconnaissance D4Y-1 ('Judy') took off under orders to relieve TONE-4 search plane and maintain contact with the enemy carrier group sighted."
> —— [S3]

**06-04 08:37–08:50（当地）** 第一波开始回收，08:50 加贺机全部收容完毕。

> "0837 Midway strike recovery begins. / 0850 All KAGA first wave aicraft recovered."
> —— [S2]

**06-04 09:05（当地）** 南云下令回收完毕后北转，寻求歼灭敌舰队。

> "0905 Nagumo orders force to head north to destroy enemy force after completion of recovery operations."
> —— [S2]

**06-04 09:20（当地）** 大黄蜂号 VT-8（15 架 TBD，Lt.Cdr. John C. Waldron）单机种突入，全队覆没，仅 Ensign George H. Gay 生还。

> "When this attack was made, at about 0920, there were four carriers in the group."
> "Of the 15 planes, not one returned from the attack. Only one pilot, Ensign George H. Gay, survived."
> —— [S17-cn7] https://www.ibiblio.org/hyperwar/USN/USN-CN-Midway/USN-CN-Midway-7.html

**06-04 09:38（当地）** 加贺瞭望发现第二波鱼雷机（企业号 VT-6，Lt.Cdr. Eugene E. Lindsey），直接以加贺为目标。

> "0938 Second enemy torpedo plane group sighted approaching from the south. (This is USS ENTERPRISE (CV-6) Torpedo Squadron VT-6's Douglas TBD 'Devastators' led by LtCdr (KIA, Navy Cross posthumously awarded ) Eugene E. Lindsey (USNA '27) which directly targeted KAGA."
> —— [S2]

**06-04 10:00（当地）** 加贺记录 VT-6 攻击被击退，舰队转向 030 度接近敌航母。

> "1000 Launched six fighters to engage torpedo planes. Attack repulsed. Fleet course set to 030 degrees to close and attack enemy carrier to the northeast."
> —— [S2]

**06-04 10:06（当地）** 赤城发现约克城 VT-3（15 架，方位 48° 右舷，距离 45,000 米）。

> "1006 AKAGI sights 15 enemy planes bearing 48 degrees starboard (118 degrees), distance 45,000 meters.{This is Yorktown's VT-3}"
> —— [S1]

**06-04 10:20（当地）** 南云下令待命即发（CAP 优先升空）；此时美机已临空。

> "1020 Cardiv 1 ordered to launch CAP fighters as soon as ready."
> —— [S2]

**06-04 10:22（当地，原记为 JST 07:22）** 加贺被企业号 VS-6 / VB-6（麦克拉斯基）俯冲命中，至少 1 枚 1,000 磅 + 3 枚 500 磅；舰桥被毁，冈田舰长阵亡。

> "1022 (0722 JST) As fighters prepare to launch, approximately 30 enemy dive-bombers overhead reported by HIRYU and also sighted by lookouts about to attack. KAGA takes evasive action to starboard, avoiding first three bombs but is struck by a minimum of one 1,000-pound (450-kg) and three 500-pound (230-kg) bombs from USS ENTERPRISE (CV-6)'s Douglas SBD 'Dauntless' VS-6 and VB-6 led by LtCdr (later Rear Admiral) Wade McClusky (USNA '26)"
> —— [S2]

**06-04 10:25–10:28（当地）** 苍龙被约克城 VB-3 命中三弹（前升降机、第二升降机之后、中部烟囱侧）；动力全失。

> "1025-1026 While continuing launch preparations against a sighted enemy carrier, attacked by thirteen enemy dive bombers. Two direct bomb hits are sustained, one on the forward elevator, the other aft the second elevator, setting off furious fires and induced explosions among the armed and fueled aircraft."
> "1029 A 1,000 pound bomb hit amidships abreast the stacks, the bomb or its blast effects apparently penetrating to explode on the lower hangar deck … SORYU's engines abruptly ceased and she lost all propulsion on both sides."
> —— [S3]

**06-04 10:26（当地，原记为 JST 07:26）** 赤城被企业号 VB-6（Lt.Cdr. Richard H. Best）3 机攻击；1 弹命中舰岛附近中部，引爆机库内满油满弹的舰攻。

> "1026, AKAGI is attacked from 80 degrees port by three VB-6's Douglas SBD-3 'Dauntless' dive-bombers led by LtCdr Richard H. Best (USNA '32) from U.S.S. ENTERPRISE (CV-6). One direct hit is scored amidships in the vicinity of the island, starting a fire in both hangar levels"
> —— [S1]

**06-04 10:29（当地）** 赤城机库内鱼雷开始诱爆；前部弹药库注水成功、后部因阀门损坏失败。

> "1029 Fire in hangar deck started exploding torpedoes stored for ready loading to attack planes. Forward and aft magazines ordered flooded; but at first, only the forward ones can be due to damaged valves aft."
> —— [S1]

**06-04 10:42（当地）** 赤城舵机卡死在 20 度，无法保持旗舰职能；南云决定转移旗舰。

> "1042 Attempting to return to course AKAGI rudder stayed locked in 20 degree turn and malfunctions. With the carrier left circling helplessly, fire engulfing the bridge, and communications failing, she cannot remain KdB flagship. Nagumo orders the carrier stopped to transfer the flag."
> —— [S1]

**06-04 10:45（当地）** 苍龙舰长柳本柳作下令非必要人员弃舰，本人拒离舰桥。

> "1045 Captain Yanagimoto ordered all non-essential personnel to Abandon Ship, especially the aviators. He refused entreaties to leave the bridge, and remained at the signal tower on the island's starboard side as flames surrounded it."
> —— [S3]

**06-04 10:54（当地）** 飞龙第一波反击起飞：18 架舰爆 + 6 架零战（小林道雄大队）。

> "At 1054, she launches 18 D3A1 'Val' dive-bombers and six A6M2 'Zeke' fighters that follow the American planes and find their carriers."
> —— [S13] http://www.combinedfleet.com/I-168.htm

日方原始报告作「0758」起飞（JST → 当地 1058），与 1054 有 4 分钟差：

> "At 0758, Hiryu's attack unit (6 fighters and 18 bombers) took off and carried out the attack."
> —— [S21]

**06-04 11:20（当地）** 赤城舰长青木及舰桥军官移至前部飞行甲板；火从升降机喷出。

> "1120 Captain Aoki and bridge officers relocate to forward flight deck. Fire is pouring out of the amidships elevator and surrounding the bridge."
> —— [S1]

**06-04 11:27（当地）** 机动部队旗移至轻巡长良。

> "1127 After transfer via NOWAKI's boat, KdB's flag is raised on light cruiser NAGARA which then immediately departs northeastward to rejoin the fleet."
> —— [S1]

**06-04 11:30（当地）** 山口多闻令第八战队各派驱逐舰一艘给三艘受损航母，并令其向主力方向后退（11:47 重复）。

> "1130: Comcardiv 2 (Rear Admiral Yamaguchi Tamon on HIRYU) orders ComCrudiv 8 (Rear Admiral Abe Hiroaki) to assign one destroyer each to the three damaged carriers, and have the damaged carriers retire toward Yamamoto's Main Body. The order is repeated at 1147."
> —— [S2]

**06-04 11:30（当地）** 约克城放出 10 架 SBD 搜索第四艘航母。

> "At 1130 the Yorktown sent out 10 scout bombers, each with one 1,000-pound bomb, to search between 280° and 20° to a distance of 200 miles for the fourth Japanese carrier."
> —— [S17-cn8] https://www.ibiblio.org/hyperwar/USN/USN-CN-Midway/USN-CN-Midway-8.html

**06-04 11:59（当地）** 约克城雷达在 250°、46 英里发现大批来袭机（30–40 架）。

> "when at 1159 radar picked up a large number of planes, estimated at 30 or 40, on bearing 250° at a distance of 46 miles."
> —— [S17-cn8]

**06-04 12:08（当地）** 飞龙第一波俯冲约克城，命中 3 弹（后升降机后、右舷烟道、一号升降机）。

> "1208 Dive bombers attack Yorktown." / "Three hits had been made."
> —— [S17-cn8]

**06-04 12:15（当地）** 攻击结束；来袭 18 架舰爆无一返航。

> "It was all over by 1215. Not one of the bombers escaped."
> —— [S17-cn8]

**06-04 12:45（当地）** 飞龙第二波起飞：10 架舰攻（友永丈市）+ 6 架零战。

> "At 1245, HIRYU launches a second strike of 10 'Kate' torpedo planes and six fighters."
> —— [S13]

（日方原始报告作「1020」起飞，即当地 1320，与 1245 冲突，见 §5 争议 4。）

**06-04 13:50（当地）** 赤城再次完全停车，开始漂流灭火。

> "1350 AKAGI fully halted again. Hereafter is drifting while attempting to fight the raging fires."
> —— [S1]

**06-04 14:10（当地，原记为 JST 11:10）** 加贺遭 USS Nautilus (SS-168) 鱼雷攻击，命中右舷后部但**未爆炸**。

> "1410: (1110 JST) KAGA is attacked by LtCdr (later Rear Admiral, retired) William H. Brockman's (USNA '27) submarine USS NAUTILUS (SS-168). One torpedo hits the starboard quarter, but fails to explode."
> —— [S2]

**06-04 14:27（当地）** 彭萨科拉号雷达（接替约克城雷达警戒）在 340°、33 英里发现第二批来袭机。

> "at 1427 the Pensacola, which had assumed radar guard after the Yorktown was damaged, picked up enemy planes bearing 340°, distance 33 miles."
> —— [S17-cn8]

**06-04 14:30（当地）** 约克城搜索机（Lt. Samuel Adams）报告飞龙位置：31°15'N, 179°05'W。

> "At about 1430, almost at the moment that the Yorktown was undergoing the torpedo attack, Lt. Samuel Adams, reported an enemy force of 1 aircraft carrier, 2 battleships, 3 heavy cruisers and 4 destroyers, course north, speed 20 knots, position, latitude 31°15' N., longitude 179°05' W."
> —— [S17-cn9] https://www.ibiblio.org/hyperwar/USN/USN-CN-Midway/USN-CN-Midway-9.html

**06-04 14:41（当地）** 日机进入约克城左舷 12,000 码，防空火网全开。

> "They had already started their glide when our vessels to port of the Yorktown opened fire at 1441 at a range of 12,000 yards."
> —— [S17-cn8]

**06-04 14:45（当地）** 两条鱼雷命中约克城左舷中部，相隔约 30 秒。

> "Two others, however, could not be avoided, and they caught her admidships on the port side. The two explosions at 1445 were about 30 seconds apart."
> —— [S17-cn8]

**06-04 14:55（当地）** 约克城弃舰。

> "at 1455 orders were given to abandon ship."
> —— [S17-cn8]

**06-04 15:30（当地）** 企业号起飞 24 架 SBD（其中 14 架来自约克城）。

> "At 1530 the Enterprise began launching an attack group of 24 scout bombers, 14 of which were from the Yorktown."
> —— [S17-cn9]

**06-04 16:03（当地）** 大黄蜂号起飞 16 架 SBD。

> "The Hornet at 1603 began launching a squadron of 16 scout bombers."
> —— [S17-cn9]

**06-04 16:40（当地）** 加贺判断无望，残余人员全部弃舰，由萩风、舞风收容。

> "1640 The situation judged hopeless, all remaining personnel are ordered (apparently by the First Damage Control Officer) to abandon ship. They are removed or subsequently rescued from the sea by destroyers HAGIKAZE and MAIKAZE."
> —— [S2]

**06-04 17:03（当地，原记为 JST 14:03）** 飞龙被 13 架企业号 SBD 俯冲命中 4 弹（前部甲板连续 3 弹 + 舰桥旁 1 弹），前升降机被掀翻贴住舰岛。

> "At 1703 while preparing to launch strike against enemy carrier, attacked by thirteen enemy dive bombers. Four direct bomb hits received, all closely spaced."
> —— [S4] http://www.combinedfleet.com/hiryu.htm
> "At 1403, at the very moment when a type 13 experimental ship-based bomber was about to take off, the Hiryu was subjected to dive bombing attacks from 13 enemy ship-based bombers."（JST）
> —— [S21]

**06-04 17:15（当地）** 加贺残员全部离舰（萩风报告南云）。

> "1715: HAGIKAZE reports to Nagumo that all remaining personnel on KAGA having earlier been ordered to abandon ship, have now been taken aboard the two destroyers."
> —— [S2]

**06-04 17:30（当地）** 大黄蜂号机群抵达，飞龙已烈焰冲天，转向攻击战列舰与巡洋舰。

> "By this time the carrier was burning so fiercely that it was no longer a useful target, and the attack was diverted to a battleship and a cruiser. Three hits, two of which were by 1,000-pound bombs, were scored on the former, and two 500-pound bomb hits on the cruiser."
> —— [S17-cn9]

**06-04 17:50（当地）** 南云向山本报告加贺失去战斗力、全员已转移。

> "1750 Nagumo reports to Yamamoto: 'KAGA is inoperational in (grid) position HE E A55. All survivors have been transferred to destroyers.'"
> —— [S2]

**06-04 18:56（当地）** 日落；此后加贺、苍龙接获自沉命令。

> "1856: Sunset. Shortly after this time, KAGA and SORYU are apparently ordered scuttled. A final caretaker crew is removed from KAGA by a written order."
> —— [S2]

**06-04 19:12（当地，原记为 JST 16:12）** 苍龙由矶风发射 3 条鱼雷自沉，3 分钟后翻覆下沉，713 人阵亡（含柳本舰长）。

> "Sunk: 1912 (1612 JST) Destroyer ISOKAZE fired three torpedoes at SORYU (at least two hit probably all three), and the carrier began to sink by the stern and three minutes later upended. Bow raised high, she plunged to the bottom taking down 713 officers and men including Captain Yanagimoto Ryusaku"
> —— [S3]

（日方原始报告记沉没为 JST 1613／爆炸 1620，即当地 1913／1920，见 §5 争议 6。）

**06-04 19:20（当地）** 赤城舰长青木决定弃舰，并电请以驱逐舰鱼雷处分。

> "1920 Five minutes after learning from the Chief Engineer that there is no hope for AKAGI operating on her own power, Captain Aoki decided to Abandon Ship. / 1925 All hands ordered to assemble and prepare to abandon ship. Captain Aoki radioed Nagumo this and requested permission to have AKAGI scuttled by destroyer torpedo."
> —— [S1]

**06-04 19:25（当地，原记为 JST 16:25）** 加贺由萩风发射 2 条鱼雷自沉，舰尾先沉，位置约 30-23.3'N, 179-17.2'W，814 人阵亡。

> "Sunk: 1925 (1625 JST) destroyer HAGIKAZE fires two torpedoes into her starboard side amidships aft. The KAGA begins to settle by the stern, yet remains on an even keel until she slides from sight in approximate position 30-23.3'N, 179-17.2' W. (See Notes). She suffers a loss of 814 officers, petty officers, and men."
> —— [S2]

**06-04 21:00（当地）** 赤城非必要人员离舰（岚 500 人、野分 200 人），青木自缚于锚甲板。

> "2100 All non-essential personnel have left the ship with 500 aboard ARASHI and 200 aboard NOWAKI. Captain Aoki and a small damage control party remain aboard. Captain Aoki had himself bound to the anchor deck to share the fate of his ship."
> —— [S1]

**06-04 21:23（当地）** 飞龙停车，风云、卷云留驻警戒。

> "At 2123 goes dead in the water, and KAZAGUMO and MAKIGUMO detached to stand by."
> —— [S4]

**06-04 21:25（当地）** 山本直接下令推迟赤城自沉；青木被劝离舰，转至岚。

> "2125 A direct order from CinC Yamamoto to postpone scuttling is received. Because of the changed circumstance, Commanding Officer is persuaded to leave the carrier, and transfers with Executive Officer to ARASHI."
> —— [S1]

### 6 月 5 日

**06-05 01:58（当地）** 飞龙发生大诱爆，希望断绝，下达弃舰令；山口多闻与加来舰长留舰。

> "At 0158 a major induced explosion occurs, and hope is lost. Abandon ship is ordered, and ComCarDiv 2 Yamaguchi gives a farewell speech, and remains aboard with Captain Kaku Tomeo."
> —— [S4]

**06-05 02:15（当地）** USS Tambor (SS-198) 在中途岛以西 90 英里发现多艘不明舰船（实为栗田的第七战队）。

> "0215 Submarine Tambor sights ships 90 miles west of Midway."
> —— [S17-cn11] https://www.ibiblio.org/hyperwar/USN/USN-CN-Midway/USN-CN-Midway-11.html

**06-05 02:55（当地，原记为 JST 5 日 23:55）** 联合舰队下令取消中途岛占领（DesOpOrd #161）。

> "2355 Radio from CinC Combined Fleet to all CinC's and ComDiv's in Combined Fleet, Chief of NavGenStaff: '… 1. Occupation of AF (Midway) is cancelled.'"
> —— [S21]（该件全段为 JST：5 日 2355 − 3h + 1d → 当地 5 日 0255）

**06-05 04:50（当地）** 山本直接下令处分赤城。

> "0450 AKAGI directed to be scuttled by direct order of CinC-Combined Fleet, Admiral Yamamoto Isoroku."
> —— [S1]

**06-05 05:10（当地，原记为 JST 6 日 02:10）** 飞龙由卷云发射 1 条鱼雷自沉（31-38'N, 178-51'W）；卷云未确认沉没即撤离。

> "at 0510 scuttled by MAKIGUMO with one torpedo in the starboard side opposite the bridge. (Scuttling position 31-38'N, 178-51'W). The MAKIGUMO then withdraws without confirming the sinking."
> —— [S4]

**06-05 05:20（当地）** 赤城由岚、萩风、舞风、野分各射 1 条鱼雷（命中 2–3 条），舰尾先沉于 30-30'N, 178-40'W；生还逾 1,070 人，阵亡 263 人。

> "0520 AKAGI lay over to starboard and sank tail first after two or three torpedo hits out of four fired into her starboard side - one each - by ARASHI, HAGIKAZE, MAIKAZE and NOWAKI in listed position 30-30'North, 178-40'West. More than 1,070 survivors are rescued, including her skipper, (Captain Aoki Taijiro) … while only 263 petty officers and men are lost."
> —— [S1]

**06-05 06:00（当地）** Tambor 报告两艘最上型重巡（实际为最上、三隈）方位 272°、距中途岛 115 英里、航向 270°。

> "0600 Tambor reports (to Midway and Honolulu) 2 Mogami type cruisers bearing 272°, 115 miles from Midway, course 270°."
> —— [S17-cn11]

**06-05 06:30（当地）** 凤翔号一架飞机发现并拍摄仍漂浮的飞龙，甲板上尚可见幸存者。

> "at 0630 a plane from HOSHO finds and photographs HIRYU still afloat and with survivors clearly seen still aboard."
> —— [S4]

**06-05 08:05（当地）** 中途岛 VMSB-241 的 6 架 SBD-2（Capt. Marshall A. Tyler）与 6 架 SB2U-3（Capt. Richard E. Fleming）攻击三隈、最上；Fleming 机被 25mm 炮火击中，投弹后坠海（追授荣誉勋章）。

> "At 0805, VMSB-241's six Douglas SBD-2 'Dauntless' dive-bombers and six Vought-Sikorsky SB2U-3 'Vindicators' from Midway, led by Captain Marshall A. Tyler, attack MIKUMA and MOGAMI, but they only score several near misses. Captain Richard E. Fleming's 'Vindicators' target MIKUMA … Fleming drops his bomb and crashes into the sea."
> —— [S7]

**06-05 08:30（当地）** B-17（8 架，Lt.Col. Brooke E. Allen）高空轰炸两艘重巡，无命中。

> "At 0834, MIKUMA and MOGAMI are bombed from high altitude by eight Boeing B-17 'Flying Fortress' from Midway, led by LtCol Brooke E. Allen, but they score no hits."
> —— [S7]

**06-05 09:12（当地）** 飞龙最终倾覆沉没，位于中途岛西北 240–260 英里；70 名滞留者中 35 人后被美军救起（含轮机长）。

> "before she arrives, the carrier at 0912 upended and sank by the bow in a position between 240 - 260 miles NW from Midway. Of the 70 men marooned aboard, only thirty-five are eventually rescued by the U.S. Navy, including her Chief Engineer."
> —— [S4]

**06-05 13:08（当地）** 扫雷舰 Vireo 拖带约克城，航速约 3 节。

> "By 1308 she had the carrier in tow and headed for Pearl Harbor at about 3 knots."
> —— [S17-cn13] https://www.ibiblio.org/hyperwar/USN/USN-CN-Midway/USN-CN-Midway-13.html

**06-05 18:15 / 18:25（当地）** 中途岛 B-17 第 92、93 飞行队分别攻击巡洋舰，均仅近失。

> "On the return contact was made at 1815 with a large cruiser on a northerly course." / "Their only contact was a cruiser which they found bearing 325° about 425 miles from Midway and which they attacked at 1825."
> —— [S17-cn11]

### 6 月 6 日

**06-06 04:15（当地）** 哈曼号把救援队送上约克城（Buckmaster 上校 + 29 名军官 + 130 名士兵）。

> "About 0415, as soon as there was sufficient light, the Hammann went alongside and transferred to the carrier a salvage party consisting of Captain Buckmaster, 29 officers and 130 men."
> —— [S17-cn13]

**06-06 05:02（当地）** 企业号起飞 18 架 SBD 向西搜索 200 英里。

> "At 0502 the Enterprise launched a search group of 18 scout-bombers, each carrying one 500-pound bomb."
> —— [S17-cn12] https://www.ibiblio.org/hyperwar/USN/USN-CN-Midway/USN-CN-Midway-12.html

**06-06 06:45（当地）** 搜索机发现一支日军编队（29°33'N, 174°30'E），报为 1 战列舰 + 5 驱逐舰，因口误被当成含航母。

> "At 0645 one of these planes found an enemy force on course 270°, position latitude 29°33' north, longitude 174°30' east."
> —— [S17-cn12]

**06-06 09:50（当地）** 大黄蜂号 26 架 SBD 攻击（目标实为最上、三隈、朝潮、荒潮）。

> "Our planes attacked at 0950." / "This Hornet attack was followed by one from the Enterprise."
> —— [S17-cn12]

**06-06 11:50–13:00（当地）** 企业号 31 架 SBD 攻击三隈，5 发直接命中（首弹命中三号主炮塔顶，崎山舰长重伤）。

> "After 1245 MIKUMA and MOGAMI are attacked by 31 SBD-3 dive-bombers from USS ENTERPRISE (CV-6). MIKUMA receives five direct hits and two near misses. The first bomb strikes the roof of No. 3 main gun turret. Captain Sakiyama, stationed in the air defense station, is severely injured by its blast."
> —— [S7]

**06-06 13:31–13:32（当地）** 伊-168（Lt.Cdr. 田边弥八）在 1,900 码距离齐射 4 条鱼雷：1 条命中哈曼号（约 4 分钟沉没，241 名船员中 81 人阵亡），2 条命中约克城右舷舰桥下方，第 4 条从舰尾掠过。

> "At 1331, from 1,900 yards, he fires two torpedoes at the overlapping formation, followed by two more three seconds later. The first torpedo hits HAMMANN, breaks her back and sinks her in about four minutes. As she goes down, her depth charges explode and kill 81 of her 241-strong crew. At 1332, the next two torpedoes strike YORKTOWN starboard below the bridge. The fourth torpedo misses and passes astern."
> —— [S13]

**06-06 13:35（当地）** 约克城瞭望发现 4 条鱼雷航迹。

> "At 1335 four torpedo wakes were sighted to starboard of the Yorktown."
> —— [S17-cn13]

**06-06 13:39（当地）** 哈曼号沉没。

> "1339 Hammann sinks."
> —— [S17-cn13]

**06-06 14:45（当地）** 大黄蜂号第二波 24 架 SBD 攻击最上（被误报为「战列舰＋巡洋舰」编队）。

> "This group of 24 scout bombers armed with 1,000-pound bombs took off at 1330 … At 1645 this group found and attacked an enemy force"
> —— [S17-cn12]

**06-06 19:30（当地）** 三隈向左倾覆沉没于 29-28'N, 173-11'E，约 700 人阵亡。

> "Around 1930 MIKUMA turns on her port side and sinks at 29-28N, 173-11E. A total of 700 crewmen are killed."
> —— [S7]

### 6 月 7 日

**06-07 04:58（当地）** 约克城向左翻转沉没，水深约 3,000 浔。

> "At 0458, the 19,875-ton YORKTOWN rolls over to port and sinks in about 3,000 fathoms of water."
> —— [S13]

对照 ONI 叙述的 05:01（见 §5 争议 7）：

> "At 0501 'she turned over on her port side and sank in about 3,000 fathoms of water with all her battle flags flying.'"
> —— [S17-cn13]

---

## §3 命中记录（逐发尽可能单列）

> 说明：凡来源只写「数发命中」而未分弹的部位/时刻者，按来源原文照录并标 `部分未获取`；**不拆分、不补齐**。

### 3.1 日军航母被弹

| # | 时刻（当地） | 受弹舰 | 命中部位 | 投弹单位 | 原句 | 来源 |
|---|---|---|---|---|---|---|
| J1 | 06-04 10:22 | 加贺 | 第 1 弹：右舷后部（原记 bomb #4） | 企业号 VS-6 / VB-6（McClusky） | "but #4 hit starboard, aft" | [S21] |
| J2 | 06-04 10:22 | 加贺 | 第 2 弹：前升降机附近（原记 bomb #7） | 同上 | "while #7 was a direct hit in the vicinity of the forward elevator" | [S21] |
| J3 | 06-04 10:22 | 加贺 | 第 3 弹：前升降机附近（bomb #8），舰桥全毁、冈田舰长阵亡 | 同上 | "Bomb #8 hit in the vicinity of the forward elevator. Practically nothing of the bridge remained after this hit." | [S21] |
| J4 | 06-04 10:22 | 加贺 | 第 4 弹：中部（bomb #9） | 同上 | "Bomb #9 also hit amidship." | [S21] |
| J5 | 06-04 10:25 | 苍龙 | 前升降机 | 约克城 VB-3（Leslie），13 机 | "one on the forward elevator" | [S3] |
| J6 | 06-04 10:26 | 苍龙 | 第二升降机之后 | 同上 | "the other aft the second elevator" | [S3] |
| J7 | 06-04 10:28（日方记 0728 JST） | 苍龙 | **未获取**（原文只记第三发） | 同上 | "Three hits were scored on her at 0725, 0726, and 0728." | [S21] |
| J8 | 06-04 10:29 | 苍龙 | 中部烟囱侧（1,000 磅），穿透至下机库爆炸，蒸汽管路断裂 | 同上 | "1029 A 1,000 pound bomb hit amidships abreast the stacks" | [S3] |
| J9 | 06-04 10:26 | 赤城 | 舰岛附近中部（1,000 磅），引爆机库内舰攻 | 企业号 VB-6（Best）3 机 | "One direct hit is scored amidships in the vicinity of the island" | [S1] |
| J10 | 06-04 10:26 | 赤城 | 舰尾舷侧（穿过护栏在左后舷外爆炸）——**Parshall & Tully 主张未在甲板起爆，故苍城实际只受一弹致命伤** | 同上 | "a second bomb slices through the net-guards of the fantail and explodes under the port quarter" | [S1] |
| J11 | 06-04 10:26 | 赤城 | 左舷中前部近失 | 同上 | "while the third is a near-miss port-side amidships-forward" | [S1] |
| J12 | 06-04 17:03 | 飞龙 | 前部飞行甲板连续 3 弹（首弹气浪把前升降机掀向舰岛） | 企业号 13 架 SBD | "The first three landed in a row on the fore part of the flight deck, the blast of the nearest flinging the forward elevator bodily against the island." | [S4] |
| J13 | 06-04 17:03 | 飞龙 | 第 4 弹：舰桥旁中部 | 同上 | "The fourth bomb struck amidships beside the bridge." | [S4] |
| J14 | 06-04 17:03 | 飞龙 | 追加命中数——**分歧**：对马（Hiryu 船员）供称 6 发 | — | "The HIRYU was hit six times during the fourth attack by dive bombers. One on forward elevator. Two just forward aft elevator." | [S22] |

加贺命中弹量另有「4 发（1×1,000 磅 + 3×500 磅）」与「4 发命中」两种说法，均指向 4：

> "Q. How many bombs hit the Kaga? / A. There were four hits on the Kaga. The first bomb hit the forward elevator…"
> —— [S22] https://www.history.navy.mil/research/library/online-reading-room/title-list-alphabetically/b/battle-of-midway-interrogation-of-japanese-officials.html

### 3.2 约克城被弹

| # | 时刻（当地） | 命中部位 | 投弹单位 | 原句 | 来源 |
|---|---|---|---|---|---|
| Y1 | 06-04 12:08 | 二号升降机之后的飞行甲板（炸弹翻滚落甲板） | 飞龙第一波 18 架 D3A1（小林道雄） | "its bomb tumbled on the Yorktown's deck just abaft the number two elevator" | [S17-cn8] |
| Y2 | 06-04 12:08 | 右舷，穿透烟道（uptakes）在第三甲板上方爆炸——**这一弹使全舰失去速度** | 同上 | "the third hit the deck on the starboard side and penetrated the uptakes, where it exploded" | [S17-cn8] |
| Y3 | 06-04 12:08 | 一号升降机（在第四甲板上方爆炸，起火） | 同上 | "hit the number one elevator and exploded above the fourth deck, starting a fire" | [S17-cn8] |
| Y4 | 06-04 14:45 | 左舷中部，鱼雷（第 1 条） | 飞龙第二波 10 架 B5N2（友永丈市） | "they caught her admidships on the port side. The two explosions at 1445 were about 30 seconds apart." | [S17-cn8] |
| Y5 | 06-04 14:45 | 左舷中部，鱼雷（第 2 条，与上条相隔约 30 秒） | 同上 | 同上 | [S17-cn8] |
| Y6 | 06-06 13:32 | 右舷舰桥下方（鱼雷 2 条） | 伊-168（Lt.Cdr. Tanabe） | "At 1332, the next two torpedoes strike YORKTOWN starboard below the bridge." | [S13] |

### 3.3 日军其他舰艇

| # | 时刻（当地） | 受弹舰 | 命中部位 / 弹种 | 投弹单位 | 原句 | 来源 |
|---|---|---|---|---|---|---|
| O1 | 06-04 01:53 | 曙丸 Akebono Maru（油船） | 鱼雷 1 条 | 中途岛 PBY-5A（Ensign Gaylord Propst） | "hit a Japanese tanker, Akebono Maru, the only U.S. torpedo to damage a Japanese ship in the entire battle" | [S24] |
| O2 | 06-04 14:10 | 加贺 | 鱼雷 1 条命中右舷后部——**未爆炸** | USS Nautilus (SS-168) | "One torpedo hits the starboard quarter, but fails to explode." | [S2] |
| O3 | 06-06 09:50 前后 | 最上 | 五号主炮塔直击（炮塔全员 18 人阵亡）；弹射甲板一弹（毁水侦 3 架） | 大黄蜂 VS-8（26 架 SBD） | "VS-8's 'Dauntlesses' score a direct hit on MOGAMI's No. 5 main gun turret; its entire crew of 18 is killed. Another bomb hit to catapult deck destroys three floatplanes" | [S8] |
| O4 | 06-06 12:45 后 | 三隈 | 5 发直击 + 2 近失（首弹中三号主炮塔顶） | 企业号 31 架 SBD | "MIKUMA receives five direct hits and two near misses." | [S7] |
| O5 | 06-06 12:45 后 | 最上 | 2 发（弹射甲板、舰桥前方） | 企业号 | "MOGAMI receives two bomb hits (to catapult deck and just forward of the bridge), causing medium damage." | [S8] |
| O6 | 06-06 约 15:00 | 最上 | 1 发 1,000 磅命中弹射甲板（起火；医护室人员几乎全伤；四号炮塔仅 2 人无伤） | 大黄蜂 23 架 SBD | "MOGAMI receives a 1000-lb bomb hit to her catapult deck, which starts a serious fire." | [S8] |
| O7 | 06-06 约 15:00 | 荒潮 | 直击 1 发（致三隈幸存者伤亡） | 大黄蜂 | "Several of MIKUMA's survivors are killed aboard ARASHIO when the latter receives a direct hit." | [S7] |
| O8 | 06-04 上午 | 榛名 | 舰尾板近失轻伤——**归因分歧**：陆战队 SB2U 声称 2 发直击；日方幸存者坚称是俯冲轰炸机所为 | VMSB-241（Norris） | "During the engagement on the 4th, the battleship Haruna received some slight damage to her stern plates from a near miss and it is possible that this damage might have come from heavy bombers, but the survivors of that ship are positive that dive bombers hurt them." | [S25] |

### 3.4 美舰被弹

| # | 时刻（当地） | 受弹舰 | 命中部位 | 投弹单位 | 原句 | 来源 |
|---|---|---|---|---|---|---|
| U1 | 06-04 12:08 | 约克城 | 见 3.2（Y1–Y3，共 3 弹） | 飞龙第一波 | "Three hits had been made." | [S17-cn8] |
| U2 | 06-04 14:45 | 约克城 | 见 3.2（Y4–Y5，鱼雷 2 条） | 飞龙第二波 | "The two explosions at 1445 were about 30 seconds apart." | [S17-cn8] |
| U3 | 06-06 13:31 | 哈曼 | 二号锅炉舱（鱼雷 1 条，龙骨断裂） | 伊-168 | "The second torpedo struck the Hammann in No. 2 fireroom. This torpedo apparently broke the ship's back" | [S17-cn13] |
| U4 | 06-06 13:32 | 约克城 | 右舷舰桥下方（鱼雷 2 条） | 伊-168 | 见 3.2 / Y6 | [S13] |

---

## §4 损失对照

### 4.1 日军

**舰船（4 航母 + 1 重巡）**

| 舰 | 处分方式 | 时刻（当地） | 执行舰 | 阵亡（各源口径见下） | 来源 |
|---|---|---|---|---|---|
| 赤城 | 自沉（鱼雷 2–3 条命中） | 06-05 05:20 | 岚、萩风、舞风、野分（各 1 条） | 263 | [S1] |
| 加贺 | 自沉（鱼雷 2 条） | 06-04 19:25 | 萩风 | 814 | [S2] |
| 苍龙 | 自沉（鱼雷 3 条） | 06-04 19:12 | 矶风 | 713 | [S3] |
| 飞龙 | 自沉（鱼雷 1 条） | 06-05 05:10 | 卷云 | 418（Tully 注：扣除战俘后实为 383） | [S4] |
| 三隈（重巡） | 空袭沉没 | 06-06 约 19:30 | —（美军击沉） | 约 700 | [S7] |

**阵亡数口径差异（三说并列，不裁决）**

- 逐舰合计（Tully TROM）：263 + 814 + 713 + 418 = **2,208**（此数为本文按四舰相加，属读者自算，非来源结论，故括号标注）。
- ONI 1943 年战斗叙述（引尼米兹报告）：> "Estimated total number of personnel lost: 4,800." —— [S17-cn13]
- 飞龙单舰访谈：> "About 500 out of the 1500 men on the ship were lost." —— [S22]

**飞机损失（口径差异）**

> "Four carriers sunk: Akagi, Kaga, Soryu, Hiryu, with the loss of all their planes and many of their personnel. Estimated 275 planes, 2400 men."
> —— [S17-cn13]

NHHC 战斗序列页给出的编制总数为 **229 架**（[S18]），与「275 架损失」不能直接对齐——两者统计对象不同（编制数 vs 含岸基/补充机的损失估计），此处仅并列。

**飞行员阵亡数（口径差异，务必注明）**

> "More importantly, the Japanese lost over 100 trained pilots, who could not be replaced."
> —— [S18]

> "About sixty pilots were lost in the battle."（飞龙单舰）
> —— [S22]

精确总数（如 Parshall & Tully 的 110 人）在所查 A/B 级源中**未获取**，仅见「over 100」的表述。

### 4.2 美军

| 项 | 数值 | 原句 | 来源 |
|---|---|---|---|
| 舰船损失 | 约克城号、哈曼号 | "Ships: Yorktown and Hammann sunk." | [S17-cn13] |
| 飞机损失 | 约 150 架（含战损与报废） | "Planes: About 150 lost in action or damaged beyond repair." | [S17-cn13] |
| 人员阵亡 | 92 名军官 + 215 名士兵 = 307 | "Personnel: 92 officers and 215 men." | [S17-cn13] |
| 哈曼号单舰 | 241 名船员中 81 人阵亡 | "her depth charges explode and kill 81 of her 241-strong crew" | [S13] |

**中途岛岸基航空兵损失（明细）**

> "Of the 27 fighter planes of the Marine air group which intercepted the enemy bombers, 15 were missing and 7 severely damaged."
> "Missing in action: 13 F2A-3's and 2 F4F-3's. Severely damaged: 5 F2A-3's, and 2 F4F-3's."
> —— [S17-cn5]

> "Of the 16 SBD's which engaged in this attack, 8 returned to the base, and of these only 6 remained fit for service."（VMSB-241 SBD）
> —— [S17-cn6]

> "Of the 15 planes, not one returned from the attack."（VT-8，大黄蜂）
> —— [S17-cn7]

> "Of the 14 planes in the Enterprise squadron (VT-6) only 4 returned, and of the Yorktown's 12 planes constituting VT-3 only 2 survived the attack."
> —— [S17-cn7]

> "Of the two B-26's lost, one was seen to launch its torpedo and then to strike the flight deck of the carrier and hurtle into the sea."
> —— [S17-cn6]

> "Of this flight only one badly shot-up plane returned to make a landing with one wheel retracted."（6 架 TBF）
> —— [S17-cn6]

---

## §5 关键争议（每条两边原话并列）

### 争议 1 · 南云换弹决策到底发生了什么：甲板换装 vs 机库换装

**A 方（传统说法，源自渊田美津雄《中途岛》）：** 第二波已挂满鱼雷摆在甲板上，因利根报告而反复「鱼雷换炸弹→炸弹换鱼雷」，官兵在甲板上手忙脚乱。

> "Consequently, at 0715… he ordered the planes of the second wave, which had been armed for an attack on enemy ships, to prepare instead for another strike on Midway. This mean that the torpedo-laden level bombers on Akagi and Kaga had to be de-armed and reloaded with bombs."
> "On board Akagi, when the order was given to clear the deck for recovery, the weary maintenance crews began once more to lower the torpedo bombers to the hangar deck. There, the orders now were to switch back from bombs to torpedoes."
> —— 渊田原文，转引自 Parshall 2006 Historicon 讲义 [S26] https://www.admiraltytrilogy.com/pdf/Hist2006_Parshall_Midway_Brief.pdf

**B 方（Parshall & Tully）：** 预备攻击队很可能从未被摆上甲板；挂弹作业在日本航母上是在封闭机库里做的，且回收作业会完全关闭飞行甲板。

> "In fact, it is our strong belief that the reserve strike force was probably never spotted at all — Arming operations for torpedo planes typically occurred in the hangar — Aviator accounts (Abe Zenji) indicate that strikes were held in hangars until needed"
> —— [S26]

> "Before angled flight decks, you did one thing at a time: Spotting / Launching / Recovery. Recovery, in particular, shuts down the flight deck completely."
> —— [S26]

**日方原始文件（第三方材料，只说明发生过换装，不涉及甲板/机库之争）：**

> "It was decided, therefore, that a second attack would be directed against Midway. Orders were issued for the ship-based attack planes to remove their torpedoes and replace them with #80 land bombs."
> —— [S21]

### 争议 2 · 「命运五分钟」（Fuchida's five minutes）

**A 方（渊田原话，被后世广泛转述）：**

> "On Akagi's flight deck all planes were in position with engines warming up. The big ship began turning into the wind. Within five minutes all her planes would be launched. / Five minutes! Who would have dreamed that the tide of battle would shift completely in that interval of time?"
> —— 渊田原文，转引自 [S26]

**B 方（Parshall 的批评）：** 该画面与甲板作业节奏、作战记录、照片三重不符；摆一个攻击波次最短 30 分钟、常规 45 分钟，且摆机期间甲板完全不能作业。

> "Fuchida's rendition of flight deck operations doesn't appear to jibe with either common sense, the operational records, or the photographic record"
> "Total time required: 30 minutes bare minimum / 45 minutes normally — Flight deck shut down while spotting"
> —— [S26]

NHHC 官方史学的版本（第三种表述，强调是「延迟与混乱」而非「五分钟」）：

> "At 1020, the Japanese were still at least 45 minutes from being able to launch a full counterstrike, the same position they had been in when the first TBFs and B-26s attacked just after 0700."
> —— [S24]

### 争议 3 · 美军岸基航空兵的战果是否为零

**A 方（「几乎为零」）：**

> "During the course of the day, the mostly unmolested B-17s would drop over 320 bombs on Japanese ships, not one of which hit."
> —— [S24]

> "Lt. James P. Uri and Captain Collins brought their badly shot-up planes home to Midway after their gallant attack, but they had scored no hits, nor had the TBF's; on this point enemy survivors are unanimous."
> —— [S25]

**B 方（「不是零」）：**
1）PBY 鱼雷命中了曙丸（见 §0b（3）、§3 O1）：
> "the only U.S. torpedo to damage a Japanese ship in the entire battle"
> —— [S24]

2）VMSB-241 声称对加贺级航母 3 发直击（ONI 1943 年叙述采信，但同页脚注已自我怀疑）：
> "Three direct hits were seen and several near hits. As our planes returned low over the water they could see her smoking badly."
> 脚注：> "Possibly this identification was mistaken. It may have been the Soryu."
> —— [S17-cn6]

3）日方原始文件承认当日空袭造成了实际损伤（但归因给「舰载机」）：
> "From about 0400 the first enemy wave attacked. From then until about 0730, the enemy attacked almost continuously."（该件把 0400 起的连续攻击记为岸基机，0730 后记为舰载机）
> —— [S21]

**判读提示：** 三份材料对「谁打的」归因不同，但都不同意「战果为零」；而 [S24] 的「not one of which hit」专指 **B-17 的 320 枚炸弹**，不是指全部岸基航空兵。任务书把这两件事混为一谈。

### 争议 4 · 飞龙是否有可能更早反击

**A 方（可以更早，山口主张立即出击）：** 山口多闻主张不等回收第一波就立即出动。

> "Rear Admiral Yamaguchi actually recommended this solution, so dire did he perceive the threat."
> —— [S24]

**B 方（不能更早，受甲板作业与回收约束）：** 第一波必须回收，否则半数飞机要掉海里；且南云当时只知道「一艘」美军航母。

> "If he were to immediately spot his decks with the full reserve strike, while violently maneuvering under fire from bombs and strafing … some would still be carrying inappropriate weapons. More importantly, Nagumo's Midway strike (half his aircraft) would run out fuel and have to ditch."
> —— [S24]

起飞时刻本身也有 4 分钟分歧（§2 已录）：TROM 记 10:54，日方报告记 JST 0758（＝当地 1058）。

### 争议 5 · 利根 4 号机延迟起飞到底是不是败因

**A 方（是重要败因，通行说法）：**

> "Its late launch has been cited by many historians as a key factor in the Japanese defeat since it did not detect the U.S. carriers until it was too late."
> —— [S23]

**B 方（NHHC 反证：延迟反而帮了南云，且按时起飞会错过美军）：**

> "The reality is that had Tone No. 4 catapulted on time and flown the prescribed search route (instead of cutting it short) it would have completely missed the U.S. task groups. The late launch was actually one of Nagumo's few lucky breaks"
> —— [S24]

> "If Tone No. 4 had launched on time and flown the prescribed route, she would have missed the U.S. carriers, and the first indication Nagumo would have had of them was the 15 TBDs of Hornet's Torpedo Squadron EIGHT."
> —— [S23]

**另附一个连带责任方的说法（筑摩 1 号机）：**

> "Chikuma's No. 1 scout, launched on time, and flying No. 5 search line, should have seen TF-17 at approximately 0615, but did not due to clouds or other factors that remain unclear."
> —— [S23]

### 争议 6 · 赤城到底中了几弹

**A 方（两弹）：** 传统说法为一弹中部、一弹后部甲板。

> "Heretofore it has been generally reported that Akagi was struck by two bombs, one amidships, and the second on the rear of the flight deck."
> —— [S1]

**B 方（实际只有一弹致命）：**

> "However, in 'Shattered Sword' we (Jon Parshall & Anthony Tully) made the case that the available facts indicate the bomb aft did not detonate on the flight deck, but exploded close beside the fantail. For this reason, Akagi was in fact mortally wounded almost certainly by one hit alone"
> —— [S1]

**日方原始报告（两弹，但部位与 A 方不同）：**

> "one direct hit was sustained on the aft rim of the lift amidship and another on the rear guard of the port flight deck. (Neither were fatal hits.)"
> —— [S21]

### 争议 7 · 沉没时刻的三处硬冲突

| 项目 | 说法甲 | 说法乙 |
|---|---|---|
| 苍龙沉没 | TROM："Sunk: 1912 (1612 JST)"[S3] | 日方报告："the ship sank at 1613 and there was a great underwater explosion at 1620"（JST→当地 1913/1920）[S21] |
| 赤城自沉 | TROM："0450 … directed to be scuttled"→"0520 … sank"[S1] | 日方报告："at 0150 on the 6th … the ship was scuttled at 0200"（JST→当地 0450/0500）[S21] |
| 约克城沉没 | TROM（伊-168 页）："At 0458, the 19,875-ton YORKTOWN rolls over to port and sinks"[S13] | ONI 叙述："At 0501 'she turned over on her port side and sank'"[S17-cn13] |
| 三隈沉没 | TROM："Around 1930 MIKUMA turns on her port side and sinks"[S7] | 尼米兹转述生还者："The Mikuma capsized and sank within an hour and a half after initial bombing this date"[S17-cn12] |

### 争议 8 · 岸基轰炸机的战果评级（1942 年当时的官方评价 vs 战后修正）

**A 方（当时第七航空队上报）：**

> "Immediately after the action, General Emmons reported that his planes had scored a total of twenty-two direct bomb hits on carriers, battleships, cruisers, and destroyers, that one destroyer had been sunk, and that three torpedoes had struck home on two carriers."
> —— [S25]

**B 方（同一文献的战後修正）：**

> "But their evidence indicates the necessity of a radical scaling down of the original claims as sent in by the Seventh Air Force."
> "it would seem that the first attack produced a probable hit upon one transport, causing a small fire which was extinguished without delaying the ship, but that the combat craft escaped damage in the attack."
> —— [S25]

---

## §6 未获取清单

| # | 项目 | 检索范围 | 说明 |
|---|---|---|---|
| 1 | 飞龙号 6/4 第一波（对中途岛）出动分项数 | [S4] 飞龙 TROM、[S20] 战斗序列、[S21] 日方报告 | 仅有总数 108 机与赤城/加贺/苍龙分项；按规矩不以减法倒推 |
| 2 | 6 月 3 日首次接触的 PBY 机号 / 乘员 | [S17-cn4]、[S23]、[S25] | 报告只给出方位、距离、机种，未给机号 |
| 3 | 萩风、舞风、矶风、谷风、浦风、滨风、风云、卷云、朝潮、荒潮 舰长姓名 | combinedfleet 对应 TROM 页（`_t.htm`/`.htm`/`_tr.htm` 三种命名皆 404） | 页面不存在，非「没查到」，属站点缺页 |
| 4 | 大和、陆奥、长门、凤翔、川内、千代田、日进等舰长姓名 | [S20]、[S18] | NHHC 战斗序列只列编成不列舰长 |
| 5 | 第二机动部队（角田：龙骧、隼鹰）编成明细 | [S20]（该页未列北方部队）；[S5] 仅提及隶属 | 需另查日方战史（未做，因 E 级源不作依据） |
| 6 | 日军飞行员阵亡的精确总数（如 110 人） | [S18]、[S22]、[S17-cn13] | 只见「over 100」「约六十（飞龙单舰）」两种表述 |
| 7 | 日军飞机损失精确架数（分机型） | [S17-cn13] 给「Estimated 275 planes」 | 与 [S18] 的编制数 229 无法对齐，无中间口径可查 |
| 8 | 美军各舰具体阵亡名单与分舰数字 | [S17-cn13] 只给总数（92 军官 + 215 士兵） | NHHC 有 508 合规 PDF 伤亡名单（页面提及），本次未下载 |
| 9 | 榛名 6/4 受损的权威归因 | [S25]、[S17-cn6]、[S9] | 三方口径冲突（见 §3 O8），无法定论 |
| 10 | 三隈沉没的精确分钟 | [S7] 只给 "Around 1930" | 原始记录未精确到分 |
| 11 | 6 月 5 日「赤城处分推迟令」的原始电报全文 | [S1] 有摘要、[S21] 有编号（DesOpOrd #160/#161） | 全文（含签发分秒）未获取 |
| 12 | Parshall & Tully《Shattered Sword》原书页码级引文 | 仅得作者本人的 2006 讲义 PDF [S26] 与 TROM 注释 | 原书未获取，故全部标 C 级 |

---

## §7 来源清单

| id | 名称 | URL | 层级 | 说明 |
|---|---|---|---|---|
| S1 | IJN AKAGI: Tabular Record of Movement（A. P. Tully，2013 修订） | http://www.combinedfleet.com/Akagi.htm | **B** | 一手日方档案（行动详报、航海日志、幸存者记录）的系统整理，逐时；作者为《Shattered Sword》合著者。含对旧说的自证式修正注释 |
| S2 | IJN Kaga: Tabular Record of Movement（Tully，2014 修订） | http://www.combinedfleet.com/kaga.htm | **B** | 同上 |
| S3 | IJN Soryu: Tabular Record of Movement（Tully，2015 增强版） | http://www.combinedfleet.com/soryu.htm | **B** | 同上；苍龙段含大量无线电原文 |
| S4 | IJN Hiryu: Tabular Record of Movement（Tully，2000） | http://www.combinedfleet.com/hiryu.htm | **B** | 篇幅短（早期版），仅给概要时间点 |
| S5 | IJN Tone: TROM | http://www.combinedfleet.com/tone_t.htm | **B** | 利根 4 号机发现时刻、舰长任命链 |
| S6 | IJN Chikuma: TROM | http://www.combinedfleet.com/chikuma_t.htm | **B** | 舰长任命链 |
| S7 | IJN Mikuma: TROM（Hackett & Kingsepp） | http://www.combinedfleet.com/mikuma_t.htm | **B** | 6/5–6/6 逐时、命中明细 |
| S8 | IJN Mogami: TROM（Hackett & Kingsepp） | http://www.combinedfleet.com/mogami_t.htm | **B** | 6/6 命中明细、91 死 101 伤 |
| S9 | IJN Haruna: TROM | http://www.combinedfleet.com/haruna.htm | **B** | 舰长任命链 |
| S10 | IJN Kirishima: TROM | http://www.combinedfleet.com/Kirishima.htm | **B** | 舰长任命链 |
| S11 | IJN Nagara: TROM | http://www.combinedfleet.com/nagara_t.htm | **B** | 舰长任命链 |
| S12 | IJN Arashi: TROM（Allyn D. Nevitt） | http://www.combinedfleet.com/arashi_t.htm | **B** | 岚号舰长 |
| S13 | IJN I-168: TROM | http://www.combinedfleet.com/I-168.htm | **B** | 飞龙两波起飞时刻、击沉约克城全过程（含 0458 沉没说） |
| S14 | IJN Nowaki: TROM（Nevitt） | http://www.combinedfleet.com/nowaki_t.htm | **B** | 野分舰长 |
| S15 | IJN Kasumi: TROM（Nevitt） | http://www.combinedfleet.com/kasumi_t.htm | **B** | 霞舰长 |
| S16 | IJN Yugumo: TROM | http://www.combinedfleet.com/yugumo_t.htm | **B** | 夕云舰长 |
| S17 | ONI Combat Narrative: The Battle of Midway（1943 年 3 月，2017 年由 NHHC 重印） | https://www.ibiblio.org/hyperwar/USN/USN-CN-Midway/index.html | **A** | 官方战时战斗叙述，全部时刻为 Zone +12（脚注 10 明示：「All times given in this narrative are zone plus 12」）。逐章 URL：-4 / -5 / -6 / -7 / -8 / -9 / -11 / -12 / -13 |
| S18 | NHHC「Battle of Midway」专题总览 | https://www.history.navy.mil/browse-by-topic/wars-conflicts-and-operations/world-war-ii/1942/midway.html | **A** | 官方史学综述；229 架、飞行员「over 100」等口径出自此页 |
| S19 | 中途岛美军战斗序列（NHHC，2018-02-14 发布） | https://www.history.navy.mil/research/library/online-reading-room/title-list-alphabetically/c/composition-of-us-forces.html | **A** | 全部舰长、航空队指挥官、机型的权威名单 |
| S20 | 中途岛日方战斗序列（NHHC，2018-02-14 发布） | https://www.history.navy.mil/research/library/online-reading-room/title-list-alphabetically/c/composition-of-japanese-forces.html | **A** | 同上，日方侧 |
| S21 | The Japanese Story of the Battle of Midway（ONI P32-1002，1947；南云一手战斗详报英译） | https://www.history.navy.mil/research/library/online-reading-room/title-list-alphabetically/j/japanese-story-of-the-battle-of-midway.html | **A** | **全文 JST（5 日制）**；含「Outline of Events」逐时无线电记录。本文所有「原记为 JST」项均出此件 |
| S22 | Battle of Midway: Interrogation of Japanese Officials（USSBS，1945-10） | https://www.history.navy.mil/research/library/online-reading-room/title-list-alphabetically/b/battle-of-midway-interrogation-of-japanese-officials.html | **A** | 飞龙军官（含对马/加来侧）访谈，加贺、飞龙被弹数与阵亡数 |
| S23 | NHHC H-gram 006-2「ISR at Midway」（S. J. Cox，2019 修订） | https://www.history.navy.mil/about-us/leadership/director/directors-corner/h-grams/h-gram-006/h-006-2.html | **A**（带作者判断） | 利根 4 号机争议的官方反证；Ady/Chase 报告时刻 |
| S24 | NHHC H-gram 006-3「The Victory—Barely」（Cox，2019 修订） | https://www.history.navy.mil/about-us/leadership/director/directors-corner/h-grams/h-gram-006/h-006-3.html | **A**（带作者判断） | 7:15 换弹决策的完整推演、TBF/B-26 攻击细节、320 枚炸弹无一命中、曙丸中雷 0153 |
| S25 | Army Air Forces in WWII, Vol. I, ch. 9「Midway」（Wesley F. Craven & James L. Cate 主编） | https://www.history.navy.mil/research/library/online-reading-room/title-list-alphabetically/b/battle-of-midway-army-air-forces.html | **B** | 陆军航空队官方战史；B-17 战果的战後修正、榛名归因分歧 |
| S26 | Jon Parshall, "The Battle of Midway: A New Look at a Classic Battle"（Historicon 2006 讲义 PDF） | https://www.admiraltytrilogy.com/pdf/Hist2006_Parshall_Midway_Brief.pdf | **C** | 二手（作者本人对《Shattered Sword》的口头浓缩）；含渊田原话引文与「甲板作业 30/45 分钟」论据。原书未获取，故不引页码 |
| S27 | "Midway — Chapter 7 of Radar and the Fighter Directors"（Engineering and Technology History Wiki） | https://ethw.org/Midway_-_Chapter_7_of_Radar_and_the_Fighter_Directors | **C** | 战斗机引导视角，交叉校验 0430 起飞、0918/0940/1010 三波鱼雷机接触时刻、1058 飞龙反击令 |
| S28 | KIDO BUTAI 索引页（combinedfleet） | http://www.combinedfleet.com/KIDO%20BUTAI.htm | **D**（导航性） | 仅用于确认 TROM 命名规则（`Akagi.htm`、`kaga.htm`、`tone_t.htm` 等），不作史实依据 |

**层级定义**
- **A**：战时/战后官方原始文件或其官方译本、官方史学机构出版物。
- **B**：基于一手档案的系统性学术整理（Tully/Hackett/Kingsepp/Nevitt 的 TROM、AAF 官方战史）。
- **C**：二手研究/作者判断性文本（含作者本人对专著的浓缩）。
- **D**：导航页、索引页，仅用于定位。
- **E**：百科类（日文维基等）——本次**未引用任何 E 级材料**作为史实依据。

---

## 附：时区换算校验表（用于本文件自查）

| 事件 | 日方原始记录（JST，5 日制） | 换算（+3h，−1d） | 本地源记载 | 一致？ |
|---|---|---|---|---|
| 第一波起飞 | 0130 | 04:30 | 0430 [S1] | ✅ |
| 加贺中弹 | 0722 | 10:22 | 1022 [S2] | ✅ |
| 赤城中弹 | 0726 | 10:26 | 1026 [S1] | ✅ |
| 苍龙中弹 | 0725/0726/0728 | 10:25/10:26/10:28 | 1025–1029 [S3] | ✅ |
| 飞龙第一波起飞 | 0758 | 10:58 | 1054 [S13] | ⚠ 4 分钟差 |
| 飞龙被弹 | 1403 | 17:03 | 1703 [S4] | ✅ |
| 苍龙沉没 | 1613 | 19:13 | 1912 [S3] | ⚠ 1 分钟差 |
| 加贺沉没 | 1625 | 19:25 | 1925 [S2] | ✅ |
| 赤城自沉 | 0200（6 日） | 05:00（5 日） | 0520 [S1] | ⚠ 20 分钟差 |
| 飞龙自沉 | 0210（6 日） | 05:10（5 日） | 0510 [S4] | ✅ |

—— 文件结束 ——
