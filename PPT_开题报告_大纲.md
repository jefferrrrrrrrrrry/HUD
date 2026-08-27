# 开题报告 PPT 大纲

> **⚠ 编号与结构均属旧版（2026-08 修订前）**：本文档采用更早的「实验1 时间／实验2a·2b 空间／实验3 交互」三实验方案，与现行「实验 1–5」五实验方案**不可逐项对应**，故未随全库重编号改写，仅作决策过程留档。以现行编号为准的文档为 `AR-HUD行人碰撞预警_毕业论文研究框架.md` 与 `thesis/第2章_文献综述_v2.md`。


**题目**：HUD/AR-HUD 行人碰撞预警的时间-空间元素设计规范研究  
**风格参考**：周颖-开题-0830.pptx（5 大 section 结构）  
**版面**：16:9，13.3"×7.5"

---

## 全册结构（5 大 Section / 35-40 页）

| 节 | 范围 | 页数 |
|---|---|---|
| **Section 1** 研究背景与意义 | Slides 3-6 | 4 |
| **Section 2** 文献综述 | Slides 8-22 | 15 |
| **Section 3** 研究问题与框架 | Slides 24-26 | 3 |
| **Section 4** 研究方案 | Slides 28-38 | 11 |
| **Section 5** 工作计划 | Slides 40-41 | 2 |

---

## 完整逐页大纲

### Slide 1：封面
```
HUD/AR-HUD 行人碰撞预警的时间-空间元素设计规范研究

答辩人：[姓名]
指导老师：[导师]
2026年[月]
```

### Slide 2：目录 Contents
```
1 研究背景与意义
2 文献综述
3 研究问题
4 研究方案
5 研究工作计划与进度安排
```

---

## ▶ Section 1：研究背景与意义（Slides 3-6）

### Slide 3：节封面 "1. 研究背景与意义"

### Slide 4：研究背景
```
HUD/AR-HUD技术正快速进入量产车型
- 据IDC预测，2030年全球AR-HUD装机量将达[X]百万套
- 2024年蔚来、奔驰、奥迪等品牌已大规模量产
- 行人事故是道路致死的第一大成因（WHO 2023：35%）

AR-HUD为行人碰撞预警提供新的可能性
- 共形增强（contact-analog）：将虚拟图形与真实行人在视野中精准对齐
- 无需视线下移，减少注意力切换成本
- (Kim et al., 2018; Wu et al., 2024)
```
**图示**：AR-HUD车型实景照片 + 行人共形警示对比图

### Slide 5：研究问题的现实困境
```
然而 AR-HUD 行人预警的"时空设计规范"尚未确立

· 时间维度争议：
  - 何时出现？TTC=2.5s vs 5.0s（Kim, 2018）vs 100m前提示（Zhang, 2024）
  - 持续多久？显示到危险解除 vs 固定3-15s（Ma, 2021）
  - 是否分级？两级 vs 三级 vs 不分级
· 空间维度争议：
  - 锁定方式：屏幕固定 vs 行人共形 vs 路面共形（Wu, 2024）
  - 颜色编码：单色红 vs 红黄绿渐变（Ma, 2024）vs 优先级编码（Chen, 2025）
  - 动效：静态 vs 动态共形跟随 vs 闪烁（Huo & Alla, 2025）
```

### Slide 6：研究意义
```
理论意义
- 整合时间×空间维度，建立HUD/AR-HUD行人预警的统一设计框架
- 验证经典视觉注意理论（Wickens多资源、Mack & Rock非注意盲视）在AR-HUD场景的适用性

实践意义
- 为量产车AR-HUD的HMI设计提供量化规范（颜色RGB/形状/FOV/TTC阈值）
- 重点服务新手驾驶员（占国内新增驾照70%）的安全需求

应用价值
- 输出可被ISO 15008/SAE J2400等标准引用的设计参数表
```

---

## ▶ Section 2：文献综述（Slides 7-22）

### Slide 7：节封面 "2. 文献综述"

