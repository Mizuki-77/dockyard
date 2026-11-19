# 图源与授权调研（image-sources）

> 用途：为战舰资料站确定「图片从哪来、能不能用、怎么标」。
> 调研日期：2026-11-17。所有授权结论均以各机构官网原文为依据，原文引用见文末「证据附录」。
> 标注约定：**✅ 已核** = 直接抓到机构官网条款原文；**⚠️ 待确认** = 站点不可达 / 条款未取到，**不得据此下结论**。

---

## 一、可用图源清单

| 机构 | 二战军舰照片 | 在线可得 | 授权类型 | 要求署名 | 可商用 | 高清免费 | API / 批量 | 结论 |
|---|---|---|---|---|---|---|---|---|
| **NHHC**（history.navy.mil，美国海军历史与遗产司令部） | ✅ 有，馆藏 100 万+ 张，明确「particular focus on the World War II era」 | ✅ 有站内搜索；每图下方 low/med/high 三档 Download | 多数为美国联邦政府作品 → Public Domain；少数在图片说明的 copyright 栏另行标注 | 署名是 **requested 非强制**：「It is requested that any photograph or document used in print or online credit the Archives」 | ✅ 可 | ✅ 免费（三档下载） | ⚠️ 官网未提及公开 API（未发现，不等于不存在）；委托扫描限 5 张/月/人 | **本站主力源** |
| **Library of Congress**（loc.gov） | ✅ 有，但分散在各套装与捐赠集合 | ✅ 可 | 联邦雇员职务作品 → PD / CC0；其余每件看 **"Rights and Access" / "Rights Advisory"** 字段 | 依件而定 | 联邦作品 ✅；其余需逐件判断 | ✅ | ⚠️ 官方 legal 页仅说明限速 **10 requests/minute**；结构化导出接口本次未核实 | **主力源（须逐件看 rights 字段）** |
| **NARA**（archives.gov / catalog.archives.gov） | ✅ 有；已核实的相关线索是 **RG 71**（Bureau of Yards and Docks 约 10 万张船厂/船坞图纸，含约 3 万张二战时期），舰体总图亦存于其 Cartographic and Architectural Branch | ✅ Catalog 在线检索 | 一般联邦作品 → PD；NARA 自产作品 **CC0 1.0**；外来捐赠/他机构来源可能受限 | 署名是 **请求非强制**：「we ask that we credit us as the source」 | ✅ 一般可 | ✅ | ✅ Catalog API，需申请 key，**10,000 queries/月**；条款明令「Please do not cache or store any content returned by the API」 | **主力源（图纸来源）** |
| **IWM**（iwm.org.uk，帝国战争博物馆） | ✅ 有，且含大量缴获的德国资料 | ✅ standard-resolution 可免费下载 | **IWM Non-Commercial Licence** | ✅ **强制**，格式 `© IWM (藏品号)` | ❌ **不可** | ❌ 高清不提供在线，需付费 | ❌ | **只能外链，且本站必须无广告无赞助** |
| **Bundesarchiv Bildarchiv**（bild.bundesarchiv.de） | ✅ 有，核心是 **Bild 101**（国防军宣传连 Wehrmacht Propagandakompanien） | ✅ 在线约 43 万张，免注册可检索 | ⚠️ **官网条款页未出现 CC-BY-SA 3.0 de 字样**；需逐张确认 | 依具体授权 | ⚠️ 需逐张确认 | ⚠️ 「Das Herunterladen und Nutzen von reproduktionsfähigen Bildern ("HighRes") ohne Wasserzeichen ist für registrierte Benutzer ggf. kostenpflichtig」= 无水印高清**可能收费** | ❌ 无公开 API，需递 Antrag 表 | **待确认，不能整库当 CC 用** |
| **海上自衛隊**（mod.go.jp/msdf） | ⚠️ 未取到 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | **待确认** |
| **呉市海事歴史科学館 / 大和ミュージアム** | ✅ 有（含 1/10 大和、馆藏照片与图纸） | ❌ 不外挂，需申请 | 馆方个别许可，**1 点 3,000 日元**使用料 | ✅ **强制**：`資料提供　大和ミュージアム` | 需申请（付费） | ❌ 非免费 | ❌ | **只能申请授权，不能当免费源** |
| **JACAR**（国立公文書館 アジア歴史資料センター） | ⚠️ 条款页 404，未取到 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | **待确认（勿猜）** |
| **AWM**（awm.gov.au，澳大利亚战争纪念馆） | ⚠️ 站点全路径 403/429，正文不可达 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | **待确认（勿猜）** |
| **Library and Archives Canada**（library-archives.canada.ca） | ⚠️ 站点超时/429 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | **待确认（勿猜）** |
| **Wikimedia Commons** | ✅ 有海量二战军舰图（多为 NHHC/IWM/Bundesarchiv/NARA 的二次转载） | ✅ | **逐文件不同**：PD / CC0 / CC-BY / CC-BY-SA | 依许可；**须署原作者，不是上传者** | 依许可（PD/CC0/CC-BY/CC-BY-SA 可） | ✅ | 有 MediaWiki API（本次不可达） | **只作索引入口，必须回溯原始机构** |
| **Flickr Commons** | ⚠️ 页面 ECONNRESET 未取到 | ⚠️ | 通称 "no known copyright restrictions"，但**本次未抓到原文** | ⚠️ | ⚠️ | ⚠️ | ⚠️ | **待确认** |
| **Europeana** | ✅ 聚合，含大量海军影像 | ✅ | **逐条 rights statement**，大量为 **NoC-NC 1.0「no copyright, non-commercial only」** | 依条 | ❌ 多数不可 | 依条 | ⚠️ API 本次未核实（站点 Cloudflare 拦截） | **多数只能外链** |

