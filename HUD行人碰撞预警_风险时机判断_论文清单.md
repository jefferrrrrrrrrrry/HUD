# HUD 行人碰撞预警——风险时机判断 相关论文清单

> 检索时间：2026-08-21 | 来源：CrossRef, OpenAlex, arXiv
> 检索关键词：HUD / AR-HUD / Pedestrian Collision Warning / Forward Collision Warning / Time-to-Collision (TTC) / Warning Timing / Driver Response / Risk Judgment

---

## 一、预警时机（TTC 阈值）与驾驶员反应

### 1. Differences in Drivers' Pedestrian Avoidance Response Based on Warning Timing, Stimulus-Response Compatibility and Drivers' Distraction
- **作者**: Hyunmin Kang, Kwanghee Han, Jaesik Lee
- **期刊**: Korean Journal of Industrial and Organizational Psychology, Vol.29(2)
- **DOI**: `10.24230/kjiop.v29i2.257-277`
- **核心**: 对比听觉行人碰撞预警系统中 **TTC 2秒 vs 4秒** 对驾驶员规避反应的影响，发现 **4秒 TTC 条件更可靠**，刺激-反应不兼容的预警方式更有效；视觉分心对规避能力损害最大。

### 2. Brake Reactions of Distracted Drivers to Pedestrian Forward Collision Warning Systems
- **作者**: Nils Lubbe
- **期刊**: Journal of Safety Research, 2017年6月
- **DOI**: `10.1016/j.jsr.2017.02.002`
- **核心**: 研究分心驾驶员对行人前向碰撞预警系统的制动反应特性。

### 3. Effects of Collision Warning System under Different Warning Timing on Driving Speed and Distance
- **作者**: Zhang Yuting, Li Xiaomeng, Yan Xuedong, Xue Qingwan
- **会议**: 2015 International Conference on Transportation Information and Safety (ICTIS)
- **DOI**: `10.1109/ictis.2015.7232174`
- **核心**: 不同预警时机下碰撞预警系统对驾驶速度和跟车距离的影响。

### 4. Forward Collision Warning System Considering Both Time-to-Collision and Safety Braking Distance
- **作者**: Yuan-Lin Chen, Kun-Yuan Shen, Shun-Chung Wang
- **会议/期刊**: IEEE ICIEA 2013 / International Journal of Vehicle Safety
- **DOI**: `10.1109/iciea.2013.6566508` / `10.1504/ijvs.2013.056968`
- **核心**: 提出同时考虑 TTC 和安全制动距离的前向碰撞预警算法。

### 5. A-TTC: A Multimodal Fusion Framework for Personalized Truck Forward Collision Warning via Dynamic Threshold Calibration
- **作者**: Yibing Wang, Qi He, Jingqiu Guo, Mark Stevenson, Yan Xu
- **DOI**: `10.2139/ssrn.6351998`
- **核心**: 提出 **驾驶员自适应 FCW 框架（A-TTC）**，通过多模态注意力网络检测驾驶员状态，混合 Gradient-Boosting + Convolutional-Transformer 预测反应时间和制动距离，动态调整 time-to-avoidance 阈值。**正式发表版（*Accid. Anal. Prev.* 2026, 236:108635）**报告：行为类别识别 84.80%、RMSE 较 LSTM 降 51.8%、总体准确率 81.42%、事件级骚扰报警占比 13.74%、威胁事件召回 89.25%（569 辆卡车 / 3,519 条视频核验事件）。**早期 SSRN 预印本的「误报率 25.16% → 12.21%」在正式版中已被删除，不可引用。**

### 6. Alarm Timing, Trust and Driver Expectation for Forward Collision Warning Systems
- **作者**: Genya Abe, John Richardson
- **期刊**: Applied Ergonomics, 2006年9月
- **DOI**: `10.1016/j.apergo.2005.11.001`
- **核心**: 研究前向碰撞预警系统中报警时机与驾驶员信任和期望的关系，经典论文。

