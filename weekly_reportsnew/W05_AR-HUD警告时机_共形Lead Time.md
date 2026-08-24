# 第 5 周汇报：AR-HUD 警告时机深化 + Kim (2018) 精读

**汇报周次**：W5（2026.07.19 – 2026.07.25）
**汇报对象**：[导师姓名]
**汇报人**：[学生姓名]

---

## 1. 本周目标

承接 W4 已完成的 AR-HUD 子集分类与共形概念引入，本周聚焦 AR-HUD 子集**警告时机**维度：

1. 汇总 6 篇明确量化 TTC 阈值的 AR-HUD 研究，形成阈值证据对照表
2. **按 IMRD 范式完整精读 Kim (2018)**——AR-HUD 阶段唯一实车（户外停车场）实证研究，Virtual Shadow 贴合式 AR 警示的奠基性工作
3. 引入 TTMD（Time-to-Minimum-Distance）公式作为二维相交场景的新指标
4. 分析共形警告在时间维度的压缩效应与反例
5. 提炼本周 5 条共识

---

## 2. AR-HUD 子集警告时机的 6 篇证据聚合

W4 已识别 AR-HUD 子集 26 篇中 15 篇（58%）明确量化警告时机。本周将其中 6 篇具备完整 TTC 参数的核心研究汇总。**主流从 HUD 阶段的单阈值演进到 AR-HUD 阶段的双阈值和复合公式**。

### 2.1 六篇 TTC 量化研究要览

| 文献 | 锁定模式 | 车速 | TTC 触发值 | 核心结果 |
|---|---|---|---|---|
| Kim (2018) Near | Pedestrian-conformal | 24 km/h | **TTC = 2.5 s**（约 16.7 m） | Virtual Shadow 减速度调节良好 |
| Kim (2018) Far | Pedestrian-conformal | 24 km/h | **TTC = 5.0 s**（约 33.5 m） | BRAKE 文本 +34.46% 过度减速 |
| Phan (2016) | Pedestrian-conformal | 50 km/h | **min(TTC = 2 s, d = 16.6 m)** | TTC 觉察 3 s → 4.5 s |
| Wang ARive (2025) | Road-conformal | 50 km/h | **TTMD ≤ 5 s + d < 5 m** / 二级切换 TTMD = 2 s | 让行成功率 p < .001 |
| Wu (2024) | Pedestrian-conformal | 60 km/h | **TTC < 3 s** | TTFF BW=617 ms（vs BD=2562 ms） |
| Huo & Alla (2025) | Pedestrian-conformal | 50 km/h | **TTC = 2.5 s**（约 34.7 m） | 危险感知 0.52 s（夜 0.58 s） |
| Chen (2024) | Pedestrian-conformal | 60 km/h | **THW ≤ 3 s** | 行人场景 BB 比 CA 更优 |

### 2.2 TTC 演化的共识

对比 W2 HUD 子集的 TTC 阈值（临界 1.8 s / 提示 2.5 s / 中国冗余 6.0 s，单值阈值为主），AR-HUD 阶段呈现两个演化特征：

1. **触发语言多元化**：从单值 TTC 演进到双阈值（Kim 2.5/5.0 s）、复合公式（Phan TTC + 距离）、二维几何指标（Wang TTMD）与稳态跟驰指标（Chen THW）
2. **临界级 TTC 稳定在 2.0–2.5 s**（与 HUD 一致，受 PIEV 物理下界约束），**提示级从 HUD 的 5.0 s 扩展到 TTMD 5 s 或 THW 3 s**

---

## 3. Kim (2018) 精读汇报（IMRD 完整展开）

本节按学术论文的**引言—方法—结果—讨论**四段范式完整汇报 Kim (2018)——AR-HUD 阶段唯一实车（户外停车场）实证研究，Virtual Shadow 贴合式 AR 警示的奠基性工作。

### 3.1 Introduction（引言）

#### 3.1.1 研究背景

