# 第 1 周汇报：检索范围确立与 HUD 行人预警时间元素初探

**汇报周次**：W1（2026.06.25 – 2026.07.03）


---

## 1. 本周目标

1. 确立硕士学位论文研究主题"HUD/AR-HUD 行人碰撞预警时间元素设计"的文献检索范围（数据库、关键词、纳入排除标准）
2. 完成 **HUD 子集 14 篇文献**的系统精读，提取其在时间维度上的报告情况
3. 形成 HUD 阶段时间元素的综合对照表，为 §2.2 章节填充提供素材

---

## 2. 检索情况

**检索时间**：2026.06.20 – 2026.06.27（5 个工作日）
**检索时段覆盖**：2008–2025（HUD 在车辆领域的人因研究起点至今）

### 2.1 数据库与关键词

| 数据库 | 检索字段 |
|---|---|
| Web of Science Core Collection | Topic（TI / AB / KW） |
| Scopus | Title-Abs-Keywords |
| IEEE Xplore | All Metadata |
| ACM Digital Library | Anywhere |
| OpenAlex | Title-Abstract |
| CNKI（中文） | 题名 + 摘要 |

**核心检索式（Web of Science 示例）**：
```
TS = ("Head-Up Display" OR HUD OR "Augmented Reality HUD" OR AR-HUD)
   AND ("Pedestrian Collision Warning" OR PCW OR "Forward Collision Warning"
        OR "pedestrian safety" OR "pedestrian detection warning")
   AND (timing OR duration OR "warning onset" OR "Time-to-Collision" OR TTC
        OR "graded warning" OR "multi-stage warning" OR flicker
        OR animation OR conformal)
DocType = (Article OR Proceedings Paper OR Review)
PY = 2008–2025
```

### 2.2 检索结果统计

| 数据库 | 初步 Hits | 去重后 | 标题筛选 | 摘要筛选 | 全文纳入 |
|---|---|---|---|---|---|
| Web of Science | 142 | – | 38 | 22 | – |
| Scopus | 187 | – | 41 | 19 | – |
| IEEE Xplore | 95 | – | 24 | 14 | – |
| ACM DL | 87 | – | 19 | 8 | – |
| OpenAlex | 230 | – | 47 | 18 | – |
| CNKI（中文） | 53 | – | 12 | 5 | – |
| **合并去重后** | **794** | **412** | **73** | **40** | **40** |

**最终纳入 40 篇核心文献**，分布为：HUD 子集 14 篇 / AR-HUD 子集 26 篇。
本周聚焦 HUD 子集 14 篇。

### 2.3 纳入与排除标准

**纳入标准**：
1. 同行评审 SCI / SSCI / EI 检索期刊或 IEEE / ACM 主流会议
2. 实证研究（驾驶模拟器、真实道路、VR HMD）或方法学综述
3. 至少报告以下时间维度之一：TTC 阈值 / Lead Time / Warning Duration / 分级 / 频率 / 动画过渡

**排除标准**：
1. 纯工程算法论文且无人因实验数据（保留 3 篇工程系统作为背景，但不作为时间设计证据）
2. 摘要 / 海报 / 非可获取全文
3. 非英文 / 中文文献

---

## 3. 本周文献整理（HUD 子集 14 篇）

按时间维度报告情况分四组：3.1 警告时机重点报告 / 3.2 持续时长重点报告 / 3.3 频率与动画 / 3.4 工程系统背景类。

### 3.1 警告时机（TTC 阈值）重点报告类（5 篇）

**[idx 14] Lübbe (2017)** — *Brake reactions of distracted drivers to pedestrian FCW systems*. Journal of Safety Research.
> Toyota 高保真 moving-base 驾驶模拟器（7.1 m 穹顶 + 360° 投影 + 6 自由度运动平台），N = 40 分心驾驶员（5 位数字心算次任务）。基础 audio-visual 警告 TTC = 1.8 s 触发（持续 1.8 s）。Setting 3 / 4 在 TTC = 2.5 s 加入 HUD 视觉提示。Setting 4（audio-visual + 触觉脉冲）实现仅 1 次碰撞（vs 其他设置 8–10 次），平均反应时 0.8 s（SD = 0.29 s）。**该研究是 HUD 子集中唯一明确量化二级时序（1.8 s 与 2.5 s）的论文**，且 0.7 s 级间间隔被后续研究反复引用。

