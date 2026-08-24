# 车辆抬头显示增强现实综述：有效性、应用与安全
**A Review of Augmented Reality Heads Up Display in Vehicles: Effectiveness, Application, and Safety**

| 项 | 内容 |
|---|---|
| 作者 | Mark Winkler（JLR 捷豹路虎，英国考文垂；攻读Warwick大学SCAV七级文凭）、Morteza Soleimani（Warwick大学WMG学院助理教授，通讯作者） |
| 年份 | 2025年1月6日在线发表 |
| 期刊 | International Journal of Human–Computer Interaction（IJHCI） |
| DOI | 10.1080/10447318.2024.2443252 |
| 类型 | Survey Article（综述论文） |
| 引用 | 截至文档采集时 Article views: 2,910 |
| 本地TXT | `/home/gezhuocheng/moe/HUD/extracted_text/19_2025_A_Review_of_Augmented_Reality_Heads_Up_Display_in_Vehicles_Effectiveness_Applica.txt` |

## 一、综述目的与定位

作者出发于一个简单事实：英国78%家庭至少拥有一辆车（2021），驾驶是日常任务。仪表盘从模拟表盘（最早可追溯Aston Martin Lagonda 1976、Renault 11 1983）演变为数字仪表盘，再演变为HUD（首款商用Oldsmobile Cutlass Supreme 1988），最后演化为AR-HUD。AR-HUD与传统HUD的核心区别在于：
- **传统HUD**：固定距离投影、信息与真实世界无对齐、易因焦距切换产生认知负担；
- **AR-HUD**：可变距离投影、信息与道路实体注册对齐、能高亮道路标志、上坡转弯、前车制动、行人等。

本综述明确**不是元分析**，而是结构化的叙事综述（narrative review），框架围绕四个研究问题：
- RQ1：AR HUD与传统HUD在有效性、性能、用户体验上的对比？
- RQ2：AR HUD对认知负荷、注意盲（inattentional blindness）、障碍物检测的影响？
- RQ3：AR HUD在自动驾驶尤其是接管（handover）场景中的整合方法？
- RQ4：实现AR HUD时需考虑的额外因素（心理影响、可视性、可用性）？

## 二、文献搜索与纳入策略

**数据库**：Google Scholar、IEEE Xplore、ScienceDirect。
**关键词**（共14组）：包括 "AR HUD effectiveness/navigation/inattentional blindness/cognitive load/obstacle detection"、"Autonomous vehicles AR HUD handover"、"SAE levels and AR HUD"、"Trust in AR HUD systems"、"AR HUD visibility and 3D"、"AR HUD and colour blindness"等。
**纳入**：与车载AR HUD直接相关、近10年内、同行评审论文（少量厂商网站）。
**排除**：非同行评审、观点文、重复文献。
**重要既有综述对比**：Kettle & Lee 2022曾系统综述AR HUD可视化领域，本文补充了**晕动症（motion sickness）、注意盲、AR HUD区域尺寸、无障碍设计**等更多视角，并提出"AR HUD作为唯一主显示器"的新研究缺口。

## 三、核心议题与文献证据

### 3.1 应用：导航

- **Bolton et al. 2015**：与传统距离-转向式HUD相比，AR地标盒（landmark box）使响应时间提升 **43.1%**、成功率提升**26.2%**；地标盒甚至比AR转向箭头效果更好。
- **Wu et al. 2009**：全挡风AR-HUD地标导航研究，从技术角度强调畸变校正的重要性。
- **Bark et al. 2014**：AR HUD使驾驶员更早识别转弯位置，凝视方向更长时间保持向前。
- **Gabbard et al. 2019**：反例——某些场景下AR图形得分**低于HUD**（分心、驾驶影响、导航、信任、视野均更差），驾驶员在AR HUD上的凝视时间和频次更高，工作负荷升高。

### 3.2 SAE自动驾驶等级与接管

引用SAE J3016 (2023)，列出Level 0–5的定义表（Table 1）。Mercedes-Benz EQS与S-Class为美国首款获得Level 3认证的产品（限内华达州）；Waymo以Jaguar I-Pace运营Level 4。

