# 准备好接管：使用抬头显示让驾驶员在自动驾驶中执行非驾驶相关任务
**Get Ready for Take-Overs: Using Head-Up Display for Drivers to Engage in Non–Driving-Related Tasks in Automated Vehicles**

| 项 | 内容 |
|---|---|
| 作者 | Li, X., Schroeter, R., Rakotonirainy, A., Kuo, J., & Lenné, M. G. |
| 年份 | 2021 |
| 期刊/会议 | Human Factors |
| DOI | 10.1177/00187208211056200 |
| 引用数 | 21 |
| 本地全文 | extracted_text/17_2021_Get_Ready_for_Take-Overs_Using_Head-Up_Display_for_Drivers_to_Engage_in_NonDriving-Related_Tasks_in_.txt |
| 主题组 | B_attentional_capture_driving + E_transparency_luminance + F_traffic_density_complexity |

## 一、研究背景与问题（[基于摘要推断]）
自动驾驶技术的进展使驾驶员可在自动模式下从事非驾驶相关任务（NDRT），但接管控制仍可能在特定条件下被请求。如何让驾驶员在 NDRT 与紧急接管之间快速切换，成为自动驾驶 HMI 设计的关键。传统手机型 NDRT 平台与车辆操作环境相互脱离，可能延长接管响应时间；HUD 因与车辆环境集成被认为更利于注意快速回归道路。Li 等（2021）旨在系统比较 HUD 与手机两种 NDRT 平台对驾驶员状态（认知负荷、生理唤醒）与接管绩效（手 / 脚反应时）的影响，并探索状态指标与接管绩效的相关性。

## 二、研究方法（[基于摘要推断]）
模拟器实验，使用 Advanced Driving Simulator 配合真实道路录制视频。被试 46 人，每位完成 3 次驾驶：(1) HUD 条件——NDRT 嵌入式 HUD 显示；(2) 手机条件——NDRT 在独立手持设备上呈现；(3) 基线——无 NDRT。采集的客观指标包括眼动数据（视线分布、眨眼率）与生理数据（ECG 心电、EDA 皮电活动）。接管绩效用两个反应时衡量：手反应时（hand reaction time）与脚反应时（foot reaction time）。研究采用被试内重复测量设计。统计：重复测量 ANOVA + 相关分析。

## 三、关键指标与测量（[基于摘要推断]）
关键指标：(1) 接管手反应时、脚反应时（s）；(2) 认知负荷（眼动 + 主观）；(3) 生理唤醒（ECG HR、EDA SCL）；(4) 视线分布（路面、HUD/手机 AOI）。状态指标与接管绩效进行 Pearson 相关分析。

## 四、主要结果与发现（[基于摘要推断]）
N=46。**接管反应时**：HUD 条件显著缩短手反应时与脚反应时（vs 手机条件，p<0.05）。**驾驶员状态**：与基线相比，HUD 条件下认知负荷与生理唤醒水平更低，说明 HUD 集成方式让驾驶员在 NDRT 时仍保持对车辆环境的边缘觉察，状态切换成本低。**相关性**：自动驾驶阶段（TOR 之前）驾驶员的视觉行为与皮电活动均与后续接管反应时显著相关——视线越偏离前方、皮电唤醒越高（或越低），后续接管越慢，提示前驱状态可预测接管绩效。摘要明确："HUD significantly shortened the take-over reaction times compared to the mobile phone condition"，"drivers in the HUD condition also experienced lower cognitive workload and physiological arousal"。具体数值（M、SD、F、p）需查阅期刊原文，本笔记主要基于摘要。

## 五、对本研究"AR-HUD导航与预警注意冲突"的启示
本研究为"HUD 作为多任务整合平台"提供间接但关键的支持：(1) 证明把 NDRT 信息搬到 HUD 上可显著缩短接管反应时（与本研究"导航 + 紧急预警"同源场景结构类似——都涉及 HUD 上两类信息的注意切换）；(2) 提供"前驱视觉/生理指标可预测注意切换效率"的方法学线索，可用于本研究的眼动 + 生理双通道指标设计；(3) 提醒注意捕获/抑制策略不仅作用于即时反应时，还会通过减少认知负荷与唤醒度间接影响安全；(4) 支持本研究"基于状态的自适应 AR-HUD"思路——根据驾驶员状态动态调整导航元素显著度，可同时降低分心代价与提升预警响应。
- 引用价值：★★★★ 强相关

## 六、本文局限性与未来工作
样本量中等（46），仅在 Advanced Driving Simulator 测试，使用真实道路视频但仍非真实驾驶；NDRT 设计偏视觉单一；未操纵 HUD 内信息显著度或透明度，无法直接验证"信号抑制"机制。未来需在真实道路、加入显著度操控、扩展样本至老年/新手。

## 七、与本研究主题的关联
本文是 HUD 在多任务自动驾驶情境的代表性研究，与本研究"AR 导航与紧急预警注意冲突"在结构上同源（两类 HUD 信息切换），其反应时与生理指标方法论可直接借鉴。

