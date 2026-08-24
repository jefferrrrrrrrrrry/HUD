# 第 6 周汇报：AR-HUD 持续时长 + 升级时序专题 + Ma (2024) 精读

**汇报周次**：W6（2026.07.26 – 2026.08.01）
**汇报对象**：[导师姓名]
**汇报人**：[学生姓名]

---

## 1. 本周目标

承接 W5 完成的 AR-HUD 警告时机分析，本周深化 AR-HUD 子集**两个核心研究空白维度**——持续时长与升级时序：

1. 汇总 AR-HUD 子集 7 篇明确报告 Duration 的研究，识别"2.5–3.0 s 传递链"共识
2. **按 IMRD 范式完整精读 Ma (2024) EID carpet**——AR-HUD 阶段唯一系统对照"生态界面 vs 主流警示"的实证研究
3. 升级时序 4 篇对比与 Lübbe 0.7 s 孤证的持续意义分析
4. 共形动画（跟随平滑度 / 跟随延迟）子维度报告率评估
5. 提炼本周 5 条共识

W6 是 AR-HUD 子集深化的收束周，W7 起进入 HUD vs AR-HUD 对比阶段。

---

## 2. AR-HUD 子集 Duration 维度证据聚合

AR-HUD 子集 26 篇中明确量化 Duration 的 7 篇按设计模式分四类：

### 2.1 模式一：固定时长（工程经验值传递链）

**Ma et al. (2021, idx 27)**——单条 3 s、紧急 10–15 s（车速自适应）。**W3 已详细分析**，依据 Wickens (2002) 多资源理论，但 Ma 自陈"the optimal duration remains an open question"——是工程经验值不是实证最优。

**Ye & Yin (2025, idx 09)**——**碰撞预警图形 Duration 固定 3 s**，直接**引用 Ma 2021 作为依据**——"3 s 已被证实为适宜"。**Duration 未作为自变量对照**，仅是固定参数。

**关键识别**：Ma 2021 → Ye & Yin 2025 形成"3 秒工程经验值传递链"——大家都引 Ma 但 Ma 自己都说是工程经验值。

### 2.2 模式二：动态消失 + 软件约束

**Wang ARive (2025, idx 20)**——激活条件 TTMD ≤ 5 s 且 d_min < 5 m，撤销条件反之。**实测平均 Duration = 2.7 s**（论文 §4.3 报告）。这个数字与 Ma 2021 的 3 s 高度接近——**两种独立模式都指向 2.5–3.0 s 的自然中位**。

### 2.3 模式三：完全动态（几何决定）

**Kim et al. (2018, idx 01)**——Virtual Shadow 共形阴影从触发开始持续到危险解除，随驾驶员-行人空间关系动态更新（阴影长度 / 透明度变化）。**没有"固定 Duration"概念——完全由几何决定**。这是 AR-HUD 共形动态 Duration 的经典范式。

### 2.4 模式四：动态 + 渐变消失（本周主打精读）

**Ma et al. (2024, idx 06) carpet**——生态界面（EID）设计：Phase 1 浅黄早期预警 → Phase 2 黄/橙加深 → 浅红/深红紧急；**风险解除后区域面积与饱和度逐渐减小直至消失**。风险感知时间从 0.81 s 缩短到 0.30 s（p<.001），DALI 主观负荷与瞳孔直径显著降低。**将在 §3 IMRD 精读**。

### 2.5 其他两篇（辅助支撑）

- **Charissis et al. (2021, idx 26)**——infotainment 场景下"基于驾驶任务复杂度的 Duration 调度"（拥堵或恶劣天气延迟消息释放）
- **Strle et al. (2023, idx 36)**——多通道生理信号（HRV / EDA / 皮温 / 瞳孔）实时反馈 Duration，LGBM 分类器 AUC ROC = 0.98

### 2.6 关键共识

AR-HUD 子集明确量化 Duration 的研究**数值都落在 2.5–3.0 s 或动态消失模式**——Ma 2021（3 s）、叶明慧 2025（沿用 3 s）、Wang 2025（动态平均 2.7 s）三篇独立研究均指向该范围。**但没有任何研究对照过不同固定 Duration 的差异**——RQ1 是首次系统对照。

