# 基于多功能预警的前向碰撞预警系统预警滞后时间改进
**Improvement of warning lag time in forward collision warning systems based on multifunctional warnings**

| 项 | 内容 |
|---|---|
| 作者 | Peachanika Thammakaroon、Poj Tangamchit；均属泰国国王科技大学（King Mongkut's University of Technology Thonburi, KMUTT）控制系统与仪器工程系（Department of Control System and Instrumentation Engineering），曼谷 |
| 年份/期刊 | 2012，*2012 IEEE International Conference on Vehicular Electronics and Safety (ICVES 2012)*，2012-07-24 至 07-27，土耳其伊斯坦布尔，pp. 146–150（IEEE，非开放获取） |
| DOI | 10.1109/icves.2012.6294314 |
| 本地 PDF | `/home/gezhuocheng/HUD/papers/76_2012_Improvement_of_warning_lag_time_in_forward_collision_warning_systems_based_on_mu.pdf` |
| 本地全文 | `/home/gezhuocheng/HUD/extracted_text/76_2012_Improvement_of_warning_lag_time_in_forward_collision_warning_systems_based_on_mu.txt` |
| 引用数 | 论文未明确报告（manifest 中 `cited_by` 为 null，Crossref 未返回数值） |
| 证据等级 | **A**（就时间参数而言：提供了「实车实测的 warning lag time = +1.47 s / +1.32 s」这一其他文献极少给出的量化值，且提出了 warning lag time 这一评价指标本身）；就人因证据而言为 **B**（仅一名驾驶员、30 min 实车） |
| 资料来源 | 全文精读 |
| 资助 | 泰国高等教育委员会 Higher Education Research Promotion and National Research University Project of Thailand |

## 一、研究背景与问题

### 1.1 领域现状
- 事故主因来自人为失误，因此主动安全与智能驾驶辅助是必然方向。驾驶员分心的常见来源包括来电干扰、疲劳与困倦。
- FCW 系统通常用多种传感器测量与前车的距离、速度、加速度（引 [1][2]），再代入车辆运动学模型预测潜在碰撞。
- **原文关键陈述**：「In general, forward collision warning signals can be issued within **the last few seconds before crash, called the critical moment**. This may not be enough for sluggish drivers to avoid a crash in tight situations.」
- 提升「预警提前期（pre-warning time）」的既有路线：
  - Nakaoka 等（引 [3]）把**驾驶员制动反应时**与**相对安全距离余量**纳入运动学模型以增加 pre-warning time；
  - **DCA（Deceleration for Collision Avoidance，避撞所需减速度）**被计算并作为前向碰撞风险指标（引 [4][5]，Hiraoka 等 2009、Takada 等 2011）；
  - 组合法：Chih-Li Hou 等（引 [6]）把 FCW 与车道偏离预警基于图像处理与车辆运动学模型集成。

### 1.2 研究缺口
原文明确两点：
1. 上述工作在**准确率（accuracy）**上取得改进，但**没有展示它们把 pre-warning time 提高了多少**——而 pre-warning time 才是评估 FCW 性能的重要指标。
2. 有一项工作（引 [7]，THASV-II 平台）比较了系统报警信号与驾驶员制动信号以说明其提高了 pre-warning time，但**并未真正测量 pre-warning time**。
3. 更根本的方法学缺口：**pre-warning time 的定义依赖「碰撞时刻」，只能在驾驶模拟器中测量（因为可以仿真碰撞），无法在真实道路实验中测量。**

### 1.3 核心研究问题
1. 提出一个**可在真实驾驶实验中测量**的性能指标 —— **warning lag time（预警滞后时间）**；
2. 通过增加预警功能层（多功能预警），把 FCW 的作用阶段从「第 3 级临界时刻」向前推到「第 2 级开放条件」，从而改善 warning lag time；
3. 在真实道路上验证 FCW 单独 vs FCW + LW 的 warning lag time 与准确率。

## 二、研究方法

### 2.1 被试与样本
- **正常驾驶员（normal drivers）**在真实道路上驾驶；原文表述为「We performed real driving experiments with normal drivers」，但实验部分只描述**一位驾驶员、一次 30 分钟测试**（"the driver does not know the output of the systems"，单数）。**具体被试人数、年龄、驾龄：论文未明确报告。** 这是本文最严重的报告缺陷。
- **关键实验控制**：**驾驶员不知道系统的输出**，以保证其驾驶行为独立于系统输出。

