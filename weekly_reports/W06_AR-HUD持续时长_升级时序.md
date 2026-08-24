# 第 6 周汇报：AR-HUD 持续时长 + 升级时序专题

**汇报周次**：W6（2026.07.26 – 2026.08.01）
**汇报对象**：[导师姓名]
**汇报人**：[学生姓名]

---

## 1. 本周目标

承接 W5 完成的 AR-HUD 警告时机分析，本周聚焦 AR-HUD 子集**两个核心研究空白维度**：

1. AR-HUD 子集 7 篇明确报告 Duration 的研究详读
2. 多级警告升级时序专题分析（Lübbe 0.7 s 孤证 + Ma 2024 三色渐变 + Chen 2024 多目标分级）
3. 共形动画与运动跟随的时间特性分析
4. 形成 AR-HUD Duration / 级间间隔 / 共形动画 三张细分表
5. 评述 AR-HUD 阶段升级时序的研究空白严重程度（vs HUD 阶段对比）

W6 是 AR-HUD 子集深化的收束周，W7 起进入 HUD vs AR-HUD 对比阶段。

---

## 2. AR-HUD 子集 Duration 维度详读

### 2.1 Ma et al. (2021, idx 27) — 3 s + 10–15 s 速度自适应

**W3 已详细分析**，此处仅复习关键设计：
- 单条警告 3 s（车速 < 75 km/h）
- 紧急警告 10 s（75–100 km/h）/ 15 s（> 100 km/h）
- 作者引用 Wickens (2002) 多资源理论为依据

**AR-HUD 阶段意义**：Ma 2021 虽以"AR-HUD"为题，但其显示模式仍为传统屏幕固定 HUD，是 AR-HUD 阶段**唯一采用固定 Duration 而非"至危险解除"** 的研究——既是孤证又是 RQ1 的关键对照锚点。

### 2.2 Ye & Yin (2025, idx 09) — 3 s 固定（沿用 Ma 2021）+ 三平面定位

> Ye, M. H., & Yin, J. (2025). Spatial plane positioning of AR-HUD graphics: Implications for driver inattentional blindness in navigation and collision warning scenarios. *Electronics*, *14*(23), 4768.

**实验设计**：
- N = 不详（论文未明示）
- 测试三种空间面定位：垂直面 / 水平面 / 混合面
- **碰撞预警图形 Duration 固定为 3 s**（引用 Ma 2021 作为依据，作者解释"3 s 已被证实为适宜"）

**核心结果**：
- 垂直面在工作负荷与实用性 UX 上最佳
- 混合面在前车碰撞反应时与享乐性 UX 上最佳
- **未对 Duration 本身做操控**——3 s 是固定参数

**对本研究的意义**：
- Ye & Yin 是 AR-HUD 子集中**第二篇采用固定 Duration** 的研究，且 Duration 是 3 s——与 Ma 2021 形成"3 s 工程经验值"传递链
- 但 **Duration 仍未作为自变量被对照**，本研究 RQ1 仍是首次系统对照实验

### 2.3 Wang ARive (2025, idx 20) — 动态消失 + 5 m 几何阈值

**W5 已分析 TTC/TTMD 设计**，此处补 Duration 维度：
- 激活条件：$t_{min} \le 5 \text{ s}$ 且 $d_{min} < 5 \text{ m}$
- 撤销条件：$t_{min} > 5 \text{ s}$ 或 $d_{min} \ge 5 \text{ m}$（行人离开危险区）
- **典型 Duration**：动态变化，依赖行人运动；实测平均 2.7 s（论文 §4.3 报告）

**对本研究的意义**：
- Wang ARive 是"至危险解除（动态）"模式的典型代表
- 实测平均 Duration ≈ 2.7 s 与 Ma 2021 固定 3 s 高度接近——**提示 2.5–3.0 s 可能是 AR-HUD 行人预警的自然 Duration "中位值"**

### 2.4 Kim et al. (2018) Virtual Shadow — 完全动态

**W5 已分析 TTC 双阈值**，此处补 Duration 维度：
- Virtual Shadow 从触发开始持续显示
- 随驾驶员-行人空间关系动态更新（阴影长度 / 透明度变化）
- 直到危险解除（行人离开横穿区或车辆完成减速）

**对本研究的意义**：
- Kim 2018 是 AR-HUD 共形动态 Duration 的**经典范式**
- 没有"固定 Duration"概念——Duration 完全由几何决定

### 2.5 Ma et al. (2024) carpet — 风险变化的饱和度渐变

> Ma, J., Li, Y., & Zuo, Y. (2024). Design and evaluation of ecological interface of driving warning system based on AR-HUD. *Sensors*, *24*(24), 8010.