---

## 3. Ma (2024) 精读汇报（IMRD 完整展开）

本节按学术论文的**引言—方法—结果—讨论**四段范式完整汇报 Ma (2024)——AR-HUD 阶段唯一系统对照"生态界面 vs 主流警示界面"的实证研究，也是"绿-黄-红渐变 + 动态消失"设计的代表性工作。

### 3.1 Introduction（引言）

#### 3.1.1 研究背景

- 在**自动驾驶未成熟、驾驶员对自动化不完全信任**的当下，以驾驶员人工反应为核心的驾驶预警系统（DWS）将长期是主流
- 驾驶员从前方道路获取的信息中**视觉占比高达 80%**
- AR-HUD 可把虚拟信息直接放在视线中，加快信息处理、减少分心
- **但存在内在矛盾**：AR-HUD 显示区域与驾驶员道路视场重叠较多，界面混乱或过大会干扰真实环境感知、增加认知负荷；反之过简又导致信息传达不清

#### 3.1.2 研究缺口

Ma 识别的关键缺口——**已有研究涉及**：
- AR-HUD 信息呈现与认知负荷（Hooey、Liu 等）
- 贴合式图形优于普通图形（Kim & Gabbard）
- AR-HUD 信息可视化分类（Tönnis、Kunze、Hauslschmidt、Wiegand、Müller）
- EID 在 ACC 与车道变更预警上的应用（Lee 2006、Seppelt 2007、Schewe 2018）
- EID 在 AR-HUD 上初次应用（Kim 2016 的 Virtual Shadow）

**但已有研究多为"单场景单警示"验证，缺乏面向"复杂多警示场景"的系统化 EID 设计策略**。

#### 3.1.3 三个可证伪命题

- **H1**：AR-HUD 生态界面（HMI1）在单警示场景中可降低驾驶员认知负荷
- **H2**：在复杂多警示场景中 HMI1 同样降低认知负荷
- **H3**：无论单或多警示，HMI1 均可缩短风险感知与决策时间

**H2 的特殊价值**：它承认单警示的成功不必然迁移到多警示——这是本文的方法学洞察。

### 3.2 Method（方法）

#### 3.2.1 被试

- 初招 N = 25，**剔除眼动识别率 < 85% 的 2 人 + 问卷错误 1 人，最终 22 名分析**
- 性别比：**12 男 / 13 女**
- 年龄：22–27 岁（**M = 25.36，SD = 1.82**）——年轻组样本
- 驾龄分布：1–2 年 5 人；2–3 年 3 人；4–5 年 5 人；5 年以上 12 人
- 招募要求：持中国驾照；≥ 1 年驾龄；有 L1–L3 自动驾驶车体验；自有或长期驾驶带 HUD 车辆
- **样本年轻是明显局限**——未覆盖中老年与新手

#### 3.2.2 实验设计

- **类型**：组内（within-subject），**2 × 5 设计**
- **自变量 1（界面，2 水平）**：HMI1 生态界面 vs HMI2 主流警示界面
- **自变量 2（警示场景，5 水平）**：
  - S1 前向碰撞（50 km/h 前车减速）
  - S2 限速（60 km/h 接近 50 km/h 限速段）
  - S3 侧向碰撞（40–50 km/h 直行进入路口，右侧来车）
  - S4 车道偏离（30 km/h 左车道带轻微左偏）
  - **S5 复合（S4 + 对向相邻车道来车）**——最复杂多警示场景，直接检验 H2

#### 3.2.3 因变量分三层

- **主观**：DALI（Driving Activity Load Index，1–10 五维度加权和）
- **眼动**：AFD（Average Fixation Duration）、APD（Average Pupil Diameter）
- **行为**：**风险感知时间**（AOI 出现到首次注视）、**风险决策时间**（首次注视到按键反应）

#### 3.2.4 设备与刺激规格

