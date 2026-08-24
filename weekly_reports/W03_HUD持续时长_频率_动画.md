# 第 3 周汇报：HUD 持续时长 / 闪烁频率 / onset-offset 动画过渡

**汇报周次**：W3（2026.07.05 – 2026.07.11）
**汇报对象**：[导师姓名]
**汇报人**：[学生姓名]

---

## 1. 本周目标

承接 W2 已建立的 HUD 警告时机理论框架，本周聚焦 HUD 子集**报告率最低的三个时间维度**——持续时长（Duration）/ 闪烁频率（Frequency）/ onset-offset 动画过渡：

1. 详细分析 Ma (2021) 的 3 s + 10–15 s 设计依据（HUD 子集唯一明确量化 Duration 的研究）
2. 引入习惯化与虚假警报疲劳（Sokolov 1963；Bliss 2003）作为 Duration 上界理论
3. 引入注意定向（Posner 1980）作为 Duration 下界理论
4. 形成 HUD 子集 Duration / Frequency / Onset 三张细分表
5. 论证这些维度作为本研究 RQ1 切入点的优势

---

## 2. 本周文献整理

### 2.1 Duration 维度：Ma (2021) 单点证据深度分析

**[idx 27] Ma et al. (2021)** — *Does augmented-reality head-up display help? A preliminary study on driving performance through a VR-simulated eye movement analysis*. IEEE Access.

**设计依据**（来自论文 §3.2）：
- 单条警告消息显示时长 = **3 s**
- 紧急危险警告消息时长 = **10–15 s**
- 作者引用依据：参考 Wickens (2002) 的多资源理论，"3 s 时长足以完成视觉信息加工 + 决策准备 + 至少一次眼跳回到前方道路"

**实验车速分级**：
- < 75 km/h：FOV 85°，单条警告 3 s
- 75–100 km/h：FOV 65°，紧急警告 10 s
- > 100 km/h：FOV 40°，紧急警告 15 s

**未提供的对照数据**：
- 1 s / 2 s / 4 s / "至危险解除"四档 Duration 的对比 → **完全缺失**
- Duration × 车速交互的具体绩效曲线 → 仅提供 FOV 分级建议，未给出量化绩效

**评述**：Ma (2021) 的 3 s 数值实质是"工程经验值"而非"实证最优值"，作者本人在 Discussion 中亦明确指出"the optimal duration remains an open question for future research"。**这恰好为本硕士论文 RQ1 提供方向上的明确性背书**——Ma 2021 的作者已在论文中承认这是空白。

### 2.2 Duration 维度：HUD 子集其余 13 篇的隐含模式

W1 已识别 HUD 子集 14 篇中仅 1 篇明确量化 Duration。但通过细读 summaries，可识别其余 13 篇的**隐含**显示模式：

| 隐含模式 | 文献数 | 代表研究 | 问题 |
|---|---|---|---|
| 至危险解除（dynamic dismissal） | 6 篇 | Winkler (2015), Doshi (2008), Frémont (2019) | 未量化"危险解除"的判定条件 |
| 与触发刺激同步固定时长 | 3 篇 | Lübbe (2017) 1.8 s | 仅与 TTC 阈值对应，非独立 Duration 设计 |
| 完全未涉及 | 4 篇 | Yoon (2014), Zhang (2024), 工程系统类 | 论文聚焦其他维度 |

**关键发现**：现有 HUD 文献中"至危险解除"是默认模式，但**无任何论文系统比较了"至危险解除" vs "固定时长"的优劣**。这正是 RQ1 实验的核心对照设计。

### 2.3 闪烁频率（Frequency）维度：HUD 子集完全空白

HUD 子集 14 篇中**零篇**明确量化闪烁频率（Hz）或脉动周期。

**唯一相关讨论**：Doshi (2008) 的 Dynamic Active Display（DAD）概念论文提到"display can be modulated in brightness or opacity to attract attention"，但未给出量化频率。

**理论参考**：
- Vehicle ergonomics 文献中"高紧迫感警告"的推荐闪烁频率为 **2–4 Hz**（Edworthy et al., 1991, 听觉警告理论的视觉延伸）
- 4 Hz 以上接近"flicker fusion"上限，被认为可能引发不适或癫痫风险（FDA 警告指南）
- 1 Hz 以下接近"缓慢闪烁"，紧迫感不足

