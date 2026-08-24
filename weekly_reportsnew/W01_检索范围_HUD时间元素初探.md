
# 第 1 周汇报：检索范围确立 + Lübbe (2017) 精读汇报

**汇报周次**：W1（2026.06.20 – 2026.06.27）
**汇报对象**：[导师姓名]
**汇报人**：[学生姓名]

---

## 1. 本周目标

1. 确立硕士学位论文研究主题"HUD/AR-HUD 行人碰撞预警时间元素设计"的文献检索范围（数据库、关键词、纳入排除标准）
2. 完成 **HUD 子集 14 篇文献**的系统精读，提取其在时间维度上的报告情况
3. 选取 **Lübbe (2017)** 作为本周深度精读文献，**按学术论文的引言—方法—结果—讨论四段范式（IMRD）** 完整汇报——不停留于设计罗列，而是理解其研究动机、方法合理性、因变量分层、讨论启示
4. 形成 HUD 阶段时间元素的综合对照表，为 §2.2 章节填充提供素材
5. **提炼本周 5 条共识**，作为可传承的结论

**说明**：本周及后续每周均按"一周一篇重点精读 + 若干并列参照"的节奏推进——按 IMRD 完整展开一篇论文需要在方法学层面的深度理解，10 周覆盖 10 篇重点精读加 30 篇参照，可以合理覆盖 40 篇核心文献。

---

## 2. 检索情况

**检索时间**：2026.06.20 – 2026.06.27（5 个工作日）
**检索时段覆盖**：2008–2025（HUD 在车辆领域的人因研究起点至今）

### 2.1 数据库与关键词

| 数据库                         | 检索字段              |
| ------------------------------ | --------------------- |
| Web of Science Core Collection | Topic（TI / AB / KW） |
| Scopus                         | Title-Abs-Keywords    |
| IEEE Xplore                    | All Metadata          |
| ACM Digital Library            | Anywhere              |
| OpenAlex                       | Title-Abstract        |
| CNKI（中文）                   | 题名 + 摘要           |

**核心检索式（Web of Science 示例）**：

```
TS = ("Head-Up Display" OR HUD OR "Augmented Reality HUD" OR AR-HUD)
   AND ("Pedestrian Collision Warning" OR PCW OR "Forward Collision Warning"
        OR "pedestrian safety" OR "pedestrian detection warning")
   AND (timing OR duration OR "warning onset" OR "Time-to-Collision" OR TTC
        OR "graded warning" OR "multi-stage warning" OR "lead time" OR conformal)
DocType = (Article OR Proceedings Paper OR Review)
PY = 2008–2025
```

### 2.2 检索结果统计

| 数据库               | 初步 Hits     | 去重后        | 标题筛选     | 摘要筛选     | 全文纳入     |
| -------------------- | ------------- | ------------- | ------------ | ------------ | ------------ |
| Web of Science       | 142           | –            | 38           | 22           | –           |
| Scopus               | 187           | –            | 41           | 19           | –           |
| IEEE Xplore          | 95            | –            | 24           | 14           | –           |
| ACM DL               | 87            | –            | 19           | 8            | –           |
| OpenAlex             | 230           | –            | 47           | 18           | –           |
| CNKI（中文）         | 53            | –            | 12           | 5            | –           |
| **合并去重后** | **794** | **412** | **73** | **40** | **40** |

**最终纳入 40 篇核心文献**，分布为：HUD 子集 14 篇 / AR-HUD 子集 26 篇。本周聚焦 HUD 子集 14 篇。

### 2.3 纳入与排除标准

**纳入标准**：

1. 同行评审 SCI / SSCI / EI 检索期刊或 IEEE / ACM 主流会议
2. 实证研究（驾驶模拟器、真实道路、VR HMD）或方法学综述
3. 至少报告以下时间维度之一：TTC 阈值 / Lead Time / Warning Duration / 分级 / 触发依据

**排除标准**：

1. 纯工程算法论文且无人因实验数据（保留 3 篇工程系统作为背景，但不作为时间设计证据）
2. 摘要 / 海报 / 非可获取全文
3. 非英文 / 中文文献

---

## 3. HUD 子集 14 篇全景与本次精读文献选择

按时间维度报告情况分五组：3.1 警告时机重点报告类 / 3.2 持续时长重点报告类 / 3.3 综述与背景类 / 3.4 工程系统类 / 3.5 自适应触发类。

> **说明**：闪烁频率与 onset-offset 动画过渡两个维度在 HUD 子集 14 篇中**报告率为 0%**（仅 Doshi 2008 一处质性提及"dynamic display"），本周不单独展开，仅在 §4 综合对照表内标注"未报告"作为背景信息。

### 3.1 警告时机（TTC 阈值）重点报告类（5 篇）