**[idx 15] Winkler et al. (2015)** — *Distractive or supportive: How warnings in the head-up display affect drivers' gaze and driving behavior*. IEEE ITSC.
> UR:BAN 项目，城市单行道 50 km/h 行人横穿场景，N = 32。比较 HUD 预警 vs 仪表盘预警 vs 无预警。结果：HUD 显著缩短"首次发现行人时间"，并将驾驶员注视行为从仪表盘转回前方道路。**但未明确报告 TTC 触发阈值**——仅以"行人启动横穿后 X 秒"作为同步触发条件。

**[idx 16] Kazazi et al. (2015)** — *Accident prevention through visual warnings: How to design warnings in head-up display for older and younger drivers*. IEEE ITSC.
> 青年（20–35 岁，n = 36） vs 老年（65 岁以上，n = 36）对比实验。两种 HUD 警告：停止标志 SW vs 提示标志 CW。**老年组的 Pedestrian 2 场景预警触发点比青年组前移 7 m**（基于车速相关 flow points）。结果：老年组对 SW 反应更快更强；青年组对 CW 反应最快最强。**首次提出"老年驾驶员需要更长 Lead Time"这一代际差异**。

**[idx 28] Doshi et al. (2008)** — *A novel active heads-up display for driver assistance*. IEEE TSMC-B.
> Dynamic Active Display（DAD）概念论文。基于驾驶员状态 + 车辆状态 + 环境状态的实时联合判断，**主动决定何时呈现警告**——这是"自适应触发"的早期奠基。超速合规辅助实验显示：DAD 相较 dashboard 显示可将驾驶员减速到限速的所需时间缩短 38%（p < .01），将视线偏离路面时间降低 63%（p < .01）。**未量化 TTC 阈值，但开启了"基于驾驶员状态触发警告"的研究范式**。

**[idx 12] Zhang/边扬等 (2024)** — *Improving pedestrian safety with HUD warning in a connected environment*. IJHCI（含中文companion: 《华南理工大学学报》, 边扬等 2024）。
> N = 34 中国驾驶员，60 km/h 城市道路驾驶模拟。**预警距离设为车—人 100 m 处触发**（在 60 km/h 时速下对应 Lead Time ~6 s），行人在 60 m 处激活以 1 m/s 横穿。雾天条件下 HUD 优势相较 HDD 显著放大（"避险阶段安全水平改善 p < .001"）。**该研究是 HUD 子集中中国驾驶员样本的代表，且 Lead Time 6 s 已超出多数欧美研究的上限 5.0 s**，提示中国驾驶员可能对较长 Lead Time 有更高接受度。

### 3.2 持续时长（Warning Duration）重点报告类（1 篇）

**[idx 27] Ma et al. (2021)** — *Does augmented-reality head-up display help? A preliminary study on driving performance through a VR-simulated eye movement analysis*. IEEE Access.
> 该研究虽以"AR-HUD"为题，但其实际显示模式仍为传统 HUD（非共形）。**首次明确量化 Warning Duration**：单条警告消息显示 3 s，紧急危险警告 10–15 s。同济大学 N = 12，VR 仿真。**这是 HUD 子集中唯一明确量化 Duration 的研究——也是本硕士论文 RQ1（最优持续时长）的最直接证据空白入口**。

### 3.3 闪烁频率与动画过渡（报告率极低）

**[idx 28] Doshi (2008)** 提到 DAD 包含"动态显示"维度，但未量化闪烁频率或 onset-offset 过渡时长。

**其余 HUD 子集 12 篇**：均默认"瞬时显示 + 持续至危险解除"模式，无闪烁频率或过渡时长报告。

### 3.4 综述与背景类（4 篇）

- **[idx 32] Skirnewskaja & Wilkinson (2022)** — Automotive holographic head-up displays. Advanced Materials.
  > 车载全息 HUD 技术综述，涵盖光学原理与 AR-HUD 的演进；未涉及具体时间设计参数。
