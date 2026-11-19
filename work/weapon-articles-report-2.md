# 武器正文交付报告 · 第二批（雷达 / 火控 / 舰载机 33 型）

日期：2026-11-18　范围：33 型新实体　目录：`data/weapon-articles/`

## 一、文件清单与规模

| 武器 id | 类别 | 简介段数 | 历史节数 | 事件数 |
|---|---|---|---|---|
| type-79z | 雷达 | 3 | 1 | 2 |
| type-79b | 雷达 | 2 | 1 | 2 |
| type-281 | 雷达 | 3 | 1 | 3 |
| type-281b | 雷达 | 3 | 1 | 2 |
| type-272 | 雷达 | 3 | 1 | 3 |
| type-282 | 雷达 | 3 | 1 | 3 |
| type-285 | 雷达 | 3 | 1 | 4 |
| type-279 | 雷达 | 3 | 1 | 2 |
| type-279b | 雷达 | 2 | 1 | 2 |
| type-271 | 雷达 | 3 | 1 | 3 |
| type-273 | 雷达 | 3 | 1 | 2 |
| type-277 | 雷达 | 3 | 1 | 3 |
| type-293 | 雷达 | 3 | 1 | 2 |
| type-284 | 雷达 | 3 | 2 | 4 |
| type-279m | 雷达 | 3 | 2 | 3 |
| fumo-23 | 雷达 | 3 | 1 | 4 |
| fumo-26 | 雷达 | 3 | 1 | 3 |
| fumo-27 | 雷达 | 3 | 1 | 4 |
| fumo-213 | 雷达 | 3 | 1 | 3 |
| hacs-mk4 | 火控 | 3 | 2 | 4 |
| pom-pom-director-mk3 | 火控 | 3 | 1 | 2 |
| fumb-4 | 火控（被动 ESM） | 3 | 1 | 3 |
| fumb-7 | 火控（被动 ESM） | 3 | 1 | 3 |
| swordfish | 舰载机 | 3 | 3 | 8 |
| fulmar | 舰载机 | 3 | 2 | 5 |
| sea-gladiator | 舰载机 | 3 | 1 | 2 |
| corsair | 舰载机 | 3 | 1 | 4 |
| avenger | 舰载机 | 3 | 1 | 4 |
| walrus | 舰载机 | 3 | 1 | 4 |
| seafox | 舰载机 | 3 | 1 | 1 |
| arado-196 | 舰载机 | 3 | 1 | 5 |
| flycatcher | 舰载机 | 3 | 1 | 3 |
| fairy-iiif | 舰载机 | 3 | 1 | 3 |

合计 33 个文件：简介 97 段，历史 39 节，事件 105 条。
全库现有 48 个武器正文文件（15 旧 + 33 新），合计事件 216 条。

## 二、校验

```
python work/check_weapon_articles.py
→ 48 个文件，0 错误 / 0 警告；结论：通过

python scripts/validate.py
→ 0 错误 / 0 警告（已含 data/weapon-articles/ 全量校验）

cmd /c "npm.cmd run build"
→ 71 page(s) built in 25.79s；dist/weapons/ 下 48 个目录页
```

## 三、因为查不到而没写的内容

以下内容在全部已查材料中都没有来源，正文一律留空，没有用估算值或百科值填充：

1. **所有雷达与火控的技术参数**——功率、频率、波长、探测距离、跟踪精度、天线增益。
   武器实体注册表里没有这些字段；`navweaps-radar`、`navweaps-radar-uk`、`navweaps-hacs`
   三页原文都给了数字，但正文一个都没取。
2. **各型雷达的产量、造价、服役艘数**——任何来源都没有。
3. **Type 79B 与 79Z 的硬件差别**——装舰清单把它们记成两个型号，
   但设计资料、型号总表、装舰清单三处都没有说明改了什么。
4. **Type 293 的独立条目**——`navweaps-radar-uk` 的英国雷达总表里没有 Type 293 这一行，
   本页内容全部来自 navypedia 装舰清单一种材料。
5. **Type 281B 与 Type 281M 的区别**——两处材料分别用这两种写法，都无法证明是两型。
6. **Type 273 与 Type 293 是否构成替代关系**——1944 年 7 月清单里一减一加，
   但没有任何一句原文说「293 取代 273 的水面搜索职能」。
