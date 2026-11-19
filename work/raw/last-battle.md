# 俾斯麦号最终战（1941-05-26/27）原始素材

采集人：last-battle-src（subagent）｜日期：2026-11-17｜目标文件：`data/battles/last-battle.yaml`（待 lead 定稿）

## 阅读前必须知道的四件事

1. **src 缩写**：本文用短码标注（`[TOV]` `[PAT]` …），含义见第四部分对照表。其中只有一部分已在 `data/sources.yaml` 登记；未登记者在对照表里明确标「**待登记**」，需 lead 决定是否补进 sources.yaml 后，才能写进正式 YAML。
2. **时间口径**：Tovey 战报（ADM 234/509）开头写明「All times are zone minus 2」；Patterson 报告、Admiralty War Diary、kbismarck 的整理页与德方 KTB 的报文时间组基本可对齐（KTB 每条同时给「Uhrzeitgruppe 报文时间组」与「记录时刻」，两者差 10–20 分钟）。**KTB 第 173 页那段「0630 望见 King George」是幸存者证词，比英方记录的 0843 早两个多小时，属证词误差，不可当时刻用。**
3. **每个数字都可能有第二个版本**。本文凡有分歧一律并列 + 标来源，不裁决；查不到的写「**未获取**」并说明试过哪几个 URL。
4. 严禁把本文的「约」当成确数。标「约」的地方，来源本身就只给了「about / circa / 约」。

### 对任务描述本身的一处更正（必须让 lead 知道）

派单里写「5-26 夜间的 Sheffield、**Victorious** 与 Swordfish 中队」。**Victorious 不在 5-26/27 的战场上，这一点有硬证据**：

- 她的 Swordfish 空袭发生在 **5-24 深夜/5-25 凌晨**（Admiralty War Diary 5-25 节：「Shortly after midnight 24/25 May F.A.A. aircraft from VICTORIOUS attacked BISMARCK with torpedoes and one hit was reported.」）。1942 年官方出版物《Coastal Command》（`kbismarck-its-the-bismarck`，tier B）记该攻击命中**右舷**，并称英方损失 2 架 Swordfish 与 2 架 Fulmar ——**但同一本书的脚注 1 自我更正：「实际上那些过时的 Swordfish 一架也没被击落」**，引用时以脚注为准。
- 5-26 当日她远在北方：09:55B 报位于 39°05'N 26°05'W、天气不宜飞行；**13:28B 已奉命赴克莱德湾加油**；5-26 全天她都在搜冰岛—法罗水道，与战场相距数百英里。
- 5-26 夜至 5-27 实施两波空袭的是 **皇家方舟号（HMS Ark Royal，Force H）**，810/818/820 中队。

→ 正式 YAML 的 `belligerents[].ships` 里**不要把 Victorious 列进 5-26/27 的参战兵力**；若要列，应注明「5-24 空袭，5-26 已脱离」。本文 `forces[].air` 条已按此处理。

---

# 第一部分：`timeline[]` YAML 片段

> 共 **62 条**（要求 ≥25 条）。`time` 已统一为 **`'MM-DD HH:MM'`**（如 `'05-26 20:47'`）——本战役跨两天，若只用 HH:MM 会出现「23:58 之后接 01:22」的排序错误。`denmark-strait.yaml` 里同一战役只跨一天，故它用裸 HH:MM；**lead 定稿时请二选一**：(a) 沿用本文的 `'MM-DD HH:MM'`，(b) 拆成 `last-battle-1` / `last-battle-2` 两个 battle 实体、各自回到裸 HH:MM。本文只给原始值。