- **环境**：同济大学汽车人因实验室，固定基座驾驶模拟器
- **仿真软件**：Unity 2023
- **显示器**：**3 块 55 英寸 4K 显示器（3840 × 2160）**
- **眼动仪**：Tobii Glasses 2 + Tobii Pro Lab 1.194

**HMI1 carpet 核心设计（5 组件）**：
- (a) **安全驾驶区**：与车身等宽，含义随场景不同（碰撞 = 安全距离 RBB；车道偏离 = 最大允许横向偏移 KBB）
- (b) **风险越界区**：驾驶行为超出安全范围的实时映射
- (c) **渐变色块**：饱和度随风险递增
- (d) (a)+(b) 复合：当前驾驶状态与安全值差异、推荐操作方向
- (e) (b)+(c) 复合：障碍物方向矢量

**三色语义**：绿 = 安全 / 浅黄 = 一级早期警告 / 黄/橙加深 = 风险上升 / 浅红/深红 = 二级紧急警告

**注册方式**：**3D 路面锁定**（Road-conformal），聚焦**中央凹视场 2° 范围**

#### 3.2.5 流程

1. 介绍研究目的、解释两类界面含义
2. 5 分钟自由练习（无事件）
3. **10 次正式驾驶**（5 场景 × 2 界面，拉丁方逆平衡）
4. 每次后填 DALI
5. 结束后半结构化访谈

### 3.3 Results（结果）

**Ma 的因变量按主观 / 眼动 / 行为三层解读**——每层反映不同的驾驶员认知过程。

#### 3.3.1 主观层 DALI——反映"驾驶员觉得多累"

| 场景 | HMI1 (SD) | HMI2 (SD) | p 值 |
|---|---|---|---|
| **全场景平均** | **21.45 (1.84)** | **30.84 (8.43)** | **< 0.001** |
| S1 前碰 | 23.64 | 25.09 | 0.324（n.s.） |
| S2 限速 | 18.91 (3.94) | 34.18 (9.18) | < 0.001 |
| S3 侧碰 | 22.73 (4.13) | 32.18 (5.55) | < 0.01 |
| S4 车道偏离 | 20.73 | 19.64 | 0.391（n.s.，HMI2 稍低） |
| **S5 复合** | **21.27 (3.82)** | **43.09 (8.36)** | **< 0.001** |

**关键发现**：**HMI1 优势在多警示（S5）场景最显著（21 vs 43）——H2 被验证**。S1 前碰与 S4 车道偏离场景 HMI1 无显著优势，提示 EID 不是万能的。

**DALI 维度分析**：
- 注意需求：HMI1 = 1.44 vs HMI2 = 3.82（p < 0.001，**下降最显著**）
- 视觉需求：HMI1 = 2.15 vs HMI2 = 2.89（p < 0.01）
- 时间需求：HMI1 = 2.18 vs HMI2 = 3.16（p < 0.001）
- 干扰水平、情境压力：无显著差异

#### 3.3.2 眼动层 AFD + APD——反映"客观视觉负载 + 生理唤醒"

**AFD（平均注视时长，秒）**：
- 全场景平均：HMI1 = 0.55 (0.07) vs HMI2 = 0.69 (0.18)
- S2 限速：0.55 vs 0.77（p < 0.05）
- **S5 复合：0.59 vs 0.92（p < 0.001）**——**HMI2 多警示场景注视时长激增 33%**

**APD（平均瞳孔直径，mm）**：
- 全场景平均：HMI1 = 4.75 (0.19) vs HMI2 = 5.10 (0.27)
- S3 侧碰：4.80 vs 5.26（p < 0.05）
- **S5 复合：4.96 vs 5.44（p < 0.001）**——**瞳孔直径是认知负荷客观代理**，HMI1 让驾驶员生理层面也更轻松

#### 3.3.3 行为层——两个时间指标最亮眼

**风险感知时间**：
- **HMI1 = 0.30 s (SD 0.04) vs HMI2 = 0.81 s (SD 0.32)**
- **缩短 62.96%，标准差减少 87.5%**
- 配对 t 检验 p = 0.022

