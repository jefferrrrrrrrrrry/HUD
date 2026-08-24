# 第 2 周汇报：HUD 警告时机（TTC 阈值族）深化 + Kazazi (2015) 精读

**汇报周次**：W2（2026.06.28 – 2026.07.04）
**汇报对象**：[导师姓名]
**汇报人**：[学生姓名]

---

## 1. 本周目标

承接 W1 已完成的 HUD 子集 14 篇精读，本周聚焦其中 **4 篇明确量化 TTC 的文献**做证据聚合，并选取 **Kazazi (2015)** 作为本周深度精读文献：

1. 把不同车速下报告的 TTC 阈值统一换算为标准车速（50 km/h）下的距离 / 时间值
2. 引入交通工程与人因经典理论（Hayward 1972 / Hooper 1936 PIEV / Olson & Sivak 1986 / AASHTO 2.5 s）作为理论锚点
3. 评述 TTC 阈值与人因机制（PIEV 总时间约束、信号检测论 d′/β 权衡、双系统理论）的对应关系
4. **按 IMRD 范式完整精读 Kazazi (2015)**——它是 HUD 子集内唯一系统检验"警告类型 × 年龄"交互效应的实证研究
5. 形成"TTC 阈值证据表"作为论文 §2.2.1 的核心实证基础
6. 提炼本周 5 条共识

---

## 2. 4 篇 TTC 量化研究的证据聚合

### 2.1 Lübbe (2017) — TTC 1.8 / 2.5 s 二级阈值

- 实验车速：50 km/h
- 警告设计：AV 在 TTC 1.8 s 触发（Imminent 范式）；HUD 在 TTC 2.5 s 触发（Cautionary 范式）；级间 0.7 s
- **50 km/h = 13.89 m/s，Lead Time 物理换算**：
  - TTC 1.8 s → 距离 25.0 m
  - TTC 2.5 s → 距离 34.7 m
  - 级间 0.7 s → 距离差 9.7 m

### 2.2 Kazazi (2015) — flow point 触发，老年组前移 7 m

- 实验车速：30 km/h
- 警告设计：基于"flow point"（车速 × 行人横穿启动同步），非固定 TTC
- **30 km/h = 8.33 m/s，Lead Time 物理换算**：
  - 青年组：假设原触发点对应 TTC ≈ 2.0 s，则 Lead Time ≈ 16.7 m
  - 老年组：前移 7 m → Lead Time ≈ 23.7 m，等效 TTC ≈ **2.84 s**
  - 老年组所需 Lead Time 比青年组增加 **42%**（0.84 s / 2.0 s）

### 2.3 Zhang/边扬 (2024) — 100 m 距离触发（中国 V2X）

- 实验车速：60 km/h
- 警告设计：固定 100 m 距离触发（不基于 TTC）；行人在 60 m 处激活
- **60 km/h = 16.67 m/s，Lead Time**：100 m → **6.0 s**
- 远超 Lübbe（2.5 s）与 Kim 2018（5.0 s）的主流上限——V2X 架构 + 雾天场景 + 隐藏行人叠加的保守裕量（详见 W1 §6）

### 2.4 Ma (2021) — 未量化 TTC（Duration 主题）

- Ma 未明确报告 TTC 阈值，仅以速度分级（<75 / 75–100 / >100 km/h）关联 FOV
- 本节仅将其作为"速度自适应"思路的代表，不进入证据聚合表的核心条目——W3 深度展开

### 2.5 证据聚合表

将上述 4 篇 HUD 量化研究换算到统一维度，配合基于人因机制的解释。

| 文献 | 实验车速 | TTC 触发值 | 等价 50 km/h 距离 | 实测平均 PRT | 安全裕量 = TTC − PRT − t_brake* | 人因机制对应 |
|---|---|---|---|---|---|---|
| Lübbe (2017) L2 | 50 km/h | **1.8 s (Imminent)** | 25.0 m | 0.80 s (SD=0.29) | 1.8 − 0.8 − 0.7 = **0.3 s** | 临界级：PIEV 全部 + 制动响应紧贴 |
| Lübbe (2017) L1 | 50 km/h | **2.5 s (Cautionary)** | 34.7 m | – | 2.5 − 1.5 − 0.7 = **0.3 s** | 提示级：PIEV 完成 + 警告读取留 0.3 s |
| Kazazi (2015) 青年 | 30 km/h | ~2.0 s (推算) | 16.7 m | ~1.1 s | 2.0 − 1.1 − 0.7 = **0.2 s** | 接近 AASHTO 临界 |
| Kazazi (2015) 老年 | 30 km/h | **~2.84 s** | 23.7 m | ~1.4 s | 2.84 − 1.4 − 0.7 = **0.74 s** | 老年 PRT 延长补偿 |
| Zhang/边扬 (2024) | 60 km/h | **~6.0 s** | 83.3 m | 未报告 | 6.0 − 1.5 − 1.3 = **3.2 s** | 远超 PIEV 需求（雾天 / V2X 冗余） |