### 2.2 实验设计
- **对照设计（两个系统条件）**：① FCW 单独；② FCW + LW（location-based warning，基于位置的预警）。
- **两个性能参数（因变量）**：**warning lag time（s）** 与 **system warning accuracy（%，分为 correct / false positive / false negative）**。
- **五级碰撞预防层级（five levels of crash prevention，Fig. 2）**——本文的理论框架：

| 级别 | 名称/状态 | 描述（原文） |
|---|---|---|
| **Level 1** | 最小碰撞风险 | 驾驶员专注驾驶并严格遵守交通法规，事故可能性极低 |
| **Level 2** | **开放条件（open condition to collision）** | 通常由违反交通规则造成；若不采取合适动作回到 Level 1，将进入 Level 3 |
| **Level 3** | **临界时刻（critical moment）** | 驾驶员若有良好操控技巧（急制动或利落转向）仍可避撞 |
| **Level 4** | 碰撞不可避免、碰撞前瞬间 | — |
| **Level 5** | 碰撞后时段 | — |

- **原文明确：典型 FCW 系统工作在 Level 3（临界时刻），即碰撞前约 2–3 秒。**（"typical FCW systems operate on stage 3, the critical moment. It is the moment about **2-3 seconds** before the impact."）
- 改进思路：把工作在 **Level 2** 的预警系统与 FCW 组合，防止驾驶员进入 Level 3，从而提高 pre-warning time。选用**基于位置的预警（LW）**作为 Level 2 系统，理由是「它是工作在 Level 2 的最可靠系统，因为其预警来自**静态环境**」。
- 组合方式：**两系统独立并发运行，预警输出直接相加（summing up the warning outputs from both systems）**（Fig. 3）。

### 2.3 实验材料与设备
三个传感器装于测试车（Fig. 8）：
1. **激光测距仪（laser rangefinder）**：装于挡风玻璃、朝前，测量与前车的跟车距离；
2. **GPS 模块**：获取车速、位置（经纬度）与航向（heading）；
3. **力敏电阻 FSR（force sensing resistor）**：装于制动踏板，获取驾驶员的**真实制动动作**。原文明确：**FSR 仅用于性能评估，正常运行的预警系统不需要它。**
- 三者接入主计算机记录与处理数据。

### 2.4 关键公式与阈值

**（1）FCW 判据 —— 估计到前车的时间 T<sub>s</sub>**

> ***T*<sub>s</sub> = D / v**    …… (1)

其中 D = 当前跟车距离，v = 本车当前速度。
- **模型简化假设（原文明确）**：**本车加速度与前车/障碍物速度均假定为零**，以尽量简化模型。
- **阈值设定（关键）**：预警判据来自防御性驾驶的**「两秒法则（two-second rule）」**——即驾驶员应至少保持距前车 2 秒的跟车距离，当 T<sub>s</sub> 小于 2 秒阈值时报警。
- **但原文明确下调了该阈值**：「we found that **2 seconds were not suitable for roads in Bangkok, which has quite aggressive driving habit. Therefore, we reduced the threshold down to 1.6 seconds.** This number came from trial and error in real driving experiments, in which we found that this value is the most suitable.」→ **实际采用 T<sub>s</sub> 阈值 = 1.6 s。**

**（2）LW 判据 —— 位置预警**

> **LW = 1，若 (d < d<sub>th</sub>) AND (v > v<sub>th</sub>) AND (|h − h<sub>D</sub>| < h<sub>th</sub>)；否则 LW = 0**    …… (2)

其中：
- d = 到最近事故热点的距离；**d<sub>th</sub>（预警距离范围）= 30 m**；
- v = 当前速度；**v<sub>th</sub>（速度限值）= 30 km/h**；
- h = 车辆航向；h<sub>D</sub> = 从车辆位置指向数据库中最近热点的角度；h<sub>th</sub> = 航向差阈值（**论文未明确报告 h<sub>th</sub> 的数值**）。
- 判据含义（Fig. 4）：若 |h − h<sub>D</sub>| 不超过 h<sub>th</sub>，说明车辆**正在驶向**热点（h 与 h<sub>D</sub> 同向）；反之则为**驶离**热点（h 与 h<sub>D</sub> 反向）。
- **事故热点（accident hotspots）数据库**：每个数据点含**纬度、经度、速度限值、航向**四项。热点定义为「可能导致事故的危险地点，例如**斑马线（zebra cross）、交叉口、危险弯道**等」。
- **LW 的语义**：当驾驶员**以高速驶向危险地点**时预警，使其在到达热点前有所准备并减速。原文举例：车辆可能在无侧向来车时顺利通过交叉口，但**这一动作本身风险很高**；若侧方有车驶来，情境将从 Level 2 转为 Level 3，驾驶员随后不得不急刹。