### 一句话分类

- **可本地归档（PD/CC0，可商用，无强制署名）**：NHHC（官方照片主体）、NARA 联邦作品、LOC 联邦作品。
- **可本地归档但有义务（CC-BY / CC-BY-SA）**：Commons 上明确标 CC-BY / CC-BY-SA 的单件；Bundesarchiv 中逐张确认为 CC-BY-SA 3.0 de 的那批。
- **只能外链**：IWM 全站、大和ミュージアム、Europeana 的 NoC-NC 条目、一切 "Editorial use only"。
- **待确认前不得使用**：AWM、LAC、JACAR、Flickr Commons、海上自衛隊。

---

## 二、模型制作者要的「细节图」从哪来

官方档案的战争照多是远景、侧影、烟幕，模型制作者要的是**分件、甲板走向、炮塔细节、舷侧板缝**。这部分必须另找渠道。

### 2.1 舰船博物馆实物照

现实情况：**博物馆官网的照片几乎全部保留版权，不能直接转载。**

| 博物馆 | 站点页脚版权声明（实测） |
|---|---|
| Battleship IOWA / Pacific Battleship Center | `© 2026 Pacific Battleship Center, a 501(c)(3) nonprofit organization` |
| Battleship Texas Foundation | `© 2026 The Battleship Texas Foundation` |
| USS Missouri（ussmissouri.org） | 站点证书链异常，未能取到正文 → ⚠️ 待确认 |

**可行路径**：**自己拍**。这是唯一无需授权的细节图来源，且模型站的核心竞争力常就在这里。

自摄注意：
- 尊重馆方现场规定（三脚架、闪光灯、无人机、商业拍摄常需报备）。
- 现役舰（如仍在役的同级舰）多属军事设施，拍摄受限；博物馆舰（Iowa、Missouri、Texas、Belfast、Mikasa）属展陈场所，通常允许个人拍摄。
- 自摄照片版权归拍摄者本人，可自由商用；但若画面中出现他人可识别的肖像、或馆方展签/图版的翻拍，那部分另论。

### 2.2 3D 扫描 / 官方线图项目

**结论：NHHC 不提供印刷复制品，也不提供 Booklet of General Plans 的在线下载。** 官方原文：

> 「Note that while NHHC is unable to provide print reproductions, you may download digital reproductions (image files) by clicking "Download" below the photos you see on our site.」

NHHC 的 *Sources Of Ship Plans* 页把图纸来源指向两处：