**评述**：HUD 子集中闪烁频率的空白比 Duration 还严重——**Ma (2021) 至少在 Duration 上做了一次量化，闪烁频率 0/14 是完全的零起点**。这一空白虽然不在本硕士论文 RQ1/RQ2 的核心范围，但可作为研究展望或博士阶段的延伸方向。

### 2.4 onset-offset 动画过渡维度：HUD 子集完全空白

HUD 子集 14 篇中**零篇**明确量化警告出现 / 消失的动画过渡时长（如淡入 / 淡出毫秒数）。

**间接证据**：
- HUD 显示器硬件层面：液晶 / OLED 投影机的响应时间通常 < 10 ms，对感知层"瞬时显示" vs "渐变显示"无硬件层约束
- 因此"瞬时显示"是软件设计层的**默认选择**，而非硬件限制

**理论参考**：
- 视觉系统对"瞬时呈现"的注意捕获更强（Yantis & Hillstrom, 1994），但伴随更高的"惊吓式反应"风险（Kim 2018 报告 BRAKE 文本在 5.0 s 远距条件下导致峰值减速度 +34.46%）
- 渐变显示（fade-in 200–500 ms）可降低惊吓但延长完整呈现时间
- **HUD 阶段未量化的设计空白将在 AR-HUD 阶段被部分填补**（共形动画与运动跟随；详见 W6）

### 2.5 Duration 边界的理论锚点（4 篇经典理论）

#### 2.5.1 Duration 下界：Posner (1980) 注意定向最低时间

> Posner, M. I. (1980). Orienting of attention. *Quarterly Journal of Experimental Psychology*, *32*(1), 3–25.

**核心结论**：视觉刺激出现到注意定向稳定建立需 **150–300 ms**；从注意定向到信息提取需另 **300–500 ms**。

**对 Duration 下界的约束**：警告必须至少持续 **500 ms** 才能保证驾驶员完成"注意定向 + 信息提取"两阶段。若 Duration < 0.5 s，则可能在驾驶员尚未完成注意定向之前即消失——这是"过短 Duration"的人因下界。

#### 2.5.2 Duration 上界：Sokolov (1963) 神经习惯化

> Sokolov, E. N. (1963). *Perception and the conditioned reflex*. Pergamon Press.

**核心结论**：反复呈现的相同刺激会经历神经习惯化（neural habituation），匹配-不匹配（matching-mismatch）模型预测注意捕获能力随时间衰减。

**对 Duration 上界的约束**：长时间持续的警告（> 10 s）可能反而降低有效性。Ma (2021) 的紧急 10–15 s 上限可能已逼近该约束。

#### 2.5.3 Duration 上界：Bliss (2003) 虚假警报疲劳

> Bliss, J. P. (2003). Investigation of alarm-related accidents and incidents in aviation. *International Journal of Aviation Psychology*, *13*(3), 249–268.

**核心结论**：当系统的虚警率超过 30% 时，驾驶员对警告的信任度与响应速度显著下降。

**对 Duration 上界的约束**：长 Duration（且后续虚警）累积效应导致信任崩溃。**对 PCW 系统而言，Duration > 5 s 可能加速信任校准失败**。

#### 2.5.4 Duration 与多通道协同：Wickens (2002, 2008) 多资源理论

> Wickens, C. D. (2002, 2008). 多资源理论核心论文。

**核心结论**：视觉-空间通道在 TTC 较短情境下负载迅速饱和；增加额外视觉刺激（如 AR-HUD 警告图标）可能产生认知干扰。

**对 Duration 设计的约束**：单通道视觉警告的 Duration 需保留"驾驶员视线回到道路"的窗口；推荐 Duration ≤ 3 s（即驾驶员单次注视 HUD 不超过 2 s + 一次眼跳缓冲）。

---

## 3. HUD 子集三大空白维度细分表（W3 核心产出）

### 3.1 Duration 维度细分表