- **NHTSA 2015 报告**：2013 年美国 4,735 名行人死亡、约 71,000 名受伤，行人死亡占交通死亡 14%（较 2007 年的 11% 上升）
- 事故贡献因素分析：驾驶员因**低可见度（15.5%）**或**行人意外出现（47%）**而未能及时识别行人
- **现有 PCW 系统的局限**：只以声音报警 + 简单视觉符号告知"存在威胁"，缺乏空间方位信息，驾驶员仍需自行定位与判断行人运动，反而增加认知负担与反应时延

#### 3.1.2 研究缺口

Kim 明确识别的**两个研究缺口**：

1. **AR 贴合式（conformal）图形与传统警示的实证对比未充分**——特别是量化"引导驾驶员注视真实行人 + 改善刹车"两个效应
2. **"单视场（monoscopic）vs 体积式（volumetric）AR-HUD"在驾驶任务中孰优孰劣尚无实证结论**——这是量产 AR-HUD 走向单焦平面还是多焦平面的关键决策问题

#### 3.1.3 两个核心命题

- **命题 1**：与"BRAKE 文本"型传统预警相比，基于"虚拟阴影（Virtual Shadow）"的贴合式 AR 图形能更有效地引导驾驶员注视真实行人，并改善刹车行为
- **命题 2**：借助真实道路环境固有的丰富深度线索时，体积式 HUD 相对单视场 HUD 在刹车性能上不会显著更好

**命题 2 的特殊意义**：这是一个"节俭原则"的命题——如果单视场对量产 AR-HUD 就够了，可大幅降低硬件成本。

### 3.2 Method（方法）

#### 3.2.1 被试

- 初招 N = 16，剔除 2 名完全忽略 AR 警示者，**最终 14 名用于分析**
- 眼动数据另剔除 2 名（因反光），**最终 12 名做眼动分析**
- 年龄 31–55 岁，**平均驾龄 23 年**（中老年经验丰富样本）
- **新手数据缺失是明显局限**——这正是 W9 Huo & Alla 补上的空白

#### 3.2.2 实验设计

- **类型**：组内重复测量（2 × 4）
- **自变量 1（视觉预警，4 水平）**：无警示 / BRAKE 文本 / 单视场虚拟阴影 / 体积式虚拟阴影
- **自变量 2（行人距离，2 水平）**：**Near TTC = 2.5 s（约 16.7 m@15 mph）** vs **Far TTC = 5.0 s（约 33.5 m@15 mph）**
- **顺序拉丁方逆平衡**，插入随机的"无事件"试次以掩盖预期

#### 3.2.3 设备与刺激规格

**实车与传感器**：
- 改装 2009 Honda Odyssey
- **OxTS RT4003 RTK GPS**（精度 < 20 cm）用于精确测量车-人几何
- 两台 GoPro Hero3+ 记录足部（制动 / 油门）和外景
- **SMI ETG 眼动仪**（30 Hz）

**HUD 原型**：
- **扫掠体积（swept-volume）技术**，焦距 8 m 到光学无穷远
- 与量产单视场 HUD（固定焦距）形成硬件对照

**Virtual Shadow 规格**：
- "**穹顶 + 系绳**"（dome + tether）形态，地面投影
- **绝对直径 1.0 米**，随距离变化视角 **2°–8°**
- 触发方式：**模拟 V2X**——车辆通过预设触发线时通过对讲机指示行人做动作，同时 GPS 自动触发 HUD 警示

#### 3.2.4 场景

- **150 米 × 100 米三面围合停车场**
- **限速 15 mph（约 24 km/h）单向车道**
- **场景选择限制**：受限于封闭场地限速，无法测试更高速度

### 3.3 Results（结果）

Kim 的因变量分四层——继承 W4 Phan 的三层框架并扩展。**按 感知 / 决策 / 操控 / 结果 四层解读**。

#### 3.3.1 发现 1：命题 2 被验证——"节俭原则"成立

**单视场 vs 体积式在所有 6 个定量指标上均无显著差异**（p 均 > .05）。