### Slide 8：文献综述总览（PRISMA-like流程）
```
检索关键词：HUD AR-HUD pedestrian collision warning + …
检索时间：2008-2025
数据库：Web of Science / Scopus / IEEE Xplore / OpenAlex / CNKI
最终纳入：40篇核心文献

按时间分布：
  2008-2015: 4篇（早期）
  2016-2020: 12篇（兴起期）
  2021-2025: 24篇（爆发期）
```
**图示**：年份分布柱状图 + 主题词云

### Slide 9：核心概念界定（1）— 时间维度
```
TTC（Time-to-Collision，碰撞时间）
  定义：以当前相对速度恒定计算，车辆与目标到达同一位置的剩余时间
  来源：Hayward (1972) 在 Highway Research Record 首次提出
  公式：TTC = d / v_rel
  典型应用：碰撞预警触发阈值（2-5s常用范围）

PRT (Perception-Reaction Time)
  来源：Hooper (1936) PIEV模型 (Perception-Identification-Emotion-Volition)

TTFF (Time to First Fixation)
  来源：眼动追踪研究的标准指标 (Rayner, 1998)
```

### Slide 10：核心概念界定（2）— 空间维度
```
共形/接触类比 (Contact-Analog, Tönnis et al., 2007)
  定义：虚拟图形与真实世界对象在视野中精确对齐
  
锁定方式分类：
  · 屏幕固定 (screen-fixed)
  · 行人锁定 (pedestrian-conformal)  
  · 路面锁定 (road-conformal)
  · 世界锁定 (world-conformal)

FOV (Field of View, 视场角)
  HUD虚像可见的水平×垂直角度
  量产HUD典型：10-20°×3-5°（Maybach), AR-HUD: 25-40°×7-12°
```

### Slide 11：文献综述（1）警告出现时机
```
固定TTC阈值类研究：
  Kim et al. (2018): 2.5s/5.0s双距离条件
  Lübbe (2017): 2.5s cautionary → 1.8s imminent，间隔0.7s
  Huo & Alla (2025): TTC=2.5s/34.72m

固定距离阈值类研究：
  Phan et al. (2016): TTC=2s 或 距离=16.6m （取最早）
  Zhang et al. (2024): 100m前语音预警 + 60m行人激活

自适应触发类：
  Frémont et al. (2019): 基于头眼监测的自适应触发
  Doshi et al. (2008): 主动注视方向跟踪
```
**问题提出 1**：警告出现时机的最优TTC阈值是多少？是否随驾驶员经验/场景变化？

### Slide 12：文献综述（2）警告持续时长 & 分级
```
持续时长：
  · 至危险解除模式（多数研究）：Kim 2018, Phan 2016, Zhang 2024
  · 固定时长模式：Ma (2021) 3s常规/10-15s紧急

分级警告设计：
  · 两级（cautionary → imminent）：Lübbe 2017 (0.7s间隔)
  · 三级威胁等级：Yoon 2014（未量化阈值）
  · 颜色×饱和度渐变三级：Ma 2024 (Phase1黄 → Phase2红)
  · 优先级多目标分级：Chen et al. 2025 ← 新颖
```
**问题提出 2**：分级警告的级别数与级别间隔如何最优化？

### Slide 13：文献综述（3）色彩编码
```
单色警示主流：
  · 红色 (Kim 2018, Wu 2024 RGB(255,0,0))
  · 黄色 (Phan 2016)

分级配色：
  · 红/黄/绿+饱和度 (Ma 2024 EID 'carpet')
  · 4色HEX分区 (Teng 2023 #2979FF/#FE0000/#4ADE80/#F26D21)
  · 红=紧急 + 青蓝=辅助 (Ma 2021)

色彩可见度专题：
  Zhong (2022): 7色×3描边×2照度Lv测量，FOV 12°×5°
  100,000lx vs 30lx下颜色排序差异
```

