# 第 4 周汇报：AR-HUD 时间元素检索 + 共形（Contact-Analog）概念引入

**汇报周次**：W4（2026.07.12 – 2026.07.18）
**汇报对象**：[导师姓名]
**汇报人**：[学生姓名]

---

## 1. 本周目标

W1–W3 已完成 HUD 子集（14 篇）的全面分析。本周转入 **AR-HUD 子集 26 篇**：

1. 完成 AR-HUD 子集 26 篇文献的检索情况补充统计
2. 引入"共形（Contact-Analog）"核心概念（Tönnis et al., 2007）及其对时间维度的新增需求
3. 按 AR-HUD 显示模式分类（行人锁定 / 路面锁定 / 世界锁定）
4. 提取 AR-HUD 子集时间 5 维报告情况，与 HUD 子集做对照
5. 评述 AR-HUD 阶段在时间设计上相较 HUD 的演进方向

---

## 2. AR-HUD 子集 26 篇检索补充情况

### 2.1 AR-HUD 子集年份分布

| 年份段 | 篇数 | 主要论文（前 3 篇） |
|---|---|---|
| 2008–2015 | 4 | Park (2013), Kim Casting Shadows (2016a), Kim Virtual Shadow (2016b) |
| 2016–2020 | 7 | Phan (2016), Kim AR PCW (2018), Zhou ARVE (2018), Kim & Gabbard (2019) |
| 2021–2025 | 15 | Ma (2021), Charissis (2021), Kettle (2022), Skirnewskaja (2022), Wang ARive (2025) |

**特征**：AR-HUD 文献近 5 年呈爆发式增长（15/26 = 58%），与共形 AR 硬件成熟同步。

### 2.2 AR-HUD 子集场景分布

| 实验环境 | 篇数 | 代表论文 |
|---|---|---|
| 固定基座驾驶模拟器 | 12 | Phan 2016, Wu 2024, Chen 2024 |
| 高保真 moving-base 驾驶模拟器 | 3 | Kim 2018, Kim 2023 自动驾驶 |
| VR HMD 驾驶仿真 | 5 | Ma 2021, Wang ARive 2025 (HoloLens 2) |
| 真实道路 / 户外停车场 | 2 | Kim 2018 户外停车场, Doshi 2008（HUD 但作为对照） |
| 综述 / 方法学 | 4 | Kettle 2022, Skirnewskaja 2022, Winkler & Soleimani 2025 |

### 2.3 AR-HUD 子集样本特征分布

| 被试群体 | 篇数 |
|---|---|
| 新手驾驶员（中国） | 5 篇（Chen 2024 contact-analog, Chen 2024 多目标, Ma 2024, Li 2025, Wu 2024） |
| 熟练驾驶员（欧美） | 8 篇（Kim 2018, Lübbe 2017 等） |
| 青年 vs 老年对比 | 1 篇（Kazazi 2015，HUD 已统计） |
| 大学生 / 混合 | 7 篇 |
| 无人因实验（综述 / 工程） | 5 篇 |

---

## 3. Contact-Analog 共形概念引入（Tönnis et al., 2007）

### 3.1 概念定义

> Tönnis, M., Sandor, C., Klinker, G., Lange, C., & Bubb, H. (2007). Experimental evaluation of an augmented reality visualization for directing a car driver's attention. In *2007 IEEE/ACM International Symposium on Mixed and Augmented Reality* (pp. 81–90).

**Contact-Analog（接触类比 / 共形）**：虚拟图形与真实世界对象在视野中**精确空间对齐**，使驾驶员的注意可被"锚定"到真实危险目标上而非屏幕固定位置。

**与屏幕固定（Screen-fixed）显示的本质区别**：
- Screen-fixed：虚拟图形位置不随头部 / 车辆运动；类似仪表盘信息
- Contact-Analog：虚拟图形位置实时跟随真实目标的视野坐标；要求 6-DoF 头部追踪 + 目标 6-DoF 检测

### 3.2 共形对时间设计的新增需求

共形显示的核心技术挑战是 **"实时跟随"**，这给时间维度引入了 HUD 阶段不存在的新参数：

1. **跟随更新频率**（Refresh Rate）：通常需 ≥ 60 Hz 以避免视觉抖动；硬件层约束
2. **跟随延迟容忍上限**（Latency Budget）：典型 < 100 ms，超过则产生视觉漂移
3. **运动跟随的时间一致性**：当行人快速横穿时，共形警告需"贴身追随"——这使"持续时长"概念被动态化（即 Duration 不再是"显示多少秒"而是"跟随多远距离 / 多少帧"）

