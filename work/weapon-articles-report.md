# 武器正文交付报告

日期：2026-11-18　范围：15 型武器　目录：`data/weapon-articles/`

## 一、文件清单与规模

| 武器 id | 文件 | 简介段数 | 历史节数 | 事件数 |
|---|---|---|---|---|
| 38cm-sk-c34 | `data/weapon-articles/38cm-sk-c34.yaml` | 5 | 3 | 8 |
| 15cm-sk-c28 | `data/weapon-articles/15cm-sk-c28.yaml` | 5 | 3 | 9 |
| 10_5cm-sk-c33 | `data/weapon-articles/10_5cm-sk-c33.yaml` | 5 | 3 | 6 |
| 37mm-sk-c30 | `data/weapon-articles/37mm-sk-c30.yaml` | 5 | 2 | 6 |
| 20mm-c30 | `data/weapon-articles/20mm-c30.yaml` | 5 | 2 | 5 |
| 20mm-c38 | `data/weapon-articles/20mm-c38.yaml` | 4 | 2 | 5 |
| 15in-42-mk1 | `data/weapon-articles/15in-42-mk1.yaml` | 5 | 4 | 8 |
| 14in-45-mk7 | `data/weapon-articles/14in-45-mk7.yaml` | 6 | 3 | 10 |
| 525in-50-mk1 | `data/weapon-articles/525in-50-mk1.yaml` | 6 | 3 | 8 |
| 2pdr-mk8 | `data/weapon-articles/2pdr-mk8.yaml` | 5 | 2 | 10 |
| 4_5in-qf-mk3 | `data/weapon-articles/4_5in-qf-mk3.yaml` | 6 | 3 | 8 |
| 40mm-bofors | `data/weapon-articles/40mm-bofors.yaml` | 5 | 2 | 8 |
| 20mm-oerlikon | `data/weapon-articles/20mm-oerlikon.yaml` | 5 | 2 | 8 |
| g7a-t1 | `data/weapon-articles/g7a-t1.yaml` | 5 | 2 | 6 |
| up-rocket | `data/weapon-articles/up-rocket.yaml` | 5 | 2 | 6 |

合计：简介 77 段，历史 38 节，事件 111 条。

## 二、校验

```
python work/check_weapon_articles.py
→ 15 个文件，0 错误 / 0 警告；结论：通过

python work/run_validate.py
→ returncode=0
  data/articles/king-george-v.yaml: 简介 6 段，历史 9 节 51 条事件
  data/articles/tirpitz.yaml: 简介 6 段，历史 6 节 26 条事件
通过：0 错误 / 0 警告

cmd /c "npm.cmd run build"
→ 71 page(s) built in 28.71s / Complete!
```

`dist/weapons/<id>/index.html` 15 个页面逐个检查，无一个出现「这一型还没有整理简介」或「这一型还没有整理服役史」。

## 三、来源

全部引用 `data/sources.yaml` 已登记 id，**未新增任何来源**，未改动 `data/images.yaml`、`data/fields.yaml`、`src/`。

其中 `20mm-c38` 与 `4_5in-qf-mk3` 在注册表里没有独立 id，分别复用 `navweaps-20mm-c30`（该页同时覆盖 C/30 与 C/38）与 `navweaps-45in-45-mk1`（`classes/illustrious.yaml` 里这门炮本来就是这么标的）。

## 四、争议并列（不裁决）

- 38cm-sk-c34：射速三说——Krupp 文件 4 度仰角 26 秒/发；1941-05 AVSK 报告扬弹机可供四塔 23–25 发/分（合每门 3 发/分）；俾斯麦丹麦海峡 13 分钟 93 发，实际不到每门 1 发/分。同一份 AVSK 报告另记扬弹机缺陷造成两次严重故障、供弹长时间中断。
- 14in-45-mk7：北角海战弹数与齐射数各文献冲突，正文并列 navweaps 采用的 A.J. Watts《Loss of Scharnhorst》Part II 统计表（前段 52 齐射 31 夹中、后段 25 齐射 21 夹中、全战 80 齐射 446 发）。
- g7a-t1：装药重量 280 kg 与 430 kg 两说，navweaps 倾向 280 kg 并推测低值属战争前期。
- 525in-50-mk1：仰角 navweaps/navypedia 70° vs rmg-kgv-guide 80°；对空升限 46,500 ft @70° vs 29,544 ft @80°（量级差）。
- 4_5in-qf-mk3：navweaps「定装弹过重、持续射击射速迅速下降」vs ADM 3363/0197「8 门炮约 30 分钟约 3,000 发、平均 12 发/分 remarkable」。
- up-rocket：英王乔治五世号座数 navweaps 记 3 座、navypedia 与 rmg-kgv-guide 记 4 座；胡德号起火点写 navweaps 概括判断与幸存者 Tilburn 推测并列，并明说这不等同于调查结论。
- 37mm-sk-c30：射速有 30 / 80（理论）/ 40（实际）三说，正文索性不写射速数字，只写「半自动、逐发装填，作为防空炮射速偏慢」这一定性结论。

## 五、因查不到而没写

- **2pdr-mk8**：删掉「威尔士亲王号在丹麦海峡用 pom-pom 开火」——无已登记来源直接支持。改用 RMG 记录的英王乔治五世号 1941-12 装备变化（5 座八联 + 1 座四联）。
- **15in-42-mk1**：仰角 20→30 度改装的具体完成年份，navweaps 未给，合并进「1935 年代中期」一条并注明；Warspite 命中「朱利奥·凯撒」只写到 1940-07，未补具体日。
- **10_5cm-sk-c33**：训练舰 Albatros 加装双联的年份来源没给，只写「战后加装」，该节 range 收窄为 {1948, 1948}。
- **up-rocket**：光辉级是否装过 UP——navweaps 装舰清单与 ADM 1/23040 分配令均无航母，写成否定结论，不写座数；英王乔治五世号 4 座的**具体位置**（原先写的「B 塔 1、Y 塔 2、舰尾 1」来自未登记的 wiki 舰级页）已删除。
- **525in-50-mk1**：「1945-09 仍装 8 座双联」这条删掉（1940 年即如此，无信息量），该节 range 改为 {1940-10, 1941-05}。
- **40mm-bofors**：navweaps 原文把浅水重炮舰 Erebus 混称「the cruisers」，正文照录原文并在中文括注她的真实舰种，未静默改写。