| idx | 第一作者 (年) | Duration 明确数值 | 隐含模式 | 上下界理论支撑 |
|---|---|---|---|---|
| 14 | Lübbe (2017) | 1.8 s（与 TTC 同步） | 触发-同步固定 | 介于 Posner 0.5 s 与 Bliss 5 s 之间 |
| 27 | Ma (2021) | **3 s / 10–15 s** | 双段式 | 3 s 符合 Wickens 通道负载；10–15 s 接近 Sokolov 习惯化 |
| 05 | Yoon (2014) | 未报告 | 至危险解除（推测） | – |
| 12 | Zhang/边扬 (2024) | 未报告 | 至危险解除（推测） | – |
| 15 | Winkler (2015) | 未报告 | 至危险解除 | – |
| 16 | Kazazi (2015) | 未报告 | 至危险解除 | – |
| 28 | Doshi (2008) | 未量化（动态） | DAD 动态调节 | – |
| 30 | Frémont (2019) | 未量化（动态） | 自适应触发后持续 | – |
| 11/19/31/32/35/37/38 | 综述 / 工程系统 | 未涉及 | – | – |

**HUD 子集 Duration 报告率**：明确量化 1/14 = **7%**，隐含"至危险解除"6/14 = 43%，未涉及 7/14 = 50%。

### 3.2 闪烁频率维度细分表

| idx | 第一作者 (年) | 闪烁频率 | 替代设计 | 理论合理范围 |
|---|---|---|---|---|
| 28 | Doshi (2008) | 未量化 | DAD 亮度 / 透明度动态调节 | 2–4 Hz |
| 14 | Lübbe (2017) | 未涉及 | 静态显示 + 触觉脉冲 | – |
| 30 | Frémont (2019) | 未涉及 | 自适应触发（不闪烁） | – |
| 其余 11 篇 | – | 未涉及 | 静态持续显示 | – |

**HUD 子集闪烁频率报告率**：0/14 = **0%**。

### 3.3 onset-offset 动画过渡维度细分表

| idx | 第一作者 (年) | 过渡设计 | 实际类型 | 理论参考 |
|---|---|---|---|---|
| 28 | Doshi (2008) | 质性提及"dynamic display" | 未量化 | Yantis & Hillstrom 注意捕获 |
| 其余 13 篇 | – | 默认瞬时 | 瞬时呈现 + 瞬时消失 | – |

**HUD 子集 onset-offset 报告率**：0/14 = **0%**（仅 Doshi 1 篇质性提及）。

---

## 4. 三维度空白严重程度排序

综合 §3 三张细分表，按"研究空白严重程度 × 本研究填补优势"两维度排序：

| 维度 | 量化报告率 | 严重程度 | 填补优势 | 本研究覆盖建议 |
|---|---|---|---|---|
| 持续时长 Duration | 7% | **最高** | 已有 1 篇孤证（Ma 2021）作为对照锚点 | ⭐⭐⭐ RQ1 核心 |
| 升级时序 Inter-level Interval | 7%（W2 已分析） | **最高** | 已有 1 篇孤证（Lübbe 0.7 s）作为对照锚点 | ⭐⭐⭐ RQ2 核心 |
| onset-offset 动画过渡 | 0% | 极高 | 完全零起点；理论参考可用 | ⭐ 可纳入 RQ1 实验的附属变量 |
| 闪烁频率 | 0% | 极高 | 完全零起点 + 硬件 / 伦理风险 | 暂不纳入；列为博士延伸 |

**结论**：本硕士论文的核心实证贡献应集中在 **Duration 与 Inter-level Interval 两个 "7% 孤证维度"**——这两个维度既有研究空白严重性，又有现有数据作为对照锚点，可形成"基于已有孤证 → 系统对照实验"的清晰研究链。

---

## 5. 本周结论

1. **HUD 阶段 Duration 维度仅有 1 篇明确量化（Ma 2021 的 3 s + 10–15 s），其余 13 篇均为"至危险解除"或未涉及**。Ma 自己亦承认 3 s 数值是工程经验值，对照实验是 open question。

2. **Duration 的理论上下界已明确**：
   - 下界 ≥ 0.5 s（Posner 注意定向 + 信息提取）
   - 上界 ≤ 5–10 s（Sokolov 习惯化 + Bliss 信任崩溃）
   - 工程推荐范围：1 s / 2 s / 3 s / "至危险解除"四档对照

3. **闪烁频率与 onset-offset 动画过渡在 HUD 阶段完全空白**（0/14）。前者涉及伦理风险，建议作为博士阶段延伸；后者可纳入 RQ1 实验的附属变量。