- **[idx 14] Lübbe (2017)** — *Brake reactions of distracted drivers to pedestrian FCW systems*. Journal of Safety Research. — **本周精读文献，§5 完整 IMRD 展开**。
- **[idx 15] Winkler et al. (2015)** — UR:BAN 项目，城市 50 km/h 场景，N=32；HUD 显著缩短首次发现行人时间；未明确 TTC 阈值。
- **[idx 16] Kazazi et al. (2015)** — 青年 vs 老年（各 N=36）；老年组预警触发点前移 7 m（30 km/h 下对应 +0.84 s）；提出代际差异。
- **[idx 28] Doshi et al. (2008)** — DAD 概念论文，基于驾驶员/车辆/环境状态自适应触发；未量化 TTC 阈值。
- **[idx 12] Zhang/边扬 (2024)** — N=34 中国驾驶员，60 km/h 城市；**100 m 距离触发（≈ 6 s Lead Time）**——HUD 子集唯一不用 TTC 的研究；雾天 HUD 优势相较 HDD 显著放大；本研究应关注"触发依据（TTC vs 距离）"这一显式设计变量。

### 3.2 持续时长（Warning Duration）重点报告类（1 篇）

- **[idx 27] Ma et al. (2021)** — 同济 VR 仿真，N=12；单条警告 3 s + 紧急 10–15 s；HUD 子集唯一明确量化 Duration 的研究；作者本人在 Discussion 中承认"the optimal duration remains an open question"。W3 深度精读的候选。

### 3.3 综述与背景类（4 篇）

- **[idx 32] Skirnewskaja & Wilkinson (2022)** — 车载全息 HUD 技术综述；未涉及时间参数。
- **[idx 31] Kettle & Lee (2022)** — AR 车-驾沟通系统综述；将 "longitudinal effects" 列为关键空白。
- **[idx 35] Guan (2024)** — HCI 视角综述；主要关注空间布局。
- **[idx 19] Winkler & Soleimani (2025)** — 跨越 HUD 与 AR-HUD 的最新综述。

### 3.4 工程系统类（3 篇，仅作背景）

- **[idx 37] Jung & Choi (2016)** — CNN 语义分割 PCW；无人因数据。
- **[idx 38] Kim (2022)** — V2X 实时预测 PCW；无人因数据。
- **[idx 39] Banerjee et al. (2021)** — 唯一含人因实验：PCW 组 SRT 3.14 s vs 基线 2.53 s；3 秒生存概率 21%→43%；未明确 TTC 阈值或 Duration。

### 3.5 自适应触发类（1 篇）

- **[idx 30] Frémont et al. (2019)** — 通过对驾驶信号建模识别"未察觉行为"，仅在未察觉时呈现 AR 预警；延续 Doshi 的 DAD 理念但未量化时机。

### 3.6 本周精读文献的选择：Lübbe (2017)

在上述 14 篇中，选择 **Lübbe (2017)** 作为本周深度精读文献，理由有三：

1. **参数覆盖最完整**：HUD 子集内唯一同时量化"警告时机（TTC 1.8 s / 2.5 s）+ 持续时长（1.8 s 固定）+ 级间时序（0.7 s）"三个时间参数的 HMI 对照实验。
2. **方法学完整度领先**：使用 Toyota Higashifuji 技术中心的 moving-base 高保真模拟器（7.1 m 穹顶 + 360° 投影 + 6 自由度运动平台 + 真实整车），是子集内方法学水准最高的实证之一。
3. **是本研究 RQ2 的直接前身**：0.7 s 级间间隔是 HUD 子集唯一的量化数据，且是"派生值"而非独立自变量——这一空白直接对应本研究 RQ2 的切入点。

---

## 4. 本周综合对照表：HUD 子集 14 篇时间维度提取

下表列出 HUD 子集 14 篇文献在时间 5 维上的报告情况，"未报告"指原文未给出量化数据。**闪烁频率与 onset 动画两列仅作背景标注，本报告不展开分析**。

