# 评估AR-HUD与风险水平对自动驾驶汽车用户体验的影响：基于真实驾驶模拟的结果
**Assessing the Impact of AR HUDs and Risk Level on User Experience in Self-Driving Cars: Results from a Realistic Driving Simulation**

| 项 | 内容 |
|---|---|
| 作者 | Seungju Kim、Jungseok Oh、Minwoo Seong（前三位并列第一）、Eunki Jeon（光州科学技术院GIST，融合技术学院）、Yeon-Kug Moon（韩国电子技术研究院KETI），Seungjun Kim（GIST，通讯作者，seungjun@gist.ac.kr） |
| 年份 | 2023年4月14日（接收1月22日，修订2月28日，录用3月3日） |
| 期刊 | Applied Sciences, Vol. 13, 4952 |
| DOI | 10.3390/app13084952 |
| 资助 | 韩国创意内容机构（KOCCA）项目R2020040058 |
| 伦理 | GIST IRB（Protocol 20210609-HR-61-02-02） |
| 本地TXT | `/home/gezhuocheng/moe/HUD/extracted_text/23_2023_Assessing_the_Impact_of_AR_HUDs_and_Risk_Level_on_User_Experience_in_Self-Drivin.txt` |

## 一、研究背景与问题

自动驾驶汽车（AV）已成主流研究方向，但**公众信任**仍是阻碍市场接受的关键障碍。AI模型的"透明度"被视作建立信任的核心要素，于是XAI（可解释AI）领域兴起：HUD是一种向驾驶员/乘客解释AI决策的可视化方式（Murugan 2022, Colley 2020）。

本研究基于Ajenaghughrure 2020的4级风险框架（Very High / High / Low / No Risk）与Morra 2019关于VR模拟驾驶辅助HMI设计的研究，**首次将"风险水平"和"AR-HUD信息提供"两个因素同时操控，并使用VR+运动平台合成真实事故场景**，量化UX变化。

**研究问题**：
- 风险水平如何影响驾驶员（实际为乘客）的GSR生理信号、Valence-Arousal主观情绪、信任、感知安全、态势认知？
- HUD信息提供能否系统性提升AV的UX？
- 生理与自报数据间相关性如何？

## 二、研究方法

### 2.1 被试

招募52名被试，平均年龄M=21.2，SD=3.49，男性25人女性27人，每人获约15美元报酬。最终因GSR异常或注释缺失，剩45人参与分析。

### 2.2 设计

**2×4×8因子设计**：
- **风险水平**：No Risk / Low Risk / Medium Risk / High Risk
- **HUD信息**：Information Given / Information Not Given
- 共**8个场景**，每场景约1分钟，**事件发生在结束前10秒**。
- 拉丁方法平衡呈现顺序。

**场景定义**：
- **No Risk**：AV正常行驶，无危险；
- **Low Risk**：AV未直接受冲击，路上突现物体导致急停（速度突变）；
- **Medium Risk**：AV受弱直接冲击（其他车辆轻微撞击）；
- **High Risk**：AV受强直接冲击（严重事故）；
- **Information Given**：HUD显示当前检测到目标的路径与信息；
- **Information Not Given**：HUD不显示任何信息。

### 2.3 设备/刺激规格

**VR+运动平台组合**：
- Unity游戏引擎构建虚拟环境；
- **Oculus Quest 2 VR HMD**：每只眼1832×1920分辨率，113.46° FOV，120 Hz刷新率；
- VR手柄用于Valence-Arousal自标注（前视VA面板，被试用摇杆移动黑点，自然语言情绪标签辅助）；
- **PS-3TM-LP550运动平台**：3自由度（heave/roll/pitch），载重550 kg；
  - heave 0–0.14 m、speed 0.276 m/s、加速0.4g；
  - roll ±10.8°、speed 18°/s；
  - pitch -12.1°到13.1°、speed 22°/s；
- 1800mm × 2500mm铝型材mockup固定其上模拟小型车辆；
- 通过Unity角速度数据驱动运动平台实现真实物理同步；
- **Empatica E4 wristband**：采样4 Hz记录GSR数据。

**GSR预处理**：
- Ledalab（MATLAB-based）做特征提取；
- 8 Hz Gaussian Window + 自适应平滑 → CDA连续分解分析，分离Tonic（SCL）和Phasic（SCR）；
- Min-Max归一化（公式1）每位被试。

### 2.4 流程