### Slide 14：文献综述（4）形状与动效
```
形状对比：
  · Bounding box (矩形包围框)
  · Contact-Analog (与目标共形)
  · Virtual Shadow / Dome+tether (Kim 2016/2018)
  · 三角形 / Stop sign (Kazazi 2015)
  · 多元图标组合 (Ma 2024 EID 'carpet')

动效设计：
  · 静态 vs 动态共形（多数研究偏好动态）
  · 闪烁注意捕获 (Huo & Alla 2025)
  · 跟随距离缩放 (Kim 2018)
```

### Slide 15：文献综述（5）空间分布
```
平面定位：
  Ye & Yin (2025 idx 09): 垂直面 vs 水平面 vs 混合面
  → 水平面（路面投射）显著降低inattentional blindness

锁定方式对比：Wu et al. (2024 idx 08)
  BD（驾驶员视线固定）vs BR（路面投射）vs BW（行人跟随）
  → BW（行人锁定）右转场景显著优于BD/BR
  首次注视时间：BW=616ms vs BD=2562ms vs BR=2729ms

FOV分级：
  Ma (2021): 65°（低速）/40°（高速）
  Teng (2023): 85°/65°/40°（速度三段）
```
**问题提出 3**：空间锁定方式与FOV如何匹配不同的驾驶场景？

### Slide 16：文献综述（6）驾驶员个体差异
```
新手 vs 熟练驾驶员：
  · Chen et al. (2024 idx 07): N=48新手，contact-analog在行人场景下反应更快
  · Chen et al. (2025 idx 40)：N=45新手，分级优先级显著优化反应时
  · Huo & Alla (2025 idx 21): 新手对AR预警依赖度更高

老年 vs 年轻：
  · Kazazi (2015): 老年对flow-point触发感受不同

环境差异：
  · 雾天/夜间：Zhang (2024)雾天HUD优势更显著
  · 城市/高速：不同FOV与TTC需求
```

### Slide 17：文献综述（7）认知负荷
```
眼动指标：
  · 首次注视时间TTFF
  · 注视次数Fixation count
  · 扫视次数Saccade count
  · 注视熵Gaze entropy (Shannon, 1948)

生理指标：
  · 瞳孔直径
  · 心率/HRV
  · 皮电反应（GSR/EDA）
  · EEG（Strle 2023 idx 36）

主观量表：
  · NASA-TLX
  · SUS
  · DALI（专用驾驶量表）
```

### Slide 18：研究空白与共识
```
已有共识：
  ✓ 共形增强 > 屏幕固定
  ✓ TTC=2.5s是常用触发点
  ✓ 红色用于紧急警示
  ✓ AR预警显著提升新手驾驶员表现

研究空白：
  ✗ 时间×空间维度的交互效应未系统研究
  ✗ 多目标场景下的优先级设计研究极少（仅Chen 2025）
  ✗ 中国驾驶员（特别是新手）的本土数据稀缺
  ✗ 量化的、可被标准引用的设计参数表缺失
```

### Slide 19：本研究的理论基础
```
1. Multiple Resource Theory (Wickens, 2002)
   → AR-HUD占用视觉空间-中央资源，但避免下视占用空间-外周

2. Inattentional Blindness Theory (Mack & Rock, 1998)
   → 非共形显示导致驾驶员忽视真实行人

3. Contact-Analog/Conformal Display Theory (Tönnis et al., 2007)
   → 与真实对象一一对应的虚拟显示降低认知映射成本

4. PIEV / Reaction Time Model (Hooper, 1936)
   → 警告时机需为感知-识别-决策-行动提供足够时间
```

---

## ▶ Section 3：研究问题（Slides 21-23）

### Slide 20：节封面 "3. 研究问题"

### Slide 21：研究问题汇总
```
基于文献综述识别的三个核心问题：

问题1：AR-HUD警告时机如何影响驾驶员对横穿行人的响应？
  · 不同TTC阈值（1.5s / 2.5s / 5.0s）的对比
  · 是否随驾驶员经验调整？

问题2：AR-HUD空间锁定方式如何影响行人感知？
  · 屏幕固定 vs 行人锁定 vs 路面锁定
  · 在不同FOV与转向场景下的差异

问题3：时间×空间设计因素是否存在交互效应？
  · 早警告+屏幕固定 vs 晚警告+行人锁定
  · 多目标场景下的优先级编码
```