| idx | 第一作者 (年)              | 警告时机 (TTC / Lead Time)                | 持续时长                 | 升级时序 (级间间隔)      | 闪烁频率 | onset 动画 |
| --- | -------------------------- | ----------------------------------------- | ------------------------ | ------------------------ | -------- | ---------- |
| 05  | Yoon (2014)                | 三级 TTC 未量化                           | 未报告                   | 三级框架（未量化阈值）   | 未报告   | 未报告     |
| 12  | Zhang/边扬 (2024)          | **100 m** 距离触发 (~6 s Lead Time) | 未报告                   | 单级                     | 未报告   | 未报告     |
| 14  | Lübbe (2017)              | **1.8 / 2.5 s 二级**                | 1.8 s 固定               | **0.7 s 间隔**     | 未报告   | 未报告     |
| 15  | Winkler (2015)             | 行人启动后 X s 触发                       | 至危险解除               | 单级                     | 未报告   | 未报告     |
| 16  | Kazazi (2015)              | flow point (老年前移 7 m)                 | 未报告                   | 单级（建议未来 cascade） | 未报告   | 未报告     |
| 19  | Winkler & Soleimani (2025) | 综述（涵盖 1.8–5.0 s 范围）              | 综述讨论                 | 综述讨论                 | 综述     | 综述       |
| 27  | Ma (2021)                  | 速度相关（未量化 TTC）                    | **3 s / 10–15 s** | 单级                     | 未报告   | 未报告     |
| 28  | Doshi (2008)               | 动态触发（DAD）                           | 动态                     | 单级                     | 未报告   | 质性描述   |
| 30  | Frémont (2019)            | 自适应（驾驶员未察觉时触发）              | 未量化                   | 单级                     | 未报告   | 未报告     |
| 31  | Kettle & Lee (2022)        | 综述                                      | 综述（标注空白）         | 综述                     | 综述     | 综述       |
| 32  | Skirnewskaja (2022)        | 技术综述（未涉及）                        | –                       | –                       | –       | –         |
| 35  | Guan (2024)                | 综述（HCI 视角）                          | –                       | –                       | –       | –         |
| 37  | Jung (2016)                | 工程算法（无人因数据）                    | –                       | –                       | –       | –         |
| 38  | Kim (2022)                 | 工程算法（V2X）                           | –                       | –                       | –       | –         |

**HUD 子集 14 篇核心三维报告率统计**：

| 时间维度                    | 明确量化报告                              | 报告率                               |
| --------------------------- | ----------------------------------------- | ------------------------------------ |
| 警告时机（TTC / Lead Time） | 4 篇（Lübbe / Kazazi / Zhang / Ma 间接） | 4/14 = 29%                           |
| 持续时长                    | 1 篇（Ma 2021）                           | 1/14 =**7%** ← 最严重空白之一 |
| 升级时序（级间间隔）        | 1 篇（Lübbe 0.7 s）                      | 1/14 =**7%** ← 最严重空白之一 |
| （闪烁频率 / onset 动画）   | 0 篇                                      | 0% ← 暂搁置                         |

---

## 5. Lübbe (2017) 精读汇报（IMRD 完整展开）

本节按学术论文的**引言—方法—结果—讨论**四段范式完整汇报 Lübbe (2017)，重点回答三个问题：

- **引言**：三个关键时间参数（TTC 1.8 s / 2.5 s / 级间 0.7 s）的选择依据是什么？研究缺口是什么？
- **方法**：Toyota moving-base 模拟器的方法学优势在哪？次任务如何操作化"重度分心"？
- **结果**：7 个因变量如何分层解读？BP 优势的机制来源是什么？
- **讨论**：Lübbe 自陈的局限有哪些？对本研究的启示是什么？

### 5.1 Introduction（引言）

#### 5.1.1 研究背景

- **驾驶员分心是行人事故的主因**——ITARDA (2012) 报告日本约 1/3 致命行人事故由分心驾驶员引起；Habibovic et al. (2013) 的自然驾驶分析证实"驾驶员注意力被分散到行人以外的事物"是主要原因。
- **FCW 系统的目标**：把分心驾驶员的注意力拉回冲突方向，联合 AEB 一起减少碰撞。
- **HMI 三类**：视觉（多数在仪表板）、听觉、触觉（座椅震动、安全带预紧、刹车脉冲）。**HUD 因接近自然视线常被认为更佳，但比较 HUD vs 仪表板告警的实证结论不一致**（Wege et al., 2013）。
- **Euro NCAP 2016 行人主动安全评估现状**：FCW 仅占总分 1/21（AEB 与 HMI 权重 5:1，FCW 在 HMI 中占 1/4）。作者认为这与 FCW 的真实安全收益不匹配，部分原因是**缺乏可靠的驾驶员制动反应模型**。

#### 5.1.2 研究缺口

Lübbe 在引言中明确识别出三个缺口：

1. **缺乏"重度分心 + 视线偏离前方"条件下 c2p FCW 的制动反应数据**——既有 Raudszus et al. (2013) 只研究"轻度分心"驾驶员（次任务只通过听觉给出，视线不偏离前方）。
2. **c2p 场景下音视频、触觉刹车脉冲、HUD 三种 HMI 缺乏并行比较**——现有研究要么单一 HMI，要么比较少数组合。
3. **Euro NCAP 需要 c2p FCW 的驾驶员制动模型，但 RT × 减速度 × jerk 联合数据集不存在**——只有 c2c 场景有部分数据。

#### 5.1.3 三个时间参数的选择依据