```yaml
timeline:
  # ---------------- 5 月 26 日：搜索、发现、跟踪 ----------------
  - time: '05-26 03:00'
    text:
      zh: 两架海岸司令部 Catalina 从北爱尔兰 Lough Erne（RAF Castle Archdale）起飞，分赴南北两条巡逻线。
      en: Two Coastal Command Catalinas took off from Lough Erne, Northern Ireland, for the northern and southern patrol lines.
    src: [kbismarck-chase]
  - time: '05-26 03:25'
    text:
      zh: 据美方随行观察员 Smith 少尉报告，他所在的 Catalina 于 03:25 起飞，04:30 经 Eagle Island 转入向西搜索航向，高度 500 英尺。
      en: Ensign Smith's report gives take-off at 0325 and departure from Eagle Island at 0430, heading west at 500 ft.
    src: [kbismarck-smith-report]
  - time: '05-26 10:10'
    text:
      zh: Catalina Z/209 在 49°33'N 21°47'W 附近发现一艘大型军舰，方位 345°、距离 8 英里；因云层遮挡一度无法确认身份。英方记载的发现者为 F/O Dennis Briggs，实际操纵飞机的是随行的美国海军少尉 Leonard B. Smith（当时美国尚未参战，英方公报只写 Briggs）。
      en: Catalina Z/209 sighted a large warship bearing 345°, 8 miles, near 49°33'N 21°47'W. Officially credited to F/O Dennis Briggs; the aircraft was actually piloted by USN Ensign Leonard B. Smith.
    src: [kbismarck-smith-report, kbismarck-chase]
  - time: '05-26 10:30'
    text:
      zh: 首次发现电报发出：「1 battleship, bearing 240°, distance 5 miles, course 150°. My position 49°33'N 21°47'W.」——注意方位与距离和 10:10 目视时不同，是发电时重新测的。
      en: 'First sighting signal: "1 battleship, bearing 240°, distance 5 miles, course 150°, my position 49°33''N 21°47''W."'
    src: [kbismarck-catalina-reports, kbismarck-coastal-command, kbismarck-chase, kbismarck-communiques]
  - time: '05-26 10:35'
    text:
      zh: 补充电报：敌航向 150°、航速 20 节，本机位置 49°28'N 21°50'W。
      en: 'Supplementary signal: enemy course 150°, speed 20 knots, own position 49°28''N 21°50''W.'
    src: [kbismarck-catalina-reports]
  - time: '05-26 10:39'
    text:
      zh: 云层意外破开，几乎正好在俾斯麦号上空。德舰立即开火，Catalina 未及重回云中即被破片击中、机体多处穿孔。
      en: The cloud broke directly over Bismarck; she opened fire at once and hit the Catalina with shrapnel before it could regain cloud cover.
    src: [kbismarck-coastal-command, kbismarck-smith-report]
  - time: '05-26 10:45'
    text:
      zh: Catalina 失去接触，敌最后位置 49°22'N 21°44'W。接触共中断 31 小时余后才重新建立。
      en: Contact lost at 1045, enemy last seen at 49°22'N 21°44'W; the chase had been without contact for over 31 hours.
    src: [kbismarck-catalina-reports]
  - time: '05-26 11:14'
    text:
      zh: 皇家方舟号的两架 Swordfish（2H，Hartley 机组）在 49°32'N 20°55'W 重新发现俾斯麦号，7 分钟后 2F（Callander 机组）也到达。此后又派出两架带远程油箱的 Swordfish 接力跟踪。
      en: Two Ark Royal Swordfish (2H, Hartley crew) regained contact at 49°32'N 20°55'W; 2F (Callander) arrived seven minutes later and two long-range Swordfish took over shadowing.
    src: [kbismarck-admiralty-war-diary, kbismarck-chase, kbismarck-histoperi]
  - time: '05-26 13:30'
    text:
      zh: Catalina M/240 报「1 艘战列舰，方位 180°、距离 4 英里、航向 130°」，本机位置 48°12'N 19°50'W。此后断续跟踪到 18:00（47°15'N 18°23'W）返航。
      en: Catalina M/240 reported one battleship bearing 180°, 4 miles, course 130°, own position 48°12'N 19°50'W; shadowing continued intermittently until 1800.
    src: [kbismarck-catalina-reports]
  - time: '05-26 14:50'
    text:
      zh: 皇家方舟号第一波 15 架 Swordfish（Stewart-Moore 少校）起飞——其中 1 架中途返航。鱼雷装双联引信、定深 30 英尺（而非 34 英尺），因为当时皇家方舟号不确定目标到底是俾斯麦号还是欧根亲王号。
      en: First Ark Royal strike force of 15 Swordfish (Lt-Cdr Stewart-Moore) took off; one turned back. Torpedoes had duplex pistols set to 30 ft instead of 34 ft because the carrier was unsure whether the target was Bismarck or Prinz Eugen.
    src: [kbismarck-chase, hmshood-tovey-dispatch]
  - time: '05-26 15:50'
    text:
      zh: '**误击事件**：机群靠 ASV 在预期阵位约 20 英里处发现一艘军舰并穿云攻击——那是轻巡谢菲尔德号（舰长 Charles A. Larcom），英方并不知道她在俾斯麦号附近。11 枚鱼雷全部落空：2 枚入水即爆、3 枚横穿巡洋舰尾迹时爆炸、其余 6 枚被规避。谢菲尔德号一炮未还。'
      en: 'The striking force attacked a ship detected by ASV about 20 miles from the expected enemy position — the light cruiser Sheffield. Eleven torpedoes were dropped: two exploded on hitting the water, three on crossing the wake, the rest were avoided. Sheffield did not fire a round in reply.'
    src: [hmshood-tovey-dispatch, kbismarck-admiralty-war-diary, kbismarck-chase]
  - time: '05-26 17:05'
    text:
      zh: 英舰队燃油告急：英王乔治五世号仅剩 1,200 吨（32%）燃油，罗德里号报告次晨 08:00 将不得不脱离。Tovey 下令主力减速至 22 节以省油，此时已被追越的罗德里号编在其后。
      en: KGV had only 1,200 tons (32 per cent) of fuel left and Rodney reported she would have to part company at 0800 next morning; speed was reduced to 22 knots at 1705 to economise fuel, with the by-then overhauled Rodney formed astern.
    src: [hmshood-tovey-dispatch, kbismarck-admiralty-war-diary]
  - time: '05-26 17:40'
    text:
      zh: 谢菲尔德号目视发现俾斯麦号，接管跟踪，并保持在西侧约 14 英里。
      en: Sheffield made visual contact with Bismarck and took over shadowing, keeping about 14 miles to the westward.
    src: [kbismarck-histoperi, kbismarck-chase]
  - time: '05-26 19:03'
    text:
      zh: 俾斯麦号致西方集群：「燃油紧急，何时可得补给？」
      en: 'Bismarck to Group West: "Fuel situation urgent. When can I expect replenishment?"'
    src: [kbismarck-histoperi]
  - time: '05-26 19:15'
    text:
      zh: 皇家方舟号第二波 15 架 Swordfish（Coode 少校）起飞，多为第一波飞机重新装弹加油。这一波换装触发引信、定深 22 英尺。起飞前受命先与谢菲尔德号会合、由她引导。
      en: Second strike force of 15 Swordfish (Lt-Cdr Coode) flown off, mostly re-armed aircraft from the first wave, now with contact pistols set to 22 ft, ordered to home via Sheffield first.
    src: [kbismarck-chase, hmshood-tovey-dispatch]
  - time: '05-26 19:48'
    text:
      zh: U-556（Wohlfarth 上尉）发现声望号与皇家方舟号，但六天前打 HX-126 时已把鱼雷用尽，只能报出对方位置、航向与航速。
      en: U-556 (Kptlt Wohlfarth) sighted Renown and Ark Royal but had no torpedoes left, having expended them on convoy HX-126 six days earlier; she could only report position, course and speed.
    src: [kbismarck-chase]
  - time: '05-26 20:47'
    text:
      zh: 第二波攻击开始，持续约半小时。机群在俾斯麦号上空的锋面云下被打散，只能以小队或双机分批进入，德舰主副炮与高炮全程猛烈射击。**无 Swordfish 被击落**（4 架被破片击伤，其中 4C 数出 175 个弹孔）。至少 2 枚命中（一说是 3 枚）。英方战后的战俘审讯呈文把这次攻击记作 20:55–21:25，与 20:47 起算的叙述差约 8 分钟——两说并列。
      en: The attack began at 2047 and lasted about half an hour. The force was split by a cold front; attacks went in by sub-flights or pairs against intense fire. No Swordfish was lost (four were damaged by splinters, one with 175 holes). At least two hits were scored. The Admiralty interrogation report times the attack 2055–2125.
    src: [kbismarck-chase, kbismarck-histoperi, hmshood-tovey-dispatch, admiralty-bismarck-interrogation]
  - time: '05-26 21:05'
    text:
      zh: 德方报文时间组 2105（记录时刻 21:14）：「BE 6192 方格，艉部中雷」。
      en: 'German time-group 2105 (logged 2114): "Square BE 6192, hit by torpedo aft."'
    src: [kbismarck-ktb]
  - time: '05-26 21:15'
    text:
      zh: 德方报文时间组 2115：「舯部中雷」；同组另一电报：「舰已不可操纵」。两枚鱼雷的命中位置：一枚左舷舯部（多数能量被水下防护与装甲带吸收，仅结构与轻微进水），一枚艉部舵机区——**舷别左/右有争议（见争议 5）：kbismarck 早期叙述记左舷艉部、后文与最新残骸分析倾向右舷，英方一手审讯明确说右舷艉部**。左舵组联轴器严重损坏，**两舵卡死在向左 12°**（Junack 证词说左舵卡在 15°；英方审讯记 10–15° 并称舰「向右缓慢转圈」）。
      en: 'Time-group 2115: "hit amidships" and "ship no longer manoeuvrable". One hit amidships to port did little damage; the second struck the stern steering area — port or starboard is disputed (see dispute 5). The coupling was wrecked and both rudders jammed at 12 degrees to port (Junack recalled 15 degrees; the Admiralty interrogation gives 10–15 degrees and has her turning slowly to starboard).'
    src: [kbismarck-ktb, kbismarck-histoperi, kbismarck-chase, admiralty-bismarck-interrogation]
  - time: '05-26 21:30'
    text:
      zh: 俾斯麦号兜了一个整圈后不由自主朝西北顶风航行，此后只能兜大圈。艉部进水使操舵舱及邻近舱室淹没，修理须在水下进行，潜水员无法下潜；曾考虑炸掉舵，但怕伤及螺旋桨而放弃。
      en: Bismarck circled and was then forced up into the north-west wind. The stern flooding put the steering compartment under water; divers could not work and the idea of blowing the rudders off was dropped for fear of damaging the propellers.
    src: [kbismarck-chase, kbismarck-histoperi]
  - time: '05-26 21:40'
    text:
      zh: Lütjens 致 OKM 与西方集群：「舰已无法机动。将战斗至最后一发炮弹。元首万岁。」（英方维基记 23:40，德方电报时间组记 21:40——见争议 7）
      en: 'Lütjens to OKM and Group West: "Ship unmanoeuvrable. We will fight to the last shell. Long live the Führer." (21:40 in the German time-groups; some accounts give 23:40.)'
    src: [kbismarck-histoperi, kbismarck-last-battle]
  - time: '05-26 21:45'
    text:
      zh: 谢菲尔德号发出最后一次敌情报告（21:40）后约 5 分钟，俾斯麦号在约 9 英里距离上向她打了 6 次齐射——前两群偏差很大，第三群跨射——未直接命中，但破片打坏其雷达、伤 12 人，其中 3 人后来死亡（Ordinary Seaman David T. George 当日阵亡、Able Seaman Ambrose Ling 5-27 阵亡、Able Seaman Raymond C. Taylor 5-28 阵亡）。谢菲尔德号全速转向、施放烟幕脱离。
      en: 'Sheffield made her last enemy report; Bismarck fired six 15-inch salvoes at her at nine miles. No direct hit, but splinters wrecked her radar and wounded twelve, three of whom died. Sheffield turned away at full speed under smoke.'
    src: [hmshood-tovey-dispatch, kbismarck-chase, kbismarck-histoperi]
  - time: '05-26 22:00'
    text:
      zh: 谢菲尔德号联络 Vian 上校的第 4 驱逐舰分队（Cossack、Maori、Zulu、Sikh 与波兰 Piorun），把敌情方位距离交给驱逐舰。
      en: Sheffield passed the enemy's bearing and range to Captain (D) Vian's 4th Destroyer Flotilla — Cossack, Maori, Zulu, Sikh and the Polish Piorun.
    src: [kbismarck-chase, hmshood-tovey-dispatch]
  - time: '05-26 22:38'
    text:
      zh: 波兰驱逐舰 Piorun（kmdr Eugeniusz Plawski）在左翼发现俾斯麦号。4 分钟后德舰向其开火。
      en: The Polish destroyer Piorun (kmdr Plawski) sighted Bismarck on the port wing; the German ship opened fire four minutes later.
    src: [hmshood-tovey-dispatch, kbismarck-histoperi, kbismarck-chase]
  - time: '05-26 22:42'
    text:
      zh: 俾斯麦号向 Piorun 开火（英方记录 2242，德方 2242 同）。Piorun 还击后施放烟幕转开；Tovey 记她此后接近到可用火炮交战的距离，随后失去接触。
      en: Bismarck opened fire on Piorun, which replied and turned away under smoke.
    src: [hmshood-tovey-dispatch, kbismarck-histoperi]
  - time: '05-26 23:00'
    text:
      zh: Cossack 在 48°N 15°W 附近（敌方位 115°、7 英里、航向 060°）与俾斯麦号建立接触。
      en: Cossack established contact with Bismarck, enemy bearing 115°, 7 miles, course 060°.
    src: [kbismarck-admiralty-war-diary]
  - time: '05-26 23:42'
    text:
      zh: 一发近失弹破片打掉 Cossack 的天线。
      en: Splinters from a near miss carried away Cossack's wireless antenna.
    src: [kbismarck-chase]
  - time: '05-26 23:58'
    text:
      zh: Lütjens 致希特勒电：「我们战斗到最后一人，忠于您，我的元首，并坚信德国的胜利。」（德方记录时刻 00:32）
      en: 'Lütjens to Hitler: "We shall fight to the last man with confidence in you, my Führer, and with rock-solid trust in Germany''s victory."'
    src: [kbismarck-ktb, kbismarck-histoperi]

  # ---------------- 5 月 27 日：夜间鱼雷战、最后炮战、沉没与救援 ----------------
  - time: '05-27 01:22'
    text:
      zh: Zulu 报告「已完成鱼雷攻击」。此后 01:38 Maori 报告攻击、0138–0140 估称一雷命中、0145 报「一雷确认，舰首起火」、0146 Captain D.4 报「Cossack 攻击完成，声称一雷命中」。整夜第 4 驱逐舰分队共发射 16 枚鱼雷，英方声称 Cossack、Maori 各命中一雷、Sikh 可能也命中——但俾斯麦号最高生还军官说驱逐舰鱼雷无一命中（见争议 6）。
      en: Zulu reported her torpedo attack delivered at 0122; Maori attacked at 0138 and claimed one hit, "fire on forecastle" at 0145; Cossack completed her attack at 0146, claiming one hit. Sixteen torpedoes were fired during the night; the German senior survivor said none hit.
    src: [kbismarck-admiralty-war-diary, hmshood-tovey-dispatch]
  - time: '05-27 02:34'
    text:
      zh: Sikh 报「敌似已停住」。
      en: Sikh reported that the enemy appeared to be stopped.
    src: [kbismarck-admiralty-war-diary]
  - time: '05-27 03:53'
    text:
      zh: Captain D.4 报告：俾斯麦号在 02:40–03:40 之间沿 310° 前进约 8 英里，**仍能进行沉重而准确的射击**。
      en: Captain (D) 4th Flotilla reported that Bismarck had made about 8 miles on 310° between 0240 and 0340 and was still firing heavily and accurately.
    src: [kbismarck-admiralty-war-diary]
  - time: '05-27 04:00'
    text:
      zh: 04:00–05:00 之间夜间驱逐舰战斗中止。舰上用广播向全舰传达了元首与海军总司令的电文。
      en: The destroyer battle broke off between 0400 and 0500; the Führer's and the Commander-in-Chief's messages were broadcast to the crew.
    src: [kbismarck-ktb]
  - time: '05-27 05:00'
    text:
      zh: 俾斯麦号报天气：半阴、云底 600 米、西北风 7 级。此时舰横在海面、几乎不动，浪打上甲板把部分 10.5 cm 高炮炮手卷下海；一架舰载机被冲下海（浮筒朝上漂流）。夜间曾试图弹射另一架 Ar 196 送走战争日志与对胡德号作战的胶片，因横摇过剧失败；弹射器蒸汽管早在 5-24 已被威尔士亲王号打坏。满油飞机随后被推下海以免起火。
      en: 'Weather report: half overcast, ceiling 600 m, NW 7. The ship lay almost stopped, abeam to the sea; one floatplane was washed overboard. An attempt to launch an Arado 196 with the war diary and the Hood film had failed in the night, its catapult having been damaged on 24 May; the fuelled aircraft was pushed overboard to reduce fire risk.'
    src: [kbismarck-ktb, kbismarck-histoperi]
  - time: '05-27 07:10'
    text:
      zh: 俾斯麦号最后一份电报（德方记录时刻 07:29）：「派 U 艇来保管战争日志！」此后德方再未收到该舰任何回复；Herzog 称天线已被打断。U-556 受命前往，但因潜航错过电令且燃油不足。
      en: 'Bismarck''s last signal (time-group 0710, logged 0729): "Send U-boat for safe-keeping of war diary!" Nothing further was ever received from her; U-556 was assigned but missed the order while submerged and was short of fuel.'
    src: [kbismarck-ktb, kbismarck-histoperi]
  - time: '05-27 07:37'
    text:
      zh: 英王乔治五世号编队得知敌在方位 120°、距离 21 英里，改向 080° 接近。08:20 望见诺福克号，建立目视联系（诺福克号整夜绕到东北方向，为战列舰做 flank marking）。
      en: 'The battlefleet learned the enemy bore 120° at 21 miles and altered to 080°; Norfolk was sighted at 0820, providing a visual link.'
    src: [hmshood-tovey-dispatch]
  - time: '05-27 08:43'
    text:
      zh: 英王乔治五世号瞭望在 25,000 码（约 23,000 m）发现俾斯麦号，方位 188°，正向英舰驶来；英队航向 110°。德舰此时航速仅 7 节，顶风，艉部进水略减小了艏倾，左倾轻微。
      en: Bismarck was sighted at 0843, bearing 188°, 25,000 yards, steering directly towards the British line, which was on 110°. The German ship was making only seven knots.
    src: [hmshood-tovey-dispatch, kbismarck-last-battle, kbismarck-patterson-report]
  - time: '05-27 08:47'
    text:
      zh: '**罗德里号开火**，距离约 20,000 m（21,870 码）。它九门 16 英寸炮全在舰前部，可同时射击。一分钟后英王乔治五世号开火（该舰记录为 08:48、距离 24,600 码），诺福克号稍后加入。'
      en: 'Rodney opened fire at 0847 at about 20,000 m; KGV followed one minute later (her own report: 0848, 24,600 yards) and Norfolk joined shortly after.'
    src: [hmshood-tovey-dispatch, kbismarck-last-battle, kbismarck-patterson-report]
  - time: '05-27 08:49'
    text:
      zh: 俾斯麦号以 Anton、Bruno 两座前炮塔（共 4 门 38 cm）还击罗德里号；Cäsar、Dora 因舵损无法转向，打不到目标。开局是 4 门德炮对 15 门英炮。首群偏近约 400 码，第二群距离对但方向错；**第二次齐射即跨射罗德里号**——这是德舰在整个决战中最接近命中英舰的一次。
      en: 'Bismarck replied at 0849 with Anton and Bruno (four 38 cm guns) at Rodney; Cäsar and Dora could not be trained. Four German guns against fifteen British; the second salvo straddled Rodney.'
    src: [kbismarck-last-battle, kbismarck-patterson-report, kbismarck-histoperi]
  - time: '05-27 08:54'
    text:
      zh: 英王乔治五世号报告首枚命中，打进俾斯麦号前上层建筑基部。诺福克号（8 门 20.3 cm）此时加入射击。
      en: KGV reported her first hit at 0854 on the base of the forward superstructure; Norfolk joined with her eight 8-inch guns.
    src: [kbismarck-patterson-report, kbismarck-last-battle]
  - time: '05-27 08:58'
    text:
      zh: 罗德里号 6 英寸副炮加入射击。
      en: Rodney's 6-inch secondary battery opened fire.
    src: [kbismarck-last-battle]
  - time: '05-27 09:02'
    text:
      zh: 俾斯麦号被多发命中舰首楼与前桅，前桅测距仪失效。多份材料把这一发（罗德里号 16 英寸齐射）记为**第一次中弹**，并称它摧毁舰桥与主火控指挥仪、当场打死舰桥内大部分军官。**但英方一手审讯记战俘说法为 08:57 首次中弹（在 08:51 罗德里号跨射之后），见争议 12。**
      en: Bismarck was hit on the forecastle and foremast, disabling the foretop rangefinder; this is usually given as her first hit and is credited with destroying the bridge and main fire-control director. The Admiralty interrogation of survivors, however, puts her first hit at 0857 (see dispute 12).
    src: [kbismarck-histoperi, kbismarck-last-battle, admiralty-bismarck-interrogation]
  - time: '05-27 09:04'
    text:
      zh: 多塞特郡号（舰长 Benjamin C. S. Martin）加入射击。此刻是两艘战列舰 + 两艘重巡同时打一条失去机动的船。
      en: Dorsetshire (Captain Benjamin C. S. Martin) opened fire, making two battleships and two heavy cruisers in action.
    src: [kbismarck-last-battle]
  - time: '05-27 09:08'
    text:
      zh: 前测距仪与 Anton、Bruno 两座前炮塔失效。火控转到后指挥所，由第四炮术官 Müllenheim-Rechberg 上尉指挥，向英王乔治五世号打了 4 次齐射。
      en: The forward rangefinder and turrets Anton and Bruno were put out of action; fire control shifted aft to the after command post under Kapitänleutnant Müllenheim-Rechberg, who fired four salvoes at KGV.
    src: [kbismarck-last-battle, kbismarck-histoperi]
  - time: '05-27 09:10'
    text:
      zh: 罗德里号在远距离发射 6 枚鱼雷（口径本文未在已抓一手材料中取得，**不作断言**），全部未中。诺福克号亦于此时前后发射 4 枚——**「诺福克号 4 枚」仅见于英文维基（tier E），kbismarck 未记，存疑**。Tovey 战报第 88 段把「罗德里号鱼雷 1 发命中」列入其损伤序列，但自己也只写「one by Rodney's torpedo」而无从证实。
      en: Rodney fired six torpedoes at long range, none hitting. Norfolk is said (secondary source only) to have fired four about this time. Tovey's dispatch lists "one by Rodney's torpedo" among possible hits, unconfirmed.
    src: [kbismarck-last-battle, hmshood-tovey-dispatch]
  - time: '05-27 09:13'
    text:
      zh: 后指挥所刚测出距离即被一发 14 英寸炮弹摧毁 cupola。此后后炮塔转局部控制射击罗德里号。
      en: The after command post was itself destroyed by a 14-inch shell just as it had found the range; the after turrets then fired under local control at Rodney.
    src: [kbismarck-last-battle, kbismarck-histoperi]
  - time: '05-27 09:17'
    text:
      zh: 英舰战列线改向敌并右转至正北（罗德里号抢先转），两舰射向约成直角，可互不干扰射击。
      en: The British line turned towards the enemy and round to due north, giving the two ships arcs at right angles.
    src: [hmshood-tovey-dispatch]
  - time: '05-27 09:21'
    text:
      zh: Dora 炮塔因自身炮弹在右炮管内爆炸而失效。
      en: Turret Dora was put out of action when one of its own shells exploded inside the right barrel.
    src: [kbismarck-last-battle, kbismarck-histoperi]
  - time: '05-27 09:27'
    text:
      zh: Anton 或 Bruno 意外打出最后一次齐射。
      en: Turret Anton or Bruno fired one last, unexpected salvo.
    src: [kbismarck-last-battle, kbismarck-histoperi]
  - time: '05-27 09:31'
    text:
      zh: Cäsar 打出最后一次齐射，四座主炮塔全部失效，只剩少数副炮仍在射击（很快也被压制）。此后英舰再未遭到有效还击。英王乔治五世号上的 Guernsey 少校记 Tovey 在整场战斗中反复喊「Close the range」，并描述此时一发德弹跨射英舰舰首（一近三远），以及一处桥楼基部的火焰「瞬间吞没整个观察所」。
      en: Cäsar fired her last salvo; all four main turrets were out of action and only a few secondary guns remained, soon silenced. Guernsey, aboard KGV, recalled Tovey repeatedly calling "Close the range", a German salvo straddling the KGV's bow, and a flame at the base of a superstructure that momentarily engulfed the whole spotting position.
    src: [kbismarck-last-battle, kbismarck-histoperi, kbismarck-guernsey-report]
  - time: '05-27 09:40'
    text:
      zh: Bruno 炮塔后壁被炸开、炮塔起火。罗德里号已进至 2,500–4,000 m，用九门 16 英寸同时打两舷。
      en: The rear wall of turret Bruno blew out and the turret caught fire; Rodney closed to 2,500–4,000 m and fired her nine 16-inch guns at both sides.
    src: [kbismarck-last-battle]
  - time: '05-27 09:56'
    text:
      zh: 罗德里号自 2,700 m 发射 2 枚鱼雷（另一记载为 09:58），可能 1 发命中左舷；10:00 后诺福克号又自约 3,600 m 发射 4 枚，可能 1 发命中右舷。两处均无确证。
      en: Rodney fired two torpedoes at 2,700 m (some accounts say 0958), possibly one hit to port; after 1000 Norfolk fired four at about 3,600 m, possibly one hit to starboard. Neither is confirmed.
    src: [kbismarck-last-battle, kbismarck-histoperi, admiralty-bismarck-interrogation]
  - time: '05-27 10:00'
    text:
      zh: 约此刻舰内涡轮舱的爆破装药爆炸——这是自沉程序实际开始执行的时刻之一（与 10:15「准备沉舰」令并存，两说的关系见第三部分争议 1）。
      en: About this time the demolition charges in the turbine room detonated — one of the moments at which the scuttling procedure actually began (see dispute 1).
    src: [kbismarck-histoperi, kbismarck-last-hours]
  - time: '05-27 10:15'
    text:
      zh: 轮机长（Korvkpt(Ing) Walter Lehmann）电话通知 Junack「准备沉舰」——这是 Junack 收到的最后一道命令，此后全舰命令传递中断。自沉装药装 9 分钟引信。同一时段，皇家方舟号 09:20 起飞的 12 架 Swordfish 抵达，因英舰炮火密集无法攻击，未投雷（英王乔治五世号一度误认其为德机并向其开高炮，未命中）。
      en: The Chief Engineer, Korvkpt(Ing) Lehmann, telephoned Junack to "prepare the ship for sinking" — the last order Junack received; charges were set with nine-minute fuses. About the same time twelve Swordfish flown off Ark Royal at 0920 arrived but could not attack through the British gunfire and dropped no torpedoes.
    src: [kbismarck-last-hours, kbismarck-last-battle]
  - time: '05-27 10:16'
    text:
      zh: 罗德里号停火（kbismarck 记 10:16）。英王乔治五世号稍后于 10:21 停火。停火原因是两舰燃油极缺，Tovey 判断「进一步炮击也不会加速其沉没」。
      en: Rodney ceased fire at 1016, KGV at 1021. Tovey broke off because KGV and Rodney were critically short of fuel and further gunfire would do little to hasten the end. The Admiralty interrogation gives 1022 for the cease-fire.
    src: [kbismarck-last-battle, hmshood-tovey-dispatch, kbismarck-patterson-report, admiralty-bismarck-interrogation]
  - time: '05-27 10:22'
    text:
      zh: 多塞特郡号自 3,000 m 向右舷发射 2 枚 21 英寸 Mark VII 鱼雷，均命中，但「几乎没有使她震动」。英方一手审讯记该舰「having hit with three torpedoes」（合计 3 雷，见争议 13）。
      en: Dorsetshire fired two 21-inch Mark VII torpedoes at 3,000 m into the starboard side; both hit, with almost no visible effect. The Admiralty interrogation credits her with three torpedo hits in all (see dispute 13).
    src: [kbismarck-histoperi, kbismarck-last-battle, admiralty-bismarck-interrogation]
  - time: '05-27 10:28'
    text:
      zh: Tovey 正式中止战斗：「Have had to discontinue action for fuel.」10:42 他通报 Force H「cannot get BISMARCK to sink by gunfire」，10:45 又补「Cannot get her to sink with guns」——措辞后被他自己评为「perhaps unfortunately phrased」。
      en: 'Tovey: "Have had to discontinue action for fuel"; at 1042 and 1045 he signalled Force H that he could not get Bismarck to sink by gunfire, phrasing he later called unfortunate.'
    src: [kbismarck-admiralty-war-diary, hmshood-tovey-dispatch]
  - time: '05-27 10:36'
    text:
      zh: 多塞特郡号转向，自 2,200 m 向左舷再射 1 枚鱼雷，命中。此时俾斯麦号已严重左倾、水已漫上主甲板、左舷副炮塔几近没入。
      en: Dorsetshire turned and fired one more torpedo at 2,200 m into the port side; by then Bismarck was listing heavily with water over the main deck.
    src: [kbismarck-histoperi, kbismarck-last-battle, kbismarck-patterson-report]
  - time: '05-27 10:39'
    text:
      zh: 俾斯麦号向左翻覆、舰艉先沉，沉没于 48°09'N 16°07'W（BE 5336 方格）。另有一组记录为 10:37、10:36 或 10:40；英海军部对外公布的是 11:01（见争议 8）。沉没点水深：Patterson 报告该处为 2,500 英寻（约 4,570 m）；1989 年 Ballard 队实测残骸处深 4,790 m（15,700 英尺）。
      en: Bismarck capsized to port and sank stern-first at 48°09'N 16°07'W. Other sources give 1037, 1036 or 1040; the Admiralty communiqué gave 1101. Patterson's report gives 2,500 fathoms (about 4,570 m) at the sinking point; Ballard's 1989 survey measured 4,790 m (15,700 ft) at the wreck.
    src: [kbismarck-histoperi, kbismarck-last-battle, hmshood-tovey-dispatch, kbismarck-admiralty-war-diary, kbismarck-patterson-report, kbismarck-wreck, kbismarck-communiques, kbismarck-debriefing]
  - time: '05-27 11:40'
    text:
      zh: 救援中止。多塞特郡号放下绳索，约 800 人在水中；瞭望报告下风出现可疑物（可能是 U 艇潜望镜），多塞特郡号与毛利人号被迫离开。**该瞭望判断很可能是错的**——Junack 记「附近并无德国 U 艇」，英方一手审讯也称「this may have been the only one in the vicinity when Bismarck sank」（附近可能仅此一艘，且几小时后才有 4–6 艘 U 艇赶到）。已救起者：多塞特郡号 85 或 86 人（含 4 名军官）、毛利人号 24 或 25 人；**Tovey 战报的官方口径是「4 军官 + 75 兵」与「毛利人 24 兵」，即合计 103 人——与 111/116 并存，见争议 14。**
      en: The rescue was abandoned at 1140 when a possible periscope was sighted; Dorsetshire and Maori had by then picked up about 85–86 and 24–25 men respectively. Junack recorded that there was no U-boat nearby, and the Admiralty interrogation thought any U-boat present may have been the only one. Tovey's dispatch gives the official figures as four officers and 75 ratings plus 24 from Maori — 103 in all (see dispute 14).
    src: [hmshood-tovey-dispatch, kbismarck-last-battle, kbismarck-last-hours, kbismarck-admiralty-war-diary, admiralty-bismarck-interrogation]
  - time: '05-27 19:30'
    text:
      zh: U-74（Kentrat 艇长）从小艇救起 3 人：Herbert Manthey、Otto Höntzsch、Georg Herzog。
      en: U-74 (Kptlt Kentrat) rescued three men from a raft — Manthey, Höntzsch and Herzog.
    src: [kbismarck-last-battle]
  - time: '05-28 22:45'
    text:
      zh: 德国气象船 Sachsenwald（Schütte 舰长）22:35 见左舷 2–3 海里处三颗红色信号弹，转向后发现一只木筏、2 人，22:45 靠帮用两副绳梯救起 Otto Maus 与 Walter Lorenzen。该舰 5-30 00:45 在搜索区与西班牙重巡 Canarias 会合，6-1 靠泊波尔多。
      en: The German weather ship Sachsenwald (Kptlt Schütte) saw three red flares at 2235 and rescued Otto Maus and Walter Lorenzen by rope ladder at 2245, later rendezvousing with the Spanish cruiser Canarias.
    src: [kbismarck-sachsenwald-report, kbismarck-last-battle]
  - time: '05-30 10:00'
    text:
      zh: 西班牙重巡 Canarias 在搜索区捞起两具遗体（Walter Gaszczak、Heinrich Neuschwander），5-31 10:00 海葬。她 5-27 约 11:00 自 El Ferrol 出动。
      en: On 30 May the Spanish cruiser Canarias recovered two bodies (Gaszczak and Neuschwander), burying them at sea on 31 May; she had sailed from El Ferrol on 27 May.
    src: [kbismarck-last-battle, kbismarck-ktb]
```