### Slide 22：研究框架（图）
```
            驾驶员因素 (新手 vs 熟练)
                    ↓
        ┌─── 时间设计 ───┐    ┌─── 空间设计 ───┐
   IV1: TTC阈值              IV2: 锁定方式
   IV2: 分级方式              IV3: 颜色编码
                    ↓
              驾驶绩效 + 注意分配
              · 制动反应时SRT
              · 最小TTC
              · TTFF/注视熵
              · NASA-TLX
                    ↓
              ┌─ 实验1: 时间维度 ─┐
              ├─ 实验2: 空间维度 ─┤
              └─ 实验3: 交互效应 ─┘
```

---

## ▶ Section 4：研究方案（Slides 24-35）

### Slide 23：节封面 "4. 研究方案"

### Slide 24：研究总览
```
研究一：警告时机研究
  · 实验1：TTC阈值与驾驶绩效

研究二：空间锁定与共形设计研究
  · 实验2a：屏幕固定 vs 共形（驾驶员经验调节）
  · 实验2b：FOV分级与场景匹配

研究三：时间×空间交互效应
  · 实验3：多目标场景的优先级编码（参照Chen 2025）
```

### Slide 25：实验1 — 警告时机研究
```
实验1：AR-HUD 警告出现时机对驾驶绩效的影响

研究目的：
  探究不同TTC阈值下AR-HUD警告对驾驶员制动反应的影响

研究方法：
  实验设计：3（TTC：1.5s/2.5s/4.0s）×2（驾驶经验：新手/熟练）混合
  被试：60名（g*power计算）
  IV：TTC触发阈值
  控制变量：车速50km/h、行人触发距离、AR图形（红色bounding box）
  DV：刹车反应时SRT、最小TTC、最大减速度、首次制动距离

实验材料：STISIM驾驶模拟器 + AR-HUD（垂直虚像面，FOV 12°×5°）
被试任务：单目标横穿行人场景，10个trial/条件
数据分析：2×3混合ANOVA + post-hoc

预期结果：
  TTC=2.5s 显著优于1.5s（更早响应）和4.0s（避免误警）
  新手×短TTC交互效应显著
```

### Slide 26：实验2a — 空间锁定方式
```
实验2a：AR-HUD空间锁定方式与驾驶员经验交互

研究目的：
  探究不同锁定方式（屏幕固定/行人锁定/路面锁定）的认知负荷与绩效

实验设计：3（锁定：BD/BR/BW，参照Wu 2024）×2（经验：新手/熟练）混合
被试：54名
IV：锁定方式
DV：
  · 行为：刹车反应时、最小TTC
  · 眼动：TTFF、注视次数、注视熵Gaze entropy
  · 主观：NASA-TLX、SUS

实验材料：HTC VIVE Pro Eye + Tobii Pro Lab
场景：直行/左转/右转三种（参照Wu 2024）
图形规格：红色RGB(255,0,0) bounding box，TTC<3s触发

预期结果：
  BW（行人锁定）在转向场景下显著优于BD/BR
  新手对BW的依赖度更高
```

### Slide 27：实验2b — FOV与场景匹配
```
实验2b：FOV分级与速度场景的匹配

研究目的：探究最优FOV与车速的匹配关系

实验设计：3（FOV：12°/25°/40°）×3（车速：30/60/90km/h）组内
被试：36名
IV：FOV、车速
DV：识别正确率、首次注视时间、主观可用性
控制：颜色、形状、锁定方式（均固定为BW行人锁定）

实验材料：可调FOV的AR-HUD仿真平台
预期结果：
  低速下窄FOV足够；高速需宽FOV
  FOV×车速交互效应显著
```