这是本研究团队特别关注的问题——Lübbe 在讨论段（原文 L517–L526）交代了每个参数的锚点：

**① AV 警告激活点为什么设为 TTC = 1.8 s？**

- **锚点 1（工程实证）**：Matsui et al. (2011) 实测报告——Toyota Prius MY2013 的行人 FCW 系统在 TTC = 1.8 s 时激活；Setting 1 (AV) 与 Setting 2 (BP) 直接复用该量产 HMI 规格。这是"从工业实践出发"的方法学策略，保证实验结果对量产车具有直接的外推效度。
- **锚点 2（仿真理论）**：Helmer (2014) 的交通仿真在"平衡虚警率与减伤"目标下得出最优触发窗口 **TTC 1.5–2.2 s**，1.8 s 位于中位。下界 1.5 s 确保驾驶员有起码 PIEV 时间；上界 2.2 s 防止过早触发导致虚警疲劳。
- **范式定位**：**1.8 s 属于 Campbell et al. (2007) 的 Imminent Crash Warning（紧迫碰撞警告）范式**——晚触发、追求 immediate driver reaction（立即制动反应），而非引导注意力。

**② HUD 提示为什么设为 TTC = 2.5 s？**

- **锚点（接受度问卷）**：Naujoks et al. (2012) 调研驾驶员对 Cautionary Crash Warning 的接受时点集中在冲突演化为不可避免碰撞前 **2–3 s**；2.5 s 位于中位。
- **范式定位**：**2.5 s 属于 Campbell et al. (2007) 的 Cautionary Crash Warning（预警式警告）范式**——早触发、追求 orienting response（引导注意）。按 Campbell 原话（论文 L537）："warnings should induce an orienting response, where appropriate, causing the driver to look in the direction of the threat"——警告应触发定向反应、让驾驶员将注意力转向威胁方向。
- **HUD 显示元素的匹配**：HUD 显示"包围行人的画框（bounding box）跟随行人移动" + 单次 57 dBA 提示音，正是为在 2.5 s 完成 orienting 任务——引导视线定位威胁位置。

**③ 0.7 s 级间间隔为什么设为 0.7 s？**

**关键洞察**：**0.7 s 不是独立设计的自变量，而是 2.5 s − 1.8 s = 0.7 s 的差值**。

- Lübbe 使用 **Campbell et al. (2007) 的 triggered approach 框架**，把 Cautionary（早期提示）和 Imminent（紧急强化）两阶段组合。0.7 s 是这个组合的"过渡时间"，数值由两个范式的时间设定推导，**没有独立的优化实验**。
- **含义**：**级间间隔本身尚未被作为独立自变量做过对照实验**。Lübbe 的 0.7 s 是 HUD 子集唯一量化数据，但它是"两个范式的合成副产品"而非最优值证明——这正是本研究 **RQ2（级间间隔最优对照）** 的直接切入点。

#### 5.1.4 研究假设

- **H1**：BP 与新型 HUD 比单纯 AV 有更高的碰撞避免率。
- **H2**：制动反应时、最大减速度、jerk 都依 HMI 而异；BP 与 HUD 比 AV 反应时短。
- **H3**：HUD 事前熟悉化（familiarization）可降低碰撞率与反应时。

### 5.2 Method（方法）

#### 5.2.1 被试

- 招募 101 人，排除 43 人（晕动症 6 / 报告非正常驾驶 5 / HMI 激活前已踩刹车 27 / 次任务期间视线回到前方 5）
- 最终 58 人有效：4 个 FCW 组各 N = 13 + 控制组 N = 6
- 年龄 19–78 岁；年里程 10–35,000 km；性别男 46–62%
- 各组人口学变量（年龄/里程/性别）无显著差异

#### 5.2.2 实验设计

- **类型**：单因素被试间设计，FCW 设置 5 水平（AV / BP / HUD / HUDfam / Control）
- **自变量**：HMI 组合
- **因变量**（7 个）：碰撞与否、碰前是否启动制动、视线方向 EoVE、制动反应时 RT、最大减速度、jerk、车速
- **数据采集**：踏板力与车辆减速度 120 Hz 采样 + 50 点滑动平均滤波；前视/侧视双摄像头记录视线；两名分析者独立判读取均值

#### 5.2.3 实验材料与设备

**驾驶模拟器**：Toyota Higashifuji Technical Center 的 moving-base 模拟器：

- 7.1 m 直径穹顶 + 360° 投影
- 6 自由度运动平台（水平活动范围 35 × 20 m）
- 车体为真实整车
- 是子集内方法学水准最高的驾驶模拟器之一

**测试场景**：

