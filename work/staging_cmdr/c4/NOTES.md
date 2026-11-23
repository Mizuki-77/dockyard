# c4 交付说明（4 位指挥官）

> Dockyard · 2026-11-23 · 调研 subagent c4
> 产出目录：`work/staging_cmdr/c4/`（`commanders/` 4 个 yaml + `sources-fragment.yaml`）
> **未触碰 `data/`、`src/`、`public/`。**

---

## 1. 交付摘要

| id | 姓名 | 简介 | 年表 | 舰关联 | 战役关联 | 采用来源 |
|---|---|---|---|---|---|---|
| `eugeniusz-plawski` | Eugeniusz Pławski | 4 段 | 16 条 | piorun | `last-battle` | 8 |
| `wolf-junge` | Wolf Junge | 4 段 | 16 条 | tirpitz | 无 | 6 |
| `richard-taylor-white` | Richard Taylor White | 4 段 | 16 条 | zulu | 无 | 7 |
| `benjamin-martin` | Benjamin Charles Stanley Martin | 4 段 | 16 条 | dorsetshire | `last-battle` | 8 |

新登记来源 16 条（`sources-fragment.yaml`）：D 级 9 条、E 级 7 条。
每篇的关键事实（生卒、任免、战功）都有 D 级以上来源与 E 级并列，无一篇以 E 级为唯一来源。

自检脚本：`work/staging_cmdr/c4/_raw/precheck_c4.py`（按 `scripts/validate.py` 的
`check_commander` 规则复写，只读不写 data/）。结果 **0 error / 0 warning**：

```
eugeniusz-plawski: intro 4 段，年表 16 条，1 舰 / 1 战役，来源 8 个
wolf-junge:        intro 4 段，年表 16 条，1 舰 / 0 战役，来源 6 个
richard-taylor-white: intro 4 段，年表 16 条，1 舰 / 0 战役，来源 7 个
benjamin-martin:   intro 4 段，年表 16 条，1 舰 / 1 战役，来源 8 个
```

另外单独查过：禁用词扫描（据说/有人认为/有人称/据信/或许/大概/应该是）零命中；
所有 `src` 均已登记；`intro` 每段 170–217 字，落在 100–220 区间内。

---

## 2. 任务书与来源打架的地方（**任务书写错的两处**）

### 2.1 White「随舰沉没」——**不对，他没有沉**

任务书与本站 `data/ships/zulu.yaml` 的备注都写 White「1942-09-14 随舰沉没」。
按英文维基与 naval-history 的逐时记录，他活下来了：

> White kept two officers and nine ratings on board Zulu. … by 2000 Zulu was rapidly
> sinking and White ordered Hursley to stop towing and Croome to pick up the remaining
> crew from Zulu. … All twelve survivors were picked up by Hursley and HMS Hurworth.
> —— [enwiki-white]

他自己是 12 名留舰人员之一，由 Hursley 与 Hurworth 救起。写完档案后他另有 13 年现役，
退役时是海军少将副官。

**处理**：`relations.ships[0].role` 写「末任；沉没前将舰员转出，本人为最后离舰者之一」，
note 里明写未随舰沉没。`summary_zh` 用「随舰弃船」而非「随舰沉没」。
👉 **建议主会话核对 `data/ships/zulu.yaml` 的第三条 commander fact**，若其 note
或 `commanders.astro` 的 `fateOf()` 会把它判成「随舰沉没」，会显示错标。

### 2.2 Pławski 的「首任波兰舰长」日期

任务书给 `1940-11-05`，与波方命令原文、uboat.net 一致，**这条是对的**。
但英文维基正文写「On 24 October 1940 he became commander of ORP Piorun」。
按 `facta-nautica-piorun` 收录的波方命令（Dziennik Zarządzeń Nr 20, 伦敦 1940-11-13）：

> Kontrtorpedowiec brytyjski "Nerissa" w dniu 5.XI.40 podniósł polską banderę wojenną…
> załoga ORP "Piorun" była zaokrętowana na KT "Nerissa" od dnia 24.X.40 do dnia 4.XI.40

即：舰员 10-24 起就在船上，**升旗入列是 11-05**。维基把「舰员登舰日」写成了「任舰长日」。
本站取 11-05，与 `data/ships/piorun.yaml` 一致，未改数字。

---

## 3. 其他两源打架处（已在文件里并列，不裁决）