*注：t_brake = 50 km/h 下紧急制动响应时间，取经验值 0.5–0.7 s；60 km/h 下取 1.3 s

### 2.6 关键发现

**发现 1：TTC 1.8–2.5 s 的"PIEV 物理下界"约束**
- 临界级 TTC（Lübbe 1.8 s）= 普通 PRT 1.0 s + 制动响应 0.7 s + 极小裕量 0.1 s
- 提示级 TTC（Lübbe 2.5 s）= 设计 PRT 1.5 s + 制动响应 0.7 s + 警告读取 0.3 s
- **这不是工程巧合，而是 PIEV 总时间的物理累加约束**

**发现 2：老年 / 分心条件需 TTC 前移 0.3–1.0 s**
- Kazazi 老年组前移 7 m（30 km/h 下 +0.84 s）
- Lee (2002) 元分析：分心条件 PRT 延长 0.5–1.0 s
- 推论：**老年 + 分心组合条件**理论上 TTC 阈值应达 3.0–3.5 s

**发现 3：100 m 距离触发（Zhang/边扬）的"过度冗余"**
- 60 km/h 下 100 m = 6.0 s Lead Time，超 PIEV 物理需求 ~3.5 s
- 解释：V2X 架构 + 雾天能见度低 + 隐藏行人（详见 W1 §6）
- **中国 V2X 场景下的 6 s Lead Time 是否代表本土偏好，需 RQ3 中国样本实验进一步验证**

---

## 3. 与人因理论的对应关系

### 3.1 PIEV 模型对 TTC 下界的约束（Hooper 1936; Olson & Sivak 1986）

PIEV 总时间（PRT）= Perception + Identification + Emotion + Volition：
- **Perception**：感觉器官捕捉刺激，~150–300 ms（Posner 1980）
- **Identification**：识别为危险目标，~300–500 ms
- **Emotion + Volition**：决策与执行动作启动，~500–700 ms
- **合计**：1.0–1.5 s（普通），1.5–2.5 s（分心 / 老年）

加上车辆制动响应（0.5–1.3 s）与极小安全裕量，**最低 TTC ≈ 1.5–3.0 s**——这与 Lübbe (1.8 s) 与 Kazazi 老年组 (2.84 s) 的实证完全一致。

### 3.2 信号检测论 SDT 对 TTC 选择的解释（Green & Swets 1966）

设 PCW 系统的 TTC 阈值为 τ：
- τ 越大（如 5.0 s）：灵敏度 **d′ 高**（更少漏报），但虚警率 **FAR 上升** → 驾驶员信任降低（Bliss 2003：FAR > 30% 时信任显著下降）
- τ 越小（如 1.0 s）：判据 **β 严格**（虚警少），但漏报风险陡增 → 极端情境下"无救援区"

**Kim (2018) 的双阈值方案（2.5 + 5.0 s）实际是 SDT 框架下的"双判据"设计**：
- 5.0 s 优化 d′（发现潜在危险，Cautionary）
- 2.5 s 优化 β（仅强警告真正紧迫，Imminent）

### 3.3 双系统理论对 TTC 时机的认知映射（Kahneman & Tversky 1974）

- **System 1（快思考）**：< 1 s 反应，无意识 / 经验启发式
- **System 2（慢思考）**：> 2 s 反应，有意识 / 分析判断

PCW 时间设计的 System 映射：
- TTC ≤ 1.8 s：**仅 System 1 可用**（紧急制动，Imminent）
- TTC = 2.5–5.0 s：**System 2 介入空间**（判断"是否真危险"，Cautionary）
- TTC > 5.0 s：可能产生过度审议，反而错过最佳响应窗口

**这是 Lübbe (2017) 选择 2.5 s 作为 Cautionary 阈值的认知机制依据**——既允许 System 2 介入做信息校验，又不至于过早进入"过度审议"模式。

---

## 4. Kazazi (2015) 精读汇报（IMRD 完整展开）

