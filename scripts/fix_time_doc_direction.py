#!/usr/bin/env python3
"""修正《时间元素设计参数_专题分析.md》中 Zhang 等（2024）制动距离的方向性笔误。

问题
  该研究的 d_b 是「**事件触发后行驶距离**」——数值越小表示制动越早。
  基线 64.50 m、HUD 27.33 m，即 HUD 使制动**提前约 37 m**。
  原文档两处把方向写反了：
    L403「显著**增大**了首次制动距离」——应为「显著**缩短**」
    L425「27.3 m，**远大于**基线 64.5 m」——27.3 明显小于 64.5，自相矛盾

  同时补一句量纲说明，避免后续再次读反。
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "时间元素设计参数_专题分析.md"

FIXES = [
    (
        '该研究证明，HUD网联预警相较基线显著增大了"首次制动距离"'
        "（HUD最早=27.3 m vs 基线=64.5 m，差值37 m）",
        '该研究证明，HUD网联预警相较基线显著**缩短**了"首次制动距离"'
        "（HUD=27.33 m vs 基线=64.50 m，**提前约37 m**）"
        "——注意该量为**事件触发后行驶距离**，数值越小表示制动越早",
    ),
    (
        "中国样本（N=34）在该距离条件下的首次制动距离平均为27.3 m，"
        "远大于基线64.5 m的制动距离，证明在中国城市低速场景下较长的Lead Time仍具有有效性。",
        "中国样本（N=34）在该距离条件下的首次制动距离平均为**27.33 m，"
        "显著短于基线的64.50 m**（即制动位置提前约37 m；该量为事件触发后行驶距离，"
        "越小越早），证明在中国城市低速场景下较长的Lead Time仍具有有效性。",
    ),
]


def main() -> None:
    s = DOC.read_text("utf-8")
    n = 0
    for old, new in FIXES:
        if old not in s:
            print(f"SKIP（已修或措辞不符）：{old[:34]}…")
            continue
        s = s.replace(old, new, 1)
        n += 1
        print(f"FIX  {old[:34]}…")
    DOC.write_text(s, encoding="utf-8")

    # 自检：不得再出现「27.3 …… 远大于 …… 64.5」这类反向表述
    bad = [k for k in ("远大于基线64.5", "增大了\"首次制动距离\"", "增大了“首次制动距离”") if k in s]
    assert not bad, f"仍有反向表述：{bad}"
    print(f"\n共修 {n} 处，自检通过 -> {DOC.name}")


if __name__ == "__main__":
    main()