1. **NARA Cartographic and Architectural Branch**（College Park, MD）——「Their collection includes the general plans and drawing of most ships stricken from the Naval Vessel Register.」**单次请求限 3 艘**。
2. **Smithsonian（National Museum of American History, History of Technology Division）**——black-line 复制品**出售**，需按其出版物目录下单。

另有一条相关馆藏线索：Bureau of Yards and Docks 的建筑/结构图约 10 万张（1870s–1950s，其中约 3 万张为二战时期），属 NARA 的 RG 71，多为船厂、船坞、码头设施图——对「船厂建造场景」类配图有用，不是舰体分件图。

### 2.3 公有领域线图：US Navy Booklet of General Plans

- **法理依据**：BOGP 由美国海军船厂/海军部编制，属 17 U.S.C. §105 意义上的美国联邦政府职务作品，**不受版权保护，属公有领域**。这一点与 NHHC 的官方表述一致（「Official government photographs and documents are in the public domain」）。
- **但托管地址未确认**：本次实测 HNSA（hnsa.org）的 manuals 库页面 64KB 正文里**没有任何 "plan" 字样**，`/manuals-documents/booklets-of-general-plans/`、`/plans/` 全部 404；`maritime.org/doc/` 返回 504。→ **BOGP 的可靠下载入口 ⚠️ 待确认**，不能凭印象写网址。
- **两个必须留意的例外**：
  1. 部分 BOGP 图纸由私营船厂绘制（Newport News、Bethlehem、Fore River 等），这类图纸的版权归属需逐张判断，**不能默认 PD**。
  2. 后期版本的 BOGP 可能含第三方补充内容，同样需看图纸标题栏的绘制单位。

**给站点的实际建议**：BOGP 类线图优先级高（对模型制作者价值最大），但落地前必须先解决「从哪拿」——建议先通过 NARA Catalog 检索 `Booklet of General Plans`，确认在线可用条目后再归档。

### 2.4 模型厂商说明书与树脂件照片——**明确不可用**

结论：**不可用**。理由分四层，任何一层单独成立就足够：

1. **说明书文字与插图**是厂商的受版权保护作品（文字作品 + 图形作品），未经许可复制即侵权。
2. **厂商产品照**是产品摄影，著作权归厂商或其委托摄影师；「我在官网看到的图」不等于「可以转载的图」。
3. **树脂改件、蚀刻片成品的照片**即使是你自己拍的，展示的仍是他人产品的**外观设计**；用于评测通常属合理使用范畴，用于「图库」则越界。
4. 模型厂商普遍在说明书与官网明确禁止转载（需逐一核对各厂条款，本次未逐个抓取）→ 具体到某厂时 ⚠️ 需单独确认。

**可接受的替代做法**：站内只写「该厂 XX 号套件提供了 XX 部位的树脂件」，不贴图；或贴**自己购买并自己拍摄**的开盒照，并注明「图片为本站自摄，非厂商提供」。厂商 logo 属商标，引用时不得暗示背书。

---

## 三、授权类型速查表

