# 第 5 周汇报：AR-HUD 警告时机与共形 Lead Time 深化

**汇报周次**：W5（2026.07.19 – 2026.07.25）
**汇报对象**：[导师姓名]
**汇报人**：[学生姓名]

---

## 1. 本周目标

承接 W4 已完成的 AR-HUD 子集分类与共形概念引入，本周深化 AR-HUD 子集中**警告时机**维度：

1. 详细分析 AR-HUD 15 篇明确量化 TTC 的研究（Kim 2018 / Phan 2016 / Wu 2024 / Wang 2025 / Huo & Alla 2025 等）
2. 引入 TTMD（Time-to-Maximum-Deceleration / Min-Distance）公式作为二维相交场景的新指标
3. 比较 AR-HUD 中"共形 vs 屏幕固定"的 TTC 阈值与绩效差异
4. 形成 AR-HUD TTC 阈值对照表 + 共形优势矩阵
5. 评述 AR-HUD TTC 设计的新增挑战（动态目标跟随、深度感知线索、多焦平面）

---

## 2. AR-HUD 子集警告时机深化分析

### 2.1 Kim et al. (2018, idx 01) — TTC 2.5 / 5.0 s 双距离对照（黄金标准研究）

> Kim, H., Gabbard, J. L., Anon, A. M., & Misu, T. (2018). Driver behavior and performance with augmented reality pedestrian collision warning: An outdoor user study. *IEEE TVCG*, *24*(4), 1515–1524.

**实验设计**：
- 环境：户外停车场实车实验（极少数真实道路 AR-HUD 研究之一）
- 测试车辆：经改装的 2009 年 Honda Odyssey，搭载体积式 HUD（焦距 8 m – 光学无穷远，~17° 圆形视场）
- 被试：N = 27
- 测试车速：15 mph ≈ 24 km/h
- 警告类型：3 种（无警告基线 / "BRAKE" 文本警告 / Virtual Shadow 共形图形）
- 触发距离：Near = TTC 2.5 s（约 16.7 m）vs Far = TTC 5.0 s（约 33.5 m）

**核心结果**：
- 传统"BRAKE"文本警告 + Far 条件 → 峰值减速度比基线**高 34.46%**（过度反应）
- Virtual Shadow 共形图形 + Near/Far 均表现适宜减速度调节
- 作者解释：**共形图形提供距离感知线索，使驾驶员能基于真实距离调节制动强度**

**对本研究的意义**：
- Kim (2018) 是**双阈值方案**的实证基础：5.0 s 优化灵敏度 d′ + 2.5 s 优化判据 β（信号检测论 SDT 框架）
- 同时证明"非共形警告 + 长 Lead Time"可能产生**惊吓式过度反应**——是共形 AR-HUD 优势的反面证据

### 2.2 Phan et al. (2016, idx 02) — TTC + 距离复合阈值

> Phan, M. T., Thouvenin, I., & Frémont, V. (2016). Enhancing the driver awareness of pedestrian using augmented reality cues. In *IEEE ITSC 2016* (pp. 1298–1304).

**实验设计**：
- 固定基座驾驶模拟器
- 复合触发阈值：**$t_{WP} = \min(t(TTC = 2 \text{ s}), t(d = 16.6 \text{ m}))$**
- 物理意义：低速时距离 16.6 m 先达到，高速时 TTC = 2 s 先达到，避免单一 TTC 阈值在高速下触发过晚

**核心结果**：
- AR cues 使行人觉察时刻的 TTC 从 3 s 延后至 **4.5 s**（即驾驶员更早感知到行人）
- 紧急制动次数从 72 次降至 11 次

**对本研究的意义**：
- Phan 复合公式提示 **TTC 阈值应是车速函数**——这是本研究 RQ1 × 车速交互的方法学借鉴

### 2.3 Wang ARive (2025, idx 20) — TTMD 二维相交场景

> Wang, C., Chu, D., & Martens, M. (2025). ARive: Assisting drivers with in-car augmented reality for risk zone detection. *PACM IMWUT*, *9*(1), Article 22.