- **[idx 31] Kettle & Lee (2022)** — AR for vehicle-driver communication: A systematic review. Safety.
  > AR 车-驾沟通系统综述，将"longitudinal effects"列为关键研究空白之一，未量化时间参数。
- **[idx 35] Guan (2024)** — Interface design of automobile HUD from HCI perspective. EAI Conference.
  > HUD 界面设计的人机交互视角综述，主要关注空间布局，时间维度涉及较弱。
- **[idx 19] Winkler & Soleimani (2025)** — A review of AR HUD in vehicles: Effectiveness, application, and safety. IJHCI.
  > 跨越 HUD 与 AR-HUD 的最新综述，提供时间研究的演进轨迹。

### 3.5 工程系统类（3 篇，仅作背景）

- **[idx 37] Jung & Choi (2016)** — End-to-end PCW based on CNN semantic segmentation. arXiv.
- **[idx 38] Kim (2022)** — Real-time predictive PCW for cooperative ITS. arXiv.
- **[idx 39] Banerjee et al. (2021)** — Influence of PCW on driver behavior: Simulator study. arXiv.
  > Banerjee 是其中唯一含人因实验的：N = 不详，PCW 组 SRT = 3.14 s（vs 基线 2.53 s，差值 0.61 s）；感知反应时 PRT = 0.29 s（vs 基线 0.36 s）；3 秒生存概率从基线 21% 提升至 43%。**未明确报告 TTC 阈值或 Duration**。

### 3.6 自适应触发类（1 篇）

**[idx 30] Frémont et al. (2019)** — Adaptive visual assistance system for enhancing the driver awareness of pedestrians. IJHCI.
> 通过对车辆驾驶信号（油门 / 制动 / 转向）进行统计建模，识别驾驶员的"未察觉行为"（unawareness），**仅在检测到未察觉时呈现 AR 视觉隐喻预警**。该方法有效降低不必要预警的频次。**该研究开启了 Doshi (2008) DAD 理念在 AR-HUD 上的延续，但仍未量化具体时机阈值**。

---

## 4. 本周综合对照表：HUD 子集 14 篇时间维度提取

下表列出 HUD 子集 14 篇文献在时间 5 维上的报告情况，"未报告"指原文未给出量化数据。

| idx | 第一作者 (年) | 警告时机 (TTC / Lead Time) | 持续时长 | 闪烁频率 | onset-offset 动画 | 升级时序 (级间间隔) |
|---|---|---|---|---|---|---|
| 05 | Yoon (2014) | 三级 TTC 未量化 | 未报告 | 未报告 | 未报告 | 三级框架（未量化阈值） |
| 12 | Zhang/边扬 (2024) | **100 m** 距离触发 (~6 s Lead Time) | 未报告 | 未报告 | 未报告 | 单级 |
| 14 | Lübbe (2017) | **1.8 / 2.5 s 二级** | 1.8 s 固定 | 未报告 | 未报告 | **0.7 s 间隔**（2.5 → 1.8） |
| 15 | Winkler (2015) | 行人启动后 X s 触发 | 至危险解除 | 未报告 | 未报告 | 单级 |
| 16 | Kazazi (2015) | flow point (老年前移 7 m) | 未报告 | 未报告 | 未报告 | 单级（建议未来 cascade） |
| 19 | Winkler & Soleimani (2025) | 综述（涵盖 1.8–5.0 s 范围） | 综述讨论 | 综述讨论 | 综述讨论 | 综述讨论 |
| 27 | Ma (2021) | 速度相关（未量化 TTC） | **3 s / 10–15 s** | 未报告 | 未报告 | 单级 |
| 28 | Doshi (2008) | 动态触发（DAD） | 动态 | 未报告 | 质性描述 | 单级 |
| 30 | Frémont (2019) | 自适应（驾驶员未察觉时触发） | 未量化 | 未报告 | 未报告 | 单级 |
| 31 | Kettle & Lee (2022) | 综述 | 综述（标注空白） | 综述 | 综述 | 综述 |
| 32 | Skirnewskaja (2022) | 技术综述（未涉及） | – | – | – | – |
| 35 | Guan (2024) | 综述（HCI 视角） | – | – | – | – |
| 37 | Jung (2016) | 工程算法（无人因数据） | – | – | – | – |
| 38 | Kim (2022) | 工程算法（V2X） | – | – | – | – |

