# HUD/AR-HUD 行人碰撞预警综合研究项目 — 总索引

> **最后更新**：2026-08（v2）
> **旧版本**：v1（40 篇口径）已备份为 `README_v1_40篇口径.md.bak`；一阶段版本见 `README_phase1.md`。

## 项目概览

本项目是关于 **AR-HUD 行人碰撞预警的时间—空间元素设计规范** 的系统文献研究与实验方案设计。

| 项目 | v1（2026-06） | **v2（2026-08）** |
|---|---|---|
| 文献总量 | 40 篇 | **102 篇**（`papers/01–102`） |
| 全文 PDF | 40 篇 | **77 篇**（其余 25 篇为硬付费墙，仅有摘要） |
| summaries | 40 篇 | **102 篇**（仅摘要者已在表头显式标注「资料来源：仅摘要」） |
| 实验方案 | 4 个实验 | **5 个实验**（新增实验 1：自发察觉基线标定） |
| 核心时间自变量 | 绝对 TTC（5.0/3.0/2.0 s） | **相对提前量 $\Delta t = t_0 - t_{warn}$ × 触发准则类型（固定时间／BTN）** |
| 统一风险量 | 无（时间用 TTC、空间用「风险」） | **BTN $= a_{req}/a_{max}$**，时间侧触发与空间侧编码共用 |
| 危险状态机 | 定性描述（§4.6） | **可实现状态机（§9.8）**：S0–S5 六状态、BTN 阈值 0.15/0.30/0.70/1.0、退出取 1/2、三条禁令、与五实验一一对应 |

---

## 文件结构

