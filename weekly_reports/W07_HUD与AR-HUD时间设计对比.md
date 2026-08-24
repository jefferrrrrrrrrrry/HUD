# 第 7 周汇报：HUD vs AR-HUD 时间设计对比矩阵 + 评估指标分类

**汇报周次**：W7（2026.08.02 – 2026.08.08）
**汇报对象**：[导师姓名]
**汇报人**：[学生姓名]

---

## 1. 本周目标

W1–W6 已完成 HUD（14 篇）与 AR-HUD（26 篇）两个子集的独立分析。本周做**对比综合**：

1. 整合两个子集证据，形成"HUD vs AR-HUD 时间设计对比矩阵"
2. 评估指标按"行为 / 眼动 / 主观 / 生理"四层分类
3. 共形 vs 屏幕固定的"时间-空间耦合"效应总结
4. 评述 AR-HUD 阶段相较 HUD 阶段的 4 项核心演进与 5 项遗留空白
5. 为 §2.2 与 §2.3 的桥接段提供素材

---

## 2. HUD vs AR-HUD 时间设计对比矩阵（W7 核心产出）

### 2.1 五维度对比矩阵

| 维度 | HUD 子集 14 篇 | AR-HUD 子集 26 篇 | 演进特征 |
|---|---|---|---|
| **警告时机** | 4/14 = 29% 量化 / 临界 1.8 s / 提示 2.5 s / 中国冗余 6.0 s | 15/26 = 58% 量化 / 临界 2.0–2.5 s / 提示 3.0–5.0 s / 二维 TTMD 2/5 s | 双阈值与复合公式成为主流 |
| **持续时长** | 1/14 = 7% 量化（Ma 2021 3 s + 10–15 s） | 7/26 = 27% 量化 / 集中在 2.5–3.0 s 或动态消失 | 共形动态消失成为新设计语言；固定 vs 动态对照仍缺 |
| **闪烁频率** | 0/14 = 0% | 3/26 = 12%（Huo & Alla, Ma 2024 等） | AR-HUD 首次出现闪烁明确报告 |
| **onset-offset 动画** | 0/14 = 0%（仅 Doshi 质性） | 5/26 = 19%（Kim 2018 Virtual Shadow 滑动等） | AR-HUD 共形跟随天然涉及过渡 |
| **升级时序** | 1/14 = 7%（Lübbe 0.7 s 孤证） | 6/26 = 23%（Ma 三色 / Wang TTMD 二级 / Chen 多目标） | 多级出现但级间时间间隔仍未量化 |

**总报告率**：HUD = 8.6% vs AR-HUD = 27.8%（**AR-HUD 整体提升 3.2 倍**）

### 2.2 时间设计参数的"演进-空白"二维图

```
              报告率高
                ▲
                │
                │ AR-HUD 警告时机 (58%)
                │           ●
                │
                │ HUD 警告时机 (29%) AR-HUD Duration (27%)
                │           ●               ●
                │
                │ AR-HUD 升级 (23%) AR-HUD onset (19%)
                │           ●               ●
                │
                │ AR-HUD 闪烁 (12%) HUD Duration (7%)  HUD 升级 (7%)
                │           ●               ●               ●
                │
                │ HUD 闪烁 (0%)  HUD onset (0%)
                │           ●               ●
                │
        ────────┼──────────────────────────────────────►
              报告率低     HUD                              AR-HUD
```

**核心识别**：
- **左下角**（HUD 闪烁 / HUD onset）：极度空白，但本研究 RQ 不优先覆盖（伦理 / 硬件约束）
- **中下区域**（HUD Duration 7% / HUD 升级 7% / AR-HUD 升级 23%）：**本研究 RQ1+RQ2 核心切入点**
- **右上区域**（AR-HUD 警告时机 58%）：相对成熟，本研究作为对照锚点而非创新点

---

## 3. 评估指标四层分类

W1–W6 涉及的评估指标按数据采集层分类如下：

### 3.1 行为层指标（驾驶绩效）

