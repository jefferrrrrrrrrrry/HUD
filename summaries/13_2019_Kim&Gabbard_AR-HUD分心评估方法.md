# 评估车载增强现实抬头显示对驾驶员的分心潜力
**Assessing Distraction Potential of Augmented Reality Head-Up Displays for Vehicle Drivers**

| 项 | 内容 |
|---|---|
| 助手元数据中标注的作者 | Hyungil Kim, Joseph L. Gabbard |
| 助手元数据中标注的期刊 | *Human Factors: The Journal of the Human Factors and Ergonomics Society*, 2019 |
| 助手元数据中标注的 DOI | 10.1177/0018720819844845 |
| 本地 PDF | `/home/gezhuocheng/moe/HUD/papers/13_2019_Assessing_Distraction_Potential_of_Augmented_Reality_Head-Up_Displays_for_V.pdf` |
| **实际从 PDF 抽取的文本内容**所指向的论文 | Nayara de Oliveira Faria（Virginia Tech，导师 Joseph L. Gabbard）发表的 **IEEE VR Workshops 2020 Doctoral Consortium** 短文 "Evaluating Automotive Augmented Reality Head-up Display Effects on Driver Performance and Distraction"，DOI 10.1109/VRW50115.2020.00128。 |
| 引用数 | 论文未明确报告 |

> **说明**：本份笔记**以本地实际抽取到的文本内容为唯一依据**（按任务要求"所有数据必须来自论文全文"），即 Faria 2020 IEEE VR Workshops Doctoral Consortium 论文。该文本与 helper 元数据所示的 Kim & Gabbard 2019 Human Factors 论文（"Assessing Distraction Potential of Augmented Reality Head-Up Displays for Vehicle Drivers"）虽题目相近、Gabbard 是共同导师，但具体作者、期刊、研究阶段不同，可能是同名/同源的相关博士工作。下文严格反映抽取文本中的事实，不引入未在文本中出现的数据。

## 一、研究背景与问题

### 1.1 领域现状
- AR-HUD 在汽车领域日益成熟，FOV 与显示深度都在扩展，使图形可以从风挡固定式（screen-fixed）延展到 conformal（与真实世界对象锚定）显示；
- AR 图形与真实世界视觉刺激的"认知—感知分离"越来越难量化；
- 现有 UI 评估方法不足以衡量 AR-HUD 对人因绩效的整体影响——因为 AR 图形不仅在环境中，**它本身就是环境的一部分**（visually integrated into the primary task space）；
- 两类核心心理-知觉现象需要被纳入 AR-HUD 评估：
  - **Inattentional Blindness（无意视盲）**——看而不见，注意被吸引时漏看其他重要信息（Simons & Chabris 1999, Neisser 1979）；
  - **Cognitive Tunneling（认知隧道）**——心理资源被不自主固定在某一信息源，忽略其他线索（Wickens, Ververs & Wickens 2000）。
- 现有 NHTSA / Alliance of Automobile Manufacturers 标准（"Driver Focus" 2006）规定单次注视 HUD ≤ 20 s 即可，但 Gabbard 等（2017）的研究提示 AR-HUD 可能允许更长的注视而不损害绩效——**20 s 阈值需要重新审视**。

### 1.2 研究问题（作者明确列出）
- **RQ**："当 AR-HUD 用户界面在视觉上与主任务空间整合时，评估其对驾驶员绩效影响的最佳方法是什么？"
- 子问题：
  - Q1：驾驶员**安全地**注视 AR-HUD 的时长上限是多少？
  - Q2：驾驶员**实际选择**注视 AR-HUD 的时长是多少？
  - Q3：无意视盲与认知隧道是 AR-HUD 分心评估的最佳测量指标吗？
  - Q4：还有哪些 AR 知觉特性需要被纳入？
  - Q5：用何种方法可以验证 AR 任务的生态效度（从受控模拟器到真实道路）？

## 二、研究方法（提议四阶段）

### 2.1 被试与样本
- 该论文是**博士论坛提案**（doctoral consortium proposal），尚未给出最终样本量；
- 文本提到"a series of carefully designed user studies"将在 Virginia Tech Cogent 实验室开展；
- 论文未明确报告每阶段具体的 N、年龄、性别、驾龄等。