```
HUD/
├── papers/                          ← 77 个 PDF 全文（01–102 中已获取者）
├── extracted_text/                  ← 98 个文本提取（PyMuPDF）
├── summaries/                       ← 102 篇中文精读笔记 ⭐
├── summaries_brief_backup/          ← 老版本简略笔记（备份）
├── _deprecated_summaries_dup/       ← 并发补写产生的重复稿，**不得引用**（见其 NOTICE.md）
├── agent_outputs/                   ← 分批结构化数据（时空参数）
│
├── papers_metadata.json             ← 102 篇元数据（含 abstract、local_pdf、source_list）
├── download_log_2026-08.json        ← 本轮下载成败日志
├── jcr_quartile_data.json           ← 期刊 JCR 分区
│
│  ── 理论与综述 ──
├── 时间元素设计参数_专题分析.md          ← 时间专题（v2 已并入新证据）⭐
├── 空间元素设计参数_专题分析.md          ← 空间专题（v2 新增第六章）⭐
├── AR-HUD行人碰撞预警_毕业论文大纲与危险判定文献综述.md  ← 大纲 + 危险状态机（v2 第九节；**§9.8 = 可实现状态机**）⭐
├── AR-HUD行人碰撞预警_毕业论文研究框架.md ← 五实验递进结构与论证契约（v2 已修订；**§14 变量文献支撑 + §15 APA 7th 参考文献**）⭐⭐
│
│  ── 本轮核心产出 ──
├── 优化方案_预警时间参数理论化重构与执行计划.md  ← 三重约束 + 一个零点模型 ⭐⭐
├── 实验1_自发察觉基线标定_文献与设计依据.md      ← 新增实验 ⭐
├── 实验2_单层时间参数筛选_文献与设计依据.md      ← v2 见 §10
├── 实验3_分层预警升级规则_文献与设计依据.md      ← v2 见 §7
├── 实验4_空间参照系与锁定策略_文献与设计依据.md  ← v2 见 §8
├── 实验5_风险演化动态_文献与设计依据.md          ← v2 见 §9
│
│  ── 表格与呈现 ──
├── HUD_AR-HUD_行人预警_时空设计_新表.{csv,md,tsv}  ← 主综合表（19 列，40 篇口径）
├── HUD_AR-HUD_行人预警_文献综合表.{csv,md,tsv}     ← 一阶段综合表
├── 研究汇报_2026_08.{html,pptx} + _讲稿.md         ← 主线汇报稿 25 页（14 讲述 + 11 备查）⭐⭐
├── 文献综述_幻灯片.{html,pptx} + _讲稿.md          ← 文献综述汇报稿 37 页 ⭐⭐
├── 审核意见与翻修记录_2026_08.md                    ← 三轮导师式审核台账 ⭐
├── PPT_开题报告_HUD_AR-HUD时空设计规范.pptx        ← 38 页开题报告 PPT（旧版，40 篇口径）
├── PPT_开题报告_大纲.md
├── 参考模板_音乐流派对驾驶行为影响的多维分析_周颖2024.md  ← 体例基准（周颖 2024 硕士论文全文转录）
│
│  ── 论文正文 ──
├── thesis/第1章_研究背景及意义.md                   ← v2（102 篇口径、三重约束、RQ1–RQ3、O1–O4）⭐
├── thesis/第2章_文献综述_v2.md                      ← 七环节 + 七组冲突 + 九项空白 + H1–H15 ⭐⭐
├── thesis/第3章_研究内容与预期目标.md               ← 五实验分工、判定顺序、设定值清单 ⭐
├── thesis/附录_空间维度简表.md
│
│  ── 盲区框架（平行框架，按视线可见性切分）──
├── 盲区框架/                        ← 独立交付子目录，含 3 份 deck + 讲稿 + pptx、thesis/、实验依据、校验脚本
│
│  ── 清单与报告 ──
├── ar-hud参考文献列表.md            ← 补充清单一（46 条 → 去重后 29 条新增）
├── HUD行人碰撞预警_风险时机判断_论文清单.md  ← 补充清单二（40 条 → 去重后 33 条新增）
├── 最终交付清单.md / REVIEW_REPORT.md / PHASE2_REPORT.md / 数据源提供性_汇总.md
│
└── scripts/                         ← 检索、下载、摘要收割、元数据合并、呈现与校验脚本
    ├── SUMMARY_SPEC.md              ← summaries 撰写规范 ⭐
    ├── shoot_slides.py                     ← deck 逐页截图 + 版心溢出探针（out 参数不带 figures/ 前缀）⭐
    ├── html2pptx.py                        ← HTML deck → **可编辑** PPTX（原生文本框／表格，非图片化）⭐⭐
    ├── verify_pptx.py                      ← PPTX 七项校验（时效性、页数、文本覆盖、越界、估算溢出、表格行高、可编辑性）⭐
    ├── verify_deck_talk.py                 ← deck 与讲稿的页数、标题逐字、分块、计时一致性 ⭐
    ├── verify_style.py                     ← 表达禁则、四类构念齐备、RQ／O 编号成套 ⭐
    ├── audit_all.py                        ← 第一轮审计：旧术语、页面结构、数值一致、编号成套 ⭐
    ├── audit_round2.py                     ← 第二轮审计：引注可追溯、配额可行性、备答覆盖、单页字数 ⭐
    ├── build_blind_review_deck.py / build_blind_review_talk.py  ← 盲区专题综述 deck 与讲稿**生成器**（改内容须改此处）
    ├── reflist_new.py / reflist2.py         ← 两份清单解析 + 去重
    ├── resolve_refs.py                      ← Crossref 校验
    ├── download_new.py / download_list2.py / download_manual.py
    ├── harvest_abstracts.py                 ← 多源摘要收割（Crossref/S2/EuropePMC/OpenAlex/DOAJ）
    ├── merge_metadata.py                    ← 合并进 papers_metadata.json
    ├── convert_template_pdf.py              ← 模板 PDF → Markdown
    ├── enrich_apa.py                        ← Crossref 批量补齐卷/期/页（APA 必需字段）
    ├── patch_apa_verified.py                ← 人工核实后的题录修正（9 处）
    ├── build_apa_refs.py                    ← 生成 APA 7th 条目 ⭐
    ├── apply_verification_fixes.py          ← 把核验结论回写全库
    ├── apa_crossref_raw.json                ← 102 篇的 Crossref/theses.fr/arXiv 核验原始数据
    └── apa_refs.json / apa_refs_preview.md  ← 102 篇 APA 7th 条目与逐条预览 ⭐
```

---

## v2 的四项实质变化

### 1. 核心时间自变量由「绝对秒数」改为「相对提前量」

v1 的 5.0 / 3.0 / 2.0 s 分别取自三篇车速、模态、分心条件都不同的研究。v2 改为

$$\Delta t = t_0 - t_{warn}$$

其中 $t_0$ 为驾驶员在无辅助条件下的自发察觉时刻，由**实验 1** 标定。三个水平为 $\Delta t \approx 0$（同步确认）、$+1.0$ s（覆盖 SPIDER 的 S+I 窗口）、$+2.5$ s（充裕窗口，检验收益递减）。

文献先例：#74（Abe & Richardson 2006）已用「驾驶员无报警条件下自主松油门时刻均值 **0.72 s**」作为判断报警早/晚的操作化阈值，据此发现信任由 **7.3 降至 4.3**（$F(1,115)=118.32$）。

### 2. 触发准则升为独立自变量：固定时间阈值 vs BTN

同一 TTC 在不同车速下对应的避险所需减速度差别很大（3.0 s 在 40 与 60 km/h 下的 $a_{req}$ 相差 1.5 倍）。BTN $= a_{req}/a_{max}$ 把车速内生化。工程先例：#99（Takada 2014，DCA 阈值 4.0/2.0 m/s² 的 2:1 滞环）、#102（Volvo CWAB-PD）、#73（A-TTC 动态标定后骚扰报警占比 13.74%、威胁召回 89.25%）。