**实际意义**：这与体积显示在静态深度判断中优于单视场的传统认知相反。Kim 解释——**"在动态深度环境 + 行动空间 + 富深度线索的真实道路场景中，单视场的透视深度线索已足以支持高质量的深度知觉"**。

**对量产 AR-HUD 决策的直接意义**：不必强求多焦平面，单视场硬件已足以支持行为改善。

#### 3.3.2 发现 2：行为模式差异——AR 让"看-判断-刹车"顺序恢复正常

**因变量说明**：Kim 定义了三种驾驶员行为模式：
- **Pattern A**：看警示 → 看行人 → 抬油门 → 刹车（信息驱动的完整决策）
- **Pattern B**：看警示 → 抬油门 → 看行人 → 刹车（部分信息驱动）
- **Pattern C**：看警示 → 抬油门 → 刹车 → 看行人（**"盲刹"模式**）

**结果**（Durbin χ²(3) = 34.87, p < 0.001）：
- **BRAKE 文本条件下 100% 驾驶员是 Pattern C**（盲刹）
- **体积式与单视场条件下 76–77% 是 Pattern A/B**（正常顺序）

**实际意义**：**Pattern 分布直接揭示"警告呈现风格"对驾驶员认知加工顺序的操控作用**——BRAKE 文本让驾驶员绕过"识别 + 决策"直接进入"执行"，AR 共形让"目视锚定 → 认知决策 → 制动执行"顺序恢复正常。

#### 3.3.3 发现 3：注视行人距离——远距条件揭示 BRAKE 的反噬效应

**因变量**：驾驶员首次注视到真实行人时距离行人多远。数值越大意味着"越早看到行人"。

**远距条件（Far, TTC = 5.0 s）**：
- 单视场 Virtual Shadow：**减 19.31%（-1.86 m）**——更晚注视？
- 体积式 Virtual Shadow：**减 25.21%（-2.43 m）**——更晚注视？
- BRAKE 文本：**+24.02%（+2.32 m）**——延后注视！

**因变量的正确解读**：Kim 报告的是"驾驶员首次注视行人时的车-人距离"。AR 条件下距离缩短（-19% / -25%）意味着驾驶员"离行人更近才注视"——但这并非负面，因为 AR 条件下驾驶员在**警示出现瞬间就已通过 AR 图形获取行人空间信息**，无需长距离扫视寻找。

**BRAKE 条件下 +24% 才是关键警示**——驾驶员先专注在"BRAKE"文字上，反而**延后了对真实行人的锚定**（先看文字 → 再找目标）。

#### 3.3.4 发现 4：踩刹车距离提前——AR 让制动启动更早

AR 让驾驶员更早开始踩刹车。
- **近距 Near（TTC = 2.5 s）**：AR vs 无警示 → 制动距离 **-32%**（更早刹车）
- **远距 Far（TTC = 5.0 s）**：AR vs 无警示 → 制动距离 **-30% 到 -39%**

**实际意义**：AR 共形警告让制动决策提前——为后续减速留出更多时间，减少最大减速度。

#### 3.3.5 发现 5：峰值减速度——BRAKE + Far 的惊吓式过度反应（最关键的反直觉发现）

- **近距条件（Near）**：所有警示都降低峰减速度（预警帮助）
- **远距条件（Far）**：**BRAKE 反而把峰值减速度提高 34.46%（+0.08 g）**——**驾驶员在不必急刹的远距场景被"通用文本警告"误导成了急刹**（增加追尾风险）
- **远距条件下 Virtual Shadow**：单视场与体积式均做出**平滑制动**，峰减速度接近基线

**因变量的实际意义**：**峰值减速度反映"制动动作的暴烈程度"——BRAKE 文本触发的是"惊吓反应"而不是"理性制动"**。

#### 3.3.6 结果小结

| 因变量层 | 关键指标 | 实际反映的驾驶员认知 |
|---|---|---|
| 感知层 | 首次注视行人距离 | 目视锚定的时机与顺序 |
| 决策层 | Pattern A/B/C 分布 | "看-判断-刹"认知加工顺序是否被扭曲 |
| 操控层 | 制动启动距离 | 决策向执行的转换效率 |
| 结果层 | 峰值减速度 | 制动动作的暴烈程度（是否惊吓） |