**风险决策时间**：
- **HMI1 = 0.53 s (SD 0.06) vs HMI2 = 0.81 s (SD 0.10)**
- **缩短 34.57%，标准差减少 40%**
- p = 0.003

**因变量分层实际意义解读**：

| 层 | 反映的驾驶员认知 | HMI1 优势的解释 |
|---|---|---|
| DALI | 主观认知努力体验 | carpet 降低注意资源分配需求（1.44 vs 3.82） |
| AFD | 客观视觉负载（每次注视多久） | 减少多点注视混乱，稳定在 0.6 s |
| APD | 生理唤醒 / 认知负荷代理 | 客观生理层面负荷降低 |
| 风险感知/决策时间 | 反应速度 + 稳定性 | 感知快 63%、决策快 35%，SD 减少 40-87% |

**一句话总结结果**：**HMI1 生态 carpet 在多警示场景（S5）优势最显著**，让驾驶员从"多点注视混乱"切换到"单一 carpet 稳定注视"，风险感知时间缩短 63%。

#### 3.3.4 访谈发现

- 多数被试反馈 HMI1 的"安全/危险区对比"让他们直观把握速度调控范围
- **经验丰富的驾驶员认为大面积警示可能占用注意**——这是访谈中出现的矛盾反馈
- 初次使用 HMI1 存在学习负担，但快速适应后产生依赖

### 3.4 Discussion（讨论）

#### 3.4.1 Ma 的核心方法学贡献——三层设计框架

**系统层**：EID + Abstraction Hierarchy（AH）+ Rasmussen SRK（Skill-Rule-Knowledge）三合一
**策略层**：Cognitive Load Theory（CLT）的内在 / 外在 / 相关负荷调节
**视觉层**：颜色 / 透明度 / 动效 / 饱和度 / 位置

这个框架比 Kim 2016 首次 EID 应用更系统，是"复杂多警示场景 EID 设计"的方法学奠基。

#### 3.4.2 Ma 自陈的六个局限

1. **仅 22 名年轻被试**（22–27 岁），未覆盖中老年与新手
2. **仅在固定基座模拟器中测试**
3. **"carpet"大面积可视区域对经验丰富驾驶员可能干扰**——访谈中确实有被试反馈
4. **未量化具体 RGB 色值**——无法直接工程复制
5. **没有具体的 TTC 阈值与触发时机量化**——与 Kim 2018 形成鲜明对照
6. **没有考虑光照 / 雨雾天气**

#### 3.4.3 对本研究（HUD/AR-HUD 时间元素设计规范）的三个具体启示

**启示 1（继承）：三色渐变 + 动态消失 Duration 模型**

Ma 的"绿-黄-红交通信号灯语义 + 饱和度随风险递增 + 风险解除后渐变消失"可直接沿用为 RQ1 的"至危险解除"操作化——**Duration 不是硬性截断而是渐变消失机制（面积 + 饱和度递减）**。这是"共形 Duration 由几何决定"的自然实现。

**启示 2（警示）：EID 优势是场景依赖的**

**S1 前向碰撞与 S4 车道偏离场景 HMI1 无显著优势**——这提示 EID carpet 不是万能的，可能因为这两个场景信息量小（单一威胁 + 简单动作），大面积 carpet 反而增加视觉复杂度。**对 RQ1 有直接意义**——**行人碰撞场景类似 S1**，需谨慎评估共形警告的视觉复杂度设计——RQ1 实验应控制共形警告的视觉复杂度（如仅使用简化包围框 + 三色饱和度渐变），避免"过度复杂"引发注意隧道。

**启示 3（扩展）：将三色渐变的"颜色分级"与"时间分级"解耦为独立自变量**

**Ma 未量化 Phase 1 → Phase 2 的时间间隔**——仅以"风险数值增加"作为质性描述。**将 Ma 2024 的"绿→黄→红"三阶段转换用具体 TTC 触发时机量化，就是本研究 RQ2 的直接扩展**——RQ2 首次将"颜色分级"与"时间分级"解耦为独立自变量，做 2 × 4 因子实验（颜色分级 2 水平：单色 vs 三色渐变 × 时间分级 4 水平：Δ = 0.5 / 0.7 / 1.0 / 1.5 s）。