### 2.2 实验设计（四阶段）
- **阶段 1**：建立 AR-HUD 注视时长阈值（thresholds for AR HUD glance duration）；
  - 已完成 3 项人因实验，混合"广义心理物理任务"与"生态有效 AR-HUD 任务"；
  - 采用"random letter reveal"技术，系统性比较 2, 5, 10, 15, 20, 30, 40, 50 s 这八档持续注视时长对驾驶绩效的影响；
  - 同时设计两个生态有效次要任务——接收短信、从列表中选择——以测量驾驶员**自愿**注视 AR-HUD 的时长；
  - 数据分析尚在进行中（文本注明 "findings of this process are still at the analysis level"）。
- **阶段 2**：开发 **Central Detection Task (CDT)** 方法与指标，评估 AR-HUD 视觉负荷对**无意视盲**的影响；
  - CDT 已在过往研究中用于检测交通灯颜色变化、前车制动等中心视野事件的视盲（Caird 2008, Olaverri-Montreal 2012, Wolffsohn 1998）。
- **阶段 3**：开发 **Peripheral Detection Task (PDT)** 方法与指标，评估 AR-HUD 视觉负荷对**认知隧道**的影响；
  - PDT 通过测量"对偏心位置目标的检测率/响应时"反映认知选择性（Martens & Van Winsum 2000）；
  - 本研究将把目标直接放在道路场景上、设置不同偏心度水平（参 Huisingh 2003）。
- **阶段 4**：在 Virginia Smart Road 真实道路上联合验证 CDT + PDT，从模拟器外推到真实环境。

### 2.3 实验材料与设备（**有详细参数**——关键工程描述）

文本对实验台进行了清晰描述：
- **驾驶模拟器**：固定基座、中等保真，2014 Mini Cooper 前半车厢；
- **投影 FOV**：曲面投影，水平 **94°** 视野显示模拟道路场景；
- **侧后镜**：完整提供周围环境视野；
- **车速仪表**：7" Lilliput USB 监视器固定在方向盘正后方；
- **AR-HUD 硬件**：Pioneer Cyber Navi HUD，支持 conformal AR 图形；
  - 显示区像素 **780 × 260**；
  - AR-HUD FOV = **15°**；
  - 虚像距离 = **约 3 m**（与眼点距离）；
- **图形渲染**：X3D + Python 定制软件与模拟器集成，使 AR 图形实时锚定到 CG 道路场景；
- **关键差异**：与"用 VR 在虚拟环境中渲染 AR"的研究不同，本研究**把 AR 图形渲染到一个"售后市场" AR-HUD 上**，并对一个投影道路场景进行校准——以提升生态效度。

### 2.4 任务与流程
- Phase 1 已实施：8 档持续注视时长 × 两个生态次要任务；
- Phase 2/3 尚在提议阶段，作者征求关于 CDT/PDT 设计的反馈；
- Phase 4 拟在 Virginia Smart Road 上做联合验证。

## 三、关键指标与测量
- **行为/视线**：注视分配、单次注视时长、对中央/外围目标的检测率与反应时；
- **认知**：无意视盲发生率（CDT）、认知隧道（PDT）；
- **生态效度**：模拟器结果与真实道路结果的可迁移性。

## 四、主要结果与发现
- 由于这是博士论坛提案性文章，**尚未给出阶段 1 的最终统计结果**；文本仅给出阶段框架、装置参数与方法路径。
- 作者明确表态："Gabbard 等（2017）已暗示 AR-HUD 或可允许超出 20 s 的注视而不损害驾驶绩效"——这是后续阶段 1 想要量化验证的核心命题。
- 论文未明确报告均值、SD、F、p、η² 等统计数值。

## 五、对 AR-HUD 时空设计的启示