**实验设计**：
- HoloLens 2 AR-HMD（不是 AR-HUD，但共形原理相同）
- 二维相交场景（如交叉口让行）
- TTMD 公式：$t_{min} = -\frac{\Delta p \cdot \Delta v}{\Delta v \cdot \Delta v}$（其中 Δp = 相对位置矢量, Δv = 相对速度矢量）
- 激活条件：$t_{min} \le 5 \text{ s}$ 且最小距离 $d_{min} < 5 \text{ m}$
- 级别切换：$t_{min} = 2$ s 从"预警"升级到"临界"

**核心结果**：
- 红地毯（Red Carpet）AR 图形在让行场景中的成功率 **p < .001 显著优于基线**
- 16/21 被试主观偏好该方案
- 与 Kim (2018) 双阈值的差异：Wang 用 5 s + 2 s（TTMD 几何意义）vs Kim 用 5.0 s + 2.5 s（纵向 TTC）

**TTMD vs 纵向 TTC 的关键差异**：
- 纵向 TTC 假设两物体沿同一直线运动，对二维相交（如交叉口横穿）失效
- TTMD 在二维空间下仍可给出有限的"最接近时刻"
- **本研究 RQ1 实验应同时考察纵向场景（TTC）与二维相交场景（TTMD）两种触发逻辑**

### 2.4 Wu et al. (2024, idx 08) — TTC < 3 s 触发，动态跟随图标

> Wu, Z., Liang, Y., Liu, G., & Ai, X. (2024). Comparative analysis of AR-HUDs crash warning icon designs: An eye-tracking study using 360° panoramic driving simulation. *Sustainability*, *16*(21), 9167.

**实验设计**：
- 360° 全景视频驾驶模拟（HTC VIVE Pro Eye + Tobii Pro Lab）
- 测试车速：60 km/h 恒速
- 行人横穿：1.5 m/s 启动
- 触发条件：TTC < 3 s

**核心结果**：
- 动态跟随型图标 BW（行人锁定）vs 固定位置 BD / BR 对比
- TTFF：BW = 616.67 ms vs BD = 2562.58 ms vs BR = 2729.92 ms（**BW 短 4 倍以上**）
- 注视次数：BW 显著少
- 主观可用性：BW 最高

**对本研究的意义**：
- TTC < 3 s 是 AR-HUD 阶段一个新阈值（介于 HUD 临界级 1.8–2.5 s 与提示级 5.0 s 之间）
- TTFF 是 **AR-HUD 时间设计的新核心因变量**——能直接反映"警告吸引注意的速度"
- 行人锁定的 TTFF 优势提示：**共形警告本身就是一种"时间压缩"机制**（不需要 Duration 长就能完成信息传递）

### 2.5 Huo & Alla (2025, idx 21) — TTC = 2.5 s + 经验差异

> Huo, F., & Alla, R. (2025). Differences in drivers' dependence on AR warning information in urban driving environments: The role of driving experience. *Frontiers in Virtual Reality*, *6*, 1638823.

**实验设计**：
- 城市道路驾驶模拟，N = 64（32 新手 + 32 熟练）
- 测试车速：50 km/h
- 统一触发 TTC = 2.5 s（对应约 34.72 m）
- 光照条件：白天 vs 夜间
- AR 警告：闪烁（flashing）方式持续呈现

**核心结果**：
- 白天危险感知时间：AR 0.52 s vs 无 AR 1.20 s（p < .01）
- 夜间危险感知时间：AR 0.58 s vs 无 AR 1.89 s（p < .01）
- **关键发现**：当 AR 系统出现随机故障时，新手表现严重退化（"依赖性"陷阱）；熟练驾驶员则保持稳定

**对本研究的意义**：
- Huo & Alla 提供了 AR-HUD 时间设计的**经验维度调节效应**实证——这是本研究 RQ3 的最直接先例
- 闪烁作为持续 Duration 的替代设计：避免 Duration 过长引起习惯化，又通过闪烁保持注意捕获

### 2.6 Chen et al. (2024 contact-analog, idx 07) — THW ≤ 3 s

> Chen, W., Niu, L., Liu, S., Ma, S., Li, H., & Yang, Z. (2024). Evaluating the effectiveness of contact-analog and bounding box prototypes in augmented reality head-up display warning for Chinese novice drivers. *IJHCI*.

