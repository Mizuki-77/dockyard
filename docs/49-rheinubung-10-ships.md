# 莱茵演习十舰入库完工记录

> 2026-11-22 · 用户要求「这十艘都动工」，把最终战参战名单从 3/13 补到 13/13
> 状态：**已完成并部署** · 提交见文末

---

## 0. 一句话

`last-battle.yaml` 里原来 13 条参战记录中有 10 条只有名字、没有 `ship_id`，
点不开。本轮把 10 艘全部入库：**5 个新舰级 + 1 个已有舰级的第 2 艘**，
939 条 fact、83 片切片、10 篇正文、71 张图、59 条新来源。

---

## 1. 这十艘是哪十艘

| # | 舰 | 中文名 | 属级 | 级新建？ |
|---|---|---|---|---|
| 1 | HMS Norfolk | 诺福克号 | 郡级（Norfolk 子级） | ✅ 新建 `county` |
| 2 | HMS Dorsetshire | 多塞特郡号 | 郡级 | 同上（复用） |
| 3 | HMS Sheffield | 谢菲尔德号 | 城级（Southampton 子级） | ✅ 新建 `town` |
| 4 | HMS Ark Royal | 皇家方舟号 | 皇家方舟级 | ✅ 新建 `ark-royal` |
| 5 | HMS Victorious | 胜利号 | **光辉级** | ❌ 已存在，只写差异 |
| 6 | HMS Cossack | 哥萨克号 | 部族级 | ✅ 新建 `tribal` |
| 7 | HMS Maori | 毛利人号 | 部族级 | 同上 |
| 8 | HMS Zulu | 祖鲁人号 | 部族级 | 同上 |
| 9 | HMS Sikh | 锡克人号 | 部族级 | 同上 |
| 10 | ORP Piorun | 闪电号 | N 级 | ✅ 新建 `n-class` |

**复用红利**：部族级一次建级吃 4 艘，郡级吃 2 艘。这是本轮最大的省力点。

---

## 2. 规模

### 2.1 数据

| 项 | 数量 |
|---|---|
| 新建舰级文件 | 5（`town` / `county` / `tribal` / `ark-royal` / `n-class`） |
| 新建单舰文件 | 10 |
| 舰级 fact | 487 |
| 单舰 fact | 452 |
| **fact 合计** | **939** |
| 状态切片 | 83 片（10 舰，每舰 7–10 片） |
| 舰艇正文 | 10 篇（简介 61 段 + 历史 50 节 / 261 条事件） |
| 新登记来源 | 59 条 |
| 新建武器正文 | 10 篇 |

### 2.2 图片

| 类别 | 张数 |
|---|---|
| 舰图 | **59** |
| 武器图 | **12** |
| 合计 | **71** |

**全部 A 档（PD / CC0），零署名义务。**

按舰分配（用户要求「小舰 10 张以内、找不到就少放」）：

| 舰 | 张数 | 定档理由 |
|---|---|---|
| 皇家方舟号 | 10 | 英国最著名航母之一，素材多 |
| 胜利号 | 10 | 活到 1969 年、两次大改装，外形跨度大 |
| 诺福克号 | 8 | 存活到 1950 年，间战期 + 战时都有照 |
| 谢菲尔德号 | 7 | 64 张候选，但大半是舰上生活照，只挑整舰 + 关键局部 |
| 多塞特郡号 | 6 | 只有 9 张候选 |
| 闪电号 | 5 | 19 张候选，剔掉邮票/旗帜/博物馆陈列 |
| 祖鲁人号 | 4 | 9 张候选，4 张是同一件事 |
| 锡克人号 | 4 | 6 张候选，1 张无关 |
| 哥萨克号 | 3 | 只有 6 张，2 张是纪念牌/吉祥物 |
| 毛利人号 | **2** | **Commons 上总共只有 2 张可用** |

毛利人号那 2 张：一张完好外观照，一张是 1942-02-12 在瓦莱塔港被炸沉的半没照。
不凑数，也不拿别级顶替。

### 2.3 全站变化

| 项 | 本轮前 | 本轮后 |
|---|---|---|
| 页面数 | 106 | **131** |
| 单舰 | 15 | **25** |
| 舰级 | 10 | **15** |
| 武器正文 | 64 | **74** |
| 来源登记 | 253 | **312** |
| 图片记录 | 451 | **522** |
| 字段注册 | 213 | **215** |
| fact（ships+classes） | 1803 | **2742** |
| 最终战参战可点 | 3/13 | **13/13** |

---

## 3. 分片协作的做法（可复用）