---

## 4. 升级时序 4 篇对比与 Lübbe 0.7 s 孤证的持续意义

### 4.1 Lübbe (2017) 0.7 s 孤证的稳定性

**W1–W2 已详细分析**——TTC = 2.5 s 触发 L1（HUD 视觉提示 + 57 dBA 低音）→ TTC = 1.8 s 触发 L2（audio-visual + 64 dBA + 触觉脉冲），**级间间隔 = 0.7 s**。

**理论支撑**（W9 将进一步展开）：
- Posner (1980) 视觉处理时间 + 信息整合时间约 0.5–1.0 s
- Endsley (1995) SA 三层 L1（感知）→ L2（理解）处理时间约 0.5–1.0 s
- **0.7 s 恰好落在该理论预测的中央位置**——并非工程巧合

### 4.2 AR-HUD 阶段级间间隔仍未量化

**Ma (2024) 三色渐变**——**级间转换基于风险数值触发而非固定时间间隔**。Ma 未报告 Phase 1 → Phase 2 的时间间隔，仅以"风险增加"作为质性描述。

**Wang ARive (2025) 二级 TTMD**：
- L1 预警级：2 s < TTMD ≤ 5 s
- L2 临界级：TTMD ≤ 2 s
- **级间间隔在 TTMD 单位下为 3 s**

**但 TTMD 不等于时间**——如果车辆与行人均以恒定速度运动，TTMD = 5 s 到 TTMD = 2 s 的真实时间间隔可能 < 3 s（因相对运动接近时 TTMD 下降加速）。**Wang 报告的"3 s TTMD 间隔"在真实场景下的等效时间间隔需另行测算**。

### 4.3 Chen (2024, idx 40) 多目标——颜色优先级分级（无级间时间）

> Chen, W., Song, C., Luo, J., Xu, Z., Li, H., Ma, S., Wang, Q., & Yang, Z. (2024). Priority design in multi-target AR-HUD warning: Evidence from eye movement and behavior of the novice driver. *IJHCI*.

- N = 45 中国新手驾驶员
- 三类警告模式：Equivalent（均等，所有目标同色红）/ Hierarchical（分级，红=最高 / 黄=次优 / 绿=低优）/ Baseline（无警告）

**核心结果**：
- 分级警告反应时 **1083 ms** vs 均等警告 **1707 ms**（**-36%**, p < .001）
- 注视熵 Hs 从 1.92 降至 1.31（-32%）
- 注视转移熵 Ht 从 0.30 降至 0.18（-40%）
- **5 目标条件下分级优势消失**（TTFF 不显著）——刺激密度饱和（Wickens 多资源上限的印证）

**关键发现**：Chen 仍以**颜色做分级**而非**时间做分级**。级间转换是空间的（红→黄）而非时间的（提前 0.7 s 触发）。

### 4.4 Yoon (2014) / Park (2013) 三级框架（未量化阈值）

- Yoon (2014)：明确提出 "three threat level decided by the calculated TTC values"，但未量化各级 TTC
- Park (2013) ETRI Journal：工程系统层面的三级预警提案

### 4.5 关键共识

AR-HUD 阶段虽出现多级警告，但**级间是空间维度（红→黄）而非时间维度（提前 0.7 s 触发）**——**Lübbe 0.7 s 到今天仍是唯一在时间维度量化级间间隔的实证**。RQ2 应首次把"颜色分级"与"时间分级"解耦为独立自变量做对照实验。

---

## 5. 共形动画维度：跟随平滑度与跟随延迟

### 5.1 共形动画的两个新子维度

AR-HUD 阶段引入"运动跟随"后，时间设计从原 5 维拓展为 7 维：
1. 警告时机（TTC / Lead Time）
2. 持续时长（Duration）
3. 闪烁频率
4. onset-offset 动画过渡
5. 升级时序（级间间隔）
6. **跟随平滑度（Refresh Rate / 阶跃 vs 平滑）**——AR-HUD 新增
7. **跟随延迟（Latency）**——AR-HUD 新增

