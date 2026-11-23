# 战舰指挥官升级：人物实体层

> 2026-11-23 · 用户要求「每个人都要介绍、经历和照片，以及和舰、战役的双向跳转」
> 状态：**已完成并部署** · 145 页

---

## 0. 一句话

把「指挥官」从**一条 fact 值**升级为**独立实体层**：
13 位有可靠资料的人各有独立页面（简介 + 年表 + 肖像 + 走舰/走战役的链接），
其余 25 条只有姓名的任期**不建页**，但留在总表与舰页里并明说「查不到生平」。

---

## 1. 为什么是 13 人，不是 37 人

原始数据里有 **37 条 `service.commander` fact**，去重后 **36 人**。

我先做了一次覆盖率实测（`work/probe_cmdr_photos.py` + `work/probe_cmdr_wiki.py`）：

| 项 | 结果 |
|---|---|
| 有英文维基条目 | 13 人（其余 23 人查不到条目） |
| 有可用肖像照 | 6 人 |
| 只有姓名 + 军衔 + 任期 | 23 人 |

**23 个「名字壳」不建页。** 理由写进了页面顶部与代码注释：

> 给一个只有名字的人编 500 字简历，会毁掉整站「每条数据都能追溯到来源」的信誉。

这是本项目红线「查不到就写查不到」的直接延伸。

---

## 2. 13 人名单

| id | 姓名 | 当职军衔 | 最终军衔 | 照片 |
|---|---|---|---|---|
| `philip-vian` | 菲利普·维安 | Capt | Admiral of the Fleet | ✅ 单人 |
| `arthur-power` | 阿瑟·鲍尔 | Captain | Admiral of the Fleet | ✅ 单人 |
| `augustus-agar` | 奥古斯都·阿加 | Captain | Captain | ❌ |
| `robert-sherbrooke` | 罗伯特·舍布鲁克 | Cdr | Rear-Admiral | ❌ |
| `benjamin-martin` | 本杰明·马丁 | Captain | Vice-Admiral（退役名册） | ❌ |
| `louis-hamilton` | 路易斯·汉密尔顿 | Captain | Admiral | ✅ **合影** |
| `michael-denny` | 迈克尔·丹尼 | Captain | Admiral | ✅ 单人 |
| `ernst-lindemann` | 恩斯特·林德曼 | Kapitän zur See | 同 | ✅ 单人 |
| `helmuth-brinkmann` | 赫尔穆特·布林克曼 | Captain | Vizeadmiral | ❌ |
| `karl-topp` | 卡尔·托普 | Kpt.z.S | Vizeadmiral | ❌ |
| `wolf-junge` | 沃尔夫·容格 | Kpt.z.S. | 同 | ❌ |
| `eugeniusz-plawski` | 欧根纽什·普瓦夫斯基 | kmdr por | komandor | ✅ **合影** |
| `richard-taylor-white` | 理查德·泰勒·怀特 | Cdr | Captain | ❌ |

### 2.1 `rank_at_post` 与 `rank_final` 是两个字段

用户要的栏目叫「战舰指挥官」，读者关心的是**他指挥那艘舰时是什么身份**。

- `karl-topp` 当提尔皮茨舰长时是 `Kpt.z.S.`，后来才升 `Vizeadmiral`。
  卡片只显示 `Vizeadmiral` 会让人以为他以上将身份在舰上待过。
- 所以卡片优先显示 `rank_at_post`，`rank_final` 用小字附在后面（`↑Vizeadmiral`）。

---

## 3. 合影的处理（用户明确要求「合影也行，标注就好」）

6 张肖像里 **2 张是合影**，两张都有官方图注点名方位，所以能准确标注：

| 人 | 图 | 标注依据 |
|---|---|---|
| `louis-hamilton` | 乔治六世在约克公爵号接见本土舰队将官（1943-08-16） | Commons 图注原文写「left to right: … Rear Admiral L H K Hamilton …」→ **左起第二人** |
| `eugeniusz-plawski` | 闪电号军官在会议室取暖 | 官方描述原文「The Captain, Eugeniusz Pławski, is farthest from the camera」→ **离镜头最远** |

**规矩**：`images.yaml` 里给这类记录加 `group_shot: true`，`note` 开头必须是
「这张是合影。××是…」。人物页据此渲染一条黄色提示条，列表页在缩略图上压「合影」角标。

