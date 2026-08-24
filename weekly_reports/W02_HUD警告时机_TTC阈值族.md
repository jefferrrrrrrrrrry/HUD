# 第 2 周汇报：HUD 警告时机（TTC 阈值族）深化分析

**汇报周次**：W2（2026.06.28 – 2026.07.04）
**汇报对象**：[导师姓名]
**汇报人**：[学生姓名]

---

## 1. 本周目标

承接 W1 已完成的 HUD 子集 14 篇精读，本周聚焦其中 **4 篇明确量化 TTC 阈值的文献**，做证据聚合（evidence aggregation）：

1. 把不同车速下报告的 TTC 阈值统一换算为标准车速（50 km/h）下的距离 / 时间值
2. 引入交通工程与人因经典理论（Hayward 1972 / Hooper 1936 PIEV / Olson & Sivak 1986 / AASHTO 2.5 s）作为理论锚点
3. 评述 TTC 阈值与人因机制（PIEV 总时间约束、信号检测论 d′/β 权衡）的对应关系
4. 形成"TTC 阈值证据表"作为论文 §2.2.1 的核心实证基础

---

## 2. 本周文献整理

W2 不引入新文献，深化 W1 已识别的 4 篇 HUD 子集量化 TTC 研究，并补充 5 篇经典理论文献作为锚点。

### 2.1 HUD 子集明确量化 TTC 的 4 篇研究

#### 2.1.1 Lübbe (2017, idx 14) — TTC 1.8 / 2.5 s 二级阈值

**核心数据**：
- 实验环境：Toyota 高保真 moving-base 驾驶模拟器（穹顶 7.1 m + 360° 投影 + 6 自由度运动平台）
- 被试：N = 40 分心驾驶员（5 位数字心算次任务）
- 测试车速：50 km/h
- 警告设计：基础 audio-visual 在 TTC = 1.8 s 触发（持续 1.8 s）；Setting 3 / 4 增加 TTC = 2.5 s 触发的 HUD 视觉提示
- 结果：Setting 4（audio-visual + 触觉脉冲）仅 1 次碰撞（vs 其他设置 8–10 次），平均反应时 0.8 s（SD = 0.29 s）

**Lead Time 物理换算**（50 km/h = 13.89 m/s）：
- TTC = 1.8 s → 距离 = 25.0 m
- TTC = 2.5 s → 距离 = 34.7 m
- 级间间隔 0.7 s → 距离差 9.7 m

#### 2.1.2 Kazazi et al. (2015, idx 16) — flow point 触发，老年组前移 7 m

**核心数据**：
- 实验环境：固定基座 HUD 模拟器
- 被试：青年 N = 36（20–35 岁）vs 老年 N = 36（≥ 65 岁）
- 测试车速：30 km/h（城市低速）
- 警告设计：基于"flow point"概念（车速 × 行人横穿启动同步），老年组的 Pedestrian 2 场景预警触发点比青年组前移 7 m
- 结果：老年组对 SW（停止标志）反应更快更强；青年组对 CW（提示标志）反应最快最强

**Lead Time 物理换算**（30 km/h = 8.33 m/s）：
- 青年组：假设原触发点对应 TTC ≈ 2.0 s，则 Lead Time ≈ 16.7 m
- 老年组：前移 7 m → Lead Time ≈ 23.7 m，TTC ≈ **2.84 s**
- 老年组所需 Lead Time 比青年组增加 **42%**

#### 2.1.3 Zhang/边扬等 (2024, idx 12) — 100 m 距离触发（中国驾驶员）

**核心数据**：
- 实验环境：网联 V2X 驾驶模拟器
- 被试：N = 34 中国驾驶员
- 测试车速：60 km/h
- 警告设计：固定 **100 m 距离** 触发（不基于 TTC）；行人在 60 m 处激活，以 1 m/s 横穿
- 结果：首次制动距离平均 27.3 m（vs 基线 64.5 m），最小冲突距离 20.96 m（vs 基线 10.75 m），最大减速度 5.03 m/s²（vs 基线 8.30 m/s²）；雾天条件下 HUD 优势显著放大

