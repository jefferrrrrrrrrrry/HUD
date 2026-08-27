#!/usr/bin/env python3
"""重建研究汇报 deck：14 讲述页（新页序）+ 10 备查页（自旧 deck 搬运）。"""
import re
from pathlib import Path

P = Path("研究汇报_2026_08.html")
s = P.read_text(encoding="utf-8")

i = s.index('<div id="stage">') + len('<div id="stage">')
j = s.rindex("</section>") + len("</section>")
head, mid, tail = s[:i], s[i:j], s[j:]
old = re.findall(r'<section class="slide.*?</section>', mid, re.S)
assert len(old) == 21, len(old)

# ── 新增样式：参数页四行制 ──────────────────────────────────
CSS = """/* 参数页：四行制（已定／未定／取值／去处） */
.p4{display:flex;flex-direction:column;flex:1 1 auto}
.p4 .row{display:flex;gap:16px;padding:12px 0;border-bottom:1px solid #EAEAEA}
.p4 .row:last-child{border-bottom:0}
.p4 .lb{flex:0 0 82px;font-size:13.5px;font-weight:700;line-height:1.5;padding-top:3px}
.p4 .tx{flex:1 1 auto;font-size:16px;line-height:1.76}
.lb.s1{color:var(--green)} .lb.s2{color:var(--red)}
.lb.s3{color:var(--blue-d)} .lb.s4{color:var(--purple)}
/* 封面上的核心问题 */
.cover .q{
  background:var(--blue-l);border-left:4px solid var(--blue);text-align:left;
  padding:15px 20px;font-size:16.5px;line-height:1.8;color:var(--blue-d);max-width:940px;margin:0 auto;
}
.cover .rq{max-width:940px;margin:16px auto 0;text-align:left;font-size:14px;line-height:1.86;color:#444}
.cover .rq b{color:var(--blue-d)}
"""
head = head.replace('.m{font-family:', CSS + '.m{font-family:')

T0 = '<span class="m">t<sub>0</sub></span>'
DT = '<span class="m">Δt</span>'


def crumb(kind, title, tag):
    return (f'  <h1 class="crumb">{kind}<em>{title}</em>'
            f'<span class="tag">{tag}</span></h1>\n')


def param(n, title, define, a, b, c, d):
    cn = "一二三四五六七"[n - 1]
    return (
        '<section class="slide">\n'
        + crumb("文献综述", f"参数{cn}　{title}", f"参数 {n} / 7")
        + '  <div class="body">\n'
        f'    <div class="def">{define}</div>\n'
        '    <div class="p4">\n'
        f'      <div class="row"><div class="lb s1">已定</div><div class="tx">{a}</div></div>\n'
        f'      <div class="row"><div class="lb s2">未定</div><div class="tx">{b}</div></div>\n'
        f'      <div class="row"><div class="lb s3">本研究取值</div><div class="tx">{c}</div></div>\n'
        f'      <div class="row"><div class="lb s4">去处</div><div class="tx">{d}</div></div>\n'
        '    </div>\n'
        '  </div>\n  <div class="pg"></div>\n</section>'
    )


new = []

# ── p01 题目 + 核心问题 ────────────────────────────────────
new.append(f"""<section class="slide cover on">
  <h1>AR-HUD 行人碰撞预警的时空参数设计<br>及其对驾驶员情境意识与避险绩效的影响</h1>
  <div class="rule"></div>
  <div class="q">
    <b>核心问题：</b>探索 AR-HUD 行人碰撞预警的<b>时空参数取值</b>与驾驶员<b>情境意识、避险绩效</b>
    之间的关系，输出兼顾<b>安全阈限</b>与<b>用户心理需求</b>的时空参数设计标准与关系模型。
  </div>
  <div class="rq">
    <b>RQ1</b>　驾驶员在无辅助条件下的自发察觉时刻 {T0} 的分布特征为何，可否作为时间参数的零点？<br>
    <b>RQ2</b>　以 {T0} 为零点的相对提前量 {DT}、触发准则与分层时序，如何影响情境意识与避险绩效？<br>
    <b>RQ3</b>　空间参照系与风险动态映射，通过情境意识的哪一层级作用于避险绩效？
  </div>
  <div class="pg"></div>
</section>""")