| 授权类型 | 能否商用 | 是否要求署名 | 是否要求同协议共享 | 典型来源 |
|---|---|---|---|---|
| **Public Domain（版权过期）** | ✅ 可 | ❌ 不要求（学术惯例上仍建议） | ❌ | LOC 原文：「Most items published in the United States more than 95 years ago are now in the public domain.」（2026 年即 1931 年前出版物） |
| **Public Domain（US Federal Government work，17 U.S.C. §105）** | ✅ 可 | ❌ 法律不要求；NHHC/NARA 只是「request」 | ❌ | NHHC 官方照片与文件、NARA 联邦档案、LOC 联邦作品 |
| **CC0 1.0** | ✅ 可 | ❌ 法律不要求 | ❌ | NARA 自产作品、LOC 联邦作品的国际复用 |
| **CC BY（如 4.0）** | ✅ 可 | ✅ **必须**：appropriate credit + 许可链接 + 声明是否改动 | ❌ | Commons 部分文件、部分馆藏开放数据 |
| **CC BY-SA（3.0 / 4.0）** | ✅ 可 | ✅ 必须（同 CC BY） | ✅ **必须**：改编作品须以同协议发布 | Commons 部分文件 |
| **CC BY-SA 3.0 DE** | ✅ 可（「sogar kommerziell」） | ✅ 必须（Namensnennung + 许可链接 + 是否改动） | ✅ 必须（Weitergabe unter gleichen Bedingungen） | Bundesarchiv 与德语维基合作释出的那批（**仅限特定 Bestand，非整库**） |
| **Bundesarchiv 一般使用条款（非 CC）** | ⚠️ 逐张确认 | ⚠️ 依约 | ⚠️ 依约 | bild.bundesarchiv.de 的其余藏品；高清可能收费 |
| **IWM Non-Commercial Licence** | ❌ **不可** | ✅ 强制，`© IWM (藏品号)` | ❌ | iwm.org.uk 全站（除标注 "Share and Reuse" 的条目） |
| **NoC-NC 1.0（no Copyright, Non-Commercial Use Only）** | ❌ 不可 | 依来源机构 | ❌ | Europeana 大量条目、公私合作数字化项目 |
| **InC 1.0（In Copyright）** | ❌ 需取得许可 | 依权利人 | ❌ | Europeana / 各馆在线藏品的默认状态 |
| **Editorial use only** | ❌ 不可（仅限新闻报道、评论、教育等编辑语境） | 通常要 | ❌ | 商业图库、部分新闻社供稿。**注：这是行业惯用条款类型，本次未抓到某家机构的原文定义，具体含义以该图库的 licence 文本为准（⚠️ 逐家确认）** |

### 三条容易搞混的边界

- **CC BY-SA 的「传染」对象是改编作品，不是引用它的网页。** 你在文章里嵌一张 CC BY-SA 图并署名 → 你的**文章**不必 CC BY-SA；你把图裁切/上色/加标注后做成自己的图集 → 那个**图集**要 CC BY-SA。
- **CC0 与 PD 的差别只在来源叙事**：CC0 是权利人主动放弃，PD 是版权本来就不存在或已过期。对使用者的实际义务基本一致（都不强制署名）。
- **「Government work」不是全球通用概念**。美国联邦作品 PD，但英国（Crown copyright）、加拿大（Crown copyright）、澳大利亚（Commonwealth copyright）都另有国家版权，且常保留部分权利。**不要把「美国 PD」外推到英/加/澳的政府照片。**

---

## 四、给这个站的建议

### 4.1 哪些本地归档，哪些只能外链

**本地归档（下载并存进 `assets/`）**

- NHHC 官方照片（PD 主体）——注意避开标注了 copyright 的个别条目，以及 personal papers collections。
- NARA 中明确 PD 的条目。
- LOC 中 "Rights and Access" 显示 PD / CC0 的条目。
- Commons 上明确标 PD / CC0 / CC-BY / CC-BY-SA 的单件（同时记录**原始机构**，别只记 Commons）。
- 本站自摄的博物馆照片。
- BOGP 线图（待确认来源后）。

**只能外链（`<a href>` + 图注，不下载）**

- IWM 全站：既不能商用，也不能「上传到第三方站点」，且禁止裁剪/上色。**外链时不得用 IWM 的图做缩略图缓存**。
- 大和ミュージアム：需付费申请，外链到其藏品页。
- Europeana 中 NoC-NC / InC 的条目。
- 任何 "Editorial use only" 素材。
- AWM / LAC / JACAR / Flickr Commons / 海上自衛隊：**待确认前一律只外链、不加图注授权声明**。

**NARA 的特殊约束（容易忽略）**：Catalog API 条款写明 「Please do not cache or store any content returned by the API.」→ **通过 API 拿到的元数据不要落库**。但图片本身若为 PD，可另从图片直链或 NHHC 站内 Download 获取后归档——两件事分开处理。

### 4.2 页面署名格式模板

统一用一个字段结构，前端渲染成一行小字 + 一个「授权详情」浮层：

```
字段：Title / Creator / Institution / Accession no. / License / Source URL / Retrieved / Modifications
```

**模板 A — NHHC（PD，署名是礼貌非义务）**

