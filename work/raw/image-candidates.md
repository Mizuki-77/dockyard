# 图片候选与失败来源清单

> 供以后复用。分三部分：① 实际核过授权但**没选**的候选；② **失败/不可用**的来源（含报错原文）；③ 已判定**不能进仓库**的来源类型。
> 所有授权均逐张从 Commons `imageinfo.extmetadata` 的 `LicenseShortName` / `License` 读取，未按文件名或常识推测。
> 采集日期：2026-11-17。工具：`work/img/commons.py`（Commons API 封装，2.5s 限速）、`work/img/fetch.py`（缩略图下载）。

---

## 一、核过授权但没选的候选

### Bismarck（另有 3 张已选，见 manifest）

| Commons 文件 | 授权（原文） | 尺寸 | 作者 / Credit | 不选原因 |
|---|---|---|---|---|
| File:Bundesarchiv Bild 193-07-4-21, Schlachtschiff Bismarck.jpg | CC BY-SA 3.0 de | 522x799 | Unknown / Bundesarchiv | 竖构图、舰体被裁，不适合横向配图 |
| File:Bundesarchiv Bild 193-01-6-23A, Schlachtschiff Bismarck.jpg | CC BY-SA 3.0 de | 800x533 | Unknown / Bundesarchiv | 局部甲板机械，看不出全舰 |
| File:Bundesarchiv Bild 193-03-1-06, Schlachtschiff Bismarck.jpg | CC BY-SA 3.0 de | 800x531 | Unknown / Bundesarchiv | 舰桥与探照灯平台，主体不是 38cm 炮塔（原本当炮塔候选，目视否定） |
| File:Bundesarchiv Bild 193-02-6-17, Schlachtschiff Bismarck.jpg | CC BY-SA 3.0 de | 800x534 | Unknown / Bundesarchiv | 舰首破浪特写但画面含纳粹旗，且舰首已有更好选择 |
| File:Bundesarchiv Bild 193-05-3-37 / 3-38 / 3-39 / 5-35 / 4-4-19A / 4-4-20A / 4-5-25A / 4-2-10A / 4-2-12A / 3-1-10 / 1-7-08A | CC BY-SA 3.0 de | 500-800px | Unknown / Bundesarchiv | 舷侧局部、吊艇、舱口、旗帜等细节，构图不适合做配图 |
| File:Bismarck in Dry Dock SLNSW FL19275838.jpg | Public domain | 3055x3950 | Claus Franzen / State Library of NSW | 竖幅船坞照，比例不适合网页横幅；且是建造期非服役期 |
| File:Signals to Bismarck.jpg | Public domain | 1503x920 | Kriegsmarine / kbismarck.com | 内容是通信设备与电文，不是舰体 |
| File:German Battleship Bismarck.jpg | **无 imageinfo（missing）** | — | — | 页面无图片信息，无法核实 |
| File:Bismarck-side-view.png | CC BY 3.0 | — | — | 是线图不是照片，且 B 档 |
| File:Schlachtschiff Bismarck (9408630263).jpg | CC BY 2.0 | — | — | 现代模型照，非历史照片 |
| File:Battleship Bismarck's port side 15 cm gun.jpeg | CC BY-SA 3.0 de | 335x220 | Bundesarchiv | 太小，无法使用 |

### 其他舰艇