### 5.2 现有研究报告率

| 文献 | 跟随平滑度 | 跟随延迟 |
|---|---|---|
| Kim (2018) | Virtual Shadow 实时平滑 | 报告 **~50 ms** |
| Wang ARive (2025) | Red Carpet 实时贴地 | 报告 **~80 ms** |
| Wu (2024) | BW 行人位置实时跟随 | 未报告 |
| Ma (2024) | 饱和度渐变 | 未报告 |
| 其他 22 篇 | 未涉及 | 未涉及 |

**报告率仅 5/26 = 19%**。

### 5.3 共形动画对认知负荷的潜在影响

W5 § 4.2 Kim & Gabbard (2019) 已警示：**视觉复杂度过高的共形警告引发注意隧道**（mental demand +23.7%，HUD-graphic 注视时长 3.33 s vs 屏幕固定 1.17 s）。

**理论推荐**（Yantis & Hillstrom 1994 + Wickens 2002）：
- 更新频率 **30–60 Hz**（避免视觉抖动）
- 跟随延迟 **≤ 100 ms**（Adelstein 2003 VR 人因研究）
- 避免高对比度阶跃跟随（引发过度捕获）

**对本研究的意义**：RQ1 方法学应明确控制共形动画的硬件参数——跟随延迟 ≤ 100 ms、刷新率 ≥ 60 Hz、平滑跟随（非阶跃）。

---

## 6. 本周共识（Weekly Consensus）

本周提炼 5 条核心共识：

1. **AR-HUD 子集 7 篇明确量化 Duration 的研究数值集中在 2.5–3.0 s 或动态消失**——Ma 2021（3 s）、叶明慧 2025（沿用 3 s）、Wang 2025（动态平均 2.7 s）三篇独立指向该范围；**但没有任何研究对照过不同固定 Duration 的差异**——RQ1 是首次系统对照。

2. **Ma (2024) EID carpet 是 AR-HUD 阶段唯一系统对照生态界面 vs 主流警示的实证**——三层设计框架（系统 EID+AH+SRK / 策略 CLT / 视觉）+ 5 组件 carpet + 三色渐变——**在多警示 S5 场景优势最显著**（DALI 21 vs 43，风险感知时间从 0.81 s 缩短到 0.30 s，减少 62.96%）。

3. **Ma (2024) 揭示"EID 优势是场景依赖的"**——S1 前向碰撞与 S4 车道偏离场景 HMI1 无显著优势——**对 RQ1 有直接意义**：行人碰撞场景类似 S1，需谨慎评估共形警告的视觉复杂度设计。

4. **Lübbe (2017) 的 0.7 s 仍是 AR-HUD 阶段唯一明确级间时间的研究**——Ma 2024 三色渐变、Wang ARive 2 s TTMD、Chen 2024 多目标分级**均用颜色或几何做分级而非时间**——RQ2 首次把"颜色分级"与"时间分级"解耦为独立自变量。

5. **共形动画维度报告率仅 5/26 = 19%**——跟随平滑度与跟随延迟仅 Kim 2018（~50 ms）和 Wang 2025（~80 ms）明确报告。本研究 §3 方法学应明确控制共形动画的硬件参数（跟随延迟 ≤ 100 ms，刷新率 ≥ 60 Hz）。

---

## 7. 下周（W7）计划

**主题**：HUD vs AR-HUD 时间设计对比 + 评估指标分类 + Chen (2024) contact-analog 精读

**具体任务**：
1. **按 IMRD 范式完整精读 Chen (2024) contact-analog vs Bounding Box**——AR-HUD 阶段中国新手样本代表性研究，Contact-Analog vs BB 反直觉发现
2. 整合 W1–W6 已识别的 HUD 与 AR-HUD 子集证据，形成"对比矩阵"
3. 评估指标的四层分类（行为 / 眼动 / 主观 / 生理）
4. 共形 vs 屏幕固定的"时间-空间耦合"效应总结
5. 提炼本周 5 条共识