**一句话总结**：**AR 贴合式让"看行人 → 判断 → 刹车"顺序正常；BRAKE 文本在远距场景引发惊吓式过度反应**——这是本文最有临床意义的发现。

### 3.4 Discussion（讨论）

#### 3.4.1 Kim 的核心设计原则

**"贴合式图形应引导（guide）而非替代（replace）驾驶员对真实物体的注视"**。

BRAKE 文本是**替代性的**——它告诉驾驶员"该刹车了"却不告诉"因为哪个行人"，把认知任务从"识别 + 决策 + 执行"简化为"看到文字 + 执行"——**这解释了 BRAKE 在远距场景的过度反应**：驾驶员绕过了"识别"和"决策"直接进入"执行"，而"执行"的强度是由"看到强命令性文字"驱动的（惊吓式）。

#### 3.4.2 Kim 自陈的四个局限

1. **15 mph 停车场场景与真实道路差距大**——外推到城市道路（30–60 km/h）需谨慎
2. **样本平均驾龄 23 年偏老、新手数据缺失**——这正是 W9 Huo & Alla 补上的空白
3. **SAGAT（暂停式情境意识问询）不适合野外路测**——只能用 Post-hoc 问卷替代
4. **未探讨多目标场景与天气**——单目标 + 晴天条件

#### 3.4.3 对本研究（HUD/AR-HUD 时间元素设计规范）的三个具体启示

**启示 1（继承）：Near/Far 双阈值 + SDT 双判据框架**

Kim 的 **TTC 2.5/5.0 s 双阈值 + SDT 双判据**（Near 优化 β 强警告紧迫、Far 优化 d′ 发现潜在危险）直接继承 W1 Lübbe 的 1.8/2.5 s Imminent/Cautionary 框架，形成"HUD-AR-HUD"演进链。**建议**：RQ2 应把双阈值作为主要的时序设计参数。

**启示 2（警示）：警告文本强度 × Lead Time 匹配是设计陷阱**

**BRAKE 文本 + Far 条件 = 惊吓式过度反应（+34.46%）**——**警告文本的语义强度必须与 Lead Time 匹配**。远距条件下（TTC 5s）应用软性图形（如 Virtual Shadow）而非强命令文本；近距条件下（TTC 2.5s）文本才合适。**建议**：RQ1 实验设计应严格控制"警告呈现风格"这个副变量避免混淆——只用单一图形（如包围框），不引入 BRAKE 文本。

**启示 3（扩展）：15 mph 停车场外推有限，必须扩展到 40-60 km/h**

Kim 的实车方法学难以扩展到硕士规模（成本、伦理），且 15 mph 只覆盖低速。**建议**：本研究采用**高保真模拟器 + 40 与 60 km/h 二档车速**——既保证生态效度，又能同时检验 Kim 双阈值在中高速场景下的可迁移性。

---

## 4. 共形 vs 屏幕固定的"时间-空间耦合"效应

W4 已通过 Phan 引入共形概念的空间原理，本节聚焦时间维度的耦合效应。

### 4.1 共形警告在时间维度上的"压缩"效应

| 因变量 | 屏幕固定 | 行人锁定共形 | 效应量 | 文献 |
|---|---|---|---|---|
| TTFF（首次注视时间） | 2562 ms（BD） | **617 ms**（BW） | **快 4.15 倍** | Wu 2024 |
| 制动反应时（行人场景） | ~1.45 s | ~1.07 s | 快 **26%** | Chen 2024 |
| 减速度峰值 | +34.46%（BRAKE + Far） | 适宜（Virtual Shadow） | 减少惊吓 | Kim 2018 |

**机制假设**：共形警告将"信息呈现的物理坐标"与"实际危险的物理坐标"对齐，**减少了驾驶员的坐标系转换认知负担**——故 TTFF 与反应时同步压缩。

### 4.2 共形警告的反例：Kim & Gabbard (2019) 注意隧道

