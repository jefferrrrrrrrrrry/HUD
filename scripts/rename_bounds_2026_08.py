#!/usr/bin/env python3
"""三重约束模型的四个约束名统一为二字并列：下界／上界／窗口／零点。

原名「上界线／下界线／中线」是从「三线夹逼」那张图的版面位置来的，
其中「中线」只在那张图里成立——它约束的不是 t_warn 这个点，而是
Δt = t₀ − t_warn 这个区间的宽度，与另两条不同类。改名后四者并列且等长：

    下界（运动学必要性）  t_warn ≥ PRT_p95 + v/a_comf + δ_brake
    上界（可靠性—信任）    t_warn ≤ t_pred(PPV ≥ π*)
    窗口（认知加工）      Δt = t₀ − t_warn ≥ 注意加工所需时间
    零点（自发察觉）      t₀

「窗口」与「中线」同宽（2 个汉字），ASCII 时间轴无需重排；
「上界线／下界线」少一字，四处 ASCII 图按等宽补两个连字符。
"""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ART_OLD = """   │◀── 上界线 ─▶│                    │              │
   │  可靠性—信任 │                    │              │
   │            │◀── 相对提前量 Δt ──▶│              │
   │            │                    │◀── 下界线 ──▶│
   │            │                    │   运动学必要性 │"""
ART_NEW = """   │◀── 上界 ───▶│                    │              │
   │  可靠性—信任 │                    │              │
   │            │◀── 相对提前量 Δt ──▶│              │
   │            │                    │◀── 下界 ────▶│
   │            │                    │   运动学必要性 │"""

FILES = [
    "thesis/_parts/sec2_1.md",
    "thesis/_parts/sec2_2a.md",
    "thesis/_parts/sec2_2b.md",
    "thesis/_parts/sec2_3.md",
    "thesis/_parts/sec2_4.md",
    "thesis/_parts/sec2_5_6.md",
    "thesis/_parts/add_2_1_7.md",
    "thesis/_parts/talk_p01_12.md",
    "thesis/_parts/talk_p13_34.md",
    "文献综述_幻灯片.html",
    "AR-HUD行人碰撞预警_毕业论文研究框架.md",
    "AR-HUD行人碰撞预警_毕业论文大纲与危险判定文献综述.md",
    "时间元素设计参数_专题分析.md",
    "优化方案_预警时间参数理论化重构与执行计划.md",
    "实验2_分层预警升级规则_文献与设计依据.md",
    "scripts/insert_chapter2_figures.py",
    "scripts/plot_chapter2_figures.py",
]

REPL: list[tuple[str, str]] = [
    (ART_OLD, ART_NEW),
    # 「中线」与「窗口」同宽，ASCII 图内直接替换
    ("中线：SPIDER 加工窗口", "窗口：SPIDER 五阶段加工"),
    ("中线：认知加工窗口（SPIDER 五阶段）", "窗口：认知加工（SPIDER 五阶段）"),
    ("**中线**：认知加工窗口", "**窗口**：认知加工"),
    ("中线：认知加工窗口", "窗口：认知加工"),
    ("中线（认知加工窗口）", "窗口（认知加工）"),
    ("中线（加工窗口）", "窗口（认知加工）"),
    ("认知加工中线", "认知加工窗口"),
    ("中线", "窗口"),
    ("上界线", "上界"),
    ("下界线", "下界"),
    ("三条约束线", "三条约束"),
    ("三条线", "三条约束"),
    # 一处「界定…共同界定」的重复表述
    ("界定为被运动学下界、可靠性上界、认知加工窗口三条约束共同界定、并以自发察觉时刻",
     "界定为同时受运动学下界、可靠性上界与认知加工窗口三重约束、并以自发察觉时刻"),
]


def main() -> None:
    bak = ROOT / "_bak_rename_terms"
    bak.mkdir(exist_ok=True)
    n_files = 0
    for rel in FILES:
        p = ROOT / rel
        if not p.exists():
            print(f"⚠ MISS {rel}")
            continue
        s0 = p.read_text(encoding="utf-8")
        s = s0
        for old, new in REPL:
            s = s.replace(old, new)
        if s == s0:
            print(f"·    {rel}（无需改）")
            continue
        dst = bak / ("b2_" + rel.replace("/", "__"))
        if not dst.exists():
            shutil.copy2(p, dst)
        p.write_text(s, encoding="utf-8")
        n_files += 1
        print(f"OK   {rel}")

    left = []
    for rel in FILES:
        p = ROOT / rel
        if p.exists():
            t = p.read_text(encoding="utf-8")
            for kw in ("上界线", "下界线", "中线", "三条线"):
                if kw in t:
                    left.append(f"{rel}: {kw} × {t.count(kw)}")
    print(f"\n改写 {n_files} 个文件；残留 {len(left)} 处")
    for x in left:
        print("  ⚠", x)


if __name__ == "__main__":
    main()