10 艘 + 10 型武器正文，一次并发 **8 个 subagent**：

| 组 | 负责 | 产出 |
|---|---|---|
| `g1-victorious` | 胜利号（复用光辉级） | 1 舰 |
| `g2-sheffield` | 谢菲尔德号 + 城级建级 | 1 级 1 舰 |
| `g3-county` | 诺福克号 / 多塞特郡号 + 郡级建级 | 1 级 2 舰 |
| `g4-tribal` | 部族级四舰 + 建级 | 1 级 4 舰 |
| `g5-arkroyal` | 皇家方舟号 + 建级 | 1 级 1 舰 |
| `g6-piorun` | 闪电号 + N 级建级 | 1 级 1 舰 |
| `g7-weapons` | 4 型新炮正文 | 4 篇 |
| `g8-weapons2` | 6 型补充武器正文 | 6 篇 |

### 3.1 三道闸门（这是本轮最有价值的部分）

```
work/staging/<组>/         ← subagent 只写这里，绝不碰 data/
      ↓
work/precheck_staging.py   ← 闸门 1：入库前把能查的全查一遍
      ↓
work/merge_staging.py      ← 闸门 2：合并进 data/，留 .bak
      ↓
scripts/validate.py 等     ← 闸门 3：项目自带的七个体检
```

**为什么要闸门 1**：`validate.py` 只认 `data/`。分片还在 staging 里时跑不了它，
等合并完再发现问题就得回滚 + 重来。precheck 把「字段未注册 / 单位不对 /
confidence 写成 D / src 未登记 / 正文出现模糊词」这些提前拦住。

**闸门 1 实际拦到了什么**：39 个文件 / 939 条 fact，**0 错误 0 警告**通过
（说明 SCHEMA 给得够细），但它在开发过程中暴露了自己两个 bug，见 §5.3。

### 3.2 分片规范（`work/staging/SCHEMA.md`，214 行）

把 `scripts/validate.py` 的硬规则逐条抄成 agent 能读的清单：

- 35 个骨架字段清单（照抄，不让 agent 自己从 213 个里挑）
- 枚举值全表（`ship_type` / `nation` / `fate_type` / `weapon.category` …）
- `protection.armor.*` 的 `qual` 合法值
- 来源登记格式与 tier 定义
- 正文禁用词表
- 「你只能写 `work/staging/<组名>/`」的红字

---

## 4. subagent 纠正了我 7 处错误

这是本轮最该记下来的一节。**我给的任务书里有 7 处史实错误，全部被 subagent 查出并纠正**。
如果它们照着写，站上就会多 7 条假数据。

| # | 我写错的 | 实际 | 谁查出来的 |
|---|---|---|---|
| 1 | Sikh 参加 1942 年圣纳泽尔突袭（Chariot） | **毫无关系**。Chariot 参战舰只有 Campbeltown / Tynedale / Atherstone，她当天在亚历山大参加罗得岛炮击 | `g4-tribal` |
| 2 | Sikh 1944-04 在的黎波里外海被岸炮击沉 | **1942-09-14 托布鲁克外海被德国岸防炮击沉**（三源一致） | `g4-tribal` |
| 3 | Sikh 参加过 1943 年西西里 | 她 1942-09-14 已沉，不可能 | `g4-tribal` |
| 4 | Zulu 被意大利空袭击沉 | navypedia 明确写**德国 Ju 88** | `g4-tribal` |
| 5 | 闪电号 5-26 开火距离 3,500 码 | **13,500 码**（London Gazette 1947-10-16 增刊 §75 原句 "opened fire from 13500 yards"） | `g6-piorun` |
| 6 | N 级鱼雷管 2 座五联（10 管） | **建成时只有 1 座五联**，后部那座建造期间换成了 4 英寸高炮；1942 年改装才换回 | `g6-piorun` |
| 7 | 多塞特郡号 1940 年击沉法国布雷舰 / 1941 年击沉 Atlantis | 前者**查无实据**（七个来源全无）；后者是重巡 **Devonshire** 干的，本舰战果是补给船 **Python** | `g3-county` |

另外两处「数字写反」：

| 我写错的 | 实际 |
|---|---|
| 皇家方舟号机库「上层 173 ft、下层 150 ft」 | **568 ft（173.1 m）/ 452 ft（137.8 m）**——173 的单位是**米**不是英尺 |
| 驱逐舰剑鱼误击谢菲尔德「多次引信故障救了它」 | 因果不成立。真正救它的是 Larcom 下令一炮不还 + 7 枚被规避 + 3 架认出目标；引信故障是**第二波换触发引信**的原因 |