7. **HACS Mk IVGB 四部的具体分工**——哪一部管哪几座炮座，材料只到「4 部、配 5.25 英寸炮」。
8. **Mk III pom-pom 指挥仪的座数**——材料明确写「座数未获取」，正文因此不写数量。
9. **Flycatcher 与 Fairey IIIF 的具体撤装月份**——材料明确写「未获取」，只到 1933 年末。
10. **Fairey Seafox 在本舰的搭载记录**——只有 navypedia 舰级页的型号清单一行，
    影像与日志证据均无，因此不写数量、不写搭载时段、不写机型参数。
11. **各型飞机与 Ar 196 的机型参数**（马力、极速、翼展、载弹量）——
    Ar 196 的一手页（`kbismarck-aviation`）实际给了 BMW 132K 960 hp、320 km/h、
    翼展 12.4 m 等数据，但本批统一按「不写机型参数」处理，没有取用。
12. **提尔皮茨号弹射器何时拆除**——所有已查来源均无记载。

## 四、正文里保留的争议（一处都没删）

| 实体 | 争议内容 |
|---|---|
| type-281b | 281B 与 281M：两种记法指同一型，合并为一个实体，两说并列 |
| type-279m | 胡德号装的是 279M（hmshood）还是 79B（navypedia），两说并列 |
| type-284 | 装成日期：技术页 1941-03-15 vs 年表 1941-03-17 |
| type-285 | 装舰时点三个口径：设计资料 1941-42、navypedia 1943-06、型号表 late 1942 |
| fumo-26 | 判型靠 3 m×6 m 天线尺寸，navweaps 原文用「probably for FuMO 26」 |
| fumo-27 | 装舰时点两说（1941 夏后塔 vs 1942-01 前塔）；navypedia 静态清单「4 × FuMO 27」 |
| fumo-213 | 同族 212 / 213 的具体分配，原文用 probably |
| swordfish | 143 mph（试飞）vs 93 knots（挂鱼雷与远程油箱的机组原话） |
| swordfish | 塔兰托时鹰号借调的 Swordfish：舰长报告 5 架 vs 叙述材料 6 架 |
| fulmar | 塔兰托机群：15 架 Fulmar（ac）vs 12 架（navypedia）；战损：11 Swordfish + 5 Fulmar vs 9 + 4 |
| sea-gladiator | 813 中队 2 架 Sea Gladiator vs 813 Fighter Flight 4 架 |
| arado-196 | 弹射器长度：16 m/24 m（德文一手）vs 32 m/48 m（dewiki）；1 座双端 vs 左右各一 |
| walrus | 「第一型装雷达的海军一线飞机」标为 naval-history-kgv 的断语，未升格为本站结论 |

## 五、新增来源（3 条，插在 `data/sources.yaml` 的 `todo:` 之前）

| id | tier | 用途 |
|---|---|---|
| `navweaps-radar-uk` | D | 英国战时舰载雷达型号总表（Type 79/271/272/273/274/275/276/277/279/280/281/282/283/284/285/286/291），引它的用途、取代关系、首装舰三栏 |
| `navweaps-hacs` | D | HACS 系统专文（tech-066），Mark I 试射、各型火控台装舰对象、B.R. 224/45 的岗位分工与偏转屏、与美国 Mark 37 的对比 |
| `naval-history-kgv` | D | KGV 逐日服役年表，只用两条：1941 年 Scapa 期间载 2 架装 ASV 11N 的 Walrus、以及 1941-04 把 Walrus 飞往冰岛 |

新增后 `data/sources.yaml` 共 171 条。

## 六、来源使用分布（本批 33 个文件）

使用次数前几名：`navweaps-radar-uk` 13、`navypedia-illustrious` 12、
`ac-design` 10、`navypedia-kgv` 10、`kbismarck-tirpitz` 7、`navweaps-radar` 6。

批内新启用的既有来源：`kbismarck-firecontrol`、`kbismarck-aviation`、
`kbismarck-chase`、`kbismarck-last-battle`、`kbismarck-denmark-strait`、
`hmshood-tovey-dispatch`、`ac-gunnery-report`、`ac-taranto-report`、
`ac-battle-damage`、`ac-blitz`、`ac-excess`、`ac-saratoga`、`ac-eastfleet`、
`ac-kamikaze`、`luftwaffe-zur-see-196-tirpitz`、`rmg-kgv-guide`、
`naval-history-illustrious`、`hooddenmark1`。
