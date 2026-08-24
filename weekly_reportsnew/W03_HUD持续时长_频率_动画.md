# 第 3 周汇报：HUD 持续时长（Duration）深化 + Ma (2021) 精读

**汇报周次**：W3（2026.07.05 – 2026.07.11）
**汇报对象**：[导师姓名]
**汇报人**：[学生姓名]

---

## 1. 本周目标

承接 W2 已建立的 HUD 警告时机理论框架，本周聚焦 HUD 子集**报告率最低的关键维度——持续时长（Duration）**：

1. 分析 HUD 子集 Duration 报告分布——1/14 = 7% 报告率的空白现状
2. **按 IMRD 范式完整精读 Ma (2021)**——HUD 子集内唯一明确量化 Duration 的研究
3. 引入 Duration 上下界的经典理论锚点：
   - 下界：Posner (1980) 注意定向
   - 上界：Sokolov (1963) 神经习惯化 + Bliss (2003) 虚警疲劳
   - 单通道约束：Wickens (2002) 多资源理论
4. 论证 Duration 作为 RQ1 核心切入点的设计逻辑
5. 提炼本周 5 条共识

**说明**：闪烁频率与 onset-offset 动画过渡两个维度在 HUD 子集 14 篇中报告率均为 0%——本研究阶段不作为独立主题展开，仅在 §3 综合对照表内标注"未报告"作为背景。

---

## 2. HUD 子集 Duration 现状与理论上下界

### 2.1 Duration 报告分布

W1 已识别 HUD 子集 14 篇中仅 1 篇明确量化 Duration（Ma 2021）。通过细读 summaries，可识别其余 13 篇的**隐含**显示模式：

| 隐含模式 | 文献数 | 代表研究 | 问题 |
|---|---|---|---|
| 至危险解除（dynamic dismissal） | 6 篇 | Winkler (2015), Doshi (2008), Frémont (2019) | 未量化"危险解除"的判定条件 |
| 与触发刺激同步固定时长 | 3 篇 | Lübbe (2017) 1.8 s | 仅与 TTC 阈值对应，非独立 Duration 设计 |
| 完全未涉及 | 4 篇 | Yoon (2014), Zhang (2024), 工程系统类 | 论文聚焦其他维度 |

**关键问题**：**现有 HUD 文献中"至危险解除"是默认模式，但无任何论文系统比较了"至危险解除" vs "固定时长"的优劣**。这正是 RQ1 实验的核心对照设计。

### 2.2 Duration 边界的理论锚点（4 篇经典理论）

#### 2.2.1 Duration 下界：Posner (1980) 注意定向最低时间

> Posner, M. I. (1980). Orienting of attention. *Quarterly Journal of Experimental Psychology*, *32*(1), 3–25.

**核心结论**：视觉刺激出现到注意定向稳定建立需 **150–300 ms**；从注意定向到信息提取需另 **300–500 ms**。

**对 Duration 下界的约束**：警告必须至少持续 **500 ms** 才能保证驾驶员完成"注意定向 + 信息提取"两阶段。若 Duration < 0.5 s，则可能在驾驶员尚未完成注意定向之前即消失——这是"过短 Duration"的人因下界。

#### 2.2.2 Duration 上界：Sokolov (1963) 神经习惯化

> Sokolov, E. N. (1963). *Perception and the conditioned reflex*. Pergamon Press.

**核心结论**：反复呈现的相同刺激会经历神经习惯化（neural habituation），匹配-不匹配（matching-mismatch）模型预测注意捕获能力随时间衰减。

**对 Duration 上界的约束**：长时间持续的警告（> 10 s）可能反而降低有效性。Ma (2021) 的紧急 10–15 s 上限可能已逼近该约束。

#### 2.2.3 Duration 上界：Bliss (2003) 虚警疲劳

> Bliss, J. P. (2003). Investigation of alarm-related accidents and incidents in aviation. *International Journal of Aviation Psychology*, *13*(3), 249–268.

**核心结论**：当系统的虚警率超过 30% 时，驾驶员对警告的信任度与响应速度显著下降。

**对 Duration 上界的约束**：长 Duration（且后续虚警）累积效应导致信任崩溃。**对 PCW 系统而言，Duration > 5 s 可能加速信任校准失败**。

#### 2.2.4 Duration 与单通道约束：Wickens (2002, 2008) 多资源理论

> Wickens, C. D. (2002, 2008). 多资源理论核心论文。