| 指标 | 定义 | 代表文献 | 主要测量精度 |
|---|---|---|---|
| **PRT**（感知反应时） | 刺激出现到开始制动 | Banerjee 2021, Lübbe 2017 | 10 ms |
| **SRT**（速度降低反应时） | 警告出现到车速明显降低 | Banerjee 2021 | 100 ms |
| **TTC@brake-onset** | 制动启动时的 TTC | Kim 2018 | 50 ms |
| **最大减速度** | 制动过程峰值减速度 | Kim 2018, Banerjee 2021 | 0.1 m/s² |
| **最小冲突距离** | 全过程车-人最近距离 | Zhang 2024 | 0.5 m |
| **首次制动距离** | 首次踩下制动时车-人距离 | Zhang 2024 | 0.5 m |
| **碰撞次数** | 实验全程碰撞计数 | Lübbe 2017 | 整数 |
| **3 秒生存概率** | 警告后 3 秒内未碰撞概率 | Banerjee 2021 | 百分比 |

### 3.2 眼动层指标

| 指标 | 定义 | 代表文献 | 主要测量精度 |
|---|---|---|---|
| **TTFF**（首次注视时间） | 刺激出现到首次注视该区域 | Wu 2024, Chen 2024 | 10 ms |
| **注视次数**（Fixation count） | 单个 trial 内注视该 AOI 的次数 | Wu 2024, Chen 2024 | 整数 |
| **注视时长**（Fixation duration） | 单次或累积注视时长 | Kim & Gabbard 2019 | 10 ms |
| **眼跳次数**（Saccade count） | 单个 trial 内的眼跳次数 | Chen 2024 | 整数 |
| **注视熵 Hs**（Stationary Gaze Entropy） | 空间注视分布的香农熵 | Chen 2024 | 0.01 bit |
| **注视转移熵 Ht**（Gaze Transition Entropy） | 注视转移模式的可预测性 | Chen 2024 | 0.01 bit |

### 3.3 主观层指标

| 指标 | 定义 | 代表文献 | 量表范围 |
|---|---|---|---|
| **NASA-TLX** | 综合工作负荷主观评分 | Strle 2023, Ma 2024 | 0–100（六维：心智 / 体力 / 时间 / 表现 / 努力 / 挫败） |
| **DALI** | 驾驶专用工作负荷 | Ma 2024 | 7 维 |
| **SUS**（System Usability Scale） | 系统可用性 | Cheng 2022, Wu 2024 | 0–100 |
| **UEQ**（User Experience Questionnaire） | UX 6 维 | Kim 2023 | -3 至 +3 |
| **Trust Scale**（Jian, Bisantz, Drury 2000） | 自动化系统信任度 | 本研究 RQ3 候选 | 7 项 |

### 3.4 生理层指标

| 指标 | 定义 | 代表文献 | 主要测量精度 |
|---|---|---|---|
| **瞳孔直径** | 瞳孔大小变化（认知负荷代理） | Ma 2024, Wu 2024 | 0.1 mm |
| **HRV**（心率变异性） | 自主神经活动指标 | Strle 2023, Teng 2023 | 1 ms |
| **EDA / GSR**（皮电反应） | 唤醒与情绪反应 | Strle 2023 | 0.01 μS |
| **皮温** | 周围血管反应 | Strle 2023 | 0.1°C |
| **EEG** | 脑电活动 | Strle 2023（提及，未实施） | 1 ms / 1 μV |

### 3.5 评估指标在 HUD vs AR-HUD 中的使用频率对比

| 指标层 | HUD 子集使用率 | AR-HUD 子集使用率 | 演进 |
|---|---|---|---|
| 行为层（≥ 3 指标） | 4/14 = 29% | 18/26 = 69% | AR-HUD 阶段更系统 |
| 眼动层（≥ 2 指标） | 2/14 = 14% | 12/26 = 46% | AR-HUD 阶段大幅提升 |
| 主观层 | 3/14 = 21% | 19/26 = 73% | AR-HUD 阶段普遍使用 |
| 生理层 | 0/14 = 0% | 4/26 = 15% | AR-HUD 阶段新增 |
| **多模态融合**（≥ 3 层） | 1/14 = 7% | 8/26 = 31% | AR-HUD 阶段成为趋势 |