# ── p02 研究背景与研究意义 ──────────────────────────────────
new.append("""<section class="slide">
"""
+ crumb("研究背景", "研究背景与研究意义", "背景")
+ f"""  <div class="body">
    <div class="def">
      全球每年约 <b>135 万人</b>死于道路交通事故，<b>行人约占 23%</b>（WHO, 2023）。传统低头显示要求视线移离前方道路，
      产生<b>视线离路时间</b>；AR-HUD 把图形与真实目标逐帧配准，理论上可同时消除视线离路时间与「信息位置—危险位置」的对应成本。
    </div>
    <div class="warn">
      <b>技术可行不等同于人因有效。</b>本文献库 102 篇中存在三项方向相反的实证结果：贴地共形箭头把图形注视时长推至
      <b>3.33 s</b>，越过分心上界（Gabbard 等, 2019）；TTC 5.0 s 的文本预警使峰值减速度<b>上升 34.46%</b>（Kim 等, 2018）；
      AR 系统随机故障时新手出现严重反应退化（Huo 与 Alla, 2025）。<b>→ 决定效果的并非是否采用 AR，而是时空参数的取值。</b>
    </div>
    <div class="cols2">
      <div class="box g">
        <h3>理论意义</h3>
        <ul class="small">
          <li>把预警时刻从<b>枚举秒数</b>改为<b>由约束导出</b>：建立运动学下界／可靠性上界／认知加工窗口的<b>三重约束模型</b>，
              并以自发察觉时刻 {T0} 为零点实测其交集</li>
          <li>以 {DT} 而非绝对 TTC 为自变量，为<b>跨车速、跨研究</b>的结论比较提供统一记法</li>
          <li>把「动态」拆为<b>风险量级映射 × 运动趋势映射</b>两个正交维度，检验其分别作用于情境意识的哪一层级</li>
        </ul>
      </div>
      <div class="box a">
        <h3>应用意义</h3>
        <ul class="small">
          <li>输出六项可落地的参数区间：<b>出现时机 · 触发准则 · 持续与撤销 · 级间间隔 · 锁定策略 · 动态编码</b></li>
          <li>参数以<b>运动学量</b>（制动威胁数 BTN）而非固定秒数表达，<b>可跨车速迁移</b>，并与量产 AEB 时序对齐</li>
          <li>面向<b>中国新手驾驶员</b>，为车载显示的人因评估条款提供实证依据</li>
        </ul>
      </div>
    </div>
  </div>
  <div class="pg"></div>
</section>""")

# ── p03–p09 七个参数 ──────────────────────────────────────
new.append(param(
    1, "预警提前量 Δt",
    f"<b>待定参数：</b>预警的触发时刻。既有研究一律以「距冲突的剩余时间」（绝对 TTC）表述。",
    "Zhang 等（2015）的<b>七档梯度对照</b>是本库唯一的梯度证据：TTC <b>2.5 s 与无预警条件无显著差异</b>"
    "（碰撞率 29.4% 对 44.1%），出现显著改善的下限为 <b>3.0 s</b>，推荐区间 3.0–4.0 s。",
    "同一取值 <b>5.0 s</b> 上存在三种相反结论——显著缩短反应时（Kang 等, 2016）、峰值减速度上升 34.46%"
    "（Kim 等, 2018）、无显著增益（Wang 等, 2025）；可识别的第三变量为<b>车速与呈现模态</b>。"
    f"更根本的是：{T0} <b>从未被作为基准量测量</b>，全部研究把预警设在绝对 TTC 上，隐含「驾驶员在预警前对行人一无所知」，"
    "而 Winkler 等（2018）报告 <b>50% 被试在预警呈现前已开始制动</b>。",
    f'自变量由绝对 TTC 改为<b>相对提前量</b> <span class="m">Δt<span class="up"> = </span>t<sub>0</sub>'
    f'<span class="up"> − </span>t<sub>warn</sub></span>，取 <b>0 ／ +1.0 ／ +2.5 s</b> 三水平，'
    f"使不同车速下的条件在<b>信息增益上等价</b>。",
    f"{T0} 由<b>研究一</b>实测（空白 G1）→ {DT} 作为<b>实验 2</b> 的自变量。",
))