### 3. 新增实验 1（自发察觉基线标定）

2（车速 40/60）× 2（遮挡 无/有）被试内，**全程无预警**。产出 $t_0$ 分布、PRT 分布、$a_{req}$ 可行域、系统渲染延迟、方差成分。理论校验值：τ 理论按 $\dot\theta_{th}=0.003$ rad/s 推算 60 km/h 无遮挡下 $t_0 \approx$ **3.2 s**，与 #02 实测的约 3 s 吻合。

### 4. 全部实验补上此前缺失的三个维度

| 维度 | 加在哪 | 依据 |
|---|---|---|
| **系统可靠性**（虚警率） | 实验 3 第二自变量（R100 / R80，虚警只施加在 L1） | #82（15% 误报无效应，但其提示提前 11–13 s 且不要求动作）与 #74（时机偏差引起强信任变化）共同界定的边界 |
| **背景视觉复杂度** | 实验 4 第二自变量（低/高拥挤） | #79（视觉拥挤 × 刺激位置）、#52（DBC 三维度量化框架） |
| **次任务负荷**（2026-08 新增） | 实验 4 区块 F 自变量（纯音乐／意图诱导型听觉问答） | #80（副任务沉浸度主效应 η² = 0.886，而「闪烁 × 沉浸度」交互 p = .126 不显著）、#14（分心下最长制动反应时 2.5 s）、#58（分心残留 > 30 s） |
| **映射函数形态 / 预测误差** | 实验 5 第三自变量与探索区块 | #90（离散四档）vs #99（连续条形）；#87 的意图预测精度上限 85.02% |

---

## 汇报交付物与校验入口（2026-08）

### 五份汇报稿（HTML + 讲稿 + 可编辑 PPTX 三件套）

| # | 汇报稿 | 页数 | 配额 | PPTX 规模 |
|---|---|---|---|---|
| 1 | `研究汇报_2026_08.html` | **25**（14 讲述 + 11 备查 p15–p25） | 16 分 10 秒 | 25 页 / 424 个可编辑对象 |
| 2 | `文献综述_幻灯片.html` | 37 | 33 分 10 秒 | 37 页 / 674 个可编辑对象 |
| 3 | `盲区框架/研究汇报_双情境框架.html` | 13 | 19 分 40 秒 | 13 页 |
| 4 | `盲区框架/开题报告_双情境框架.html` | 14 | 20 分 50 秒 | 14 页 |
| 5 | `盲区框架/文献综述_盲区情境.html` | 14 | 17 分 0 秒 | 14 页 |

**两轨制计时口径**（须先读）：讲稿中 `⏱` 标注的是该页的**讲述配额**，不是逐字稿的朗读时长。逐字稿全文朗读时长按 245 字/分钟另行标注于各讲稿头部（分别约 30／110／35／49／32 分钟），其作用是备稿与应答，**不用于全文朗读**。不变量为「每页『只说一句』须能在本页配额内讲完」，由 `audit_round2.py [G]` 机检。

**数值口播约定**：投影上的表内统计量、括注内次级参数与备查页数值属备查性质，不逐一口播；讲稿只覆盖参数锚点数值、构成结论冲突两端的数值与本研究推导的校验值。

### 校验入口（改动任一交付物后按序全跑）

```bash
python3 scripts/shoot_slides.py <deck.html> <out>   # 截图 + 溢出探针（out 不带 figures/ 前缀）
python3 scripts/verify_deck_talk.py <deck> <talk>   # 页数、标题逐字、分块、计时
python3 scripts/verify_style.py                     # 表达禁则、构念齐备、编号成套
python3 scripts/audit_all.py                        # 旧术语、页面结构、数值一致、编号
python3 scripts/audit_round2.py                     # 引注可追溯、配额可行性、备答覆盖、单页字数
python3 scripts/html2pptx.py --all                  # 五份 deck → 可编辑 PPTX
python3 scripts/verify_pptx.py --all                # 时效性、页数、文本覆盖、越界、溢出、行高、可编辑性
python3 盲区框架/scripts/verify_blind.py             # 盲区目录七项
```

**三条纪律**：① 凡改 deck 必重跑 `shoot_slides.py`，否则溢出报告过期；② 凡改 deck 必重跑 `html2pptx.py`，`verify_pptx.py [0]` 会以 mtime 比对拦截过期 PPTX；③ 盲区专题综述 deck 与讲稿由**生成脚本**产出，直接改 HTML 会在下次重建时被覆盖。

**已知限制**：本机无 LibreOffice，PPT 视觉保真无法渲染核验，只能靠 `verify_pptx.py` 的结构比对与几何估算。

---