**没有官方方位依据的合影不能用** —— 标错比不标更糟。

---

## 4. 双向跳转怎么实现的

```
data/commanders/<id>.yaml
    relations.ships:   [{ship: cossack, role: 舰长, from, to}]
    relations.battles: [{battle: last-battle, role: ...}]
            ↓ 反向索引（src/lib/data.ts）
getCommandersOfShip(shipId)   → 舰页「历任指挥官」
getCommandersOfBattle(bId)    → 战役页「参战指挥官」
            ↓ 正向
resolveCommanderShips(c)      → 人物页「指挥过的舰」卡
resolveCommanderBattles(c)    → 人物页「参加过的战役」
```

**关系只存在指挥官侧**，舰与战役文件不维护指挥官列表 —— 一处修改，两端同步。

结果：

| 页面 | 链接数 | 实例 |
|---|---|---|
| `/commanders` | 13 张卡 | 按英国 8 / 德国 4 / 波兰 1 分组 |
| `/ships/cossack` | 4 | Sherbrooke ×2、Vian ×2（都是两段任期） |
| `/battles/last-battle` | 4 | Martin、Vian、Lindemann、Pławski |
| `/battles/denmark-strait` | 2 | Lindemann、Brinkmann |

---

## 5. subagent 纠正了 7 处（这轮最该记的）

4 个 subagent 分头写 13 人，**每一组都查出我任务书里的错**：

| # | 我写错的 | 实际 | 谁 |
|---|---|---|---|
| 1 | **White 随舰沉没** | **没有**。他留下 12 人抢救，全部由 Hursley/Hurworth 救起，此后服役至 1955 | c4 |
| 2 | **Vian 参加北角海战/击沉沙恩霍斯特** | **无关**。1943-09~11 他在萨勒诺，北角时英方指挥是 Fraser 与 Burnett | c1 |
| 3 | **Hamilton 是丹麦海峡当天舰长** | **不是**。1941-02-15 就交给了 Leach；05-24 在舰桥上的是 Leach | c2 |
| 4 | Agar 最终军衔是准将 | 是 **Captain**（上校）。准将是退休名册晋衔 | c1 |
| 5 | Sherbrooke 在哥萨克号只有一段任期 | **两段**：1939-12-29~1940-01-18 与 1940-03-29~05-21 | c1 |
| 6 | Denny 勋衔含 KBE | 是 CB/CBE/DSO/**KCB**/**GCB**；最终军衔是 Admiral 非 Admiral of the Fleet | c2 |
| 7 | Power 生于 1899 | **1889**（按 1899 算他 5 岁入 Britannia） | c2 |

### 5.1 顺带修掉的三处既有数据错误

这些不是 subagent 报告里提的，是我核对时**顺着查出来**的：

| 文件 | 问题 | 修法 |
|---|---|---|
| `data/ships/zulu.yaml` | `Richard Taylor White（1942-04-28 至 1942-09-14 沉没）` —— 读起来像他随舰沉没 | 改「任职，任期至本舰 1942-09-14 沉没」+ note 写明他没死 |
| `data/ships/maori.yaml` | `Rafe Edward Courage（…至 1942-02-12 沉没）` —— 同样歧义 | 同上；并说明毛利人号是港内锚泊时被炸沉，不写他阵亡 |
| `data/ships/prince-of-wales.yaml` | Hamilton 任期 `to` 留空 —— 读起来像他指挥到 1941-12 沉没，实际只带了 27 天 | 补 `to: 1941-02-15` + 三源说明 |
| `data/ships/cossack.yaml` | Vian 两任之间的空档（1940-03-29~05-21）没有 fact，时间轴上这段没人 | 补录 Sherbrooke 第二段任期 |

**教训**：「至 YYYY-MM-DD 沉没」这种写法，读者会默认人也没了。舰沉与舰长生死必须分开写。

---

## 6. 页面设计

### 6.1 `/commanders` 总表（重做）

分三层，对应数据的三档：

1. **有档案的 13 人** —— 卡片（照片或首字母占位 / 姓名 / 当职军衔 / 一句话 / 舰名）
2. **仅有姓名的 25 条** —— 紧凑表，标「无传记资料」
3. 顶部四个数字：13 位有档案例 / 6 位有肖像 / 25 条仅姓名 / 覆盖 10 舰

顶部有一条黄色声明条解释为什么分两层。

### 6.2 `/commanders/[id]` 人物页