> *[舰名与场景]*，NH [编号]，courtesy of the Naval History & Heritage Command（Public Domain）。
> 来源：`https://www.history.navy.mil/...`，获取于 2026-11-17。本站已裁切/缩放，未改动内容。

NHHC 原文格式要求：`NH 1234 courtesy of the Naval History & Heritage Command`；若图片说明里注明来源是别的机构（如 National Archives），**改署那个机构**。

**模板 B — NARA（PD / CC0）**

> *[标题]*，Record Group [编号]，National Archives and Records Administration（Public Domain）。
> 来源：`https://catalog.archives.gov/id/[id]`，获取于 2026-11-17。

若用到 Catalog API 开发的功能，页面需展示：`This product uses the National Archives Catalog API but is not endorsed or certified by the National Archives and Records Administration.` 且**不得使用 NARA 的 logo / 徽标**。

**模板 C — CC BY / CC BY-SA（含 Commons 转载）**

> *[标题]*，作者 [**原作者姓名，不是上传者**]，[原始机构]，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。
> 来源：`[原始机构页面]`（经 Wikimedia Commons），获取于 2026-11-17。本站已裁切，未改动内容。
> 若为 CC BY-SA：本图及基于本图的改编内容以 [CC BY-SA 4.0](...) 发布。

CC 的硬性三要素：**appropriate credit + 许可链接 + 声明是否改动**。缺一项即不合规。

**模板 D — IWM（仅外链，不下载）**