## 关键新证据速查（v2 新增，含数值）

| 编号 | 一句话 | 关键数值 |
|---|---|---|
| #71 Zhang 2015 | **本库梯度最细的时机对照** | 7 档 2.5–5.5 s；**2.5 s 与无预警无显著差异**（碰撞率 29.4% vs 44.1%）；有效下限 3.0 s，推荐 3.0–4.0 s；最大减速距离 SD **40.75 → 15.97 m** |
| #74 Abe 2006 | 报警时机—信任—期望 | 自主松油门基线 **0.72 s**；信任 7.3 → 4.3；早报警 BRT 1.20 → 0.93 s |
| #72 Chen 2013 | PRT 三段分解 | 0.44–0.52 + 0.15–0.25 + 0.15–0.40 = **0.74–1.17 s**；不可压缩总时延 **1.04–1.92 s** |
| #78 Large 2019 | **Daimler 四级级联** | 4.0 → 2.6 → 1.6 → 1.1 s（级间 **1.4 / 1.0 / 0.5 s**）；PROSPECT 迫近 1.8 s |
| #90 Suzuki 2010 | 视觉 4.0 s → 听觉 2.0 s；风险区 $R_x = T_{tc}\cdot V_{car}$ | 危险等级每 **1.0 s** 一档 |
| #77 Lind 2007 | **显示位置的量化基线** | CWHUD 快约 **200 ms**（$F(3,45)=10.8$）；漏报 **1 / 6 / 12 / 17 次**；闪烁 4 Hz、占空比 60% |
| #80 Shen 2026 | 闪烁占空比 | 周期 2 s；**50% 最优**（1041.58 ± 380.87 ms）；无闪烁最差 |
| #99 Takada 2014 | **DCA 触发 + 2:1 滞环** | 触发 4.0 / 解除 2.0 m/s²；反应时 $T$ = 1.2 s（= 90 百分位）/ 0.2 s |
| #102 Coelingh 2010 | Volvo AEB 时序 | 介入于 TTC ≈ **1 s**；物理最早 **1.6 s**；制动纯延迟 **180 ms** + 斜坡 **20 m/s³** |
| #100 Gray 2014 | 连续强度调制 | $I \approx a + kD^{-2}$；**上升型显著优于下降型**（$p=0.003$）；BRT 低约 100 ms |
| #76 Thammakaroon 2012 | **系统侧延迟** | FCW 报警比真实制动**晚 1.47 s** |
| #84 Char **2020** | 3700+ 事故重建 + 200 人模拟器 | FCW 1.7/2/2.3/2.6 s，**仿真最优 2.6 s**；行人 $t_{LTTB}\approx 1.5$ s；传感 **FOV > 30° 可在 TTC 2 s 检出 > 90%** |
| #69 Zhu 2025 | **眼动判定门槛** | TDT 最优 **500–2000 ms**；TTFF 最优 **100–300 ms** |
| #62 Winkler 2018 | 无 TTC 阈值、用路标触发 | BRT 1.4 → 1.03–1.05 s；**LI 场景 50% 被试在预警前已制动**；RT 清洗界 0.2–2.9 s |
| #58 Strayer 2025 | **SPIDER 2.0 理论骨架** | Scanning / Predicting / Identification / Decision-making / Executing |
| #59 Wang 2024 | **DSID + SRK 信号化** | 三元素全含者最优；同时提升 SA 与降低负荷 |
| #73 A-TTC 2026 | 自然驾驶骚扰报警实测 | **569 辆**卡车、**3,519** 条视频核验事件；动态标定后骚扰报警占比 **13.74%**、召回 **89.25%**、准确率 81.42%；**正式版未报固定阈值基线**（预印本的 25.16% 已作废） |

---

## 文献索引

### 01–40（v1，全部有全文）

见 `README_v1_40篇口径.md.bak` 的索引表与 `HUD_AR-HUD_行人预警_时空设计_新表.md`。summaries 文件名格式为 `summaries/{idx}_{年份}_{作者}_{主题}.md`。

### 41–102（v2 新增）

「全文 = 仅摘要」者的 summaries 已在表头标注资料来源，**其数值不得作为参数锚点使用**。