- 3 km 城市路段，限速 30 km/h，纵向无插队车辆
- 6 个交叉口；前 5 次执行次任务但无行人
- 第 6 次为测试事件：**行人从右侧以 2 m/s 垂直横穿**
- 数字次任务在 TTC = 3.0 s 时出现、持续 2.5 s（覆盖整个警告期）
- 行人在 TTC = 2.7 s 进入视野
- 次任务指令在 TTC = 3.5 s 给出

**次任务（重度分心操作定义）**：副驾屏幕显示 5 位随机数字，要求记忆并复述——**视线完全离开前方去看副驾屏幕**。

**5 个 Setting 详细规格**：

| Setting    | 组成                                                                            | 激活时点                            |
| ---------- | ------------------------------------------------------------------------------- | ----------------------------------- |
| 1: AV      | 仪表板闪烁 + 词"Brake!"（日文）+ 64 dBA 警告音，重复 1.8 s                      | TTC = 1.8 s（Matsui 2011 量产规格） |
| 2: BP      | AV +**三角形刹车脉冲**（持续 ~0.2 s，峰值 3 m/s²，对应 Lexus LS MY2014） | TTC = 1.8 s                         |
| 3: HUD     | 两阶段：HUD 提示（画框 + 单声 57 dBA）+ AV                                      | TTC = 2.5 s（HUD）→ 1.8 s（AV）    |
| 4: HUDfam  | 同 Setting 3 但事前演示 HUD 工作机制                                            | 同 Setting 3                        |
| 5: Control | 无 FCW                                                                          | –                                  |

### 5.3 Results（结果）

**Lübbe 报告 7 个因变量。为理解结果的完整含义，需按"救命 / 认知 / 力学"三层解读**——**只看单一指标会得出误导性结论**。这是本文最有方法学启发的部分。

#### 5.3.1 救命层（2 个 DV）——回答"警告是否让人活下来"

| #  | 因变量                     | 操作定义                      | 结果                                                                                                                                                                                                      | 反映的实际情况                                                                                                      |
| -- | -------------------------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| ① | **是否碰撞**         | 二值：车-行人是否发生实际碰撞 | Setting 1 AV: 10/13；**Setting 2 BP: 1/13**；Setting 3 HUD: 10/13；Setting 4 HUDfam: 8/13。Fisher-Irwin 整体 p < 0.01，**BP 显著优于其他三组**（vs AV / HUD 均 p < 0.01；vs HUDfam p = 0.01） | 最上位安全终局；对应 Euro NCAP AEB 评估目标                                                                         |
| ② | **碰前是否启动制动** | 二值：碰撞前踏板力是否 > 10 N | AV: 8/13；**BP: 13/13**；HUD: 6/13；HUDfam: 8/13                                                                                                                                                    | 过程—结果分离指标。**BP 的救命机制不是"刹得更狠"，而是"让每个人都刹车"（唤醒率）**——这个洞察只看 RT 会漏掉 |

#### 5.3.2 认知层（2 个 DV）——回答"警告如何中断分心 + 拉回注意力"

| #  | 因变量                         | 操作定义                                | 结果                                                                                                                                                                                                                                                       | 反映的实际情况                                                                                                                |
| -- | ------------------------------ | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| ③ | **EoVE**（视线返回前方） | 从警告触发到头/眼首次转向前方道路的时长 | AV: 0.65 s；**BP: 0.41 s**；HUD: 0.43 s；HUDfam: 0.53 s                                                                                                                                                                                              | 分心中断效率；**触觉的"注意抢占"最快**——触觉信号绕过视觉通道的分心瓶颈                                                |
| ④ | **制动反应时 RT**        | 从警告到踏板力 > 10 N 的时间            | **全样本**（含碰后才反应）：AV 2.8 s、**BP 0.8 s (SD 0.29)**、HUD 4.1 s、HUDfam 2.3 s（F = 3.81, p = 0.016，BP 显著快于 HUD）；**碰前启动子集**：AV 1.0 s、BP 0.8 s、HUD 1.0 s、HUDfam 0.9 s（F = 0.81, p = 0.50，**无显著差异**） | 覆盖完整 PIEV 链。**BP 优势主要来自"让更多人启动制动"（唤醒率），而不是"启动后更快"（个体反应速度）**——最反直觉的发现 |

#### 5.3.3 力学层（3 个 DV）——回答"制动质量如何"