| Commons 文件 | 授权 | 尺寸 | 不选原因 |
|---|---|---|---|
| File:Battleship Tirpitz off Kiel Sept 1941.jpg | Public domain | 595x431 | **内容与文件名不符**：目视确认是一枚下落中的炸弹/炮弹特写，不是提尔皮茨。已下载后删除 |
| File:German battleship Tirpitz partly covered by a smokescreen at Kaafjord A22634.jpg | Public domain | 1271x689 | credit 指向 media.iwm.org.uk（IWM 数字副本），按保守策略清退 |
| File:German battleship Tirpitz evading torpedoes during Operation Sportpalast.jpg | Public domain | 800x540 | 画面烟雾占大半，舰体辨识度低 |
| File:HMS Hood 24 May 1941.jpeg | Public domain | 624x493 | 分辨率低，且有 1932 年的高清全舰侧视 |
| File:HMS Hood aerial photo 24 May 1941.jpg | Public domain | 624x636 | 俯拍爆炸瞬间，但与 hood-explosion 重复，且尺寸小 |
| File:HMS Hood Aft guns 1926 USNHC 57184.jpg | Public domain | 5407x4418 | 是炮位特写，与 HMS Hood 舰体页需求不符 |
| File:HMS Prince of Wales (53) in Placentia Bay... (NH 67194-A).jpg | Public domain | 2845x2106 | 与已选的 argentia 版同源，取高清那张即可 |
| File:HMS Prince Of Wales in Singapore.jpg / HMS Prince of Wales Singapore (041562).jpg | Public domain | 1302x896 / 800x527 | 停泊状态、构图平淡 |
| File:Aboard British battleship HMS Prince of Wales.jpg | Public domain | 1415x1073 | 舰内舱室，非舰体外景 |
| File:HMS Prince of Wales sinking.jpg | Public domain | 640x216 | 极窄条幅，640px 宽，网页不可用 |
| File:The Loss of HMS Prince of Wales and Repulse 10 December 1941 H12775.jpg | Public domain | 800x791 | 已有 force-z 那张同日高清图 |
| File:Sinking of HMS Prince of Wales and Repulse 10 December 1941 H12775.jpg | **missing** | — | 无 imageinfo |
| File:Prinz Eugen Kiel.jpg | Public domain | 509x742 | 竖幅、分辨率低 |
| File:German cruiser Prinz Eugen firing forward guns during tests in 1946.jpg | Public domain | 677x855 | 竖幅炮口焰，舰体不完整 |
| File:German cruiser Prinz Eugen off Philadelphia Navy Yard in 1946.jpg | Public domain | 908x537 | 分辨率低于已选的巴拿马运河版 |
| File:Cruiser Prinz Eugen anchored in Bikini Lagoon on 14 June 1946.jpg | Public domain | 5567x4177 | 锚泊远景，主体偏小 |
| File:Prinz Eugen ONI-204-48.JPG | Public domain | 1819x1148 | 识别剪影图，非照片 |
| File:HMS RODNEY.jpg | Public domain | 3341x1432 | **来源可疑**：credit 为 kepfeltoltes.hu（匈牙利图床），非机构来源，已下载后删除 |
| File:HMS Rodney (47263845882).jpg | CC BY-SA 2.0 | 3672x4896 | 现代博物馆模型照，非历史照片 |
| File:HMS Rodney after refitting at Liverpool.jpg | Public domain | 1241x776 | IWM 编号 A 9607，digitized by IWM，保守起见未选 |
| File:HMS Rodney in support of the Normandy landings.jpg | Public domain | 800x616 | IWM 编号 A 23960，同上 |
| File:Rodney&Punjabi1940.jpg | Public domain | 1300x1108 | IWM 编号 A 194，同上 |
| File:HMS Nelson & HMS Rodney.jpg | Public domain | 792x444 | 双舰合影，Rodney 只占一半，且来源为图床 |
| File:HMS King George V and USS Missouri ... (80-G-455703).jpg 之外的 KGV 候选：Battleship HMS King George V - IWM Q 75215.jpg（800x445）、King George V class battleship 1945.jpg（1911x1320） | Public domain | — | IWM Q 编号 / 分辨率不足；站内暂无 kgv id，先不单独建条 |
| File:When a Battleship Puts To Sea. 1940, on Board the British Battleship HMS Rodney. A145.jpg | Public domain | 4529x3508 | IWM A 145，舰内生活场景为主 |
| File:USS Iowa (BB-61) fires broadside c1987.jpg / USS Iowa (BB-61) underway at sea c1952.jpg / 80-G-K-1066 USS IOWA (BB-61).jpg | Public domain | 593x445 / 841x510 / 1034x1280 | 分辨率均低于已选的 3000x1681 那张 |
| File:USS Missouri BB-63 1945.jpg / USS Missouri (BB-63) firing guns in 1946.jpg / USS Missouri (BB-63) at anchor, circa in August 1944.jpg | Public domain | 2057x1626 / 1214x1696 / 5703x4258 | 已有密苏里高清航行照，这些是锚泊或夜间射击，重复度高 |
| File:Yamato during Trial Service.jpg / Yamato sea trials late 1941.jpg / Yamato Sibuyan-Sea.jpg / Yamato battleship.jpg | Public domain | 2000x1201 / 744x515 / 735x495 / 968x310 | 分辨率或角度不如已选的宿毛湾、萨马岛两张 |
| File:Japanese battleship Yamato running trials off Bungo Strait, 20 October 1941.jpg | Public domain | 3430x1756 | credit 为 **Yamato Museum（呉海事科学館）**，按规则清退（已下载后删除） |

### 武器