### 2.5 warning lag time 的定义与测量方法（本文方法学核心）

**定义（原文）**：
> **warning lag time = 「系统发出预警」与「一名没有主动预警系统的正常驾驶员执行制动」之间的时间间隔**（"the time period between the issue of warning and the execution of brake by a normal driver who has no active warning systems"）。

**与 pre-warning time 的区别（Fig. 5）**：
- **pre-warning time** = 预警发出与**碰撞冲击时刻**之间的时间间隔 → 只能在模拟器中测（可仿真碰撞）；
- **warning lag time** = 预警发出与**真实驾驶员制动动作**之间的时间间隔 → 可在真实道路上测。
- **符号约定（Table I 注）**：**「−」表示预警滞后时间发生在真实制动之前；「+」表示发生在真实制动之后。**

**重要观察（原文）**：「In typical FCW systems, **the warnings usually come after brakes from alert drivers** because human perception is better than current sensing technology. As a result, human drivers can perceive more road environments and react quicker than a machine.」→ **典型 FCW 的报警晚于警觉驾驶员的自发制动。**

**测量步骤（三步，基于互相关）**：
1. 计算**真实制动信号**与**系统输出信号**之间的**互相关（cross-correlation）**；
2. 在互相关输出的**中部附近寻找局部极大值（local maxima）**（因为时延不会偏离中心 delay = 0 s 太远）；
3. **warning lag time = 互相关输出中心与局部极大值之间的距离**（Fig. 7）。
- 判读规则：局部极大值在中心**右侧** → 系统预警发生在真实制动**之前**（有正的 pre-warning time）；在**左侧** → 系统预警**滞后于**真实制动。
- 前提假设：**系统预警信号的模式与真实制动信号的模式相似，只是存在一个短的时间平移**。

### 2.6 任务与流程
- 在**城市道路真实驾驶 30 分钟**；
- 测试路线包含 **28 个事故热点**；
- 分别测试 FCW 单独与 FCW + LW 两个条件；
- 准确率计算前，**先把系统预警的时间轴按 warning lag time 平移**，再与真实制动比对（Fig. 9）。

## 三、关键指标与测量

| 指标 | 类型 | 操作化定义 |
|---|---|---|
| **warning lag time（s）** | **时间类（核心）** | 系统预警与无预警驾驶员真实制动之间的时间差，用互相关法测得；「+」= 预警晚于制动 |
| **pre-warning time（s）** | 时间类（对照概念） | 预警与碰撞冲击之间的时间差；本文因真实道路无碰撞而**未测量** |
| **T<sub>s</sub>（s）** | 时间类（判据） | D/v，估计到前车的时间；阈值 1.6 s |
| accuracy — correct（%） | 准确性 | 系统预警与真实制动一致的比例 |
| accuracy — false positive（%） | 准确性 | 系统报警但驾驶员未制动 |
| accuracy — false negative（%） | 准确性 | 驾驶员制动但系统未报警 |

## 四、主要结果与发现

### 4.1 主结果（Table I，原样转录）

| 预警系统 | **warning lag time (s)** | Correct (%) | False positive (%) | False negative (%) |
|---|---|---|---|---|
| **FCW** | **+1.47** | **79.54** | 10.09 | 10.37 |
| **FCW with LW** | **+1.32** | **79.01** | 10.66 | 10.33 |

（表注：「−」与「+」分别表示预警滞后时间发生在真实制动之前与之后。）

### 4.2 结论性数值
- **FCW 单独的输出平均比真实制动晚 1.47 s**；
- **FCW + LW 的 warning lag time 为 1.32 s**；
- → **加入 LW 使 pre-warning time 改善 0.15 s**（原文：「can help improve the pre-warning time for **0.15 sec.** (from the pre-warning time +1.47 sec. to the pre-warning time +1.32 sec.)」）。
- **准确率几乎持平**：FCW+LW 相对 FCW 单独，correct 下降约 **0.53%**（79.54% → 79.01%）；false positive 上升 0.57 个百分点，false negative 基本不变。
- **FCW 假阴性的主因（原文明确）**：测试路段**交通拥堵**——车辆停止时驾驶员仍把脚放在制动踏板上，这被计为一次制动动作，而车辆不动时 FCW 不会报警。

