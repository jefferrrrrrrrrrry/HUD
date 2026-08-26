#!/usr/bin/env python3
"""第 2 章文献综述的自绘图件（4 张）。

全部为综述性示意图/证据谱，数据点均取自正文已核验的文献数值，不含任何本研究结果。
输出 svg + png（600 dpi）到 figures/。
"""
from __future__ import annotations

from pathlib import Path

import matplotlib as mpl

mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.patches import FancyArrowPatch, Rectangle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures"
OUT.mkdir(parents=True, exist_ok=True)
for f in (ROOT / "assets" / "fonts").glob("*.otf"):
    font_manager.fontManager.addfont(str(f))
mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Noto Sans CJK SC", "DejaVu Sans"],
    "axes.unicode_minus": False,
    "svg.fonttype": "none",
    "pdf.fonttype": 42,
    "axes.edgecolor": "#404040",
    "axes.labelcolor": "#1a1a1a",
    "text.color": "#1a1a1a",
    "xtick.color": "#404040",
    "ytick.color": "#404040",
})

BLUE, RED, GREEN, GREY, AMBER = "#4472C4", "#C00000", "#3E7D3E", "#8C8C8C", "#E0A100"


def save(fig, stem: str) -> None:
    for ext in ("svg", "png"):
        fig.savefig(OUT / f"{stem}.{ext}", dpi=(600 if ext == "png" else None),
                    bbox_inches="tight", pad_inches=0.10, facecolor="white")
    plt.close(fig)
    print("saved", stem)


# ────────────────────────────────────────────────────────────────────────────
# 图 2-1　预警出现时机的证据谱
# ────────────────────────────────────────────────────────────────────────────
def fig_onset_spectrum() -> None:
    # (标签, TTC 秒, 类别)  类别: eff 有效 / ineff 无效 / neutral 采用但未对照 / decl 收益递减
    pts = [
        ("Zhang 等 (2015) 2.5 s\n与无预警无差异", 2.5, "ineff"),
        ("Lubbe (2017) 1.8 s\n临界级", 1.8, "neutral"),
        ("Lubbe (2017) 2.5 s\n提示级", 2.5, "neutral"),
        ("Phan 等 (2016) 2.0 s\n+ 距离 16.6 m 复合", 2.0, "neutral"),
        ("Huo 与 Alla (2025)\n2.5 s", 2.5, "eff"),
        ("Kim 等 (2018) 2.5 s\nNear", 2.5, "eff"),
        ("Wu 等 (2024) < 3 s", 3.0, "eff"),
        ("Chen 等 (2024b)\nTHW ≤ 3 s", 3.0, "eff"),
        ("Zhang 等 (2015)\n推荐 3.0–4.0 s", 3.5, "eff"),
        ("Kang 等 (2016) 4.0 s\n优于 2.0 s（听觉）", 4.0, "eff"),
        ("Suzuki 等 (2010) 视觉层 4.0 s\n→ 听觉层 2.0 s", 4.0, "neutral"),
        ("Kim 等 (2018) 5.0 s Far\n峰值减速度 +34.46%", 5.0, "decl"),
        ("Wang 等 (2025) ≤ 5 s\n未降低反应时", 5.0, "decl"),
        ("Zhang 等 (2024) 100 m\n≈ 6 s @60 km/h", 6.0, "neutral"),
    ]
    COLOR = {"eff": GREEN, "ineff": RED, "neutral": BLUE, "decl": AMBER}
    MARK = {"eff": "o", "ineff": "X", "neutral": "s", "decl": "^"}

    fig, ax = plt.subplots(figsize=(11.6, 5.6))
    ax.axvspan(0, 3.0, color=RED, alpha=0.055)
    ax.axvspan(3.0, 4.0, color=GREEN, alpha=0.085)
    ax.axvspan(4.0, 6.5, color=AMBER, alpha=0.06)
    ax.text(1.5, 14.6, "单层预警无效区\n（< 3.0 s）", ha="center", va="top", fontsize=10.5, color=RED)
    ax.text(3.5, 14.6, "梯度证据推荐区\n3.0–4.0 s", ha="center", va="top", fontsize=10.5,
            color=GREEN, fontweight="bold")
    ax.text(5.3, 14.6, "收益递减区\n（> 4.0 s）", ha="center", va="top", fontsize=10.5, color=AMBER)

    ys = list(range(len(pts) - 1, -1, -1))
    for (lab, x, kind), y in zip(pts, ys):
        ax.scatter([x], [y], s=115, marker=MARK[kind], color=COLOR[kind], zorder=4,
                   edgecolor="white", linewidth=0.9)
        ax.plot([0, x], [y, y], color=GREY, lw=0.5, alpha=0.45, zorder=1)
        ax.text(x + 0.13, y, lab, va="center", fontsize=9.3, color="#1a1a1a")

    # 人类判别能力上界（Chen 等 2019）
    ax.axvline(4.0, color=GREEN, ls="--", lw=1.4, alpha=0.85, zorder=2)
    ax.annotate("人类意图判别力峰值 TTA 4 s\n（Chen 等, 2019；5 s 时虚警率 0.55）",
                xy=(4.0, 7.4), xytext=(6.55, 9.4), fontsize=9.4, color=GREEN,
                ha="left", arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.1,
                connectionstyle="arc3,rad=-0.18"))
    ax.axvline(1.6, color="#666666", ls=":", lw=1.3, zorder=2)
    ax.text(1.63, 0.42, "AEB 物理最早介入 1.6 s\n（Coelingh 等, 2010）",
            fontsize=9.0, color="#555555", va="bottom",
            bbox=dict(facecolor="white", edgecolor="none", pad=1.2))

    ax.set_xlim(0, 8.9)
    ax.set_ylim(-0.7, 15.1)
    ax.set_xticks(np.arange(0, 6.6, 0.5))
    ax.set_xlabel("预警触发时刻（距冲突的剩余时间 TTC / TTMD，s）", fontsize=11.5)
    ax.set_yticks([])
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)
    ax.grid(axis="x", color="#DDDDDD", lw=0.5)

    handles = [
        plt.Line2D([], [], marker="o", ls="", color=GREEN, label="报告有效"),
        plt.Line2D([], [], marker="X", ls="", color=RED, label="报告无效（与无预警无差异）"),
        plt.Line2D([], [], marker="^", ls="", color=AMBER, label="过度反应或无增益"),
        plt.Line2D([], [], marker="s", ls="", color=BLUE, label="采用但未与其他阈值对照"),
    ]
    ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.735, 0.44),
              frameon=True, framealpha=0.94, edgecolor="#CCCCCC", fontsize=9.6)
    save(fig, "ch2_fig_onset_spectrum")