| Commons 文件 | 授权 | 尺寸 | 不选原因 |
|---|---|---|---|
| File:2-cm-Flak 38.jpg | CC BY-SA 3.0 | 777x777 | 陆用单装，不是四联装舰用炮座 |
| File:Niemiecki okręt wojenny (2-2523).jpg | Public domain | 3500x2456 | **内容不符**：目视确认主体是一门 10.5cm 单装炮，不是 2cm 四联装。已下载后删除 |
| File:Bundesarchiv Bild 193-04-4-16A（15cm 那张的重复下载） | CC BY-SA 3.0 de | 800x532 | 已选，此处仅记录曾有同名重复文件 `15cm-sk-c28-twin-mount.jpg`，因目视确认主体是烟囱基座而改名 `15cm-sk-c28-on-bismarck.jpg` |
| File:Battleship Bismarck port side 15 cm gun.jpeg | **missing** | — | 无 imageinfo |

### 战役 / 历史

| Commons 文件 | 授权 | 尺寸 | 不选原因 |
|---|---|---|---|
| File:The Royal Navy during the Second World War A9798.jpg | Public domain | 800x674 | credit 指向 media.iwm.org.uk，IWM 数字副本 |
| File:Bismarck reconnaissance.jpg | Public domain（PD-UKGov） | 1952x1772 | credit "CS 159 ... Imperial War Museums"，IWM 扫描件，已下载后删除 |
| File:HMS Dorsetshire Bismarck survivors.jpg | Public domain（PD-UKGov） | 2604x3113 | credit "ZZZ 3130C ... Imperial War Museums"，同上，已删除 |
| File:Rodney firing on Bismarck.png | Public domain（PD-UKGov / PD-BritishGov） | 1243x538 | credit "MH 15931 ... Imperial War Museums"，已删除（见下节说明） |
| File:Cruisers Admiral Scheer and Prinz Eugen at Lofjord 1942.jpg | Public domain（PD-UKGov） | 791x660 | credit "C 5627 ... Imperial War Museums"，已删除 |
| File:Battleship Bismarck burning and sinking 1941.jpg | Public domain | 1259x454 | 条幅太窄（长宽比 2.8:1）；且已有 denmark-strait-bismarck-after-action |
| File:Battleship Bismarck under fire and burning 1941.jpg | Public domain | 765x590 | 分辨率低、画质糊 |
| File:Bundesarchiv Bild 146-1998-035-05, Schlachtschiff Bismarck, Seegefecht.jpg | CC BY-SA 3.0 de | 792x529 | 同批次 Lagemann 底片，与已选两张内容重复 |
| File:Bundesarchiv Bild 101II-MN-1361-16A 之外的服役仪式候选 | CC BY-SA 3.0 de | — | 同批底片，构图不如已选那张 |

---

## 二、失败 / 不可用的来源（含错误原文）

### 1. `upload.wikimedia.org` 直连不可用
- 直连 → **curl exit 000（连接失败）**，无响应。
- 走代理 `http://127.0.0.1:7897` → **HTTP 429 Too Many Requests**。
- 结论：**所有图片必须走 `thumb.wikimedia.org`**。

### 2. Commons 缩略图宽度白名单（踩坑两次）
- `iiurlwidth=1600` 直接下载 → **HTTP 400**，原文：
  `Error: 400, Use thumbnail sizes listed on https://w.wiki/GHai`
- 实测放行宽度：**120 / 250 / 330 / 500 / 960 / 1280 / 1920 / 3840**（另 20/40/60 也可）。
- 实测 400 的宽度：800、1000、1024、1152、1440、1500、1536、**1600**、1800、2000、2048、2160、2400、2560、2880、3000、3200、3400、4096。
- 结论：**统一用 `iiurlwidth=1280` + `/1280px-` 路径**；小原图（如 799px）也能上采样出 1280px 缩略图（HTTP 200）。

### 3. `thumb.wikimedia.org` 的"原图路径"无效
- `https://thumb.wikimedia.org/wikipedia/commons/<hash>/<file>`（不带 `/thumb/`）→ **HTTP 301**，`location: https://commons.wikimedia.org/`。加 `-L` 跟随后拿到 **HTTP 200 的 HTML 首页**，不是图片。
- 结论：必须用 `thumb.wikimedia.org/wikipedia/commons/thumb/<hash>/<file>/<W>px-<file>`。

### 4. NHHC（`www.history.navy.mil`）具体照片子页拿不到
- 域名直连 + 浏览器 UA → HTTP 200 可用。
- 但具体子页 `https://www.history.navy.mil/our-collections/photography/numerical-list-of-images/nhhc-series/nh-series/NH-59000/NH-59671.html` 用 `Invoke-WebRequest` 请求报：
  `基础连接已经关闭: 发送时发生错误`
- 试过的两个 NHHC 照片子页全部同样报错，未能验证到任何一张 NHHC 直链。
- 结论：**NHHC 只通过 Commons 上的 PD 扫描件间接使用**，不直连其站点。