**实验设计**：
- 生态界面（EID）设计：地毯式（carpet）共形警告
- Phase 1：浅黄色渐变（早期预警）
- Phase 2：深黄色渐变最终变为浅红色（临界）
- 风险解除后区域面积与饱和度逐渐减小直至消失

**核心结果**：
- 风险感知时间平均缩短 **62.96%**（p < .001）
- 风险决策时间平均缩短 **34.57%**（p = .003）
- DALI 主观认知负荷与瞳孔直径显著降低

**对本研究的意义**：
- Ma 2024 carpet 是"动态消失 + 渐变饱和度"的代表
- **没有量化 Phase 1 → Phase 2 的级间时间**——仅以"风险增加"作为质性描述
- 这是 §3 升级时序分析的关键空白

### 2.6 Charissis et al. (2021, idx 26) — infotainment 的消息暂存策略

> Charissis, V., Falah, J., Lagoo, R., Alfalah, S. F. M., Khan, S., & Wang, S. (2021). Employing emerging technologies to develop and evaluate in-vehicle intelligent systems for driver support: Infotainment AR HUD case study. *Applied Sciences*, *11*(4), 1397.

**实验设计**：
- AR-HUD 信息娱乐场景（非行人预警，但 Duration 设计有借鉴）
- 在拥堵或恶劣天气下采用 **"消息暂存"策略**：消息延迟至安全时机（即 THW 充裕时）释放

**对本研究的意义**：
- Charissis 提出"基于驾驶任务复杂度的 Duration 调度"概念
- 这是 AR-HUD 阶段"自适应 Duration"的前置探索

### 2.7 Strle (2023) — 生理信号反馈环路

> Strle, G., Košir, A., Sodnik, J., & Stojmenova, K. (2023). Physiological signals as predictors of cognitive load induced by the type of automotive head-up display. *IEEE Access*, *11*, 87884–87898.

**实验设计**：
- 融合 HRV / EDA / 皮温 / 瞳孔多通道生理信号
- AR-HUD 认知负荷预测的最佳 AUC ROC = **0.98**（LGBM 分类器）

**对本研究的意义**：
- 为"基于生理信号的 Duration 实时调节"提供方法学基础
- 是未来博士阶段研究的延伸方向

---

## 3. 多级警告升级时序专题

### 3.1 Lübbe (2017) 0.7 s 孤证（再述）

**W1–W2 已分析**，此处汇总要点：
- 二级警告：TTC = 2.5 s 触发 L1（HUD 视觉提示 + 57 dBA 低音）→ TTC = 1.8 s 触发 L2（audio-visual + 64 dBA + 触觉脉冲）
- **级间间隔 = 0.7 s**
- Setting 4 仅 1 次碰撞，反应时 0.8 s（SD = 0.29）

**理论解释**（基于 W2 PIEV 与 SDT 框架）：
- L1（提示级）→ L2（临界级）的级间间隔需保证驾驶员有时间完成 **L1 感知 → L2 理解** 的认知阶段
- Posner (1980) 视觉处理时间 + 信息整合时间约 0.5–1.0 s
- **0.7 s 恰好落在该理论预测的中央位置**——可能并非偶然

### 3.2 Ma et al. (2024) — 绿/黄/红三色渐变（级间未量化）

承接 §2.5 Ma 2024 carpet 设计：
- Phase 1 绿色（预警）→ Phase 2 黄色（警告）→ 浅红色（临界）
- **级间转换基于风险数值（TTC / TTMD 等）而非固定时间间隔**

**关键问题**：Ma 2024 未报告 Phase 1 → Phase 2 的时间间隔，仅以"风险增加"作为质性描述。

### 3.3 Wang ARive (2025) — TTMD 二级

承接 §2.3：
- L1 预警级：$2 \text{ s} < t_{min} \le 5 \text{ s}$
- L2 临界级：$t_{min} \le 2 \text{ s}$
- **级间间隔在 TTMD 单位下为 3 s**

但 TTMD 不等于时间——TTMD 是"几何最接近时刻"。如果车辆与行人均以恒定速度运动，TTMD = 5 s 与 TTMD = 2 s 的真实时间间隔可能 < 3 s（因相对运动接近时 TTMD 下降加速）。

**关键问题**：Wang 报告的"3 s TTMD 间隔"在真实场景下的等效时间间隔需另行测算。

### 3.4 Chen et al. (2024) 多目标 — 颜色优先级分级（无级间时间）

> Chen, W., Song, C., Luo, J., Xu, Z., Li, H., Ma, S., Wang, Q., & Yang, Z. (2024). Priority design in multi-target AR-HUD warning: Evidence from eye movement and behavior of the novice driver. *IJHCI*.