| #  | 因变量                                       | 操作定义                        | 结果                                                                                                 | 反映的实际情况                                                                                                                                     |
| -- | -------------------------------------------- | ------------------------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| ⑤ | **最大减速度**                         | 制动过程中的最大值（m/s²）     | AV 7.2 → HUDfam 6.7，F = 0.046,**p = 0.99**，与 HMI 无关                                      | 反映紧迫感与制动力度；**"决策强度"由场景决定而非 HMI**                                                                                       |
| ⑥ | **Jerk**                               | 最大减速度 ÷ 达到时间（m/s³） | AV 11.3 → HUDfam 10.4，F = 0.037,**p = 0.99**，组间无差异；**90 分位 17.3 m/s³**       | 反映制动是否"惊吓式突进"；90 分位是 AR-HUD 触发时机设计的关键边界                                                                                  |
| ⑦ | **车速（1.8 s TTC 时 vs 制动启动时）** | 两个时刻的车辆速度（km/h）      | 1.8 s TTC 时：各组 26.5–27.5 km/h 无显著差异；**制动启动时**：BP 24.4 km/h vs 其他 ~26.8 km/h | 反映刹车脉冲本身的机械减速贡献；BP 组低 3 km/h**纯来自 0.2 s 触觉脉冲**（3 m/s² × 0.2 s ≈ 2.16 km/h）——这个"机械收益"在 AV/HUD 组不存在 |

**关键相关性**：最大减速度与 jerk 高度相关（ρ = 0.83）；与 RT 不相关（ρ = −0.04 / 0.18）——**制动力度是独立于反应速度的维度**。

#### 5.3.4 结果一句话总结

**单看 RT 或单看碰撞率都会误判——三层指标缺一不可**，因为"是否救命 / 是否唤醒 / 是否柔和"是三个不同的问题。这个方法学规范将严格用在本研究 RQ1–RQ3 的因变量设计中。

### 5.4 Discussion（讨论）

#### 5.4.1 Lübbe 自己的机制解读

- **BP 优势的机制**：触觉刹车脉冲"迫使驾驶员感觉车辆在自己制动"，这个身体感觉最有效地中断了次任务，让分心的驾驶员"察觉—启动制动"过程的比例提升。**BP 的救命机制来自唤醒率（DV2），不来自反应速度（DV4）**。
- **HUD 未显示优势的原因**：HUD 组 10/13 碰撞率与 AV 组 10/13 无显著差异——**视线不在前方时纯视觉刺激无法被即时获取**。这是"接近自然视线"这一优势的边界条件——只在驾驶员至少偶尔看前方时才成立。
- **Familiarization 短期不足**：HUDfam 8/13 vs HUD 10/13 差异不显著（p = 0.13），事前 5 分钟演示不足以让驾驶员在第一次真实警告时快速反应。Lübbe 推测这需要长期使用才能发挥。

#### 5.4.2 Lübbe 自陈的四个局限

1. **样本量偏小**：每组 N = 13，统计功效有限；差异需要较大效应量才能显著。
2. **次任务非自然**：副驾屏幕的 5 位数字记忆是实验室强制分心，与真实驾驶中的"看手机、聊天、调空调"等分心场景可能不等价——**分心强度可能过高**。27/101 因预先刹车被剔除的高比例也提示这个问题。
3. **场景过于简单**：30 km/h 城市低速 + 单一行人 + 单一突发事件——**更高速、多车、多行人、复杂场景的反应特性另需研究**。
4. **HUD 设计单一**：只对比了"包围行人的画框跟随" 这一种 HUD 设计，未与更复杂的 AR 共形图形（如虚拟阴影、路面地毯）做对比——AR-HUD 的潜在优势空间可能未充分暴露。

#### 5.4.3 对本研究（HUD/AR-HUD 时间元素设计规范）的三个具体启示

**启示 1（继承）：分心水平应作为本研究的显式调节变量或前提条件**

Lübbe 揭示纯视觉 HUD 在"重度分心 + 视线偏离前方"条件下有效性有限。如果 RQ1 不控制分心水平，会得到"HUD 无效"的误导结论。**建议**：RQ1 应把分心控制在轻度以下（如听觉次任务）或作为二档对照（无分心 / 轻度分心）——避免与 Lübbe 相同的场景边界。

**启示 2（补空白）：0.7 s 级间间隔是 RQ2 的直接起点**

如 §5.1.3 所述，0.7 s 是"两个范式的差值"而非独立自变量，且没有其他量化数据。**建议**：RQ2 把 0.7 s 作为"中位锚点"，在其两侧设 **0.5 s、0.7 s、1.0 s、1.5 s 四档做对照**——首次系统量化级间间隔的最优值。这既复制了 Lübbe，又扩展了他没做的自变量维度。

**启示 3（方法学规范）：因变量必须联合"救命 / 认知 / 力学"三层**

Lübbe 的因变量分层揭示，BP 组的碰撞率下降不是因为反应更快（RT 无差异），而是因为唤醒率提升（DV2 从 8/13 到 13/13）。**建议**：RQ1–RQ3 三个实验的因变量设计都必须联合三层指标——救命层（碰撞率、启动率）、认知层（EoVE、RT）、力学层（减速度、jerk、车速）——才能识别真实机制而非表面数据。

---