**实验设计**：
- N = 48 中国新手驾驶员
- 测试车速：60 km/h
- 触发条件：**THW（车头时距）≤ 3 s**（与瑞典国家道路管理局 Vogel 2003 推荐一致）
- 警告对比：Contact-Analog 共形 vs Bounding Box

**核心结果**：
- 追尾场景：Contact-Analog 反应更快
- 行人场景：**Bounding Box 反应时更短**
- 与交通密度无关

**对本研究的意义**：
- THW（车头时距）vs TTC（碰撞时间）的差异：THW 不要求相对速度差，适用于稳态跟驰场景
- 中国新手数据：本研究 RQ3 中国驾驶员组的对照锚点
- Contact-Analog vs Bounding Box 反直觉结果（行人场景 Bounding Box 更优）提示**共形警告的优势是场景依赖的**

---

## 3. AR-HUD 子集 TTC 阈值证据对照表（W5 核心产出）

下表汇总 AR-HUD 子集中 8 篇明确量化 TTC 的研究：

| 文献 | 锁定模式 | 实验车速 | TTC 触发值 | 等价 50 km/h 距离 | 核心结果（反应时 / 制动） |
|---|---|---|---|---|---|
| Kim (2018) Near | Pedestrian-conformal | 24 km/h | **2.5 s** | 16.7 m | Virtual Shadow 减速度调节良好 |
| Kim (2018) Far | Pedestrian-conformal | 24 km/h | **5.0 s** | 33.5 m | "BRAKE" 文本 +34.46% 过度减速 |
| Phan (2016) | Pedestrian-conformal | 50 km/h | **2 s 或 d=16.6 m** | 16.6 m / 27.8 m | TTC 觉察从 3 s 延后至 4.5 s |
| Wang ARive (2025) L1 | Road-conformal (TTMD) | 50 km/h | **5 s (TTMD)** | – | 让行成功率 p < .001 |
| Wang ARive (2025) L2 | Road-conformal (TTMD) | 50 km/h | **2 s (TTMD)** | – | 临界级颜色加深 |
| Wu (2024) | Pedestrian-conformal | 60 km/h | **< 3 s (TTC)** | 41.7 m | TTFF BW=617 ms |
| Huo & Alla (2025) | Pedestrian-conformal | 50 km/h | **2.5 s** | 34.7 m | 危险感知 0.52 s（夜 0.58 s） |
| Chen (2024) | Pedestrian-conformal | 60 km/h | **THW ≤ 3 s** | 41.7 m | 行人场景 Bounding Box 更优 |

### 3.1 AR-HUD TTC 阈值的"演化共识"

把 AR-HUD 子集 TTC 值与 HUD 子集（W2 已分析）对照：

| 阶段 | 主流 TTC 范围 | 关键差异 |
|---|---|---|
| HUD 子集（W2） | 临界 1.8 s / 提示 2.5 s / 中国冗余 6.0 s | 单值阈值 |
| AR-HUD 子集（W5） | 临界 2.0–2.5 s / 提示 3.0–5.0 s / 二维场景 TTMD 2/5 s | **双值或复合公式**成为主流 |

**演化要点**：
1. AR-HUD 阶段倾向于**双阈值或复合公式**（Kim 2.5/5.0、Phan TTC+距离、Wang TTMD 双级），而 HUD 阶段多为单值
2. AR-HUD 引入 **THW、TTMD** 等新指标，丰富了"时间触发"的语言
3. **关键共识**：AR-HUD 临界级稳定在 **2.0–2.5 s**（与 HUD 一致），但提示级上限从 HUD 的 5.0 s 扩展到 **TTMD 5 s 或 THW 3 s**

---

## 4. 共形 vs 屏幕固定的"时间-空间耦合"分析

AR-HUD 阶段对"共形（Contact-Analog）vs 屏幕固定（Screen-fixed）"的对照研究丰富。从时间维度看：

### 4.1 共形警告在时间维度上的"压缩"效应

