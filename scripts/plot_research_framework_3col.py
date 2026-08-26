#!/usr/bin/env python3
"""研究问题 / 方法 / 研究内容 三列研究框架图（仿开题 PPT 体例）。

概念图：只表达计划中的研究结构与证据递进，不编码任何实验结果。
"""
from __future__ import annotations

from pathlib import Path

import matplotlib as mpl

mpl.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures"
OUT.mkdir(parents=True, exist_ok=True)

for f in (ROOT / "assets" / "fonts").glob("*.otf"):
    font_manager.fontManager.addfont(str(f))
CJK = "Noto Sans CJK SC"
mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": [CJK, "DejaVu Sans"],
    "axes.unicode_minus": False,
    "svg.fonttype": "none",
    "pdf.fonttype": 42,
})

BLUE = "#4472C4"
BLUE_D = "#2F528F"
GREY = "#BFBFBF"
GREY_D = "#7F7F7F"
LINE = "#404040"
W, H = 1390, 850

fig, ax = plt.subplots(figsize=(13.90, 8.50), dpi=100)
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.invert_yaxis()
ax.axis("off")


def rrect(x, y, w, h, fc, ec, lw=1.2, r=10, z=2):
    p = FancyBboxPatch((x + r, y + r), w - 2 * r, h - 2 * r,
                       boxstyle=f"round,pad={r}", linewidth=lw,
                       facecolor=fc, edgecolor=ec, zorder=z)
    ax.add_patch(p)
    return p


def rect(x, y, w, h, fc, ec, lw=1.1, z=2):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=fc, edgecolor=ec,
                           linewidth=lw, zorder=z))


def txt(x, y, s, size=12, color="#000000", weight="normal", ha="center", va="center", z=5):
    ax.text(x, y, s, fontsize=size, color=color, fontweight=weight,
            ha=ha, va=va, zorder=z, linespacing=1.55)


def chevron(x, y, w, h, fc="#FFFFFF", ec=LINE, lw=1.1):
    """五边形箭头（PPT 的 V 形箭头）。"""
    t = h * 0.30
    pts = [(x, y + t), (x + w * 0.55, y + t), (x + w * 0.55, y),
           (x + w, y + h / 2), (x + w * 0.55, y + h),
           (x + w * 0.55, y + h - t), (x, y + h - t)]
    ax.add_patch(Polygon(pts, closed=True, facecolor=fc, edgecolor=ec,
                         linewidth=lw, zorder=3))


# ── 列几何 ────────────────────────────────────────────────────────────────
C1X, C1W = 46, 250          # 研究问题
C2X, C2W = 370, 92          # 方法
C3X, C3W = 570, 774         # 研究内容
CHX, CHW = 468, 96          # 箭头带

# ── 顶部表头 ──────────────────────────────────────────────────────────────
for x, w, s in ((C1X, C1W, "研究问题"), (C2X, C2W + 20, "方法"), (C3X, C3W, "研究内容")):
    rrect(x, 28, w, 68, "#FFFFFF", LINE, lw=1.3, r=12)
    txt(x + w / 2, 62, s, 17, weight="bold")

# ── 行几何：三个研究问题 ───────────────────────────────────────────────────
ROWS = [
    dict(qy=128, qh=210,
         q="① 无预警辅助条件下，\n驾驶员何时自发察觉\n横穿行人、多快启动\n首个避险动作？"),
    dict(qy=372, qh=210,
         q="② AR-HUD 行人预警应\n相对该基线提前多少、\n持续多久、何时升级？"),
    dict(qy=616, qh=206,
         q="③ 预警应锁定在哪里、\n空间信息如何随风险\n连续变化？"),
]
for r in ROWS:
    rect(C1X, r["qy"], C1W, r["qh"], BLUE, BLUE_D)
    txt(C1X + C1W / 2, r["qy"] + r["qh"] / 2, r["q"], 12.5, "#FFFFFF")

# ── 方法列：两个灰块 ───────────────────────────────────────────────────────
rect(C2X, 128, C2W, 210, GREY, GREY_D)
txt(C2X + C2W / 2, 233, "基线\n标定\n研究", 13.5, "#000000", weight="bold")

rect(C2X, 372, C2W, 450, GREY, GREY_D)
txt(C2X + C2W / 2, 597, "模\n拟\n驾\n驶\n实\n验\n研\n究", 13.5, "#000000", weight="bold")

# 问题框 → 方法块 的细连线
for r in ROWS:
    yc = r["qy"] + r["qh"] / 2
    ax.plot([C1X + C1W, C2X], [yc, yc], color=LINE, lw=1.1, zorder=1)

# 方法块 → 研究内容 的 V 形箭头
for cy in (233, 480, 719):
    chevron(CHX, cy - 34, CHW, 68)

# ── 研究内容列 ────────────────────────────────────────────────────────────
BAR_H = 46


def block(y, h, title, rows, tagged=False):
    """一个研究块：顶部蓝色标题条 + 白底内容区。"""
    rect(C3X, y, C3W, BAR_H, BLUE, BLUE_D)
    txt(C3X + C3W / 2, y + BAR_H / 2, title, 14, "#FFFFFF", weight="bold")
    rect(C3X, y + BAR_H, C3W, h - BAR_H, "#FFFFFF", LINE)
    if not tagged:
        n = len(rows)
        inner = h - BAR_H
        gap = 42
        y0 = y + BAR_H + inner / 2 - gap * (n - 1) / 2
        for i, s in enumerate(rows):
            cy = y0 + gap * i
            txt(C3X + 26, cy, "·", 18, ha="left")
            txt(C3X + 48, cy, s, 12.5, ha="left")
    else:
        tw = 176
        n = len(rows)
        inner = h - BAR_H
        for i, (tag, s) in enumerate(rows):
            cy = y + BAR_H + inner * (i + 0.5) / n
            txt(C3X + 18 + tw / 2, cy, tag, 13, weight="bold")
            bx, bw = C3X + 18 + tw + 8, C3W - (18 + tw + 8) - 18
            rect(bx, cy - 30, bw, 60, "#FFFFFF", LINE, lw=1.0)
            txt(bx + bw / 2, cy, s, 12, ha="center")


block(128, 210, "研究零：驾驶员自发察觉基线的标定（实验 0）", [
    "标定自发察觉时刻 $t_0$、感知反应时 PRT 与 $a_{req}$ 可行域",
    "为实验 1–4 提供时间零点、运动学下界与样本量方差成分",
])

block(372, 210, "研究一：AR-HUD 行人碰撞预警的时间参数设计规范", [
    ("单层预警", "实验 1：相对提前量 $\\Delta t$（0/+1.0/+2.5 s）× 触发准则（时间阈值 / BTN）"),
    ("分层预警", "实验 2：级间间隔（0.7/1.0/1.5 s）× 系统可靠性（100% / 80%）"),
], tagged=True)

block(616, 206, "研究二：空间动态信息对预警效果的促进作用", [
    ("空间参照系", "实验 3：Baseline / BD / BR / BW / BW+BR × 背景视觉复杂度"),
    ("风险演化动态", "实验 4：风险量级映射（BTN）× 运动趋势映射　2 × 2"),
], tagged=True)

fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
for ext in ("svg", "png", "pdf"):
    fig.savefig(OUT / f"research_framework_3col.{ext}",
                dpi=(600 if ext == "png" else None), bbox_inches="tight",
                pad_inches=0.06, facecolor="white")
print("saved:", ", ".join(f"figures/research_framework_3col.{e}" for e in ("svg", "png", "pdf")))