### 4.3 结论（原文 Conclusion）
在碰撞预防层级的**第 2 级**加入预警系统，可以**把 pre-warning time 提高 0.15 s，而准确率仅小幅下降**。

> 本文**未做任何统计检验**（无 F/t/p/效应量/置信区间）；结果为单次 30 min 实车的描述性数值。

## 五、对 AR-HUD 行人预警时空设计的启示

### 5.1 时间参数（本课题核心，穷尽转录）

**A. warning lag time（本文独有的关键量）**
- **FCW 单独：+1.47 s**（系统报警晚于真实驾驶员制动 1.47 s）；
- **FCW + LW：+1.32 s**；
- **改善量：0.15 s（150 ms）**；
- **符号约定**：「+」= 报警在真实制动之后；「−」= 报警在真实制动之前。
- **测量法**：真实制动信号与系统输出信号的**互相关**，取中部局部极大值与中心的距离。

**B. TTC / 跟车时间阈值**
- **判据公式：T<sub>s</sub> = D / v**（式 1），其中 D = 跟车距离，v = 本车速度；**假定本车加速度 = 0、前车速度 = 0**。
- **原始阈值：两秒法则（two-second rule），T<sub>s</sub> < 2 s 报警**；
- **实际采用阈值：T<sub>s</sub> = 1.6 s**（因曼谷驾驶习惯激进，2 s 不适用；1.6 s 由实车试错确定为最合适）。
- **典型 FCW 的作用时窗（原文明确）**：**碰撞前约 2–3 秒（Level 3 临界时刻）**；另一处表述为**「碰撞前 2–5 秒内」**（"Since FCW systems are activated at a critical moment, **within 2-5 seconds before accidents**, timing is a crucial parameter"）。

**C. 位置预警（LW）的时空阈值**
- **速度阈值 v<sub>th</sub> = 30 km/h**；
- **热点预警距离范围 d<sub>th</sub> = 30 m**；
- **航向差阈值 h<sub>th</sub>：论文未明确报告数值**；
- 由 v<sub>th</sub> 与 d<sub>th</sub> 可推算 LW 的**等效提前期**：以 30 km/h（8.33 m/s）行驶时，30 m 对应约 **3.6 s** 的提前期（本摘要推算，原文未给出）。这解释了 LW 为何能把预警前移——但**改善量仅 0.15 s，远小于 3.6 s**，说明两系统输出简单相加时 LW 的贡献被严重稀释。

**D. 驾驶员反应时基线**
- **论文未明确报告 RT/BRT 的绝对数值**。本文只测「系统报警相对于真实制动的时间差」，不测驾驶员从危险出现到制动的时间。
- **分心条件下的反应时增量**：**论文未明确报告**（虽在引言中把分心列为事故主因，实验中未设分心条件）。

**E. 预警持续时长 / 升级间隔 / 减速度阈值**
- 预警持续时长：**论文未明确报告**；
- 预警模态（视觉/听觉/触觉）：**论文未明确报告**；
- 分级升级间隔：**论文未明确报告**（两个系统的输出是「相加」而非按时间升级）；
- 减速度阈值：**论文未明确报告**（引言提到 DCA 指标但本文未采用）。

**F. 时序结构（分级）**
- **五级碰撞时间线：Level 1 安全 / Level 2 开放条件 / Level 3 临界时刻（碰撞前 2–3 s）/ Level 4 碰撞不可避免 / Level 5 碰撞后**。
- **设计要义**：**FCW 只覆盖 Level 3；要真正提前预警，必须增加一个覆盖 Level 2 的功能层**。本文选择的 Level 2 触发条件是「静态环境」的（位置 + 速度 + 航向），因为静态环境判据最可靠。
- 未来工作（原文）：第二条改进路线是**用通信信道促进多车协同驾驶（cooperative driving）**，即分布式感知以扩大传感器范围。

### 5.2 空间参数
- **呈现位置 / 空间参照系**：**论文未明确报告**（未说明报警是视觉、听觉还是 HUD，也未说明位置；仅有「Alarm / 系统输出」抽象信号）。
- **视场角 FOV / 偏心度**：不适用（论文未明确报告）。
- **图形形态、颜色、透明度、动效、闪烁频率与占空比**：**论文未明确报告**。
- **可迁移的空间量**：
  - **激光测距仪安装位置：挡风玻璃处、朝前**（这与 AR-HUD 的视点位置相近，对「传感器视角 = 驾驶员视角」的 AR 配准有参考意义）；
  - **事故热点预警半径 30 m**；
  - **热点类型明确包含「斑马线（zebra cross）」** —— 这是本文与**行人**预警的唯一直接接口：**斑马线可作为行人风险的静态先验（static prior），在 Level 2 就预置 AR-HUD 的行人注意提示，而不必等待动态检测到行人**。