### 3.3 共形显示的三类锁定模式（与时间的耦合）

| 锁定模式 | 时间维度含义 | 代表文献 |
|---|---|---|
| **行人锁定**（Pedestrian-conformal） | Duration = 行人在视野内持续帧数 | Kim 2018 Virtual Shadow, Wu 2024 BW 图标 |
| **路面锁定**（Road-conformal） | Duration = 危险区域在前方道路投射的持续帧数 | Wang 2025 ARive 红地毯, Ma 2024 carpet |
| **世界锁定**（World-conformal） | Duration = 与全局地图标记同步 | Roh 2023 AR navigation |

**关键洞察**：AR-HUD 引入共形后，**"至危险解除"不再是工程默认，而是物理上的必然**——行人离开视野（或离开危险区），共形图形自然消失。这与 HUD 阶段的"主动设定持续时长"形成本质对照。

---

## 4. AR-HUD 子集 26 篇时间 5 维报告情况

### 4.1 时间维度报告率（AR-HUD vs HUD 对比）

| 时间维度 | HUD 子集 14 篇 | AR-HUD 子集 26 篇 | 演进特征 |
|---|---|---|---|
| 警告时机（TTC / Lead Time） | 4/14 = 29% | **15/26 = 58%** | AR-HUD 阶段更系统量化 |
| 持续时长（Duration） | 1/14 = 7% | **7/26 = 27%** | 仍是空白主区，但已有"动态共形"作为新设计语言 |
| 闪烁频率 | 0/14 = 0% | **3/26 = 12%** | Huo & Alla, Ma 2024 饱和度脉动等开始量化 |
| onset-offset 动画 | 0/14 = 0% | **5/26 = 19%** | 共形跟随天然涉及过渡 |
| 升级时序（级间间隔） | 1/14 = 7% | **6/26 = 23%** | 三级 / 多目标分级出现，但级间阈值多未量化 |

**核心发现**：AR-HUD 阶段在所有 5 维上的报告率均显著提升，但**持续时长（27%）与升级时序（23%）仍是研究空白主区**——这恰好对应本硕士论文 RQ1+RQ2。

### 4.2 AR-HUD 子集时间维度明确量化情况一览

下表列出 AR-HUD 子集中**至少一维度明确量化**的 18 篇核心研究（其余 8 篇为综述或工程系统类）：

| idx | 第一作者 (年) | 锁定模式 | 量化时间维度 |
|---|---|---|---|
| 01 | Kim (2018) | Pedestrian-conformal | TTC 2.5/5.0 s 双阈值 |
| 02 | Phan (2016) | Pedestrian-conformal | TTC = 2 s 或 d = 16.6 m 复合 |
| 03/04 | Kim (2016a/b) | Pedestrian-conformal | Virtual Shadow 至危险解除 |
| 06 | Ma (2024) | Road-conformal | 三色渐变（pre-warning → warning → urgent） |
| 07 | Chen (2024) Contact-Analog | Pedestrian-conformal | THW ≤ 3 s |
| 08 | Wu (2024) | Pedestrian-conformal (BW) | TTC < 3 s, TTFF 量化 |
| 09 | 叶明慧 (2025) | 三平面定位 | Duration 3 s（参考 Ma 2021） |
| 10 | Tong (2021) | Pedestrian-conformal | 行人侧 AR 预警 |
| 13 | Kim & Gabbard (2019) | 综述 | 注视时长 ≤ 2 s 标准 |
| 17 | Roh (2023) | Road-conformal | 黄=行人 / 红=PMU |
| 18 | Park (2013) | 工程系统 | 三级（未量化） |
| 20 | Wang ARive (2025) | Road-conformal | TTMD ≤ 5 s + 2 s 二级 |
| 21 | Huo & Alla (2025) | Pedestrian-conformal | TTC = 2.5 s + 闪烁 |
| 23 | Kim (2023) | 自动驾驶 | 接管 10 s 预告 |
| 24 | Li (2025) | 雾天 | 信息冗余 vs 单一 |
| 27 | Ma (2021) | 屏幕固定 + 速度自适应 | Duration 3 s / 10–15 s |
| 30 | Frémont (2019) | 自适应 | 驾驶员未察觉时触发 |
| 36 | Strle (2023) | 综合 | 生理信号实时反馈 |
| 40 | Chen (2024) 多目标 | Pedestrian-conformal | 优先级分级（红/黄/绿） |

---

## 5. AR-HUD 阶段时间设计的演进方向

综合 §3 与 §4，可识别 AR-HUD 相较 HUD 阶段在时间设计上的 4 个演进方向：

### 5.1 演进 1：从"主动设定 Duration"到"共形动态消失"