> Kim, H., & Gabbard, J. L. (2019). Assessing distraction potential of augmented reality head-up displays for vehicle drivers. *Human Factors*, *64*(5), 852–865.

**核心反例**：贴地共形 AR 箭头并不必然优于屏幕固定 2D 箭头——共形条件下 **mental demand 增加 23.7%**（vs 屏幕固定 +11.7%）、effort 更高、**HUD-graphic 注视时长最长 3.33 s vs 屏幕固定 1.17 s**。

**对本研究的意义**：**共形优势是有条件的**——当共形警告本身的视觉复杂度过高时，可能引发**注意隧道（attentional tunneling）**。RQ1 实验应控制共形警告的视觉复杂度（如仅使用简化包围框），避免此 confound。

---

## 5. AR-HUD TTC 设计的三个新增挑战

相较 HUD 阶段的"固定 TTC 阈值"，AR-HUD 时间设计面临三个 HUD 阶段不需考虑的新维度：

### 5.1 挑战 1：动态目标跟随的延迟容忍

共形警告要求 HUD 系统实时跟踪行人位置。跟随延迟（latency）若超过 100 ms 即产生视觉漂移。**这要求 TTC 阈值的判定必须考虑硬件层延迟**：

$$\text{实际 Lead Time} = \text{TTC 触发阈值} - \text{系统延迟（感知 + 处理 + 显示）}$$

例如 Wang ARive (2025) 报告系统总延迟 **~80 ms**（HoloLens 2 端到端），故实际 Lead Time = 2 s − 0.08 s = 1.92 s——对临界级的物理裕量产生 4% 压缩。

### 5.2 挑战 2：深度感知线索的双刃剑

AR-HUD 提供与外部物体一致的双目视差与运动视差（vergence-accommodation 一致性），但这一优势在 **TTC 短（< 2 s）情境下**可能被认知负荷反噬：
- TTC 短时，驾驶员需快速判断"距离 + 方向 + 速度"
- 深度感知线索增加了第 4 个判断维度（"虚拟图形 vs 真实物体的相对位置"）
- 总认知负荷可能超出 System 1 的容量上限（Kahneman 1.2 s 上限）

### 5.3 挑战 3：多焦平面 vs 单焦平面的注视切换

**Kim (2018) 证明单视场 = 体积式**在真实道路富深度线索场景下无差异——这一"节俭原则"结论减轻了本研究方法学负担：**RQ1 使用单焦平面模拟已足够**。但仍需在讨论中说明：
- 单焦平面：警告焦距固定 ≈ 2.3 m，与外部行人焦距（10-30 m）存在调节冲突
- 多焦平面：警告焦距与行人焦距匹配，调节冲突最小
- 本研究因方法学限制无法对照，仅在 §5 局限性中说明

---

## 6. 本周共识（Weekly Consensus）

本周提炼 5 条核心共识：

1. **AR-HUD 警告时机演进为"双阈值 + 复合公式"**——Kim 2018 TTC 2.5/5.0 双阈值、Phan 2016 TTC + 距离复合、Wang 2025 TTMD 二维公式、Chen 2024 THW；但**核心边界仍受 W2 讨论的 PIEV 物理下界约束**（2.5 s 是 Cautionary 下限）。

2. **Kim (2018) Virtual Shadow 是 AR-HUD 阶段唯一实车实证**——Near/Far 双阈值（2.5/5.0 s）继承 Lübbe 的 Imminent/Cautionary 框架并用 SDT 双判据支撑；**贴合式让驾驶员"看行人 → 判断 → 刹车"顺序恢复正常**（AR 76-77% 是 Pattern A/B，BRAKE 100% 是 Pattern C）。

3. **Kim 揭示"警告文本强度 × Lead Time 匹配"设计陷阱**——**BRAKE 强命令性文本 + Far Lead Time = 惊吓式过度反应（峰值减速度 +34.46%）**；这是 RQ1 设计中必须控制的"警告呈现风格"副变量。

