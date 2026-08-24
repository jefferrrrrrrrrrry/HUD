# HUD / AR-HUD 行人碰撞预警 论文调研

> **调研时间**：2026 年 6 月  
> **检索来源**：OpenAlex、Unpaywall、EuropePMC、arXiv  
> **总论文数**：**39 篇** | **已下载 PDF**：**12 篇** | **中文摘要完成**：**39 篇** ✅

## 📁 目录结构

```
HUD/
├── README.md                  📌 本文件 — 论文索引与导航
├── REVIEW_REPORT.md           ⭐ 综述总结报告（建议先读）
├── papers/                    📥 已下载 OA PDF（12 篇）
├── extracted_text/            📝 PDF 提取的纯文本
├── summaries/                 📰 每篇论文的中文摘要（39 篇）
├── papers_metadata.json       💾 全部论文元数据（含英文摘要）
└── download_log.json          📋 下载日志
```

## 🚀 快速开始

1. **看综述总结** → [`REVIEW_REPORT.md`](./REVIEW_REPORT.md)（推荐先读，约 15 分钟通览全局）
2. **按主题查阅** → 见下方分类表，点击中文摘要链接
3. **看 PDF 原文** → `papers/` 下 12 篇可直接打开
4. **看英文摘要** → 见本 README 第 4 节

---

## 1. 数据库与检索策略

| 检索数据库 | 用途 |
|---|---|
| **OpenAlex API** | 主检索源，覆盖 191+ 相关论文，提供完整元数据与摘要 |
| **arXiv** | 检索"pedestrian collision warning"直接相关 3 篇 |
| **Unpaywall** | 查找闭源论文的 OA 备份链接 |
| **EuropePMC** | MDPI/部分医学库的 PMC 备份下载 |

**关键词**：`AR HUD pedestrian collision warning`、`head-up display pedestrian warning`、`ARHUD vulnerable road user`、`AR HUD FCW`、`AR HUD pedestrian detection driver`、`augmented reality windshield pedestrian`

**下载情况说明**：
- ✅ **已下载（12 篇）**：arXiv、Frontiers、IEEE Access、PMC、TU/e 仓库等开放源
- ❌ **未下载（27 篇）**：MDPI（Akamai 反爬）、Wiley、IEEE Xplore、ACM 等闭源源
- 📰 **所有 39 篇均已生成中文摘要**，未下载论文摘要基于 OpenAlex 提供的完整英文 abstract

---

## 2. 按主题分类的论文清单

> 图例：📥 已下载 PDF | 📰 中文摘要 | 🔗 仅元数据


### 🎯 AR-HUD 行人碰撞预警 - 核心实验研究

