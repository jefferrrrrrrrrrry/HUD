#!/usr/bin/env python3
"""Draw the AR-HUD pedestrian-warning thesis research framework.

Conceptual figure only: it visualizes the planned evidence chain and does not
encode observed experimental results.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures"
OUT.mkdir(parents=True, exist_ok=True)

FONT_CANDIDATES = [
    # Microsoft YaHei locations commonly used on Windows/macOS Office installs.
    Path("C:/Windows/Fonts/msyh.ttc"),
    Path("C:/Windows/Fonts/msyh.ttf"),
    Path("/Library/Fonts/Microsoft YaHei.ttf"),
    Path("/Library/Fonts/msyh.ttf"),
    # Local rendering fallback when Microsoft YaHei is not installed.
    Path("/System/Library/Fonts/PingFang.ttc"),
    Path("/System/Library/Fonts/Hiragino Sans GB.ttc"),
    Path("/System/Library/Fonts/STHeiti Medium.ttc"),
]

font_family = "DejaVu Sans"
for font_path in FONT_CANDIDATES:
    if font_path.exists():
        font_manager.fontManager.addfont(str(font_path))
        font_family = font_manager.FontProperties(fname=str(font_path)).get_name()
        break

mpl.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": [
            "Microsoft YaHei",
            "微软雅黑",
            font_family,
            "Arial",
            "Helvetica",
            "DejaVu Sans",
            "sans-serif",
        ],
        "svg.fonttype": "none",
        "pdf.fonttype": 42,
        "font.size": 7.2,
        "axes.spines.right": False,
        "axes.spines.top": False,
        "axes.linewidth": 0.8,
        "legend.frameon": False,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
    }
)


COLORS = {
    "ink": "#25313C",
    "muted": "#5D6B78",
    "line": "#80909E",
    "neutral": "#F3F5F7",
    "neutral_2": "#E7EBEF",
    "blue": "#2F679C",
    "blue_fill": "#E7F0F8",
    "blue_fill_2": "#D3E5F3",
    "teal": "#2F7E7A",
    "teal_fill": "#E5F3F1",
    "teal_fill_2": "#D1EAE6",
    "gold": "#A2762B",
    "gold_fill": "#F6EEDC",
    "final": "#244B70",
}


def add_box(
    ax,
    x,
    y,
    w,
    h,
    text,
    *,
    face="white",
    edge=None,
    lw=0.9,
    radius=0.9,
    fontsize=7.0,
    color=None,
    weight="normal",
    align="center",
    pad=0.7,
    zorder=2,
):
    edge = edge or COLORS["line"]
    color = color or COLORS["ink"]
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle=f"round,pad={pad / 10:.2f},rounding_size={radius}",
        linewidth=lw,
        edgecolor=edge,
        facecolor=face,
        zorder=zorder,
    )
    ax.add_patch(patch)
    ha = {"center": "center", "left": "left", "right": "right"}[align]
    tx = x + w / 2 if align == "center" else (x + 1.1 if align == "left" else x + w - 1.1)
    ax.text(
        tx,
        y + h / 2,
        text,
        ha=ha,
        va="center",
        fontsize=fontsize,
        color=color,
        fontweight=weight,
        linespacing=1.18,
        zorder=zorder + 1,
    )
    return patch


def add_arrow(
    ax,
    start,
    end,
    *,
    color=None,
    lw=1.1,
    style="-",
    mutation=9,
    connection="arc3,rad=0",
    zorder=3,
):
    color = color or COLORS["line"]
    arrow = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=mutation,
        linewidth=lw,
        linestyle=style,
        color=color,
        connectionstyle=connection,
        shrinkA=1.5,
        shrinkB=1.5,
        zorder=zorder,
    )
    ax.add_patch(arrow)
    return arrow


def add_band(ax, y, h, title, subtitle, *, face, edge, panel):
    band = FancyBboxPatch(
        (2.5, y),
        95,
        h,
        boxstyle="round,pad=0.12,rounding_size=1.2",
        linewidth=1.15,
        edgecolor=edge,
        facecolor=face,
        zorder=0,
    )
    ax.add_patch(band)
    ax.text(4.2, y + h - 1.7, panel, fontsize=15.5, fontweight="bold", color=edge, va="top")
    ax.text(7.0, y + h - 1.7, title, fontsize=15.5, fontweight="bold", color=edge, va="top")
    ax.text(38.0, y + h - 1.9, subtitle, fontsize=9.8, color=COLORS["muted"], va="top")


# Exact PowerPoint widescreen ratio: 13.333 x 7.5 in (16:9).
fig, ax = plt.subplots(figsize=(13.333333, 7.5))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis("off")

# Title and gap
ax.text(
    50,
    99.2,
    "AR-HUD 行人碰撞预警的时空参数研究框架",
    ha="center",
    va="top",
    fontsize=21.5,
    fontweight="bold",
    color=COLORS["ink"],
)
ax.text(
    50,
    94.3,
    "从参数筛选、机制分解到设计规范整合",
    ha="center",
    va="top",
    fontsize=10.5,
    color=COLORS["muted"],
)

add_box(
    ax,
    5,
    87.7,
    90,
    3.6,
    "研究缺口｜现有研究多比较“有/无 AR”，尚缺时间阈值、持续时长、级间间隔与空间动态机制的系统对照",
    face=COLORS["neutral"],
    edge=COLORS["line"],
    fontsize=10.8,
)

# Driver processing chain
stage_x = [5, 29.2, 53.4, 77.6]
stage_text = [
    "风险感知\n发现警告与行人",
    "定位与理解\n确认目标和冲突位置",
    "预测与决策\n判断路径侵入与紧迫度",
    "避险执行\n松油、制动或转向",
]
for x, text_value in zip(stage_x, stage_text):
    add_box(
        ax,
        x,
        81.4,
        17.4,
        4.3,
        text_value,
        face="white",
        edge=COLORS["line"],
        fontsize=10.3,
    )
for i in range(3):
    add_arrow(ax, (stage_x[i] + 17.4, 83.55), (stage_x[i + 1], 83.55), lw=1.15, mutation=10)
ax.text(
    48.8,
    79.8,
    "理论支撑：PIEV 反应链 · 情境意识（SA）",
    ha="right",
    va="top",
    fontsize=8.8,
    color=COLORS["muted"],
)
ax.text(
    51.2,
    79.8,
    "生态界面设计（EID）· 多资源与注意捕获理论",
    ha="left",
    va="top",
    fontsize=8.8,
    color=COLORS["muted"],
)
add_arrow(ax, (50, 87.7), (50, 85.7), lw=1.15, mutation=10)

add_box(
    ax,
    16,
    74.0,
    68,
    3.0,
    "总目标｜建立“时间分层 × 空间动态”的可检验设计规范，并识别其作用于风险加工链的阶段",
    face=COLORS["final"],
    edge=COLORS["final"],
    color="white",
    fontsize=11.4,
    weight="bold",
)
add_arrow(ax, (50, 81.4), (50, 77.0), lw=1.1, mutation=10)

# Study 1
add_band(
    ax,
    52.8,
    19.2,
    "研究一｜时间参数设计规范",
    "回答：何时出现、显示多久、何时升级？",
    face=COLORS["blue_fill"],
    edge=COLORS["blue"],
    panel="a",
)
add_box(
    ax,
    4.8,
    55.1,
    25.0,
    11.5,
    "实验1｜单层时间参数\n阶段A：出现 5 / 3 / 2 s\n阶段B：持续 1 / 2 / 3 s\n或状态维持\n检验：安全—平顺—负荷折中",
    face="white",
    edge=COLORS["blue"],
    fontsize=10.6,
    align="left",
)
add_box(
    ax,
    31.8,
    56.6,
    12.2,
    8.4,
    "决策门 1\n安全不劣\n效应有意义\n负荷可接受",
    face=COLORS["gold_fill"],
    edge=COLORS["gold"],
    fontsize=10.7,
    weight="bold",
)
add_box(
    ax,
    46.3,
    55.1,
    25.5,
    11.5,
    "实验2｜分层升级规则\n无警告 / 入选单层 / 二级分层\nL1–L2：0.7 / 1.0 / 1.5 s\n机制分解：发现阶段\nvs 验证—决策阶段",
    face="white",
    edge=COLORS["blue"],
    fontsize=10.5,
    align="left",
)
add_box(
    ax,
    74.2,
    55.1,
    21.0,
    11.5,
    "时间设计规范\n出现窗口\n持续与撤销规则\nL1–L2 触发与升级",
    face=COLORS["blue_fill_2"],
    edge=COLORS["blue"],
    fontsize=10.8,
    weight="bold",
)
add_arrow(ax, (29.8, 60.85), (31.8, 60.85), color=COLORS["blue"], lw=1.25, mutation=10)
add_arrow(ax, (44.0, 60.85), (46.3, 60.85), color=COLORS["blue"], lw=1.25, mutation=10)
add_arrow(ax, (71.8, 60.85), (74.2, 60.85), color=COLORS["blue"], lw=1.25, mutation=10)

# Time-to-space control hand-off. Keep this as a frameless transition note so
# it cannot visually collide with either study container.
ax.text(
    84.7,
    50.9,
    "研究二固定研究一的时间方案",
    ha="center",
    va="center",
    fontsize=9.2,
    color=COLORS["blue"],
)
add_arrow(ax, (84.7, 55.1), (84.7, 52.0), color=COLORS["blue"], style="--", lw=1.0)
add_arrow(ax, (84.7, 49.8), (84.7, 49.0), color=COLORS["blue"], style="--", lw=0.9, mutation=8)

# Study 2
add_band(
    ax,
    29.4,
    19.6,
    "研究二｜空间动态信息的促进作用",
    "先回答“锁定在哪里”，再回答“如何随风险变化”。",
    face=COLORS["teal_fill"],
    edge=COLORS["teal"],
    panel="b",
)
add_box(
    ax,
    4.8,
    31.8,
    26.0,
    11.4,
    "实验3｜空间参照系与锁定策略\n无警告 / BD / BR / BW / BW+BR\n主指标：真实行人 TTFF\n机制指标：定位转换成本",
    face="white",
    edge=COLORS["teal"],
    fontsize=10.6,
    align="left",
)
add_box(
    ax,
    32.5,
    33.3,
    12.2,
    8.3,
    "决策门 2\n定位收益明确\n安全不劣\n并列选更简",
    face=COLORS["gold_fill"],
    edge=COLORS["gold"],
    fontsize=10.7,
    weight="bold",
)
add_box(
    ax,
    47.0,
    31.8,
    26.5,
    11.4,
    "实验4｜风险演化动态（2×2）\n风险量级映射：无 / 有\n运动趋势映射：无 / 有\nD0–D3：检验主效应、交互与过度动态",
    face="white",
    edge=COLORS["teal"],
    fontsize=10.5,
    align="left",
)
add_box(
    ax,
    75.6,
    31.8,
    19.6,
    11.4,
    "空间动态规范\n参照系/锁定方式\n最小必要动态信息\n适用与失效边界",
    face=COLORS["teal_fill_2"],
    edge=COLORS["teal"],
    fontsize=10.8,
    weight="bold",
)
add_arrow(ax, (30.8, 37.5), (32.5, 37.5), color=COLORS["teal"], lw=1.25, mutation=10)
add_arrow(ax, (44.7, 37.5), (47.0, 37.5), color=COLORS["teal"], lw=1.25, mutation=10)
add_arrow(ax, (73.5, 37.5), (75.6, 37.5), color=COLORS["teal"], lw=1.25, mutation=10)

# Unified outcome chain
ax.text(
    3.3,
    25.1,
    "统一证据链",
    fontsize=12.2,
    fontweight="bold",
    color=COLORS["ink"],
    va="center",
)
metric_x = [16.5, 33.0, 49.5, 66.0, 82.5]
metric_text = [
    "感知\nTTFF · 漏检",
    "理解\n定位 · 风险判断",
    "预测\n轨迹 · 冲突点",
    "执行\n制动 · jerk",
    "安全与代价\nTTMD · 碰撞 · 负荷",
]
for x, text_value in zip(metric_x, metric_text):
    add_box(
        ax,
        x,
        22.4,
        14.2,
        5.4,
        text_value,
        face=COLORS["neutral"],
        edge=COLORS["line"],
        fontsize=9.5,
    )
for i in range(4):
    add_arrow(ax, (metric_x[i] + 14.2, 25.1), (metric_x[i + 1], 25.1), lw=0.95, mutation=8)
add_arrow(ax, (85.4, 31.8), (89.6, 27.8), color=COLORS["teal"], lw=0.9, style="--")

# Final contribution
add_arrow(ax, (50, 22.4), (50, 19.7), color=COLORS["final"], lw=1.35, mutation=11)
add_box(
    ax,
    7,
    11.0,
    86,
    8.2,
    "最终成果｜AR-HUD 行人碰撞预警时空整合模型与设计规范\n出现时机 + 持续/撤销 + 级间间隔 + 空间参照系 + 风险量级动态 + 运动趋势动态\n判定原则：安全约束优先 → 操控平顺 → 认知代价 → 反应速度与偏好",
    face=COLORS["final"],
    edge=COLORS["final"],
    color="white",
    fontsize=11.5,
    weight="bold",
)

add_box(
    ax,
    7,
    5.7,
    86,
    3.4,
    "结论边界｜短期模拟驾驶 · 视觉 AR-HUD · 行人横穿场景；真实道路、长期适应与多模态紧急干预需独立验证",
    face=COLORS["neutral"],
    edge=COLORS["neutral_2"],
    fontsize=9.1,
    color=COLORS["muted"],
)
ax.text(
    50,
    2.7,
    "实线：实验递进与参数收敛　　虚线：跨研究控制参数与统一评价约束",
    ha="center",
    va="center",
    fontsize=8.8,
    color=COLORS["muted"],
)

basename = OUT / "ar_hud_thesis_research_framework"
fig.savefig(f"{basename}.svg")
fig.savefig(f"{basename}.pdf")
fig.savefig(f"{basename}.png", dpi=300)
fig.savefig(
    f"{basename}.tiff",
    dpi=300,
    pil_kwargs={"compression": "tiff_lzw"},
)
plt.close(fig)

print(f"Saved: {basename}.svg")
print(f"Saved: {basename}.pdf")
print(f"Saved: {basename}.png")
print(f"Saved: {basename}.tiff")