HUD 阶段："显示 3 s 后消失"是软件层主动决策。
AR-HUD 阶段：行人离开视野后共形图形自然消失，Duration 由物理几何决定。

**对本研究的启示**：AR-HUD 阶段的"Duration 对照实验"应包含 **"至危险解除（动态）" vs "固定 3 s（强制）"** 的关键对照——这是 HUD 阶段未充分考察的对比。

### 5.2 演进 2：从"单级阈值"到"多级渐进"

HUD 阶段：Lübbe 1.8/2.5 s 二级是最复杂的设计。
AR-HUD 阶段：
- Ma (2024) 三色渐变（绿 → 黄 → 红，无明确级间时间）
- Wang ARive 二级 TTMD（5 s 提示 / 2 s 临界）
- Chen (2024) 多目标三级（红=立即 / 黄=接近 / 绿=远距）

**但级间间隔仍未量化**：Lübbe 0.7 s 仍是唯一明确级间间隔的研究，AR-HUD 阶段虽出现多级但**未给出级间最优时间**。

### 5.3 演进 3：从"瞬时呈现"到"运动跟随动画"

HUD 阶段：默认瞬时呈现。
AR-HUD 阶段：
- Kim (2018) Virtual Shadow 跟随行人位置滑动
- Wu (2024) BW 图标随行人位置动态跟随
- Ma (2024) carpet 随风险变化饱和度变化

**仍未量化的子维度**：跟随平滑度（更新帧率 vs 阶跃式） / onset-offset 淡入淡出过渡时长。

### 5.4 演进 4：从"固定阈值"到"自适应触发"

HUD 阶段：Frémont (2019), Doshi (2008) 是早期探索。
AR-HUD 阶段：
- Strle (2023) 多通道生理信号实时反馈（HRV / EDA / 瞳孔）→ AR-HUD 认知负荷预测 AUC 0.96–0.98
- Teng (2023) IVPM-GA 机器学习优化
- Frémont (2019) 自适应继续扩展

**仍未量化的子维度**：自适应触发与固定阈值的具体绩效差异。

---

## 6. AR-HUD 子集时间设计的核心研究空白识别

承接 W3 已识别的"Duration 与 Inter-level Interval 是 HUD 阶段最严重空白"，**W4 进一步识别 AR-HUD 阶段的特异性空白**：

| 空白类型 | 严重程度 | AR-HUD 独有性 | 本研究覆盖建议 |
|---|---|---|---|
| 固定 Duration vs "至危险解除"对照 | ⭐⭐⭐ | AR-HUD 特有（共形动态消失） | RQ1 核心 |
| 多级级间间隔（0.5 / 0.7 / 1.0 / 1.5 s） | ⭐⭐⭐ | 共享（HUD/AR-HUD 均缺） | RQ2 核心 |
| 共形跟随平滑度 vs 阶跃式 | ⭐⭐ | AR-HUD 特有 | 列为延伸 |
| onset-offset 渐变 vs 瞬时 | ⭐⭐ | AR-HUD 部分涉及 | 列为 RQ1 附属变量 |
| 自适应触发的可靠性临界值 | ⭐ | AR-HUD 特有 | 列为博士延伸 |

---

## 7. 本周结论

1. **AR-HUD 子集 26 篇在时间维度上比 HUD 子集报告率显著提升**：5 维报告率从 HUD 平均 8.6% 提升到 AR-HUD 平均 27.8%。

2. **Contact-Analog 共形概念是 AR-HUD 阶段的核心新增维度**：行人锁定 / 路面锁定 / 世界锁定三类模式各自对时间设计有不同要求，引入了"动态消失" / "运动跟随"等 HUD 阶段不存在的子维度。

3. **AR-HUD 阶段持续时长仍是空白主区（27% 报告率）**：尽管共形显示物理上支持"动态消失"，但**固定 Duration vs 动态消失的对照实验仍未出现**——这是本硕士论文 RQ1 的明确切入点。

4. **AR-HUD 阶段升级时序仍未量化级间间隔**：Ma 2024 三色渐变、Wang ARive 二级 TTMD、Chen 多目标分级均出现但**均无明确级间时间**，Lübbe (2017) 的 0.7 s 仍是唯一孤证。

5. **共形动态消失是 AR-HUD 时间设计的"语言转换"**：本硕士论文应将"至危险解除（动态）"作为 RQ1 实验的标准对照条件，把"固定 Duration"作为对照创新点。

---

## 8. 下周（W5）计划

**主题**：AR-HUD 警告时机与共形 Lead Time 深化分析

