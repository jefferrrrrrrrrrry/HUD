#!/usr/bin/env python3
"""术语重构（2026-08）：废除「三线夹逼／夹逼」与「红利」两组不清晰的表述。

改动一：核心理论模型改名
  「三线夹逼模型」→「三重约束模型」（全称：预警时刻的三重约束模型）
  动词「夹逼」→「共同界定／共同框定／限定」，视上下文选词
  理由：「夹逼」是数学分析里的极限定理术语（squeeze theorem），
        借来描述「三个不等式约束共同确定一个可行区间」并不准确——
        夹逼定理要求两侧收敛到同一点，而本模型要的是一个有宽度的区间。
        「三重约束 + 可行设计区间」既准确又不需要听众做术语转换。

改动二：AR-HUD 收益分解改名
  「位置红利」→「位置增益」，「共形红利」→「共形增益」
  理由：「红利」（dividend）指无需额外投入即可分得的收益，隐含
        「白得的好处」这层意思，与实验语境不合；且它不是人因/HCI
        领域的既有术语，听众须自行猜测所指。
        「增益（gain）」是标准术语，且能直接写成可加分解：
            总增益 = 位置增益 + 共形增益
        位置增益＝把信息搬进前风挡视野所得（普通 HUD 即可获得）；
        共形增益＝图形与真实目标空间贴合所得的额外量（AR 独有）。

幂等：重复执行不会二次改写（替换目标里不含被替换的源串）。
"""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FILES = [
    "thesis/_parts/sec2_1.md",
    "thesis/_parts/sec2_2a.md",
    "thesis/_parts/sec2_2b.md",
    "thesis/_parts/sec2_3.md",
    "thesis/_parts/sec2_4.md",
    "thesis/_parts/sec2_5_6.md",
    "thesis/_parts/talk_p01_12.md",
    "thesis/_parts/talk_p13_34.md",
    "文献综述_幻灯片.html",
    "AR-HUD行人碰撞预警_毕业论文研究框架.md",
    "AR-HUD行人碰撞预警_毕业论文大纲与危险判定文献综述.md",
    "时间元素设计参数_专题分析.md",
    "空间元素设计参数_专题分析.md",
    "优化方案_预警时间参数理论化重构与执行计划.md",
    "实验2_分层预警升级规则_文献与设计依据.md",
    "最终交付清单.md",
    "README.md",
    "scripts/insert_chapter2_figures.py",
    "scripts/plot_chapter2_figures.py",
    "summaries/12_2024_边扬_网联HUD行人过街预警.md",
]

# 顺序敏感：长串在前
REPL: list[tuple[str, str]] = [
    # ── 模型名 ────────────────────────────────────────────────────────
    ("核心理论模型：三线夹逼", "核心理论模型：预警时刻的三重约束"),
    ("三线夹逼 + 一个零点", "三重约束 + 一个零点"),
    ("三线夹逼 + SPIDER", "三重约束 + SPIDER"),
    ("时间参数的三线夹逼模型", "预警时刻的三重约束模型"),
    ("三线夹逼模型", "三重约束模型"),
    ("三线夹逼框架", "三重约束框架"),
    ("三线夹逼", "三重约束"),
    # ── 动词「夹逼」：按搭配选词 ──────────────────────────────────────
    ("被三条约束线夹逼", "由三条约束共同界定"),
    ("受三条约束线夹逼", "受三条约束共同界定"),
    ("三条约束夹逼", "三条约束共同界定"),
    ("认知加工中线夹逼", "认知加工窗口共同界定"),
    ("被哪些约束夹逼", "被哪些约束限定"),
    ("四源夹逼区间", "四源共同界定的区间"),
    ("四源夹逼", "四源共同界定"),
    ("三源夹逼出", "三源共同界定出"),
    ("三源夹逼", "三源共同界定"),
    ("**夹逼**出", "**共同界定**出"),
    ("夹逼级间间隔", "界定级间间隔"),
    ("夹逼依据", "界定依据"),
    ("夹逼结论", "区间结论"),
    ("夹逼区间", "共同界定的区间"),
    ("产业时序的夹逼", "产业时序的共同界定"),
    ("产业时序夹逼", "产业时序共同界定"),
    ("区间夹逼", "区间界定"),
    ("夹逼得出", "共同界定得出"),
    ("夹逼出", "共同界定出"),
    ("夹逼", "共同界定"),          # 兜底
    # ── 收益分解改名 ──────────────────────────────────────────────────
    ("位置红利", "位置增益"),
    ("共形红利", "共形增益"),
    ("视野内显示\"的红利", "视野内显示\"的位置增益"),
    ("视野内显示」的红利", "视野内显示」的位置增益"),
]


def main() -> None:
    bak = ROOT / "_bak_rename_terms"
    bak.mkdir(exist_ok=True)
    total = 0
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
        dst = bak / rel.replace("/", "__")
        if not dst.exists():
            shutil.copy2(p, dst)
        p.write_text(s, encoding="utf-8")
        n = sum(s0.count(o) for o, _ in REPL)
        total += 1
        print(f"OK   {rel}（{n} 处）")

    left = []
    for rel in FILES:
        p = ROOT / rel
        if p.exists():
            t = p.read_text(encoding="utf-8")
            for kw in ("夹逼", "红利"):
                if kw in t:
                    left.append(f"{rel}: {kw} × {t.count(kw)}")
    print(f"\n改写 {total} 个文件；残留 {len(left)} 处" + ("：" if left else "（已清零）"))
    for x in left:
        print("  ⚠", x)


if __name__ == "__main__":
    main()