### 7. The Human Factors of Collision Warning Systems: System Performance, Alarm Timing, and Driver Trust
- **作者**: Genya Abe, John Richardson
- **来源**: PsycEXTRA Dataset, 2004
- **DOI**: `10.1037/e577202012-006`
- **核心**: 碰撞预警系统的人因研究，涵盖系统性能、报警时机和驾驶员信任。

### 8. Improvement of Warning Lag Time in Forward Collision Warning Systems Based on Multifunctional Warnings
- **作者**: Peachanika Thammakaroon, Poj Tangamchit
- **会议**: IEEE ICVES 2012
- **DOI**: `10.1109/icves.2012.6294314`
- **核心**: 基于多功能预警改善前向碰撞预警系统的预警延迟时间。

---

## 二、HUD / AR-HUD 碰撞预警显示

### 9. An Efficient Visual Forward Collision Warning Display for Vehicles
- **作者**: Henrik Lind
- **会议**: SAE Technical Paper 2007-01-1105
- **DOI**: `10.4271/2007-01-1105`
- **核心**: 对比四种 FCW 视觉预警显示（**CWHUD、方向盘、仪表、高位下视**），发现 **碰撞预警HUD（CWHUD）制动反应时间低200ms，漏警率最低（1次漏警 vs HHDD 17次），用户偏好度最高**。

### 10. Driver Behavior and Performance with Augmented Reality Pedestrian Collision Warning: An Outdoor User Study
- **作者**: Hyungil Kim, Joseph L. Gabbard, Alexandre Miranda Anon, Teruhisa Misu
- **期刊**: IEEE Transactions on Visualization and Computer Graphics, 2018年4月
- **DOI**: `10.1109/tvcg.2018.2793680`
- **核心**: 户外实车研究，评估 AR 行人碰撞预警对驾驶员行为和性能的影响。

### 11. Casting Shadows: Ecological Interface Design for Augmented Reality Pedestrian Collision Warning
- **作者**: Hyungil Kim, Jessica D. Isleib, Joseph L. Gabbard
- **会议**: 2016 IEEE Virtual Reality (VR)
- **DOI**: `10.1109/vr.2016.7504725`
- **核心**: 提出基于生态界面设计的 AR 行人碰撞预警（投射阴影提示），评估其对风险感知的效果。

### 12. Investigating the Effect of Urgency and Modality of Pedestrian Alert Warnings on Driver Acceptance and Performance
- **作者**: David R. Large, Hyungil Kim, Coleman Merenda, Samantha Leong, Catherine Harvey, Gary Burnett, Joseph L. Gabbard
- **期刊**: Transportation Research Part F: Traffic Psychology and Behaviour, 2018
- **DOI**: `10.1016/j.trf.2018.09.028`
- **核心**: 研究行人预警的紧迫程度和呈现模态对驾驶员接受度和性能的影响。Nottingham 与 Virginia Tech 联合研究。

### 13. Effects of Visual Crowding and Stimulus Location on Driver Pedestrian Perception in AR-HUD Warning
- **作者**: 鲍威宇
- **期刊**: Advances in Psychology, 2024
- **DOI**: `10.12677/ap.2024.148539`
- **核心**: 研究 AR-HUD 预警中视觉拥挤和刺激位置对驾驶员行人感知的影响。

### 14. Spatial Plane Positioning of AR-HUD Graphics: Implications for Driver Inattentional Blindness in Navigation and Collision Warning Scenarios
- **作者**: Menlong Ye, Jun Yin
- **期刊**: Electronics
- **DOI**: `10.3390/electronics14234768`
- **核心**: AR-HUD 图形空间平面位置对驾驶员无意视盲的影响。水平平面位置对注意力盲视无显著影响，但碰撞预警图形的垂直平面位置提供最佳用户体验和最低工作负荷。

### 15. Effect of AR-HUD Warning Information Presentation Modes on Driver Situation Awareness under Single-Hazard Scenarios
- **作者**: Chang Shen, Hua Qin, Shijiao Li, Xipu Shi, Chuanyu Zou, Linghua Ran
- **会议**: AHFE International — Usability and User Experience
- **DOI**: `10.54941/ahfe1008065`
- **核心**: 研究 AR-HUD 预警信息闪烁模式对打破认知隧道效应的影响，发现 **50%占空比闪烁模式效果最优**，在高沉浸分心条件下将反应时间缩短近一半。