---

# 第二部分：`hits_received[]` / `consequences[]` / `losses[]`

## 2.0 先给 `belligerents[]` 与 `forces[]`（用户要求 1）

```yaml
belligerents:
  - side: axis
    label: { zh: 德国, en: Germany }
    ships:
      - name: Bismarck
        ship_id: bismarck
        role: { zh: 战列舰 · 编队旗舰, en: Battleship · fleet flagship }
  - side: allies
    label: { zh: 英国（含波兰驱逐舰 Piorun）, en: United Kingdom (with Polish destroyer Piorun) }
    ships:
      - name: HMS King George V
        role: { zh: 战列舰 · 本土舰队旗舰, en: Battleship · Home Fleet flagship }
      - name: HMS Rodney
        role: { zh: 战列舰 · 原定赴波士顿修理, en: Battleship · en route to Boston for repairs }
      - name: HMS Norfolk
        role: { zh: 重巡洋舰 · 整夜绕至东北做 flank marking, en: Heavy cruiser }
      - name: HMS Dorsetshire
        role: { zh: 重巡洋舰 · 执行最后雷击, en: Heavy cruiser · delivered the final torpedoes }
      - name: HMS Sheffield
        role: { zh: 轻巡洋舰 · 5-26 跟踪, en: Light cruiser · shadower on 26 May }
      - name: HMS Ark Royal
        role: { zh: 航空母舰 · Force H, en: Aircraft carrier · Force H }
      - name: HMS Victorious
        role: { zh: 航空母舰 · 5-24 空袭（5-26 已脱离、不在战场，见文首更正）, en: Aircraft carrier · 24 May strike only; detached well before 26–27 May }
      - name: HMS Cossack
        role: { zh: 驱逐舰 · 第 4 驱逐舰分队旗舰, en: Destroyer · Captain (D), 4th Flotilla }
      - name: HMS Maori
      - name: HMS Zulu
      - name: HMS Sikh
      - name: ORP Piorun
        role: { zh: 驱逐舰 · 波兰海军, en: Destroyer · Polish Navy }

# 各舰武备与「当时状态」。火力数字取 navweaps 与 Tovey/Patterson 报告；
# 状态一栏只写来源明确说过的话，查不到的写未获取。
forces:
  - side: axis
    guns:
      zh: 8 × 38 cm SK C/34（4 座双联）+ 12 × 15 cm + 16 × 10.5 cm 高炮
      en: 8 × 38 cm SK C/34 (4 twin turrets) + 12 × 15 cm + 16 × 10.5 cm AA
    state:
      zh: 航速 7 节、顶风；两舵卡死向左 12°，无法用主机保持航向；Anton/Bruno 可射，Cäsar/Dora 因舵损无法转向；左倾轻微至明显（各来源不一致）。
      en: Seven knots, steering jammed 12° to port; Anton and Bruno could bear, Cäsar and Dora could not be trained; slight to marked list to port depending on the account.
    src: [kbismarck-last-battle, kbismarck-histoperi, hmshood-tovey-dispatch]

  - side: allies
    guns:
      zh: 罗德里号 9 × 40.6 cm（16"/45 Mark I，三座三联全在舰前部）+ 12 × 15.2 cm（6"/50 Mark XXIII，六座双联）；英王乔治五世号 10 × 35.6 cm（14"/45 Mark VII）+ 16 × 13.3 cm（5.25 英寸）；诺福克号、多塞特郡号各 8 × 20.3 cm（8"/50 Mark VIII）
      en: Rodney 9 × 40.6 cm (16"/45 Mk I, all forward) + 12 × 15.2 cm (6"/50 Mk XXIII); KGV 10 × 35.6 cm (14"/45 Mk VII) + 16 × 13.3 cm; Norfolk and Dorsetshire 8 × 20.3 cm (8"/50 Mk VIII) each
    state:
      zh: 罗德里号最高航速 21 节，已被英王乔治五世号追越、编在其后；炮术报告中 X 炮塔在前 25 次齐射中只有 6 次能瞄准目标，25 次后又有 9 次不能（合计 28 次）；战斗结束时 A 塔右炮因 tilting tray 卡死完全失效、B 塔左炮因下发射药提升机 double loaded 极短暂失效、B 塔中炮因两发弹无发射药暂时失效；4.7 英寸高炮全程未开火。英王乔治五世号 A 塔失效近 30 分钟、Y 塔 7 分钟、B 塔短暂失效，R.D/F 受损，有时一次 14 英寸齐射只有 1–2 门能打，只好改用全舷射。
      en: Rodney's best speed was 21 knots and she had been overhauled by KGV. Her report records that X turret could bear on only 6 of the first 25 salvoes and failed 9 more times; at the end A turret's right gun was out (jammed tilting tray), B's left gun briefly out (double-loaded hoist) and B's centre gun temporarily out. The 4.7-inch AA never fired. KGV had A turret out for nearly 30 minutes, Y for 7 minutes, B briefly, her R.D/F damaged, and sometimes only one or two 14-inch guns per salvo.
    src: [kbismarck-rodney-report, kbismarck-patterson-report, navweaps-16in-45-mk1, navweaps-14in-45-mk7, navweaps-8in-50-mk8, navweaps-6in-50-mk23]

  - side: allies
    air:
      zh: 5-26 两波各 15 架 Swordfish（皇家方舟号 810/818/820 中队）；5-27 09:20 再起飞 12 架，抵达时未能攻击。**必须更正一个常见误解** —— 胜利号（HMS Victorious）并未参加 5-26 夜至 5-27 的决战。她的 Swordfish 空袭发生在 5-24 深夜至 5-25 凌晨（对俾斯麦号，命中 1 雷），此后即脱离。Admiralty War Diary 5-26 记她当日 09:55B 位于 39°05'N 26°05'W、天气不宜飞行，13:28B 已奉命赴克莱德湾加油 —— 距战场数百英里。5-26/27 在场的是皇家方舟号（Force H）。
      en: Two strikes of 15 Swordfish each on 26 May from Ark Royal; twelve more flown off at 0920 on 27 May but unable to attack. Victorious did NOT take part in the 26-27 May action — her Swordfish strike was on the night of 24/25 May, after which she was detached, and on 26 May she was ordered to the Clyde to refuel while far to the north.
    src: [hmshood-tovey-dispatch, kbismarck-last-battle, kbismarck-admiralty-war-diary]
```