**预期产出**：W07_HUD与AR-HUD时间设计对比.md（含 Chen 2024 IMRD 精读 + 5 维对比矩阵）

---

## 8. 本周引用 References

Charissis, V., Falah, J., Lagoo, R., Alfalah, S. F. M., Khan, S., & Wang, S. (2021). Employing emerging technologies to develop and evaluate in-vehicle intelligent systems for driver support: Infotainment AR HUD case study. *Applied Sciences*, *11*(4), 1397. https://doi.org/10.3390/app11041397

Chen, W., Song, C., Luo, J., Xu, Z., Li, H., Ma, S., Wang, Q., & Yang, Z. (2024). Priority design in multi-target AR-HUD warning: Evidence from eye movement and behavior of the novice driver. *International Journal of Human-Computer Interaction*. https://doi.org/10.1080/10447318.2024.2439572

Endsley, M. R. (1995). Toward a theory of situation awareness in dynamic systems. *Human Factors*, *37*(1), 32–64. https://doi.org/10.1518/001872095779049543

Kim, H., & Gabbard, J. L. (2019). Assessing distraction potential of augmented reality head-up displays for vehicle drivers. *Human Factors*, *64*(5), 852–865. https://doi.org/10.1177/0018720819844845

Kim, H., Gabbard, J. L., Anon, A. M., & Misu, T. (2018). Driver behavior and performance with augmented reality pedestrian collision warning: An outdoor user study. *IEEE Transactions on Visualization and Computer Graphics*, *24*(4), 1515–1524. https://doi.org/10.1109/tvcg.2018.2793680

Lübbe, N. (2017). Brake reactions of distracted drivers to pedestrian forward collision warning systems. *Journal of Safety Research*, *61*, 23–32. https://doi.org/10.1016/j.jsr.2017.02.002

Ma, J., Li, Y., & Zuo, Y. (2024). Design and evaluation of ecological interface of driving warning system based on AR-HUD. *Sensors*, *24*(24), 8010. https://doi.org/10.3390/s24248010

Ma, X., Jia, M., Hong, Z., Kwok, A. P. K., & Yan, M. (2021). Does augmented-reality head-up display help? A preliminary study on driving performance through a VR-simulated eye movement analysis. *IEEE Access*, *9*, 129951–129964. https://doi.org/10.1109/access.2021.3112240

Park, H. S., Park, M. W., Won, K., Kim, K.-H., & Jung, S. K. (2013). In-vehicle AR-HUD system to provide driving-safety information. *ETRI Journal*, *35*(6), 1038–1047. https://doi.org/10.4218/etrij.13.2013.0041

Posner, M. I. (1980). Orienting of attention. *Quarterly Journal of Experimental Psychology*, *32*(1), 3–25. https://doi.org/10.1080/00335558008248231

Strle, G., Košir, A., Sodnik, J., & Stojmenova, K. (2023). Physiological signals as predictors of cognitive load induced by the type of automotive head-up display. *IEEE Access*, *11*, 87884–87898. https://doi.org/10.1109/access.2023.3305383

Wang, C., Chu, D., & Martens, M. (2025). ARive: Assisting drivers with in-car augmented reality for risk zone detection. *PACM IMWUT*, *9*(1), Article 22. https://doi.org/10.1145/3712270

Ye, M. H., & Yin, J. (2025). Spatial plane positioning of AR-HUD graphics: Implications for driver inattentional blindness in navigation and collision warning scenarios. *Electronics*, *14*(23), 4768. https://doi.org/10.3390/electronics14234768

Yoon, C., Kim, K.-H., Park, H. S., Park, M. W., & Jung, S. K. (2014). Development of augmented forward collision warning system for head-up display. In *IEEE ITSC 2014* (pp. 2277–2279). IEEE. https://doi.org/10.1109/itsc.2014.6958054

---

*汇报状态：W6 完成（2026.08.01），继续沿用"每周一篇重点精读 + IMRD 完整展开 + 5 条本周共识"结构*
*下次汇报：W7（2026.08.08），主题 = HUD vs AR-HUD 对比矩阵 + Chen (2024) IMRD 精读*