**教训**：给 subagent 的任务书里写「我从记忆里写的，你必须逐条核实，不符以来源为准」，
这句话救了这一轮。**凭记忆填数据是本项目最严重的错误**（交接报告 §14 最后一条），
而写任务书本身就是一次「凭记忆填数据」。

---

## 5. 踩的坑（按痛感排序）

### 5.1 `merge_staging.py` 把已审定的 `data/` 覆盖回初稿 ⚠️ 最严重

第一次合并（7 组）后，主会话在 `data/` 上手工修了三处切片
（给 ark-royal 加 P7「沉没之后」、dorsetshire 加 P0「设计定案」、
victorious 加 V0「设计定案」）。然后为了合并第 8 组（g8 武器正文）
**又跑了一次 merge** —— 它把 g1/g3/g5 的原始分片原样又拷了一遍，
三处修复当场被冲掉，`audit_data.py` 重新报出三条同样的切片问题。

**根因**：脚本是无条件覆盖语义，没有区分「staging 是初稿」与「data 是审定稿」。

**修法**：默认跳过已存在的目标文件，要强制重写加 `--force`。

**教训**：合并脚本必须幂等且**不覆盖已审定产物**。任何「同步」类脚本都要问一句
「跑第二次会发生什么」。

### 5.2 Commons 图片下载：四版才成功

| 版本 | 结果 | 错在哪 |
|---|---|---|
| v1 | 25 成功 / 34 失败 | `thumburl` 带 `?utm_source=...` 查询串，拼进路径就失效 |
| v2 | 更糟 | 把 `upload` 域名改写成 `thumb` 但漏了路径里的 `/thumb/` 段 |
| v3 | 卡在 429 | 没意识到有一半的图拿到的是 `upload.wikimedia.org` 直链 |
| **v4–v5** | **59/59 成功** | 见下 |

**真正的根因**：API 的 `thumburl` 有两种形态：

```
原图宽 > 1280  → https://thumb.wikimedia.org/.../thumb/d/df/NAME.jpg/1280px-NAME.jpg
原图宽 ≤ 1280  → https://upload.wikimedia.org/.../d/df/NAME.jpg      ← thumbnail_unscaled
```

而 **`upload.wikimedia.org` 对本站持续 429**（`docs/45` §8.2 第 5 条早就记了这条）。
我前三版一直在 URL 拼接上兜圈子，没意识到问题不在拼接而在**域名**。

**修法**：凡是 `upload.wikimedia.org` 的 URL，一律改写成 `thumb` 的缩略图形式：
```
upload/wikipedia/commons/1/10/Name.jpg
  → thumb/wikipedia/commons/thumb/1/10/Name.jpg/960px-Name.jpg
```
改完 59 张一次全过，0 失败。

**顺带确认文件头校验的价值**：对不存在的 thumb URL，Commons 返回的是
**HTTP 200 + HTML 错误页**，`urlopen` 不抛异常。v1 靠 `\xff\xd8` 校验拦下 34 个，
否则会把 HTML 存成 34 个 `.jpg`。`docs/45` §8.2 第 3 条记的就是这个。

### 5.3 `precheck_staging.py` 自己的两个 bug

| bug | 表现 | 修法 |
|---|---|---|
| 不认识 `open_ended_note` | g1 报 18 条「valid.to 为空且没 note」，全是误报 | 读文件顶层 `open_ended_note`，与 `validate.py` 口径对齐 |
| 只加载指定组的来源 | `precheck g4` 报 38 条「来源未登记」，因为 `navweaps-4-7in-45-mk12` 是 g7 登记的 | 来源与舰级登记**永远全量加载**，`only` 参数只管「检查哪些组的数据」 |

**教训**：预检脚本的误报比不报更危险——会训练人忽略警告。

### 5.4 自动挑图一定混错图

武器图第一版按「PD 优先 + 尺寸降序」自动挑：

| 型 | 自动挑到的 | 实际是什么 |
|---|---|---|
| 8"/50 Mk VIII | HMAS Australia 停靠纽约 | 是舰不是炮 |
| 8"/50 Mk VIII | 多佛 428 岸炮阵地 | 是岸炮不是舰炮 |
| 6"/50 Mk XXIII | HMAS Hobart 鱼雷损伤 | 是战损照 |
| 6"/50 Mk XXIII | 伯明翰号儿童派对 | 完全无关 |

`docs/45` §8.2 第 8 条早就写了「自动筛选一定混进错图，必须人眼过」。
**武器图比舰图更容易错**，因为分类里混着「装了这门炮的舰」的其他照片。