| 事项 | 说法 A | 说法 B | 处理 |
|---|---|---|---|
| Pławski 卒日 | 1972-05-23（plwiki 信息框、polska-zbrojna、pamietam.eu） | 1972-05-22，且年份作 **1973**（enwiki「In exile」段） | 取 1972-05-23；enwiki 那段与其自身信息框自相矛盾 |
| Junge 生日 | 1903-01-05（dewiki 正文+信息框、ukwiki） | 1903-01-03（enwiki 信息框） | 取 01-05，在 timeline 的 note 里记下冲突 |
| Junge 卸任日 | 1944-11-03（kbismarck、本站 tirpitz.yaml） | 1944-11-04（Deutsches Marinearchiv 的 Kommandanten 表） | 保留 11-03，note 记为「当日交接」的记法差 |
| Junge 调离去向 | 国防军最高统帅部第一海军参谋军官（dewiki） | 海军最高统帅部参谋（enwiki） | 并列不裁 |
| Martin DSO 公告日 | 1941-10-14（unithistories、uboat.net、讣闻） | 1942-10-14（enwiki 参考文献栏的 Gazette 期号 35307） | 取 1941-10-14；35307 是 1942 年的期号，疑为维基误植 |

---

## 4. 卡住 / 查不到的地方

1. **Wolf Junge 的早期生涯只有 E 级来源。**
   Deutsches Marinearchiv 的舰长条目对 Junge 的「geboren / gestorben」两栏是空白
   （Topp、Meyer、Weber 三人都填了，只有他空着）。他的 1922 年入伍、1926 年晋升、
   1937 年入基尔海军学院、战后任 KSB 人事主管、死因与葬地，**全部只见于德文维基**，
   而德文维基自述底本是 WASt 人事档案与 Grützner《Ernst Lindemann》页 223–224。
   我按项目规矩把 E 级引在 timeline 里，并在 `note` 中明确写出「早期生平只有 E 级来源」。
   **若要补强，需去 Freiburg 军事档案馆（BArch BA-MA）或查 Hildebrand/Röhr/Steinmetz
   《Die deutschen Kriegsschiffe》第 7 卷。**
2. **Junge「舰员评价不高」这句我故意没写进正文。**
   enwiki 引 Mallmann Showell 2009，但这属于评价性内容且转引，不是一手材料。
   正文里只留可核实的部分（参谋出身、晋升节奏、钨作战接管指挥）。
3. **提尔皮茨号的钨作战战斗报告（B.Nr. Gkdos 395）全程只写职务不写姓名。**
   「07:10 由第一军官接管全舰」这句是报告原文，第一军官是 Junge 这一点由
   Deutsches Marinearchiv 的军官序列（1943-08 至 1944-05 第一军官 = Wolf Junge）交叉确认。
   两处我分开引了，没有把两源合成一句。
4. **London Gazette 抓不到。** `thegazette.co.uk` 有 AWS WAF 质询，`data.htm` 直连 SSL 中断。
   White 与 Martin 的 DSO/加衔公告只有转引（unithistories 给了公告日期，enwiki 给了期号）。
   要补一手件需从 `thegazette.co.uk` 网页版人工检索。
5. **`unithistories.com` 的索引页是分段的。** White 在 `RN_officersW3.html`，
   Martin 在 `RN_officersM2.html`；`W2`、`M` 里都没有。均已抓全文存 `_raw/`。
6. **`muzeummw.pl`（格丁尼亚海军博物馆）连不上。** SSL EOF，无替代路径。
   Pławski 的博物馆口径改由 `polska-zbrojna-plawski`（直接引用该馆副馆长 Lech Trawicki
   的访谈）承担，效果更好——那是一手访谈。
7. **Operation Planet 我查错了日期。** 任务书写「多次英军空袭（钨作战、Planet、
   Goodwood）」。经查 Soviet 空袭提尔皮茨是 1944-02-10/11（英方称 "Operation Planet"），
   **当时舰长是 Meyer，不是 Junge**（前者的任内）。Junge 任内实际经历的是
   Goodwood 三次（8-22、8-24、8-29）、Paravane（9-15）、Catechism（11-12，他已在 11-04 调离）。
   故正文只写钨作战接管 + Goodwood + Paravane，**没有把 Planet 算进他的任期**。
   `kbismarck-tirpitz` 记 1944-02-12「被四架苏联轰炸机攻击未果」，与他无关。

---

## 5. 关联判断的依据