**接管研究核心证据**：
- **Feierle et al. 2022**：与传统驾驶相比，AR HUD降低**接管时间**、减少碰撞数；图3显示AR HUD在可用性评分、信任、有用性、满意度上**均优于无AR HUD**。
- **Langlois & Soualmi 2016**（Table 2 关键数据）：
  | 事件 | 无AR HUD | 有AR HUD | p值 |
  |---|---|---|---|
  | 接管请求→双手上方向盘 | 3.12s (SD 1.24) | 3.13s (SD 1.42) | 0.645 |
  | 接管请求→第一次刹车 | 14.01s (SD 10.65) | **11.68s (SD 9.25)** | 0.576 |
  - AR HUD**不影响接管动作本身**，但接管后控车更平滑、变道更主动；
- **Smith et al. 2020**：在意外事件场景下，AR HUD未减少碰撞数；显示位置（低/中/高HUD vs HDD）影响结果；
- **Gerber et al. 2023**：专家访谈认为Level 3的非驾驶相关活动（NDRA）持续时间需要每1–2分钟提醒，但应"基于情境"。

### 3.3 心理因素

**(a) Inattentional Blindness（注意盲）**
- 起源于Neisser 1975的视频实验（球传递视频）。
- **Wang et al. 2022**（核心数据，Table 3）：
  | 增强条件 | 注意盲发生率 (%) |
  |---|---|
  | 无AR HUD | 47.75 |
  | AR HUD-NP（仅高亮非行人） | **63.25** |
  | AR HUD-P（高亮全部含行人） | **32.48** |
  - 关键发现：AR HUD既能降低注意盲（当行人被增强）也能加剧（当行人未被增强）；高工作负荷下尤甚。

**(b) Cognitive Load（认知负荷）**
- **Ma et al. 2021**：符合人机工程原则的AR-HUD设计能改善认知资源分配，但"过于单一与中心化"的设计反而损害驾驶绩效。
- 量化方法：**Detection Response Task**（Maag et al. 2023）结合反应时与漏判。
- 综述结论：认知负荷高度依赖设计——既有研究支持"AR降低负荷"也有"AR增加负荷"的对立证据。

**(c) Trust（信任）**
- **Von Sawitzky et al. 2019**：仅显示world-fixed信息（如下一转弯路径）即可达到高信任水平。
- **Abdi et al. 2015**：AR HUD应展示驾驶辅助系统的状态以建立信任。
- **Jung et al. 2015**：建议在关键场景下展示AR标签的不确定性。

**(d) Anxiety（焦虑）**
- **Hwang et al. 2016**：AR HUD对有"对人焦虑"的驾驶员有放松作用。

**(e) Colour Blindness（色盲）**
- 英国约300万色盲人士；全球约1/12男性、1/200女性。
- **Tanuwidjaja et al. 2014**提出可穿戴AR色盲辅助；**He et al. 2022**建议AR HUD图形可定制色盲友好配色，对交通灯加叠加层。

### 3.4 设计与功能特性

**(a) 障碍物高亮**
- **Karatas et al. 2020**：AR HUD识别行人更快（凝视步数2 vs 6）。
- **Phan et al. 2016**：23个行人场景中，AR均更早识别。
- **Chen et al. 2024**：**虚拟阴影盒（projected paths）显著优于bounding box**。
- **Kim & Gabbard 2022**：bounding box检测行人更频繁但准确性更低，影响对其他环境元素的识别。

**(b) 可视性与3D**
- **Gabbard et al. 2022**：AR HUD图形易受**颜色混合（colour blending）**影响——背景与叠加图重叠会使预期颜色难以辨别。
- **Deng et al. 2021**：立体3D AR-HUD存在"sweet spot"——位置稍偏即图像退化；提出动态预畸变校正HUDNet方法。
- **Lee et al. 2021**：基于目标识别动态调整内容颜色避免冲突。
- **Gabbard et al. 2014**：monoscopic在1.5–30米生效，对汽车应用**单目AR-HUD通常足够**；与Bark 2014的"3D更易判距"相反，仍存在争议。

**(c) 尺寸与控制**
- **Charissis et al. 2021**：中等尺寸HUD比小尺寸传统HUD表现更好。
- **Wan & Tsimhoni 2021**：定义了文字易读性的尺寸与角度要求（"Double 007 Rule"）。
- **Pe čenik et al. 2023**：FOV大小对SA无显著影响。
- 手势控制：**Charissis 2021**提出手势识别避免HDD查找；用户可学习最多6种手势（Graichen 2022）。

## 四、未解挑战与未来趋势

### 4.1 关键研究缺口：AR HUD作为唯一主显示