| # | 年份 | 标题 | 期刊/会议 | 引用 | 资源 |
|---|------|------|-----------|------|------|
| 1 | 2018 | Driver Behavior and Performance with Augmented Reality Pedestrian Collision | IEEE Transactions on Visu | 69 | [📰摘要](summaries/01_2018_Kim_AR行人碰撞预警户外实验.md) [🔗DOI](https://doi.org/10.1109/tvcg.2018.2793680) |
| 2 | 2016 | Enhancing the driver awareness of pedestrian using augmented reality cues | - | 36 | [📰摘要](summaries/02_2016_Phan_AR提升行人感知.md) [🔗DOI](https://doi.org/10.1109/itsc.2016.7795724) |
| 3 | 2016 | Casting shadows: Ecological interface design for augmented reality pedestri | - | 4 | [📰摘要](summaries/03_2016_Kim_虚拟阴影生态界面.md) [🔗DOI](https://doi.org/10.1109/vr.2016.7504725) |
| 4 | 2016 | Virtual Shadow | Proceedings of the Human  | 27 | [📰摘要](summaries/04_2016_Kim_虚拟阴影HFES扩展.md) [🔗DOI](https://doi.org/10.1177/1541931213601474) |
| 5 | 2014 | Development of augmented forward collision warning system for Head-Up Displ | - | 8 | [📰摘要](summaries/05_2014_Yoon_HUD前向碰撞预警.md) [🔗DOI](https://doi.org/10.1109/itsc.2014.6958054) |
| 30 | 2019 | Adaptive Visual Assistance System for Enhancing the Driver Awareness of Ped | International Journal of  | 22 | [📰摘要](summaries/30_2019_Fremont_自适应行人辅助.md) [🔗DOI](https://doi.org/10.1080/10447318.2019.1698220) |

### 🇨🇳 AR-HUD 警示界面设计 - 中国研究密集区

| # | 年份 | 标题 | 期刊/会议 | 引用 | 资源 |
|---|------|------|-----------|------|------|
| 6 | 2024 | Design and Evaluation of Ecological Interface of Driving Warning System Bas | Sensors | 11 | [📥PDF](papers/06_2024_Design_and_Evaluation_of_Ecological_Interface_of_Driving_Warning_System_Based_on.pdf) [📰摘要](summaries/06_2024_Tongji_AR-HUD_DWS_Ecological_Interface.md) [🔗DOI](https://doi.org/10.3390/s24248010) |
| 7 | 2024 | Evaluating the Effectiveness of Contact-Analog and Bounding Box Prototypes  | International Journal of  | 6 | [📰摘要](summaries/07_2024_Chen_共形vs包围盒新手驾驶员.md) [🔗DOI](https://doi.org/10.1080/10447318.2024.2327197) |
| 8 | 2024 | Comparative Analysis of AR-HUDs Crash Warning Icon Designs: An Eye-Tracking | Sustainability | 7 | [📰摘要](summaries/08_2024_Wu_预警图标360眼动.md) [🔗DOI](https://doi.org/10.3390/su16219167) |
| 9 | 2025 | Spatial Plane Positioning of AR-HUD Graphics: Implications for Driver Inatt | Electronics | 2 | [📰摘要](summaries/09_2025_Ye_空间位置非注意盲视.md) [🔗DOI](https://doi.org/10.3390/electronics14234768) |
| 10 | 2021 | An Augmented Warning System for Pedestrians: User Interface Design and Algo | Applied Sciences | 13 | [📰摘要](summaries/10_2021_Tong_行人侧增强预警.md) [🔗DOI](https://doi.org/10.3390/app11167197) |
| 12 | 2024 | Improving Pedestrian Safety with Head-Up Display Warning in a Connected Env | International Journal of  | 6 | [📰摘要](summaries/12_2024_Zhang_网联HUD雾天行人.md) [🔗DOI](https://doi.org/10.1080/10447318.2024.2368910) |
| 24 | 2025 | The Influence of Information Redundancy on Driving Behavior and Psychologic | Applied Sciences | 2 | [📰摘要](summaries/24_2025_Li_雾天冗余界面.md) [🔗DOI](https://doi.org/10.3390/app152011072) |
| 27 | 2021 | Does Augmented-Reality Head-Up Display Help? A Preliminary Study on Driving | IEEE Access | 37 | [📰摘要](summaries/27_2021_Ma_ARHUD布局眼动.md) [🔗DOI](https://doi.org/10.1109/access.2021.3112240) |
| 33 | 2022 | Usability Evaluation of in-Vehicle AR-HUD Interface Applying AHP-GRA | Human-Centric Intelligent | 6 | [📥PDF](papers/33_2022_Usability_Evaluation_of_in-Vehicle_AR-HUD_Interface_Applying_AHP-GRA.pdf) [📰摘要](summaries/33_2022_Usability_AHP-GRA.md) [🔗DOI](https://doi.org/10.1007/s44230-022-00011-1) |
| 34 | 2022 | Color Visibility Evaluation of In-Vehicle AR-HUD Under Different Illuminanc | Proceedings of the Intern | 6 | [📥PDF](papers/34_2022_Color_Visibility_Evaluation_of_In-Vehicle_AR-HUD_Under_Different_Illuminance.pdf) [📰摘要](summaries/34_2022_Color_Visibility_AR-HUD.md) [🔗DOI](https://doi.org/10.4108/eai.17-6-2022.2322686) |
| 35 | 2024 | Interface Design of Automobile Head-up Display from the Perspective of Huma | - | 0 | [📥PDF](papers/35_2024_Interface_Design_of_Automobile_Head-up_Display_from_the_Perspective_of_Human-Mac.pdf) [📰摘要](summaries/35_2024_HUD_HMI_Interface_Design.md) [🔗DOI](https://doi.org/10.4108/eai.24-5-2024.2350098) |

### 📊 AR-HUD/HUD 警示对驾驶员行为/认知负荷影响

| # | 年份 | 标题 | 期刊/会议 | 引用 | 资源 |
|---|------|------|-----------|------|------|
| 11 | 2020 | Collision Avoidance Head-Up Display: Design Considerations for Emergency Se | - | 16 | [📰摘要](summaries/11_2020_BramLarbi_应急车辆HUD.md) [🔗DOI](https://doi.org/10.1109/icce46568.2020.9043068) |
| 13 | 2019 | Assessing Distraction Potential of Augmented Reality Head-Up Displays for V | Human Factors The Journal | 104 | [📰摘要](summaries/13_2019_Kim_AR分心量化方法.md) [🔗DOI](https://doi.org/10.1177/0018720819844845) |
| 14 | 2017 | Brake reactions of distracted drivers to pedestrian Forward Collision Warni | Journal of Safety Researc | 49 | [📰摘要](summaries/14_2017_Lubbe_分心驾驶制动反应.md) [🔗DOI](https://doi.org/10.1016/j.jsr.2017.02.002) |
| 15 | 2015 | Distractive or Supportive -- How Warnings in the Head-up Display Affect Dri | - | 39 | [📰摘要](summaries/15_2015_Winkler_HUD预警凝视行为.md) [🔗DOI](https://doi.org/10.1109/itsc.2015.172) |
| 16 | 2015 | Accident Prevention through Visual Warnings: How to Design Warnings in Head | - | 22 | [📰摘要](summaries/16_2015_Kazazi_HUD老年年轻预警.md) [🔗DOI](https://doi.org/10.1109/itsc.2015.171) |
| 36 | 2023 | Physiological Signals as Predictors of Cognitive Load Induced by the Type o | IEEE Access | 12 | [📰摘要](summaries/36_2023_Strle_生理信号认知负荷.md) [🔗DOI](https://doi.org/10.1109/access.2023.3305383) |
| 39 | - | Influence of Pedestrian Collision Warning Systems on Driver Behavior - Simu | - | ? | [📥PDF](papers/39__Influence_of_Pedestrian_Collision_Warning_Systems_on_Driver_Behavior_-_Simulator.pdf) [📰摘要](summaries/39_2021_arXiv_PCW_DriverBehavior_Simulator.md) [🔗](#https://arxiv.org/abs/2112.09074) |

### 🤖 计算机视觉 + 深度学习 + AR-HUD

| # | 年份 | 标题 | 期刊/会议 | 引用 | 资源 |
|---|------|------|-----------|------|------|
| 17 | 2023 | Augmented Reality-Based Navigation Using Deep Learning-Based Pedestrian and | IEEE Access | 12 | [📥PDF](papers/17_2023_Augmented_Reality-Based_Navigation_Using_Deep_Learning-Based_Pedestrian_and_Pers.pdf) [📰摘要](summaries/17_2023_KATECH_DL_PM_Pedestrian_AR-HUD.md) [🔗DOI](https://doi.org/10.1109/access.2023.3286872) |
| 22 | 2018 | ARVE | - | 22 | [📰摘要](summaries/22_2018_Zhou_ARVE车联边缘.md) [🔗DOI](https://doi.org/10.1145/3229556.3229564) |
| 28 | 2008 | A Novel Active Heads-Up Display for Driver Assistance | IEEE Transactions on Syst | 128 | [📰摘要](summaries/28_2008_Doshi_主动HUD驾驶辅助.md) [🔗DOI](https://doi.org/10.1109/tsmcb.2008.923527) |
| 37 | - | End-to-End Pedestrian Collision Warning System based on CNN Semantic Segmen | - | ? | [📥PDF](papers/37__End-to-End_Pedestrian_Collision_Warning_System_based_on_CNN_Semantic_Segmentatio.pdf) [📰摘要](summaries/37_2016_arXiv_End2End_PCW_CNN_SemSeg.md) [🔗](#https://arxiv.org/abs/1612.06558) |
| 38 | - | Real-Time Predictive Pedestrian Collision Warning Service for Cooperative I | - | ? | [📥PDF](papers/38__Real-Time_Predictive_Pedestrian_Collision_Warning_Service_for_Cooperative_ITS.pdf) [📰摘要](summaries/38_2020_arXiv_PPCWS_3DPose.md) [🔗](#https://arxiv.org/abs/2009.10868) |

### 🥽 AR-HMD 头戴式与下一代探索

| # | 年份 | 标题 | 期刊/会议 | 引用 | 资源 |
|---|------|------|-----------|------|------|
| 20 | 2025 | ARive: Assisting Drivers with In-Car Augmented Reality for Risk Zone Detect | Proceedings of the ACM on | 1 | [📥PDF](papers/20_2025_ARive__Assisting_Drivers_with_In-Car_Augmented_Reality_for_Risk_Zone_Detection.pdf) [📰摘要](summaries/20_2025_Honda_TUe_ARive_AR-HMD_Risk_Zone.md) [🔗DOI](https://doi.org/10.1145/3712270) |
| 21 | 2025 | Differences in drivers’ dependence on AR warning information in urban drivi | Frontiers in Virtual Real | 0 | [📥PDF](papers/21_2025_Differences_in_drivers’_dependence_on_AR_warning_information_in_urban_driving_en.pdf) [📰摘要](summaries/21_2025_AR_Warning_Dependence_Driving_Experience.md) [🔗DOI](https://doi.org/10.3389/frvir.2025.1638823) |

### 📚 AR-HUD 综述/技术展望

| # | 年份 | 标题 | 期刊/会议 | 引用 | 资源 |
|---|------|------|-----------|------|------|
| 18 | 2013 | In‐Vehicle AR‐HUD System to Provide Driving‐Safety Information | ETRI Journal | 120 | [📰摘要](summaries/18_2013_Park_车载ARHUD系统.md) [🔗DOI](https://doi.org/10.4218/etrij.13.2013.0041) |
| 19 | 2025 | A Review of Augmented Reality Heads Up Display in Vehicles: Effectiveness,  | International Journal of  | 14 | [📰摘要](summaries/19_2025_Winkler_ARHUD车载综述.md) [🔗DOI](https://doi.org/10.1080/10447318.2024.2443252) |
| 26 | 2021 | Employing Emerging Technologies to Develop and Evaluate In-Vehicle Intellig | Applied Sciences | 60 | [📰摘要](summaries/26_2021_Charissis_信息娱乐ARHUD.md) [🔗DOI](https://doi.org/10.3390/app11041397) |
| 29 | 2023 | Machine learning-based cognitive load prediction model for AR-HUD to improv | Frontiers in Public Healt | 8 | [📥PDF](papers/29_2023_Machine_learning-based_cognitive_load_prediction_model_for_AR-HUD_to_improve_OSH.pdf) [📰摘要](summaries/29_2023_ML_Cognitive_Load_Prediction_AR-HUD.md) [🔗DOI](https://doi.org/10.3389/fpubh.2023.1195961) |
| 31 | 2022 | Augmented Reality for Vehicle-Driver Communication: A Systematic Review | Safety | 26 | [📰摘要](summaries/31_2022_Kettle_AR车辆沟通综述.md) [🔗DOI](https://doi.org/10.3390/safety8040084) |
| 32 | 2022 | Automotive Holographic Head‐Up Displays | Advanced Materials | 75 | [📰摘要](summaries/32_2022_Skirnewskaja_全息HUD.md) [🔗DOI](https://doi.org/10.1002/adma.202110463) |

### 🚗 自动/半自动驾驶相关 AR-HUD

| # | 年份 | 标题 | 期刊/会议 | 引用 | 资源 |
|---|------|------|-----------|------|------|
| 23 | 2023 | Assessing the Impact of AR HUDs and Risk Level on User Experience in Self-D | Applied Sciences | 13 | [📰摘要](summaries/23_2023_Kim_ARHUD自动驾驶UX.md) [🔗DOI](https://doi.org/10.3390/app13084952) |
| 25 | 2019 | AR DriveSim: An Immersive Driving Simulator for Augmented Reality Head-Up D | Frontiers in Robotics and | 44 | [📥PDF](papers/25_2019_AR_DriveSim__An_Immersive_Driving_Simulator_for_Augmented_Reality_Head-Up_Displa.pdf) [📰摘要](summaries/25_2019_AR_DriveSim_Immersive_Simulator.md) [🔗DOI](https://doi.org/10.3389/frobt.2019.00098) |

---

## 3. 已下载 PDF 速查表

12 篇可直接阅读 PDF 原文：

| # | 论文 | PDF |
|---|------|-----|
| 6 | Design and Evaluation of Ecological Interface of Driving Warning System Based on | [06_2024_Design_and_Evaluation_of_Ecological_Interf...](papers/06_2024_Design_and_Evaluation_of_Ecological_Interface_of_Driving_Warning_System_Based_on.pdf) |
| 17 | Augmented Reality-Based Navigation Using Deep Learning-Based Pedestrian and Pers | [17_2023_Augmented_Reality-Based_Navigation_Using_D...](papers/17_2023_Augmented_Reality-Based_Navigation_Using_Deep_Learning-Based_Pedestrian_and_Pers.pdf) |
| 20 | ARive: Assisting Drivers with In-Car Augmented Reality for Risk Zone Detection | [20_2025_ARive__Assisting_Drivers_with_In-Car_Augme...](papers/20_2025_ARive__Assisting_Drivers_with_In-Car_Augmented_Reality_for_Risk_Zone_Detection.pdf) |
| 21 | Differences in drivers’ dependence on AR warning information in urban driving en | [21_2025_Differences_in_drivers’_dependence_on_AR_w...](papers/21_2025_Differences_in_drivers’_dependence_on_AR_warning_information_in_urban_driving_en.pdf) |
| 25 | AR DriveSim: An Immersive Driving Simulator for Augmented Reality Head-Up Displa | [25_2019_AR_DriveSim__An_Immersive_Driving_Simulato...](papers/25_2019_AR_DriveSim__An_Immersive_Driving_Simulator_for_Augmented_Reality_Head-Up_Displa.pdf) |
| 29 | Machine learning-based cognitive load prediction model for AR-HUD to improve OSH | [29_2023_Machine_learning-based_cognitive_load_pred...](papers/29_2023_Machine_learning-based_cognitive_load_prediction_model_for_AR-HUD_to_improve_OSH.pdf) |
| 33 | Usability Evaluation of in-Vehicle AR-HUD Interface Applying AHP-GRA | [33_2022_Usability_Evaluation_of_in-Vehicle_AR-HUD_...](papers/33_2022_Usability_Evaluation_of_in-Vehicle_AR-HUD_Interface_Applying_AHP-GRA.pdf) |
| 34 | Color Visibility Evaluation of In-Vehicle AR-HUD Under Different Illuminance | [34_2022_Color_Visibility_Evaluation_of_In-Vehicle_...](papers/34_2022_Color_Visibility_Evaluation_of_In-Vehicle_AR-HUD_Under_Different_Illuminance.pdf) |
| 35 | Interface Design of Automobile Head-up Display from the Perspective of Human-Mac | [35_2024_Interface_Design_of_Automobile_Head-up_Dis...](papers/35_2024_Interface_Design_of_Automobile_Head-up_Display_from_the_Perspective_of_Human-Mac.pdf) |
| 37 | End-to-End Pedestrian Collision Warning System based on CNN Semantic Segmentatio | [37__End-to-End_Pedestrian_Collision_Warning_System...](papers/37__End-to-End_Pedestrian_Collision_Warning_System_based_on_CNN_Semantic_Segmentatio.pdf) |
| 38 | Real-Time Predictive Pedestrian Collision Warning Service for Cooperative ITS | [38__Real-Time_Predictive_Pedestrian_Collision_Warn...](papers/38__Real-Time_Predictive_Pedestrian_Collision_Warning_Service_for_Cooperative_ITS.pdf) |
| 39 | Influence of Pedestrian Collision Warning Systems on Driver Behavior - Simulator | [39__Influence_of_Pedestrian_Collision_Warning_Syst...](papers/39__Influence_of_Pedestrian_Collision_Warning_Systems_on_Driver_Behavior_-_Simulator.pdf) |

---

## 4. 英文摘要（按 idx 排序）


### 🔗 [1] Driver Behavior and Performance with Augmented Reality Pedestrian Collision Warning: An Outdoor User Study

**作者**：Hyungil Kim, Joseph L. Gabbard, Alexandre Miranda Añon, Teruhisa Misu | **2018** · IEEE Transactions on Visualization and Computer Graphics | **被引**：69

**DOI**：[10.1109/tvcg.2018.2793680](https://doi.org/10.1109/tvcg.2018.2793680)

📰 **中文摘要**：[`01_2018_Kim_AR行人碰撞预警户外实验.md`](summaries/01_2018_Kim_AR行人碰撞预警户外实验.md)

**英文摘要**：

> This article investigates the effects of visual warning presentation methods on human performance in augmented reality (AR) driving. An experimental user study was conducted in a parking lot where participants drove a test vehicle while braking for any cross traffic with assistance from AR visual warnings presented on a monoscopic and volumetric head-up display (HUD). Results showed that monoscopic displays can be as effective as volumetric displays for human performance in AR braking tasks. The experiment also demonstrated the benefits of conformal graphics, which are tightly integrated into the real world, such as their ability to guide drivers' attention and their positive consequences on driver behavior and performance. These findings suggest that conformal graphics presented via monoscopic HUDs can enhance driver performance by leveraging the effectiveness of monocular depth cues. The proposed approaches and methods can be used and further developed by future researchers and practitioners to better understand driver performance in AR as well as inform usability evaluation of future automotive AR applications.

### 🔗 [2] Enhancing the driver awareness of pedestrian using augmented reality cues

**作者**：Minh Tien Phan, Indira Thouvenin, Vincent Frémont | **2016** · - | **被引**：36

**DOI**：[10.1109/itsc.2016.7795724](https://doi.org/10.1109/itsc.2016.7795724)

📰 **中文摘要**：[`02_2016_Phan_AR提升行人感知.md`](summaries/02_2016_Phan_AR提升行人感知.md)

**英文摘要**：

> Pedestrian accident is a serious problem for the society. Pedestrian Collision Warning Systems (PCWS) are proposed to detect the presence of pedestrians and to warn the driver about the potential dangers. However, their interfaces associated with ambiguous alerts can distract drivers and create more dangers. On the other hand, Augmented Reality (AR) with Head-Up Display (HUD) interfaces have recently attracted the attention in the field of automotive research as they can maintain driver's gaze on the road. In this paper, we design a new PCWS with the AR cues and propose an experimental to evaluate the AR cues by assessing the driver's awareness of a pedestrian. At this stage, a fixed-based driving simulator is used for the study. Twenty five healthy middle-aged licensed drivers participate in the experiment. A car following task is proposed as the main driving task. Three levels of the driver's awareness of a pedestrian: the perception level, the vigilance level and the anticipation level are assessed through the observable outcomes. The results show that the proposed AR cues can enhance the driver's awareness of a pedestrian in all the three levels.

### 🔗 [3] Casting shadows: Ecological interface design for augmented reality pedestrian collision warning

**作者**：Hyungil Kim, Jessica D. Isleib, Joseph L. Gabbard | **2016** · - | **被引**：4

**DOI**：[10.1109/vr.2016.7504725](https://doi.org/10.1109/vr.2016.7504725)

📰 **中文摘要**：[`03_2016_Kim_虚拟阴影生态界面.md`](summaries/03_2016_Kim_虚拟阴影生态界面.md)

**英文摘要**：

> Ecological interface design (EID) has the opportunity to complement current approaches for augmented reality (AR) interface design by considering human-environment interaction and leveraging the inherent benefit of AR interfaces: conformal graphics. This work applies EID to design a novel interface for pedestrian collision warning for an automotive AR head-up display (HUD). Our initial usability evaluation shows potential benefits of incorporating EID into AR interface design.

### 🔗 [4] Virtual Shadow

**作者**：Hyungil Kim, Jessica D. Isleib, Joseph L. Gabbard | **2016** · Proceedings of the Human Factors and Ergonomics Society Annual Meeting | **被引**：27

**DOI**：[10.1177/1541931213601474](https://doi.org/10.1177/1541931213601474)

📰 **中文摘要**：[`04_2016_Kim_虚拟阴影HFES扩展.md`](summaries/04_2016_Kim_虚拟阴影HFES扩展.md)

**英文摘要**：

> Most obvious benefit of augmented reality (AR) displays is direct perception of information atop physical reality. In driving context, however, AR interfaces should be designed carefully to guide drivers’ attention while minimizing attentional narrowing. This work aims to design an interface for cross traffic alert using an AR head up display (HUD) that is compatible with both the driver’s cognitive process and physical reality of driving environment. Ecological interface design (EID) allowed us to complement current user centered design (UCD) approaches by considering human-environment interaction and leveraging the inherent benefit of AR interfaces: conformal graphics. We designed a novel interface that casts virtual shadows of approaching obstacles through an AR HUD and prototyped this idea for a specific use-case of pedestrian collision warning. Our initial usability evaluation demonstrated potential benefits of incorporating EID into AR interface design. The approaches and design idea from this study can be leveraged by future researchers and designers to create more reliable and safer AR interfaces for vehicle drivers.

### 🔗 [5] Development of augmented forward collision warning system for Head-Up Display

**作者**：Changrak Yoon, Kyong-Ho Kim, Hye Sun Park, Min Woo Park | **2014** · - | **被引**：8

**DOI**：[10.1109/itsc.2014.6958054](https://doi.org/10.1109/itsc.2014.6958054)

📰 **中文摘要**：[`05_2014_Yoon_HUD前向碰撞预警.md`](summaries/05_2014_Yoon_HUD前向碰撞预警.md)

**英文摘要**：

> In this paper, we present an augmented forward collision warning system for Head-Up Display (HUD). The convergence of HUD and Augmented Reality (AR) needs challenge and make innovative application in automobile industry. We focus on an advance of Forward Collision Warning System (FCWS) by the fusion of HUD and AR. The proposed system detects the frontal vehicles and pedestrians, assesses the imminent danger caused by the detected results, and alerts the augmented warnings to support safe driving practices.

### 📥 [6] Design and Evaluation of Ecological Interface of Driving Warning System Based on AR-HUD

**作者**：Jun Ma, Yuhui Li, Yuanyang Zuo | **2024** · Sensors | **被引**：11

**DOI**：[10.3390/s24248010](https://doi.org/10.3390/s24248010)

📰 **中文摘要**：[`06_2024_Tongji_AR-HUD_DWS_Ecological_Interface.md`](summaries/06_2024_Tongji_AR-HUD_DWS_Ecological_Interface.md)

📥 **本地 PDF**：[`06_2024_Design_and_Evaluation_of_Ecological_Interface_of_Driving_Warning_System_Based_on.pdf`](papers/06_2024_Design_and_Evaluation_of_Ecological_Interface_of_Driving_Warning_System_Based_on.pdf)

**英文摘要**：

> As the global traffic environment becomes increasingly complex, driving safety issues have become more prominent, making manual-response driving warning systems (DWSs) essential. Augmented reality head-up display (AR-HUD) technology can project information directly, enhancing driver attention; however, improper design may increase cognitive load and affect safety. Thus, the design of AR-HUD driving warning interfaces must focus on improving attention and reducing cognitive load. Currently, systematic research on AR-HUD DWS interfaces is relatively scarce. This paper proposes an ecological interface cognitive balance design strategy for AR-HUD DWS based on cognitive load theory and environmental interface design theory. The research includes developing design models, an integrative framework, and experimental validation suitable for warning scenarios. Research results indicate that the proposed design effectively reduces cognitive load and significantly decreases driver response and comprehension times, outperforming existing interfaces. This design strategy and framework possess promotional value, providing theoretical references and methodological guidance for AR-HUD warning interface research.

### 🔗 [7] Evaluating the Effectiveness of Contact-Analog and Bounding Box Prototypes in Augmented Reality Head-Up Display Warning for Chinese Novice Drivers Under Various Collision Types and Traffic Density

**作者**：Wanting Chen, Liuqiucheng Niu, Shan Liu, Shu Ma | **2024** · International Journal of Human-Computer Interaction | **被引**：6

**DOI**：[10.1080/10447318.2024.2327197](https://doi.org/10.1080/10447318.2024.2327197)

📰 **中文摘要**：[`07_2024_Chen_共形vs包围盒新手驾驶员.md`](summaries/07_2024_Chen_共形vs包围盒新手驾驶员.md)

**英文摘要**：

> Augmented Reality Head-Up Display (AR-HUD) is a promising solution to the current warning system distraction problem. However, how to effectively convey warnings through AR graphics is still unclear. This study examines the effectiveness of the contact-analog graphic compared to the bounding box graphic in various collision types and traffic densities. Forty-eight participants watched AR-augmented driving videos and were instructed to respond to critical events. Reaction time, response rate, and subjective evaluations were compared for rear-end and pedestrian collisions in different traffic densities under different warnings. Both bounding box and contact-analog warnings improved driving performance compared to the non-warning group. The contact-analog warning performed better for rear-end collisions, while the bounding box warning had a lower reaction time for pedestrian collisions, regardless of traffic density.

### 🔗 [8] Comparative Analysis of AR-HUDs Crash Warning Icon Designs: An Eye-Tracking Study Using 360° Panoramic Driving Simulation

**作者**：Zhendong Wu, Ying Liang, Guocui Liu, Xiaoqun Ai | **2024** · Sustainability | **被引**：7

**DOI**：[10.3390/su16219167](https://doi.org/10.3390/su16219167)

📰 **中文摘要**：[`08_2024_Wu_预警图标360眼动.md`](summaries/08_2024_Wu_预警图标360眼动.md)

**英文摘要**：

> Augmented Reality Head-Up Displays (AR-HUDs) enhance driver perception and safety, yet optimal hazard warning design remains unclear. This study examines three AR-HUD crash warning icon types (BD, BR, BW) across various turning scenarios. Using a 360-degree video-based driving simulation with 36 participants, eye-tracking metrics were collected. Results show BW icons, dynamically linked to hazards, significantly improve drivers’ pedestrian risk awareness and visual attention allocation compared to BD and BR systems. BW consistently demonstrated longer gaze duration, higher fixation counts, and shorter time to first fixation across all turns. BD and BR icons were more susceptible to lane changes, potentially diverting attention from hazards. Findings suggest prioritizing dynamic tracking warning icons over fixed-position alternatives to minimize visual competition and distraction, providing crucial insights for AR-HUD optimization in automated vehicles.

### 🔗 [9] Spatial Plane Positioning of AR-HUD Graphics: Implications for Driver Inattentional Blindness in Navigation and Collision Warning Scenarios

**作者**：M. H. Ye, Jun Yin | **2025** · Electronics | **被引**：2

**DOI**：[10.3390/electronics14234768](https://doi.org/10.3390/electronics14234768)

📰 **中文摘要**：[`09_2025_Ye_空间位置非注意盲视.md`](summaries/09_2025_Ye_空间位置非注意盲视.md)

**英文摘要**：

> In-vehicle Augmented Reality Head-Up Displays (AR-HUDs) enhance driving performance and experience by presenting critical information such as navigation cues and collision warnings. Although many studies have investigated the efficacy of AR-HUD navigation and collision warning interface designs, existing research has overlooked the critical interplay between graphic spatial positioning and safety risks arising from inattentional blindness. This study employed a single-factor within-subjects design, with Experiment 1 and Experiment 2 separately examining the impact of the spatial planar position (horizontal planar position, vertical planar position, mixed planar position) of AR-HUD navigation graphics and collision warning graphics on drivers’ inattentional blindness. The results revealed that the spatial planar position of AR-HUD navigation graphics has no significant effect on inattentional blindness behavior or reaction time. However, the horizontal planar position yielded the best user experience with low workload, followed by the mixed planar position. For AR-HUD collision warning graphics, their spatial planar position does not significantly influence the frequency of inattentional blindness; From the perspectives of workload and user experience, the vertical planar position of collision warning graphics provides the best experience with the lowest workload, while the mixed planar position demonstrates superior hedonic qualities. Overall, this study offers design guideli...

### 🔗 [10] An Augmented Warning System for Pedestrians: User Interface Design and Algorithm Development

**作者**：Yourui Tong, Bochen Jia, Shan Bao | **2021** · Applied Sciences | **被引**：13

**DOI**：[10.3390/app11167197](https://doi.org/10.3390/app11167197)

📰 **中文摘要**：[`10_2021_Tong_行人侧增强预警.md`](summaries/10_2021_Tong_行人侧增强预警.md)

**英文摘要**：

> Warning pedestrians of oncoming vehicles is critical to improving pedestrian safety. Due to the limitations of a pedestrian’s carrying capacity, it is crucial to find an effective solution to provide warnings to pedestrians in real-time. Limited numbers of studies focused on warning pedestrians of oncoming vehicles. Few studies focused on developing visual warning systems for pedestrians through wearable devices. In this study, various real-time projection algorithms were developed to provide accurate warning information in a timely way. A pilot study was completed to test the algorithm and the user interface design. The projection algorithms can update the warning information and correctly fit it into an easy-to-understand interface. By using this system, timely warning information can be sent to those pedestrians who have lower situational awareness or obstructed view to protect them from potential collisions. It can work well when the sightline is blocked by obstructions.

### 🔗 [11] Collision Avoidance Head-Up Display: Design Considerations for Emergency Services’ Vehicles

**作者**：Kweku F. Bram-Larbi, Vassilis Charissis, Soheeb Khan, Ramesh Lagoo | **2020** · - | **被引**：16

**DOI**：[10.1109/icce46568.2020.9043068](https://doi.org/10.1109/icce46568.2020.9043068)

📰 **中文摘要**：[`11_2020_BramLarbi_应急车辆HUD.md`](summaries/11_2020_BramLarbi_应急车辆HUD.md)

**英文摘要**：

> Emergency Services’ (ES) vehicles primary objective is to attend an accident or other incident scenes in a fast, safe and efficient manner. Yet this task is becoming increasingly difficult due to the increasing population and the plethora of emergency cases. These factors affect directly the traffic both within the urban and the rural environment, increasing dramatically the “time to arrive” at the point of interest. Numerous Head-Down Display (HDD) systems have populated the dashboard area of the ES vehicles in order to tackle this issue, with limited success. To this end, the development of emerging technologies in both computing and telecommunications have enabled modern vehicular systems to assist drivers in their decision-making process. Head-Up Displays (HUD) present a combinatory approach of the aforementioned technologies, which present crucial information to the driver through Augmented Reality (AR) projection. In order to develop a design and development framework for the utilisation of AR and HUD technology, this paper presents the results of 50 drivers investigation related to their activities during immobile or slow-moving traffic which results in driver’s distraction and inability to respond to the incoming ES vehicles. In turn, the paper discusses these results and offers an overview of the Human-Machine Interface requirements for a prototype HUD aiming to assist the safety, speed and manoeuvrability of the ES vehicles.

### 🔗 [12] Improving Pedestrian Safety with Head-Up Display Warning in a Connected Environment

**作者**：Yu Zhang, Yang Bian, Xiaohua Zhao, Xuewei Li | **2024** · International Journal of Human-Computer Interaction | **被引**：6

**DOI**：[10.1080/10447318.2024.2368910](https://doi.org/10.1080/10447318.2024.2368910)

📰 **中文摘要**：[`12_2024_Zhang_网联HUD雾天行人.md`](summaries/12_2024_Zhang_网联HUD雾天行人.md)

**英文摘要**：

> In this paper, the potential of using a head-up display (HUD) in the connected environment to improve a vehicle’s running comfort and pedestrian safety is tested, by providing warning information to drivers in advance. To achieve this objective, driving simulation technology is used to construct the connected environment and develop the HUD, and the effectiveness of the system is then tested. Specifically, thirty-four participants were recruited to conduct driving simulation experiments in six scenarios: three warning display types (Baseline/Head-down display/Head-up display) combined with two weather conditions (clear weather/foggy weather). The effects of the three different warning display types on braking risk-avoidance strategy were studied by comparing the drivers’ performance during the perception and decision stage (position of accelerator-pedal release, position of first braking), the risk-avoidance manipulation stage (maximum deceleration, braking distance) and the risk-avoidance result stage (minimum collision distance, position of minimum speed). The influences of weather conditions and driver attributes were also considered. When the HUD warnings were activated, drivers started to decelerate further away from pedestrians, with a more stable and moderate deceleration process and a greater safety margin between the vehicle and the pedestrians. Using HUD warnings in foggy conditions improved drivers’ perception and decision abilities, this study confirmed the great ...

### 🔗 [13] Assessing Distraction Potential of Augmented Reality Head-Up Displays for Vehicle Drivers

**作者**：Hyungil Kim, Joseph L. Gabbard | **2019** · Human Factors The Journal of the Human Factors and Ergonomics Society | **被引**：104

**DOI**：[10.1177/0018720819844845](https://doi.org/10.1177/0018720819844845)

📰 **中文摘要**：[`13_2019_Kim_AR分心量化方法.md`](summaries/13_2019_Kim_AR分心量化方法.md)

**英文摘要**：

> OBJECTIVE: To develop a framework for quantifying the visual and cognitive distraction potential of augmented reality (AR) head-up displays (HUDs). BACKGROUND: AR HUDs promise to be less distractive than traditional in-vehicle displays because they project information onto the driver's forward-looking view of the road. However, AR graphics may direct the driver's attention away from critical road elements. Moreover, current in-vehicle device assessment methods, which are based on eyes-off-road time measures, cannot capture this unique challenge. METHOD: = 24) was conducted in a driving simulator to apply the proposed method for the assessment of two AR pedestrian collision warning (PCW) design alternatives. RESULTS: Only one of the two tested AR interfaces improved driver awareness of pedestrians without visually and cognitively distracting drivers from other road elements that were not augmented by the display but still critical for safe driving. CONCLUSION: Our initial human-subject experiment demonstrated the potential of the proposed method in quantifying both positive and negative consequences of AR HUDs on driver cognitive processes. More importantly, the study suggests that AR interfaces can be informative or distractive depending on the perceptual forms of graphical elements presented on the displays. APPLICATION: The proposed methods can be applied by designers of in-vehicle AR HUD interfaces and be leveraged by designers of AR user interfaces in general.

### 🔗 [14] Brake reactions of distracted drivers to pedestrian Forward Collision Warning systems

**作者**：Nils Lübbe | **2017** · Journal of Safety Research | **被引**：49

**DOI**：[10.1016/j.jsr.2017.02.002](https://doi.org/10.1016/j.jsr.2017.02.002)

📰 **中文摘要**：[`14_2017_Lubbe_分心驾驶制动反应.md`](summaries/14_2017_Lubbe_分心驾驶制动反应.md)

_(无可获取的英文摘要)_

### 🔗 [15] Distractive or Supportive -- How Warnings in the Head-up Display Affect Drivers' Gaze and Driving Behavior

**作者**：Susann Winkler, Juela Kazazi, Mark Vollrath | **2015** · - | **被引**：39

**DOI**：[10.1109/itsc.2015.172](https://doi.org/10.1109/itsc.2015.172)

📰 **中文摘要**：[`15_2015_Winkler_HUD预警凝视行为.md`](summaries/15_2015_Winkler_HUD预警凝视行为.md)

**英文摘要**：

> Urban areas expose drivers to a lot of challenges (e.g., many kinds of distracting stimuli and road users) and critical situations, increasing the probability of driver errors. Therefore the accident rate in urban areas is quite high and driver assistance is needed. As part of the research project UR:BAN, this study investigates the effectiveness of four different types of driver warnings (+ control group), presented in a head-up display (HUD), to support drivers in a very critical urban scenario. The aim of these driver warnings was to alert drivers to a forthcoming pedestrian crossing the ego vehicle's road, eliciting a fast and strong response from the drivers like an emergency brake. The driver warnings varied in their strategy (attention vs. reaction oriented) and specificity (generic vs. specific). In a driving simulation the drivers' gaze and driving behavior were analyzed. A total of sixty drivers were tested in a between-subjects design (27 female, 33 male, M = 23.7 years, SD = 3.7 years). In general, all driver warnings affected the drivers' performance positively. Even though the number of collisions was not reduced, drivers showed a faster and stronger brake reaction when being warned, which nevertheless reduced the collision severity. While all drivers gazed at the safety-critical object, only about half of the drivers showed a HUD glance. When the drivers gazed at the HUD, the positive effect of the driver warnings on the brake reaction time was reduced. Thus, d...

### 🔗 [16] Accident Prevention through Visual Warnings: How to Design Warnings in Head-up Display for Older and Younger Drivers

**作者**：Juela Kazazi, Susann Winkler, Mark Vollrath | **2015** · - | **被引**：22

**DOI**：[10.1109/itsc.2015.171](https://doi.org/10.1109/itsc.2015.171)

📰 **中文摘要**：[`16_2015_Kazazi_HUD老年年轻预警.md`](summaries/16_2015_Kazazi_HUD老年年轻预警.md)

**英文摘要**：

> Many severe accidents occur in urban areas. As part of the research project UR:BAN this study investigated how different types of visual warnings can prevent collisions within these areas and trigger the adequate reaction in critical situations. For this, two different warning types were implemented in a head-up display. It was assumed that one of the warning types should trigger an immediate and firm brake reaction of the driver (stop sign warning) whereas the other type of warning should animate the driver to be cautious, for example by slightly pressing the brake pedal (caution sign warning). As collisions in urban areas are also very difficult for older drivers, differences of the effects of the two warning types between older and younger drivers on driver performance (numbers of collisions, brake reaction time, maximum braking value) were examined. For this, four urban scenarios were implemented in a static driving simulator varying the characteristics of the critical object (e.g., pedestrian, lead vehicle, obstacle). In total 72 drivers (36 participants aged 20-35 years, 36 participants aged 65+ years) were tested in a between-subjects design (Age, Type of Warning). The study revealed that the number of collisions was reduced when drivers were warned (especially for younger drivers) demonstrating the positive effect of these warning types in very critical scenarios. If the situation is not very critical, warnings did not reduce the numbers of collisions, since the total...

### 📥 [17] Augmented Reality-Based Navigation Using Deep Learning-Based Pedestrian and Personal Mobility User Recognition—A Comparative Evaluation for Driving Assistance

**作者**：Dong Hyeon Roh, Jae Yeol Lee | **2023** · IEEE Access | **被引**：12

**DOI**：[10.1109/access.2023.3286872](https://doi.org/10.1109/access.2023.3286872)

📰 **中文摘要**：[`17_2023_KATECH_DL_PM_Pedestrian_AR-HUD.md`](summaries/17_2023_KATECH_DL_PM_Pedestrian_AR-HUD.md)

📥 **本地 PDF**：[`17_2023_Augmented_Reality-Based_Navigation_Using_Deep_Learning-Based_Pedestrian_and_Pers.pdf`](papers/17_2023_Augmented_Reality-Based_Navigation_Using_Deep_Learning-Based_Pedestrian_and_Pers.pdf)

**英文摘要**：

> Recently, research on augmented reality-based head-up displays (AR-HUDs) for driving assistance has been widely conducted in the automotive industry. The disadvantage of having to look away from the road while driving can be compensated by using AR-HUD-based visualization instead of an auxiliary display on the central dashboard. As the number of personal mobility users on the road increases, and their moving speed is considerably faster than pedestrians, personal mobility makes it more difficult for the driver to cope with dangerous situations. However, there is little research work for considering personal mobility users for driving assistance. This study aims to enhance the driver’s situational awareness to respond to unexpected situation by providing driver assistance information on the AR-HUD by combining deep learning and AR. In particular, the deep learning-based anomaly detection method can recognize personal mobility users effectively. This study also investigates the driver’s understanding of the relationship between the amount of prioritized information provided to AR-HUD and situational cognitive ability. This understanding can be used to adjust the amount of information displayed on the AR-HUD to maintain drivers’ situational awareness. The proposed approach was evaluated through an online study. The results showed that the proposed deep learning-based AR-HUD system improved the driver’s situational awareness and showed advantages in driving assistance compared to...

### 🔗 [18] In‐Vehicle AR‐HUD System to Provide Driving‐Safety Information

**作者**：Hye Sun Park, Min Woo Park, Kwanghee Won, Kyong‐Ho Kim | **2013** · ETRI Journal | **被引**：120

**DOI**：[10.4218/etrij.13.2013.0041](https://doi.org/10.4218/etrij.13.2013.0041)

📰 **中文摘要**：[`18_2013_Park_车载ARHUD系统.md`](summaries/18_2013_Park_车载ARHUD系统.md)

**英文摘要**：

> Augmented reality (AR) is currently being applied actively to commercial products, and various types of intelligent AR systems combining both the Global Positioning System and computer‐vision technologies are being developed and commercialized. This paper suggests an in‐vehicle head‐up display (HUD) system that is combined with AR technology. The proposed system recognizes driving‐safety information and offers it to the driver. Unlike existing HUD systems, the system displays information registered to the driver's view and is developed for the robust recognition of obstacles under bad weather conditions. The system is composed of four modules: a ground obstacle detection module, an object decision module, an object recognition module, and a display module. The recognition ratio of the driving‐safety information obtained by the proposed AR‐HUD system is about 73%, and the system has a recognition speed of about 15 fps for both vehicles and pedestrians.

### 🔗 [19] A Review of Augmented Reality Heads Up Display in Vehicles: Effectiveness, Application, and Safety

**作者**：M. Winkler, Morteza Soleimani | **2025** · International Journal of Human-Computer Interaction | **被引**：14

**DOI**：[10.1080/10447318.2024.2443252](https://doi.org/10.1080/10447318.2024.2443252)

📰 **中文摘要**：[`19_2025_Winkler_ARHUD车载综述.md`](summaries/19_2025_Winkler_ARHUD车载综述.md)

**英文摘要**：

> This paper reviews the evolution of driver displays, focusing on the transition to Augmented Reality Heads-Up Display (AR HUD) in vehicles. It compares AR HUD with traditional HUD, emphasising safety, cognitive workload, and user experience. Particular attention is given to AR HUD’s role in automated vehicles, especially during driver handover from automated to manual driving. Findings suggest AR HUD can enhance safety and user experience when applied effectively but may increase distraction and cognitive load if misused. Benefits include improved navigation through reduced cognitive load, decreased inattentional blindness, and better obstacle detection, such as identifying pedestrians. A notable gap in the literature is that AR HUD is often studied as an extension of the main driver display rather than as a primary display. This review highlights AR HUD's potential as the sole display, emphasising the need for further research. Overall, AR HUD presents transformative possibilities for enhancing vehicle user experience.

### 📥 [20] ARive: Assisting Drivers with In-Car Augmented Reality for Risk Zone Detection

**作者**：Chao Wang, Derck Chu, Marieke Martens | **2025** · Proceedings of the ACM on Interactive Mobile Wearable and Ubiquitous Technologies | **被引**：1

**DOI**：[10.1145/3712270](https://doi.org/10.1145/3712270)

📰 **中文摘要**：[`20_2025_Honda_TUe_ARive_AR-HMD_Risk_Zone.md`](summaries/20_2025_Honda_TUe_ARive_AR-HMD_Risk_Zone.md)

📥 **本地 PDF**：[`20_2025_ARive__Assisting_Drivers_with_In-Car_Augmented_Reality_for_Risk_Zone_Detection.pdf`](papers/20_2025_ARive__Assisting_Drivers_with_In-Car_Augmented_Reality_for_Risk_Zone_Detection.pdf)

**英文摘要**：

> Human factors such as fatigue and distraction often impair drivers' ability to gauge traffic dynamics, leading to collisions, especially at unsignalized intersections. Augmented reality (AR) technology, particularly through advanced 3D projections and wearable head-mounted displays (HMDs), offers a promising enhancement by integrating comprehensive environmental awareness directly into the driver's field of view. This paper presents "ARive," an innovative AR driver-assistance system designed to improve road safety by projecting dynamic risk zones beneath other traffic participants, thus providing real-time kinematic information to promote safer driving distances and informed decision-making. The research involved developing two distinct AR designs and testing them using a fixed-base driving simulator with integrated real-time data communication. A user study with 17 participants revealed that while AR projections significantly improve distance maintenance, particularly in abrupt braking scenarios, they do not markedly affect brake response times or enhance safety during critical events. These findings suggest the need for further optimization of AR design elements to maximize effectiveness, highlighting the potential of AR in enhancing driver awareness and safety.

### 📥 [21] Differences in drivers’ dependence on AR warning information in urban driving environments: the role of driving experience

**作者**：Faren Huo, Rubanka Alla | **2025** · Frontiers in Virtual Reality | **被引**：0

**DOI**：[10.3389/frvir.2025.1638823](https://doi.org/10.3389/frvir.2025.1638823)

📰 **中文摘要**：[`21_2025_AR_Warning_Dependence_Driving_Experience.md`](summaries/21_2025_AR_Warning_Dependence_Driving_Experience.md)

📥 **本地 PDF**：[`21_2025_Differences_in_drivers’_dependence_on_AR_warning_information_in_urban_driving_en.pdf`](papers/21_2025_Differences_in_drivers’_dependence_on_AR_warning_information_in_urban_driving_en.pdf)

**英文摘要**：

> Augmented Reality Head-Up Displays (AR HUDs) have been shown to enhance drivers’ performance and road safety. However, with the growing attention to trust in automated driving systems, excessive reliance on automation may lead to complacency and dependency. This study therefore aimed to examine how drivers with different levels of experience depend on AR warning messages under varying environmental conditions (daytime vs. nighttime urban driving) and to propose strategies for optimizing AR warning interaction design. A before-and-after comparative experimental design was employed. Participants completed driving tasks involving a typical urban hazard—pedestrians suddenly running into the road—under two conditions: (1) without AR warning messages and (2) with an induced random AR warning failure in an AR message environment. The perceived time-to-pedestrian values were analyzed to quantify driving dependence. Participants were divided into experienced and novice driver groups, and the effects of driving experience and lighting condition were examined. Objectively, both experienced and novice drivers’ dependence on AR warning messages was primarily influenced by the driving environment. Under high-load conditions such as nighttime driving, both groups maintained higher attention and exhibited minimal dependence on AR warnings. Under lower-load daytime conditions, dependence varied by driving experience: experienced drivers remained self-reliant due to ingrained driving habits an...

### 🔗 [22] ARVE

**作者**：Pengyuan Zhou, Wenxiao Zhang, Tristan Braud, Pan Hui | **2018** · - | **被引**：22

**DOI**：[10.1145/3229556.3229564](https://doi.org/10.1145/3229556.3229564)

📰 **中文摘要**：[`22_2018_Zhou_ARVE车联边缘.md`](summaries/22_2018_Zhou_ARVE车联边缘.md)

**英文摘要**：

> Vehicular communication applications, be it for driver-assisting augmented reality systems or fully driverless vehicles, require an efficient communication infrastructure for timely information delivery. Centralized, cloud-based infrastructures present latencies too high to satisfy the requirements of emergency information processing and transmission. In this paper, we present a novel Vehicle-to-Edge (ARVE) infrastructure, with computational units co-located with the base stations and aggregation points. Embedding computation at the edge of the network allows to reduce the overall latency compared to vehicle-to-cloud and significantly trim the complexity of vehicle-to-vehicle communication. To demonstrate the efficiency of our solution, we apply these principles on an augmented reality head-up display. In this use case, vehicular communication is exploited to connect vehicle's vision, and quickly propagate emergency information. ARVE is a general system framework, applicable to many practical scenarios. Our preliminary evaluation shows that ARVE noticeably decreases transmission latency with reasonable capital expenditure.

### 🔗 [23] Assessing the Impact of AR HUDs and Risk Level on User Experience in Self-Driving Cars: Results from a Realistic Driving Simulation

**作者**：Seung Ju Kim, Seungju Kim, Jungseok Oh, Minwoo Seong | **2023** · Applied Sciences | **被引**：13

**DOI**：[10.3390/app13084952](https://doi.org/10.3390/app13084952)

📰 **中文摘要**：[`23_2023_Kim_ARHUD自动驾驶UX.md`](summaries/23_2023_Kim_ARHUD自动驾驶UX.md)

**英文摘要**：

> The adoption of self-driving technologies requires addressing public concerns about their reliability and trustworthiness. To understand how user experience in self-driving vehicles is influenced by the level of risk and head-up display (HUD) information, using virtual reality (VR) and a motion simulator, we simulated risky situations including accidents with HUD information provided under different conditions. The findings revealed how HUD information related to the immediate environment and the accident’s severity influenced the user experience (UX). Further, we investigated galvanic skin response (GSR) and self-reported emotion (Valence and Arousal) annotation data and analyzed correlations between them. The results indicate significant differences and correlations between GSR data and self-reported annotation data depending on the level of risk and whether or not information was provisioned through HUD. Hence, VR simulations combined with motion platforms can be used to observe the UX (trust, perceived safety, situation awareness, immersion and presence, and reaction to events) of self-driving vehicles while controlling the road conditions such as risky situations. Our results indicate that HUD information provision significantly increases trust and situation awareness of the users, thus improving the user experience in self-driving vehicles.

### 🔗 [24] The Influence of Information Redundancy on Driving Behavior and Psychological Responses Under Different Fog and Risk Conditions: An Analysis of AR-HUD Interface Designs

**作者**：Junfeng Li, Kexin Chen, Mo Chen | **2025** · Applied Sciences | **被引**：2

**DOI**：[10.3390/app152011072](https://doi.org/10.3390/app152011072)

📰 **中文摘要**：[`24_2025_Li_雾天冗余界面.md`](summaries/24_2025_Li_雾天冗余界面.md)

**英文摘要**：

> Adverse road conditions, particularly foggy weather, significantly impair drivers’ abilities to gather information and make judgments in response to unexpected events. To investigate the impact of different Augmented Reality-Head-Up Display (AR-HUD) interfaces (words-only, symbols-only, and words + symbols) on driving behavior, this study simulated driving scenarios under varying visibility and risk levels in foggy conditions, measuring reaction time (RT), time-to-collision (TTC), the maximum lateral acceleration, the maximum longitudinal acceleration, and subjective data. The results indicated that risk levels significantly affected drivers’ RT, TTC, and maximum longitudinal and lateral accelerations. The three interfaces significantly differed in RT and TTC across different risk levels in heavy fog. In light fog, words-only and redundant interfaces significantly affected RT across different risk levels; words-only and symbols-only interfaces significantly affected TTC across different risk levels. In addition, participants responded faster when using text-related interfaces in the subject’s native language. After analyzing data on perceived usability across the three interfaces, the results indicated that under high-risk conditions, both in light fog and heavy fog, participants rated the redundant interface as having higher usability and preferred the redundant interfaces. Based on these findings, this paper proposes the following design strategies for AR-HUD visual interfa...

### 📥 [25] AR DriveSim: An Immersive Driving Simulator for Augmented Reality Head-Up Display Research

**作者**：Joseph L. Gabbard, Missie Smith, Kyle Tanous, Hyungil Kim | **2019** · Frontiers in Robotics and AI | **被引**：44

**DOI**：[10.3389/frobt.2019.00098](https://doi.org/10.3389/frobt.2019.00098)

📰 **中文摘要**：[`25_2019_AR_DriveSim_Immersive_Simulator.md`](summaries/25_2019_AR_DriveSim_Immersive_Simulator.md)

📥 **本地 PDF**：[`25_2019_AR_DriveSim__An_Immersive_Driving_Simulator_for_Augmented_Reality_Head-Up_Displa.pdf`](papers/25_2019_AR_DriveSim__An_Immersive_Driving_Simulator_for_Augmented_Reality_Head-Up_Displa.pdf)

**英文摘要**：

> Optical see-through automotive head-up displays (HUDs) are a form of augmented reality (AR) that is quickly gaining penetration into the consumer market. Despite increasing adoption, demand, and competition among manufacturers to deliver higher quality HUDs with increased fields of view, little work has been done to understand how best to design and assess AR HUD user interfaces, and how to quantify their effects on driver behavior, performance, and ultimately safety. This paper reports on a novel, low-cost, immersive driving simulator created using a myriad of custom hardware and software technologies specifically to examine basic and applied research questions related to AR HUDs usage when driving. We describe our experiences developing simulator hardware and software and detail a user study that examines driver performance, visual attention, and preferences using two AR navigation interfaces. Results suggest that conformal AR graphics may not be inherently better than other HUD interfaces. We include lessons learned from our simulator development experiences, results of the user study and conclude with limitations and future work.

### 🔗 [26] Employing Emerging Technologies to Develop and Evaluate In-Vehicle Intelligent Systems for Driver Support: Infotainment AR HUD Case Study

**作者**：Vassilis Charissis, Jannat Falah, Ramesh Lagoo, Salsabeel F. M. Alfalah | **2021** · Applied Sciences | **被引**：60

**DOI**：[10.3390/app11041397](https://doi.org/10.3390/app11041397)

📰 **中文摘要**：[`26_2021_Charissis_信息娱乐ARHUD.md`](summaries/26_2021_Charissis_信息娱乐ARHUD.md)

**英文摘要**：

> The plurality of current infotainment devices within the in-vehicle space produces an unprecedented volume of incoming data that overwhelm the typical driver, leading to higher collision probability. This work presents an investigation to an alternative option which aims to manage the incoming information while offering an uncluttered and timely manner of presenting and interacting with the incoming data safely. The latter is achieved through the use of an augmented reality (AR) head-up display (HUD) system, which projects the information within the driver’s field of view. An uncluttered gesture recognition interface provides the interaction with the AR visuals. For the assessment of the system’s effectiveness, we developed a full-scale virtual reality driving simulator which immerses the drivers in challenging, collision-prone, scenarios. The scenarios unfold within a digital twin model of the surrounding motorways of the city of Glasgow. The proposed system was evaluated in contrast to a typical head-down display (HDD) interface system by 30 users, showing promising results that are discussed in detail.

### 🔗 [27] Does Augmented-Reality Head-Up Display Help? A Preliminary Study on Driving Performance Through a VR-Simulated Eye Movement Analysis

**作者**：Xiangdong Ma, Mengting Jia, Zhicong Hong, Alex Pak Ki Kwok | **2021** · IEEE Access | **被引**：37

**DOI**：[10.1109/access.2021.3112240](https://doi.org/10.1109/access.2021.3112240)

📰 **中文摘要**：[`27_2021_Ma_ARHUD布局眼动.md`](summaries/27_2021_Ma_ARHUD布局眼动.md)

**英文摘要**：

> Augmented reality heads-up display (AR-HUD) is becoming increasingly popular as a way to keep drivers focusing on roads. By overlaying visuals on the windshield, AR-HUDs improve the drivers’ view of the environment outside the car, creating a stronger sense of awareness of the surroundings. However, whether AR-HUD and to what extent different AR-HUD layouts could improve drivers’ driving performance are still questionable. Unfortunately, AR-HUD is still at a research stage, not yet fully commercialized. Hence, there are few actual products in the market available for testing. For this reason, this study developed a virtual reality driving simulator to tested drivers’ driving performance environment under three scenarios: without AR-HUD, dispersed layout (AR-HUD1), and dense layout (AR-HUD2). Twelve subjects were invited to join the experiment. Their driving performance was measured in various aspects. This study showed that AR-HUD with interfaces that conform to human-computer interaction principles and visual design rules could improve cognitive resource allocation and promote driving safety. Conversely, a poor designed AR-HUD could negatively impact driving safety.

### 🔗 [28] A Novel Active Heads-Up Display for Driver Assistance

**作者**：Anup Doshi, Shinko Y. Cheng, Mohan M. Trivedi | **2008** · IEEE Transactions on Systems Man and Cybernetics Part B (Cybernetics) | **被引**：128

**DOI**：[10.1109/tsmcb.2008.923527](https://doi.org/10.1109/tsmcb.2008.923527)

📰 **中文摘要**：[`28_2008_Doshi_主动HUD驾驶辅助.md`](summaries/28_2008_Doshi_主动HUD驾驶辅助.md)

**英文摘要**：

> In this paper, we introduce a novel laser-based wide-area heads-up windshield display which is capable of actively interfacing with a human as part of a driver assistance system. The dynamic active display (DAD) is a unique prototype interface that presents safety-critical visual icons to the driver in a manner that minimizes the deviation of his or her gaze direction without adding to unnecessary visual clutter. As part of an automotive safety system, the DAD presents alerts in the field of view of the driver only if necessary, which is based upon the state and pose of the driver, vehicle, and environment. This paper examines the effectiveness of DAD through a comprehensive comparative experimental evaluation of a speed compliance driver assistance system, which is implemented on a vehicular test bed. Three different types of display protocols for assisting a driver to comply with speed limits are tested on actual roadways, and these are compared with a conventional dashboard display. Given the inclination, drivers who are given an overspeed warning alert reduced the time required to slow down to the speed limit by 38% (p < 0.01) as compared with the drivers not given the alert. Additionally, certain alerts decreased distraction levels by reducing the time spent looking away from the road by 63% (p < 0.01). Ultimately, these alerts demonstrate the utility and promise of the DAD system.

### 📥 [29] Machine learning-based cognitive load prediction model for AR-HUD to improve OSH of professional drivers

**作者**：Jian Teng, Fucheng Wan, Yiquan Kong, Ju-Kyoung Kim | **2023** · Frontiers in Public Health | **被引**：8

**DOI**：[10.3389/fpubh.2023.1195961](https://doi.org/10.3389/fpubh.2023.1195961)

📰 **中文摘要**：[`29_2023_ML_Cognitive_Load_Prediction_AR-HUD.md`](summaries/29_2023_ML_Cognitive_Load_Prediction_AR-HUD.md)

📥 **本地 PDF**：[`29_2023_Machine_learning-based_cognitive_load_prediction_model_for_AR-HUD_to_improve_OSH.pdf`](papers/29_2023_Machine_learning-based_cognitive_load_prediction_model_for_AR-HUD_to_improve_OSH.pdf)

**英文摘要**：

> Motivation: Augmented reality head-up display (AR-HUD) interface design takes on critical significance in enhancing driving safety and user experience among professional drivers. However, optimizing the above-mentioned interfaces poses challenges, innovative methods are urgently required to enhance performance and reduce cognitive load. Description: A novel method was proposed, combining the IVPM method with a GA to optimize AR-HUD interfaces. Leveraging machine learning, the IVPM-GA method was adopted to predict cognitive load and iteratively optimize the interface design. Results: Experimental results confirmed the superiority of IVPM-GA over the conventional BP-GA method. Optimized AR-HUD interfaces using IVPM-GA significantly enhanced the driving performance, and user experience was enhanced since 80% of participants rated the IVPM-GA interface as visually comfortable and less distracting. Conclusion: In this study, an innovative method was presented to optimize AR-HUD interfaces by integrating IVPM with a GA. IVPM-GA effectively reduced cognitive load, enhanced driving performance, and improved user experience for professional drivers. The above-described findings stress the significance of using machine learning and optimization techniques in AR-HUD interface design, with the aim of enhancing driver safety and occupational health. The study confirmed the practical implications of machine learning optimization algorithms for designing AR-HUD interfaces with reduced cogni...

### 🔗 [30] Adaptive Visual Assistance System for Enhancing the Driver Awareness of Pedestrians

**作者**：Vincent Frémont, Minh-Tien Phan, Indira Thouvenin | **2019** · International Journal of Human-Computer Interaction | **被引**：22

**DOI**：[10.1080/10447318.2019.1698220](https://doi.org/10.1080/10447318.2019.1698220)

📰 **中文摘要**：[`30_2019_Fremont_自适应行人辅助.md`](summaries/30_2019_Fremont_自适应行人辅助.md)

**英文摘要**：

> In the past decade, Pedestrian Collision Warning Systems have been proposed to detect pedestrians and warn drivers of imminent collision. However, such systems are often limited by eye-off-road and cognitive overload problems. Head Up displays with augmented reality are being considered as a key technology for changing drivers’ user experiences. In this paper, we propose a new visual assistance system that can enhance drivers’ perception by dynamically directing attention to pedestrians to avoid collisions using Augmented Reality cues. The proposed system takes into account driver behaviors through vehicle driving signals analysis, in order to warn it at the right moments. To that end, we statistically model correct and incorrect driver behaviors in situations with pedestrians. Based on this model, a warning visual metaphor is displayed if unawareness is detected and a driving simulator was used to evaluate the concept. The experimental results suggest that our proposed adaptive visual aids can enhance driver awareness of pedestrians in critical situations.

### 🔗 [31] Augmented Reality for Vehicle-Driver Communication: A Systematic Review

**作者**：Liam Kettle, Yi‐Ching Lee | **2022** · Safety | **被引**：26

**DOI**：[10.3390/safety8040084](https://doi.org/10.3390/safety8040084)

📰 **中文摘要**：[`31_2022_Kettle_AR车辆沟通综述.md`](summaries/31_2022_Kettle_AR车辆沟通综述.md)

**英文摘要**：

> Capabilities for automated driving system (ADS)-equipped vehicles have been expanding over the past decade. Research has explored integrating augmented reality (AR) interfaces in ADS-equipped vehicles to improve drivers’ situational awareness, performance, and trust. This paper systematically reviewed AR visualizations for in-vehicle vehicle-driver communication from 2012 to 2022. The review first identified meta-data and methodological trends before aggregating findings from distinct AR interfaces and corresponding subjective and objective measures. Prominent subjective measures included acceptance, trust, and user experience; objective measures comprised various driving behavior or eye-tracking metrics. Research more often evaluated simulated AR interfaces, presented through windshields, and communicated object detection or intended maneuvers, in level 2 ADS. For object detection, key visualizations included bounding shapes, highlighting, or symbols. For intended route, mixed results were found for world-fixed verse screen-fixed arrows. Regardless of the AR design, communicating the ADS’ actions or environmental elements was beneficial to drivers, though presenting clear, relevant information was more favorable. Gaps in the literature that yet to be addressed include longitudinal effects, impaired visibility, contextual user needs, system reliability, and, most notably, inclusive design. Regardless, the review supports that integrating AR interfaces in ADS-equipped vehicles...

### 🔗 [32] Automotive Holographic Head‐Up Displays

**作者**：Jana Skirnewskaja, Timothy D. Wilkinson | **2022** · Advanced Materials | **被引**：75

**DOI**：[10.1002/adma.202110463](https://doi.org/10.1002/adma.202110463)

📰 **中文摘要**：[`32_2022_Skirnewskaja_全息HUD.md`](summaries/32_2022_Skirnewskaja_全息HUD.md)

**英文摘要**：

> Driver's access to information about navigation and vehicle data through in-car displays and personal devices distract the driver from safe vehicle management. The discrepancy between road safety and infotainment must be addressed to develop safely operated modern vehicles. Head-up displays (HUDs) aim to introduce a seamless uptake of visual information for the driver while securely operating a vehicle. HUDs projected on the windshield provide the driver with visual navigation and vehicle data within the comfort of the driver's personal eye box through a customizable extended display space. Windshield HUDs do not require the driver to shift the gaze away from the road to attain road information. This article presents a review of technological advances and future perspectives in holographic HUDs by analyzing the optoelectronics devices and the user experience of the driver. The review elucidates holographic displays and full augmented reality in 3D with depth perception when projecting the visual information on the road within the driver's gaze. Design factors, functionality, and the integration of personalized machine learning technologies into holographic HUDs are discussed. Application examples of the display technologies regarding road safety and security are presented. An outlook is provided to reflect on display trends and autonomous driving.

### 📥 [33] Usability Evaluation of in-Vehicle AR-HUD Interface Applying AHP-GRA

**作者**：Yunuo Cheng, Zhong Xia, Min Ye, Tian Liwei | **2022** · Human-Centric Intelligent Systems | **被引**：6

**DOI**：[10.1007/s44230-022-00011-1](https://doi.org/10.1007/s44230-022-00011-1)

📰 **中文摘要**：[`33_2022_Usability_AHP-GRA.md`](summaries/33_2022_Usability_AHP-GRA.md)

📥 **本地 PDF**：[`33_2022_Usability_Evaluation_of_in-Vehicle_AR-HUD_Interface_Applying_AHP-GRA.pdf`](papers/33_2022_Usability_Evaluation_of_in-Vehicle_AR-HUD_Interface_Applying_AHP-GRA.pdf)

**英文摘要**：

> Abstract Usability is regarded to be a fundamental requirement for in-vehicle HMIs, and usability evaluation reflects the impact of the interface and the acceptance from the users. This study introduced a usability evaluation model of AR-HUD interface by applying grey analytic hierarchy process (AHP). First, based on the ameliorated PSSUQ (Post-Study System Usability Questionnaire), the usability evaluation system was modified and optimized according to the characteristics of AR-HUD. On this basis, the preference weights for evaluation indexes were calculated by AHP and the idea of group decision. Finally, the criteria of usability were integrated into grey relational degree by applying grey relational analysis (GRA) to obtain optimal design. A case study was conducted to demonstrate the applicability of the developed model to the usability evaluation of AR-HUD interface design. According to the existing AR-HUD interface design, 7 dimensions of design elements (A-G) and 18 interface prototypes (S1-S18) were selected by Taguchi orthogonal array test (TOAT). As the results indicated, the grey relational degree of S5 was 0.923, signifying that it was the optimal sample; and the results were also compared with entropy-TOPSIS to verify the feasibility of the proposed method. The grey-based AHP evaluation model can be used to evaluate the usability level of AR-HUD interface effectively, which may help designers achieve insights for design process and samples decision-making.

### 📥 [34] Color Visibility Evaluation of In-Vehicle AR-HUD Under Different Illuminance

**作者**：Xia Zhong, Yunuo Cheng, Liwei Tian | **2022** · Proceedings of the International Conference on Information Economy, Data Modeling and Cloud Computing, ICIDC 2022, 17-19 June 2022, Qingdao, China | **被引**：6

**DOI**：[10.4108/eai.17-6-2022.2322686](https://doi.org/10.4108/eai.17-6-2022.2322686)

📰 **中文摘要**：[`34_2022_Color_Visibility_AR-HUD.md`](summaries/34_2022_Color_Visibility_AR-HUD.md)

📥 **本地 PDF**：[`34_2022_Color_Visibility_Evaluation_of_In-Vehicle_AR-HUD_Under_Different_Illuminance.pdf`](papers/34_2022_Color_Visibility_Evaluation_of_In-Vehicle_AR-HUD_Under_Different_Illuminance.pdf)

**英文摘要**：

> Drivers’ visual distraction serves as the main cause of traffic accidents, different ambient illuminance can also exert a considerable impact on the drivers’ cognition efficiency. It is therefore very important to study the color visibility of AR-HUD interface under different illuminance. In this st

### 📥 [35] Interface Design of Automobile Head-up Display from the Perspective of Human-Machine Interaction

**作者**：Lening Guan | **2024** · - | **被引**：0

**DOI**：[10.4108/eai.24-5-2024.2350098](https://doi.org/10.4108/eai.24-5-2024.2350098)

📰 **中文摘要**：[`35_2024_HUD_HMI_Interface_Design.md`](summaries/35_2024_HUD_HMI_Interface_Design.md)

📥 **本地 PDF**：[`35_2024_Interface_Design_of_Automobile_Head-up_Display_from_the_Perspective_of_Human-Mac.pdf`](papers/35_2024_Interface_Design_of_Automobile_Head-up_Display_from_the_Perspective_of_Human-Mac.pdf)

**英文摘要**：

> Under the background of user-centered era, the traditional head-down display (HDD) is gradually being replaced by head-up display (HUD). As the carrier of HUD information presentation and the medium for direct interaction with drivers, the design research of HUD interface has become increasingly imp

### 🔗 [36] Physiological Signals as Predictors of Cognitive Load Induced by the Type of Automotive Head-Up Display

**作者**：Gregor Strle, Andrej Košir, Jaka Sodnik, Kristina Stojmenova | **2023** · IEEE Access | **被引**：12

**DOI**：[10.1109/access.2023.3305383](https://doi.org/10.1109/access.2023.3305383)

📰 **中文摘要**：[`36_2023_Strle_生理信号认知负荷.md`](summaries/36_2023_Strle_生理信号认知负荷.md)

**英文摘要**：

> Visual information complexity of automotive head-up displays (HUDs) may increase cognitive load and reduce driver performance in critical situations. This study examined whether physiological indicators of cognitive load could predict the type of HUD while driving. Physiological signals of heart rate variability (HRV), electrodermal activity (EDA), skin temperature, and pupil dilation were recorded from 28 participants using a motion-based driving simulator. Two types of HUD with different information complexities were compared: baseline HUD and augmented reality HUD. Heart rate and EDA were processed to generate standardized biomedical features. Two separate sets of features were created for pupil dilation and skin temperature using time-series analysis and basic statistics. The fusion of physiological signals was used to test the impact of different signal combinations on classification performance. Three gradient boosting classifiers LightGBM (LGBM), HistGradientBoostingClassifier (HGBC), and XGBoost (XGB) were trained on physiological signals to predict the type of HUD. Classifiers based on the fusion of HRV, EDA and time-series features for skin temperature and pupil dilation achieved moderate performance, with average AUC ROC scores of XGB=0.67, LGBM=0.69, and HGBC=0.70. Classifiers based on the fusion of HRV, EDA, and the basic statistical features for skin temperature and pupil dilation achieved notable overall improvement in performance, with an average AUC ROC score...

### 📥 [37] End-to-End Pedestrian Collision Warning System based on CNN Semantic Segmentation

📰 **中文摘要**：[`37_2016_arXiv_End2End_PCW_CNN_SemSeg.md`](summaries/37_2016_arXiv_End2End_PCW_CNN_SemSeg.md)

📥 **本地 PDF**：[`37__End-to-End_Pedestrian_Collision_Warning_System_based_on_CNN_Semantic_Segmentatio.pdf`](papers/37__End-to-End_Pedestrian_Collision_Warning_System_based_on_CNN_Semantic_Segmentatio.pdf)

_(无可获取的英文摘要)_

### 📥 [38] Real-Time Predictive Pedestrian Collision Warning Service for Cooperative ITS

📰 **中文摘要**：[`38_2020_arXiv_PPCWS_3DPose.md`](summaries/38_2020_arXiv_PPCWS_3DPose.md)

📥 **本地 PDF**：[`38__Real-Time_Predictive_Pedestrian_Collision_Warning_Service_for_Cooperative_ITS.pdf`](papers/38__Real-Time_Predictive_Pedestrian_Collision_Warning_Service_for_Cooperative_ITS.pdf)

_(无可获取的英文摘要)_

### 📥 [39] Influence of Pedestrian Collision Warning Systems on Driver Behavior - Simulator Study

📰 **中文摘要**：[`39_2021_arXiv_PCW_DriverBehavior_Simulator.md`](summaries/39_2021_arXiv_PCW_DriverBehavior_Simulator.md)

📥 **本地 PDF**：[`39__Influence_of_Pedestrian_Collision_Warning_Systems_on_Driver_Behavior_-_Simulator.pdf`](papers/39__Influence_of_Pedestrian_Collision_Warning_Systems_on_Driver_Behavior_-_Simulator.pdf)

_(无可获取的英文摘要)_

---

## 5. 调研方法学

### 5.1 PDF 下载策略
- 优先级：arXiv > EuropePMC > 学术机构仓库 > 出版商网站
- 反爬处理：使用 `curl_cffi`（Chrome120 TLS 指纹）、cookie session、Referer 链
- 失败原因：MDPI 受 Akamai 严格保护；ACM/Wiley/IEEE 闭源 + 反爬；未尝试 sci-hub

### 5.2 中文摘要生成
- **已下载论文**（12 篇）：基于 PDF 全文提取，生成详细深度摘要（包含背景/方法/实验/结果/启示/局限）
- **未下载论文**（27 篇）：基于 OpenAlex/Unpaywall 提供的完整英文 abstract，生成精炼中文要点（≤500 字）

### 5.3 元数据完整性
- ✅ 39/39 论文有完整 OpenAlex 元数据
- ✅ 38/39 论文有英文摘要（仅 #14 Lübbe 2017 无 abstract）
- ✅ 39/39 论文有作者/年份/期刊/DOI
- ✅ 39/39 论文有中文摘要

---

## 6. 联系/反馈

如发现链接失效或需要补充论文，可参考：
- `papers_metadata.json`：所有论文的备用 OA 链接（`alt_oa_urls` 字段）
- `download_log.json`：每篇论文的下载尝试记录

> 本调研使用代理 `oversea-squid2.ko.txyun:11080` 完成跨境检索与下载。