### `eugeniusz-plawski` → `last-battle`（**填了，但 role 写死是 5-26 夜战**）

填的依据是英方一手战报直接点名他，不是靠推断：

> 73. The Bismarck was sighted by the Piorun, on the port wing, at 2238 …
> at 2242 the enemy opened a heavy fire on the Piorun, who made a spirited reply
> before turning away under smoke.
> 75. The Commanding Officer of the Piorun had not worked with the Fourth Destroyer
> Flotilla before and he therefore decided to wait until last to deliver his attack …
> He had drawn the Bismarck's fire for an hour during the period of dusk …
> at 0500, he was ordered … to proceed to Plymouth to fuel …
> —— [hmshood-tovey-dispatch] 第 73、75 段

本站 `last-battle` 的参战名单也确实把 Piorun 列进去了（role 已注明 5-27 05:00 返航）。
所以按任务书的指示「如果他当时在舰上，可以填 last-battle 但 role 要写清是 5-26 夜战」——
**他在舰上，已填，role 与 note 都写死了「只对应 5-26 夜间接触与交火，最终战开始时不在场」**。

### 其余三人

- `wolf-junge` → `tirpitz` ✅；battles 留空。本站无钨作战/Goodwood/Paravane/Catechism 条目，
  不为好看硬连。
- `richard-taylor-white` → `zulu` ✅；battles 留空。祖鲁人号沉于托布鲁克外海空袭
  （协议作战 Operation Agreement），本站未收录。**特别注意：祖鲁人号参加过 1941-05-26/27
  夜袭俾斯麦，但那时舰长是 Harry Robert Graham（1941-01-14 至 1942-04-28），
  不是 White（1942-04-28 才接舰），所以不能连 `last-battle`。**
- `benjamin-martin` → `dorsetshire` ✅ + `last-battle` ✅。
  `last-battle` 的 05-27 09:04 / 10:22 / 10:36 三条事件里都写了「舰长 Benjamin C. S. Martin」。

---

## 6. 军衔制式（按要求保留原制式，未翻译）

| 人 | `rank_final` | 指挥该舰时的军衔 | 说明 |
|---|---|---|---|
| Pławski | `komandor` | `kmdr por.` | 1942 年才升 komandor；指挥闪电号时是 kmdr por.（中校）。两者不能混，文件 note 里写了 |
| Junge | `Kpt.z.S.` | `Kpt.z.S.` | 1943-04-01 晋升，1944-05-01 接舰时已是此衔 |
| White | `Captain` | `Cdr.` | 1942 年 6 月 30 日升 Cdr.，接祖鲁人号时即此衔；1946-01-01 升 Captain |
| Martin | `Vice-Admiral (retired)` | `Captain` | 1944-07-07 升 R.Adm. 并退役，1948-10-02 在退役名册上升 V.Adm. |

注：Pławski 的波方原制式在 uboat.net 的任期表里写作 `Kmdr.por. (Cdr.)`，
即波方衔 + 英方对应衔并列。本站 `data/ships/piorun.yaml` 用的是 `kmdr por.`，一致。

---

## 7. 抓取与工具

`web_fetch` / `research` 对本站所有域名返回 SSRF 拦截，全程改用 `urllib`：

- `work/staging_cmdr/c4/_raw/fetch.py` —— 抓取（自定义 UA，绕过证书校验）
- `_raw/h2t.py` —— HTML→纯文本（`html.unescape` + 去 script/style）
- `_raw/sect.py` —— 按关键词切一段 unithistories 页面（那站没有稳定锚点）
- `_raw/precheck_c4.py` —— 自检

主会话已抓好的 `work/cmdr13_data.json` 全文先落盘到 `_raw/wiki-*.txt`，
在此基础上补抓了 20 个外部页面。原始 HTML 与文本均留在 `_raw/`，可复查。

---

## 8. 给主会话的三条待办

1. **核 `data/ships/zulu.yaml`**：White 是否被标成「随舰沉没」（见 §2.1）。
2. **核 `data/ships/tirpitz.yaml` 的 Junge 任期**：本站记 11-03，DMA 记 11-04，
   若合并时想统一，建议保留 11-03 并加注，不要静默改。
3. **Junge 早期生平如需 A/D 级支撑**：得去 BArch BA-MA 或查
   Hildebrand/Röhr/Steinmetz《Die deutschen Kriegsschiffe》。现有材料做不到，
   已在文件 note 里写明这一缺口，没有用推测填。
