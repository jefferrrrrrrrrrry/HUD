# 第 4 周汇报：AR-HUD 时间元素检索 + Phan (2016) 精读 + 共形概念引入

**汇报周次**：W4（2026.07.12 – 2026.07.18）
**汇报对象**：[导师姓名]
**汇报人**：[学生姓名]

---

## 1. 本周目标

承接 W1–W3 已完成的 HUD 子集 14 篇精读，本周转入 **AR-HUD 子集 26 篇**：

1. 完成 AR-HUD 子集 26 篇的检索分布特征分析（年份、场景、样本特征）
2. 引入 **Tönnis et al. (2007) 的共形（Contact-Analog）核心概念**及其对时间维度的影响
3. **按 IMRD 范式完整精读 Phan (2016)**——AR-HUD 阶段较早系统建立"感知-警觉-预期"三层评估模型的实证研究，首次对比 conformal（贴合式）vs non-conformal（非贴合式）两种 AR 提示
4. 按显示模式分类：行人锁定 / 路面锁定 / 世界锁定（为 W8 空间维度详细简表预热）
5. 提取 AR-HUD 子集 26 篇在时间 5 维上的报告情况（对照 W1 HUD 子集统计）
6. 提炼本周 5 条共识

---

## 2. AR-HUD 子集 26 篇分布特征

### 2.1 年份分布

| 时段 | 篇数 | 占比 | 代表研究 |
|---|---|---|---|
| 2008–2015 | 4 | 15% | Tönnis 2007（共形概念）、Phan 2016、Kim 2016（Virtual Shadow 早期） |
| 2016–2020 | 7 | 27% | Kim 2018、Frémont 2019、Ma 2021、Gabbard 2019（AR DriveSim） |
| **2021–2025** | **15** | **58%** | Chen 2024×2、Ma 2024 carpet、叶明慧 2025、Wu 2024、Wang ARive 2025、Huo & Alla 2025 |

**趋势**：AR-HUD 是新兴领域——2021 年后暴增与共形 AR 硬件（HoloLens 2、Magic Leap、车厂量产 AR-HUD）大规模落地同步。

### 2.2 实验场景分布

| 场景类型 | 篇数 | 代表研究 |
|---|---|---|
| 固定基座模拟器 | 12 | Phan 2016、Chen 2024、叶明慧 2025 |
| 高保真移动模拟器 | 3 | Bram-Larbi 2020（应急服务） |
| VR HMD | 5 | Ma 2021 同济、Wang ARive 2025 HoloLens 2、Wu 2024 |
| 真实道路 / 停车场 | 2 | Kim 2018 停车场（实车）、Kim & Gabbard 2019 |
| 综述 / 概念 | 4 | Tönnis 2007、Kettle & Lee 2022、Winkler & Soleimani 2025 |

**注**：真实道路实车研究仅 Kim 2018 一篇——是 AR-HUD 阶段外推效度最高的实证。

### 2.3 样本特征

**中国新手驾驶员样本 5 篇**：
- Chen (2024) contact-analog vs BB：N = 48
- Chen (2024) 多目标优先级：N = 45
- Ma (2024) carpet：N = 22
- Li (2025) 雾天信息冗余：N 未标注
- Wu (2024) 三锁定：N = 36

**欧美 / 熟练样本 8 篇**：包括 Kim 2018、Wang ARive 2025、Phan 2016 等。

**结论**：中国学者在 AR-HUD 领域已有较强的本土数据积累——本研究做中国样本并非孤立。

### 2.4 5 维报告率对比 HUD 阶段

| 时间维度 | HUD 子集报告率 | AR-HUD 子集报告率 | 提升 |
|---|---|---|---|
| 警告时机（TTC / Lead Time） | 29% (4/14) | **58%** (15/26) | +29 pp |
| 持续时长（Duration） | 7% (1/14) | **27%** (7/26) | +20 pp |
| 闪烁频率（Frequency） | 0% (0/14) | 12% (3/26) | +12 pp |
| onset-offset 动画 | 0% (0/14) | 19% (5/26) | +19 pp |
| 升级时序（Cascade Interval） | 7% (1/14) | **23%** (6/26) | +16 pp |
| **总均值** | **8.6%** | **27.8%** | **3.2 倍** |