```
标题 + 军衔 + 国籍 + 生卒
├─ 头部：照片（或首字母占位牌）+ 英文全名 + 一句话 + 出生地
├─ 简介：4-5 段，每段带小标题
├─ 与本站的连接：指挥过的舰（图卡）/ 参加过的战役
├─ 生平年表：16-20 条，左侧时间轴
└─ 资料来源
```

**照片缺失不破图**：`aspect-ratio: 4/5` 的斜纹占位牌 + 姓名首字母 + 「暂无照片」，
下面附一句「不用他人照片或生成图代替 —— 查不到就空着」。

### 6.3 舰页与战役页

- 舰页「历任指挥官」：有档案的可点（带 → ），无档案的虚框 + 「无传记资料」
- 战役页「参战指挥官」：左侧蓝条卡片，姓名 / 军衔 / 在战役中的身份

两个区块都带一句说明：只列有档案的，没资料的补不进来。

---

## 7. 规模

| 项 | 数量 |
|---|---|
| 指挥官档案 | **13 人** |
| 简介段落 | **55 段** |
| 生平年表 | **238 条** |
| 关联舰任期 | 15 条 |
| 关联战役 | 6 条 |
| 肖像照 | **6 张**（4 单人 + 2 合影） |
| 新登记来源 | **51 条**（363 总） |
| 新增页面 | **13 个**（132 → **145**） |

---

## 8. 校验与踩的坑

### 8.1 新增 `check_commander()` 到 validate.py

指挥官不是 fact，没有 unit/qual/confidence，但有**结构**：

- `name` 必须有 zh + en
- `life.born/died` 日期格式，且 born ≤ died
- `intro` 每段必有 heading + text，扫模糊词
- `timeline` 每条必有 date + text + src，且日期升序
- **`relations.ships[].ship` 必须存在于 `data/ships/`**
- **`relations.battles[].battle` 必须存在于 `data/battles/`**

后两条是重点 —— 引用写错会在页面上造出 404 链接。

### 8.2 坑 1：同一个人出现两次

舰页第一版的「已覆盖」判据是「fact 里的每个词都能在档案全名里找到」，
结果 Sherbrooke 与 Vian **同时出现在「有档案」和「无传记资料」两栏** ——
因为档案 `name.en` 是 `Robert St. Vincent Sherbrooke`，fact 解析后可能带逗号残留。

改成**姓氏 + 首字母**双判据后修复：10 条 → 6 条。

### 8.3 坑 2：年份越界检查的误报

第一版规则「正文任何年份早于出生年/晚于卒年就报错」，实测 4 条**全是误报**：

- Lindemann 1942-01-06 遗孀代领追授勋章（死后的事）
- Pławski 2004-06-16 骨灰迁葬波兰（死后的事）
- White 祖宅「1699 年起的宅子」（说的是建筑）

改成带关键词窗口（追授/葬/宅/舰/服役…）的版本后，真实越界 0 条。
另外加了一条「入役年龄 13-16 岁」的合理性检查，13 人全部通过。

### 8.4 坑 3：`rank_final` 写成 `Vice-Admiral (retired)`

页面直接显示原文，中英混排很难看。改成 `Vice-Admiral（退役名册）`。
同时摘要里「医院学校出身的第一位将官」这个说法不准确 ——
他确实在 1944 年升了现役少将，但把话说全更稳：
「皇家海军医院学校出身的第一位现役将官」。

---

## 9. 遗留

| # | 事项 | 严重度 |
|---|---|---|
| 1 | 23 人无传记资料（数据缺口，非疏漏） | — |
| 2 | 13 人里 7 人无照片 | 中 |
| 3 | Wolf Junge 早期生平只有德文维基单源 | 中 |
| 4 | Lindemann 的分歧叙事全是间接证据（无舰桥生还者） | 中 |
| 5 | `thegazette.co.uk` 的 PDF 返回 202 空 body，VC/DSO citation 全文未拿到一手件 | 低 |
| 6 | Denny 接任胜利号日期两说（1943-12-08 vs 1944-03-04）已并列 | 低 |

---

## 10. 下一步

- **扩舰**（用户原本的计划）：太平洋战场除中途岛 7 艘外仍空白
- 若要补更多指挥官：优先找有新舰入库时顺带产生的 `service.commander` fact，
  再走这次的同一套流程（probe 覆盖 → 选拔 → 分片写 → 合并）