## 2.1 `hits_received[]`（俾斯麦号中弹）

```yaml
hits_received:
  - text:
      zh: 5-24 丹麦海峡：被威尔士亲王号命中 3 发（Tovey 战报口径）。
      en: Three gunfire hits from Prince of Wales on 24 May, per Tovey's dispatch.
    src: [hmshood-tovey-dispatch]
  - text:
      zh: 5-26 20:47 起的空袭：英方与德方都确认至少 2 枚 18 英寸 Mark XII 航空鱼雷命中——一枚左舷舯部（主装甲带下缘，能量多被水下防护吸收，仅结构与轻微进水）、一枚艉部舵机区（左舵组联轴器严重损坏，两舵卡死向左 12°）。有材料说 3 枚（第 3 枚通常指另一枚打在舯部附近）。
      en: 'At least two 18-inch Mark XII aerial torpedoes: one amidships to port with little effect, one in the stern steering area which wrecked the rudder coupling and jammed both rudders 12° to port.'
    src: [kbismarck-chase, kbismarck-histoperi, kbismarck-admiralty-war-diary]
  - text:
      zh: 5-27 08:54：英王乔治五世号命中俾斯麦号前上层建筑基部（该舰报告口径）。
      en: At 0854 on 27 May KGV hit the base of the forward superstructure.
    src: [kbismarck-patterson-report]
  - text:
      zh: 5-27 09:02：罗德里号 16 英寸齐射命中前上层建筑，摧毁舰桥与前桅测距仪/主火控指挥仪，当场打死舰桥内大部分军官，并波及前主炮塔。**部分材料（含德方档案整理页与英方维基）把这一击记为同时打死 Lindemann、Lütjens 与舰桥其余人员；另一些幸存者说沉没前还看见 Lindemann 在甲板上——见争议 3。** 另：英方一手审讯记战俘称首枚中弹在 **08:57**（08:51 罗德里号跨射之后），并记 Müllenheim-Rechberg 认为摧毁主火控的那一发其实**来自多塞特郡号**——见争议 12。
      en: 'At 0902 a Rodney 16-inch salvo wrecked the bridge, foretop rangefinder and main fire-control director, killing most of the bridge staff. Some accounts place the deaths of Lindemann and Lütjens here; other survivors saw Lindemann on deck later. The Admiralty interrogation puts the first hit at 0857, and Müllenheim-Rechberg believed the shell that destroyed the main fire control came from Dorsetshire.'
    src: [kbismarck-histoperi, kbismarck-last-battle, admiralty-bismarck-interrogation]
  - text:
      zh: 5-27 约 09:40：Bruno 炮塔后壁被炸开、起火。
      en: About 0940 the rear wall of turret Bruno blew out and the turret burned.
    src: [kbismarck-last-battle]
  - text:
      zh: 5-27 约 10:00：**据单一二手叙述**，一发英王乔治五世号 14 英寸炮弹穿透上部纵深装甲带，在舰尾食堂内爆炸，炸死副舰长（First Officer）Hans Oels 与约一百人。**本条仅见于英文维基（tier E），本次未在一手材料中取得佐证**；Oels 下令自沉一事同样只见于二手文献与 Cameron 2002 的引文。使用前应另找一手来源，或按「存疑」标注。
      en: 'About 1000 a 14-inch shell from KGV reportedly penetrated the upper citadel belt and burst in the aft canteen, killing First Officer Oels and about a hundred men. This appears only in secondary/encyclopedic accounts and was not corroborated in any primary source gathered here.'
    src: [kbismarck-last-battle]
  - text:
      zh: 5-27 约 10:05：英王乔治五世号自约 3,000 码打出三发可见命中——两发打进上层建筑基部甲板，一发从前部打进 B 炮塔、似将塔后半整体掀入海。
      en: About 1005, from about 3,000 yards, KGV observed three clear hits — two on the superstructure base and one entering B turret from forward, apparently tearing away the rear of the turret.
    src: [kbismarck-patterson-report]
  - text:
      zh: 鱼雷命中（合计，各方数字不一）：5-26 航空雷 2（或 3）；5-27 01:22–01:46 驱逐舰雷英方声称 2–3 发命中、德方最高生还军官称 0；09:56 罗德里号 2 枚（可能 1 命中左舷）；10:00 后诺福克号 4 枚（可能 1 命中右舷）；10:22 多塞特郡号 2 枚右舷均命中；10:36 多塞特郡号 1 枚左舷命中。**英方一手审讯只记「Rodney 命中一雷」+「多塞特郡三雷全中」，不列驱逐舰战果；Tovey 第 88 段则把 5-27 晨驱逐舰鱼雷两发计入损伤序列。见争议 6 与争议 13。**
      en: 'Torpedo hits, all sources: two (possibly three) aerial on 26 May; two to three claimed by destroyers in the night, denied by the German senior survivor; possibly one from Rodney at 0956 and one from Norfolk after 1000; two confirmed from Dorsetshire to starboard at 1022 and one to port at 1036. The Admiralty interrogation credits only Rodney with one torpedo hit and Dorsetshire with three.'
    src: [kbismarck-admiralty-war-diary, hmshood-tovey-dispatch, kbismarck-last-battle, kbismarck-histoperi, admiralty-bismarck-interrogation]
  - text:
      zh: '**残骸调查 + 英方一手审讯的物证口径**：可见舰体上只有 2 处 320 mm 主装甲带被完全穿透，都在右舷舯部；主装甲带与装甲甲板全程未被击穿。英方审讯记战俘一致供称「no shells penetrated the armour belt」（除一名下级军官外）。这是「自沉说」最重要的物证（但穿透数量取决于能否看清被泥掩埋的部分）。多名战俘还认为炮战结束时若没有最后的鱼雷与自沉，舰仍可能开回港。'
      en: 'Wreck survey: only two complete penetrations of the 320 mm main belt, both on the starboard side amidships; neither belt nor armoured deck was pierced through. Prisoners interrogated by the Admiralty agreed that no shells penetrated the armour belt. This is the strongest physical evidence for the scuttling argument.'
    src: [kbismarck-last-battle, kbismarck-wreck, admiralty-bismarck-interrogation]
  - text:
      zh: 炮弹发射总数：本次战斗四舰合计 2,876 发（罗德里号 40.6 cm 380、英王乔治五世号 35.6 cm 339、诺福克号 20.3 cm 527、多塞特郡号 20.3 cm 254、罗德里号 15.2 cm 716、英王乔治五世号 13.3 cm 660）。罗德里号自己的炮术报告只给 16 英寸 378 发、6 英寸 706 发——**378 与 380、706 与 716 是同一批数字的两个版本**。
      en: 'Total rounds fired in the final action: 2,876 (Rodney 380 × 40.6 cm, KGV 339 × 35.6 cm, Norfolk 527, Dorsetshire 254, Rodney 716 × 15.2 cm, KGV 660). Rodney''s own gunnery report gives 378 × 16-inch and 706 × 6-inch — the same expenditure recorded two ways.'
    src: [kbismarck-last-battle, kbismarck-rodney-report, kbismarck-patterson-report, kbismarck-admiralty-war-diary]
  - text:
      zh: 命中数：**永远无法确知**。kbismarck 的原话是「200、300，也许更多？」；英方维基记「四舰共发约 2,800 发、命中约 400 发」。见争议 2。
      en: 'The number of hits can never be established: specialist estimates range from 200–300 to about 400 out of roughly 2,800 rounds fired.'
    src: [kbismarck-last-battle]
```