作者最重要的论点：**当前文献都把AR HUD视作"主仪表盘的延展"，而非主显示本身**。Figure 9（Tonnis 2006的driver task分层）展示了"primary task / secondary task / tertiary task"模型——若将secondary task（数字仪表盘的内容）整合到primary task区域（AR HUD），将出现尺寸、信息密度、颜色法规、特殊符号等一系列工程与人因挑战。

Table 4列出了JLR车辆若要把所有仪表内容迁移到AR HUD才需要研究的内容：
- **Telltales（指示灯）**：受ASIL等级与法规约束，需要确保色盲场景下也可分辨；
- **温度信息**：两区/四区温度若全部呈现会触发认知过载；
- **ADAS confidence view**：动态变化最大，需常驻显示；
- **通知、警告、错误**：当前JLR HUD仅显示大红色三角警告，要全面化需研究文本可读性、多语种（如阿拉伯文需更多垂直空间）；
- **门未关、安全带提醒**等。

### 4.2 其他未解问题

- **戴墨镜的可视性**（JLR提出过的内部问题）；
- **3D AR HUD对无立体视/深度知觉受限者的支持**；
- **乘客与行人**也可从AR受益（Zhu 2024, Tabone 2023）。

## 五、对AR-HUD时空设计的启示

**时间层面**：
- Bolton 2015的43%响应时间提升、Karatas 2020的"6步→2步凝视"是该领域被多次引用的"时序优势"数据；
- 接管场景下AR HUD不缩短首次接管时间，但能提前预警→提前减速、提前变道（Langlois 2016）。

**平面层面**：
- world-fixed信息（如下一转弯路径）即足以建立信任（Von Sawitzky 2019）；
- 中等尺寸HUD优于小尺寸（Charissis 2021），未来"AR HUD作主显示"需进一步扩大FOV。

**立体层面**：
- 单目AR-HUD通常够用（Gabbard 2014, 1.5–30米monocular cues有效）；
- 立体3D存在sweet spot问题（Deng 2021），需要动态预畸变校正。

**适用边界**：
- 高工作负荷下AR HUD可能加剧注意盲（Wang 2022）；
- 设计不当反而增加分心（Gabbard 2019）；
- 必须设计认知友好（Ma 2021）；
- 色盲、视觉障碍等无障碍设计严重不足；
- 警告若部分高亮（如仅车辆未含行人）反而引发"非增强目标的注意盲"。

## 六、综述局限性

作者承认：① 这是叙事综述而非系统综述/元分析，未做PRISMA流程图与质量评级；② 数据库限于Google Scholar、IEEE Xplore、ScienceDirect；③ 偏向JLR视角（Winkler为JLR员工）；④ "AR HUD作主显示"的论证主要基于JLR当前能力推断，而非已发表实验。

## 七、与本研究主题的关联

本综述对本研究HUD/AR-HUD行人碰撞预警的时空设计起到**坐标系作用**：

1. **行人预警证据汇总**：3.4(a)节系统对比了bounding box（Kim & Gabbard 2022）vs virtual shadow（Chen 2024）vs 闪烁红箭头（Karatas 2020）等多种高亮策略——是本研究主题的核心议题；
2. **注意盲与高亮策略**：Wang 2022的63.25% vs 32.48% vs 47.75%三组对比，直接说明"部分高亮"会产生反效果，提示设计时**必须覆盖所有高危目标或都不高亮**；
3. **接管/自动驾驶情景**：综述系统整理了Level 2/3接管研究——这是本研究主题向自动驾驶过渡场景的延伸；
4. **时空设计取舍**：综述明确单目vs立体的争论（Gabbard 2014 vs Bark 2014），与本研究关心的"平面/立体"维度直接对应；
5. **新手vs熟练驾驶员**：综述未着重探讨经验差异，留下空间——而本研究21号Huo & Alla 2025正好填补这一空白。

> **Takeaway**: Winkler & Soleimani 2025是当前AR-HUD研究最新（2025年1月）的英文综述，**梳理了"导航→接管→心理→设计"四大议题**，明确提出"AR HUD作为唯一主显示"的研究缺口。对本研究主题最具启发的核心结论是：① AR HUD不是更好的UI默认值——设计不当会增加负荷与分心；② 行人高亮必须"全或无"，否则触发未增强目标的注意盲；③ 色盲、立体盲等无障碍设计严重缺失；④ 当前尺寸限制使其无法承担全部仪表功能——这些都是本研究在时空设计时必须直面的边界条件。
