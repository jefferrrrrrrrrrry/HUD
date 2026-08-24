#!/usr/bin/env python3
"""把冲突六的裁定结论同步到幻灯片 p20 与 p27。

改动
  p20 不透明度块：从「3 倍记法冲突（未裁定）」改为「已裁定：四源收敛 0.6–0.75」，
      表格加一列「换算为不透明度」，结论框换成裁定依据 + 构念差异。
  p27 冲突六块：同步为「本轮已裁定」，并保留方法学含义的第二层。
幂等：已含裁定标记则跳过。
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "文献综述_幻灯片.html"

OLD_P20 = """      <div class="box r"><h3>不透明度：3 倍记法冲突</h3>
        <table class="mini">
          <tr><th>来源</th><th class="n">值</th></tr>
          <tr><td>Ye 与 Yin（2025）</td><td class="n">0.75</td></tr>
          <tr><td>Hou 等（2024）</td><td class="n">T1/T0.75<br>T0.5/T0.35</td></tr>
          <tr><td>Li 等（2025a）</td><td class="n">0.1–1.0 梯度<br><b>≥ 0.6 与 0.7</b></td></tr>
          <tr><td>Lopez 与 Moacdieh（2025）</td><td class="n"><b>20% 与 60%</b><br>（N = 27）</td></tr>
        </table>
        <div class="warn" style="margin-top:8px"><b>「透明度」与「不透明度」在摘要层面无法区分</b>。若 20% 指不透明度，则与 ≥ 0.6 <b>相差 3 倍</b>；且前者测<b>偏好</b>、后者测<b>客观绩效</b>，<b>不得混合引用</b>。<br><b>本研究的处理：</b>主条件取 <b>0.6</b>，预实验<b>同时测 0.2</b>；若排序不一致则作为局限报告，<b>而不是挑一个支持自己的数值</b>。</div>
      </div>"""

NEW_P20 = """      <div class="box g"><h3>不透明度：3 倍冲突<span class="k3"> 已裁定</span></h3>
        <table class="mini">
          <tr><th>来源</th><th class="n">原文值</th><th class="n">换算不透明度</th></tr>
          <tr><td>Ye 与 Yin（2025）</td><td class="n">0.75</td><td class="n">0.75</td></tr>
          <tr><td>Hou 等（2024）</td><td class="n">T1/T0.75<br>T0.5/T0.35</td><td class="n"><b>最优 0.5–0.75</b></td></tr>
          <tr><td>Li 等（2025a）</td><td class="n">0.1–1.0 十档</td><td class="n"><b>≥ 0.6</b></td></tr>
          <tr><td>Lopez 与 Moacdieh（2025）</td><td class="n">20% 与 60%</td><td class="n"><b>0.6</b> 一致<br>0.2 见下</td></tr>
        </table>
        <div class="ok" style="margin-top:7px"><b>裁定依据：</b>Ye 与 Yin（2025）引 Hou 等时写「不透明度设为 <b>0.75</b>，该值在<b>可见性</b>上有优势」——<b>一个提升可见性的 0.75 只能是 alpha</b>，不可能是「75% 透明」。→ 四源收敛 <b>0.6–0.75</b>。</div>
        <div class="warn" style="margin-top:6px"><b>20% 不是推荐值：</b>原文为「20% 与 60% <b>均</b>支持情境意识」且自陈「仍需研究」。差异在<b>构念</b>：Li 测<b>读 AR 的速度</b>（越不透明越快），Lopez 测<b>路侧情境意识</b>（越不透明遮挡越多）。<b>0.6 同时满足两侧</b>。</div>
      </div>"""

OLD_P27 = ('<p class="small"><b>冲突六　不透明度 3 倍</b>：20% 若指不透明度则与 ≥ 0.6 '
           '相差 3 倍；若指透明度则方向一致而数值仍不同；且一测偏好、一测绩效。<br>'
           '<b>处理：</b>主条件 0.6 + 预实验测 0.2 的<b>敏感性检验</b>；'
           '排序不一致则报告为局限。</p>')

NEW_P27 = ('<p class="small"><b class="k3">冲突六　不透明度 3 倍（本轮已裁定）</b>：'
           '① <b>记法已定</b>——Ye 与 Yin（2025）把 Hou 等的 T 标尺当作「提升<b>可见性</b>的 0.75」'
           '使用，故 T 功能上是 alpha，最优换算为 <b>0.5–0.75</b>；'
           '② <b>剩余差异是构念而非矛盾</b>——Lopez 原文为「20% 与 60% <b>均</b>支持情境意识」，'
           '<b>未推荐 20%</b>，与 Li 等在 <b>0.6</b> 上一致。<b>四源收敛 0.6–0.75。</b><br>'
           '<b>处理更新：</b>主条件仍取 <b>0.6</b>（交集的保守下界），0.2 档的检验目的'
           '从「消解记法不确定」改为「<b>检验遮挡收益是否超过可读性代价</b>」。</p>')

OLD_METH = ('<div class="ok" style="margin-top:8px"><b>方法学意义：</b>当文献记法不统一而又'
            '无法立即取得全文时，正确做法是把不确定性<b>显式转化为敏感性检验</b>，'
            '而不是在正文中挑一个数值当作定论。</div>')

NEW_METH = ('<div class="ok" style="margin-top:8px"><b>方法学意义（两层）：</b>'
            '① 记法不统一而无法取得全文时，应把不确定性<b>显式转化为敏感性检验</b>，'
            '而不是挑一个数值当定论。<br>'
            '② <b>本轮新得</b>：B 类冲突有时可由「<b>引用者如何使用该参数</b>」间接裁定——'
            '原文不可得时，一篇<b>引用并复现其设置</b>的开放获取文献，'
            '往往在方法节保留了记法方向的判据。代价是证据等级降为间接。<br>'
            '<b class="k">须记录的漏检：</b>Hussain 与 Park（2023, IJHCI）专题研究'
            '「透明度水平 × 真实背景」，与本参数直接相关却<b>不在本库 102 篇内</b>。</div>')


def main() -> None:
    s = HTML.read_text("utf-8")
    n = 0
    # 幂等标记须取各块**独有**的文字，不能用 HTML 属性前缀（那会误命中别处）
    for label, old, new, mark in (
        ("p20 不透明度块", OLD_P20, NEW_P20, "四源收敛 <b>0.6–0.75</b>"),
        ("p27 冲突六段落", OLD_P27, NEW_P27, "冲突六　不透明度 3 倍（本轮已裁定）"),
        ("p27 方法学意义框", OLD_METH, NEW_METH, "方法学意义（两层）"),
    ):
        if mark in s:
            print(f"SKIP {label}（已改）")
            continue
        assert old in s, f"未找到 {label}"
        s = s.replace(old, new, 1)
        n += 1
        print(f"OK   {label} 已改写")

    HTML.write_text(s, encoding="utf-8")
    pages = len(re.findall(r"<section\b", s))
    print(f"\n改写 {n} 处，共 {pages} 页；请重跑 scripts/shoot_slides.py 复检溢出")


if __name__ == "__main__":
    main()