## 6. 本周共识（Weekly Consensus）

本周提炼 5 条核心共识作为可传承结论：

1. **HUD 子集 14 篇中警告时机是唯一相对成熟的时间维度（29%），持续时长（7%）与级间间隔（7%）是两大空白主区**——恰对应本论文 RQ1 与 RQ2 的天然切入点。
2. **Lübbe 2017 的 1.8 s / 2.5 s 不是任意选定，而是分别锚定于 Imminent 与 Cautionary 两个警告范式**（Campbell 2007 / Naujoks 2012）；两级设计遵循 triggered approach，但 **0.7 s 级间间隔本身是"派生量"而非自变量**——这是 RQ2 的直接起点。
3. **因变量必须分层解读**——救命层（collision / brake initiation）、认知层（EoVE / RT）、力学层（deceleration / jerk）缺一不可；BP 组的救命机制是"唤醒率↑"而非"RT↓"，只有联合多层指标才能识别真实机制。
4. **纯视觉 HUD 在"重度分心 + 视线偏离前方"条件下有效性有限**（HUD 组碰撞率 10/13 与 AV 组无显著差异）——提示本研究应把分心水平作为**调节变量或前提条件**，而非默认忽略。
5. **Lübbe 场景仅覆盖 30 km/h 城市低速与单一行人**，作者本人在讨论段承认更高速、多车、复杂场景的反应特性另需研究——**这也支持我们在 RQ1 中做 40+60 km/h 二档车速对照**，检验 TTC 阈值与 Duration 是否随车速变化。

---

## 7. 下周（W2）计划

**主题**：HUD 警告时机（TTC 阈值族）深化分析

**具体任务**：

1. 对 HUD 子集中明确量化 TTC 的 4 篇（Lübbe / Kazazi / Zhang / Ma 间接）做 evidence aggregation，统一换算到 50 km/h 标准车速下的距离 / 时间值
2. **本周精读候选：Kazazi et al. (2015)**——聚焦其代际差异实证（老年前移 7 m）与"flow point"设计的引言动机；按 IMRD 完整展开
3. 引入交通工程经典文献（Hayward 1972 TTC 原始定义；Hooper 1936 PIEV 模型；Olson & Sivak 1986 PRT 经验值；AASHTO 2.5 s 标准）作为理论锚点
4. 形成"TTC 阈值证据表"作为论文 §2.2.1 的核心实证基础
5. 评述 TTC 阈值与人因机制（PIEV 总时间约束、信号检测论 d′/β 权衡）的对应关系

**预期产出**：W02_HUD警告时机_TTC阈值族.md（含 TTC 证据表 + Kazazi 2015 IMRD 精读 + 理论锚定段 + 本周共识 5 条）

---

## 8. 本周引用 References

Banerjee, S., Khadem, N. K., Kabir, M. M., & Jeihani, M. (2021). *Influence of pedestrian collision warning systems on driver behavior: A driving simulator study* [Preprint]. arXiv. https://arxiv.org/abs/2112.09074

Bram-Larbi, K. F., Charissis, V., Khan, S., Lagoo, R., Harrison, D. K., & Drikakis, D. (2020). Collision avoidance head-up display: Design considerations for emergency services' vehicles. In *2020 IEEE International Conference on Consumer Electronics (ICCE)* (pp. 1–6). IEEE. https://doi.org/10.1109/icce46568.2020.9043068

Campbell, J. L., Richard, C. M., Brown, J. L., & McCallum, M. (2007). *Crash warning system interfaces: Human factors insights and lessons learned* (Report No. DOT HS 810 697). National Highway Traffic Safety Administration.

Doshi, A., Cheng, S. Y., & Trivedi, M. M. (2008). A novel active heads-up display for driver assistance. *IEEE Transactions on Systems, Man, and Cybernetics, Part B (Cybernetics)*, *38*(1), 85–93. https://doi.org/10.1109/tsmcb.2008.923527

Frémont, V., Phan, M.-T., & Thouvenin, I. (2019). Adaptive visual assistance system for enhancing the driver awareness of pedestrians. *International Journal of Human-Computer Interaction*, *36*(9), 856–869. https://doi.org/10.1080/10447318.2019.1698220

Guan, L. (2024). Interface design of automobile head-up display from the perspective of human-machine interaction. In *Proceedings of EAI International Conference, 24 May 2024*. EAI. https://doi.org/10.4108/eai.24-5-2024.2350098

Habibovic, A., Tivesten, E., Uchida, N., Bärgman, J., & Ljung Aust, M. (2013). Driver behavior in car-to-pedestrian incidents: An application of the Driving Reliability and Error Analysis Method (DREAM). *Accident Analysis & Prevention*, *50*, 554–565. https://doi.org/10.1016/j.aap.2012.05.034