**关键观察**：
- 警告时机 58% 已相对成熟，作为锚点而非创新点
- **持续时长 27% 和升级时序 23% 仍是空白主区**——AR-HUD 阶段虽有提升，但绝对水平仍未超过 30%
- 闪烁与 onset 维度虽从 0% 出现到 12% 和 19%，但本研究阶段暂搁置，聚焦 Duration 与级间

---

## 3. 共形（Contact-Analog）概念引入

### 3.1 Tönnis et al. (2007) 的原始定义

> Tönnis, M., Sandor, C., Klinker, G., Lange, C., & Bubb, H. (2007). Experimental evaluation of an augmented reality visualization for directing a car driver's attention. *IEEE International Symposium on Mixed and Augmented Reality (ISMAR)*.

**核心定义**：**Contact-Analog（共形）指虚拟图形与真实世界对象在视野中精确空间对齐**——虚拟图形的位置、大小、姿态随驾驶员视点与真实目标的相对运动实时更新，使虚拟图形看上去"贴"在真实对象上。

### 3.2 共形 vs 屏幕固定的本质差异

| 维度 | 屏幕固定（Screen-Fixed） | 共形（Contact-Analog / World-Fixed） |
|---|---|---|
| 位置绑定 | 挡风玻璃或 HUD 二维平面 | 真实世界三维坐标 |
| 头部/车辆运动响应 | 位置不变 | 位置实时跟随视点变换 |
| 技术要求 | 单向渲染 | 6 自由度头部追踪 + 目标追踪 |
| 深度线索 | 无（或有限） | 完整（双眼视差 / 辐辏 / 运动视差） |
| Duration 决定方式 | 软件设定 | 几何决定（对象在视野中的持续帧数） |
| 代表研究 | Ma 2021、Wu 2024 BD、Phan 2016 警告面板 | Kim 2018 Virtual Shadow、Chen 2024 Contact-Analog |

### 3.3 三类共形锁定

- **行人锁定（Pedestrian-conformal）**：图形位置随行人 GPS 移动
  - 例：Kim 2018 Virtual Shadow、Chen 2024 Contact-Analog、Wu 2024 BW
  - Duration = 行人在视野的持续帧数
- **路面锁定（Road-conformal）**：图形贴在道路的固定物理位置
  - 例：Wang ARive 2025 红地毯、Ma 2024 carpet
  - Duration = 危险区域在道路投射的持续帧数
- **世界锁定（World-conformal）**：图形与全局地图 / 环境坐标同步
  - 例：Roh 2023 AR 导航
  - Duration = 与全局导航路径同步

### 3.4 共形引入的时间维度新参数

**共形警告让 HUD 阶段不存在的两个时间参数变得关键**：

| 参数 | 典型值 | 依据 | 意义 |
|---|---|---|---|
| **跟随更新频率** | ≥ 60 Hz | Flicker fusion 阈值 | 低于 60 Hz 会感知到画面闪烁 |
| **跟随延迟** | < 100 ms | Adelstein (2003) VR 人因研究 | 超过 100 ms 会感知虚拟图形与真实场景脱离 |

**Kim 2018 报告系统延迟约 50 ms**；**Wang ARive 2025 HoloLens 2 端到端约 80 ms**——都在这个可接受区间内。

### 3.5 共形对 Duration 设计的根本影响

**共形让"至危险解除"从工程默认变成物理必然**：
- 屏幕固定条件：Duration 是软件设定的独立参数（如 Ma 2021 的 3 s）
- 共形条件：**Duration 默认由几何决定**（行人 / 危险区在视野中的持续时间）

但软件层仍可以叠加"最短显示时长"或"最长显示时长"的约束（如 Wang ARive 的实测 Duration 平均 2.7 s 就是几何加软件混合的结果）。

**对本研究的意义**：**RQ1 的对照条件"至危险解除"应严格操作化为"仅由几何决定，无强制时长约束"**——与"固定 1 s / 2 s / 3 s"的软件约束形成严格对照。

---

## 4. Phan (2016) 精读汇报（IMRD 完整展开）

本节按学术论文的**引言—方法—结果—讨论**四段范式完整汇报 Phan (2016)——AR-HUD 阶段较早系统建立"感知-警觉-预期"三层评估模型的实证研究。

### 4.1 Introduction（引言）

#### 4.1.1 研究背景

