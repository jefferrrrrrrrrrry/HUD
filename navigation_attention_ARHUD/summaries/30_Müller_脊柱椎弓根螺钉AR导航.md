# 基于术中3D成像的脊柱椎弓根螺钉AR导航
**Augmented reality navigation for spinal pedicle screw instrumentation using intraoperative 3D imaging**

| 项 | 内容 |
|---|---|
| 作者 | Fabio Müller, Simon Roner, Florentin Liebmann, José M. Spirig, Philipp Fürnstahl, Mazda Farshad |
| 年份 | 2019 |
| 期刊/会议 | The Spine Journal |
| DOI | 10.1016/j.spinee.2019.10.012 |
| 引用数 | 137 |
| 本地全文 | extracted_text/30_2019_Augmented_reality_navigation_for_spinal_pedicle_screw_instrumentation_using_intraoperative_3D_imagin.txt |
| 主题组 | A_AR_HUD_navigation |

## 一、研究背景与问题
脊柱手术中椎弓根螺钉的精确植入需要极高精度，传统姿态追踪系统（PTS, pose-tracking system）借助2D监视器引导操作，但要求医生频繁切换视线于术野与显示器之间，影响操作连贯性。基于头戴式设备（HMD）的AR可将3D全息术前规划直接叠加于术者视野，理论上消除视线切换并维持术野专注。然而，已有AR导航研究多采用手动/地标/超声配准，尚未将"术中3D影像配准"——脊柱手术的现行金标准——与HMD-AR结合并与高端PTS对比。本研究问题：使用HoloLens HMD结合术中3D荧光配准的AR导航，其手术精度能否达到高端PTS（fusionTrack500）的水平？

## 二、研究方法
实验性尸体研究。3具新鲜冷冻腰椎尸体标本（T12到尾骨），每具均规划双侧L1-L5全部椎弓根（每具10枚椎弓根）。AR组：2具脊柱共20根K-wires由HMD（Microsoft HoloLens）AR全息引导；PTS组：1具脊柱共10根K-wires由Atracsys fusionTrack500 PTS引导（金标准对照）。两组均使用术中3D荧光（Ziehm Vision RFD 3D，1 mm层厚）进行配准。术前1 mm层厚CT（SOMATOM Edge Plus）生成3D三角网格模型，用CASPA软件按Weinstein技术规划螺钉轨迹（沿椎弓根中线平行椎体上缘）。脊柱嵌入非透明琼脂凝胶模拟标准后入路。AR组使用商业基准标记（IMAGE LOCK VisiMARKER）固定于棘突上，PTS组用红外反射球（ILUMARK Snap）固定于椎体侧方。术后CT扫描进行精度评估。

## 三、关键指标与测量
主要指标：3D平移误差TE（mm）= 进钉点欧氏距离；3D角度误差AE（°）= 轨迹方向向量夹角；2D轴位/矢状位投影TE与AE（用于与文献对比）；总体导航耗时（s）。同时手术医生填写主观可用性问卷（1-5分9项：配准精度、舒适度、直观性、入点可视化、轨迹可视化、时间消耗、稳定性、可行性、无菌性）。统计：Welch's t检验，p<0.05显著。

## 四、主要结果与发现
(1) 3D平移误差：AR组 M=3.4 mm, SD=1.6 mm，PTS组 M=3.2 mm, SD=2.0 mm，t检验p=0.85，差异不显著。(2) 3D角度误差：AR组 M=4.3°, SD=2.3°，PTS组 M=3.5°, SD=1.4°，p=0.30，差异不显著。(3) 2D轴位TE：AR=1.8±1.3 mm，PTS=1.6±1.0 mm；矢状TE：AR=2.6±4.7 mm，PTS=0.9±0.8 mm。(4) 轴位AE：AR=3.4±2.5°，PTS=2.4±1.4°；矢状AE：AR=2.1±1.5°，PTS=2.3±1.4°。(5) PTS组排除2例严重异常（L2右滑脱、L4右标记触碰桌面致配准漂移）。(6) 导航总时长：AR组 57.5±46.9 s vs PTS组 45±16.5 s，p=0.30。(7) 标记直接附着 vs 邻椎标记的精度无显著差异（TE p=0.63, AE p=0.85）。(8) 主观问卷均值：AR=3.4, PTS=4.0；其中AR在"系统直观性"上得5分（最高）超过PTS的4分；PTS在"配准精度视觉印象"(5)和"时间消耗"(4)上更优。Müller等结论：HMD-AR在脊柱椎弓根导航的精度可媲美高端PTS，但目前因软件稳定性、抖动、研究模式依赖等技术限制尚未达到临床应用门槛。文中亦提到"杂乱"与"全息抖动"会带来注意干扰，与Dixon等(2013)的AR注意成本观察相呼应。

## 五、对本研究"AR-HUD导航与预警注意冲突"的启示
该论文为AR-HUD（广义HMD类AR）"在视野内直接叠加导航信息"的精度可行性提供了正面证据，支持"AR导航是有潜力的"前置假设。但其也间接揭示了AR-HUD的两类风险：(1) 全息抖动（hologram jittering）在标记同时追踪时易发，可能产生类似AR-HUD预警的不稳定视觉信号，造成无意识的注意捕获；(2) 文中提及"直接术野专注无需视线切换"的优势——这正是AR-HUD相对HDD的核心价值，但也是Dixon et al.(2013)所发现的注意隧道根源。组合策略上，本文支持"AR可在精度上替代传统显示，但需附加注意管理"的设计观。
- 引用价值：★★ 弱（精度证据，与本研究核心议题距离较远）

## 六、本文局限性与未来工作
单医生操作；样本仅3具脊柱30枚螺钉；HoloLens研究模式不稳定；未引入眼动测量；未量化注意分配；未涉及IB；未考察光照、出血、呼吸伪影等真实手术场景。未来工作：自动化分割与配准、临床试验、HMD人因工效学。

## 七、与本研究主题的关联
本文聚焦AR导航精度而非注意冲突，因此在本研究中作为"AR导航技术能力"维度的背景文献，可在论证AR-HUD的发展前景或与Dixon et al.(2013)形成对照（精度收益 vs 注意成本）。可在导论或讨论中简要引用以衬托AR-HUD的"双刃剑"属性。