## 2.2 `consequences[]`

```yaml
consequences:
  - text:
      zh: 舵机被毁是整场追击的转折点：两舵卡死后，俾斯麦号只能兜圈、被西北风顶向追击的英舰，5-26 夜至 5-27 晨只以 7 节左右前进，从 5-26 的 24 节一路掉到决战时的 7 节。**舵角三种口径**：向左 12°（kbismarck）、左舵 15°（Junack）、10–15°（英方一手审讯，并称舰「向右缓慢转圈」）——见争议 5。
      en: 'The wrecked steering was the turning point of the chase: with both rudders jammed Bismarck could only circle and was forced up into the north-west wind towards her pursuers, dropping from 24 knots to about 7. The jam angle is given as 12°, 15°, or 10–15° (the last with her turning slowly to starboard).'
    src: [kbismarck-chase, kbismarck-histoperi, kbismarck-admiralty-war-diary, admiralty-bismarck-interrogation]
  - text:
      zh: 5-26 夜德方仍有战斗力：03:53 英方报告它「仍能进行沉重而准确的射击」，一发炮弹削掉 Cossack 的天线，另三发跨射 Zulu 伤 3 人。
      en: 'She remained dangerous through the night: at 0353 the British reported heavy and accurate fire; one shell carried away Cossack''s antenna and three straddled Zulu, wounding three.'
    src: [kbismarck-admiralty-war-diary]
  - text:
      zh: 5-27 决战中火控被逐层剥离：09:02 前桅测距仪失效 → 09:08 前指挥所与两座前炮塔失效、火控转后 → 09:13 后指挥所被毁 → 09:21 Dora 自爆失效 → 09:31 Cäsar 最后一击。此后只剩局部控制的零星副炮。
      en: 'Fire control was stripped layer by layer: foretop rangefinder at 0902, forward command post and both forward turrets at 0908, after command post at 0913, Dora at 0921, Cäsar''s last salvo at 0931.'
    src: [kbismarck-histoperi, kbismarck-last-battle]
  - text:
      zh: 通信中断：07:10 之后德方再未收到该舰任何电报；德方 09:15、10:56、11:23、11:52、12:10 的询问全部无回复，Group West 从路透社报道确认其已沉没。
      en: 'After 0710 nothing more was heard from her; Group West''s signals at 0915, 1056, 1123, 1152 and 1210 went unanswered and the report was confirmed from a Reuters bulletin.'
    src: [kbismarck-ktb]
  - text:
      zh: 舰体向左翻覆、舰艉先沉，舰旗仍在飘扬。Tovey 战后评语：「most gallant fight against impossible odds worthy of the old days of the Imperial German Navy, and she went down with her colours flying.」英方一手审讯同记「Bismarck sank, **with her colours flying**, at 1037 in position 48°09'N, 16°07'W, close to where the final action had started」；多塞特郡号 1107B 电报亦记「She had ceased firing but her colours were still flying」。
      en: She capsized to port and sank stern-first with her colours still flying, prompting Tovey's tribute to "the old days of the Imperial German Navy"; the Admiralty interrogation likewise records that she sank colours flying at 1037 in 48°09'N 16°07'W.
    src: [kbismarck-admiralty-war-diary, admiralty-bismarck-interrogation]
  - text:
      zh: 英方代价：主力舰与巡洋舰无伤亡、无损伤；Cossack、Zulu 轻微损伤与少数伤亡，Sikh 一人落海失踪。Sheffield 被破片伤 12 人（3 人后死）。5-28 返航途中 Mashona 被 He 111 炸沉，46 人阵亡。
      en: 'British cost: no casualties or damage in the capital ships or cruisers; slight damage and a few casualties in Cossack and Zulu, one man lost overboard from Sikh; Sheffield lost three men later; on 28 May Mashona was sunk by bombers with 46 dead.'
    src: [kbismarck-admiralty-war-diary, kbismarck-chase]
```