- **行人是最脆弱的道路使用者**（WHO 2013），在白天和夜晚都难以观察
- 现有 PCWS 能高精度检测行人，但报警方式多为蜂鸣声 + 仪表盘上的简单视觉提示——两类问题：
  - 声音报警只在驾驶员"了解声音含义"或"伴随视觉信息"时才有用
  - 模糊提示反而会让驾驶员困惑、产生分心
- **HUD + AR 视觉提示被认为是更优的解决路径**——让驾驶员视线保持在道路上、突出关键对象、引导驾驶员采取正确行动

#### 4.1.2 研究缺口

**缺口 1：DAP（Driver Awareness of Pedestrian）研究极少**——现有工作（Fukagawa 2013）只把"无事故发生"等同于"驾驶员已感知"，定义过于简化。

**缺口 2：AR 视觉线索"贴合式 vs 非贴合式"仍存争议**：
- Rusch (2013) 指出静态边界框反而比无视觉线索引发更长反应时
- Schall (2013) 则称边界框能改善老年驾驶员对低能见度危险的检测

Phan 的目标是**用系统实验解决这个矛盾**。

#### 4.1.3 研究假设

- **H1**：基于"贴合式边界框 + 非贴合式黄色行人警告面板"的 AR-PCW 能在**感知、警觉、预期**三个层级上提升驾驶员对行人的觉察
- **H2**：在引入前车随机加减速的跟车任务中，AR 提示能改变驾驶员策略——**让其降低跟车精度而提高对行人的注意**

**假设 H2 的特殊价值**：它承认 AR 提示的价值不是"两全其美"，而是"注意力重分配"——这是本文的方法学洞察。

### 4.2 Method（方法）

#### 4.2.1 被试

- 招募 27 人，2 人因模拟器晕动症未完成——最终 N = 25
- 性别比：21 男 / 4 女（**性别比不均是局限**）
- 年龄 21–35 岁（未给出 M、SD）
- 至少 3 年驾驶经验
- 均为学生、熟悉模拟器

#### 4.2.2 实验设计

- **类型**：组内（within-subject）
- **自变量**：HUD 配置（2 水平：noAR vs AR）
- **因变量**（分三层）：
  - **感知层**：VRT（Visual Reaction Time，以 TTC 计算的按键时刻）
  - **警觉层**：跟车距离 HVD（Head Vehicle Distance）、油门踏板位置 APP（Accelerator Pedal Position）
  - **预期层**：紧急刹车次数（刹车力 > 200 N 且 TTC < 2 s）
- **主观**：自评问卷 6 题

#### 4.2.3 实验材料与设备

**模拟器**：固定基座，由 Oktal 公司制造，SCANeR-Studio 驱动引擎。投影屏放置在驾驶员前方 1.5 m。

**模拟 HUD**：使用透明度更高的矩形区域渲染**中心 FOV 约 15°**——模拟车载组合式 HUD（Combiner HUD）。

**双 AR 视觉线索**：
- **贴合式**（world-locked）：包围行人的**黄色边界框**，随行人移动
- **非贴合式**（screen-fixed）：**警告面板**显示在 HUD 左下角，含黄色行人图标；虚拟焦距 2.5–4 m

**颜色选择依据**：黄色用于传达"警告"而非"立即威胁"（Chapanis 1994; Gelasca 2005）。

**触发逻辑（复合阈值）**：
- 边界框：检测到行人即显示
- 警告面板：`t_WP = min(t(TTC=2s), t(d=16.6m))`
- **TTC_critical = 2 s**：对应 McLaughlin (2008) 人群响应分布的 90% 覆盖率
- **d_critical = 16.6 m**：当车速 < 30 km/h 时优先采用，避免触发过晚

#### 4.2.4 场景与任务

- **主任务**：跟车任务，被试需保持与前车约 50 m 距离
- 前车在被试进入行人场景时（行人前方 100 m 范围内）随机加速——**引入干扰**
- 每次驾驶包含 **23 个行人事件**，位置、出现、行为随机
- 行人会"有意"过马路

**流程**：
1. 练习：驾驶员先在无行人场景下学习保持 50 m 跟车距离
2. 两次正式驾驶（noAR 与 AR 配置），每次 23 次行人事件
3. 被试察觉行人时按方向盘按钮（**仅 14 名按指示完成此动作**）
4. 每次 AR 驾驶后填问卷

#### 4.2.5 方法学局限（前置说明）

- **仅 14 人完成按键任务**——感知层 VRT 分析样本从 25 减到 14
- **23 场景重复呈现**——存在学习效应
- **性别比 21:4** 不平衡