① 知情同意+E4佩戴+E4 Realtime API开始记录 → ② 登上运动平台+佩戴VR HMD+手柄 → ③ 练习场景（充分熟悉VA标注）→ ④ 8场景拉丁方随机顺序，每场景后填中期问卷 → ⑤ 8场景结束后填后测问卷。

## 三、关键指标与测量

### 3.1 GSR特征（事件前10秒 vs 事件后10秒）

- GSR Max、GSR Mean（整体）；
- GSR Tonic Max、GSR Tonic Mean（SCL）；
- **GSR Phasic Max、GSR Phasic Mean（SCR，主要分析指标）**——SCR幅度与感知威胁正相关。

### 3.2 自报VA数据

- Arousal Max、Mean、Min；
- Valence Max、Mean、Min。

### 3.3 问卷量表

- **Trust**（Choi & Ji 2015，3题5点）；
- **Perceived Safety**（Hewitt 2019，3题5点）；
- **Immersion and Presence**（Kalawsky 1999，10题）；
- **Situation Awareness**（Salmon 2009，9题）；
- **Reaction to Events**（Morra 2019，4题）；
- **Post-Questionnaire**（6题，针对风险水平×信息提供的偏好）。

### 3.4 统计

JASP软件，重复测量ANOVA，Bonferroni校正后事后比较，p<0.05显著。

## 四、主要结果与发现（具体数值）

### 4.1 GSR Phasic分析

- **GSR Phasic Max**：F(3,132)=34.871, **p<0.001**
  - High > Medium (p=0.003)、Low (p<0.001)、No Risk (p<0.001)；
  - Medium > Low (p<0.001)、No Risk (p<0.001)；
  - **AR信息使GSR Phasic Max略升高**（p=0.350不显著）；
- **GSR Phasic Mean**：F(3,132)=25.567, **p<0.001**
  - High > Medium (p=0.001)、Low (p<0.001)、No Risk (p<0.001)；
  - Medium > Low (p<0.001)、No Risk (p=0.004)；

**事件前后对比（t检验）**：6种条件下GSR Phasic值在事件后显著升高（p<0.001至p=0.015）——证明VR场景设计成功唤起预期情绪。

### 4.2 VA数据分析

- **Arousal Max**：F(3,132)=41.043, p<0.001——High>Medium(p<0.001), Low/No Risk；Medium>No Risk(p<0.001)；
  - **AR信息使Arousal Max显著降低**（p=0.004）；
- **Arousal Mean**：F(3,132)=20.057, p<0.001；
  - AR信息使Mean Arousal略降（p=0.018）；
- **Valence Min**：F(3,132)=29.555, p<0.001——High<Medium<Low<No Risk；
  - **AR信息使Valence Min显著升高**（p=0.031）；
- **Valence Mean**：F(3,132)=14.482, p<0.001；
  - AR信息使Mean Valence略升（p=0.074）；

**总结**：风险升高→Arousal升高、Valence降低（负面情绪），AR信息提供能**降低Arousal、提升Valence**（更平静、更愉悦）。

### 4.3 问卷数据

**Trust（信任）**：F(3,132)=26.863, p<0.001
- High < Low (p<0.001)、No Risk (p<0.001)；
- **AR信息使Trust显著升高**：F(1,44)=7.278, p<0.05；

**Perceived Safety（感知安全）**：F(3,132)=13.660, p<0.001
- High < Low/No Risk (p<0.001)；
- AR信息使感知安全略升（p=0.109，未达显著）；

**Immersion & Presence（沉浸感）**：八条件间**无显著差异**，平均≥4.0——验证VR模拟在所有条件下均提供了同等沉浸感；

**Situation Awareness（态势认知）**：F(3,132)=45.982, p<0.001
- 风险越高SA越低，High<Medium(p<0.05)<Low/No Risk(p<0.001)；
- **AR信息使SA显著提升**：F(1,44)=11.272, **p<0.01**；

**Reaction to Events（事件反应）**：
- 第1题"情境危险"：F(3,132)=141.74, p<0.001，按风险水平梯度变化；
- 第2题"事件惊讶"：F(3,132)=92.155, p<0.001；
- 第3题"我能预见危险"：F(3,132)=20.645, p<0.001；
  - **AR信息显著提升预见能力**：F(1,44)=26.752, p<0.001；
- 第4题"界面提供有用信息"：F(3,132)=11.176, p<0.001；
  - **AR信息显著提升此评分**：F(1,44)=54.092, p<0.001。

### 4.4 后测问卷