## 2.3 `losses[]`

```yaml
losses:
  - side: axis
    ships_lost: { zh: 俾斯麦号（自沉与战损复合，见争议 1）, en: Bismarck (scuttled and/or sunk by battle damage) }
    killed: 约 2200
    survivors: 114
    note:
      zh: >
        生还人数三种口径并列：**114**（英方维基）／**115**（Junack 回忆、kbismarck 正文「2,200 余名官兵仅 115 人生还」）／**116 被活救**（kbismarck 脚注：多塞特郡 86 + 毛利人 25 + U-74 3 + Sachsenwald 2）。
        差额来自 Maschinengefreiter Gerhard Lüttich——被救起但 1941-05-28 伤重死于多塞特郡号上，5-28 以全军训礼海葬。故「被救 116、生还 115、返国 109」三者可以同时成立。
        编制 2,220 人（2,092 舰员 + 128 舰队参谋），另加 100 余名编外人员（训练支队、电影组等），**确切死亡数未知**。
        **第三说（英方一手审讯）**：C.B. 4051 (24) 记「total number on board was given as between 2,300 and 2,400 ... more than 100 officers」——即舰上总数 2,300–2,400、军官 100 余名。此数与德方 2,220 + 编外人员的算法相容，但**没有一份来源给出确切总数**，故 killed 只能写「约 2,200」。
        100 名军官中仅 2 人获救。沉没前约 800 人离舰，其余随舰沉没；水温约 13 ℃。
      en: >
        Survivor counts differ: 114 / 115 alive, or 116 picked up (Dorsetshire 86 + Maori 25 + U-74 3 + Sachsenwald 2), the difference being Lüttich, who died aboard Dorsetshire on 28 May.
        Complement was 2,220 (2,092 crew + 128 fleet staff) plus over 100 supernumeraries; the Admiralty interrogation (C.B. 4051 (24)) was told the total on board was "between 2,300 and 2,400 ... more than 100 officers". No source gives an exact total, so exact casualties are unknown. Only two of about 100 officers survived.
    src: [kbismarck-last-battle, kbismarck-last-hours, kbismarck-admiralty-war-diary, admiralty-bismarck-interrogation]

  - side: allies
    ships_lost: { zh: 无（5-27 决战中）; 5-28 损失驱逐舰 Mashona, en: none in the final action; destroyer Mashona lost on 28 May }
    killed: 0
    survivors: null
    note:
      zh: >
        决战本身英方阵亡 0：两艘战列舰与两艘重巡无伤亡。驱逐舰有少数破片伤（Sheffield 12 伤、3 人后死；Sikh 1 人落海失踪）。
        若把 5-26 至 5-28 全期算进去，英方维基给「49 killed / 5 wounded / Mashona scuttled」——**这个 49 是全期合计，不是 5-27 炮战的**。
      en: >
        No British deaths in the action itself. The figure of 49 killed covers the whole operation through 28 May, including the loss of Mashona.
    src: [kbismarck-admiralty-war-diary, kbismarck-chase]
```

---

# 第三部分：争议点清单（并列，不裁决）

### 争议 1：她到底是怎么沉的 —— 五种说法

| # | 说法 | 持论者 | 依据 |
|---|---|---|---|
| 1 | **英军炮火/鱼雷击沉** | 1941 年英方公报、丘吉尔在下院的说法、部分英方战报叙述 | 5-27 公报(B) 明写「Dorsetshire 受命以鱼雷击沉，Bismarck 于今晨 11.01 沉没」；5-29 公报「炮火使其沉默」；Tovey 战报第 88 段称其「at the end of this she was in a sinking condition」。**注意 Tovey 本人同时说多塞特郡的最后鱼雷「only hastened her end」——即他也承认炮火已足够。** |
| 2 | **自沉（舰员主动打开通海阀 + 爆破装药）** | Junack（最高生还轮机军官）回忆、Müllenheim-Rechberg、德国海军传统叙事、Cameron 2002 残骸调查 | Junack 记 10:15 接到轮机长「准备沉舰」令、装 9 分钟引信，作为在场最高军官下令弃舰；离舰后**从舰腹看出舰壳未被鱼雷损伤**；残骸只见 2 处主装甲带穿透，装甲带与装甲甲板未被击穿；Cameron 等 2002 结论「WHO SANK THE BISMARCK – The British or the Germans? We are convinced the answer is ... BOTH!!」但仍认定「Bismarck unquestionably would have sunk due to progressive flooding hours after the battle ended」 |
| 3 | **两者皆是（战损使她必沉，自沉只是提前几分钟到数小时）** | Cameron/Dulin/Garzke/Jurens/Smith 2002 残骸取证分析、英方维基的现行表述、kbismarck 也倾向此说 | 同上的残骸证据 + 5-27 上午她已进水、倾侧、失控；英方维基导言：「most experts agree that the accumulated battle damage would have caused the Bismarck to sink eventually」 |
| 4 | **修正说：自沉「只加速了几分钟」甚至无关** | David L. Mearns（2001 年率 Northern Horizon 队调查）一派 | 主张战损本身已足以在很短时间内使她沉没，自沉的实际影响被夸大。**本文未能取得 Mearns 原始报告文本**，此说仅作为「存在这一派」记录，试过的 URL 见文末「未获取清单」 |
| 5 | **德国官方口径：成为优势兵力之牺牲品（Opfer der Übermacht），完全不自沉** | 1941-05-27 晚柏林国防军最高统帅部公告；Bismarck 战争日志（KTB）结语 | KTB 原文：「Das Schiff ist in heldenmütigem Kampfe der Übermacht des Gegners zum Opfer gefallen, nachdem es am Abend vorher durch einen unglücklichen Treffer seine Manövriereigenschaften eingebüßt hatte.」＝该舰在前一晚因一次不幸的命中丧失机动性后，于英勇战斗中成为敌方优势兵力之牺牲品。**通篇未提自沉，也把 5-26 的雷击写成「一次不幸的命中」淡化处理。** 1941 年的德方公告还称击沉了 Hood、击伤了英王乔治五世号。 |

**第 6 条旁证（不是「说法」，是英方一手审讯的措辞，直接影响 1/2/3 的权重）**：

英海军部《GERMAN BATTLESHIP BISMARCK — Interrogation of Survivors》（C.B. 4051 (24)，1941 年 8 月，SECRET）原文：

> "The actual cause of sinking is still a matter of dispute among survivors. There is however a considerable body of evidence to support the view that the inevitable end of the Bismarck was hastened by the explosion of specially prepared scuttling charges."

关键点有三条，都出自这份审讯：
- 战俘供称收到了明确口令：「Abandon ship. Ship is to be sunk!」「Clear ship for scuttling; apply explosive charges.」有专门的自沉队引爆炸药（「some at the sea-water inlets and discharges, others in the turbine rooms, boiler rooms and auxiliary machinery rooms」），全部水密门与注水阀敞开；**炸药引爆后约十分钟沉没、向左翻覆、螺旋桨仍在转**。
- 「It is alleged that the 'abandon ship' order never reached many parts of the ship.」——与幸存者「无一人听到弃舰令」的证词互证。
- **物证口径**：「All prisoners, with the exception of one junior officer, state that no shells penetrated the armour belt.」唯一例外者称一发炮弹在舰桥下方或略前方穿透并在舰内爆炸。多名战俘认为炮战结束时**若没有最后的鱼雷与自沉，舰仍可能开回港**。

→ 这份审讯既不支持纯「炮火击沉」，也不支持「自沉无关」，它的措辞是 **hastened**（加速）——与第 3 说最接近，但把自沉的作用限定为「加速不可避免的结局」。

来源：`admiralty-bismarck-interrogation`

### 争议 2：命中数到底是 200–300 还是 400+

- **200–300（甚至更多，无法确定）**：kbismarck `bismarck-last-battle.html` 原文「The number of hits will never be known. 200, 300, maybe more?」——它同时给出本次战斗共发射 2,876 发。
- **约 400**：英方维基「四舰合计约 2,800 发、命中约 400 发」。
- **不可调和的物理原因**：大量命中落在无装甲的上层建筑与舷侧，观察者只能记「多次命中」；Rodney 的炮术报告只记自己打了多少发、不记命中；德方无一幸存者能统计。**建议正式文件把「发射数」作为可信数据、把「命中数」明确标为争议区间（约 200–400）。**
- **英方一手审讯的反向证据**：战俘一致供称「no shells penetrated the armour belt」（除一名下级军官外），意即哪怕命中数高达数百，**落在装甲带上的命中为零**；这与「上层建筑被打成筛子、舰体本身仍浮着」的目击描述一致，也是为什么「命中数」与「沉没原因」必须分开讨论。来源：`admiralty-bismarck-interrogation`

### 争议 3：Lindemann 何时死亡

- **09:02，与 Lütjens 及舰桥其余人员同时**：kbismarck 与英方维基都记，一发 Rodney 16 英寸齐射命中前上层建筑、毁舰桥与主火控指挥仪，「据幸存者称」很可能同时炸死 Lindemann、Lütjens 与舰桥人员。
- **较晚，甚至沉没时仍在舰上**：另有幸存者证词称沉没前还看见 Lindemann 在甲板上（英方维基同段并列了这条）。
- **四种说法并列（英方一手审讯的版本）**：C.B. 4051 (24) 明写「Of the end of the Admiral and Captain nothing definite is known.」，随后并列三条互斥证词：
  1. 部分战俘称从水中看见二人**并肩站在舰首楼**，向水中的人挥手直至下沉；
  2. Müllenheim-Rechberg 称一名水兵报称二人**站在舰桥上**随舰下沉；
  3. 另一名军官战俘认为二人**在舰桥被 Rodney 炮弹命中时即已阵亡**（≈ 上条 09:02 说）。
  → 加上「看见他在甲板上」，实际至少有 4 种，且**没有任何一种有一手文件支持**。
- **档案层面无解**：KTB 结语明写「无一幸存者看见其沉没」「幸存者证词……不足以说明其最后时刻」；德方 6-14 的审讯呈文（Naval Group Command West B.Nr. g.Kdos. 3156/41）也自述「The actual sinking was not witnessed by any of the survivors」。**100 名军官中仅 2 人获救，是这个问题无解的直接原因。**
- 来源：`kbismarck-last-battle`、`wiki-en-last-battle`、`kbismarck-ktb`、`kbismarck-debriefing`、`admiralty-bismarck-interrogation`

### 争议 4：英舰是否在最后阶段停止射击、为什么停