> 图片来源：[Imperial War Museums](https://www.iwm.org.uk/collections/item/object/[编号])，`© IWM ([编号])`。
> 依据 IWM Non-Commercial Licence 展示，本站为非商业性资料站，无广告、无订阅、无商品销售、无募捐入口。

**模板 E — 大和ミュージアム（如获授权）**

> 資料提供　大和ミュージアム

### 4.3 最容易踩的版权坑（按危险程度排序）

1. **IWM 的「非商业」卡的是站点的商业模式，不是「你这一次的用途」。** 条款明确：网站上一旦有广告、商品销售、订阅、placement、donation，就不再属于 allowed use。而这类资料站最常见的变现路径恰是广告与周边。**更狠的是它还禁止裁剪与「upload to third party sites such as Wikimedia」**——所以「Commons 上有 IWM 的图」这件事本身说明那张图是违规上传，不能因为在你手上就变合法。

2. **「美国政府作品 = 公有领域」不能外推。** 至少三处破例：
   - NHHC 的 personal papers collections：「may not be reproduced in print or online without permission from the Archives Branch」。
   - NARA：「not all materials appearing on this website are in the public domain」，部分为捐赠或他机构来源，「Permission to use these images should be obtained directly from those organizations」。
   - LOC：每件都要看 "Rights and Access" / "Rights Advisory"，「Just because we've put a work online doesn't mean that you can freely reuse it.」
   - 另外，即便是美军拍的照片，画面里也可能夹着船厂（私营企业）拍摄的工程照。

3. **把 Bundesarchiv 整库当 CC-BY-SA 3.0 de 标注，等于编造授权。** 本次实测其官网使用条款页**没有出现 CC-BY-SA 3.0 de 字样**，只有「注册免费、无水印高清可能收费、需递 Antrag」。CC-BY-SA 3.0 de 是当年与德语维基百科的合作协议，覆盖的是特定 Bestand 的一批图。**逐张确认，确认不了就写「需进一步确认」并只外链。**

4. **署名写错对象。** Commons 上要署的是**原作者**（「it is the content creator who must be credited, not the uploader」），不是上传者；转载 Commons 文件必须回溯原始机构（Bundesarchiv / NARA / NHHC），否则授权链断裂。此外 Commons 免责声明明确「the Wikimedia Foundation does not provide any warranty regarding the copyright status」——**Commons 的授权标签不是担保**。

5. **忘了「同一张图在不同馆有不同授权」。** 同一艘 Bismarck 的照片，NHHC 版本可能是 PD，Bundesarchiv 版本可能是 CC-BY-SA 3.0 de，IWM 版本是非商业许可。**授权跟着「这张具体的数字化副本」走，不跟着「这个历史事件」走**。归档时必须记录来源机构 + 藏品号，不能只记文件名。

---

## 附录：证据等级与原文出处

| # | 机构 | 页面 | 状态 |
|---|---|---|---|
| 1 | NHHC | https://www.history.navy.mil/about-us/services-and-policies/scan-copyright.html | ✅ 已抓（Published Fri Oct 27 2017） |
| 2 | NHHC | https://www.history.navy.mil/our-collections/photography.html | ✅ 已抓 |
| 3 | NHHC | https://www.history.navy.mil/about-us/instructions-and-forms/obtain-duplications-of-records-and-photos.html | ✅ 已抓 |
| 4 | NHHC | https://www.history.navy.mil/research/histories/ship-histories/sources-of-ship-plans.html | ✅ 已抓（Published Mon May 18 13:13:51 EDT 2026） |
| 5 | NHHC | https://www.history.navy.mil/research/archives/resources-for-researchers/research-guide-drawings-maps-charts-buildings-structures-installations-us-navy.html | ✅ 已抓 |
| 6 | IWM | https://www.iwm.org.uk/corporate/policies/non-commercial-licence | ✅ 已抓（Last updated December 2024） |
| 7 | IWM | https://www.iwm.org.uk/commercial/collections-sales-licensing | ✅ 已抓 |
| 8 | Bundesarchiv | https://www.bundesarchiv.de/im-archiv-recherchieren/archivgut-recherchieren/recherchesysteme/digitales-bildarchiv/ 及 …/nutzung-von-bildern-und-plakaten/ | ✅ 已抓（**无 CC-BY-SA 3.0 de 字样**） |
| 9 | CC | https://creativecommons.org/licenses/by-sa/3.0/de/ | ✅ 已抓（德文 deed 全文） |
| 10 | CC | https://creativecommons.org/licenses/by/4.0/ 与 https://creativecommons.org/publicdomain/zero/1.0/ | ✅ 已抓 |
| 11 | NARA | https://www.archives.gov/global-pages/privacy.html | ✅ 已抓（last reviewed October 16, 2026） |
| 12 | NARA | https://www.archives.gov/research/catalog/help/api | ✅ 已抓（12.9KB） |
| 13 | LOC | https://www.loc.gov/legal/understanding-copyright/ | ✅ 已抓（17.6KB） |
| 14 | LOC | https://www.loc.gov/legal/ 与 https://www.loc.gov/free-to-use/ | ✅ 已抓 |
| 15 | Wikimedia Commons | https://commons.wikimedia.org/wiki/Commons:Reusing_content_outside_Wikimedia | ✅ 已抓（raw wikitext 全文） |
| 16 | RightsStatements | https://rightsstatements.org/page/InC/1.0/ 、/InC-EDU/1.0/ 、/NoC-NC/1.0/ 、/NoC-OKLR/1.0/ | ✅ 已抓 |
| 17 | 大和ミュージアム | https://yamato-museum.com/ 照片・図面資料の使用について | ✅ 已抓 |
| 18 | AWM | https://www.awm.gov.au/about/copyright | ⚠️ **未取到**（全路径 403 / 429，仅 footer「All rights reserved」） |
| 19 | LAC | https://library-archives.canada.ca/…/copyright | ⚠️ **未取到**（超时 / 429） |
| 20 | JACAR | https://www.jacar.go.jp/english/terms/ | ⚠️ **未取到**（404） |
| 21 | Europeana | https://www.europeana.eu/en/rights | ⚠️ **未取到**（Cloudflare challenge） |
| 22 | Flickr Commons | https://www.flickr.com/commons/usage/ | ⚠️ **未取到**（ECONNRESET） |
| 23 | 海上自衛隊 | https://www.mod.go.jp/msdf/ | ⚠️ **未取到** |
| 24 | Booklet of General Plans 托管地 | （HNSA / maritime.org 均未定位） | ⚠️ **未确认** |

> 待确认项的处理原则：**在拿到机构原文之前，一律按「不可本地归档」处理，只做外链，且不写授权声明。** 宁可少一个源，不要编一条条款。