new.append(param(
    2, "触发准则",
    "<b>待定参数：</b>触发条件所依据的物理量——固定时间阈值（TTC），或<b>制动威胁数 BTN</b>"
    "（＝避险所需减速度／最大可用减速度，无量纲）。",
    "算法侧四项研究一致主张以<b>运动学量</b>而非固定秒数触发：Takada 等（2014）的减速度触发准则"
    "（触发 4.0／解除 2.0 m/s²，2 : 1 滞环）、Chen 等（2013）的双条件、Coelingh 等（2010）的量产 AEB 时序"
    "（物理最早 1.6 s、制动建立 0.68 s）、Char（2020）基于 3 700 例事故重建的检出率。",
    "固定时间阈值<b>跨车速失效</b>：TTC 2 s 在 40 km/h 下对应 BTN 0.35，在 80 km/h 下对应 <b>0.69</b>，"
    "运动学难度相差一倍，故以固定秒数表述的参数在物理上不可跨车速迁移。"
    "但人因侧<b>从未做过准则类型的对照实验</b>（空白 G2）。",
    "<b>实验 2</b> 把准则类型设为自变量（固定时间阈值／减速度归一化）。BTN 分母统一取 "
    '<span class="m">a<sub>max</sub></span> = 8 m/s²，并<b>另以研究一实测的舒适减速度为分母并列报告</b>，不择一而用。',
    "<b>实验 2</b> 自变量；BTN 同时作为<b>实验 5</b> 风险量级映射的映射源。",
))

new.append(param(
    3, "分层结构与级间间隔",
    "<b>待定参数：</b>级数、各级触发点与<b>级间间隔</b>。分层的主张并非增加信息量，而是使预警强度与风险阶段相匹配。",
    "四条产业级级联时序共同界定区间 <b>0.5–2.0 s</b>，且越接近碰撞间隔越短（Lubbe, 2017：0.7 s；"
    "Daimler 转引：1.4／1.0／0.5 s；Suzuki 等, 2010：档距 1.0 s）；其中 <b>1.0 s 获双源支持</b>。"
    "Phan（2016）的覆盖人群百分位为第二级锚点提供依据：TTC 2.0 s 覆盖 90%。",
    "上述区间<b>全部来自产业实现的时序</b>，本库无一项以级间间隔为自变量的人因实验（空白 G4）；"
    "因此间隔过短是否导致理解不及、过长是否造成重复提醒、是否存在倒 U 型最优区间，均无从判断。"
    "常被引用的 0.7 s 实为<b>单一来源</b>，且可能使两级警告在知觉上融合为单一刺激。",
    "<b>实验 3</b> 以级间间隔 <b>0.7 ／ 1.0 ／ 1.5 s</b> 为自变量，另加无警告基线与实验 2 入选单层方案两个对照；"
    '并设<b>状态条件化升级仲裁</b>——第二级前若已检测到 <span class="m">a<sub>ego</sub></span> &lt; −0.075 g 则取消升级。',
    "<b>实验 3</b> 自变量；升级仲裁的取消率／错误率作为过程指标。",
))

new.append(param(
    4, "持续时长与撤销策略",
    "<b>待定参数：</b>在屏持续时长与退出方式（硬切／渐隐／滞环）。该参数在七项中证据最为薄弱。",
    "固定时长型研究多取 <b>3 s</b>（Ma 等, 2021；Ye 与 Yin, 2025）。撤销侧唯一可用规则为 Takada 等（2014）的 "
    "<b>2 : 1 滞环</b>。本研究综合的理论上下界：下界 <b>≥ 500 ms</b>（注意定向 150–300 ms ＋ 信息提取 300–500 ms）、"
    "上界 <b>≤ 3 s</b>（单通道视觉须留出视线回到道路的窗口）。",
    "持续时长的<b>报告率不足 15%</b>，而「1 s／2 s／3 s／至危险解除」这一最基本的对照<b>本库无一篇</b>（空白 G3）；"
    "渐隐时长<b>没有任何文献支撑</b>。Ma 等（2021）自陈其 3 s 为工程经验值而非实证最优值。",
    "<b>实验 2</b> 设区块 B，比较<b>固定 1.5 s ／ 状态维持 ／ 风险耦合衰减</b>三种策略，"
    "主要终点取<b>漏检率与视觉占用</b>而非仅反应时；渐隐参数按推导值执行，并在论文中显式标注为无文献支撑。",
    "<b>实验 2</b> 区块 B；所有条件间<b>固定闪烁状态</b>，以免反应时差异被归因于闪烁。",
))