# ────────────────────────────────────────────────────────────────────────────
# 图 2-2　三重约束模型
# ────────────────────────────────────────────────────────────────────────────
def fig_three_bounds() -> None:
    fig, ax = plt.subplots(figsize=(11.4, 4.8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6.05)
    ax.axis("off")

    ax.text(0.30, 5.98, "预警时刻的三重约束：三者的交集即可行设计区间",
            ha="left", va="top", fontsize=10.8, color="#333333", fontweight="bold")
    ax.annotate("", xy=(9.7, 4.5), xytext=(0.35, 4.5),
                arrowprops=dict(arrowstyle="-|>", color="#333333", lw=1.6))
    ax.text(9.72, 5.98, "→ 横轴为距冲突的剩余时间（右侧更紧急）", ha="right", va="top",
            fontsize=10.0, color="#666666")

    marks = [(1.5, "$t_{pred}$\n可预测起点"), (3.4, "$t_{warn}$\n预警时刻"),
             (5.9, "$t_0$\n自发察觉", ), (7.8, "$t_{LPB}$\n最晚制动点"), (9.3, "冲突")]
    for m in marks:
        x, lab = m[0], m[1]
        ax.plot([x, x], [4.32, 4.68], color="#333333", lw=1.5)
        ax.text(x, 5.02, lab, ha="center", va="bottom", fontsize=10.2,
                fontweight=("bold" if "t_{warn}" in lab or "t_0" in lab else "normal"))

    WBOX = dict(facecolor="white", edgecolor="none", pad=1.6)

    def band(y, x0, x1, color, title, tail, side="right", inside=None):
        """带 + 双向箭头。标题在带上方，公式与负责实验并排放在带的外侧，
        故不会出现「箭头穿过文字」；只有足够宽的带才在带内写字（并加白底）。"""
        ax.add_patch(Rectangle((x0, y), x1 - x0, 0.42, facecolor=color, alpha=0.20,
                               edgecolor=color, lw=1.2, zorder=2))
        ax.add_patch(FancyArrowPatch((x0 + 0.06, y + 0.21), (x1 - 0.06, y + 0.21),
                                     arrowstyle="<|-|>", mutation_scale=11,
                                     color=color, lw=1.3, zorder=3))
        ax.text(x0 + 0.08, y + 0.60, title, fontsize=10.6, color=color,
                fontweight="bold", zorder=6)
        if tail:
            ax.text(x1 + 0.16 if side == "right" else x0 - 0.16, y + 0.21, tail,
                    va="center", ha="left" if side == "right" else "right",
                    fontsize=9.3, color="#333333", zorder=6)
        if inside:
            ax.text((x0 + x1) / 2, y + 0.21, inside, ha="center", va="center",
                    fontsize=9.3, zorder=6, bbox=WBOX)

    band(3.25, 1.5, 3.4, RED, "上界：可靠性—信任",
         "$t_{warn}\\leq t_{pred}(PPV \\geq \\pi^{*})$\n→ 实验 2 操纵系统可靠性")
    band(2.15, 3.4, 5.9, BLUE, r"相对提前量 $\Delta t = t_0 - t_{warn}$",
         "本研究估计 $\\Delta t \\geq 0.9$–1.2 s\n→ 实验 1 的核心自变量")
    band(1.05, 5.9, 7.8, GREEN, "下界：运动学必要性",
         "$t_{warn} \\geq PRT_{p95}+v_{ego}/a_{comf}+\\delta_{brake}$\n→ 实验 0 测 PRT 分布",
         side="left")
    band(0.18, 3.4, 7.8, AMBER, "窗口：认知加工（SPIDER 五阶段）", "",
         inside="S 617 ms（实测）+ I 300–600 ms（本研究推导）")

    ax.annotate("零点由实验 0 实测；\nτ 理论校验值 TTC ≈ 3.2 s @60 km/h",
                xy=(5.9, 4.28), xytext=(6.42, 3.78), fontsize=9.3, color="#444444",
                zorder=6,
                arrowprops=dict(arrowstyle="->", color="#888888", lw=1.0))
    save(fig, "ch2_fig_three_bounds")


# ────────────────────────────────────────────────────────────────────────────
# 图 2-3　三个时间窗的张力：人因需求 / 人类判别 / 算法预测
# ────────────────────────────────────────────────────────────────────────────
def fig_time_window_tension() -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.4, 4.5),
                                   gridspec_kw={"width_ratios": [1.05, 1]})

    # 左：Chen 等 (2019) 命中率与虚警率
    tta = np.array([3, 4, 5])
    ax1.plot(tta, [0.86, 0.92, 0.90], "-o", color=BLUE, lw=2, label="熟练：命中率")
    ax1.plot(tta, [0.89, 0.93, 0.87], "--o", color=BLUE, lw=1.6, alpha=0.6,
             markerfacecolor="white", label="新手：命中率")
    ax1.plot(tta, [0.39, 0.43, 0.55], "-s", color=RED, lw=2, label="熟练：虚警率")
    ax1.plot(tta, [0.31, 0.28, 0.35], "--s", color=RED, lw=1.6, alpha=0.6,
             markerfacecolor="white", label="新手：虚警率")
    ax1.axvline(4, color=GREEN, ls=":", lw=1.4)
    ax1.text(4.03, 0.13, "判别力峰值", fontsize=9.4, color=GREEN)
    ax1.annotate("虚警率 0.55", xy=(5, 0.55), xytext=(4.35, 0.68), fontsize=9.4, color=RED,
                 arrowprops=dict(arrowstyle="->", color=RED, lw=1.0))
    ax1.set_xticks(tta)
    ax1.set_xlabel("到达时间 TTA（s）", fontsize=11)
    ax1.set_ylabel("比率", fontsize=11)
    ax1.set_ylim(0.1, 1.0)
    ax1.set_title("驾驶员对行人过街意图的判别绩效\n（Chen 等, 2019，Table 1 原值）", fontsize=11.0)
    ax1.legend(frameon=False, fontsize=9, loc="center left")
    ax1.grid(color="#EEEEEE", lw=0.6)
    for sp in ("top", "right"):
        ax1.spines[sp].set_visible(False)

    # 右：三个时间窗
    rows = [
        ("人因需求\n（大型车 + 舒适减速）", 0, 6.28, GREEN,
         "6.07–6.28 s\nChang 与 Chang (2009)"),
        ("人类判别能力上界", 0, 4.0, BLUE, "TTA 4 s 峰值\nChen 等 (2019)"),
        ("算法预测能力上界", 0, 1.0, RED, "动作前 0.5–1.0 s\nCangut 与 Alver (2026)"),
        ("本领域实证研究的\n实际取值区间", 2.0, 5.0, "#8064A2",
         "2–5 s\n（本研究对本库 14 项取值的归纳，\n非任一文献报告值）"),
    ]
    for i, (lab, x0, x1, c, note) in enumerate(rows):
        y = len(rows) - 1 - i
        ax2.barh(y, x1 - x0, left=x0, height=0.46, color=c, alpha=0.35,
                 edgecolor=c, lw=1.4)
        ax2.text(-0.22, y, lab, ha="right", va="center", fontsize=10)
        ax2.text(x1 + 0.16, y, note, va="center", fontsize=9.1, color="#333333")
    ax2.set_xlim(-0.05, 10.6)
    ax2.set_ylim(-0.7, 3.7)
    ax2.set_xticks(range(0, 8))
    ax2.set_xlabel("碰撞前时间（s）", fontsize=11)
    ax2.set_yticks([])
    ax2.set_title("需求 > 人类判别上界 > 算法预测上界", fontsize=11.5)
    ax2.grid(axis="x", color="#EEEEEE", lw=0.6)
    for sp in ("top", "right", "left"):
        ax2.spines[sp].set_visible(False)

    fig.subplots_adjust(wspace=0.42)
    save(fig, "ch2_fig_time_window_tension")