**核心结论**：视觉-空间通道在 TTC 较短情境下负载迅速饱和；增加额外视觉刺激（如 AR-HUD 警告图标）可能产生认知干扰。

**对 Duration 设计的约束**：单通道视觉警告的 Duration 需保留"驾驶员视线回到道路"的窗口；推荐 Duration ≤ 3 s（即驾驶员单次注视 HUD 不超过 2 s + 一次眼跳缓冲）。

### 2.3 Duration 合理设计区间

综合四个理论锚点：

| 边界 | 数值 | 依据 |
|---|---|---|
| **物理下界** | ≥ 500 ms | Posner 注意定向 + 信息提取 |
| **认知推荐** | ≤ 3 s | Wickens 单通道负载饱和 |
| **绝对上界** | ≤ 5–10 s | Sokolov 习惯化 + Bliss 虚警疲劳 |

**RQ1 拟设 4 档 Duration**：1 s / 2 s / 3 s / **至危险解除（动态消失）**——覆盖从下界到 Wickens 推荐上限的完整实证区间，并首次纳入"至危险解除" vs "固定时长"的对照。

---

## 3. Ma (2021) 精读汇报（IMRD 完整展开）

本节按学术论文的**引言—方法—结果—讨论**四段范式完整汇报 Ma (2021)，重点回答四个问题：

- **引言**：为什么在这个时间点做 AR-HUD 布局研究？Duration 3 s 是怎么选的？
- **方法**：VR HMD + 眼动是可行的方法学吗？Ma 的规格设计合理吗？
- **结果**：分散 vs 密集布局的对照发现了什么？各因变量反映驾驶员的什么真实情况？
- **讨论**：Ma 自陈的局限是什么？对本研究的启示？

### 3.1 Introduction（引言）

#### 3.1.1 研究背景

- **驾驶涉及视觉、注意、记忆、感知-运动技能等多维认知资源**——美国 NHTSA 数据显示分心驾驶占 2012 年所有死亡事故的 10%、伤亡事故 18%、机动车事故 16%
- **驾驶员 80% 的信息来自前视视觉**（业内公认的经验值）
- **AR-HUD 承诺**把信息直接叠加到挡风玻璃上、维持视觉资源专注于前方道路——这是相较传统 HDD 的核心优势

#### 3.1.2 研究缺口

**两条关键缺口**：

1. **AR-HUD 尚未量产**、市售产品稀少、难以做真车实验——实证证据必须靠仿真获得。这构成一个方法学层面的必要性。
2. **AR-HUD 的界面布局设计缺乏系统对照**——特别是分散布局（元素分布在不同视场区域）与密集布局（元素集中某一区域）的绩效差异未量化。

#### 3.1.3 Duration 3 s + 10-15 s 的选择依据

Ma 在方法段明确交代——3 s 依据 **Wickens (2002) 多资源理论**："3 s 时长足以完成视觉信息加工 + 决策准备 + 至少一次眼跳回到前方道路"；紧急警告 10-15 s 对应"驾驶员需要更长时间理解 + 执行避险动作"。

**但作者本人在讨论段明确指出**："**the optimal duration remains an open question for future research**"——他承认这只是工程经验值，不是实证最优值。**这一句话直接为本硕士论文 RQ1 提供方向背书**——Ma 自己承认这是空白。

#### 3.1.4 研究问题

- **RQ1**：AR-HUD 系统是否提升驾驶绩效？（对照 No AR-HUD vs 两种 AR-HUD 布局）
- **RQ2**：不同 AR-HUD 界面布局对驾驶绩效的影响？（对照分散 vs 密集）

### 3.2 Method（方法）

#### 3.2.1 被试

- N = 12（男 6 女 6）
- 年龄 21–25 岁
- 至少 3 年驾龄
- 均使用过 VR 设备
- 视力正常/矫正正常
- 实验前 24 h 无饮酒、3 h 无剧烈运动
- **样本量偏小是明显局限**，作者自己也承认是 preliminary study

#### 3.2.2 实验设计

- **类型**：被试内设计
- **自变量**：AR-HUD 条件（3 水平）：No AR-HUD / AR-HUD1（分散布局，dispersed layout）/ AR-HUD2（密集布局，dense layout）
- **因变量**（分三层）：
  - 视觉搜索层：区域关注时长、视觉搜索广度、扫视速度分布
  - 车辆控制层：车速、油门/刹车踏板变化模式
  - 生理层：眨眼频率、眨眼时长