new.append(param(
    5, "系统可靠性与虚警代价",
    "<b>待定参数：</b>可容许的虚警率与漏报率上限。该参数同时确定<b>提前量的上界</b>——预警不得早于算法可作可靠判断的时刻。",
    "Schall 等（2013）：15% 误报 ＋ 15% 漏报（可靠性 85%）<b>对所有因变量均无显著效应</b>，"
    "其关键条件为提示提前 11–13 s、语义为警示级、<b>不要求立即动作</b>；同一系统使老年驾驶员行人检出率由 66.10% 升至 91.13%。"
    "工程可达水平：骚扰报警占比 <b>13.74%</b>（Wang 等, 2026）。",
    "Abe 与 Richardson（2006）在<b>要求立即制动</b>的条件下得到强效应：信任由 <b>7.3 降至 4.3</b>，"
    "晚报警反使制动反应时由 0.95 <b>延长至 1.07 s</b>。两处结论的第三变量是<b>行动要求强度</b>，"
    "但可靠性与提前量的<b>交互从未被检验</b>（空白 G5）。",
    "<b>实验 3</b> 把系统可靠性设为自变量，并把虚警<b>只施加在第一级</b>（低行动要求级别），"
    "据此检验「虚警代价随行动要求强度递增」这一预测，同时分离可靠性与时机的交互。",
    f"<b>实验 3</b> 自变量；并作为 {DT} <b>上界</b>的约束来源（三重约束模型之一）。",
))

new.append(param(
    6, "空间参照系与锁定策略",
    "<b>待定参数：</b>图形锁定于何处——<b>BD</b> 屏幕／视线固定、<b>BR</b> 道路／冲突点锁定、"
    "<b>BW</b> 跟随危险行人的目标锁定（记法沿用 Wu 等, 2024）。",
    "Wu 等（2024，N = 36）三方对照的首次注视时间：<b>BW 617 ms</b>、BD 2 563 ms、BR 2 730 ms，差异接近 <b>4 倍</b>。"
    "Lind（2007）四方对照：碰撞预警平视显示的制动反应时快约 <b>200 ms</b>，漏报 <b>1 次</b>对高位下视显示 17 次。",
    "<b>BD／BR／BW／BW+BR 的正交对照至今无一实现</b>，亦无一项操纵背景视觉复杂度（空白 G6）。"
    "更需辨析的是：碰撞预警平视显示<b>本身即屏幕固定式</b>前视野显示，却已取得上述优势，"
    "故 AR 的收益必须拆为<b>位置增益</b>（把信息搬进前视野）与<b>共形增益</b>（图形贴合真实目标）两项，混计会系统性高估共形性。",
    "<b>实验 4</b> 采用五水平正交对照（Baseline／BD／BR／BW／BW+BR）× 背景视觉复杂度，时间参数全部固定为实验 2–3 入选组合；"
    "因 BD 已含位置增益，<b>样本量按更小的增量效应估计</b>。另设区块 F（BD／BW × 次任务负荷）检验共形增益是否依赖负荷。",
    "<b>实验 4</b> 自变量；主要指标含真实行人首次注视时间，并并列报告漏检率。",
))

new.append(param(
    7, "风险动态映射",
    "<b>待定参数：</b>图形随风险<b>连续变化</b>的映射方式。形态、颜色与不透明度已有较充分证据，映射方式为拟填补的主要空白。",
    "颜色：Zhong 等（2022）实车 42 组合显示<b>红与黄为跨照度鲁棒色对</b>（日间黄 4.12、夜间红 3.88），"
    "蓝与紫在两种照度下均最差。不透明度：四个来源收敛于 <b>0.6–0.75</b>。形态优劣依赖场景，行人场景下边界框反而更快。",
    "「动态」<b>从未被拆为风险量级映射与运动趋势映射的正交组合</b>（空白 G7），"
    "故既有「动态编码优于静态编码」的结论无法说明其<b>作用路径</b>——即究竟改善了对风险程度的理解，还是对未来位置的预测。",
    "<b>实验 5</b> 采用 <b>2（风险量级映射：有／无，以 BTN 为映射源）× 2（运动趋势映射：有／无）</b>设计，"
    "颜色与不透明度固定为上述鲁棒取值；预期两个维度<b>分别</b>作用于情境意识的理解层与预测层。",
    "<b>实验 5</b> 自变量；其交互项是「时间侧—空间侧整合模型」的关键系数。",
))