| idx | 年份 | 第一作者 | 标题（截断） | 全文 | summaries 文件 |
|---|---|---|---|---|---|
| 41 | 2015 | Bolton | An investigation of augmented reality presentations  | Y | `41_2015_Bolton_AR-HUD地标式导航呈现研究.md` |
| 42 | 2026 | Chen | Hierarchical Feature Evaluation and Decision‑Making  | 仅摘要 | `42_2026_Chen_毕达哥拉斯Hamacher聚合的AR-HUD分层特征评价决策.md` |
| 43 | 2023 | Chen | Inattentional blindness to unexpected hazard in augm | 仅摘要 | `43_2023_Chen_刺激与增强图形相对位置对无意视盲的影响.md` |
| 44 | 2019 | Chen | Drivers’ recognition of pedestrian road-crossing int | Y | `44_2019_Chen_驾驶员对行人过街意图的识别绩效与过程.md` |
| 45 | 2023 | Cheng | Does the AR-HUD system affect driving behaviour? An  | 仅摘要 | `45_2023_Cheng_AR-HUD系统是否影响驾驶行为眼动实验.md` |
| 46 | 2018 | Wintersberger | Fostering User Acceptance and Trust in Fully Automat | Y | `46_2018_Wintersberger_AR提升全自动驾驶信任与接受度.md` |
| 47 | 2021 | Yau | Graph-SIM: A Graph-based Spatiotemporal Interaction  | Y | `47_2021_Yau_Graph-SIM行人动作预测时空交互建模.md` |
| 48 | 2024 | Hou | The Effect of Dynamic Effects and Color Transparency | 仅摘要 | `48_2025_Hou_AR-HUD导航图形动效与色彩透明度对无意视盲的影响.md` |
| 49 | 2022 | Jing | The impact of different AR-HUD virtual warning inter | 仅摘要 | `49_2022_Jing_AR-HUD虚拟预警界面对接管绩效与视觉特征的影响.md` |
| 50 | 2020 | Karatas | Evaluation of AR-HUD Interface During an Automated I | Y | `50_2020_Karatas_自动介入时AR-HUD界面评估.md` |
| 51 | 2016 | Langlois | Augmented reality versus classical HUD to take over  | Y | `51_2016_Langlois_AR与传统HUD的接管辅助对比.md` |
| 52 | 2025 | Li | Effects of Driving Background Complexity and Interfa | 仅摘要 | `52_2025_Li_驾驶背景复杂度与界面不透明度对AR-HUD视觉认知的影响.md` |
| 53 | 2025 | Lopez | Opacity in car augmented reality head-up displays: u | 仅摘要 | `53_2025_Lopez_车载AR-HUD不透明度偏好视觉注意与情境意识.md` |
| 54 | 2018 | Merenda | Augmented Reality Interface Design Approaches for Go | Y | `54_2018_Merenda_目标导向与刺激驱动AR界面设计路径.md` |
| 55 | 2013 | Pammer | Attentional differences in driving judgments for cou | Y | `55_2013_Pammer_城乡场景注意差异与语义一致性无意视盲.md` |
| 56 | 2013 | Park | Efficient Information Representation Method for Driv | Y | `56_2013_Park_驾驶员中心AR-HUD高效信息表征方法.md` |
| 57 | 2015 | Pfannmüller | A Comparison of Display Concepts for a Navigation Sy | Y | `57_2015_Pfannmüller_接触类比HUD导航显示概念比较.md` |
| 58 | 2025 | Strayer | SPIDER 2.0: Driver Distraction and Visual Attention | 仅摘要 | `58_2025_Strayer_SPIDER2.0驾驶分心与视觉注意.md` |
| 59 | 2024 | Wang | A new dynamic spatial information design framework f | 仅摘要 | `59_2024_Wang_AR-HUD动态空间信息设计框架唤起本能反应.md` |
| 60 | 2021 | Wang | Inattentional Blindness in Augmented Reality Head-Up | Y | `60_2021_Wang_AR-HUD辅助驾驶中的无意视盲.md` |
| 61 | 2025 | Wei | Study on AR-HUD Design in Unprotected Intersection S | 仅摘要 | `61_2025_Wei_自动驾驶无保护交叉口AR-HUD信息组合设计.md` |
| 62 | 2018 | Winkler | How to warn drivers in various safety-critical situa | Y | `62_2018_Winkler_不同安全关键情境下的预警策略与驾驶员反应.md` |
| 63 | 2023 | Wu | The Effect of AR-HUD Takeover Assistance Types on Dr | 仅摘要 | `63_2023_Wu_AR-HUD接管辅助信息类型与情境意识.md` |
| 64 | 2024 | Yamin | In-vehicle human–machine interface guidelines for au | 仅摘要 | `64_2024_Yamin_AR-HUD车内人机界面指南综述.md` |
| 65 | 2023 | You | A Novel Cooperation-Guided Warning of Invisible Dang | 仅摘要 | `65_2023_You_协同引导式不可见危险预警.md` |
| 66 | 2024 | Yu | Effects of a color gradient and emoji in AR-HUD warn | 仅摘要 | `66_2024_Yu_颜色渐变与emoji对接管绩效与驾驶员情绪的影响.md` |
| 67 | 2023 | Yunuo | How does AR-HUD system affect driving behaviour Evid | 仅摘要 | `67_2023_Cheng_AR-HUD对驾驶行为影响的眼动实验证据.md` |
| 68 | 2024 | Zeng | The impact of AR-HUD lane enhancement on lateral con | 仅摘要 | `68_2024_Zeng_雾天AR-HUD车道增强与横向控制绩效.md` |
| 69 | 2025 | Zhu | Visual Saliency Design for AR-HUD Navigation in Extr | Y | `69_2025_Zhu_极端天气AR-HUD导航视觉显著性与无意视盲.md` |
| 70 | 2016 | Kang | Differences in drivers’ pedestrian avoidance respons | 仅摘要 | `70_2016_Kang_听觉行人碰撞预警时机与刺激反应兼容性.md` |
| 71 | 2015 | Yuting | Effects of collision warning system under different  | Y | `71_2015_Zhang_预警释放时机对驾驶速度与距离的影响.md` |
| 72 | 2013 | Chen | Forward collision warning system considering both ti | Y | `72_2013_Chen_TTC与安全制动距离双判据前向碰撞预警.md` |
| 73 | 2026 | Wang | A-TTC: A Multimodal Fusion Framework for Personalize | 仅摘要 | `73_2026_Wang_A-TTC动态阈值标定的个性化卡车FCW框架.md` |
| 74 | 2006 | Abe | Alarm timing, trust and driver expectation for forwa | Y | `74_2006_Abe_报警时机驾驶员信任与期望.md` |
| 75 | 2004 | Abe | The human factors of collision warning systems: Syst | 仅摘要 | `75_2004_Abe_碰撞预警系统人因系统性能报警时机与信任.md` |
| 76 | 2012 | Thammakaroon | Improvement of warning lag time in forward collision | Y | `76_2012_Thammakaroon_多功能预警改进预警滞后时间.md` |
| 77 | 2007 | Lind | An Efficient Visual Forward Collision Warning Displa | Y | `77_2007_Lind_高效视觉前向碰撞预警显示CWHUD.md` |
| 78 | 2019 | Large | Investigating the effect of urgency and modality of  | Y | `78_2019_Large_行人预警紧迫性与模态对接受度与绩效的影响.md` |
| 79 | 2024 | 鲍 | Effects of Visual Crowding and Stimulus Location on  | Y | `79_2024_鲍威宇_视觉拥挤与刺激位置对行人感知的影响.md` |
| 80 | 2026 | Shen | Effect of AR-HUD Warning Information Presentation Mo | Y | `80_2026_Shen_AR-HUD预警呈现模式与情境意识闪烁占空比.md` |
| 81 | 2016 | Phan | Estimation of driver awareness of pedestrian for an  | Y | `81_2016_Phan_AR行人碰撞预警的驾驶员觉察建模与预警时机.md` |
| 82 | 2013 | Schall | Augmented reality cues and elderly driver hazard per | Y | `82_2013_Schall_AR提示与老年驾驶员危险感知.md` |
| 83 | 2018 | Maroto | Head-up Displays (HUD) in driving | Y | `83_2018_Maroto_HUD在驾驶中的综述.md` |
| 84 | **2020** | Char | Pedestrian and cyclist forward collision warning sys | Y | `84_2022_Char_行人与骑行者FCW触发时机与事故重建仿真.md`（文件名年份未改，内容以 2020 为准） |
| 85 | 2013 | Chang | The Development of Parameters and Warning Algorithms | 仅摘要 | `85_2013_Chang_交叉口公交-行人碰撞预警系统参数与预警算法开发.md` |
| 86 | 2009 | Chang | Parameters analysis for an intersection bus-pedestri | Y | `86_2009_Chang_交叉口公交-行人碰撞预警系统参数分析.md` |
| 87 | 2026 | Cangut | Machine Learning-Based Pedestrian Intention Predicti | Y | `87_2026_Cangut_机器学习行人过街意图预测与碰撞预警.md` |
| 88 | 2025 | Certad | V2P Collision Warnings for Distracted Pedestrians: A | Y | `88_2025_Certad_V2P碰撞预警与传统听觉警报对比.md` |
| 89 | 2021 | Wolf | Early warning of pedestrians and cyclists | Y | `89_2021_Wolf_行人与骑行者的早期预警.md` |
| 90 | 2010 | Suzuki | Sensor fusion-based pedestrian collision warning sys | Y | `90_2010_Suzuki_斑马线检测与传感器融合行人预警分级时机.md` |
| 91 | 2023 | Sun | A Reinforcement Learning-Based Adaptive Forward Coll | 仅摘要 | `91_2023_Sun_强化学习实时反应时自适应前向碰撞预警.md` |
| 92 | 2016 | Kuo | Pedestrian Collision Warning of Advanced Driver Assi | Y | `92_2016_Kuo_单目视觉行人碰撞预警与灰色路径预测.md` |
| 93 | 2023 | Zhang | Research on pedestrian vehicle collision warning bas | 仅摘要 | `93_2023_Zhang_基于路径预测的行人车辆碰撞预警.md` |
| 94 | 2024 | Joo | Predictive Safety-Aware Transmit Rate Control Scheme | 仅摘要 | `94_2024_Joo_预测性安全感知发射速率控制与网联前向碰撞预警.md` |
| 95 | 2005 | Miyoshi | Development of Forward-Collision Avoidance Warning S | 仅摘要 | `95_2005_Miyoshi_适配驾驶员特性的前向碰撞避免预警系统.md` |
| 96 | 2019 | Elliott | Recent advances in connected and automated vehicles | Y | `96_2019_Elliott_网联与自动驾驶车辆研究进展综述.md` |
| 97 | 2020 | Rasouli | Autonomous Vehicles That Interact With Pedestrians:  | Y | `97_2020_Rasouli_自动驾驶车辆与行人交互理论与实践综述.md` |
| 98 | 2019 | Amini | Negotiation and Decision-Making for a Pedestrian Roa | Y | `98_2019_Amini_行人过街协商与决策文献综述.md` |
| 99 | 2014 | Takada | Effectiveness of forward obstacles collision warning | Y | `99_2014_Takada_基于避撞减速度DCA的前向碰撞预警阈值.md` |
| 100 | 2014 | Gray | A Comparison of Different Informative Vibrotactile F | Y | `100_2014_Gray_振动触觉前向碰撞预警与制动反应时.md` |
| 101 | 2003 | — | Human Factors in Forward Collision Warning Systems:  | 仅摘要 | `101_2003_SAEJ2400_前向碰撞预警人因操作特性与界面要求.md` |
| 102 | 2010 | Coelingh | Collision Warning with Full Auto Brake and Pedestria | Y | `102_2010_Coelingh_VolvoCWAB-PD自动制动触发时机.md` |