#### 3.2.3 设备与刺激规格

**VR + 眼动 + 物理设备**：
- HTC VIVE Pro Eye VR 头盔（内置眼动追踪）
- 高性能 PC + Unity 3D 虚拟环境
- 压力传感踏板 + 转角传感方向盘
- 引入光照烘焙 + 实时光、全局光照 GI、雨/雪/沙暴/暮光等天气

**AR-HUD 界面设计的关键规格**（本课题重点提取）：
- **单一界面元素数量**：7–9 个（依据 Miller 1956 短期记忆容量）
- **单条警告时长**：**3 s**
- **紧急危险警告时长**：**10–15 s**
- **视场角随车速分级**：
  - < 75 km/h → **65°** 双眼视场
  - > 75 km/h → **40°** 双眼视场
- **颜色编码（4 色 HEX）**：
  - #FE0000（纯红）：紧急警告（行人检测、车体碰撞）
  - #2979FF（深蓝）：驾驶辅助（导航箭头、车速、油量）
  - #4ADE80（绿）
  - #F26D21（橙）
- **粒子着色器渲染 AR 半透明 Sprite** 叠加到挡风玻璃

#### 3.2.4 场景与任务

- 一段直线道路 + 两个十字路口
- 保持稳定车速 40 m/s（论文原文写 m/s，从上下文推断实际约为 40 km/h）
- 两个路口设置周边车辆突然加速以测试 AR-HUD 预警效用
- 要求驾驶员注意行人、车辆、绿色"建筑"图标（模拟导航功能）
- 整个实验约 10 分钟

### 3.3 Results（结果）

**Ma 报告的因变量可按视觉搜索层 / 车辆控制层 / 生理层三层解读**——每一层反映驾驶员的不同真实情况。

#### 3.3.1 视觉搜索层——反映"注意分配策略"

| # | 因变量 | 结果 | 反映的实际情况 |
|---|---|---|---|
| ① | **水平视野广度**（SD） | F(2) = 4.312, p = 0.022；AR1 > AR2 | **分散布局迫使驾驶员做更广的视觉扫描**——注意力分布在多个区域；密集布局让注意力集中一区 |
| ② | **峰值扫视速度**（°/s） | No AR = 7607（最高，被无关物体吸引）；AR1 = 5977（最低，注视精准）；AR2 = 6147 | **无 AR 时驾驶员被无关物体反复吸引，扫视频繁但低效**；AR 辅助下扫视目标明确 |
| ③ | **不同区段扫视速度分布** | 无 AR 在 50-150°/s 段最活跃（低幅短扫视频繁），AR 条件在 150-450°/s 段更活跃 | **符合"认知分心补偿"假说**——无 AR 时驾驶员用大量低幅扫视代偿信息缺失 |

#### 3.3.2 车辆控制层——反映"操作模式"

| # | 因变量 | 结果 | 反映的实际情况 |
|---|---|---|---|
| ④ | **车速** | F = 166.99, p < 0.001；AR2 > No AR > AR1 | AR1 最稳、AR2 最快——**布局影响速度控制策略** |
| ⑤ | **油门均值** | AR1 vs AR2 t = 2.52, p = 0.0269；AR1 显著低于 AR2 | **AR1 是"小幅度多频次精细调整"、AR2 是"大幅度低频调整"**——布局改变操作模式 |
| ⑥ | **刹车均值（突发情境）** | AR2 显著低于 AR1（t = 2.51, p = 0.0272） | **AR2 密集布局在紧急响应上更优、AR1 在日常控速上更优**——这是一个反直觉的双面性发现 |

#### 3.3.3 生理层——反映"负荷与放松度"

| # | 因变量 | 结果 | 反映的实际情况 |
|---|---|---|---|
| ⑦ | **眨眼频率** | F = 5.686, p = 0.008；No AR > AR2 | **AR-HUD 辅助下驾驶员更放松**——眨眼频率降低通常代表认知负荷降低或专注度提高（Doughty 2003） |
| ⑧ | **眨眼时长** | 无显著差异 | 单次眨眼动作稳定，不受布局影响 |

#### 3.3.4 一句话总结结果

**AR-HUD 有效，但布局是"日常 vs 紧急"的权衡**——分散布局利日常巡航（精细控速、注意广泛分布），密集布局利紧急响应（快速反应、注意集中一区）。**这直接暗示 Duration 也可能存在"日常 vs 紧急"的分场景需求**——RQ1 的 4 档设计应涵盖这个可能。