本节按学术论文的**引言—方法—结果—讨论**四段范式完整汇报 Kazazi (2015)，重点回答四个问题：
- **引言**：为什么在 HUD 子集内挑年龄这个变量？研究缺口是什么？
- **方法**：老年 vs 青年设计有什么方法学优势与局限？
- **结果**：警告 × 年龄交互效应到底如何？
- **讨论**：Kazazi 提出的 cascade 是什么？对本研究的启示？

### 4.1 Introduction（引言）

#### 4.1.1 研究背景

- **城市道路是事故最集中的场景**——信息密度高、注意力被多重交通元素瓜分
- 既有研究确认 HUD 相比 HDD 在反应时上有显著优势——Liu & Wen (2004) 报告 HUD 缩短反应时 0.8–1.0 s
- **HUD 显示警告应"支持而不分心"**——位置（HUD/HDD）、模态（视觉/听觉/触觉）、信息类型（文字/符号）都需斟酌
- **交通标志被认为是直观的警告图形**——驾驶员每天接触并已有条件反射式反应

#### 4.1.2 研究缺口

**老年驾驶员**的信息处理速度较慢（Rackoff 1974; Schlag 1993; Caird 2007），可能需要不同的警告策略；同时老年驾驶员往往**通过简化驾驶任务（如降速）来代偿**。但既有研究未系统检验"警告类型 × 年龄"的交互效应——这构成本文的直接切入点。

Kazazi 的研究是 UR:BAN 项目框架下的第二篇——第一篇是 Winkler (2015) 姊妹论文（青年组基线），本文在此基础上扩展到老年组做代际对比。

#### 4.1.3 研究问题

1. 警告系统能否减少老年与年轻驾驶员在不同临界程度场景下的碰撞？
2. 警告符号是否需要对老年与年轻驾驶员有所区别？
3. 何种警告符号在 BRT 与最大制动量上最有效？

#### 4.1.4 研究假设

- **H1**：Stop 标志（SW）能引发快而强的紧急制动
- **H2**：Caution 标志（CW）让驾驶员注意但不一定急刹
- **H3**：老年驾驶员或受益于"更强提示"（SW），年轻人或受益于"留有判断空间"（CW）

### 4.2 Method（方法）

#### 4.2.1 被试

- **老年组**：N = 36（男 29 / 女 7），平均年龄 71.9 岁（SD = 4.4），年里程约 12,000 km
- **年轻组**：N = 36（男 20 / 女 16），平均年龄 23.9 岁（SD = 4.2），年里程约 6,000 km
- 全部经过 25 分钟模拟器训练
- **排除**：16 名老年 + 2 名年轻被试因晕动症被排除（老年组排除率显著高，是本研究的选择偏倚风险）
- 视力正常或矫正；报酬：巧克力 / 每小时 8 € / 学分

#### 4.2.2 实验设计

- **类型**：被试间设计，2（年龄：老 / 青）× 3（警告类型：Control / SW / CW）
- 每个年龄组下的每个警告条件约 12 人
- **自变量**：警告类型 / 年龄
- **因变量**：碰撞次数 / BRT 制动反应时 / 最大制动量（%）
- **统计**：GLM + χ²（碰撞）；α = 0.05

#### 4.2.3 实验材料与设备

- **驾驶模拟器**：Braunschweig 工业大学固定底座中等保真模拟器；180° 投影，三 LCD 后视镜；SILAB 软件；自动挡
- **HUD 警告规格**：
  - **位置**：道路上方，不遮挡真实交通灯或标志
  - **持续时间**：取决于驾驶员速度——警告在两个 flow point 之间持续，若驾驶员停车则警告持续更长
  - **仅视觉**（无听觉，避免高频警告烦扰）
  - SW 尺寸：19.9 × 17.7 cm；CW 尺寸：21 × 19 cm
  - SW = 标准 Stop 标志；CW = 内含相应危险图标（行人 / 车辆 / 障碍物）的 Caution 三角
- **4 个场景（criticality 递增 / 递减）**：
  1. **Pedestrian 1（critical）**：左转时行人横穿
  2. **Pedestrian 2（very critical）**：泊车后突然冲出行人——**对老年组警告时机比年轻组提前 7 m 触发**
  3. **Vehicle（less critical）**：前车突然停车
  4. **Obstacle（less critical）**：山丘后突然出现的稻草捆

#### 4.2.4 一个重要方法学局限（confound）