4. **Kim 证明"单视场 = 体积式"节俭原则**——真实道路富深度线索场景下二者无显著差异；**对量产 AR-HUD 决策的直接意义**——不必强求多焦平面，单视场硬件已足以支持行为改善；本研究方法学采用单焦平面模拟得到支撑。

5. **Kim 的 15 mph 停车场场景外推效度有限，样本 23 年驾龄偏老**——**新手 + 高速场景在 AR-HUD 阶段仍是空白**，正对应本研究 RQ3（新手依赖性）与 RQ1（车速二档 40/60 km/h）的设计。

---

## 7. 下周（W6）计划

**主题**：AR-HUD 持续时长（Duration）+ 升级时序专题 + Ma (2024) EID carpet 精读

**具体任务**：
1. **按 IMRD 范式完整精读 Ma (2024) carpet**——AR-HUD 阶段生态界面（EID）设计与"绿-黄-红渐变 + 动态消失"的代表性研究
2. 汇总 AR-HUD 子集 7 篇明确报告 Duration 的研究
3. 多级警告升级时序专题分析（Lübbe 0.7 s 孤证 + Ma 2024 三色渐变 + Chen 2024 多目标分级）
4. 共形动画与运动跟随的时间特性分析（跟随平滑度 / 跟随延迟）
5. 提炼本周 5 条共识

**预期产出**：W06_AR-HUD持续时长_升级时序.md（含 Ma 2024 IMRD 精读）

---

## 8. 本周引用 References

Chen, W., Niu, L., Liu, S., Ma, S., Li, H., & Yang, Z. (2024). Evaluating the effectiveness of contact-analog and bounding box prototypes in augmented reality head-up display warning for Chinese novice drivers. *International Journal of Human-Computer Interaction*. https://doi.org/10.1080/10447318.2024.2327197

Huo, F., & Alla, R. (2025). Differences in drivers' dependence on AR warning information in urban driving environments: The role of driving experience. *Frontiers in Virtual Reality*, *6*, 1638823. https://doi.org/10.3389/frvir.2025.1638823

Kim, H., & Gabbard, J. L. (2019). Assessing distraction potential of augmented reality head-up displays for vehicle drivers. *Human Factors*, *64*(5), 852–865. https://doi.org/10.1177/0018720819844845

Kim, H., Gabbard, J. L., Anon, A. M., & Misu, T. (2018). Driver behavior and performance with augmented reality pedestrian collision warning: An outdoor user study. *IEEE Transactions on Visualization and Computer Graphics*, *24*(4), 1515–1524. https://doi.org/10.1109/tvcg.2018.2793680

National Highway Traffic Safety Administration. (2015). *Traffic safety facts 2013: Pedestrians* (DOT HS 812 124). U.S. Department of Transportation.

Phan, M. T., Thouvenin, I., & Frémont, V. (2016). Enhancing the driver awareness of pedestrian using augmented reality cues. In *2016 IEEE 19th International Conference on Intelligent Transportation Systems (ITSC)* (pp. 1298–1304). IEEE. https://doi.org/10.1109/itsc.2016.7795724

Vogel, K. (2003). A comparison of headway and time to collision as safety indicators. *Accident Analysis & Prevention*, *35*(3), 427–433. https://doi.org/10.1016/S0001-4575(02)00022-2

Wang, C., Chu, D., & Martens, M. (2025). ARive: Assisting drivers with in-car augmented reality for risk zone detection. *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies*, *9*(1), Article 22. https://doi.org/10.1145/3712270

Wu, Z., Liang, Y., Liu, G., & Ai, X. (2024). Comparative analysis of AR-HUDs crash warning icon designs: An eye-tracking study using 360° panoramic driving simulation. *Sustainability*, *16*(21), 9167. https://doi.org/10.3390/su16219167

---

*汇报状态：W5 完成（2026.07.25），继续沿用"每周一篇重点精读 + IMRD 完整展开 + 5 条本周共识"结构*
*下次汇报：W6（2026.08.01），主题 = AR-HUD 持续时长 + 升级时序 + Ma (2024) IMRD 精读*