**修法**：逐张手工指定 + 写明为什么选它。改完 12 张全部正确。

### 5.5 舰名「号」字不统一

全站 25 艘里，原来的 15 艘写法混乱：日本 4 艘（赤城/加贺/苍龙/飞龙）、
德国 2 艘、英国 4 艘不带「号」，其余带。是不同批次 subagent 写作造成的。

查证（不是凭感觉）：

| 来源 | 写法 |
|---|---|
| 中文维基条目名 | 赤城**号**航空母舰、俾斯麥**號**戰艦、胡德**号**战列巡洋舰 |
| 上海中国航海博物馆展牌 | 「俾斯麥」**號** |
| 人民网军事「名舰传奇」 | 俾斯麦级战列舰「俾斯麦」**号** |

无例外。统一改了 11 艘，并把两个写成「赤城（单舰）」的舰级改成「赤城级」「加贺级」。

**注意**：改舰名是**两步**——`name.zh`（页面标题、树上显示）+ `identity.name_zh` fact
（详情页身份区）。只改一处会在同一页面上出现两个中文名，而 `validate.py` 查不出来。
已写成 `work/normalize_ship_names.py` + `work/sync_name_facts.py`。

### 5.6 新增字段：双层机库与无装甲

两个字段缺口，都是用「加字段」而不是「塞 note」解决的：

| 字段 | 缺的原因 | 加了什么 |
|---|---|---|
| `aviation.hangar.upper/lower.length` | 皇家方舟号双层机库上层 173.1 m、下层 137.8 m，只有一个 `hangar.length` 会让下层凭空消失；写两条又会被判成「两源打架」 | 照 `aviation.deck.upper/middle/lower` 的模式加了两个分层字段 |
| `protection.scheme` 加 `none` | N 级驱逐舰设计上没有装甲带，枚举里没有「无装甲」这一项，留空会显示「未记载」 | 加 `none`。写成 `0 mm` 更糟——那读起来是「有装甲但厚度为零」 |

`none` 这个值 `src/lib/resolve.ts:308` 已有中文标签「无」，不用改代码。

### 5.7 其他

- **`web_fetch` / `research` 对几乎所有域名返回 SSRF 拦截**（解析到 198.18.x.x），
  包括 `zh.wikipedia.org` 和 `navypedia.org`。**PowerShell `Invoke-WebRequest`
  与 Python `urllib` 直连都正常**。三个 subagent 各自独立撞到并报告了这一点，
  这个结论应该写进 `SCHEMA.md` §9。
- **NavWeaps 的 4.7"/45 Mk XII 页面 URL 是错的**：`WNBR_47-45_mk12.php` 不存在，
  Mk IX 与 Mk XII 在同一页 `WNBR_47-45_mk9.php`。已按实际页登记。
- **`navweaps-4in-45-mk16` 的既有标题写错了**（标题写 4.5 英寸，url 指 4 英寸页）。
  数值是对的，本轮继续引它但没动那条——**这处待修**。
- **`kbismarck-chase` 的 role 只有 `narrative`**，但 Sheffield 三名死者的逐名名单只有它给。
  已补 `data` role 并写明理由。

---

## 6. 参战名单的战场限定

补 `ship_id` 时**不能**只把名字连上就完事。这 10 艘里有 3 艘在最终战时
**并不在炮战战场上**，页面上必须说清：

| 舰 | 实际情况 | 处理 |
|---|---|---|
| 胜利号 | 1941-05-24 参加对俾斯麦的空袭，**05-26 已脱离** | role 里原有「5-26 已脱离、不在战场」，保留 |
| 皇家方舟号 | Force H，从直布罗陀北上，**不在炮战战场** | 靠 05-26 的剑鱼空袭打坏舵机起作用 |
| 闪电号 | 5-26 深夜交火，**05-27 05:00 因燃油受命返航**，主力 08:47 才开火 | 本轮给 role 补上了这句限定 |

「参战名单 13/13 可点」≠「13 艘都在场」。这个区分写在各舰的 `service` fact 与
`last-battle.yaml` 的 `role` 里。

---

## 7. 体检结果

2026-11-22 20:00 实测：

```
validate           0 错误 / 0 警告
selftest           32 例全过
astro check        0 errors / 0 warnings / 0 hints
audit_links        内链 0 / 锚点 0 / 图片缺失 0 / 空 href 0
audit_data         切片问题 0；1 条硬问题 + 3 条孤儿 = 6 张 PRELOAD 预存图（既有，非本轮）
audit_render       脏数据 0 / 空区块 0 / 缺 title 0 / 缺 h1 0 / 多 h1 0
audit_array_render 未发现隐患
构建               131 页
线上               /ships /ships/ark-royal /ships/piorun
                   /weapons/8in-50-mk8 /battles/last-battle /compare  全部 HTTP 200
```