### 16. Estimation of Driver Awareness of Pedestrian for an Augmented Reality Advanced Driving Assistance System
- **作者**: Minh Tien Phan
- **机构**: Université de Compiègne（法国）
- **DOI**: `10.70675/a7d4e2caz40d9z4210z8fb2z164f9a83bf26`
- **核心**: 博士论文，提出 **AR-PCW 系统**概念——基于驾驶员对行人意识/无意识状态估计（DAP/DUP）来决定 AR 预警时机，使用 SVM/HMM 建模。25名驾驶员参与模拟器实验，AR 提示在感知、警觉和预期三个层面改善 DAP。

### 17. Augmented Reality Cues and Elderly Driver Hazard Perception
- **作者**: Mark Christopher Schall Jr.
- **DOI**: `10.17077/etd.tbjq72y2`
- **核心**: AR 提示对老年驾驶员危险感知的影响研究。

### 18. Head-up Displays (HUD) in Driving
- **作者**: Marcos Maroto, Enrique Caño, Pavel González, Diego Villegas
- **来源**: arXiv:1803.08383, 2018
- **核心**: 综述 HUD 在驾驶中的信息呈现方式研究，指出信息呈现的**时间、方式和通道**对驾驶安全至关重要，提出上下文感知的多模态主动推荐系统解决方案。

---

## 三、行人碰撞预警算法与系统

### 19. Pedestrian and Cyclist Forward Collision Warning System Effectiveness Estimation Based on Simulation of Kinematic Reconstructions
- **作者**: François Char
- **机构**: Aix-Marseille（法国）
- **DOI**: `10.70675/3b5791f1z1884z4ee3z8ff1z001f38f0b61c`
- **核心**: 基于 **3700+ 事故重建仿真**（2200起自行车 + 1500起行人），评估行人/骑行者 FCW 系统有效性，分析 **FCW 触发时机**和紧急制动时长的最优参数。200名参与者驾驶模拟器实验，分析注视、FCW 响应、制动反应时间。

### 20. The Development of Parameters and Warning Algorithms for an Intersection Bus-Pedestrian Collision Warning System
- **作者**: Chien-Yen Chang, Ting-Wei Chang
- **机构**: Chung Hua University, Taiwan
- **DOI**: `10.4018/978-1-4666-2649-2.ch011`
- **核心**: 交叉路口公交行人碰撞预警系统的参数分析和预警算法设计，包含**感知-反应时间、紧急减速率和行人步行速度**等基本参数。

### 21. Parameters Analysis for an Intersection Bus-Pedestrian Collision Warning System
- **作者**: Chien-Yen Chang, Ting-Wei Chang
- **会议**: 2009 IEEE Asia-Pacific Services Computing Conference (APSCC)
- **DOI**: `10.1109/apscc.2009.5394118`

### 22. End-to-End Pedestrian Collision Warning System Based on a Convolutional Neural Network with Semantic Segmentation
- **作者**: Heechul Jung, Min-Kook Choi, Kwon Soon, Woo Young Jung
- **来源**: arXiv:1612.06558, 2016
- **核心**: 基于语义分割的端到端行人碰撞预警 CNN 框架，有效减少误报。

### 23. Machine Learning-Based Pedestrian Intention Prediction Models for Collision Warning at Unsignalized Crosswalks
- **作者**: Sami Haktan Cangut, Yalçın Alver
- **会议**: Road and Rail Infrastructure IX (CETRA 2026)
- **DOI**: `10.5592/co/cetra.2026.1849`
- **核心**: 使用 BiLSTM / Social-LSTM / Transformer 预测行人过街意图（4835条观测），Social-LSTM 精度 85.02%、F1=84.57%，为碰撞预警时机判断提供可靠的意图预测输入。