### 4.3 Results（结果）

**Phan 首次为 AR 行人预警建立"感知-警觉-预期"三层评估模型**——后续 Kim 2018、Wu 2024、Chen 2024 等 AR-HUD 研究都沿用这个框架。

#### 4.3.1 感知层：VRT（Visual Reaction Time）——反映"注意觉察时机"

| # | 条件 | VRT（以 TTC 计算） | 反映的实际情况 |
|---|---|---|---|
| ① | noAR | ~3 s TTC（驾驶员在车距行人 3 s 处才察觉） | 无 AR 时觉察时机较晚，接近临界级 |
| | AR | **~4.5 s TTC**（提前 1.5 s 察觉） | AR 让觉察时机前移进入 Cautionary 区 |
| | ANOVA | F(1, 642) = 23.46, **p < 0.05** | 大效应量 |

**23 个场景中 AR 条件均更早察觉**——效应稳定。

**实际意义**：**感知层 VRT 反映"驾驶员注意觉察的时间点"——AR 贴合式提示让觉察前移 1.5 秒**，为后续制动准备留出更多时间。

#### 4.3.2 警觉层：HVD + APP——反映"注意分配的重新配置"

| # | 因变量 | 结果 | 反映的实际情况 |
|---|---|---|---|
| ② | **HVD**（跟车距离，m） | noAR = 86 m；AR = 118 m；F(1, 1148) = 13.25, **p < 0.05** | **AR 条件下跟车性能变差——但这是"有意为之"** |
| ③ | **APP**（油门踏板按压比例，0-1） | noAR = 0.46；AR = 0.23；F(1, 1148) = 18.47, **p < 0.05** | 驾驶员在 AR 条件下油门踩得更浅，**主动减速** |

**实际意义**：**警觉层 HVD 与 APP 揭示 AR 的核心机制不是"两全其美"，而是"注意力重分配"**——驾驶员牺牲跟车精度（HVD 从 86m 增到 118m）换取对行人的关注（APP 从 0.46 降到 0.23，主动减速）。

#### 4.3.3 预期层：Urgent Braking——反映"驾驶员的场景预判"

| # | 因变量 | 结果 | 反映的实际情况 |
|---|---|---|---|
| ④ | **紧急刹车次数** | noAR 共 72 次；AR 共 **11 次（减少 ~85%）** | AR 让"被动急刹"切换为"主动预判 + 缓刹" |

**实际意义**：**预期层紧急刹车次数反映"驾驶员对场景的预判能力"——AR 贴合式提示让被动急刹从 72 次减到 11 次**，说明驾驶员在 AR 条件下有充分的时间做出预判，避免了紧急制动。

#### 4.3.4 主观偏好

- **Q05**：25/25 被试希望车内装载 HUD + AR-PCW
- **Q06**：**17/25 偏好"边界框"而非"警告面板"**——他们认为边界框可定位行人，而警告面板"强迫他们刹车"并使其分心

**关键发现**：主观上驾驶员更接受贴合式（world-locked）的边界框，而不喜欢屏幕固定的警告面板——**这与客观数据的方向一致**。

#### 4.3.5 与文献的对比

- 与 Schall (2013) 一致：AR 提示帮助提前识别危险
- 与 Rusch (2013) 一致：贴合式 AR 提示能引导注意
- 反对 Dzindolet (2002) 部分论断：非贴合式"自动化辅助"可能分散注意，但本研究的"贴合式边界框"未见明显遮蔽效应

### 4.4 Discussion（讨论）

#### 4.4.1 Phan 的核心方法学贡献

**Phan 建立的"感知-警觉-预期"三层评估模型**成为 AR-HUD 研究的方法学范式基础——后续 Kim 2018（用 Situation Awareness L1/L2/L3 三层）、Wu 2024（用 TTFF + 注视次数 + 总时长三层）、Chen 2024（用 RT + 响应率 + UEQ 三层）均沿用类似框架。

#### 4.4.2 Phan 自陈的五个局限

1. **模拟器行人检测假定 100% 准确**——与现实不符（真实系统检测精度约 85-95%）
2. **样本仅 21–35 岁**——未涵盖老年
3. **23 场景重复呈现**——存在学习效应；驾驶员经历多次行人事件后变得更警觉
4. **仅在模拟器中验证**——未在真实道路或智能车平台测试
5. **只测中央 15° FOV**——未涉及更宽视场