### 5. Bismarck 残骸：Commons 上不存在
- 试过的检索词（`srsearch`，`srnamespace=6`）全部无有效结果：
  `Bismarck wreck`、`Bismarck Wrack`、`Bismarck wreck ROV`、`Bismarck 1989 discovery`、`Bismarck seabed`、`Bismarck debris field`、`Bismarck shipwreck photo`、`Bismarck wreck Ballard`，以及 `list=allimages&aiprefix=Bismarck wreck`。
- `Category:Wreck of the Bismarck` → 返回空（分类不存在）。
- `Category:Sinking of the Bismarck` → 返回空。
- 结论：**Commons 没有任何俾斯麦号残骸照片，这是明确缺口**。1989 年 Ballard / 后续 ROV 影像的版权多在 WHOI / Nauticos / 各家纪录片方手里，不在 Commons，也没有 PD 版本。

### 6. `srsearch` 对舰炮关键词基本失效
- `38 cm SK C/34 turret` 的第一名竟是无关键词匹配的 Bundesarchiv 193-05-2-07A，其余全是无关 PDF。
- 结论：**查 Commons 分类用 `action=query&list=categorymembers&cmtitle=Category:...` 比 `list=search` 可靠得多**。本轮 15cm / 38cm 炮塔图的分类归属就是用这个确认的。

### 7. `File:Sinking of HMS Prince of Wales and Repulse 10 December 1941 H12775.jpg`、`File:German Battleship Bismarck.jpg`、`File:Battleship Bismarck port side 15 cm gun.jpeg`
- 三者 `imageinfo` 均返回 `missing: true`（页面无图片文件）。
- 结论：**Commons 上存在页面但没有文件**，不能当候选。

### 8. `File:prinz-eugen-1942-lofjord.jpg` 等曾下载但内容/来源有问题的文件
- `ships/tirpitz-1941-kiel.jpg`：内容是一枚下落中的炸弹，非提尔皮茨 → 删除，换 `tirpitz-1941-broadside.jpg`。
- `weapons/2cm-flakvierling-38-deck.jpg`：主体是 10.5cm 单装炮 → 删除。
- `weapons/38cm-turret-model-1to50.jpg`：来源不明 → 删除，换 CC0 的安特卫普博物馆藏品照。
- `battles/bismarck-1940-stern-view.jpg`：内容是远景剪影不是舰尾 → 改名 `bismarck-1940-at-sea-distant.jpg`。
- `ships/prince-of-wales-1941-halberd-salvo.jpg`：**右下角有 IWM 水印**（目视确认）→ 删除。

---

## 三、判定"不能进仓库"的来源类型（政策结论）

| 来源 | 判定 | 依据 |
|---|---|---|
| **IWM 数字副本**（credit 里出现 `media.iwm.org.uk`，或编号形如 `MH 15931` / `C 5627` / `CS 159` / `ZZZ 3130C` / `A 23960`） | 保守清退 | IWM 站点条款禁止 upload to third party sites such as Wikimedia；本站 `data/sources.yaml` 已有 `iwm-noncommercial` 条目。**注意**：Commons 上这些文件的作品本身多为 `PD-UKGov` / `PD-BritishGov`（1957 年前皇家版权已过期），权利人层面已属公有领域，争议在于数字副本的来源条款 |
| **Yamato Museum / 呉海事科学館** | 清退 | 馆藏条款限制再利用 |
| **Europeana NoC-NC** | 清退 | 非商业授权 |
| **任何 "Editorial use only"** | 清退 | 不可用于常规站点 |
| **个人图床**（kepfeltoltes.hu、navsource.net 等） | 需谨慎 | 图片本身标 PD，但上传链非权威机构；`HMS RODNEY.jpg` 因此被弃用 |

---

## 四、脚本与中间产物

| 文件 | 作用 |
|---|---|
| `work/img/commons.py` | Commons API 封装：`search()` / `info()`，2.5s 限速防 429 |
| `work/img/fetch.py` | 缩略图下载：`thumb_path()` 改写 thumb.wikimedia.org 路径，`download()` 校验 Content-Type 与字节数，超 500KB 自动降宽度 |
| `work/img/probe.py` | 500px 探针下载，用于拼 contact sheet 目视筛图 |
| `work/img/build_manifest.py` | 生成 `work/img/manifest.json`（从 extmetadata 实时取授权，不硬编码） |
| `work/img/map_final.json` | 本地文件名 → Commons 标题映射 |
| `work/img/meta*.json` / `lic_final.json` | 各轮 extmetadata 原始快照 |