**实验设计**：
- N = 45 中国新手驾驶员
- 三类警告模式：Equivalent（均等，所有目标同色红）/ Hierarchical（分级，红=最高优先 / 黄=次优 / 绿=低优）/ Baseline（无警告）
- 多目标场景：2–5 个同时出现的行人 / 车辆

**核心结果**：
- 分级警告反应时 **1083 ms** vs 均等警告 **1707 ms**（**−36%**, p < .001）
- 注视熵 Hs 从 1.92 降至 1.31（−32%）
- 注视转移熵 Ht 从 0.30 降至 0.18（−40%）
- **5 目标条件下分级优势消失**（TTFF 不显著），表明刺激密度饱和

**对本研究的意义**：
- Chen 2024 是 AR-HUD 多目标分级的关键证据
- **关键问题**：仍以"颜色"做分级，而非"时间"做分级——级间转换是空间的（红→黄）而非时间的（提前 0.7 s 触发）
- 提示本研究 RQ2 实验应**首次将"颜色分级"与"时间分级"解耦**

### 3.5 Yoon (2014) / Park (2013) — 三级框架（未量化阈值）

- Yoon (2014)：明确提出 "three threat level decided by the calculated TTC values"，但未量化各级 TTC
- Park (2013) ETRI Journal：同样为工程系统层面的三级预警提案

**对本研究的意义**：三级框架在工程层面已有共识，但人因层面**完全未量化级间时间**——本研究若考察三级警告即填补该空白。

---

## 4. 共形动画与运动跟随的时间特性

### 4.1 共形动画的子维度（W4 §5.3 已预热）

AR-HUD 阶段引入"运动跟随"后，时间设计从原 5 维拓展为：

1. 警告时机（TTC / Lead Time）
2. 持续时长（Duration）
3. 闪烁频率
4. onset-offset 动画过渡
5. 升级时序（级间间隔）
6. **跟随平滑度**（Refresh Rate / 阶跃 vs 平滑） ← AR-HUD 新增
7. **跟随延迟**（Latency） ← AR-HUD 新增

### 4.2 现有研究对共形动画的报告

| idx | 文献 | 跟随平滑度 | 跟随延迟 |
|---|---|---|---|
| 01 | Kim (2018) | Virtual Shadow 实时平滑 | 报告 ~50 ms |
| 08 | Wu (2024) | BW 行人位置实时跟随 | 未报告 |
| 20 | Wang (2025) | Red Carpet 实时贴地 | 报告 80 ms |
| 24 | Li (2025) | 信息冗余实时切换 | 未报告 |
| 40 | Chen (2024) | bounding box 实时贴行人 | 未报告 |

**结论**：跟随平滑度与跟随延迟报告率约 2/26 = 7.7%（仅 Kim 2018 与 Wang 2025 明确）。

### 4.3 共形动画对认知负荷的潜在影响

W5 §4 Kim & Gabbard (2019) 已警示：**视觉复杂度过高的共形警告引发注意隧道**。共形动画（特别是高更新频率 + 阶跃式更新）可能加剧此问题。

理论参考：
- Yantis & Hillstrom (1994) 视觉显著性：运动 stimuli 的注意捕获最强
- Wickens (2002) 多资源：动态共形占用"视觉空间"资源
- 推论：共形动画的更新频率应在 **30–60 Hz**（平滑感知）但避免高对比度阶跃跟随

---

## 5. AR-HUD 子集三张细分表（W6 核心产出）

### 5.1 AR-HUD Duration 维度细分表（7 篇明确报告）

| idx | 第一作者 (年) | Duration 数值 | 模式 | 与 Ma 2021 3 s 关系 |
|---|---|---|---|---|
| 09 | 叶明慧 (2025) | **3 s** | 固定（引用 Ma 2021） | 沿用 |
| 20 | Wang (2025) | 平均 **2.7 s** | 动态（TTMD 几何） | 接近 |
| 24 | Li (2025) | **未量化**（动态） | 雾天信息冗余 | – |
| 26 | Charissis (2021) | 暂存策略调度 | 自适应 | – |
| 27 | Ma (2021) | **3 s + 10–15 s** | 固定速度自适应 | 锚点 |
| 36 | Strle (2023) | 生理反馈调节 | 自适应 | – |
| 06 | Ma (2024) | 风险解除后渐变消失 | 动态 + 渐变 | – |

**关键发现**：AR-HUD 子集中明确量化 Duration 的研究均在 **2.5–3.0 s 附近**或"动态消失"模式——**没有任何研究对照不同固定 Duration 的差异**。

### 5.2 AR-HUD 级间间隔细分表

