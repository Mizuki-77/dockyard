# 人物分片写作规范（给 subagent 用）

> Dockyard · 2026-11-23 · 战舰指挥官升级
>
> **你只能写 `work/staging_cmdr/<你的组名>/` 目录。绝对不要碰 `data/`、`src/`、`public/`。**
> 主会话会用脚本合并。

---

## 0. 你要产出什么

每人一个文件：`commanders/<id>.yaml`

```yaml
id: philip-vian
name:
  zh: 菲利普·维安
  en: Philip Vian
  full: Admiral of the Fleet Sir Philip Louis Vian, GCB, KBE, DSO & Two Bars

# 生卒（查不到就不写这一整块，不要填 approx）
life:
  born: 1894-06-15
  born_place: London
  died: 1968-05-27
  died_place: ...

# 军衔（最终军衔，字符串，保留原制式）
rank_final: Admiral of the Fleet

# 一句话身份（30 字内，给卡片用）
summary_zh: 从驱逐舰舰长做到海军元帅，二战英国最有攻击性的舰队指挥官之一

# 简介：3-5 段，每段 100-220 字
intro:
  - heading: 出身与早期
    text: ...
  - heading: ...

# 生平年表：8-20 条，每条必须有 src
timeline:
  - date: 1894-06-15
    text: 生于伦敦……
    src: [enwiki-philip-vian]

# 与本站已有的关联（这一块决定双向跳转，必须填对）
relations:
  # 本站已收录、他指挥过的舰（从下面的清单里挑，id 必须完全一致）
  ships:
    - ship: cossack
      role: 舰长
      from: 1940-01-18
      to: 1941-07-10
  # 他参加过的、本站已收录的战役（从清单里挑）
  battles:
    - battle: last-battle
      role: 第 4 驱逐舰分队指挥官，率部夜袭
```

---

## 1. 本站已有的舰（`ship` 字段只能填这些 id）

```
akagi 赤城号 / kaga 加贺号 / soryu 苍龙号 / hiryu 飞龙号
enterprise 企业号 / yorktown 约克城号 / hornet 大黄蜂号
hood 胡德号 / king-george-v 英王乔治五世号 / prince-of-wales 威尔士亲王号
illustrious 光辉号 / victorious 胜利号 / rodney 罗德尼号
ark-royal 皇家方舟号 / norfolk 诺福克号 / dorsetshire 多塞特郡号
sheffield 谢菲尔德号 / cossack 哥萨克号 / maori 毛利人号
zulu 祖鲁人号 / sikh 锡克人号
bismarck 俾斯麦号 / tirpitz 提尔皮茨号 / prinz-eugen 欧根亲王号
piorun 闪电号
```

## 2. 本站已有的战役（`battle` 字段只能填这些 id）

```
denmark-strait  丹麦海峡海战（1941-05-24）
last-battle     最终战与沉没（1941-05-26 至 05-27）
midway          中途岛海战（1942-06-04）
```

**只填他确实参加过的。** 不确定就不填，不要为了页面好看硬连。

---

## 3. 硬规则（违反即返工）

1. **查不到就写查不到。** 不要编造生平细节、不要「大概出生在」。
   生卒日期拿不准就整条不写，在 `NOTES.md` 里记一句「未获取」。
2. **每条 timeline 必须有 `src`。** 来源 id 见下面的来源清单。
3. **不许出现这些词**：据说 / 有人认为 / 有人称 / 据信 / 或许 / 大概 / 应该是。
4. **有争议的说法并列。** 两个来源打架就两条都写，`note` 里写「两说并列，不裁决」。
5. **军衔保留原制式**，不要翻译成「上校/中校」——`Kpt.z.S.` 就是 `Kpt.z.S.`。

---

## 4. 来源怎么登记

新建 `sources-fragment.yaml`：

```yaml
sources:
  - id: enwiki-philip-vian
    title: Philip Vian — Wikipedia
    url: https://en.wikipedia.org/wiki/Philip_Vian
    type: encyclopedia
    tier: E
    role: [lead]
    lang: en
    access: direct
    fetched: 2026-11-23
    license: cc_by_sa
    note: 用于找线索与核对年表；正文事实须另有非 E 级来源支撑，见下。
```

⚠️ **注意 tier 规则**：本项目规定 **tier E（百科）不能作为 fact 的来源**。
但人物传记是叙事，`timeline` 的 `src` 允许引 E 级——**前提是你同时找到了
非 E 级来源并一并列出**。

所以策略是：
- 维基用来搭骨架、找线索
- 对关键事实（生卒、任免、战功）去找 **D 级以上**来源：
  `unithistories.com`、`naval-history.net`、`uboat.net`、`kbismarck.com`、
  `unitats.org`、`britishmilitaryhistory.co.uk`、`krigsmarine` 相关站、
  London Gazette（thegazette.co.uk）
- 找不到非 E 级来源的关键事实，**降低篇幅、写保守些**，不要硬撑

`tl;dr`：E 级可以引，但**别让它成为唯一来源**。

---

## 5. 抓取方式（重要）

`web_fetch` / `research` 在本机对所有域名返回 SSRF 拦截。**用这两种**：

```powershell
Invoke-WebRequest -Uri "https://en.wikipedia.org/wiki/Philip_Vian" -UseBasicParsing -OutFile work/staging_cmdr/<组>/_raw/x.html
```

```python
import urllib.request
req = urllib.request.Request(url, headers={'User-Agent': 'DockyardArchive/1.0'})
data = urllib.request.urlopen(req, timeout=45).read()
```

主会话已经抓好的维基全文在 **`work/cmdr13_data.json`**，先看那个，别重复抓。

---

## 6. 交付

还要写 `NOTES.md`，含：
- 交付摘要（几篇、每篇几段几事件、用了几个来源）
- 卡住的地方（哪些事实查不到、试了哪些站点）
- 有争议的记载（两源打架的列出了吗）

自检：

```powershell
python -c "import yaml,glob;[yaml.safe_load(open(p,encoding='utf-8')) for p in glob.glob('work/staging_cmdr/<组>/**/*.yaml',recursive=True)];print('yaml ok')"
python work/precheck_cmdr.py <组名>
```