# ── p10 过渡页 ────────────────────────────────────────────
new.append("""<section class="slide">
"""
+ crumb("承接", "七项参数的共同前提：时间零点尚未被测量", "为何先做研究一")
+ f"""  <div class="body">
    <div class="def">
      七项参数中的前五项均以<b>时间</b>表述，而这些秒数共享同一个零点：<b>冲突时刻</b>。
      该记法隐含一个从未被检验的假设——<b>驾驶员在预警呈现前对行人一无所知</b>。
    </div>
    <div class="cols2">
      <div class="box r">
        <h3>隐含假设的三条否证</h3>
        <ul class="small">
          <li>Winkler 等（2018）：左转侵入场景中 <b>50% 被试在预警呈现前已开始制动</b></li>
          <li>Phan 等（2016）：无预警条件下行人觉察时刻已在 <b>TTC 约 3 s</b></li>
          <li>Abe 与 Richardson（2006）：无报警条件下<b>自主松油基线 0.72 s</b></li>
        </ul>
        <p class="small" style="margin-top:7px"><b>后果：</b>以绝对 TTC 为自变量时，同一取值在不同车速与遮挡条件下
        对应的<b>信息增益不同</b>，故条件间的比较不成立——这也正是同一个 5.0 s 出现三种相反结论的原因之一。</p>
      </div>
      <div class="box g">
        <h3>研究一的三项职能</h3>
        <ul class="small">
          <li><b>重设零点。</b>实测 {T0} 的分布，使时间参数由绝对 TTC 改写为
              <span class="m">Δt<span class="up"> = </span>t<sub>0</sub><span class="up"> − </span>t<sub>warn</sub></span></li>
          <li><b>提供基线参数。</b>感知反应时分位数、BTN 校准值、实测舒适减速度、无预警条件下的碰撞率</li>
          <li><b>决定后续设计的可行性。</b>{T0} 的<b>被试内标准差</b>决定 {DT} 能否作被试内因子；
              若三重约束的交集为空，则否证本研究的参数化路径</li>
        </ul>
      </div>
    </div>
    <div class="ok">
      <b>因此研究一在前。</b>它不检验任何设计方案的优劣，其唯一职能是<b>为后续四个实验标定基线参数</b>；
      同时它是本研究「参数由约束导出而非由文献枚举」这一主张的<b>前置可否证环节</b>。
    </div>
  </div>
  <div class="pg"></div>
</section>""")

# ── p11 研究一：变量 ──────────────────────────────────────
new.append("""<section class="slide">
"""
+ crumb("研究一", "研究一的变量结构：2 × 2 设计与四类因变量构念", "研究一 1 / 3")
+ f"""  <div class="body">
    <div class="def">
      研究一为<b>测量性研究，不含 AR 操纵</b>，全部条件均为无预警条件；不设实验组—对照组，故其自变量为
      <b>影响自发察觉时刻的两个情境因素</b>，而非任何显示设计参数。
    </div>
    <div class="cols2 w37">
      <div class="box">
        <h3>自变量：2 × 2 被试内</h3>
        <ul class="small">
          <li><b>行车速度</b>　40 ／ 60 km/h<br>
              <span class="cite">覆盖国内城市主要限速档，并与 Large 等（2019）的 40、Wu 等（2024）的 60 可对照</span></li>
          <li><b>视线遮挡</b>　无 ／ 停放车辆部分遮挡<br>
              <span class="cite">遮挡直接改变光学膨胀率越过知觉阈值的时刻，即直接改变 {T0}</span></li>
        </ul>
        <p class="small" style="margin-top:6px">→ 四个标定单元，顺序按拉丁方平衡。</p>
      </div>
      <div class="box">
        <h3>因变量：四类构念及其操作化指标</h3>
        <ul class="small">
          <li><b>情境意识</b>　{T0}（首次注视行人时刻，注视识别阈 80 ms／100 px）；SA 三级得分（感知／理解／预测）</li>
          <li><b>安全绩效</b>　首个避险动作时刻（松油阈值 −0.075 g）、峰值减速度、碰撞率；
              过程量为感知反应时及其三段分解与所需减速度轨迹</li>
          <li><b>认知负荷</b>　NASA-TLX 与瞳孔直径基线，用作后续四个实验的<b>负荷参照基线</b></li>
          <li><b>用户体验</b>　无预警条件下的主观风险感与紧迫度评定，用作后续实验的<b>体验参照基线</b></li>
        </ul>
      </div>
    </div>
    <div class="note">
      <b>指标归属的理论依据：</b>{T0} 是<b>时刻量</b>，SA 是<b>潜在构念</b>，二者为「操作化指标—构念」关系而非同一事物的两个名称。
      本研究把 {T0} 明确归属为<b>情境意识感知层在无辅助条件下的达成时刻</b>，并另设 SA 三级得分与之并存。
    </div>
  </div>
  <div class="pg"></div>
</section>""")