Helmer, T. (2014). *Development of a methodology for the evaluation of active safety using the example of a system to reduce car-to-pedestrian rear-end collisions* [Doctoral dissertation]. Technische Universität Berlin.

ITARDA. (2012). *ITARDA information No. 96*. Institute for Traffic Accident Research and Data Analysis.

Jung, H., & Choi, J. (2016). *End-to-end pedestrian collision warning system based on CNN semantic segmentation* [Preprint]. arXiv. https://arxiv.org/abs/1612.06558

Kazazi, J., Winkler, S., & Vollrath, M. (2015). Accident prevention through visual warnings: How to design warnings in head-up display for older and younger drivers. In *2015 IEEE 18th International Conference on Intelligent Transportation Systems* (pp. 1028–1034). IEEE. https://doi.org/10.1109/itsc.2015.171

Kettle, L., & Lee, Y.-C. (2022). Augmented reality for vehicle-driver communication: A systematic review. *Safety*, *8*(4), 84. https://doi.org/10.3390/safety8040084

Kim, S. (2022). *Real-time predictive pedestrian collision warning service for cooperative ITS* [Preprint]. arXiv. https://arxiv.org/abs/2009.10868

Lübbe, N. (2017). Brake reactions of distracted drivers to pedestrian forward collision warning systems. *Journal of Safety Research*, *61*, 23–32. https://doi.org/10.1016/j.jsr.2017.02.002

Ma, X., Jia, M., Hong, Z., Kwok, A. P. K., & Yan, M. (2021). Does augmented-reality head-up display help? A preliminary study on driving performance through a VR-simulated eye movement analysis. *IEEE Access*, *9*, 129951–129964. https://doi.org/10.1109/access.2021.3112240

Matsui, Y., Han, Y., & Mizuno, K. (2011). Performance of collision damage mitigation braking systems and their effects on human injury in the event of car-to-pedestrian accidents. *Stapp Car Crash Journal*, *55*, 461–478.

Naujoks, F., Grattenthaler, H., & Neukum, A. (2012). Zeitliche Gestaltung effektiver Fahrerinformationen zur Kollisionsvermeidung auf Basis kooperativer Perzeption [Timing of effective driver information for collision avoidance based on cooperative perception]. In *5. Tagung Fahrerassistenz*.

Raudszus, D., Ranovona, M., Geronimi, S., Kunert, M., Schubert, E., & Schaller, T. (2013). *Response of drivers to pedestrian FCW warning in mildly distracted driving conditions* [Technical Report]. AsPeCSS Project.

Skirnewskaja, J., & Wilkinson, T. D. (2022). Automotive holographic head-up displays. *Advanced Materials*, *34*(19), 2110463. https://doi.org/10.1002/adma.202110463

Wege, C., Will, S., & Victor, T. (2013). Eye movement and brake reactions to real world brake-capacity forward collision warnings—A naturalistic driving study. *Accident Analysis & Prevention*, *58*, 259–270. https://doi.org/10.1016/j.aap.2012.09.013

Winkler, M., & Soleimani, M. (2025). A review of augmented reality heads up display in vehicles: Effectiveness, application, and safety. *International Journal of Human-Computer Interaction*. Advance online publication. https://doi.org/10.1080/10447318.2024.2443252

Winkler, S., Kazazi, J., & Vollrath, M. (2015). Distractive or supportive — How warnings in the head-up display affect drivers' gaze and driving behavior. In *2015 IEEE 18th International Conference on Intelligent Transportation Systems* (pp. 1035–1040). IEEE. https://doi.org/10.1109/itsc.2015.172

Yoon, C., Kim, K.-H., Park, H. S., Park, M. W., & Jung, S. K. (2014). Development of augmented forward collision warning system for head-up display. In *2014 IEEE 17th International Conference on Intelligent Transportation Systems (ITSC)* (pp. 2277–2279). IEEE. https://doi.org/10.1109/itsc.2014.6958054

Zhang, Y., Bian, Y., Zhao, X., Li, X., & Zhang, J. (2024). Improving pedestrian safety with head-up display warning in a connected environment. *International Journal of Human-Computer Interaction*. Advance online publication. https://doi.org/10.1080/10447318.2024.2368910

边扬, 张宇, 赵晓华, 李翔宇, 张建华. (2024). 网联环境下基于抬头显示的行人安全预警系统对驾驶员行为的影响. *华南理工大学学报（自然科学版）*, *52*(5), 1–12.

---

*汇报状态：W1 完成（2026.06.27），本次改造引入"每周一篇重点精读 + IMRD 完整展开 + 5 条本周共识"三段增强结构*
*下次汇报：W2（2026.07.04），主题 = HUD 警告时机 TTC 阈值族深化 + Kazazi (2015) IMRD 精读*