### Slide 28：实验3 — 多目标优先级编码
```
实验3：多目标场景下的优先级颜色编码（拓展Chen 2025）

研究目的：
  探究分级颜色优先级在多目标AR-HUD警告中的效用，并扩展至中国驾驶员样本

实验设计：3（警告模式：Equivalent/Hierarchical/Baseline）×2（目标数量：2/3）混合
被试：60名新手驾驶员
IV：
  · 警告模式（参照Chen 2025）
  · 目标数量
DV：反应时、saccade counts、gaze entropy、TTFF

实验材料：
  · AR增强驾驶视频（参照Chen 2025范式）
  · Hierarchical模式：红=最高优先级，黄=次优先级，绿=低优先级
  · Equivalent模式：所有目标同色（红）

数据分析：2×3混合ANOVA + Tukey HSD
预期结果：
  Hierarchical在3目标场景下显著优于Equivalent
  复制并扩展Chen 2025结论
```

### Slide 29：实验技术路线图
```
准备阶段（M1-M3）：
  - 文献综述完善
  - 实验平台搭建（STISIM + AR-HUD + Tobii）
  - 刺激材料制作
  - 预实验

数据收集（M4-M9）：
  - 实验1（M4-M5）：60被试
  - 实验2a（M6）：54被试
  - 实验2b（M7）：36被试  
  - 实验3（M8-M9）：60被试

分析与写作（M10-M12）：
  - 数据清洗与统计分析
  - 论文撰写与修改
```

### Slide 30：变量与统计方法汇总表
```
| 实验 | 设计 | N | 主要DV | 统计 |
|---|---|---|---|---|
| 1 | 3×2混合 | 60 | SRT,TTC,deceleration | 2×3 ANOVA |
| 2a | 3×2混合 | 54 | SRT,TTFF,gaze entropy,NASA-TLX | 2×3 ANOVA |
| 2b | 3×3组内 | 36 | 识别率,TTFF | 3×3 RM-ANOVA |
| 3 | 3×2混合 | 60 | RT,saccade,gaze entropy | 2×3 ANOVA |
```

---

## ▶ Section 5：工作计划（Slides 32-33）

### Slide 31：节封面 "5. 研究工作计划与进度安排"

### Slide 32：工作计划与进度安排（Gantt图）
```
任务                    M1 M2 M3 M4 M5 M6 M7 M8 M9 M10 M11 M12
文献综述完善            ■■■■
实验平台搭建            ■■■■
预实验                    ■■
实验1数据采集                ■■■■
实验2a数据采集                    ■■
实验2b数据采集                      ■■
实验3数据采集                          ■■■■
数据分析                          ■■■■■■■■■■■■
论文撰写                              ■■■■■■■■■■
论文修改与答辩准备                            ■■■■
```

### Slide 33：预期产出
```
学术成果：
  · 1篇 SSCI 二区论文（IJHCI/Ergonomics/Applied Ergonomics）
  · 1篇 中文核心论文（《心理学报》/《人类工效学》）
  · 1篇 会议论文（CHI/AutomotiveUI）

应用产出：
  · AR-HUD 行人预警时空设计规范（草案）
  · 可复用的AR驾驶模拟实验平台
```

### Slide 34：Thanks ！
```
敬请老师们提出宝贵意见

致谢：[导师]、[实验室]、[资助来源]
```

---

## PPT 制作技术规范

- **版面**：16:9 (13.3" × 7.5")
- **字体**：标题=思源宋体36pt；正文=思源黑体16pt；引用=14pt
- **配色**：深蓝色主调（参照周颖PPT）+ 红/黄/绿强调色
- **图表**：使用 matplotlib 生成统一风格
- **引用风格**：所有引用APA 7th格式

## 文件输出

- Markdown 大纲：`/home/gezhuocheng/moe/HUD/PPT_开题报告_大纲.md`（本文档）
- 实际PPTX：`/home/gezhuocheng/moe/HUD/PPT_开题报告_HUD_AR-HUD时空设计规范.pptx`