# ── p12 研究一：实施方案 ──────────────────────────────────
new.append("""<section class="slide">
"""
+ crumb("研究一", "研究一的实施方案：被试、任务、流程与清洗规则", "研究一 2 / 3")
+ """  <div class="body">
    <table>
      <tr><th style="width:88px">要素</th><th>设定与依据</th></tr>
      <tr><td><b>被试</b></td><td>N ≈ 24。标定实验以<b>估计精度</b>而非效应检出为目标，正式值由预实验方差成分重算并写入预注册。
        持照驾驶员，含新手（驾龄 &lt; 1 年）与熟手两层。<b class="k">须与实验 2 复用同一批被试</b>——因 <span class="m">Δt</span>
        需要被试自身的 <span class="m">t<sub>0</sub></span>。</td></tr>
      <tr><td><b>任务</b></td><td>模拟器城市道路定速跟驰，遇危险自行避险，<b>未告知危险类型与出现时点</b>。
        <b class="k">不设次任务</b>——本实验测的是无附加负荷下的自发察觉基线，加入次任务将污染零点。</td></tr>
      <tr><td><b>流程</b></td><td>知情同意 → 视力与晕动筛查 → 适应驾驶 8 min → 正式四个标定单元 → 单元间休息 3 min →
        眼动标定复核 → 事后访谈与量表。单次 session ≤ 25–30 min（晕动控制）。</td></tr>
      <tr><td><b>试次</b></td><td>危险事件 24 次、填充 ≥ 36 次、捕获 8 次，<b>危险占比 &lt; 40%</b>（以免形成预期）；
        事件间隔 <b>≥ 60 s</b>（依据：次任务后的分心残留可持续 30 s 以上，留一倍冗余）。</td></tr>
      <tr><td><b>清洗</b></td><td>反应时纳入界 0.2–2.9 s；眼动有效率 ≥ 80%；学习效应以试次序号作协变量<b>显式检验</b>
        （参考量级 0.16 s）。</td></tr>
    </table>
    <div class="note">
      <b>预先声明的研究者设定值（无文献支撑，列入局限并写入预注册）：</b>事件间路程 300–600 m、session 时长上限、
      行人肩宽 0.5 m（膨胀率计算用）、最小侵入余量非劣界 −0.2 s、样本量。其中<b>非劣界与样本量须由预实验的最小实际意义差重算</b>。
    </div>
  </div>
  <div class="pg"></div>
</section>""")

# ── p13 研究一：预期结果与产出 ────────────────────────────
new.append("""<section class="slide">
"""
+ crumb("研究一", "研究一的预期结果与五项产出的去处", "研究一 3 / 3")
+ f"""  <div class="body">
    <div class="cols2">
      <div class="box g">
        <h3>预期结果（含理论校验值）</h3>
        <ul class="small">
          <li>{T0} <b>中位数</b>：60 km/h 无遮挡条件下预期 <b>3.0–3.5 s</b>（光学膨胀率推算 3.2 s，Phan 等实测约 3 s）。
              <b>若大幅偏离，先检验模拟器视觉保真度而非直接采信。</b></li>
          <li><b>主效应方向</b>：{T0} 随车速升高而<b>缩短</b>（膨胀率越阈发生于更近距离）；遮挡条件下<b>显著晚于</b>无遮挡。</li>
          <li><b>首个避险动作时刻</b>：无预警条件下预期在距冲突点约 1.5 s，碰撞率约 44%（Zhang 等, 2015 同源）。</li>
          <li><b>效度证据</b>：预期 SA 感知层得分与 {T0} <b>显著负相关</b>；若不相关，须在讨论中重新审视该指标归属。</li>
        </ul>
      </div>
      <div class="box">
        <h3>五项产出与下游去处</h3>
        <table class="mini">
          <tr><th>产出</th><th>去处</th></tr>
          <tr><td>{T0} 分布</td><td class="n">实验 2 的 {DT} 零点</td></tr>
          <tr><td>感知反应时 p85</td><td class="n">提前量下界</td></tr>
          <tr><td>BTN 校准值</td><td class="n">实验 2 触发准则<br>实验 5 映射源</td></tr>
          <tr><td>实测舒适减速度</td><td class="n">BTN 第二分母<br>代价终点判据</td></tr>
          <tr><td>方差成分</td><td class="n">全部实验的样本量</td></tr>
        </table>
        <p class="small" style="margin-top:7px"><b>可否证点：</b>若 {T0} 的<b>被试内标准差过大</b>，则 {DT}
        不可作被试内因子，实验 2 须改为组间设计；若三重约束的交集为空，则否证参数化路径本身。</p>
      </div>
    </div>
  </div>
  <div class="pg"></div>
</section>""")