- **停了，但理由不是人道**：Tovey 明写「燃油极度短缺（KGV 仅剩 1,200 吨 / 32%）」「进一步炮击也不会加速其沉没」「须考虑近失弹或鱼雷损及燃油舱后停在 U 艇集结区的风险」，故 10:15–10:28 之间中止战斗，并令仍有鱼雷的舰只使用。KGV 自己的记录是 10:21 停火。
- **没完全停**：多塞特郡号在主炮停火后继续用鱼雷（10:22 两枚、10:36 一枚）；多份材料强调「四艘英舰在整个自沉过程中一直在射击」（英方维基导言原话）。
- **Patterson（KGV 舰长）的补充**：他写道若早看到有人从后甲板跳海就会下令停火，但他没看到；他确实在 10:10–10:15 看到跳海者、白色维利弹与主桅倒塌。
- **英方一手审讯的第三口径**：C.B. 4051 (24) 写「As further gunfire would not hasten her end, Commander-in-Chief, Home Fleet, decided to discontinue the gun action and **fire ceased at 1022**」——注意它给的是 **10:22**，比 Tovey 的 10:28（中止决定）与 Patterson 的 10:21 都不同；同一份文件又说多塞特郡「**having hit with three torpedoes**」，即英方自己认定雷击 3 发全中。
- 来源：`hmshood-tovey-dispatch`、`kbismarck-admiralty-war-diary`、`kbismarck-patterson-report`、`wiki-en-last-battle`、`admiralty-bismarck-interrogation`

### 争议 5：命中艉部的那枚鱼雷来自左舷还是右舷

- **左舷艉部**：kbismarck `histoperi.html` 与多数早期叙述；Junack 记「第二雷使左舵卡在 15°」。
- **右舷艉部 frame 10.5–14.5**：kbismarck `bismarck-chase.html` 正文与脚注 7 明确说「命中艉部之雷来自左舷还是右舷长期有争议，**最新残骸分析倾向右舷**」。
- **英方一手审讯站在右舷一边**：C.B. 4051 (24) 原文「One torpedo had struck amidships on the port side, one on the **starboard quarter**, and possibly a third on the port quarter」，并记该雷「wrecked the steering gear jamming the rudders at an angle variously estimated at between 10 and 15 degrees and causing Bismarck to turn slowly in circles to **starboard**」。某战俘进一步称该雷在「右舷舵机舱下方无装甲配平舱外侧」爆炸，II 段淹至主甲板。
- **舵角也分歧**：10–15°（审讯报告、Junack 记 15°）对 12°（kbismarck `histoperi`）。转向方向同样分歧：向右（审讯报告）对向左（多数二次叙述）。
- 来源：`kbismarck-chase`、`kbismarck-histoperi`、`kbismarck-last-hours`、`admiralty-bismarck-interrogation`

### 争议 6：夜间驱逐舰鱼雷到底有没有命中

- **有，2–3 发**：英方公报(B)、Tovey 战报第 74 段（Cossack、Maori 各命中，Maori 那枚引起舰首起火，Sikh 可能也命中）、Admiralty War Diary 的 0122–0146 逐条电报（Maori「One hit confirmed. Fire on forecastle」）、Patterson 报告。
- **没有，0 发**：Admiralty War Diary 同页即注明「Bismarck 的 senior surviving officer 称驱逐舰鱼雷无一命中」；德方 KTB 的幸存者证词也称未观察到鱼雷或火炮命中。Tovey 第 88 段仍把「5-27 晨驱逐舰鱼雷两发」计入其损伤序列——**英方最高层也接受了「有命中」**。
- 旁证支持「未命中」：德舰在 02:40–03:40 之间仍前进了 8 英里、03:53 仍能准确射击，与「吃了 2–3 枚鱼雷」的状态不符。
- **英方一手审讯也不支持驱逐舰命中**：C.B. 4051 (24) 的整条损伤序列只列「5-24 炮火 3 发、5-25 一雷、5-26 两雷、Rodney 鱼雷一发 + 其后炮火重击」，驱逐舰鱼雷不在其统计内；且明写「All Home Fleet ships had expended their torpedoes, **including Rodney, who had scored one hit**」——英方自己把鱼雷战果归给 Rodney，不归给驱逐舰。
- 来源：`hmshood-tovey-dispatch`、`kbismarck-admiralty-war-diary`、`kbismarck-ktb`、`kbismarck-patterson-report`、`admiralty-bismarck-interrogation`

### 争议 7：Lütjens「将战至最后一发炮弹」电报的时刻

- **21:40**：kbismarck `histoperi.html`、`bismarck-last-battle.html`（德方电报时间组口径）。
- **23:40**：英方维基。
- **2358/2359 组（记录时刻 00:32/00:34）**：KTB 另记该夜另有致希特勒电（2358 组）与「武备机械完好，但无法用主机操舵」（2359 组）——**即「战至最后一发炮弹」这句在一夜之间发过两次以上，或至少被记了两次**，这是三个时刻并存的原因之一。
- 转写误差还是时区差，本文无法判定；三个时刻都记录在案。
- 来源：`kbismarck-histoperi`、`kbismarck-last-battle`、`kbismarck-ktb`、`wiki-en-last-battle`

### 争议 8：沉没时刻与坐标（同一件事四个版本）

| 项目 | 值 | 来源 |
|---|---|---|
| 沉没时刻 | **10:37** | Tovey 战报第 86 段；**英方一手审讯 C.B. 4051 (24) 亦记 1037**（两者独立，但都源自英方同一系统） |
| | **10:36** | Patterson（KGV 舰长）报告 |
| | **10:39** | kbismarck `histoperi` / `bismarck-last-battle`（沉没点 BE 5336 方格） |
| | **10:40** | 英方维基 |
| | **11:01** | 英海军部对外公报、Admiralty War Diary 1101B、多塞特郡 1039/27 电报「Enemy is sunk」（对外公布口径，非目击时刻） |
| | **10:22（停火）/ 10:28（中止战斗）** | 英方一手审讯记停火 10:22；Tovey 战报记 10:28 决定中止；Patterson 记 10:21 停火 —— 见争议 4 |
| 沉没坐标 | **48°09'N 16°07'W** | Tovey 战报、Admiralty War Diary、kbismarck |
| | **48°10'N 16°12'W** | Patterson 报告（并记水深 2,500 英寻）、英方维基信息框 |
| 水深 | **2,500 英寻（约 4,570 m）** | Patterson 报告 |
| | **4,790 m（15,700 ft）** | 1989 年 Ballard 队实测（残骸实际位置，比推算沉没点更可靠） |

### 争议 9：Rodney 的炮弹消耗 378 还是 380

- **378 发 16 英寸 / 706 发 6 英寸**：Rodney 自己的《Preliminary Gunnery Report》（enclosure "E"，1941-07）。
- **380 / 716**：kbismarck、Admiralty War Diary 的返港补给申请、Patterson 报告（“I understand Rodney fired 380 rounds of 16-inch and 716 of 6-inch”）。
- 同一份 Rodney 报告内部也有算术不一致：B 塔三根炮管分计 45 + 44 + 52 = 141，塔总计却写 144。

### 争议 10：5-26 空袭命中的鱼雷数

- **2 枚**：Tovey 战报（「At least two hits were scored」）、kbismarck `bismarck-last-battle`、英方一手审讯（「at least two, and possibly three hits were made」的保守读法）。
- **2 枚、可能 3 枚**：1942 年官方出版物《Coastal Command》（`its-the-bismarck.html`，tier B）正文写「取得两枚、可能三枚命中」，且书中**脚注自我更正**了正文另外两处错误（「驱逐舰那晚并未命中 Bismarck」；「实际上那些过时的 Swordfish 一架也没被击落」）——引用该书时必须以脚注为准；kbismarck `histoperi`；英方一手审讯原文（「One torpedo had struck amidships on the port side, one on the starboard quarter, **and possibly a third on the port quarter**」）。
- **英方公报口径**：「一雷命中舯部，第二雷命中右舷艉部」——**注意公报说艉部命中在右舷，与多数叙述的左舷相反**，这一点与一手审讯一致（见争议 5）。
- **攻击时长也分歧**：20:47 起算（kbismarck `chase`）对 20:55–21:25（英方一手审讯）。德方 KTB 按幸存者证词记为「约 2030」开始、且声称击落 7 架——**与英方 15 架、零损失直接冲突，KTB 自己已注明英方记载不同**。
- 来源：`hmshood-tovey-dispatch`、`kbismarck-last-battle`、`kbismarck-histoperi`、`kbismarck-its-the-bismarck`、`kbismarck-communiques`、`kbismarck-chase`、`admiralty-bismarck-interrogation`、`kbismarck-ktb`

### 争议 11：5-26 第一波空袭 Sheffield 的鱼雷数（11 还是别的）

- **11 枚**：Tovey 战报（2 枚入水即爆、3 枚横穿尾迹时爆、其余 6 枚被规避）。
- kbismarck `chase` 记为同一组 11 枚、同样三种归宿，两处一致。**这一条其实没有争议，列出是为了防止有人把「15 架飞机」误当成「15 枚鱼雷」。**

### 争议 12：Bismarck 的第一枚中弹在 08:57 还是 09:02

- **09:02**：kbismarck `last-battle` / `histoperi`、Patterson 报告（「at 0902 the Bismarck was seen to be hit」）——口径为「首发命中即摧毁前桅测距仪那一发」。
- **08:57**：英方一手审讯（C.B. 4051 (24)）：「At 0851 Rodney had straddled Bismarck but it was not until **0857**, according to prisoners, that Bismarck sustained her first hit.」——即战俘把首弹记在 08:51 跨射之后 6 分钟。
- **差 5 分钟的原因**：英舰报告按目击落弹时刻记，战俘按舰内感受/传令时刻记；两者无需强行统一。

### 争议 13：Dorsetshire 的鱼雷命中数（3 说并存）

- **右舷 2 枚全中、左舷 1 枚命中（共 3）**：kbismarck `last-battle`（10:22 两枚「均命中无明显效果」、10:36 一枚命中）、英方一手审讯（「having hit with three torpedoes」）。
- **先右舷 2 枚其一命中、再左舷 1 枚命中（共 2）**：英方维基（并注明残骸检查显示最后一雷似在左舷上层建筑处爆炸）。
- **只有最后那几枚「加速了结局」**：Tovey 战报第 88 段措辞「the final torpedoes from the Dorsetshire only hastened her end」——不确认数量。
- 三说都保留；共同点是**至少 2 枚命中，且都在主炮停火之后**。

### 争议 14：救援人数（三套数字互相冲突）

| 数字 | 来源 | 说明 |
|---|---|---|
| 多塞特郡 86 + 毛利人 25 = **111**（另计 U-74 3 + Sachsenwald 2，共 116 被活救） | kbismarck `last-battle` 脚注 | 最细的一套 |
| 多塞特郡 **4 军官 + 75 兵 = 79** + 毛利人 **24** = **103** | Tovey 战报第 87 段 | 英方正式战报口径 |
| 多塞特郡与毛利人合计「**over 100**」 | Admiralty War Diary 27 日、「More than one hundred officers and men」英海军部 5-29 公报 | 对外模糊口径 |
| 多塞特郡 **110 人（含 4 军官）** 上舰后中止救援；另称「German fishing vessel Sachsenwald 又救起 100 人」 | 英方一手审讯 C.B. 4051 (24) | **「Sachsenwald 救 100 人」与 Sachsenwald 舰长报告「只救 2 人」严重冲突，应视为审讯报告的错记或泛指；Canarias 只找到「约一百具浮尸」** |
| 「水中约 400 人，仅约 85 人获救」 | Junack 回忆 | 当事人视角，含「瞭望判断错误、附近并无 U 艇」 |