---

## 使用指南

| 我想…… | 打开 |
|---|---|
| 拿到可直接实现的预警状态机（阈值 + 出处 + 禁令） | `AR-HUD行人碰撞预警_毕业论文大纲与危险判定文献综述.md` **§9.8** |
| 理解本轮为什么要改核心变量 | `优化方案_预警时间参数理论化重构与执行计划.md`（第二、三部分） |
| 查某篇论文的完整数值 | `summaries/{idx}_*.md`，先看表头「资料来源」判断是全文还是仅摘要 |
| 查时间参数（TTC/PRT/持续/级间间隔/延迟） | `时间元素设计参数_专题分析.md` |
| 查空间参数（颜色/动效/FOV/锁定/透明度） | `空间元素设计参数_专题分析.md`，v2 修订见第六章 |
| 查危险出现/解除的判定标准与状态机 | `AR-HUD行人碰撞预警_毕业论文大纲与危险判定文献综述.md` §4、§9.2 |
| 写某个实验的方法学部分 | 对应的 `实验N_*.md`，v1 节为证据盘点、v2 节为最终设计 |
| 对齐学位论文体例 | `参考模板_音乐流派对驾驶行为影响的多维分析_周颖2024.md` |
| 补写新的 summaries | `scripts/SUMMARY_SPEC.md` |
| **给某个变量/水平/场景参数找引文** | `AR-HUD行人碰撞预警_毕业论文研究框架.md` **§14**（逐变量对照表，含证据强度列） |
| **取 APA 7th 参考文献条目** | `scripts/apa_refs_preview.md`（102 篇全量）或研究框架 **§15**（本章引用者） |
| 判断某个理论依据可不可信 | 研究框架 **§14.1**（期刊/被引/评级）与 **§14.2**（一处必须降级的推导） |
| **上台讲这套研究** | `研究汇报_2026_08.pptx`（放映）+ `研究汇报_2026_08_讲稿.md`（备稿；先读头部两轨制计时口径） |
| **在 PowerPoint 里改版式或文字** | 五份 `.pptx` 均为原生文本框与表格，可直接编辑；改完请回改对应 `.html` 源并重跑 `html2pptx.py`，否则下次导出会覆盖 |
| **查某条审核意见是怎么处置的** | `审核意见与翻修记录_2026_08.md`（三轮台账，每条含「问题—依据—处置—复核方式」） |
| **写学位论文第 1／3 章** | `thesis/第1章_研究背景及意义.md`、`thesis/第3章_研究内容与预期目标.md`（均为 v2／102 篇口径） |
| 了解按视线可见性切分的平行框架 | `盲区框架/README.md` |