#### 4.4.3 对本研究（HUD/AR-HUD 时间元素设计规范）的三个具体启示

**启示 1（继承）：三层因变量模型直接沿用**

Phan 的"感知（VRT/TTFF）+ 警觉（跟车距离/眼动分布）+ 预期（紧急刹车次数/最大减速度）"三层与 W1 Lübbe 的"救命 / 认知 / 力学"三层结构相互印证——形成方法学互补。**建议**：RQ1–RQ3 因变量设计融合两套框架——覆盖救命层（碰撞/启动率）、感知层（VRT/TTFF）、警觉层（HVD/眼动分布）、力学层（减速度/jerk）四层。

**启示 2（扩展）：复合阈值可扩展为独立自变量**

Phan 的 `min(TTC=2s, d=16.6m)` 是"时间 + 距离"双阈值。这为 RQ 提供了一个新的自变量维度——**"触发依据"（TTC vs 距离 vs 复合）** 可以作为一个显式的实验条件，检验哪种触发方式更符合驾驶员的自然认知。

**启示 3（设计选择）：贴合式（共形）作为 RQ 的核心自变量水平**

17/25 主观偏好贴合式 + 客观上紧急刹车减少 85%——**建议**：RQ1 应把行人锁定的共形警告作为核心自变量水平，与屏幕固定作对照。这与 RQ1 的"至危险解除"（共形几何决定）设计天然契合——**共形 + 至危险解除**是最符合驾驶员认知的时空设计组合。

---

## 5. 本周共识（Weekly Consensus）

本周提炼 5 条核心共识：

1. **AR-HUD 子集 26 篇的年份分布高度集中于近 5 年**（2021-2025 占 58%）——**AR-HUD 是新兴且中国有本土积累的领域**（中国新手样本 5 篇），本研究做中国样本并非孤立。

2. **Tönnis (2007) 的共形（Contact-Analog）概念是 AR-HUD 相较 HUD 的本质区别**——引入了跟随更新频率（≥ 60 Hz）和跟随延迟（< 100 ms）两个 HUD 阶段不存在的时间参数；**共形让"至危险解除"从工程默认变成物理必然**——这是 RQ1 中"至危险解除 vs 固定时长"对照的物理基础。

3. **Phan (2016) 建立的"感知-警觉-预期"三层评估模型**是 AR-HUD 研究的方法学范式基础——后续 Kim 2018、Wu 2024、Chen 2024 均沿用；本研究 RQ1–RQ3 因变量设计直接继承并与 W1 Lübbe 的"救命/认知/力学"三层融合为四层框架。

4. **Phan 揭示 AR 贴合式提示的核心价值是"注意力重分配 + 主动预判"**——**紧急刹车从 72 次减到 11 次（-85%）** ——不是"两全其美"而是"牺牲跟车换取行人关注"；这提示 RQ1 应把"跟车任务性能"作为副变量记录以捕捉这种权衡。

5. **AR-HUD 阶段虽总报告率提升 3.2 倍（8.6% → 27.8%），但 Duration 27% 和级间时序 23% 仍是空白主区**——RQ1 和 RQ2 的定位在 AR-HUD 阶段仍然成立；闪烁频率与 onset 动画维度暂搁置。

---

## 6. 下周（W5）计划

**主题**：AR-HUD 警告时机 + Kim (2018) 精读

**具体任务**：
1. **按 IMRD 范式完整精读 Kim (2018)**——AR-HUD 阶段唯一实车（户外停车场）实证研究，Virtual Shadow 贴合式 AR 警示的奠基性工作
2. 深化 AR-HUD 阶段的 TTC 双阈值（2.5 s / 5.0 s）设计逻辑与 SDT 框架的对应
3. 引入 TTMD（Time-to-Minimum-Distance）公式作为二维相交场景的新指标（Wang ARive 2025）
4. 对比 6 篇明确量化 TTC 的 AR-HUD 研究（Kim 2018 / Wang ARive 2025 / Wu 2024 / Chen 2024 / Huo 2025 / Phan 2016）
5. 分析共形警告在时间维度上的压缩效应（TTFF、RT、减速度惊吓）

**预期产出**：W05_AR-HUD警告时机_共形Lead Time.md（含 Kim 2018 IMRD 精读 + 6 篇 TTC 对照表 + 共形时间压缩分析 + 本周共识 5 条）