→ **建议正式文件采用「多塞特郡 85–86 + 毛利人 24–25，合计约 110；U-74 又救 3、Sachsenwald 又救 2」这个区间，并明确注明「英方一手审讯关于 Sachsenwald 的数字不可用」。**

---

# 第四部分：来源缩写 → URL 对照表

标记说明：**已登记** = 已在 `data/sources.yaml` 里，可直接作 `src`；**待登记** = 本次新抓，需 lead 补登后才能进正式 YAML。

## 4.1 已登记（可直接引用）

| 缩写 | 登记 id | tier | URL | 备注 |
|---|---|---|---|---|
| `[LB]` | `kbismarck-last-battle` | D | https://www.kbismarck.com/bismarck-last-battle.html | 决战逐分钟叙述 + 弹药统计 + 德国官方公告全文 + 生还人数脚注 |
| `[CH]` | `kbismarck-chase` | D | https://www.kbismarck.com/bismarck-chase.html | 追击全程；含 5-26 两波空袭细节、误击 Sheffield 的 11 雷去向、鱼雷命中舷侧之争的脚注 7 |
| `[H]` | `kbismarck-histoperi` | D | https://www.kbismarck.com/histoperi.html | 生涯逐日时间线；5-26/27 每个时刻最完整的一份 |
| `[W]` | `kbismarck-wreck` | D | https://www.kbismarck.com/wreck.html | 残骸位置/深度/探访年表/德政府立场 |
| `[ROD]` | `kbismarck-rodney-report` | A | https://www.kbismarck.com/rodney-gunnery-report.html | Rodney 炮术报告原文（378 / 706、各塔分计、X 塔 28 次不能瞄准、失效火炮） |
| `[LH]` | `kbismarck-last-hours` | A | https://www.kbismarck.com/bismarck-last-hours.html | Junack 回忆（10:15 接令、9 分钟引信、翻覆方向、救援瞭望判断错误） |
| `[KTB]` | `kbismarck-ktb` | A | bs-ktb.zip（本地 `work/raw/ktb/bs-ktb.txt`，177 页英德对照） | 德方战争日志；末页给出官方口径原文与「无一幸存者看见其沉没」 |
| `[DEB]` | `kbismarck-debriefing` | A | https://www.kbismarck.com/archives/debriefing.html | 德方 1941-06-14 对 5 名获救者的审讯呈文（Naval Group Command West B.Nr. g.Kdos. 3156/41） |
| `[NAV16]` | `navweaps-16in-45-mk1` | D | navweaps.com（走代理） | 16"/45 Mark I：弹重 929 kg、初速 788/797 m/s、备弹 95+10 |
| `[NAV14]` | `navweaps-14in-45-mk7` | D | navweaps.com（走代理） | 14"/45 Mark VII：弹重 721 kg、初速 757/732 m/s、备弹 100 |
| `[NAV8]` | `navweaps-8in-50-mk8` | D | navweaps.com（走代理） | 8"/50 Mark VIII：弹重 116.1 kg、初速 855 m/s |
| `[NAV6]` | `navweaps-6in-50-mk23` | D | navweaps.com（走代理） | 6"/50 Mark XXIII：弹重 50.8 kg、初速 841 m/s、6–8 发/分 |
| `[WP]` | `wiki-en-last-battle` | E | https://en.wikipedia.org/wiki/Last_battle_of_Bismarck | **仅作线索，不作 fact src** |

## 4.2 待登记（本次新抓，全部已落地为纯文本，在 `work/raw/` 下）

| 缩写 | 建议 id | tier | URL | 本地文件 | 内容 |
|---|---|---|---|---|---|
| `[PAT]` | `kbismarck-patterson-report` | A | https://www.kbismarck.com/patterson-bismarck-report.html | `lb-patterson.txt` | **KGV 舰长 W. R. Patterson 战报**（1941-06-17，No. 4099/192）：四阶段、0848 开火 24,600 码、A/Y/B 塔故障、3,000 码三发可见命中、14 英寸 339 发、5.25 英寸 600 发、48°10'N 16°12'W |
| `[GUE]` | `kbismarck-guernsey-report` | A | https://www.kbismarck.com/guernsey-bismarck-report.html | `lb-guernsey.txt` | KGV 上 Lt.Cdr. Hugh Guernsey 目击记（非正式报告，文学性） |
| `[CAT]` | `kbismarck-catalina-reports` | A | https://www.kbismarck.com/catalina-reports.html | `lb-catalina.txt` | **Catalina Z/209 与 M/240 的 5-26 原始电报全文**（Enclosure No.3 to F.O.C. Force H No. 471/14） |
| `[SMITH]` | `kbismarck-smith-report` | A | https://www.kbismarck.com/smithreport.html | `lb-smith.txt` | **美海军少尉 Leonard B. Smith 的搜索报告**（CNO Intelligence Division Serial 1066，1941-06-09）：0325 起飞、1010 发现、投弃 4 枚深弹、2 处弹孔 |
| `[CC]` | `kbismarck-coastal-command` | B | https://www.kbismarck.com/coastal-command-bismarck.html | `lb-coastal.txt` | 《London Gazette》1947-10-14 增刊：海岸司令部 69 架次 580 小时；1030 发现、1039 云层破开被击中 |
| `[AWD]` | `kbismarck-admiralty-war-diary` | A | https://www.kbismarck.com/admiralty-war-diary.html | `lb-admiralty-diary.txt`（107,139 字符；26 日节 `_tmp/adm-26.txt`、27 日节 `_tmp/adm-27.txt`） | **英国海军部战争日志 5-26/27 全部电报**（原件藏 US NARA）：0122–0146 驱逐舰逐条、1028 中止、1039「Enemy is sunk」、1101B 沉没位置、1107B「both sides」 |
| `[TOV]` | `hmshood-tovey-dispatch` | A | http://www.hmshood.org.uk/reference/official/adm234/adm234-509tovey.htm | `_tmp/tovey.txt`（83,722 字符） | **Tovey 战报 ADM 234/509**（No. 896/H.F. 1325，1941-07-05）：91 段正文 + KGV 航迹附录；燃油、误击 Sheffield 的 11 雷、第 88 段损伤序列、救援数字、1037 沉没 |
| `[SACH]` | `kbismarck-sachsenwald-report` | A | https://www.kbismarck.com/sachsenwald-bismarck-report.html | `lb-sachsenwald.txt` | 德国气象船 Sachsenwald 舰长 Schütte 报告（1941-05-30 海上）：2235 见 3 颗红色信号弹、2245 救起 Maus 与 Lorenzen、5-30 0045 与 Canarias 会合 |
| `[COMM]` | `kbismarck-communiques` | B | https://www.kbismarck.com/british-communiques.html | `lb-communiques.txt` | 英海军部 5-24/25/26/27/29 公报全文（11.01 沉没、More than one hundred 被俘、Mashona 沉没） |
| `[ITB]` | `kbismarck-its-the-bismarck` | B | https://www.kbismarck.com/its-the-bismarck.html | `lb-itsbismarck.txt` | 1942 年官方出版物《Coastal Command》第一章（含两处自我更正脚注：驱逐舰那晚并未命中 / Swordfish 一架未损失） |
| `[INT]` | `admiralty-bismarck-interrogation` | A | https://www.uboatarchive.net/Int/BismarckINT.htm | `lb-uboat-int.txt`（229,668 字符） | **英海军部《GERMAN BATTLESHIP BISMARCK — Interrogation of Survivors》，C.B. 4051 (24)，1941-08，SECRET**。争议 1/3/5/6/10/12/13/14 的一手旁证：自沉令原文与「hastened」措辞、装甲带未被穿透、Lindemann/Lütjens 之死的三种互斥证词、艉部雷在**右舷**、首弹 0857、停火 1022、多塞特郡「三雷全中」、编制 2,300–2,400。**注意其「Sachsenwald 救 100 人」明显错记** |

> **抓取方式备忘（给 lead 和下一次采集）**：
> - navweaps.com、de.wikipedia.org **必须走代理 `http://127.0.0.1:7897`**。
> - `hmshood.org.uk` **必须直连 + 带 Referer `http://www.hmshood.org.uk/`**（走代理或被 403；Wayback 返回 429）。
> - kbismarck.com 直连可通，带浏览器 UA 更稳。
> - 工具：`work/raw/_tmp/grab2.py`（抓取，直连失败自动走代理）、`work/raw/_tmp/links.py`（抽真实 href）、`work/raw/_tmp/html2txt.py`（HTML→纯文本）。

## 4.3 未获取清单（说明试过什么）

| 想要的东西 | 状态 | 试过的 URL |
|---|---|---|
| Norfolk 的 action report（ADM 原文） | **未获取** | kbismarck `archives/index.html` 索引内无此件；`admiralty-war-diary.html` 只含电报摘要。**建议下一步查 UK National Archives Discovery（ADM 234/509 同卷附件）**——本次未尝试，因需付费下载。 |
| Dorsetshire 的 action report | **未获取** | 同上。舰长 Benjamin C. S. Martin 的报告不在 kbismarck 档案里；仅有 Admiralty Diary 的 1107B 电报「I torpedoed BISMARCK both sides before she sank」 |
| Rodney 战报中的「命中记录」部分 | **未获取** | `rodney-gunnery-report.html` 只有 Preliminary Gunnery Report 的统计段，无逐次命中记录。同一档案目录下的 "Rodney's report" 完整版未找到 |
| Mearns 2001 年残骸调查报告原文 | **未获取** | 只在 `bismarck-last-battle` 的参考文献里见到转述。未尝试第三方镜像，因版权不明 |
| de.wikipedia「Letztes Gefecht der Bismarck」 | **未抓** | 代理可用但未抓（英方一手材料已足够；德方口径已由 KTB 与官方公告覆盖）。若需德方民间叙述可补 |
| 英方对获救者的审讯报告 ADM 267/137 全文（PDF） | **未抓** | 索引里有 `https://www.kbismarck.com/archives/survivor-reports.pdf`，本次未下载（PDF 需额外解析）。**但其内容已由 `https://www.uboatarchive.net/Int/BismarckINT.htm`（C.B. 4051 (24) 全文，229,668 字符）覆盖并已并入本文——这份是同一份英方审讯报告的纯文本版**。 |
| Sheffield 的火炮配置（本次来源未覆盖） | **未获取** | 本次抓取的 navweaps 页面只有 16"/14"/8"/6" Mark XXIII（Rodney 副炮）。Sheffield 属 Town 级轻巡，其 6 英寸炮型号**本文不作断言** |
| Rodney 赴波士顿修理的具体故障 | **未获取** | 只知「on her way to Boston for repairs」（`lb-chase.txt`）与「最高航速 21 节」「已被 KGV 追越」；具体是舵机、主机还是锅炉，`lb-chase` / `tovey` / `lb-lb` 均未写。**不得猜。** |