| 因变量 | 屏幕固定（如 BD） | 行人锁定共形（如 BW） | 效应量 |
|---|---|---|---|
| TTFF（首次注视时间） | 2562 ms (Wu 2024 BD) | **617 ms** (Wu 2024 BW) | 共形快 **4.15 倍** |
| 制动反应时（行人场景） | 平均 1.45 s (Chen 2024) | 平均 1.07 s (Chen 2024) | 共形快 **26%** |
| 减速度调节精度 | 过度反应 +34.46% (Kim 2018 BRAKE) | 适宜（Kim 2018 Virtual Shadow） | 共形减少惊吓 |

**机制假设**：共形警告将"信息呈现的物理坐标"与"实际危险的物理坐标"对齐，**减少了驾驶员的"坐标系转换"认知负担**，故 TTFF 与反应时同步压缩。

### 4.2 共形警告的反例：Kim & Gabbard (2019) 注意捕获过强

> Kim, H., & Gabbard, J. L. (2019). Assessing distraction potential of augmented reality head-up displays for vehicle drivers. *Human Factors*, *64*(5), 852–865.

**核心反例**：贴地共形 AR 箭头并不必然优于屏幕固定 2D 箭头——共形条件下 mental demand 增加 **23.7%**（vs 屏幕固定 +11.7%）、effort 更高、HUD-graphic 注视时长更长（最长 3.33 s vs 1.17 s）。

**对本研究的意义**：共形优势是**有条件的**——当共形警告本身的视觉复杂度过高时，可能引发**注意隧道（attentional tunneling）**。本研究 RQ1 实验应控制共形警告的视觉复杂度，避免此 confound。

---

## 5. AR-HUD TTC 设计的新增挑战

相比 HUD 阶段的"固定 TTC 阈值"，AR-HUD 时间设计面临 3 个新挑战：

### 5.1 挑战 1：动态目标跟随的延迟容忍

共形警告要求 HUD 系统实时跟踪行人位置。当行人快速横穿时，跟随延迟（latency）若超过 100 ms 即产生视觉漂移。**这要求 TTC 阈值的判定必须考虑硬件层延迟**：

实际 Lead Time = TTC 触发阈值 − 系统延迟（感知 + 处理 + 显示）

例如 Wang ARive (2025) 报告系统总延迟 **~80 ms**（HoloLens 2 端到端），故实际 Lead Time = 2 s − 0.08 s = 1.92 s——这对临界级的物理裕量产生 4% 压缩。

### 5.2 挑战 2：深度感知线索的双刃剑

AR-HUD 提供与外部物体一致的双目视差与运动视差（vergence-accommodation 一致性），但这一优势在 **TTC 短（< 2 s）情境下**可能被认知负荷反噬：

- TTC 短时，驾驶员需快速判断"距离 + 方向 + 速度"三个维度
- 深度感知线索增加了第 4 个判断维度（"虚拟图形 vs 真实物体的相对位置"）
- 总认知负荷可能超出 System 1 的容量上限（Kahneman 1.2 s 上限）

### 5.3 挑战 3：多焦平面 vs 单焦平面的注视切换

体积式 HUD（如 Kim 2018 的 8 m–光学无穷远焦距调节）vs 单焦平面 AR-HUD（如多数车厂量产产品的固定 2.3 m 焦距）在 **TTC 短时**对驾驶员视觉调节的要求不同：

- 单焦平面：警告焦距固定 ≈ 2.3 m，与外部行人焦距（10–30 m）存在调节冲突
- 多焦平面：警告焦距与行人焦距匹配，调节冲突最小

**对本研究的启示**：本实验若使用单焦平面 AR-HUD 模拟，应在 §5 局限性中说明这一限制。

---

## 6. 本周结论

1. **AR-HUD 临界 TTC 稳定在 2.0–2.5 s（与 HUD 一致），但提示级扩展更丰富**：Kim 2.5/5.0、Phan 2 s+16.6 m、Wang TTMD 5 s、Wu THW 3 s、Chen THW 3 s——AR-HUD 阶段的时间触发"语言"已演化出双阈值与复合公式。

2. **共形警告在时间维度上压缩 TTFF 与反应时**：Wu 2024 报告 BW 共形比 BD 屏幕固定 TTFF 短 **4.15 倍**（617 ms vs 2562 ms）——这是 AR-HUD 相比 HUD 的核心时间优势。