4. **本硕士论文 RQ1 的设计依据完整确立**：
   - 实验自变量 1：Duration 四档（1 s / 2 s / 3 s / 至危险解除）
   - 实验自变量 2：车速二档（40 km/h / 60 km/h）
   - 设计：3×2 混合（被试间 Duration × 被试内车速）或 4×2 混合
   - 预期 H1：3 s 或"至危险解除"反应时持平，NASA-TLX 后者更低
   - 预期 H2：1 s 在 40 km/h 足够，60 km/h 显著恶化反应

5. **W3 是 HUD 阶段（W1–W3）的收束周**：W4 起转入 AR-HUD 子集，重点考察共形能力如何改变时间维度。

---

## 6. 下周（W4）计划

**主题**：AR-HUD 时间元素检索 + 共形（Contact-Analog）概念引入

**具体任务**：
1. 完成 AR-HUD 子集 26 篇文献的检索情况补充表（W1 已统计总量，W4 细分到 AR-HUD 子集）
2. 引入"共形（Contact-Analog）"核心概念（Tönnis et al., 2007）及其对时间维度的影响
3. 按显示模式分类：行人锁定 / 路面锁定 / 世界锁定（W8 详细空间表的预热）
4. 提取 AR-HUD 子集 26 篇在时间 5 维上的报告情况（对照 W1 HUD 子集的统计）
5. 评述 AR-HUD 阶段相较 HUD 阶段在时间设计上的演进方向

**预期产出**：W04_AR-HUD时间元素检索.md（含 AR-HUD 子集 26 篇分类 + 共形概念引入 + 时间 5 维报告率对照）

---

## 7. 本周引用 References

Bliss, J. P. (2003). Investigation of alarm-related accidents and incidents in aviation. *International Journal of Aviation Psychology*, *13*(3), 249–268. https://doi.org/10.1207/S15327108IJAP1303_04

Doshi, A., Cheng, S. Y., & Trivedi, M. M. (2008). A novel active heads-up display for driver assistance. *IEEE Transactions on Systems, Man, and Cybernetics, Part B (Cybernetics)*, *38*(1), 85–93. https://doi.org/10.1109/tsmcb.2008.923527

Edworthy, J., Loxley, S., & Dennis, I. (1991). Improving auditory warning design: Relationship between warning sound parameters and perceived urgency. *Human Factors*, *33*(2), 205–231. https://doi.org/10.1177/001872089103300206

Frémont, V., Phan, M.-T., & Thouvenin, I. (2019). Adaptive visual assistance system for enhancing the driver awareness of pedestrians. *International Journal of Human-Computer Interaction*, *36*(9), 856–869. https://doi.org/10.1080/10447318.2019.1698220

Kim, H., Gabbard, J. L., Anon, A. M., & Misu, T. (2018). Driver behavior and performance with augmented reality pedestrian collision warning: An outdoor user study. *IEEE Transactions on Visualization and Computer Graphics*, *24*(4), 1515–1524. https://doi.org/10.1109/tvcg.2018.2793680

Lübbe, N. (2017). Brake reactions of distracted drivers to pedestrian forward collision warning systems. *Journal of Safety Research*, *61*, 23–32. https://doi.org/10.1016/j.jsr.2017.02.002

Ma, X., Jia, M., Hong, Z., Kwok, A. P. K., & Yan, M. (2021). Does augmented-reality head-up display help? A preliminary study on driving performance through a VR-simulated eye movement analysis. *IEEE Access*, *9*, 129951–129964. https://doi.org/10.1109/access.2021.3112240

Posner, M. I. (1980). Orienting of attention. *Quarterly Journal of Experimental Psychology*, *32*(1), 3–25. https://doi.org/10.1080/00335558008248231

Sokolov, E. N. (1963). *Perception and the conditioned reflex*. Pergamon Press.

Wickens, C. D. (2002). Multiple resources and performance prediction. *Theoretical Issues in Ergonomics Science*, *3*(2), 159–177. https://doi.org/10.1080/14639220210123806

Wickens, C. D. (2008). Multiple resources and mental workload. *Human Factors*, *50*(3), 449–455. https://doi.org/10.1518/001872008X288394

Yantis, S., & Hillstrom, A. P. (1994). Stimulus-driven attentional capture: Evidence from equiluminant visual objects. *Journal of Experimental Psychology: Human Perception and Performance*, *20*(1), 95–107. https://doi.org/10.1037/0096-1523.20.1.95

---

*汇报状态：W3 完成（2026.07.11）*
*下次汇报：W4（2026.07.18），主题 = AR-HUD 时间元素检索 + 共形概念引入*