### 24. Influence of Pedestrian Collision Warning Systems on Driver Behavior: A Driving Simulator Study
- **作者**: Snehanshu Banerjee, Mansoureh Jihani, Nashid K. Khadel, Md. Muhib Kabir
- **来源**: arXiv:2112.09074, 2021
- **核心**: 93名参与者驾驶模拟器研究，PCW 系统显著影响减速时间和减速率。使用 Log-logistic AFT 模型计算减速时间。

### 25. V2P Collision Warnings for Distracted Pedestrians: A Comparative Study with Traditional Auditory Alerts
- **作者**: Novel Certad, Enrico Del Re, Joshua Varughese, Cristina Olaverri-Monreal
- **来源**: arXiv:2504.13906, 2025
- **核心**: 车对行人（V2P）碰撞预警与传统听觉警报的比较，V2P 对手机分心行人特别有效。

### 26. Early Warning of Pedestrians and Cyclists
- **作者**: Joerg Christian Wolf
- **来源**: arXiv:2107.05186, 2021
- **核心**: 探索对驾驶员发出行人/骑行者**早期预警**所需的条件，指出通过位置可靠预测行人意图是核心挑战。

### 27. Sensor Fusion-Based Pedestrian Collision Warning System with Crosswalk Detection
- **作者**: Shige Suzuki, Pongsathorn Raksincharoensak, Ikuo Shimizu, Masao Nagai, Rolf Adomat
- **会议**: 2010 IEEE Intelligent Vehicles Symposium
- **DOI**: `10.1109/ivs.2010.5548120`

### 28. A Reinforcement Learning-Based Adaptive Forward Collision Warning System by Considering Drivers' Reaction Time in Real Time
- **作者**: Yi-Han Sun, Xia Wu, Si-Yuan Gong, Rui Yang
- **期刊**: CICTP 2023
- **DOI**: `10.1061/9780784484869.024`
- **核心**: 基于强化学习的自适应前向碰撞预警系统，**实时考虑驾驶员反应时间**调整预警逻辑。

### 29. Pedestrian Collision Warning of Advanced Driver Assistance Systems
- **作者**: Ying-Che Kuo, Ci-Ming Fu, Cheng-Tao Tsai, Chun-Cheng Lin, Gih-Hao Chang
- **会议**: 2016 International Symposium on Computer, Consumer and Control (IS3C)
- **DOI**: `10.1109/is3c.2016.189`

### 30. Research on Pedestrian Vehicle Collision Warning Based on Path Prediction
- **作者**: Yue Zhang, Xu Wang, Kaimin Zhuo, Wenjian Jiao, Wenxin Yang
- **会议**: 2023 7th ICTIS
- **DOI**: `10.1109/ictis60134.2023.10243767`
- **核心**: 基于路径预测的行人车辆碰撞预警研究。

### 31. A Real-Time Predictive Pedestrian Collision Warning Service for Cooperative Intelligent Transportation Systems Using 3D Pose Estimation
- **作者**: Ue-Hwan Kim, Dongho Ka, Hwasoo Yeo, Jong-Hwan Kim
- **来源**: arXiv:2009.10868, 2020
- **核心**: 基于 3D 姿态估计的实时预测性行人碰撞预警服务（P2CWS），方向识别 89.3% 准确率、意图预测 91.28% 准确率。

### 32. Predictive Safety-Aware Transmit Rate Control Scheme for Real-Time Proactive Forward Collision Warning System
- **作者**: Yang-Jun Joo, Dong-Kyu Kim, Eui-Jin Kim
- **DOI**: `10.2139/ssrn.4927850`
- **核心**: 面向 V2X 前向碰撞预警的预测性安全感知发送速率控制方案，根据预测碰撞风险自适应调整信标频率。

### 33. Development of Forward-Collision Avoidance Warning System Adapted for Driver Characteristics
- **作者**: Noboru Miyoshi, Masao Nagai, Takeyoshi Kamada, Hidehisa Yoshida
- **会议**: SAE Technical Paper 2005-08-0554
- **DOI**: `10.4271/2005-08-0554`
- **核心**: 适应驾驶员特性的前向碰撞预警系统开发。

---

## 四、综述与人因研究