---

## 已知的证据缺口（按优先级）

0a. **【题录与归因核验的五条教训】**（2026-08，逐条已在全库更正，详见研究框架 §14.9）
   - **Crossref 的登记年不等于答辩年**：#84 Char 经 theses.fr（NNT 2020AIXM0610）核实答辩于 **2020-12-18**，本库此前记作 2022。
   - **Crossref 的 publisher 不等于学位授予机构**：#81、#84 被记为 ABES（法国书目机构），真实授予机构为 Université de Technologie de Compiègne 与 Aix-Marseille Université。
   - **Crossref 会把中文作者的姓名颠倒、或把全名塞进 family 字段**：#33、#67、#71 与 #2、#5、#28、#72 共 7 条已修。
   - **二次转引的门限值可能无法溯源**：本库多处引用「Bliss (2003) 元分析给出虚警率 30% 信任崩塌门限」。经核验 Bliss (2003) 是**航空事故档案分析**（非元分析、非驾驶研究），且 **30% 这一数值在 Bliss 的任何原始文献中均未核实到**。已改为 Bliss et al. (1995) 的概率匹配关系与 Bliss & Acton (2003) 的汽车碰撞报警研究；实验 3 的 20% 虚警率依据改为 #78 与 #82。
   - **理论框架不等于理论参数**：$S+I \\approx 0.9$–1.2 s 以 SPIDER 命名，但 SPIDER 两篇原文均未报告阶段耗时，且该区间中 I 阶段（300–600 ms）是本课题自估值。已在全库降级为「本研究的工作假设」，1.0 s 的可引依据改以 #78、#90 的工程时序为主。见研究框架 §14.2。