---

## 7. 本周引用 References

Adelstein, B. D., Lee, T. G., & Ellis, S. R. (2003). Head tracking latency in virtual environments: Psychophysics and a model. *Proceedings of the Human Factors and Ergonomics Society Annual Meeting*, *47*(20), 2083–2087.

Chapanis, A. (1994). Hazards associated with three signal words and four colours on warning signs. *Ergonomics*, *37*(2), 265–275.

Chen, W., Niu, L., Liu, S., Ma, S., Li, H., & Yang, Z. (2024). Evaluating the effectiveness of contact-analog and bounding box prototypes in augmented reality head-up display warning for Chinese novice drivers under various collision types and traffic density. *International Journal of Human-Computer Interaction*. https://doi.org/10.1080/10447318.2024.2327197

Dzindolet, M. T., Pierce, L. G., Beck, H. P., & Dawe, L. A. (2002). The perceived utility of human and automated aids in a visual detection task. *Human Factors*, *44*(1), 79–94.

Fukagawa, R. et al. (2013). Driver awareness of pedestrian in cross-walk situations. [Journal reference incomplete in source].

Gelasca, E. D., Tomasic, D., & Ebrahimi, T. (2005). Which colors best catch your eyes: A subjective study of color saliency. In *First International Workshop on Video Processing and Quality Metrics for Consumer Electronics*.

Kim, H., Gabbard, J. L., Anon, A. M., & Misu, T. (2018). Driver behavior and performance with augmented reality pedestrian collision warning: An outdoor user study. *IEEE Transactions on Visualization and Computer Graphics*, *24*(4), 1515–1524. https://doi.org/10.1109/tvcg.2018.2793680

Ma, J., Li, Y., & Zuo, Y. (2024). Design and evaluation of ecological interface of driving warning system based on AR-HUD. *Sensors*, *24*(24), 8010. https://doi.org/10.3390/s24248010

Ma, X., Jia, M., Hong, Z., Kwok, A. P. K., & Yan, M. (2021). Does augmented-reality head-up display help? A preliminary study on driving performance through a VR-simulated eye movement analysis. *IEEE Access*, *9*, 129951–129964.

McLaughlin, S. B., Hankey, J. M., & Dingus, T. A. (2008). A method for evaluating collision avoidance systems using naturalistic driving data. *Accident Analysis & Prevention*, *40*(1), 8–16.

Phan, M. T., Thouvenin, I., & Frémont, V. (2016). Enhancing the driver awareness of pedestrian using augmented reality cues. In *2016 IEEE 19th International Conference on Intelligent Transportation Systems (ITSC)* (pp. 1298–1304). IEEE. https://doi.org/10.1109/ITSC.2016.7795724

Rusch, M. L., Schall, M. C., Gavin, P., Lee, J. D., Dawson, J. D., Vecera, S., & Rizzo, M. (2013). Directing driver attention with augmented reality cues. *Transportation Research Part F: Traffic Psychology and Behaviour*, *16*, 127–137.

Schall, M. C., Rusch, M. L., Lee, J. D., Dawson, J. D., Thomas, G., Aksan, N., & Rizzo, M. (2013). Augmented reality cues and elderly driver hazard perception. *Human Factors*, *55*(3), 643–658.

Tönnis, M., Sandor, C., Klinker, G., Lange, C., & Bubb, H. (2007). Experimental evaluation of an augmented reality visualization for directing a car driver's attention. In *IEEE/ACM International Symposium on Mixed and Augmented Reality (ISMAR)* (pp. 56–59). IEEE.

Wang, W., Xu, J., Liu, X., & Zhang, X. (2025). ARive: Assisting drivers with in-car augmented reality for risk zone detection. *Proceedings of the ACM Symposium on User Interface Software and Technology (UIST)*.

Wu, Z., Liang, Y., Liu, G., & Ai, X. (2024). Comparative analysis of AR-HUDs crash warning icon designs: An eye-tracking study using 360° panoramic driving simulation. *Sustainability*, *16*(21), 9167. https://doi.org/10.3390/su16219167

---

*汇报状态：W4 完成（2026.07.18），继续沿用"每周一篇重点精读 + IMRD 完整展开 + 5 条本周共识"结构*
*下次汇报：W5（2026.07.25），主题 = AR-HUD 警告时机 + Kim (2018) IMRD 精读*