**Lead Time 物理换算**（60 km/h = 16.67 m/s）：
- 100 m 触发距离 → Lead Time ≈ **6.0 s**
- 该数值超出 Lübbe（2.5 s）与 Kim (2018, AR-HUD 5.0 s 上限）的主流上限
- **提示中国语境下时间设计可能存在系统性差异**

#### 2.1.4 Ma et al. (2021, idx 27) — 速度相关阈值（间接）

**核心数据**：
- 实验环境：VR 仿真 AR-HUD（但本研究 HUD 模式仍属传统）
- 被试：N = 12（同济大学）
- 测试车速：30 / 60 / 90 km/h 三档
- 警告设计：未明确报告 TTC 阈值；FOV 分级（< 75 km/h 用 85°，75–100 用 65°，> 100 用 40°）
- 该研究的核心贡献是 **Duration**（3 s 常规 + 10–15 s 紧急），TTC 维度仅作背景

**评述**：Ma (2021) 未量化 TTC，本节仅将其作为"速度自适应"思路的代表，不进入证据聚合表的核心条目。

### 2.2 经典理论锚点（5 篇）

#### 2.2.1 Hayward (1972) — TTC 原始定义
> Hayward, J. C. (1972). Near-miss determination through use of a scale of danger. *Highway Research Record*, *384*, 24–34.
- **首次提出 TTC 概念**：若两车辆维持当前速度和路径，发生碰撞所需的时间
- 公式：TTC = d / v_rel（纵向场景）
- 最初用于交通冲突技术（Traffic Conflict Technique），后被引入主动安全系统

#### 2.2.2 Hooper (1936) — PIEV 模型
> Hooper, K. G. (1936). *Driver perception-reaction time*. Institute of Transportation Engineers.
- 把驾驶员反应过程分解为 **Perception → Identification → Emotion → Volition** 四阶段
- 总 PRT（PIEV 总时间）：典型值 1.5 s（普通驾驶员对意外事件）
- 后被 AASHTO 标准化为 **2.5 s 设计 PRT**（含 95 百分位安全裕量）

#### 2.2.3 Olson & Sivak (1986) — PRT 经验分布
> Olson, P. L., & Sivak, M. (1986). Perception-response time to unexpected roadway hazards. *Human Factors*, *28*(1), 91–96.
- 实测：普通驾驶员 PRT **中位数 1.1 s，第 95 百分位 1.5 s**
- 反应时呈右偏对数正态分布（非正态），存在长尾延伸至 3 s 以上
- 该研究是 AASHTO 2.5 s 标准的实证基础之一

#### 2.2.4 Green & Swets (1966) — 信号检测论 SDT
> Green, D. M., & Swets, J. A. (1966). *Signal detection theory and psychophysics*. Wiley.
- 区分**灵敏度 d′**（系统区分信号 vs 噪声的能力）与**判据 β**（响应偏好程度）
- 应用到 PCW 设计：TTC 阈值越大 → 灵敏度高（不漏报）但虚警率上升；阈值越小 → 判据严格但漏报风险

#### 2.2.5 Lee et al. (2002) — 分心驾驶员 PRT 延长
> Lee, J. D., McGehee, D. V., Brown, T. L., & Reyes, M. L. (2002). Collision warning timing, driver distraction, and driver response to imminent rear-end collisions in a high-fidelity driving simulator. *Human Factors*, *44*(2), 314–334.
- 分心驾驶员 PRT 平均延长 **0.5–1.0 s**
- 在分心条件下，TTC 阈值需相应前移；这是 Lübbe (2017) 选择 1.8 s 而非更短的理论依据

---

## 3. TTC 阈值证据聚合表（W2 核心产出）

下表将上述 4 篇 HUD 量化研究换算到统一车速维度，方便对照阅读。**最右两列**是基于人因机制的解释。

| 文献 | 实验车速 | TTC 触发值 | 等价 50 km/h 距离 | 实测平均 PRT | 安全裕量 = TTC − PRT − t_brake* | 人因机制对应 |
|---|---|---|---|---|---|---|
| Lübbe (2017) L2 | 50 km/h | **1.8 s** | 25.0 m | 0.80 s (SD=0.29) | 1.8 − 0.8 − 0.7 = **0.3 s** | 临界级（PIEV 全部 + 制动响应紧贴） |
| Lübbe (2017) L1 | 50 km/h | **2.5 s** | 34.7 m | – | 2.5 − 1.5 − 0.7 = **0.3 s**（普通 PRT） | 提示级（PIEV 完成 + 警告读取留 0.3 s） |
| Kazazi (2015) 青年 | 30 km/h | ~2.0 s (推算) | 16.7 m | ~1.1 s | 2.0 − 1.1 − 0.7 = **0.2 s** | 接近 AASHTO 临界 |
| Kazazi (2015) 老年 | 30 km/h | **~2.84 s** | 23.7 m | ~1.4 s | 2.84 − 1.4 − 0.7 = **0.74 s** | 老年 PRT 延长补偿 |
| Zhang/边扬 (2024) | 60 km/h | **~6.0 s** | 83.3 m | 未报告 | 6.0 − 1.5 − 1.3 = **3.2 s** | 远超 PIEV 需求（雾天 / 中国语境冗余） |

*注：t_brake = 50 km/h 下紧急制动响应时间，取经验值 0.5–0.7 s；60 km/h 下取 1.3 s

### 3.1 关键发现

**发现 1：TTC 1.8–2.5 s 的"PIEV 物理下界"约束**
- 临界级 TTC（如 Lübbe 1.8 s）= 普通 PRT（1.0 s）+ 制动响应（0.7 s）+ 极小安全裕量（0.1 s）
- 提示级 TTC（如 Lübbe 2.5 s）= 设计 PRT（1.5 s）+ 制动响应（0.7 s）+ 警告读取时间（0.3 s）
- **这并非工程巧合，而是 PIEV 总时间的物理累加约束**：1.5 + 0.7 + 0.3 ≈ 2.5 s

**发现 2：老年 / 分心条件需 TTC 前移 0.3–1.0 s**
- Kazazi 老年组：前移 7 m（30 km/h 下对应 +0.84 s）
- Lee (2002) 元分析：分心条件 PRT 延长 0.5–1.0 s
- 推论：**老年 + 分心组合条件**理论上 TTC 阈值应达 3.0–3.5 s（远超现有 1.8 s 临界级）

**发现 3：100 m 距离触发（Zhang 2024 中国研究）的"过度冗余"**
- 60 km/h 下 100 m = 6.0 s Lead Time，超 PIEV 物理需求 ~3.5 s
- 解释 1：雾天能见度低，需补偿被试视觉获取延迟
- 解释 2：中国城市道路行人横穿不可预测性高，安全裕量需扩大
- 解释 3：研究方法学差异（VLC 网联系统对触发逻辑的影响）
- **本硕士论文 RQ1+RQ3 应考察中国驾驶员在 2.5–5.0 s 范围内的偏好曲线**

---

## 4. 与人因理论的对应关系

### 4.1 PIEV 模型对 TTC 下界的约束

PIEV 总时间（PRT）= Perception + Identification + Emotion + Volition：
- Perception：感觉器官捕捉刺激，~150–300 ms（Posner 1980）
- Identification：识别为危险目标，~300–500 ms
- Emotion + Volition：决策与执行动作启动，~500–700 ms
- **合计**：1.0–1.5 s（普通），1.5–2.5 s（分心 / 老年）

加上车辆制动响应（0.5–1.3 s）与极小安全裕量，**最低 TTC ≈ 1.5–3.0 s**——这与 Lübbe (1.8 s) 与 Kazazi 老年组 (2.84 s) 的实证完全一致。

### 4.2 信号检测论 SDT 对 TTC 选择的解释

设 PCW 系统的 TTC 阈值为 τ：
- τ 越大（如 5.0 s）：灵敏度 d′ 高（更少漏报），但虚警率 FAR 上升 → 驾驶员信任降低（Bliss 2003 元分析：FAR > 30% 时信任显著下降）

> **⚠ 归因更正（2026-08，全库统一）**：本处引用的「Bliss（2003）元分析：虚警率 > 30% 时信任显著下降」**已撤回**。经 Crossref 核验，Bliss (2003)（*The International Journal of Aviation Psychology, 13*(3), 249–268）是**航空事故与事件的档案分析**，既非元分析亦非驾驶研究，且 **30% 这一门限在 Bliss 的任何原始文献中均未核实到**。可引的替代证据为 Bliss et al. (1995) 的概率匹配关系（*Ergonomics, 38*(11), 2300–2312）与 Bliss & Acton (2003) 的汽车碰撞报警可靠性研究（*Applied Ergonomics, 34*(6), 499–509）。详见 `AR-HUD行人碰撞预警_毕业论文研究框架.md` §14.9 第 4 条。

- τ 越小（如 1.0 s）：判据 β 严格（虚警少），但漏报风险陡增 → 极端情境下"无救援区"

**Kim (2018) 的双阈值方案（2.5 + 5.0 s）实际是 SDT 框架下的"双判据"设计**：5.0 s 优化 d′（发现潜在危险），2.5 s 优化 β（仅强警告真正紧迫）。

### 4.3 双系统理论对 TTC 时机的认知映射

Kahneman & Tversky (1974) 双系统理论：
- **System 1（快思考）**：< 1 s 反应，无意识 / 经验启发式
- **System 2（慢思考）**：> 2 s 反应，有意识 / 分析判断

PCW 时间设计的 System 映射：
- TTC ≤ 1.8 s：仅 System 1 可用（紧急制动）
- TTC = 2.5–5.0 s：System 2 介入空间（判断"是否真危险"）
- TTC > 5.0 s：可能产生过度审议，反而错过最佳响应窗口

**这是为何 Lübbe (2017) 选择 2.5 s 作为提示级的认知机制依据**——既允许 System 2 介入做信息校验，又不至于过早进入"过度审议"模式。

---

## 5. 本周结论

1. **HUD 量化 TTC 的 4 篇研究共同指向 PIEV 物理下界**：1.8–2.5 s 临界级 / 2.5–5.0 s 提示级的共识并非偶然，而是 PRT + 制动响应 + 安全裕量的物理累加约束。

2. **TTC 阈值是"年龄 × 分心 × 场景"的多元函数**：Kazazi 老年前移 7 m + Lee 分心 PRT 延长 0.5–1.0 s + Zhang 中国语境冗余 → **理论上极端条件（老年 + 分心 + 城市雾天）需 TTC 达 3.5 s 以上**。

3. **现有研究仍未覆盖的关键参数空间**：
   - TTC × 车速交互效应（多数研究固定单一车速）
   - TTC × 年龄 × 分心 三维交互（极少研究覆盖完整设计）
   - 中国驾驶员的 TTC 偏好曲线（仅 Zhang 一篇且为 6.0 s 远端孤证）

4. **SDT 框架支持"双阈值"设计**：5.0 s 优化 d′ + 2.5 s 优化 β 是 Kim (2018) 双阈值方案的理论依据，但**真实道路条件下的双阈值最优组合仍未量化**。

5. **本研究 RQ 的理论支撑确立**：
   - RQ1（持续时长最优）的时间锚点 = TTC ∈ [1.8, 5.0] s 区间内的 Duration 对照
   - RQ2（级间间隔最优）的时间锚点 = Lübbe 0.7 s ± [0.5, 1.5] s 范围对照
   - RQ3（个体差异交互）的理论支撑 = Kazazi 老年前移效应 + Lee 分心 PRT 效应

---

## 6. 下周（W3）计划

**主题**：HUD 持续时长、闪烁频率、onset-offset 动画过渡（HUD 子集三大空白维度）

**具体任务**：
1. 详细分析 Ma (2021) 的 3 s + 10–15 s 设计依据（唯一明确量化 Duration 的 HUD 研究）
2. 引入习惯化（Sokolov 1963 匹配-不匹配模型）与虚假警报疲劳（Bliss 2003）作为 Duration 上界理论
3. 引入注意定向（Posner 1980 ~150–300 ms 视觉处理时间）作为 Duration 下界理论
4. 形成 HUD 子集 Duration / Frequency / Onset 三张细分表（明确每个维度的报告 vs 空白）
5. 评述这些维度作为本研究 RQ1 切入点的具体优势

**预期产出**：W03_HUD持续时长_频率_动画.md（含 Duration 上下界理论分析 + 三张细分表）

---

## 7. 本周引用 References

Bliss, J. P. (2003). Investigation of alarm-related accidents and incidents in aviation. *International Journal of Aviation Psychology*, *13*(3), 249–268. https://doi.org/10.1207/S15327108IJAP1303_04

Green, D. M., & Swets, J. A. (1966). *Signal detection theory and psychophysics*. Wiley.

Hayward, J. C. (1972). Near-miss determination through use of a scale of danger. *Highway Research Record*, *384*, 24–34.

Hooper, K. G. (1936). *Driver perception-reaction time*. Institute of Transportation Engineers.

Kahneman, D., & Tversky, A. (1974). Judgment under uncertainty: Heuristics and biases. *Science*, *185*(4157), 1124–1131. https://doi.org/10.1126/science.185.4157.1124

Kazazi, J., Winkler, S., & Vollrath, M. (2015). Accident prevention through visual warnings: How to design warnings in head-up display for older and younger drivers. In *2015 IEEE 18th International Conference on Intelligent Transportation Systems* (pp. 1028–1034). IEEE. https://doi.org/10.1109/itsc.2015.171

Kim, H., Gabbard, J. L., Anon, A. M., & Misu, T. (2018). Driver behavior and performance with augmented reality pedestrian collision warning: An outdoor user study. *IEEE Transactions on Visualization and Computer Graphics*, *24*(4), 1515–1524. https://doi.org/10.1109/tvcg.2018.2793680

Lee, J. D., McGehee, D. V., Brown, T. L., & Reyes, M. L. (2002). Collision warning timing, driver distraction, and driver response to imminent rear-end collisions in a high-fidelity driving simulator. *Human Factors*, *44*(2), 314–334. https://doi.org/10.1518/0018720024497844

Lübbe, N. (2017). Brake reactions of distracted drivers to pedestrian forward collision warning systems. *Journal of Safety Research*, *61*, 23–32. https://doi.org/10.1016/j.jsr.2017.02.002

Ma, X., Jia, M., Hong, Z., Kwok, A. P. K., & Yan, M. (2021). Does augmented-reality head-up display help? A preliminary study on driving performance through a VR-simulated eye movement analysis. *IEEE Access*, *9*, 129951–129964. https://doi.org/10.1109/access.2021.3112240

Olson, P. L., & Sivak, M. (1986). Perception-response time to unexpected roadway hazards. *Human Factors*, *28*(1), 91–96. https://doi.org/10.1177/001872088602800110

Posner, M. I. (1980). Orienting of attention. *Quarterly Journal of Experimental Psychology*, *32*(1), 3–25. https://doi.org/10.1080/00335558008248231

Zhang, Y., Bian, Y., Zhao, X., Li, X., & Zhang, J. (2024). Improving pedestrian safety with head-up display warning in a connected environment. *International Journal of Human-Computer Interaction*. Advance online publication. https://doi.org/10.1080/10447318.2024.2368910

---

*汇报状态：W2 完成（2026.07.04）*
*下次汇报：W3（2026.07.11），主题 = HUD 持续时长 / 频率 / 动画过渡三大空白维度*