**具体任务**：
1. 详细分析 AR-HUD 子集 15 篇明确量化 TTC 的研究（Kim 2018 / Phan 2016 / Wu 2024 / Wang 2025 / Huo & Alla 2025 等）
2. 引入 TTMD（Wang ARive 公式）作为二维相交场景的新指标
3. 比较 AR-HUD 中"共形 vs 屏幕固定"的 TTC 阈值与绩效差异
4. 形成 AR-HUD TTC 阈值对照表 + 共形优势矩阵
5. 评述 AR-HUD TTC 设计的新增挑战（动态目标跟随、深度感知线索）

**预期产出**：W05_AR-HUD警告时机_共形Lead Time.md

---

## 9. 本周引用 References

Chen, W., Niu, L., Liu, S., Ma, S., Li, H., & Yang, Z. (2024). Evaluating the effectiveness of contact-analog and bounding box prototypes in augmented reality head-up display warning for Chinese novice drivers. *International Journal of Human-Computer Interaction*. https://doi.org/10.1080/10447318.2024.2327197

Chen, W., Song, C., Luo, J., Xu, Z., Li, H., Ma, S., Wang, Q., & Yang, Z. (2024). Priority design in multi-target AR-HUD warning: Evidence from eye movement and behavior of the novice driver. *International Journal of Human-Computer Interaction*. https://doi.org/10.1080/10447318.2024.2439572

Huo, F., & Alla, R. (2025). Differences in drivers' dependence on AR warning information in urban driving environments: The role of driving experience. *Frontiers in Virtual Reality*, *6*, 1638823. https://doi.org/10.3389/frvir.2025.1638823

Kim, H., Gabbard, J. L., Anon, A. M., & Misu, T. (2018). Driver behavior and performance with augmented reality pedestrian collision warning: An outdoor user study. *IEEE Transactions on Visualization and Computer Graphics*, *24*(4), 1515–1524. https://doi.org/10.1109/tvcg.2018.2793680

Kim, H., Isleib, J. D., & Gabbard, J. L. (2016a). Casting shadows: Ecological interface design for augmented reality pedestrian collision warning. In *2016 IEEE Virtual Reality (VR)* (pp. 235–236). IEEE. https://doi.org/10.1109/vr.2016.7504725

Kim, H., Isleib, J. D., & Gabbard, J. L. (2016b). Virtual shadow: Ecological interface design for augmented reality pedestrian collision warning. *Proceedings of the Human Factors and Ergonomics Society Annual Meeting*, *60*(1), 1838–1842. https://doi.org/10.1177/1541931213601474

Ma, J., Li, Y., & Zuo, Y. (2024). Design and evaluation of ecological interface of driving warning system based on AR-HUD. *Sensors*, *24*(24), 8010. https://doi.org/10.3390/s24248010

Phan, M. T., Thouvenin, I., & Frémont, V. (2016). Enhancing the driver awareness of pedestrian using augmented reality cues. In *2016 IEEE 19th International Conference on Intelligent Transportation Systems (ITSC)* (pp. 1298–1304). IEEE. https://doi.org/10.1109/itsc.2016.7795724

Strle, G., Košir, A., Sodnik, J., & Stojmenova, K. (2023). Physiological signals as predictors of cognitive load induced by the type of automotive head-up display. *IEEE Access*, *11*, 87884–87898. https://doi.org/10.1109/access.2023.3305383

Teng, J., Wan, F., Kong, Y., & Kim, J.-K. (2023). Machine learning-based cognitive load prediction model for AR-HUD to improve OSH of professional drivers. *Frontiers in Public Health*, *11*, 1195961. https://doi.org/10.3389/fpubh.2023.1195961

Tönnis, M., Sandor, C., Klinker, G., Lange, C., & Bubb, H. (2007). Experimental evaluation of an augmented reality visualization for directing a car driver's attention. In *2007 IEEE/ACM International Symposium on Mixed and Augmented Reality* (pp. 81–90). IEEE. https://doi.org/10.1109/ISMAR.2007.4538831

Wang, C., Chu, D., & Martens, M. (2025). ARive: Assisting drivers with in-car augmented reality for risk zone detection. *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies*, *9*(1), Article 22. https://doi.org/10.1145/3712270

Wu, Z., Liang, Y., Liu, G., & Ai, X. (2024). Comparative analysis of AR-HUDs crash warning icon designs: An eye-tracking study using 360° panoramic driving simulation. *Sustainability*, *16*(21), 9167. https://doi.org/10.3390/su16219167

---

*汇报状态：W4 完成（2026.07.18）*
*下次汇报：W5（2026.07.25），主题 = AR-HUD 警告时机与共形 Lead Time 深化*