- Q1–4（不同风险下是否觉得AR更安全）：仅High vs No Risk显著（p<0.05）；
- Q5–6（AR vs 无AR下信任随风险变化）：Q5（AR下信任随风险升高）显著>Q6（无AR下信任随风险升高）（Wilcoxon Z=3.677, p<0.001）；
- **核心结论**：AR信息提供能在所有风险水平下**保持/提升信任**，而无AR时高风险显著降低信任。

## 五、对AR-HUD时空设计的启示

**时间层面**：
- 事件前后10秒的GSR/VA对比验证了**预警提前显示能在事件发生前的关键窗口降低生理唤醒**——AR-HUD应在事件**前2–5秒**提供清晰的"将发生事件"信息；
- High Risk场景下AR信息提供使Arousal Max显著降低、Valence Min显著升高——预警的"安抚效应"在最危急时刻最显著。

**平面/立体层面**：
- 本研究使用Unity中的HUD覆盖层（具体形式未在文章中详细描述设计图），但在VR环境中其实现接近"挡风玻璃直投"；
- VR+运动平台的组合（PS-3TM-LP550 + Oculus Quest 2）为本领域的实验平台提供了**高保真且可重复的范式**——可在真实事故场景下采集生理与主观数据，这是传统模拟器/路上实验难以做到的。

**适用边界**：
- 当前是"自动驾驶"场景下的"乘客"实验，**被试为乘客而非主动驾驶员**——这与本研究"行人碰撞预警"的"主动驾驶员"场景有所不同，但**对预警的"前瞻性可视化"原则可迁移**；
- VR的高沉浸感（M≥4.0）使其作为实验工具有效；
- 仅52人，年龄分布偏年轻（M=21.2）；
- 仅8场景，每条件1组数据，未覆盖天气、密度等更多维度。

## 六、本文局限性与未来工作

1. **场景多样性有限**：每风险×信息组合仅1个VR场景；
2. **样本年龄偏年轻**（M=21.2）；
3. **乘客而非驾驶员**：不能直接推广到主动驾驶；
4. **未做生理与主观相关性分析**（虽提出，但未深入）；
5. **未使用神经网络做UX预测**——作者建议未来引入CNN/LSTM做精细情绪识别。

**未来工作**：① 多种天气、温度、密度的VR场景扩展；② 多被试社交互动场景（车内多人）；③ 接管请求（TOR）任务；④ 深度学习辅助的UX预测。

## 七、与本研究主题的关联

本论文对本研究主题的启发主要在**方法论与情绪量化**层面：

1. **VR + 运动平台方法论**：PS-3TM-LP550 + Oculus Quest 2的组合可被本研究借鉴用于实验室阶段的预警实验——尤其对**严重事故场景**（无法在实车上测试），VR是唯一伦理上可行的方式；
2. **GSR + 自报VA双通道量化**：生理与主观相结合的方法学，可用于本研究主题中量化"AR-HUD预警的安抚vs惊吓"效应——本研究发现**AR信息使Arousal降低**说明设计良好的预警起到"镇定作用"而非"惊吓作用"；
3. **风险等级×信息提供的2×4设计**：是本研究主题中"高/低风险×有/无AR"对比的方法学参考；
4. **信任的关键发现**：AR信息使**所有风险水平下的信任均上升**（与GSR的镇定效应一致）——这对自动驾驶时代的预警设计意义重大；
5. **乘客vs主动驾驶员**：本论文在自动驾驶情境下做实验，未来本研究主题应考虑**SAE Level 2/3下"司机-乘客"双模式**下的预警设计差异；
6. **沉浸感前提**：M≥4.0的沉浸感是VR实验有效性的前提，为本研究主题中VR实验的方法学有效性提供了具体指标参考。

> **Takeaway**: Kim et al. 2023 用VR + 运动平台 + GSR + VA 自标注的**多通道方法学**首次量化了**风险水平×AR-HUD信息提供**的2×4交互效应，发现：① 风险升高时GSR Phasic Mean/Max显著升高、Arousal升高、Valence降低；② AR信息提供能**显著降低Arousal Max** (p=0.004)、提升Valence Min (p=0.031)、提升Trust (p<0.01)、提升SA (p<0.01)——即**AR预警起到"生理镇定"和"信任建设"的双重作用**。这一发现支持本研究主题中"AR预警在高风险场景下应当增加信息密度"的设计取向，并提供了VR+运动平台+GSR+VA的完整实验方法学，可用于本研究的实验室阶段验证。