**核心识别**：AR-HUD 阶段的研究方法学**显著比 HUD 阶段更多模态**。本研究 RQ1–RQ3 实验应采用**行为 + 眼动 + 主观 + 生理**四层融合测量。

---

## 4. 共形 vs 屏幕固定的"时间-空间耦合"效应

承接 W5 §4 已分析的共形优势，本节系统化总结：

### 4.1 共形警告在时间维度上的优势矩阵

| 因变量 | 屏幕固定 | 行人锁定共形 | 效应量 | 文献来源 |
|---|---|---|---|---|
| TTFF | 2562 ms | 617 ms | **−76%**（4.15×） | Wu 2024 BW vs BD |
| 反应时（行人场景） | 1.45 s | 1.07 s | **−26%** | Chen 2024 |
| 反应时（追尾场景） | 1.27 s | 0.91 s | **−28%** | Chen 2024 |
| 减速度峰值 | +34.46% over baseline | +14.21% | **−59% 惊吓**减少 | Kim 2018 |
| 制动距离精度 | 高 SD | 低 SD | – | Kim 2018 |

### 4.2 共形优势的反例（条件依赖性）

| 反例 | 原因 | 文献 |
|---|---|---|
| Mental demand 增加 23.7% | 共形 + 视觉复杂度高 | Kim & Gabbard 2019 |
| HUD 注视时长延长 (3.33 vs 1.17 s) | 注意隧道 | Kim & Gabbard 2019 |
| 5 目标场景下分级优势消失 | 刺激密度饱和 | Chen 2024 |
| 行人场景 Bounding Box > Contact-Analog | 视觉显著性差异 | Chen 2024 |

**结论**：共形优势是**有条件的**——视觉复杂度低 / 单目标 / 行人锁定 三个条件需同时满足。本研究 RQ1 实验设计应控制这三个条件。

### 4.3 时间-空间耦合机制假设

基于上述对比，可提出耦合机制：

**假设 1（空间锚定降低时间需求）**：共形警告将"信息呈现物理坐标"与"实际危险物理坐标"对齐，减少了驾驶员的坐标系转换，故 TTFF 与反应时同步压缩。

**假设 2（共形 Duration 由几何决定）**：行人锁定共形警告的 Duration 等于行人在视野内的持续时间，故 Duration 不再是软件层主动设定，而是物理几何的副产品。

**假设 3（共形分级可在空间维度而非时间维度实施）**：Chen 2024 多目标分级使用颜色（红 / 黄 / 绿）做分级而非时间间隔——这是 AR-HUD 阶段升级时序"空间化"的萌芽。

---

## 5. AR-HUD 相较 HUD 的 4 项核心演进与 5 项遗留空白

### 5.1 核心演进（4 项）

1. **时间触发语言多元化**：从单值 TTC 到双阈值（Kim 2018）/ 复合公式（Phan 2016）/ TTMD（Wang 2025）/ THW（Chen 2024）
2. **Duration 从主动设定到共形动态消失**：物理几何替代软件层决策
3. **从瞬时呈现到运动跟随动画**：引入跟随平滑度、跟随延迟两个新子维度
4. **多模态评估（行为 + 眼动 + 主观 + 生理）成为新规范**：单层测量逐步退场

### 5.2 遗留空白（5 项，按优先级）

| 优先级 | 空白 | 备选研究 RQ |
|---|---|---|
| ⭐⭐⭐ | 固定 Duration（1 / 2 / 3 s）vs "至危险解除"动态对照 | RQ1 |
| ⭐⭐⭐ | 级间时间间隔（0.5 / 0.7 / 1.0 / 1.5 s）对照 | RQ2 |
| ⭐⭐ | Duration × 车速交互效应 | RQ1 × 车速 |
| ⭐⭐ | 中国驾驶员的 TTC 偏好曲线 | RQ3 中国语境 |
| ⭐ | 跟随平滑度与跟随延迟的人因边界 | 博士延伸 |