### 5.3 可直接写入设计规范的条目
1. **若**要评估 AR-HUD 行人预警系统在**真实道路**上的时机性能，**则**应采用 **warning lag time** 指标（系统报警与无预警驾驶员真实制动之间的时间差，用互相关法测量），而非只能在模拟器中获得的 pre-warning time（出处：Section IV、Fig. 5–7）。
2. **若**参照本文实测基线，**则**须承认**典型 FCW 的报警晚于警觉驾驶员的自发制动 1.47 s**；AR-HUD 若要产生真实增益，其触发时机必须比该基线提前 1.5 s 以上（出处：Table I）。
3. **若**只在 Level 3（碰撞前 2–3 s 临界时刻）报警，**则**对反应迟缓的驾驶员不足以避撞；应增设一个工作在 **Level 2（开放条件）**的功能层（出处：Section I、Section III.A）。
4. **若**要为 AR-HUD 增加 Level 2 层，**则**可采用**静态环境先验**（位置 + 速度 + 航向），因为静态环境判据最可靠；本文阈值为 **速度 > 30 km/h 且距热点 < 30 m 且航向指向热点**（出处：式 (2)、Section III.B）。
5. **若**目标场景为行人，**则**可把**斑马线**作为静态热点，在进入 30 m 范围内即预置行人注意提示，不必等动态行人检测（出处：Section III.B 对 accident hotspots 的定义；此条为基于原文热点类型的推断应用）。
6. **若**采用「两秒法则」作为跟车判据，**则**必须按当地驾驶文化标定：本文在曼谷把阈值从 **2.0 s 下调至 1.6 s**（出处：Section II）。**这条对我们做中国城市场景的阈值本地化极有参考价值。**
7. **若**把两个预警层「输出相加」，**则**提前量增益会被严重稀释：LW 理论提前期约 3.6 s（30 m / 30 km/h），实际仅换来 0.15 s 的 warning lag time 改善（出处：Table I + 本摘要推算）。因此**分级预警应设计显式的层间时序逻辑，而非简单叠加**。

## 六、本文局限性与未来工作
1. **样本严重不足且报告缺失**：未报告被试人数、年龄、驾龄；实验描述指向**单一驾驶员、单次 30 min 行驶**。**因此 1.47 s / 1.32 s 应视为个案量级参考，而非群体均值。**
2. **无统计检验**：0.15 s 的改善与 0.53% 的准确率下降均无显著性检验，无法排除测量噪声。
3. **运动学模型过度简化**：式 (1) 假定**本车加速度为零、前车速度为零**——这在跟车场景中是明显不成立的假设，会系统性低估危险（前车运动时 T<sub>s</sub> 被低估或高估取决于相对速度方向）。
4. **交通拥堵污染数据**：作者自承假阴性主要来自「停车时驾驶员仍踩着刹车」的误计，说明制动信号的操作化定义不够严谨（未做停车状态排除）。
5. **互相关法的前提可疑**：假定「系统预警模式与真实制动模式相似、仅存在时间平移」；在报警与制动事件数量不匹配时（FP 10%、FN 10%）该假设会带来偏差。
6. **HMI 完全缺失**：预警的模态、位置、时长、强度全未定义，无法直接迁移到 HUD 设计。
7. **热点数据库依赖**：LW 完全依赖预先采集的 28 个热点数据库，对未收录地点无效；且未讨论数据库维护与 GPS 精度问题。
8. **未来工作（原文明确）**：通过**车间通信信道实现协同驾驶（cooperative driving）**，用分布式感知扩大传感范围，作为第二条提升 pre-warning time 的路线。

## 七、与本课题的关联与引用建议

- **可用于章节**：
  - 「预警时机评价指标」方法学小节的**核心引文**——warning lag time 的定义与互相关测量法，是我们做实车/半实车验证时唯一可用的时机指标；
  - 「分级预警时序结构」章：五级碰撞时间线（Level 1–5）与「FCW 只覆盖 Level 3」的论断，可直接作为我们论证「AR-HUD 需要早级 + 晚级双层预警」的框架；
  - 「阈值本地化」小节：两秒法则从 2.0 s 下调到 1.6 s 的案例；
  - 「静态先验用于行人预警」小节：斑马线作为热点。