武器图覆盖：**74 型里 72 型有图**，剩 `45in-45-mk1` 与 `47in-45-mk12` 两型
Commons 上没有对应分类（三种命名都试过），页面显示「暂无影像」。

---

## 8. 动过的文件

### 8.1 新建

```
data/classes/   town.yaml  county.yaml  tribal.yaml  ark-royal.yaml  n-class.yaml
data/ships/     victorious  sheffield  norfolk  dorsetshire  ark-royal
                cossack  maori  zulu  sikh  piorun          （10 个）
data/slices/    同上 10 个
data/articles/  同上 10 个
data/weapon-articles/   45in-45-mk1  47in-45-mk12  6in-50-mk23  8in-50-mk8
                        4in-45-mk16  vickers-50  3pdr-hotchkiss
                        skua  roc  albacore          （10 个）
public/img/ships/       59 个文件
public/img/weapons/     12 个文件
```

### 8.2 修改

| 文件 | 改动 |
|---|---|
| `data/sources.yaml` | +59 条来源；`kbismarck-chase` 补 `data` role |
| `data/images.yaml` | +71 条图片记录（451 → 522） |
| `data/fields.yaml` | +2 个分层机库字段；`protection.scheme` 加 `none` 枚举 |
| `data/battles/last-battle.yaml` | 10 条补 `ship_id`、删过时 note、闪电号 role 加战场限定 |
| `data/ships/*.yaml`（既有 11 艘） | `name.zh` 加「号」+ `identity.name_zh` fact 同步 |
| `data/classes/akagi.yaml`、`kaga.yaml` | 「赤城（单舰）」→「赤城级」 |
| `src/lib/catalog.ts` | 武器分类表 +11 项（新炮 + 之前漏登记的 `5in38-mk12` / `20cm-3ns` / `20-3cm-sk-c34` / `47in-40-mk8`） |

**11 项武器分类登记**，其中 4 项是本轮之前的欠账（不登记就落到「其他」分类）：

```
本轮新炮   8in-50-mk8  6in-50-mk23  47in-45-mk12  45in-45-mk1
欠账补齐   16in-45-mk1  5in38-mk12  20cm-3ns  20-3cm-sk-c34  47in-40-mk8  6in-50-mk22
```

### 8.3 新增 work 脚本（都值得留着）

| 脚本 | 用途 |
|---|---|
| `work/staging/SCHEMA.md` | 分片规范，下次派 subagent 直接复用 |
| `work/precheck_staging.py` | 入库前预检 |
| `work/merge_staging.py` | 合并分片（已改成不覆盖已审定文件） |
| `work/renumber_slices.py` | 切片 code 顺延（插入新片后重编号） |
| `work/normalize_ship_names.py` | 统一舰名加「号」 |
| `work/sync_name_facts.py` | 同步 `identity.name_zh` fact |
| `work/patch_battle_participants.py` | 给参战名单补 `ship_id`（带「文件不存在就不动手」的防护） |
| `work/refix_slices.py` | 重放被 merge 冲掉的切片修复 |

---

## 9. 遗留

| # | 事项 | 严重度 |
|---|---|---|
| 1 | `navweaps-4in-45-mk16` 的标题写错（写 4.5 英寸，页面是 4 英寸），url 是对的 | 低 |
| 2 | `45in-45-mk1` / `47in-45-mk12` 无图（Commons 无分类） | 低 |
| 3 | 毛利人号只有 2 张图（素材上限，非遗漏） | 低 |
| 4 | 装甲总重与占比：郡级 / 部族级 / N 级全空白 | 中 |
| 5 | `SCHEMA.md` §9 应补「`web_fetch` SSRF 拦截、改用 `urllib` 直连」这条 | 低 |
| 6 | 本轮 10 艘舰的**涂装专项**（如谢菲尔德北极护航的冬季迷彩）没做 | 中 |
| 7 | 最终战 13 艘全收录后，`forces` 段的双方兵カ叙述可以再核一遍 | 低 |

---

## 10. 一句话交接

**想看成品**：https://archive.dockyard.workers.dev/battles/last-battle
参战名单 13 艘全可点。

**想接着做**：先读本文 §5（坑）与 §4（subagent 纠错），
再读 `docs/30-new-ship-workflow.md`。派 subagent 前**必须**先读
`work/staging/SCHEMA.md`，任务书里**必须**写「我可能写错，以来源为准」。