### 34. Recent Advances in Connected and Automated Vehicles
- **作者**: David L. Elliott, Walter Keen, Lei Miao
- **期刊**: Journal of Traffic and Transportation Engineering (English Edition), 2019
- **DOI**: `10.1016/j.jtte.2018.09.005`
- **核心**: CAV 领域综述，涵盖行人检测与保护、碰撞避免等子方向。

### 35. Autonomous Vehicles That Interact with Pedestrians: A Survey of Theory and Practice
- **作者**: Amir Rasouli, John K. Tsotsos
- **期刊**: IEEE Transactions on Intelligent Transportation Systems, 2019
- **DOI**: `10.1109/tits.2019.2901817`
- **核心**: 自动驾驶车辆与行人交互的综述，分析行人行为因素和视觉感知推理算法。

### 36. Negotiation and Decision-Making for a Pedestrian Roadway Crossing: A Literature Review
- **作者**: Roja Ezzati Amini, Christos Katrakazas, Constantinos Antoniou
- **期刊**: Sustainability, 2019
- **DOI**: `10.3390/su11236713`
- **核心**: 行人过街协商与决策的文献综述，识别影响人车交互的关键因素。

### 37. Effectiveness of Forward Obstacles Collision Warning System Based on Deceleration for Collision Avoidance
- **作者**: Shota Takada, Toshihiro Hiraoka, Hiroshi Kawakami
- **机构**: Kyoto University
- **核心**: 基于减速度的前方障碍物碰撞预警系统有效性评估。

### 38. A Comparison of Different Informative Vibrotactile Forward Collision Warnings: Does the Warning Need to Be Linked to the Collision Event?
- **作者**: Rob Gray, Cristy Ho, Charles Spence
- **期刊**: PLoS ONE, 2014
- **DOI**: `10.1371/journal.pone.0087070`
- **核心**: 比较不同振动触觉前向碰撞预警信号，研究与碰撞事件关联的预警对制动反应时间的影响。CV-linked 的预警显著加快反应。

### 39. Human Factors in Forward Collision Warning Systems: Operating Characteristics and User Interface Requirements
- **作者**: ADAS Committee
- **标准**: SAE Information Report J2400
- **DOI**: `10.4271/j2400_200308`
- **核心**: SAE 标准报告，描述 FCW 操作员界面要素及预警系统的测试方法。

### 40. Collision Warning with Full Auto Brake and Pedestrian Detection — A Practical Example of Automatic Emergency Braking
- **作者**: Erik Coelingh, Andreas Eidehall, Mattias Bengtsson
- **会议**: 2010 13th International IEEE Conference on Intelligent Transportation Systems
- **DOI**: `10.1109/itsc.2010.5625077`

---

## 关键发现摘要

| 维度 | 核心结论 |
|------|---------|
| **TTC 阈值** | 4秒 TTC 比 2秒 TTC 更安全可靠，预警越早驾驶员反应越从容（Kang et al.） |
| **动态阈值** | 固定 TTC 阈值不适配异质驾驶员，A-TTC 等框架通过多模态融合动态调整，可在维持威胁事件召回 89.25% 的同时把事件级骚扰报警占比压到 13.74%（正式版口径；**无固定阈值对照基线**） |
| **HUD vs 其他显示** | 碰撞预警 HUD（CWHUD）制动反应时间比仪表/方向盘显示低约 200ms，漏警率最低（Lind, 2007） |
| **AR-HUD 设计** | 预警图形的空间位置、闪烁模式（50%占空比最优）显著影响驾驶员情境意识（Shen et al.） |
| **驾驶员状态感知** | 视觉分心对规避能力损害最大；预警需适应驾驶员意识状态（DAP/DUP），Phan 提出 AR-PCW 系统 |
| **行人意图预测** | 基于深度学习的行人意图预测（F1>84%）可为预警时机判断提供可靠输入（Cangut & Alver, 2026） |
| **大规模验证** | 3700+ 事故重建 + 200人模拟器实验验证 FCW 触发时机最优参数（Char） |
| **预警时机与信任** | 早期研究（Abe & Richardson）奠定预警时机对驾驶员信任和期望影响的理论基础 |