- **与已收录文献的一致之处**：
  - 与 **idx 72（Chen 2013）** 高度一致：72 采用**临界 TTC = 1.5 s**，本文采用 **T<sub>s</sub> 阈值 = 1.6 s**，两者几乎重合；且两文都用 5 级分级（72 为 Level 0–4，本文为 Level 1–5，语义不同但层数相同）。
  - 与 **idx 72** 的时延预算呼应：72 推算「驾驶员反应时 0.74–1.17 s + 制动压力建立 0.30–0.75 s = 1.04–1.92 s」，与本文实测 warning lag time **1.47 s** 落在同一区间内。**这一交叉验证给出一个重要解读：本文观测到的 1.47 s 滞后，很可能主要不是系统故障，而是「人的感知—动作链本身就比机器的检测—判定链更快」的自然结果**（本文自己也这样解释：human perception is better than current sensing technology）。
  - 与 **idx 74（Abe 2006）** 的关键呼应：Abe 证明**报警只要晚于驾驶员自身第一反应（松油门时点，均值 0.72 s）就会被判为「晚报警」、信任从 7.3 跌到 4.3**。本文实测报警晚于真实**制动** 1.47 s（比松油门更晚），**因此按 Abe 的判据，本文的 FCW 必然全部落在「被感知为晚报警」的区间内**。两文合读给出一个强命题：**当前实车 FCW 的报警时机普遍位于「被感知为晚」的区域，这可能是 FCW 主观评价不佳的结构性根因。** 这是本批次最有价值的跨文献推论之一，建议写入时间参数专题分析。
- **与已收录文献的冲突之处（必须显式指出）**：
  1. **与 idx 71（Zhang 2015）的实然—应然冲突**：71 要求预警**至少在碰撞前 3.0 s、最好 3.0–4.0 s** 发出；本文实测的系统报警却**晚于真实制动 1.47 s**，而真实制动本身通常已在碰撞前 1–2 s 区间。也就是说，**本文系统的实际报警时机比 71 的建议值晚了数秒量级**。边界条件分析：
     - 71 是**驾驶模拟器**中由实验者**精确编排**的报警时刻（预设为距冲突点 2.5–5.5 s），是「理想触发」；本文是**真实道路上由传感器与算法实时判定**的报警时刻，受传感范围、算法保守性、模型简化（假定前车速度为零）三重限制。
     - 因此两者的差距不是结论矛盾，而是**「人因上的应然阈值」与「工程上的实然能力」之间的差距**。AR-HUD 设计规范中必须显式列出这个差距，并说明其对感知链路时延预算的要求。
  2. **与 idx 72 的阈值定位冲突（同 72 摘要中已述）**：本文/72 的 1.5–1.6 s 是「已进入危险」的判据线，而 70/71/78 的 3–4 s 是「首次告知性预警」的时机。**两类阈值不应混用**：AR-HUD 的早级应取 3–4 s（甚至 5 s），晚级/危险级取 1.5–1.6 s。
  3. **与「早预警提升安全边际」的证据方向不一致处**：本文加入 Level 2 预警后，pre-warning time 仅改善 **0.15 s**，而 idx 71 显示预警从 2.5 s 提前到 5.5 s 可把最大减速时刻余隙从 33.24 m 拉到 59.49 m。本文的微弱增益提示：**「简单叠加两个预警层」并不能有效兑现早预警的理论收益**，必须有显式的层间时序编排。
- **引用注意**：
  - 引用 **1.47 s / 1.32 s / 0.15 s** 时，必须注明**样本极小（近似单一驾驶员、单次 30 min 城市道路、曼谷、含拥堵路段）、无统计检验**，只能作为量级参考；
  - 引用 **1.6 s 阈值**时须注明其来源是「针对曼谷激进驾驶习惯的实车试错标定」，不是普适值；
  - warning lag time 这一**指标本身**是本文最可靠、最值得引用的贡献，与具体数值的可靠性应分开评价。

> **Takeaway**：实车实测显示典型 FCW 的报警**比真实驾驶员制动晚 1.47 s**（跟车阈值 T<sub>s</sub> = D/v = 1.6 s，从两秒法则下调）；把预警层从「Level 3 临界时刻（碰撞前 2–3 s）」扩展到「Level 2 开放条件（距热点 30 m 且车速 > 30 km/h）」后仅改善 **0.15 s**，准确率从 79.54% 微降至 79.01%。