# ────────────────────────────────────────────────────────────────────────────
# 图 2-4　眼动指标：从单调假设到区间判定
# ────────────────────────────────────────────────────────────────────────────
def fig_eye_metric_bands() -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.2, 4.0))

    # TTFF
    ax1.axvspan(100, 300, color=GREEN, alpha=0.16, label="最优区间 100–300 ms")
    ax1.axvspan(0, 100, color=GREY, alpha=0.14)
    bars = [("BW 目标锁定\n(Wu 等, 2024)", 617, BLUE),
            ("分级警告\n(Chen 等, 2024b)", 1051, BLUE),
            ("行人探测潜伏期\n(Chen 等, 2019)", 1345, GREY),
            ("BD 屏幕固定\n(Wu 等, 2024)", 2563, RED),
            ("BR 道路锁定\n(Wu 等, 2024)", 2730, RED)]
    for i, (lab, v, c) in enumerate(bars):
        y = len(bars) - 1 - i
        ax1.barh(y, v, height=0.5, color=c, alpha=0.72)
        ax1.text(v + 55, y, f"{v} ms", va="center", fontsize=9.6)
        ax1.text(-90, y, lab, ha="right", va="center", fontsize=9.5)
    ax1.set_xlim(0, 3350)
    ax1.set_ylim(-0.7, 4.7)
    ax1.set_yticks([])
    ax1.set_xlabel("首次注视时间 TTFF（ms）", fontsize=11)
    ax1.set_title("TTFF：最优区间 100–300 ms（Zhu 等, 2025）\nBW 617 ms 属\"显著改善但未达最优\"",
                  fontsize=11)
    ax1.legend(frameon=False, fontsize=9.4, loc="lower right")
    ax1.grid(axis="x", color="#EEEEEE", lw=0.6)
    for sp in ("top", "right", "left"):
        ax1.spines[sp].set_visible(False)

    # TDT
    ax2.axvspan(500, 2000, color=GREEN, alpha=0.16, label="最优区间 500–2 000 ms")
    ax2.axvspan(0, 500, color=AMBER, alpha=0.13, label="≤ 500 ms 注意不足")
    ax2.axvspan(2000, 4000, color=RED, alpha=0.10, label="≥ 2 000 ms 分心")
    bars2 = [("屏幕固定箭头\n(Gabbard 等, 2019)", 1170, BLUE),
             ("50% 占空比闪烁\n(Shen 等, 2026)", 1041.58, GREEN),
             ("无闪烁\n(Shen 等, 2026)", 1633.38, AMBER),
             ("高沉浸分心 + 无闪烁\n(Shen 等, 2026)", 2777.80, RED),
             ("贴地共形箭头\n(Gabbard 等, 2019)", 3330, RED)]
    for i, (lab, v, c) in enumerate(bars2):
        y = len(bars2) - 1 - i
        ax2.barh(y, v, height=0.5, color=c, alpha=0.72)
        ax2.text(v + 60, y, f"{v:g}", va="center", fontsize=9.6)
        ax2.text(-110, y, lab, ha="right", va="center", fontsize=9.5)
    ax2.set_xlim(0, 4000)
    ax2.set_ylim(-0.7, 4.7)
    ax2.set_yticks([])
    ax2.set_xlabel("注视时长 / 反应时（ms）", fontsize=11)
    ax2.set_title("TDT：双侧门槛判定\n共形箭头 3 330 ms 已越过分心上界", fontsize=11)
    ax2.legend(frameon=False, fontsize=8.8, loc="lower right")
    ax2.grid(axis="x", color="#EEEEEE", lw=0.6)
    for sp in ("top", "right", "left"):
        ax2.spines[sp].set_visible(False)

    fig.subplots_adjust(wspace=0.58)
    save(fig, "ch2_fig_eye_metric_bands")


if __name__ == "__main__":
    fig_onset_spectrum()
    fig_three_bounds()
    fig_time_window_tension()
    fig_eye_metric_bands()