**Pedestrian 2 场景下，老年组的警告触发点比青年组提前 7 m**。这是因为之前 UR:BAN 团队的青年基线实验发现警告太晚，作者为老年组做了"补偿"——但这引入了 confound：老年组不仅"年龄不同"，还"警告更早"，两个因素在该场景下无法解耦。这一点在 §4.4 讨论段有明确影响。

### 4.3 Results（结果）

**Kazazi 报告三类因变量**——救命层（碰撞数）、认知层（BRT 制动反应时）、力学层（最大制动量）——与 Lübbe 三层结构一致。

#### 4.3.1 救命层：碰撞数

- **老年组整体碰撞数低于年轻组**——老年组通过"降速代偿"简化任务
- **Pedestrian 1**：Control 组年轻组碰撞显著多于老年组（χ² = 6.75, p = 0.027）；SW / CW 组无显著年龄差异
- **Pedestrian 2**（very critical）：Control 组年轻碰撞显著多于老年（χ² = 6.75, p = 0.027）；**SW 组年轻碰撞显著多于老年**（χ² = 6.32, p = 0.037）——可能因为老年组警告时机提前 7 m
- **Vehicle**：无显著差异
- **Obstacle**：所有人都未碰撞

#### 4.3.2 认知层：BRT 制动反应时

| 场景 | 警告类型主效应 | 年龄主效应 | W × A 交互 |
|---|---|---|---|
| Pedestrian 1 | F(2,60) = 3.68, p = 0.032, η² = 0.120 | n.s. | **F = 4.64, p = 0.014, η² = 0.147** |
| Pedestrian 2 | F(2,72) = 7.59, p = 0.001, η² = 0.187 | n.s. | n.s. |
| Vehicle | F(2,62) = 9.71, p < 0.001, η² = 0.258 | F(1,62) = 10.66, p = 0.002 | n.s. |
| Obstacle | F(2,70) = 10.85, p < 0.001, η² = 0.253 | n.s. | n.s. |

**关键交互效应**（Pedestrian 1，critical）：
- **老年组**：SW 最快、CW 反而比 Control 更慢（意外结果）
- **年轻组**：CW 最快、SW 中等
- **直接验证 H3**：老年偏好强提示 SW、年轻偏好留判断空间 CW

**整体平均 BRT**：Control 1.9 s → SW 1.2 s → CW 1.4 s（**SW 最快**）

#### 4.3.3 力学层：最大制动量

- **Pedestrian 1**：W × A 交互（F = 3.89, p = 0.026）——老年组 SW 最高、CW 反而比 Control 还低；年轻组 CW 最高
- **Pedestrian 2**：SW vs Control p = 0.031；CW vs Control p = 0.046
- **Vehicle**：SW vs Control p < 0.001；老年组整体制动量低（35.6% vs 65.2%）——因速度低
- **Obstacle**：SW vs Control p < 0.001；SW vs CW p < 0.001

**整体平均**：SW > CW > Control

#### 4.3.4 因变量的实际意义（分层解读）

| # | 因变量 | 反映驾驶员的什么真实情况 |
|---|---|---|
| ① | **碰撞数** | 救命终局。老年组底数低是"降速代偿"结果，不能全部归因到"感知能力更强" |
| ② | **BRT 制动反应时** | 认知处理速度。**"警告类型 × 年龄"交互揭示：不同年龄对图形语义的敏感度不同**——老年组熟悉 Stop 标志（多年经验），青年组能理解 Caution 的"提前提示"含义 |
| ③ | **最大制动量** | 力度指标。SW 引发"急刹"（力度大），CW 引发"缓刹"（力度中等）——**验证 H1（SW 强）与 H2（CW 弱）的图形语义假设** |

### 4.4 Discussion（讨论）

#### 4.4.1 Kazazi 的核心提议：警告级联（cascade）

Kazazi 在讨论段明确提出——**先呈现 CW（Cautionary Warning）引导注意，如果驾驶员对 CW 未做反应（如轻踩刹车不足），再升级触发 SW（Stop Warning）**。这个 cascade 机制与 Lübbe (2017) 的"Cautionary 2.5 s → Imminent 1.8 s"双阶段是**同源思路**——共同构成"分级警告"的实证基础。

**但 Kazazi 的 cascade 只是提议而未做实证测试**——她的实验里 SW 和 CW 是独立呈现的，没有测试"CW 后无反应触发 SW"的时间参数。

#### 4.4.2 Kazazi 自陈的四个局限