3. **共形优势是有条件的**：Kim & Gabbard (2019) 反例提示视觉复杂度过高的共形警告会引发注意隧道。本研究 RQ1 应控制视觉复杂度。

4. **TTMD 公式适用于二维相交场景**：Wang ARive 2025 的 $t_{min}$ 计算方法在交叉口、并道等场景下比纵向 TTC 更适用。本研究若覆盖交叉口场景应同时报告 TTC 与 TTMD。

5. **AR-HUD TTC 设计的硬件层约束**：系统延迟（< 100 ms）、深度感知线索的认知负荷、多焦平面切换等——这些是 HUD 阶段不需考虑的新维度，应在本研究方法学中讨论。

---

## 7. 下周（W6）计划

**主题**：AR-HUD 持续时长 + 升级时序（多级警告）

**具体任务**：
1. AR-HUD 子集中 7 篇明确量化 Duration 的研究详读（Ma 2021 / Ye & Yin 2025 / Wang 2025 等）
2. 多级警告升级时序专题分析：Lübbe 0.7 s 孤证 + Ma 2024 三色渐变 + Chen 2024 多目标分级
3. 共形动画与运动跟随的时间特性分析
4. 形成 AR-HUD Duration 表 + 级间间隔表 + 共形动画表三张细分表
5. 评述 AR-HUD 阶段升级时序的研究空白严重程度（vs HUD 阶段对比）

**预期产出**：W06_AR-HUD持续时长_升级时序.md

---

## 8. 本周引用 References

Chen, W., Niu, L., Liu, S., Ma, S., Li, H., & Yang, Z. (2024). Evaluating the effectiveness of contact-analog and bounding box prototypes in augmented reality head-up display warning for Chinese novice drivers. *International Journal of Human-Computer Interaction*. https://doi.org/10.1080/10447318.2024.2327197

Huo, F., & Alla, R. (2025). Differences in drivers' dependence on AR warning information in urban driving environments: The role of driving experience. *Frontiers in Virtual Reality*, *6*, 1638823. https://doi.org/10.3389/frvir.2025.1638823

Kim, H., & Gabbard, J. L. (2019). Assessing distraction potential of augmented reality head-up displays for vehicle drivers. *Human Factors*, *64*(5), 852–865. https://doi.org/10.1177/0018720819844845

Kim, H., Gabbard, J. L., Anon, A. M., & Misu, T. (2018). Driver behavior and performance with augmented reality pedestrian collision warning: An outdoor user study. *IEEE Transactions on Visualization and Computer Graphics*, *24*(4), 1515–1524. https://doi.org/10.1109/tvcg.2018.2793680

Phan, M. T., Thouvenin, I., & Frémont, V. (2016). Enhancing the driver awareness of pedestrian using augmented reality cues. In *2016 IEEE 19th International Conference on Intelligent Transportation Systems (ITSC)* (pp. 1298–1304). IEEE. https://doi.org/10.1109/itsc.2016.7795724

Tönnis, M., Sandor, C., Klinker, G., Lange, C., & Bubb, H. (2007). Experimental evaluation of an augmented reality visualization for directing a car driver's attention. In *2007 IEEE/ACM International Symposium on Mixed and Augmented Reality* (pp. 81–90). IEEE.

Vogel, K. (2003). A comparison of headway and time to collision as safety indicators. *Accident Analysis & Prevention*, *35*(3), 427–433. https://doi.org/10.1016/S0001-4575(02)00022-2

Wang, C., Chu, D., & Martens, M. (2025). ARive: Assisting drivers with in-car augmented reality for risk zone detection. *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies*, *9*(1), Article 22. https://doi.org/10.1145/3712270

Wu, Z., Liang, Y., Liu, G., & Ai, X. (2024). Comparative analysis of AR-HUDs crash warning icon designs: An eye-tracking study using 360° panoramic driving simulation. *Sustainability*, *16*(21), 9167. https://doi.org/10.3390/su16219167

---

*汇报状态：W5 完成（2026.07.25）*
*下次汇报：W6（2026.08.01），主题 = AR-HUD 持续时长 + 升级时序专题*