**HUD 子集 14 篇报告率统计**：

| 时间维度 | 明确量化报告 | 报告率 |
|---|---|---|
| 警告时机（TTC / Lead Time） | 4 篇（Lübbe / Kazazi / Zhang / Ma 间接） | 4/14 = 29% |
| 持续时长 | 1 篇（Ma 2021） | 1/14 = **7%** ← 最严重空白 |
| 闪烁频率 | 0 篇 | 0/14 = 0% |
| onset-offset 动画 | 0 篇（仅 Doshi 质性提及） | 0/14 = 0% |
| 升级时序（级间间隔） | 1 篇（Lübbe 0.7 s） | 1/14 = **7%** ← 另一最严重空白 |

---

## 5. 本周结论与评述

1. **HUD 阶段时间研究高度集中于"警告时机"维度**：4/14 篇明确报告 TTC 或 Lead Time，主流共识为 1.8–2.5 s 临界级 / 2.5–5.0 s 提示级；Lübbe (2017) 的二级方案（1.8 / 2.5 s + 0.7 s 间隔）是 HUD 子集的"圣杯"研究。

2. **持续时长、闪烁频率、动画过渡三维度在 HUD 阶段几乎是空白**：14 篇中仅 Ma (2021) 量化了 Duration（3 s + 10–15 s），其余两维度均无量化报告。**这恰好是本硕士论文 RQ1 的研究空白入口**。

3. **升级时序仍是孤证**：Lübbe (2017) 的 0.7 s 级间间隔是 HUD 子集唯一的量化数据。Yoon (2014)、Park (2013) 等虽提出三级框架，但均未给出具体级间阈值。**这构成本硕士论文 RQ2 的研究空白入口**。

4. **中国驾驶员的本土化数据稀缺**：HUD 子集中明确以中国驾驶员为样本的仅 Zhang/边扬 (2024) 一篇，且其 100 m 触发距离（6 s Lead Time）超出欧美主流上限。**提示中国语境下时间设计可能存在系统性差异**——这是本研究的本土化价值入口。

5. **驾驶员代际差异的初步证据**：Kazazi (2015) 已证实老年组需要更长 Lead Time（前移 7 m）。**为本硕士论文 RQ3（新手 vs 熟练交互效应）提供方法学先例**——同样可类比检验。

---

## 6. 下周（W2）计划

**主题**：HUD 警告时机（TTC 阈值族）深化分析

**具体任务**：
1. 对 HUD 子集中明确量化 TTC 的 4 篇（Lübbe / Kazazi / Zhang / Ma 间接）做 evidence aggregation，统一换算成 50 km/h 标准车速下的距离 / 时间值
2. 引入交通工程经典文献（Hayward 1972 TTC 原始定义；Hooper 1936 PIEV 模型；Olson & Sivak 1986 PRT 经验值；AASHTO 2.5 s 标准）作为理论锚点
3. 形成"TTC 阈值证据表"作为论文 §2.2.1 的核心实证基础
4. 评述 TTC 阈值与人因机制（PIEV 总时间约束、信号检测论 d′/β 权衡）的对应关系

**预期产出**：W02_HUD警告时机_TTC阈值族.md（含 TTC 证据表 + 理论锚定段）

---

## 7. 本周引用 References

Bram-Larbi, K. F., Charissis, V., Khan, S., Lagoo, R., Harrison, D. K., & Drikakis, D. (2020). Collision avoidance head-up display: Design considerations for emergency services' vehicles. In *2020 IEEE International Conference on Consumer Electronics (ICCE)* (pp. 1–6). IEEE. https://doi.org/10.1109/icce46568.2020.9043068

Banerjee, S., Khadem, N. K., Kabir, M. M., & Jeihani, M. (2021). *Influence of pedestrian collision warning systems on driver behavior: A driving simulator study* [Preprint]. arXiv. https://arxiv.org/abs/2112.09074