### 时间元素（出现时机 TTC、持续时长、分级间隔）
- **20 s 上限可能不适用于 AR-HUD**：这是本提案的核心立场。AR-HUD 因图形锚定于真实环境，注视它**不等于**离开主任务空间，因此传统 HDD 注视时长法则不一定能照搬。
- 测试档位 2/5/10/15/20/30/40/50 s——这是行业内最系统的"单次注视时长上限"实验设计之一，可借鉴。

### 空间元素（平面 2D）
- AR-HUD 图形分两类——**screen-relative**（屏幕坐标）vs **conformal**（与世界锚定）；
- 这一二分法是 AR-HUD 内容的基础维度，对应行人标注的"指示型 / 接触型"两类规范。

### 空间元素（立体：分布面 / FOV / 相对位置）
- **Pioneer Cyber Navi HUD**：FOV = 15°、虚像距眼点 3 m、780×260 像素——这是真实产品级 AR-HUD 的典型参数；
- 整车模拟器投影场景 FOV = 94°——为 AR-HUD（15°）在真实驾驶场景中所占的"小窗口"提供基线对比；
- 设计含义：AR-HUD 仅占道路视场 ~16%，行人标注图形需在这 15° 窗口内既可见又不遮挡关键路况。

### 设计原则与适用边界
- 原则 1：AR-HUD 不是"附加视觉刺激"，而是**集成进主任务空间**——评估方法必须改变（不能套用 HDD 评估范式）；
- 原则 2：必须同时评估"中心 + 外围"两类视觉事件——CDT + PDT；
- 原则 3：需引入 conformal 与 screen-fixed 两种图形类型的分类对照；
- 适用边界：本论文是方法学提议，**尚无具体行人事件的实验数据**，仅给出研究路线图与装置参数。

## 六、本文局限性与未来工作
1. 论文本身是博士论坛提案，缺乏完整实验数据；
2. 阶段 1 数据"在分析中"，未在本提案中报告；
3. 作者对 CDT/PDT 任务设计、AR 知觉特性的完备性、生态效度等问题征求同行反馈；
4. 未来工作即四阶段路线图——从模拟器到 Virginia Smart Road 真实道路。

## 七、与本研究主题（HUD/AR-HUD 行人标注的时间空间设计规范）的关联

虽然本文本身是方法学提案，但对行人 AR-HUD 标注综述有重要参考：

1. **时间维度规范**：注视时长 20 s 上限可能对 AR-HUD 偏严；AR-HUD 行人标注图形可适当延长持续时间（如 idx 9 的 3 s 或 idx 12 的"事件级触发"），不必受 HDD 时间约束。
2. **空间维度规范**：
   - AR-HUD 实际 FOV 仅 15°（虚像距 3 m）；行人标注图形不能超出此窗口，否则丢失；
   - Screen-fixed vs Conformal 二分对应行人标注的"指示箭头"vs"行人轮廓贴标"两条路线。
3. **评估方法学**：CDT（中心检测）+ PDT（外围检测）的二合一方法直接适用于"行人 AR 标注是否引发对其他危险的视盲/隧道效应"评估。
4. **生态效度阶段化**：从模拟器到 Smart Road 的四阶段路线，可作为行人 AR 标注研究从实验室走向现实的方法论模板。
5. **与 idx 9（无意视盲）的衔接**：本文系统提出 CDT/PDT 方法论框架，idx 9（叶明慧 2025）正是 CDT 方法的具体应用——行人冲入、红灯、前车制动三类中央目标。
6. **20 s 阈值再审视**：这一点对预警分级设计有直接意义——AR 行人标注可以"持续呈现至危险解除"而不必担心超过 HDD 时序限制，但仍需用 CDT/PDT 验证未引入新的隧道效应。

> **Takeaway**：本文是 AR-HUD 分心评估方法学的**奠基性博士论坛提案**——核心论点是"AR-HUD 因视觉整合属性，需用 CDT（中心检测，反映无意视盲） + PDT（外围检测，反映认知隧道）联合评估，传统 20 s 注视上限可能被打破"；并给出 Pioneer Cyber Navi HUD（FOV 15°、虚像 3 m、780×260 px）+ 94° 投影模拟器的实验台规范。这些方法学与硬件参数对行人 AR-HUD 标注的"时空规范实验设计"具直接借鉴价值。