0b. **预印本数值必须在正式发表后重新核验**。#73（A-TTC）的 SSRN 预印本报「固定阈值误报率 25.16% → 12.21%」，其正式版（*Accid. Anal. Prev.* 2026, 236:108635）**删除了该基线**，且样本由 816 车 / 9,435 条改为 **569 车 / 3,519 条**、准确率由 82.67% 改为 **81.42%**、指标改为**事件级骚扰报警占比 13.74%** + 威胁事件召回 **89.25%**。该数值曾被 6 份文档引用并作为实验 3「20% 虚警率」的首要依据，已全部更正（依据改为 #78 的 20% 操纵档 + #82 的 15% 零效应）。**凡本库标注为 preprint 的条目，投稿前须逐条复核。**

1. **危险解除与警告撤销**：直接对照「突然消失 vs 渐隐 vs 降级」的人因研究仍为 **0 篇**。工程侧只有 #99 的 2:1 滞环先例。状态机中退出阈值、$t_{conf}$、渐隐时长三个参数**全部为推导值**（见 §9.8.6）。
2. **不透明度记法冲突**：#48（T1/T0.75/T0.5/T0.35）、#52（≥0.6、0.7）、#53（20%、60%）三者记法与数值互不一致，且无法从摘要确定是「透明度」还是「不透明度」。**引用前必须取得其中一篇全文。**
3. **SPIDER 2.0 全文（#58）**：两条推导的共同前提是五阶段严格串行且耗时可加。**2026-08 更新**：经 Unpaywall 核验该文实为 **hybrid OA**（此前误记为付费墙），但 Annual Reviews 站点有 Cloudflare 防护，**须经机构网络人工下载**；且已确认其摘要层面无任何阶段耗时数据，故相关推导已在全库降级为工作假设（见研究框架 §14.2）。
4. **闪烁频率的 8 倍分歧**：#77 用 4 Hz、#80 用 0.5 Hz，但两者占空比接近（60% vs 50%）。提示占空比可能比频率更接近有效变量，须做频率 × 占空比二维网格检验。
5. **系统渲染延迟（warning lag）**：102 篇中几乎无一报告；#76 实测实车 FCW 滞后 1.47 s。已列为全部实验的必测项。
6. **SAE J2400（#101）全文**：其范围声明明确**只适用于追尾场景**，不覆盖行人横穿，因此其界面要求不能直接迁移——这一局限须在学位论文中显式说明。

---

## 后续工作建议

1. 按 `优化方案` 第六部分的 Phase 4 做一致性校验（各文档间的水平值、编号、术语是否互相矛盾）。
2. 先做实验 1 的预实验（N ≈ 8），确认 $t_0$ 的被试内 SD 是否 < 1 s——这决定 $\Delta t$ 能否个体化操纵。
3. 确认模拟器能否实时计算 BTN，并按 $R_x = T_{tc}\cdot V_{car}$ 动态绘制路面标记；若不能，记录退化方案。
4. 在 OSF / AsPredicted 预注册实验 1 与实验 2 的假设与清洗规则（清洗界 0.2–2.9 s，依据 #62）。
5. 对「危险解除/警告撤销」发起第二轮定向检索，检索式增加 alarm cancellation、warning withdrawal、hysteresis threshold、de-escalation、warning offset。