### 3.4 Discussion（讨论）

#### 3.4.1 Ma 自陈的核心局限——3 s 是工程经验值

**Ma 在讨论段明确写道**：**"the optimal duration remains an open question for future research"** ——3 秒依据 Wickens 多资源理论推导，但没有做过 1、2、4、5 秒的对照实验，也没有做过"至危险解除"的对照。**这一句话直接为本研究 RQ1 提供方向背书**——Ma 自己承认这是空白。

#### 3.4.2 Ma 自陈的五个具体局限

1. **仅 12 人**——preliminary 规模，不足以做交互效应检验
2. **未集成 EEG 等生理指标**——只有眨眼频率作为生理代理
3. **VR 下深度提示有限**——虚拟深度与真实深度差距可能影响外推效度
4. **驾驶任务过于简单**——直线 + 2 路口，无变道、超车、倒车
5. **未研究 AR 图形对比度、光照变化、车速变化**等情境因素

#### 3.4.3 对本研究（HUD/AR-HUD 时间元素设计规范）的三个具体启示

**启示 1（继承）：Duration 应分场景对照**

Ma 揭示"分散布局利日常、密集布局利紧急"——这暗示 Duration 也可能需要分场景。**建议**：RQ1 设 **4 档 Duration（1 s / 2 s / 3 s / 至危险解除）**，覆盖从 Posner 下界（0.5 s）到 Wickens 推荐上限（3 s）到"动态消失"的完整区间。同时把车速作为二档控制变量（40 km/h 与 60 km/h）——检验 Duration × 车速的交互。

**启示 2（方法学）：VR + 眼动是可行的 preliminary 方法学，但需扩展样本**

Ma 的 VR + 眼动 + 物理设备组合可复用，但 **N = 12 只能定性**。**建议**：RQ1 采用**驾驶模拟器 + 眼动仪**替代 VR HMD——避免 VR 的深度感知失真（Ma 自己承认 VR 深度提示有限）；样本扩展到 **N ≥ 80** 以支撑 4 × 2 混合设计的统计功效。

**启示 3（扩展）：布局与 Duration 应联合设计**

如果 AR2 密集布局在紧急响应上更优，那么紧急场景下 Duration 短（如 1-2 s）可能足够；日常场景下 Duration 长（如 3-5 s）配合分散布局可能更好。**建议**：RQ1 的附加变量可以包含"警告呈现风格"（简洁 vs 详细）作为 2 水平副变量——检验 Duration 与呈现风格的联合效应。

---

## 4. 本周共识（Weekly Consensus）

本周提炼 5 条核心共识：

1. **HUD 子集 Duration 报告率仅 7%**——14 篇里只有 Ma 2021 一篇量化、其余 6 篇隐含"至危险解除"、3 篇触发同步固定、4 篇未涉及；**没有一篇系统对照过"固定 vs 动态"**——这是 RQ1 的天然空白入口。

2. **Duration 的理论上下界已由经典文献钉住**——**下界 500 ms**（Posner 注意定向 + 信息提取）；**认知推荐 ≤ 3 s**（Wickens 单通道负载饱和）；**绝对上界 5-10 s**（Sokolov 神经习惯化 + Bliss 虚警疲劳）。

3. **Ma (2021) 的 3 s + 10-15 s 是工程经验值不是实证最优值**——**作者本人在讨论段明确写道 "the optimal duration remains an open question"**——直接为 RQ1 提供方向背书。

4. **Ma (2021) 反直觉地揭示"分散布局利日常、密集布局利紧急"**——这暗示 Duration 应分场景对照——常规和紧急可能需要不同的时长阈值；**RQ1 应设 4 档 Duration**（1 s / 2 s / 3 s / 至解除）覆盖完整区间。

5. **闪烁频率与 onset 动画维度 HUD 子集 0% 报告率**——本研究阶段暂搁置，聚焦 Duration（7%）与级间间隔（7%）两个空白维度作为 RQ1 与 RQ2 的核心。

---

## 5. 下周（W4）计划

**主题**：AR-HUD 时间元素检索 + Phan (2016) 精读 + 共形（Contact-Analog）概念引入