| idx | 第一作者 (年) | 级数 | 级间间隔 | 备注 |
|---|---|---|---|---|
| 14 | Lübbe (2017) | 2 | **0.7 s**（TTC 2.5 → 1.8） | HUD 阶段，AR-HUD 阶段唯一引用 |
| 06 | Ma (2024) | 2–3 | **未量化** | 颜色 / 饱和度渐变 |
| 20 | Wang (2025) | 2 | 3 s (TTMD 单位) | 几何阈值非时间 |
| 40 | Chen (2024) 多目标 | 3 | **未量化**（空间分级） | 颜色优先级非时间 |
| 18 | Park (2013) | 3 | **未量化** | 工程系统 |
| 05 | Yoon (2014) | 3 | **未量化** | 工程系统 |

**关键发现**：AR-HUD 阶段虽有多级警告出现，但**真正量化级间时间间隔的仍只有 Lübbe 0.7 s 一篇**——这正是本研究 RQ2 的核心研究空白。

### 5.3 AR-HUD 共形动画维度细分表

| idx | 第一作者 (年) | 跟随平滑度 | 跟随延迟 | onset-offset 过渡 |
|---|---|---|---|---|
| 01 | Kim (2018) | 实时平滑 | ~50 ms | 瞬时 / 渐变（未量化） |
| 08 | Wu (2024) | BW 实时跟随 | 未报告 | 瞬时 |
| 20 | Wang (2025) | 实时平滑 | 80 ms | Red Carpet 渐变铺开 |
| 21 | Huo & Alla (2025) | **闪烁** | 未报告 | 闪烁 |
| 06 | Ma (2024) | 饱和度渐变 | 未报告 | 渐变铺开 / 消失 |
| 其余 21 篇 | – | 未涉及 | 未涉及 | 未涉及 |

**关键发现**：共形动画维度报告率约 **5/26 = 19%**，且无统一报告标准。

---

## 6. 本周结论

1. **AR-HUD 子集 Duration 仍是核心空白**：7/26 篇报告，但所有数值集中在 2.5–3.0 s 或"动态消失"模式——**没有任何研究对照不同固定 Duration 的差异**。这强化了 W3 结论：本研究 RQ1 是首次系统对照实验。

2. **AR-HUD 阶段升级时序仍未量化级间时间**：Lübbe (2017) 的 0.7 s 仍是唯一明确级间时间的研究。Ma 2024 三色渐变、Wang ARive TTMD 二级、Chen 2024 多目标分级**均未量化级间时间间隔**。这强化了 W3 结论：本研究 RQ2 是首次量化级间时间对照实验。

3. **共形动画是 AR-HUD 引入的新时间维度**：跟随平滑度与跟随延迟报告率仅 ~8%，但**共形警告本身的优势依赖于这些动画特性**。本研究 §3 应明确控制共形动画的硬件参数。

4. **2.5–3.0 s 是 AR-HUD 行人预警 Duration 的"自然中位"**：Ma 2021 (3 s)、叶明慧 2025 (3 s)、Wang 2025 (动态平均 2.7 s) 三篇独立研究均指向该范围——本研究 RQ1 的固定 Duration 对照应**至少包含 2 s 与 3 s 两档**。

5. **W1–W6 HUD 与 AR-HUD 子集分析完成**：W7 起进入 HUD vs AR-HUD 对比阶段，把已识别的时间设计共识与空白系统化对照。

---

## 7. 下周（W7）计划

**主题**：HUD vs AR-HUD 时间设计对比 + 评估指标分类

**具体任务**：
1. 整合 W1–W6 已识别的 HUD 与 AR-HUD 子集证据，形成"对比矩阵"
2. 评估指标的分层（行为 / 眼动 / 主观 / 生理）
3. 共形 vs 屏幕固定的"时间-空间耦合"效应总结
4. 评述 AR-HUD 阶段相较 HUD 阶段的 4 项核心演进与 5 项遗留空白
5. 为 §2.2 与 §2.3 的桥接段提供素材

**预期产出**：W07_HUD与AR-HUD时间设计对比.md

---

## 8. 本周引用 References

Charissis, V., Falah, J., Lagoo, R., Alfalah, S. F. M., Khan, S., & Wang, S. (2021). Employing emerging technologies to develop and evaluate in-vehicle intelligent systems for driver support: Infotainment AR HUD case study. *Applied Sciences*, *11*(4), 1397. https://doi.org/10.3390/app11041397

Chen, W., Song, C., Luo, J., Xu, Z., Li, H., Ma, S., Wang, Q., & Yang, Z. (2024). Priority design in multi-target AR-HUD warning: Evidence from eye movement and behavior of the novice driver. *International Journal of Human-Computer Interaction*. https://doi.org/10.1080/10447318.2024.2439572

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

*汇报状态：W6 完成（2026.08.01）*
*下次汇报：W7（2026.08.08），主题 = HUD vs AR-HUD 对比矩阵*