1. **触发用 flow point 而非 TTC**，警告时机随速度变化不严格量化——未来应统一基于 TTC
2. **Pedestrian 2 老 / 青警告时机不同**（老年前移 7 m），比较受限——年龄和触发时机两个因素混淆
3. **老年志愿者可能"健康选择偏倚"**——16 名老年因晕动被排除，且性别比严重不均（男女 29:7）
4. **顺序未平衡**——为聚焦警告效应，作者放弃了顺序平衡

#### 4.4.3 对本研究（HUD/AR-HUD 时间元素设计规范）的三个具体启示

**启示 1（继承）：年龄应作为本研究的显式因变量或调节变量**

Kazazi 首次实证证明"警告类型 × 年龄"交互存在——老年偏好强提示、青年偏好留判断空间。**建议**：本研究 RQ3 应包含年龄或"经验（新手 vs 熟练）"维度，验证 Kazazi 的代际交互在中国样本 + AR-HUD 环境中是否复现。

**启示 2（补空白）：cascade 的级间时间参数是 RQ2 的直接空白**

Kazazi 和 Lübbe 都独立提出了 cascade 机制，但两者都没有把"级间时间"作为独立自变量做过对照。**建议**：RQ2 应把 cascade 的级间间隔作为核心自变量做 **4 档对照（0.5 / 0.7 / 1.0 / 1.5 s）**——首次同时补 Lübbe 与 Kazazi 两条线的空白。

**启示 3（方法学规范）：所有年龄组必须共用完全相同的触发时机**

Kazazi 的老年组触发前移 7 m 引入了年龄 × 时机的 confound——即使她后续分析已经识别这一问题，但已经无法在数据层面完全解耦。**建议**：本研究方法学应严格保持所有条件下（不同年龄、不同分心水平、不同车速）**触发时机完全一致**——如果需要考察时机效应，应把它作为独立自变量而非"补偿参数"。

---

## 5. 本周共识（Weekly Consensus）

本周提炼 5 条核心共识：

1. **主流 HUD 警告时机边界由 PIEV 物理下界约束**——Imminent 落在 1.8-2.8 s（PRT 1.0 + 制动 0.7 + 裕量 0.1），Cautionary 落在 2.5-5.0 s（PRT 1.5 + 制动 0.7 + 读取 0.3）；这些数值不是工程巧合而是人因累加。

2. **TTC 阈值是"年龄 × 分心 × 场景"的多元函数**——老年 PRT 延长 0.3-0.5 s（Kazazi 实证 +0.84 s），分心 PRT 延长 0.5-1.0 s（Lee 2002 元分析）；极端条件理论需 3.0-3.5 s。

3. **Kazazi (2015) 首次实证证明"警告类型 × 年龄"交互效应存在**——Pedestrian 1 critical 场景下老年偏好 SW 强提示（F = 4.64, p = 0.014）、青年偏好 CW 留判断空间；这是本研究 RQ3 应包含年龄/经验维度的直接证据。

4. **警告级联（cascade）机制被 Lübbe 与 Kazazi 独立提出但级间时间未量化**——Lübbe 的 0.7 s 是"派生量"，Kazazi 只是提议未实证；本研究 RQ2 应把级间间隔作为核心自变量做 0.5/0.7/1.0/1.5 s 四档对照。

5. **Kazazi 的老年组触发前移 7 m 引入 confound**——本研究方法学应严格保持所有条件的触发时机完全一致；若考察时机效应应作为独立自变量而非"补偿参数"。

---

## 6. 下周（W3）计划

**主题**：HUD 持续时长（Duration）深化 + Ma (2021) 精读

**具体任务**：
1. 引入 Ma (2021) 作为 HUD 子集内唯一明确量化 Duration 的研究——按 IMRD 完整精读
2. 分析 Ma 2021 的"3 s 常规 + 10-15 s 紧急"设计依据（引用 Wickens 2002 多资源理论）
3. 引入习惯化（Sokolov 1963 匹配-不匹配模型）与虚警疲劳（Bliss 2003）作为 Duration 上界理论
4. 引入注意定向（Posner 1980 ~150–300 ms 视觉处理时间）作为 Duration 下界理论
5. 论证 Duration 作为本研究 RQ1 核心切入点的优势

**说明**：按本周新采用的"每周一篇重点精读"节奏，闪烁频率与 onset-offset 动画维度不再作为独立主题展开——它们在 HUD 子集报告率为 0%，暂搁置。