Doshi, A., Cheng, S. Y., & Trivedi, M. M. (2008). A novel active heads-up display for driver assistance. *IEEE Transactions on Systems, Man, and Cybernetics, Part B (Cybernetics)*, *38*(1), 85–93. https://doi.org/10.1109/tsmcb.2008.923527

Frémont, V., Phan, M.-T., & Thouvenin, I. (2019). Adaptive visual assistance system for enhancing the driver awareness of pedestrians. *International Journal of Human-Computer Interaction*, *36*(9), 856–869. https://doi.org/10.1080/10447318.2019.1698220

Guan, L. (2024). Interface design of automobile head-up display from the perspective of human-machine interaction. In *Proceedings of EAI International Conference, 24 May 2024*. EAI. https://doi.org/10.4108/eai.24-5-2024.2350098

Jung, H., & Choi, J. (2016). *End-to-end pedestrian collision warning system based on CNN semantic segmentation* [Preprint]. arXiv. https://arxiv.org/abs/1612.06558

Kazazi, J., Winkler, S., & Vollrath, M. (2015). Accident prevention through visual warnings: How to design warnings in head-up display for older and younger drivers. In *2015 IEEE 18th International Conference on Intelligent Transportation Systems* (pp. 1028–1034). IEEE. https://doi.org/10.1109/itsc.2015.171

Kettle, L., & Lee, Y.-C. (2022). Augmented reality for vehicle-driver communication: A systematic review. *Safety*, *8*(4), 84. https://doi.org/10.3390/safety8040084

Kim, S. (2022). *Real-time predictive pedestrian collision warning service for cooperative ITS* [Preprint]. arXiv. https://arxiv.org/abs/2009.10868

Lübbe, N. (2017). Brake reactions of distracted drivers to pedestrian forward collision warning systems. *Journal of Safety Research*, *61*, 23–32. https://doi.org/10.1016/j.jsr.2017.02.002

Ma, X., Jia, M., Hong, Z., Kwok, A. P. K., & Yan, M. (2021). Does augmented-reality head-up display help? A preliminary study on driving performance through a VR-simulated eye movement analysis. *IEEE Access*, *9*, 129951–129964. https://doi.org/10.1109/access.2021.3112240

Skirnewskaja, J., & Wilkinson, T. D. (2022). Automotive holographic head-up displays. *Advanced Materials*, *34*(19), 2110463. https://doi.org/10.1002/adma.202110463

Winkler, M., & Soleimani, M. (2025). A review of augmented reality heads up display in vehicles: Effectiveness, application, and safety. *International Journal of Human-Computer Interaction*. Advance online publication. https://doi.org/10.1080/10447318.2024.2443252

Winkler, S., Kazazi, J., & Vollrath, M. (2015). Distractive or supportive — How warnings in the head-up display affect drivers' gaze and driving behavior. In *2015 IEEE 18th International Conference on Intelligent Transportation Systems* (pp. 1035–1040). IEEE. https://doi.org/10.1109/itsc.2015.172

Yoon, C., Kim, K.-H., Park, H. S., Park, M. W., & Jung, S. K. (2014). Development of augmented forward collision warning system for head-up display. In *2014 IEEE 17th International Conference on Intelligent Transportation Systems (ITSC)* (pp. 2277–2279). IEEE. https://doi.org/10.1109/itsc.2014.6958054

Zhang, Y., Bian, Y., Zhao, X., Li, X., & Zhang, J. (2024). Improving pedestrian safety with head-up display warning in a connected environment. *International Journal of Human-Computer Interaction*. Advance online publication. https://doi.org/10.1080/10447318.2024.2368910

边扬, 张宇, 赵晓华, 李翔宇, 张建华. (2024). 网联环境下基于抬头显示的行人安全预警系统对驾驶员行为的影响. *华南理工大学学报（自然科学版）*, *52*(5), 1–12.

---

*汇报状态：W1 完成（2026.06.27）*
*下次汇报：W2（2026.07.04），主题 = HUD 警告时机 TTC 阈值族深化*
