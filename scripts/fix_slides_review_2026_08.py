#!/usr/bin/env python3
"""按评阅意见修订《文献综述_幻灯片.html》九处内容（2026-08）。

对应的九条意见
  1. p02「本章的问题结构」不够清晰      → 由「目录式三栏」改为「三个前置问题 + 本章回答」的链条
  2. p05 SPIDER 与框架数值的对应不清楚   → 按 #58 全文改写：SPIDER 给结构不给数值，另列其三项量化贡献
  3. p06 表格与新术语（上界/下界/窗口）对齐，并补「各约束由谁测定」
  4. p07「危险场景生态硬约束」出处不明   → 逐端点标注一手出处，并声明「硬约束」是本研究的判读
  5. p09 Zhang（2015）的预警计时基线是什么 → 新增「该研究的计时基线」四行说明
  6. p10 图下灰字与黄框重叠             → 图注压缩为一行
  7. p15 图从何而来                     → 图注逐面板给出数据出处与本研究归纳的部分
  8. p16 反应时的上界/下界怎么定         → 明确区分三种不同的「上下界」，禁止混用
  9. p31 实验 0/1/2 是否统一场景条件      → 增加场景一致性约束说明

幂等：每处先查新文本特征串，已改则跳过。
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "文献综述_幻灯片.html"

# ══════════════════════════════════════════════════════════════════════════
# 1) p02　本章的问题结构
# ══════════════════════════════════════════════════════════════════════════
P02_OLD = """    <div class="def">
      AR-HUD 行人预警的效果<b>不由「有没有 AR」决定，而由时空参数取什么值决定</b>。本章按「自下而上／自上而下」两条注意路径把设计空间分为时间与空间两侧：<b>时间参数决定驾驶员是否拥有足够的加工窗口，空间参数决定该窗口内的定位与预测效率</b>。
    </div>
    <div class="cols3">
      <div class="box"><h3>2.1　概念与理论</h3>
        <ul class="small" style="margin-left:16px">
          <li>HUD／AR-HUD、PCW</li>
          <li>六项时间指标（TTC／TTMD／BTN／τ／<span class="m">t<sub>0</sub></span>／<span class="m">Δt</span>）</li>
          <li>六项空间要素</li>
          <li>SPIDER · τ 理论 · 多资源 · EID · SRK</li>
          <li><b>三重约束模型</b></li>
          <li>行人侧行为参数</li>
        </ul>
      </div>
      <div class="box"><h3>2.2–2.3　证据综述</h3>
        <ul class="small" style="margin-left:16px">
          <li>出现时机：横向比较 → <b>梯度对照</b></li>
          <li>触发准则：固定秒数 → <b>减速度归一化</b></li>
          <li>持续时长 · 闪烁占空比</li>
          <li>分层与级间间隔</li>
          <li>可靠性上界 · 反应时下界</li>
          <li>位置增益 · 锁定策略 · 颜色 · FOV</li>
          <li>无意视盲与注意隧道</li>
        </ul>
      </div>
      <div class="box"><h3>2.4–2.6　辨析与提问</h3>
        <ul class="small" style="margin-left:16px">
          <li><b>七组主要冲突 + 四组次级冲突</b></li>
          <li>三类冲突来源：条件差异／记法口径／推论过度</li>
          <li>方法学评述</li>
          <li>九项研究空白</li>
          <li>三个核心研究问题</li>
          <li>H1–H4（理论导出）· H5–H14（文献归纳）</li>
        </ul>
      </div>
    </div>
    <div class="ok"><b>本章的方法论主张：</b>冲突不应被「取平均」或回避，而应作为<b>调节变量存在的实证信号</b>——识别那个未被控制的第三变量，就等于识别了一个应当纳入设计的维度。</div>"""

P02_NEW = """    <div class="def">
      AR-HUD 行人预警的效果<b>不由「有没有 AR」决定，而由时空参数取什么值决定</b>。所以本章不问「哪个值最好」，而先回答<b>三个前置问题</b>——它们决定了后面所有数值能不能用。
    </div>
    <div class="cols3">
      <div class="box"><h3>问题一　参数值从哪里来？</h3>
        <p class="small"><span class="k">难处：</span>文献里出现过 1.8／2.0／2.5／3.0／4.0／5.0／6.0 s，<b>没有任何一篇说明自己为什么取这个值</b>。逐个试是无穷的。</p>
        <p class="small" style="margin-top:7px"><span class="k3">本章的回答：</span>都不取。改为<b>先确定参数被什么约束住</b>——建立<b>三重约束模型</b>（上界、下界、认知窗口 + 零点 <span class="m">t<sub>0</sub></span>），把「最优 TTC 是多少」换成<b>「可行区间在哪里」</b>。</p>
        <p class="cite" style="margin-top:6px">→ §2.1　概念 · 六项时间指标 · 六项空间要素 · 五项理论 · <b>三重约束模型</b> · 行人侧参数</p>
      </div>
      <div class="box"><h3>问题二　为什么文献结论互相矛盾？</h3>
        <p class="small"><span class="k">难处：</span>同一个 <b>5.0 s</b>，Kang 等（2016）报告有效、Kim 等（2018）报告过度反应、Wang 等（2025）报告无增益。<b>取平均或各引一句都是错的。</b></p>
        <p class="small" style="margin-top:7px"><span class="k3">本章的回答：</span>把每一组矛盾拆到<b>条件差异／记法口径／推论过度</b>三类来源上，逐组找出那个<b>未被控制的第三变量</b>——共<b>七组主要 + 四组次级冲突</b>。</p>
        <p class="cite" style="margin-top:6px">→ §2.2 时间侧证据｜§2.3 空间侧证据｜§2.4 冲突辨析与方法学评述</p>
      </div>
      <div class="box"><h3>问题三　哪些还没有人回答？</h3>
        <p class="small"><span class="k">难处：</span>综述若只汇总已有结论，就无法说明「为什么还要做实验」。必须指出<b>零对照的参数</b>。</p>
        <p class="small" style="margin-top:7px"><span class="k3">本章的回答：</span><b>九项研究空白</b>（其中 4 项为「零人因对照」）→ 收敛为<b>三个层层递进的核心问题</b> → <b>H1–H4</b>（由理论导出、可否证）+ <b>H5–H14</b>（由文献归纳）。</p>
        <p class="cite" style="margin-top:6px">→ §2.5 空白与问题提出｜§2.6 本章小结（七处对既有共识的修正）</p>
      </div>
    </div>
    <div class="ok"><b>贯穿三个问题的一条方法论主张：</b>结论冲突不该被「取平均」或回避，而应当作<b>调节变量存在的实证信号</b>——<b>找出那个未被控制的第三变量，就等于找到了一个应当纳入设计的维度</b>。本研究的五个实验，每一个都对应一个这样被找出来的维度。</div>"""

# ══════════════════════════════════════════════════════════════════════════
# 2) p05　SPIDER：改为「结构 vs 数值」的分工表述
# ══════════════════════════════════════════════════════════════════════════
P05_OLD = """    <div class="def">
      <b>SPIDER</b> = Scanning · Predicting · Identifying · Deciding · Executing Responses。由 Strayer 与 Fisher（2016）提出，Strayer 与 McDonnell（2025）更新为 SPIDER 2.0 <span class="cite">（*Human Factors*，JCR Q1，IF 3.6；*Annual Review of Vision Science*）</span>。<b>选它而非 PIEV 的两个理由：</b>PIEV 的 Emotion 阶段无法操作化；SPIDER 本身围绕<b>分心</b>构建，能同时容纳「AR 帮助注意」与「AR 造成注意隧道」两种效应。
    </div>
    <table class="mini">
      <tr><th style="width:12%">成分</th><th style="width:24%">代理指标</th><th>本库可参照的经验值</th></tr>
      <tr><td><b>S</b>canning</td><td>TTFF（警告／行人）、道路注视比例</td><td><span class="k3">617 ms</span>（动态跟随 BW；Wu 等, 2024 <b>实测</b>）；1 051 ms（分级警告；Chen 等, 2024b）</td></tr>
      <tr><td><b>P</b>redicting</td><td>路径侵入预测正确率、冲突点空间误差</td><td>本库未见直接报告</td></tr>
      <tr><td><b>I</b>dentifying</td><td>目标验证时间 = TTFF(行人) − TTFF(警告)</td><td><span class="k4">300–600 ms</span>（<b>本研究由 TTFF 差值推导，原文未报告</b>）</td></tr>
      <tr><td><b>D</b>eciding</td><td>首次注视行人 → 松油时间</td><td>本库未见直接报告</td></tr>
      <tr><td><b>E</b>xecuting</td><td>制动启动时间、峰值减速度、jerk</td><td>800 ms（SD 290 ms；分心 + 多模态；Lubbe, 2017）</td></tr>
    </table>
    <div class="warn"><b>⚠ 可信度限定（本研究的诚实声明）：</b>经核查两篇原文，SPIDER <b>均未报告任何阶段耗时，也未声明五阶段严格串行</b>——它是<b>助记性框架（mnemonic），不是可计算的过程模型</b>。因此「<span class="m">S<span class="up">+</span>I<span class="up"> ≈ 0.9</span></span>–1.2 s」一律表述为<b>本研究基于 SPIDER 阶段划分建立的工作假设</b>；1.0 s 的<b>主要依据是工程证据</b>（Daimler 级联 1.0 s 级间、Suzuki 等 1.0 s 档距），理论推导只作事后解释。</div>"""

P05_NEW = """    <div class="def">
      <b>SPIDER</b> = <b>S</b>canning · <b>P</b>redicting · <b>I</b>dentification · <b>D</b>ecision-making · <b>E</b>xecuting a <b>R</b>esponse。Strayer 与 Fisher（2016，*Human Factors*，Q1，IF 3.6）提出，Strayer 与 McDonnell（2025，*Annu. Rev. Vis. Sci.*，CC BY，<b>已取得全文</b>）更新为 2.0。<b>它与本研究框架的分工是：SPIDER 定「结构」，实证文献定「数值」。</b>
    </div>
    <div class="cols2 w73">
      <div class="box"><h3>结构：阶段 → 代理指标 → Endsley 层级</h3>
        <table class="mini">
          <tr><th style="width:15%">阶段</th><th>本研究的代理指标</th><th class="n" style="width:19%">SA 层级<br>（原文明确）</th></tr>
          <tr><td><b>S</b>canning</td><td>TTFF（警告／行人）、道路注视比例、注视分散度</td><td class="n">层级 1<br>感知</td></tr>
          <tr><td><b>P</b>redicting</td><td><span class="k3">预期性注视比例</span>、风险区首次注视时刻<br><span class="cite">（原文确认代理量即 anticipatory glances）</span></td><td class="n">层级 3<br>预测</td></tr>
          <tr><td><b>I</b>dentification</td><td>目标验证时间 = TTFF(行人) − TTFF(警告)、<b>漏检率／无意视盲率</b></td><td class="n">层级 2<br>理解</td></tr>
          <tr><td><b>D</b>ecision</td><td>首次注视行人 → 松油时间、间隙判断、安全边际</td><td class="n">SA 的<br><b>下游</b></td></tr>
          <tr><td><b>E</b>xec. Resp.</td><td>制动启动时间、峰值减速度、jerk、<b>反应时分布尾部</b></td><td class="n">SA 的<br><b>下游</b></td></tr>
        </table>
        <div class="note" style="margin-top:8px"><b>原文 Figure 1 的一处结构事实：</b>只有 <b>S、P、I 与情境意识之间是双向箭头</b>，D 与 ER 是 SA 的下游。<b>把五阶段画成一条单向串行链是对原图的误读</b>——这也解释了为什么阶段耗时不可简单相加。</div>
      </div>
      <div class="box a"><h3>数值：SPIDER 给出的与不给出的</h3>
        <div class="warn"><b>不给出：任何阶段耗时。</b>两篇原文<b>均未报告一个毫秒值</b>，也未声明五阶段严格串行。故「<span class="m">S<span class="up">+</span>I<span class="up"> ≈ 0.9</span></span>–1.2 s」只能表述为<b>本研究基于其阶段划分建立的工作假设</b>：S 的 617 ms 取自 Wu 等（2024）实测，I 的 300–600 ms 是<b>本研究由 TTFF 差值自行估计</b>。1.0 s 的<b>主要依据是工程证据</b>（Daimler 级联 1.0 s 级间、Suzuki 等 1.0 s 档距）。</div>
        <div class="ok" style="margin-top:9px"><b>给出：三个可直接约束本研究的数值。</b>
          <ul style="margin:5px 0 0 17px">
            <li class="tight"><b>任一阶段成功率 −5% → 相对碰撞风险 ×2</b><br><span class="cite">（转述 Fisher 与 Strayer, 2014）→ SPIDER 是<b>成功概率模型</b>，故漏检率必须与反应时并列为主要因变量</span></li>
            <li class="tight"><b>次任务结束后分心仍持续 &gt; 30 s</b><br><span class="cite">（转述 Strayer 等, 2022b）→ 本研究试次间隔取 <b>≥ 60 s</b></span></li>
            <li class="tight"><b>识别类差错 41% ≫ 决策 33% ≫ 操作 11%</b><br><span class="cite">（NMVCCS，Singh, 2015）→ 干预点应放在 S/I 而非 ER</span></li>
          </ul>
        </div>
      </div>
    </div>"""

# ══════════════════════════════════════════════════════════════════════════
# 3) p06　表格与新术语对齐 + 补「谁来测定」
# ══════════════════════════════════════════════════════════════════════════
P06_OLD = """    <div class="def">预警呈现时刻 <span class="m">t<sub>warn</sub></span> <b>不是待搜索的自由参数</b>，而是由三条约束共同界定、并以自发察觉时刻 <span class="m">t<sub>0</sub></span> 为零点的量。三条约束的交集即<b>可行设计区间</b>。</div>
    <figure><img src="figures/ch2_fig_three_bounds.png" alt="三重约束模型"></figure>
    <table class="mini">
      <tr><th style="width:20%">约束线</th><th style="width:34%">数学表述</th><th>本研究如何确定</th></tr>
      <tr><td class="k3">下界：运动学必要性</td><td><span class="m">t<sub>warn</sub><span class="up">≥ </span><span class="up">PRT</span><sub>p95</sub><span class="up">+</span>v<sub>ego</sub><span class="up">/</span>a<sub>comf</sub><span class="up">+</span>δ<sub>brake</sub></span></td><td>实验 0 测 PRT 分布；由车速与 <span class="m">a<sub>comf</sub></span> 算出</td></tr>
      <tr><td class="k">上界：可靠性—信任</td><td><span class="m">t<sub>warn</sub><span class="up">≤ </span>t<sub>pred</sub><span class="up">(</span><span class="up">PPV</span><span class="up">≥</span>π<sup>*</sup><span class="up">)</span></span></td><td>实验 2 操纵系统可靠性直接检验</td></tr>
      <tr><td class="k4">窗口：认知加工</td><td><span class="m">Δt<span class="up">≥Σ</span></span> SPIDER（<b>本研究估计</b> 0.9–1.2 s）</td><td>实验 1 以 <span class="m">Δt</span> 为自变量直接检验</td></tr>
      <tr><td class="k2">零点：自发察觉基线</td><td><span class="m">t<sub>0</sub></span></td><td>实验 0 实测；τ 理论给出下限校验 TTC ≈ 3.2 s</td></tr>
    </table>"""

P06_NEW = """    <div class="def">预警呈现时刻 <span class="m">t<sub>warn</sub></span> <b>不是待搜索的自由参数</b>。它同时受<b>三个约束</b>，并以自发察觉时刻 <span class="m">t<sub>0</sub></span> 为零点；三者的交集即<b>可行设计区间</b>。<b>本研究的贡献不是「猜一个更好的秒数」，而是把这个区间实测出来。</b></div>
    <figure><img src="figures/ch2_fig_three_bounds.png" alt="预警时刻的三重约束模型"></figure>
    <table class="mini">
      <tr><th style="width:17%">约束</th><th style="width:15%">一句话含义</th><th style="width:30%">数学表述</th><th>由谁测定</th></tr>
      <tr><td class="k3">① 运动学下界</td><td>预警<b>必须足够早</b>：来不及刹住就没有意义</td><td><span class="m">t<sub>warn</sub><span class="up">≥ </span><span class="up">PRT</span><sub>p95</sub><span class="up">+</span>v<sub>ego</sub><span class="up">/</span>a<sub>comf</sub><span class="up">+</span>δ<sub>brake</sub></span></td><td><b>实验 0</b> 测 PRT 分布与 <span class="m">a<sub>comf</sub></span>，由车速算出</td></tr>
      <tr><td class="k">② 可靠性上界</td><td>预警<b>不能太早</b>：算法判不准，虚警毁掉信任</td><td><span class="m">t<sub>warn</sub><span class="up">≤ </span>t<sub>pred</sub><span class="up">(</span><span class="up">PPV</span><span class="up">≥</span>π<sup>*</sup><span class="up">)</span></span></td><td><b>实验 2</b> 操纵系统可靠性直接检验</td></tr>
      <tr><td class="k4">③ 认知窗口</td><td>窗口宽度<b>必须容得下注意加工</b></td><td><span class="m">Δt<span class="up"> = </span>t<sub>0</sub><span class="up"> − </span>t<sub>warn</sub><span class="up"> ≥ </span></span>加工所需（<b>本研究估计</b> 0.9–1.2 s）</td><td><b>实验 1</b> 以 <span class="m">Δt</span> 为自变量直接检验</td></tr>
      <tr><td class="k2">零点 <span class="m">t<sub>0</sub></span></td><td>没有零点，<b>「提前多少」无从定义</b></td><td>驾驶员在无辅助条件下的自发察觉时刻</td><td><b>实验 0</b> 实测；τ 理论给出校验值 TTC ≈ 3.2 s</td></tr>
    </table>"""

# ══════════════════════════════════════════════════════════════════════════
# 4) p07　生态约束的出处
# ══════════════════════════════════════════════════════════════════════════
P07_OLD = """      <div class="box"><h3>间隙接受：危险场景的生态硬约束</h3>
        <table class="mini">
          <tr><th>判据</th><th class="n">数值</th></tr>
          <tr><td><b>无人接受的间隙下界</b></td><td class="n"><b>&lt; 1.5 s</b></td></tr>
          <tr><td>行人通常不过街的 TTC</td><td class="n">&lt; 3 s</td></tr>
          <tr><td>行人非常可能过街的 TTC</td><td class="n">&gt; 7 s</td></tr>
          <tr><td>平均间隙接受区间</td><td class="n"><b>3–7 s</b></td></tr>
          <tr><td>起步损失时间（路段中部）</td><td class="n">1.3 s</td></tr>
        </table>
        <div class="ok" style="margin-top:9px"><b>硬约束：</b>危险场景的车—人间隙必须落在 <b>1.5–7 s</b> 区间内——低于 1.5 s 则行人横穿在生态上不合理，高于 7 s 则冲突不成立。<b>本库既有实验很少显式论证这一点</b>。</div>
        <div class="note" style="margin-top:8px"><b>行人的判断能力上限：</b>车速 &lt; 45 km/h 能正确估计车速，&lt; 65 km/h 能正确估计车距。反直觉推论：<b>同一 TTC 下来车越快，行人反而更常过街</b>（更依赖距离线索）。</div>
      </div>"""

P07_NEW = """      <div class="box"><h3>间隙接受：危险场景在生态上是否成立</h3>
        <table class="mini">
          <tr><th>判据</th><th class="n" style="width:15%">数值</th><th style="width:47%">一手出处（两篇综述均为转引）</th></tr>
          <tr><td><b>无人接受的间隙</b></td><td class="n"><b>&lt; 1.5 s</b></td><td>英国实测「所有行人接受 10.5 s、<b>无人接受 &lt; 1.5 s</b>」——Ezzati Amini 等（2019）转引，原文献编号 [116]</td></tr>
          <tr><td>通常不过街的 TTC</td><td class="n">&lt; 3 s</td><td><b>DiPietro 与 King（1970）</b>——Rasouli 与 Tsotsos（2020）转引</td></tr>
          <tr><td>非常可能过街的 TTC</td><td class="n">&gt; 7 s</td><td><b>Schmidt 与 Färber（2009）</b>——同上转引；Ezzati Amini 等经 Schroeder <b>独立得到同一区间</b></td></tr>
          <tr><td>起步损失时间</td><td class="n">1.3 s</td><td>路段中部受控过街，Bennett 等——Ezzati Amini 等（2019）转引</td></tr>
        </table>
        <div class="ok" style="margin-top:8px"><b>本研究由此得出的场景约束（判读，非原文表述）：</b>危险场景的车—人间隙应落在 <b>1.5–7 s</b>——低于 1.5 s 则行人横穿在生态上不合理，高于 7 s 则冲突不成立；<b>3–7 s 是行人自身决策最不确定的模糊带，也是 AR 介入价值最高的窗口</b>。</div>
        <div class="warn" style="margin-top:7px"><b>两点必须声明：</b>① 两篇原文只报告分布，<b>「硬约束」一词是本研究的判读</b>；② 全部端点均为<b>综述转引</b>（1970／2009 年的一手文献本课题未取得），故只用于<b>场景合理性辩护</b>，不作为效应量依据。两篇独立综述给出同一区间，是本判读的主要支撑。</div>
      </div>"""

# ══════════════════════════════════════════════════════════════════════════
# 5) p09　Zhang（2015）的计时基线
# ══════════════════════════════════════════════════════════════════════════
P09_OLD = """    <div class="ok"><b>两项梯度研究的汇合结论：</b>单层预警有效区间下界在 <b>3.0 s</b>，上界在 <b>4.0–5.0 s</b> 出现收益递减。<b>梯度证据把下界从既有共识的 2.5 s 上修到 3.0 s</b>——这是本课题对原有结论的一处实质性修正。</div>"""

P09_NEW = """    <div class="note"><b>Zhang 等（2015）的秒数是以什么为基线算出来的？——四点必须交代，否则不能迁移：</b>
      ① <b>零点＝冲突点</b>（交叉口内两车轨迹的交点），<b>不是</b>碰撞时刻、也不是行人所在位置；
      ② <b>时间量＝本车按当前车速到冲突点的接近时间</b>，由模拟器的「TTC 传感器」实时外推（<b>恒速假设</b>），预警由接近传感器在预设接近时间处触发；场景由闯红灯车在本车距冲突点 <b>7 s</b> 时以 <b>20 m/s</b> 驶出而生成，限速 <b>80 km/h</b> 城市双车道；
      ③ <b>「有效」的判定基线＝无预警组 NA</b>，做逐 0.5 s 切片的配对 <span class="m">t</span> 检验（NA 组直到 1.5 s 才猛制动、碰撞率 44.1%）——所谓「2.5 s 无效」即<b>全部切片上与 NA 无显著差异</b>；
      ④ 因此它给的是<b>距冲突点的剩余时间</b>，<b>不是</b>相对驾驶员察觉时刻的提前量。<b>迁移到本课题必须换算：</b><span class="m">Δt<span class="up"> = </span>t<sub>0</sub><span class="up"> − </span>t<sub>warn</sub></span>，而 <span class="m">t<sub>0</sub></span> 在该研究中未被测量。</div>
    <div class="ok"><b>两项梯度研究的汇合结论：</b>单层预警有效区间下界在 <b>3.0 s</b>，上界在 <b>4.0–5.0 s</b> 出现收益递减。<b>梯度证据把下界从既有共识的 2.5 s 上修到 3.0 s</b>——这是本课题对原有结论的一处实质性修正。</div>"""

# ══════════════════════════════════════════════════════════════════════════
# 6) p10　图注压缩为一行
# ══════════════════════════════════════════════════════════════════════════
P10_OLD = """      <figcaption>图 2-2　预警出现时机的证据谱。绿色圆点＝报告有效；红叉＝与无预警无显著差异；橙三角＝过度反应或无增益；蓝方块＝采用但未与其他阈值对照。背景三色带为由梯度证据界定的无效区（&lt; 3.0 s）／推荐区（3.0–4.0 s）／收益递减区（&gt; 4.0 s）。</figcaption>"""
P10_NEW = """      <figcaption>图 2-2　预警出现时机的证据谱：本库 14 项取值 × 4 类判定结果；三色带由梯度证据界定（图例见图内）。</figcaption>"""

# ══════════════════════════════════════════════════════════════════════════
# 7) p15　图的数据出处
# ══════════════════════════════════════════════════════════════════════════
P15_OLD = """      <figcaption>图 2-3　左：驾驶员对行人过街意图的判别绩效（Chen 等, 2019）。右：人因需求、人类判别能力与算法预测能力三个时间窗的量级对比。</figcaption>"""
P15_NEW = """      <figcaption>图 2-3　本研究自绘，无本研究数据。<b>左</b>：直接取自 Chen 等（2019）Table 1 原值——熟练组命中率 0.86／0.92／0.90、虚警率 0.39／0.43／<b>0.55</b>，新手组命中率 0.89／0.93／0.87、虚警率 0.31／0.28／0.35（TTA 3／4／5 s）；该文另设 TTA = 2 s，因 97.1% 行人最终未过街、样本失衡而被<b>原作者排除</b>，故不入图。<b>右</b>：三条量级取自 Chang 与 Chang（2009，<span class="m">T<sub>wd</sub></span> = 6.07–6.28 s，公交 + 舒适减速）、Chen 等（2019，d′ 峰值 TTA 4 s）、Cangut 与 Alver（2026，动作前 0.5–1.0 s）；<b>最下一条 2–5 s 是本研究对本库 14 项实证取值的归纳，非任一文献报告值</b>。</figcaption>"""

# ══════════════════════════════════════════════════════════════════════════
# 8) p16　三种「上下界」的区分
# ══════════════════════════════════════════════════════════════════════════
P16_OLD = """        <div class="ok" style="margin-top:8px"><b>下界推导（60 km/h）：</b>若求「舒适停住」（<span class="m">a<sub>comf</sub></span> = 3.5 m/s²）需 <b>≈ 6.97 s</b>；若只求「避免碰撞」（<span class="m">a<sub>max</sub></span> = 8 m/s²）降至 <b>≈ 4.3 s</b>。<br>→ <b>梯度研究得出的 3.0–4.0 s 恰好位于两者之间</b>：真实驾驶员不追求舒适停住，而是接受较大减速度换取更晚的预警。</div>"""

P16_NEW = """        <div class="ok" style="margin-top:8px"><b>本研究的下界推导（60 km/h，取 <span class="m"><span class="up">PRT</span><sub>p95</sub></span> = 1.5 s、<span class="m">δ<sub>brake</sub></span> = 0.7 s）：</b><br>
          <span class="m">t<sub>warn</sub><span class="up"> ≥ 1.5 + 16.7/</span>a<span class="up"> + 0.7</span></span>　→　「舒适停住」（<span class="m">a<sub>comf</sub></span> = 3.5 m/s²）需 <b>≈ 6.97 s</b>；「仅避免碰撞」（<span class="m">a<sub>max</sub></span> = 8 m/s²）降至 <b>≈ 4.3 s</b>。<br>→ <b>梯度研究得出的 3.0–4.0 s 恰好位于两者之间</b>：真实驾驶员不追求舒适停住，而是接受较大减速度换取更晚的预警。</div>
        <div class="warn" style="margin-top:7px" data-move="right"><b>⚠ 框架中出现三种不同的「上界／下界」，不可混用：</b>
          <table class="mini" style="margin-top:5px">
            <tr><th style="width:23%">是什么的界</th><th style="width:31%">取值</th><th>依据与用途</th></tr>
            <tr><td><b>①</b> 反应时<b>本身</b>的取值范围</td><td>驾驶员 0.74–1.17 s；含车辆侧 1.04–1.92 s</td><td>Chen 等（2013）三段分解。<b>是文献实测分布，不是设计界限</b></td></tr>
            <tr><td><b>②</b> 反应时<b>数据清洗</b>的界</td><td>下 <b>0.2 s</b>（视为预期性反应）／上 <b>2.9 s</b>（<span class="m">g</span> = 3.0）</td><td>Winkler 等（2018）规则，本研究<b>直接沿用并预注册</b>，剔除比例照实报告</td></tr>
            <tr><td><b>③</b> <b>预警提前量</b>的界（即三重约束）</td><td>下界 = ①+②式算出（4.3–6.97 s @60 km/h）；<b>上界 = <span class="m">t<sub>pred</sub></span></b>，由可接受虚警率定</td><td>下界＝运动学；上界＝Chen 等（2019）虚警率 0.55@5 s + 信任证据（p14）。<b>这一条才是设计界限</b></td></tr>
          </table></div>"""

# ══════════════════════════════════════════════════════════════════════════
# 9) p31　实验 0/1/2 的场景一致性约束
# ══════════════════════════════════════════════════════════════════════════
P31_OLD = """    <div class="note" style="flex:0 0 auto"><b>五个实验的递进逻辑（这也是本研究不是「五个并列小实验」的理由）：</b>实验 0 提供<b>零点与下界</b>（<span class="m">t<sub>0</sub></span> 分布 → 实验 1 自变量换算基准；<span class="m"><span class="up">PRT</span><sub>p95</sub></span> → 可避险区校验；<span class="m">t<sub>0</sub></span> 时刻 BTN → 触发阈值校准；<span class="m">a<sub>comf</sub></span> 实测 → 全部实验的归一化分母；方差成分 → 样本量估计）→ 实验 1 建立<b>单层时间基线</b> → 实验 2 升级为<b>分层规则</b>并检验低可靠性稳健性 → 实验 3 <b>固定全部时间参数</b>只比较「锁定在哪里」 → 实验 4 <b>固定时间与空间载体</b>只比较「如何随风险变化」。</div>"""

P31_NEW = """    <div class="note" style="flex:0 0 auto"><b>五个实验的递进逻辑（这也是本研究不是「五个并列小实验」的理由）：</b>实验 0 提供<b>零点与下界</b>（<span class="m">t<sub>0</sub></span> 分布 → 实验 1 自变量换算基准；<span class="m"><span class="up">PRT</span><sub>p95</sub></span> → 可避险区校验；<span class="m">t<sub>0</sub></span> 时刻 BTN → 触发阈值校准；<span class="m">a<sub>comf</sub></span> 实测 → 全部实验的归一化分母；方差成分 → 样本量估计）→ 实验 1 建立<b>单层时间基线</b> → 实验 2 升级为<b>分层规则</b>并检验低可靠性稳健性 → 实验 3 <b>固定全部时间参数</b>只比较「锁定在哪里」 → 实验 4 <b>固定时间与空间载体</b>只比较「如何随风险变化」。</div>
    <div class="warn" style="flex:0 0 auto;margin-top:7px"><b>由核心理论模型强制导出的一条设计约束：实验 0／1／2 必须共用同一场景族。</b>因为自变量是 <span class="m">Δt<span class="up"> = </span>t<sub>0</sub><span class="up"> − </span>t<sub>warn</sub></span>，而 <span class="m">t<sub>0</sub></span> <b>不是常数</b>——它随<b>车速</b>与<b>遮挡</b>系统变化（遮挡直接改变光学膨胀率 <span class="m">θ̇</span> 越过阈值的时刻）。因此：<b>实验 0 按「车速 40／60 × 遮挡 无／有」四个单元分别标定 <span class="m">t<sub>0</sub></span>；实验 1 只能在已标定的单元内换算 <span class="m">Δt</span>；实验 2 把车速与遮挡固定在实验 1 入选的水平上</b>，使 <span class="m">t<sub>0</sub></span> 成为常量，只让级间间隔与可靠性变化。<b>实验 3／4 已固定全部时间参数，故可另设场景操纵</b>（背景复杂度、风险演化），不受此约束。</div>"""

# (名称, 旧串, 新串, 幂等探针——只在新串中出现的特征子串)
FIXES = [
    ("p02 问题结构", P02_OLD, P02_NEW, "问题一\u3000参数值从哪里来？"),
    ("p05 SPIDER", P05_OLD, P05_NEW, "SPIDER 定「结构」，实证文献定「数值」"),
    ("p06 三重约束表", P06_OLD, P06_NEW, "① 运动学下界"),
    ("p07 生态约束出处", P07_OLD, P07_NEW, "一手出处（两篇综述均为转引）"),
    ("p09 Zhang 计时基线", P09_OLD, P09_NEW, "的秒数是以什么为基线算出来的"),
    ("p10 图注压缩", P10_OLD, P10_NEW, "本库 14 项取值 × 4 类判定结果"),
    ("p15 图数据出处", P15_OLD, P15_NEW, "本研究自绘，无本研究数据"),
    ("p16 三种上下界", P16_OLD, P16_NEW, "框架中出现三种不同的「上界／下界」"),
    ("p31 场景一致性", P31_OLD, P31_NEW, "实验 0／1／2 必须共用同一场景族"),
]


def main() -> None:
    s = HTML.read_text(encoding="utf-8")
    bak = ROOT / "_bak_rename_terms" / "slides_before_content_fix.html"
    if not bak.exists():
        shutil.copy2(HTML, bak)

    n, miss = 0, []
    for name, old, new, probe in FIXES:
        if probe in s:
            print(f"SKIP {name}（已改）")
            continue
        if old not in s:
            miss.append(name)
            print(f"⚠ MISS {name}")
            continue
        s = s.replace(old, new, 1)
        n += 1
        print(f"OK   {name}")

    HTML.write_text(s, encoding="utf-8")
    print(f"\n改 {n} 处；未命中 {len(miss)} 处 {miss}")
    if miss:
        sys.exit(1)


if __name__ == "__main__":
    main()