---

## 6. 本周结论

1. **AR-HUD 阶段时间设计的报告率全面高于 HUD 阶段**（27.8% vs 8.6%），但**Duration 与级间时间间隔仍是最严重空白**（7%–27% 区间），构成本研究 RQ1+RQ2 的明确切入点。

2. **评估指标已演进至多模态融合**：AR-HUD 阶段 31% 的研究采用 ≥ 3 层指标融合（行为 + 眼动 + 主观 + 生理），HUD 阶段仅 7%。本研究 RQ1–RQ3 应采用 4 层融合规范。

3. **共形警告的优势是条件依赖的**：视觉复杂度低 / 单目标 / 行人锁定 三条件需同时满足。本研究 §3 实验设计应明确控制这些条件。

4. **时间-空间耦合机制提示**："共形 Duration 由几何决定"是 AR-HUD 时间设计的新范式——本研究 RQ1 的核心对照应为"固定 vs 动态消失"而非"短 vs 长"。

5. **AR-HUD 阶段升级时序的"空间化"萌芽**：Chen 2024 多目标分级使用颜色而非时间间隔——本研究 RQ2 应**首次将颜色分级与时间分级解耦对照**。

---

## 7. 下周（W8）计划

**主题**：空间维度背景化简表

**具体任务**：
1. 整合 40 篇文献的空间维度信息（锁定方式 / FOV / 颜色 / 形状 / 动效）
2. 简化为 2–3 张表格作为论文 §2.1.3 与附录 A 的素材
3. 与时间维度的对照关系做单段评述
4. 不展开为独立子节——保持空间维度的"背景化"定位

**预期产出**：W08_空间维度背景化简表.md

---

## 8. 本周引用 References

Chen, W., Niu, L., Liu, S., Ma, S., Li, H., & Yang, Z. (2024). Evaluating the effectiveness of contact-analog and bounding box prototypes in augmented reality head-up display warning for Chinese novice drivers. *IJHCI*. https://doi.org/10.1080/10447318.2024.2327197

Chen, W., Song, C., Luo, J., Xu, Z., Li, H., Ma, S., Wang, Q., & Yang, Z. (2024). Priority design in multi-target AR-HUD warning. *IJHCI*. https://doi.org/10.1080/10447318.2024.2439572

Jian, J.-Y., Bisantz, A. M., & Drury, C. G. (2000). Foundations for an empirically determined scale of trust in automated systems. *International Journal of Cognitive Ergonomics*, *4*(1), 53–71. https://doi.org/10.1207/S15327566IJCE0401_04

Kim, H., & Gabbard, J. L. (2019). Assessing distraction potential of augmented reality head-up displays for vehicle drivers. *Human Factors*, *64*(5), 852–865. https://doi.org/10.1177/0018720819844845

Kim, H., Gabbard, J. L., Anon, A. M., & Misu, T. (2018). Driver behavior and performance with augmented reality pedestrian collision warning. *IEEE TVCG*, *24*(4), 1515–1524. https://doi.org/10.1109/tvcg.2018.2793680

Shiferaw, B., Crewther, D., & Downey, L. A. (2018). Gaze entropy measures detect alcohol-induced driver impairment. *Drug and Alcohol Dependence*, *191*, 250–257. https://doi.org/10.1016/j.drugalcdep.2018.07.014

Strle, G., Košir, A., Sodnik, J., & Stojmenova, K. (2023). Physiological signals as predictors of cognitive load induced by the type of automotive head-up display. *IEEE Access*, *11*, 87884–87898. https://doi.org/10.1109/access.2023.3305383

Wu, Z., Liang, Y., Liu, G., & Ai, X. (2024). Comparative analysis of AR-HUDs crash warning icon designs. *Sustainability*, *16*(21), 9167. https://doi.org/10.3390/su16219167

---

*汇报状态：W7 完成（2026.08.08）*
*下次汇报：W8（2026.08.15），主题 = 空间维度背景化简表*