**具体任务**：
1. 完成 AR-HUD 子集 26 篇文献的检索情况补充表——细分年份、场景类型、样本特征
2. 引入 **Tönnis et al. (2007) 的共形（Contact-Analog）概念**及其对时间维度的影响
3. **按 IMRD 范式完整精读 Phan (2016)**——AR-HUD 阶段较早系统建立"感知-警觉-预期"三层评估模型的研究，首次对比 conformal（贴合式）vs non-conformal 两种 AR 提示
4. 按显示模式分类：行人锁定 / 路面锁定 / 世界锁定（为 W8 空间维度详细简表预热）
5. 提取 AR-HUD 子集 26 篇在时间 5 维上的报告情况（对照 W1 HUD 子集的统计）
6. 评述 AR-HUD 阶段相较 HUD 阶段在时间设计上的演进方向

**预期产出**：W04_AR-HUD时间元素检索.md（含 Phan 2016 IMRD 精读 + 共形概念引入 + 时间 5 维报告率对照 + 本周共识 5 条）

---

## 6. 本周引用 References

Bliss, J. P. (2003). Investigation of alarm-related accidents and incidents in aviation. *International Journal of Aviation Psychology*, *13*(3), 249–268. https://doi.org/10.1207/S15327108IJAP1303_04

Doshi, A., Cheng, S. Y., & Trivedi, M. M. (2008). A novel active heads-up display for driver assistance. *IEEE Transactions on Systems, Man, and Cybernetics, Part B (Cybernetics)*, *38*(1), 85–93.

Doughty, M. J. (2003). Consideration of three types of spontaneous eyeblink activity in normal humans. *Optometry and Vision Science*, *80*(11), 725–733.

Frémont, V., Phan, M.-T., & Thouvenin, I. (2019). Adaptive visual assistance system for enhancing the driver awareness of pedestrians. *International Journal of Human-Computer Interaction*, *36*(9), 856–869.

Kim, H., Gabbard, J. L., Anon, A. M., & Misu, T. (2018). Driver behavior and performance with augmented reality pedestrian collision warning: An outdoor user study. *IEEE Transactions on Visualization and Computer Graphics*, *24*(4), 1515–1524.

Lübbe, N. (2017). Brake reactions of distracted drivers to pedestrian forward collision warning systems. *Journal of Safety Research*, *61*, 23–32. https://doi.org/10.1016/j.jsr.2017.02.002

Ma, X., Jia, M., Hong, Z., Kwok, A. P. K., & Yan, M. (2021). Does augmented-reality head-up display help? A preliminary study on driving performance through a VR-simulated eye movement analysis. *IEEE Access*, *9*, 129951–129964. https://doi.org/10.1109/access.2021.3112240

Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review*, *63*(2), 81–97.

Posner, M. I. (1980). Orienting of attention. *Quarterly Journal of Experimental Psychology*, *32*(1), 3–25. https://doi.org/10.1080/00335558008248231

Sokolov, E. N. (1963). *Perception and the conditioned reflex*. Pergamon Press.

Wickens, C. D. (2002). Multiple resources and performance prediction. *Theoretical Issues in Ergonomics Science*, *3*(2), 159–177. https://doi.org/10.1080/14639220210123806

Wickens, C. D. (2008). Multiple resources and mental workload. *Human Factors*, *50*(3), 449–455. https://doi.org/10.1518/001872008X288394

Winkler, S., Kazazi, J., & Vollrath, M. (2015). Distractive or supportive — How warnings in the head-up display affect drivers' gaze and driving behavior. In *2015 IEEE 18th International Conference on Intelligent Transportation Systems* (pp. 1035–1040). IEEE.

Yantis, S., & Hillstrom, A. P. (1994). Stimulus-driven attentional capture: Evidence from equiluminant visual objects. *Journal of Experimental Psychology: Human Perception and Performance*, *20*(1), 95–107.

Yoon, C., Kim, K.-H., Park, H. S., Park, M. W., & Jung, S. K. (2014). Development of augmented forward collision warning system for head-up display. In *2014 IEEE 17th International Conference on Intelligent Transportation Systems (ITSC)* (pp. 2277–2279). IEEE.

Zhang, Y., Bian, Y., Zhao, X., Li, X., & Zhang, J. (2024). Improving pedestrian safety with head-up display warning in a connected environment. *International Journal of Human-Computer Interaction*.

---

*汇报状态：W3 完成（2026.07.11），继续沿用"每周一篇重点精读 + IMRD 完整展开 + 5 条本周共识"结构*
*下次汇报：W4（2026.07.18），主题 = AR-HUD 时间元素检索 + Phan (2016) IMRD 精读 + 共形概念引入*