# ── p14 后续路线 ──────────────────────────────────────────
new.append("""<section class="slide">
"""
+ crumb("研究规划", "研究二与研究三：四个主实验的分工", "路线图")
+ """  <div class="body">
    <table>
      <tr><th style="width:74px">实验</th><th style="width:200px">自变量</th><th>主要终点与所答问题</th></tr>
      <tr><td class="n"><b>实验 2</b><br><span class="cite">研究二</span></td>
          <td>相对提前量 <span class="m">Δt</span> × 触发准则<br><span class="cite">区块 B：持续与撤销策略</span></td>
          <td>单层预警的<b>时间参数可行区间</b>：最小有效提前量、准则类型的主效应，以及漏检率与视觉占用的权衡</td></tr>
      <tr><td class="n"><b>实验 3</b><br><span class="cite">研究二</span></td>
          <td>级间间隔 × 系统可靠性<br><span class="cite">状态条件化升级仲裁</span></td>
          <td>分层预警的<b>升级时序规范</b>：级间间隔是否存在倒 U 型最优区间，虚警代价是否随行动要求强度递增</td></tr>
      <tr><td class="n"><b>实验 4</b><br><span class="cite">研究三</span></td>
          <td>锁定策略五水平 × 背景视觉复杂度<br><span class="cite">区块 F：次任务负荷</span></td>
          <td><b>位置增益与共形增益的分离</b>：共形性的增量效应有多大，以及该增量是否依赖背景复杂度与负荷</td></tr>
      <tr><td class="n"><b>实验 5</b><br><span class="cite">研究三</span></td>
          <td>风险量级映射 × 运动趋势映射</td>
          <td>动态编码的<b>作用路径</b>：两个维度是否分别作用于情境意识的理解层与预测层</td></tr>
    </table>
    <div class="ok">
      <b>递进而非并列。</b>上游实验的入选参数在下游实验中<b>固定</b>：实验 1 的五项产出定义实验 2 的自变量刻度，
      实验 2–3 的入选时间参数在实验 4–5 中固定，从而使空间参数的效应不与时间参数混淆。
      全局硬约束：<b>实验 1／2／3 必须共用同一场景族与同一套标定单元</b>，否则 <span class="m">t<sub>0</sub></span> 不可迁移。
    </div>
  </div>
  <div class="pg"></div>
</section>""")

assert len(new) == 14, len(new)

# ── 备查页：自旧 deck 搬运（0-based 索引）──────────────────
BACKUP = [1, 2, 3, 4, 6, 15, 16, 17, 19, 20]
RETITLE = {19: "研究二与研究三：实验 2–5 的设计详表"}
for k in BACKUP:
    sec = old[k]
    sec = re.sub(r'<span class="tag">[^<]*</span>', '<span class="tag">备查</span>', sec)
    if k in RETITLE:
        sec = re.sub(r"<em>.*?</em>", f"<em>{RETITLE[k]}</em>", sec, count=1, flags=re.S)
    new.append(sec)

out = head + "\n\n" + "\n\n".join(new) + "\n\n" + tail.lstrip("\n")
P.write_text(out, encoding="utf-8")
print(f"✓ 重建完成：{len(new)} 页（讲述 14 + 备查 {len(BACKUP)}）")