**预期产出**：W03_HUD持续时长_频率_动画.md（含 Ma 2021 IMRD 精读 + Duration 上下界理论 + 本周共识 5 条）

---

## 7. 本周引用 References

Bliss, J. P. (2003). Investigation of alarm-related accidents and incidents in aviation. *International Journal of Aviation Psychology*, *13*(3), 249–268. https://doi.org/10.1207/S15327108IJAP1303_04

Caird, J. K., Chugh, J. S., Wilcox, S., & Dewar, R. E. (2007). A design guideline and evaluation framework to determine the relative safety of in-vehicle intelligent transportation systems for older drivers. *Human Factors*, *49*(6), 902–927.

Green, D. M., & Swets, J. A. (1966). *Signal detection theory and psychophysics*. Wiley.

Hayward, J. C. (1972). Near-miss determination through use of a scale of danger. *Highway Research Record*, *384*, 24–34.

Hooper, K. G. (1936). *Driver perception-reaction time*. Institute of Transportation Engineers.

Kahneman, D., & Tversky, A. (1974). Judgment under uncertainty: Heuristics and biases. *Science*, *185*(4157), 1124–1131. https://doi.org/10.1126/science.185.4157.1124

Kazazi, J., Winkler, S., & Vollrath, M. (2015). Accident prevention through visual warnings: How to design warnings in head-up display for older and younger drivers. In *2015 IEEE 18th International Conference on Intelligent Transportation Systems* (pp. 1028–1034). IEEE. https://doi.org/10.1109/itsc.2015.171

Kim, H., Gabbard, J. L., Anon, A. M., & Misu, T. (2018). Driver behavior and performance with augmented reality pedestrian collision warning: An outdoor user study. *IEEE Transactions on Visualization and Computer Graphics*, *24*(4), 1515–1524. https://doi.org/10.1109/tvcg.2018.2793680

Lee, J. D., McGehee, D. V., Brown, T. L., & Reyes, M. L. (2002). Collision warning timing, driver distraction, and driver response to imminent rear-end collisions in a high-fidelity driving simulator. *Human Factors*, *44*(2), 314–334. https://doi.org/10.1518/0018720024497844

Liu, Y.-C., & Wen, M.-H. (2004). Comparison of head-up display (HUD) vs. head-down display (HDD): Driving performance of commercial vehicle operators in Taiwan. *International Journal of Human-Computer Studies*, *61*(5), 679–697.

Lübbe, N. (2017). Brake reactions of distracted drivers to pedestrian forward collision warning systems. *Journal of Safety Research*, *61*, 23–32. https://doi.org/10.1016/j.jsr.2017.02.002

Ma, X., Jia, M., Hong, Z., Kwok, A. P. K., & Yan, M. (2021). Does augmented-reality head-up display help? A preliminary study on driving performance through a VR-simulated eye movement analysis. *IEEE Access*, *9*, 129951–129964. https://doi.org/10.1109/access.2021.3112240

Olson, P. L., & Sivak, M. (1986). Perception-response time to unexpected roadway hazards. *Human Factors*, *28*(1), 91–96. https://doi.org/10.1177/001872088602800110

Posner, M. I. (1980). Orienting of attention. *Quarterly Journal of Experimental Psychology*, *32*(1), 3–25.

Rackoff, N. J. (1974). *An investigation of age-related changes in drivers' visual search behavior*. Human Factors Research Report 1974/29.

Schlag, B. (1993). Elderly drivers in Germany: Fitness and driving behavior. *Accident Analysis & Prevention*, *25*(1), 47–55.

Winkler, S., Kazazi, J., & Vollrath, M. (2015). Distractive or supportive — How warnings in the head-up display affect drivers' gaze and driving behavior. In *2015 IEEE 18th International Conference on Intelligent Transportation Systems* (pp. 1035–1040). IEEE. https://doi.org/10.1109/itsc.2015.172

Zhang, Y., Bian, Y., Zhao, X., Li, X., & Zhang, J. (2024). Improving pedestrian safety with head-up display warning in a connected environment. *International Journal of Human-Computer Interaction*. Advance online publication. https://doi.org/10.1080/10447318.2024.2368910

---

*汇报状态：W2 完成（2026.07.04），沿用 W1 引入的"每周一篇重点精读 + IMRD 完整展开 + 5 条本周共识"结构*
*下次汇报：W3（2026.07.11），主题 = HUD 持续时长深化 + Ma (2021) IMRD 精读*
