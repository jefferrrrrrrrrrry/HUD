#!/usr/bin/env python3
"""学术表达规范校验器。

用法：
    python3 scripts/verify_style.py                # 校验默认目标集
    python3 scripts/verify_style.py <file> [...]   # 校验指定文件

校验项：
  [1] 口语化句式（幻灯片正文严格；讲稿放宽口播连接词，但研究问题句式仍受约束）
  [2] 记法禁则（组合上点、旧提法）
  [3] 构念名与操作化定义配对（因变量四类构念须在研究目标页齐备）
  [4] 研究问题编号成套（RQ1–RQ3）与研究目标编号成套（O1–O4）
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# ── 严格禁用：幻灯片正文与讲稿的研究问题／目标表述均不得出现 ──
STRICT = {
    r"什么时候": "改为「在何时刻」或直接命名构念（自发察觉时刻 t₀）",
    r"多快(?:做|完成)?": "改为「感知反应时 PRT 的分布特征」",
    r"孰优": "改为「优劣序为何」或「各水平间的差异如何」",
    r"更好还是更差": "改为「存在方向相反的结论」",
    r"有效还是无效": "改为「效应方向不一致」",
    r"是最优还是": "改为「最优取值的估计存在分歧」",
    r"到底": "删除",
    r"说白了": "删除",
    r"弄难": "改为「提高任务难度」",
    r"别的研究": "改为「既有研究」",
    r"动比不动好": "改为「动态编码优于静态编码」",
    r"越早越好(?!」)": "须加引号并标为朴素假设，如「提前量越大越有利」这一朴素假设",
    r"越多越好(?!」)": "须加引号并标为朴素假设",
    r"\u0307": "组合上点在多数字体缺字形；一律写 dθ/dt",
    # 自创缩写：无现成文献出处，一律不得使用
    r"\bT-SA\b": "无文献出处；用「情境意识·感知层」+ 操作化指标 t₀",
    r"\bP-T-E\b": "无文献出处；用「感知—决策—执行」或 SPIDER 阶段名",
    r"\bTLDP\b|\bDRM\b|\bFEN\b|\bCRT-L\b|\bDDW\b": "无文献出处；时间节点一律用 t₀ / t_warn / t_LPB / Δt",
    r"时间情境意识": "t₀ 为时刻量、SA 为构念，不可合称；见 §2.1.5b",
    r"基准时间节点": "BTN 是制动威胁数（无量纲运动学比值），非时间节点；见 §2.1.3",
    r"Baseline Time Node": "BTN = brake threat number（制动威胁数）",
    # 模糊效应表述：须给出方向与量
    r"(?<![无不])(?:有|无)效(?![性度果应载荷])(?=[。，、）]|$)": "改为具体效应描述（如「显著缩短制动反应时」「峰值减速度上升 34.46%」）",
}

# ── 仅幻灯片正文禁用（讲稿属口播文本，予以豁免）──
SLIDE_ONLY = {
    r"一句话": "幻灯片正文改为「概括而言」或「结论」",
    r"请注意": "幻灯片正文删除，改为直陈",
    r"请看": "幻灯片正文删除",
    r"我们(?!国)": "幻灯片正文改为「本研究」",
}

# ── 必须成对出现的构念名（研究目标页）──
DV_CONSTRUCTS = ["安全绩效", "认知负荷", "情境意识", "用户体验"]

DEFAULT = [
    "研究汇报_2026_08.html",
    "文献综述_幻灯片.html",
    "研究汇报_2026_08_讲稿.md",
    "文献综述_幻灯片_讲稿.md",
]


def in_scope(txt: str) -> bool:
    """[3][4] 仅适用于含研究目标页的汇报稿；专题综述稿予以豁免。"""
    return "研究目标" in txt


def check(path: Path) -> int:
    txt = path.read_text(encoding="utf-8")
    is_talk = path.suffix == ".md"
    bad = 0
    rules = dict(STRICT)
    if not is_talk:
        rules.update(SLIDE_ONLY)

    # 纠错语所在行视为正当的反面引用，予以豁免
    EXEMPT = ("禁则", "禁用", "不渲染", "缺字形", "应作", "不得写成",
              "改为", "朴素假设", "转述失真",
              "不可读作", "不得读作", "不改称", "一类构念名", "一类时间量",
              "直接改名", "非时间节点")
    hits = []
    for n, line in enumerate(txt.splitlines(), 1):
        if any(e in line for e in EXEMPT):
            continue
        for pat, why in rules.items():
            for m in re.finditer(pat, line):
                hits.append((n, m.group(0), why))
    if hits:
        bad += len(hits)
        print(f"  ✗ {path.name}　{len(hits)} 处")
        for n, g, why in hits[:12]:
            print(f"      L{n}  「{g}」　→ {why}")
        if len(hits) > 12:
            print(f"      …另 {len(hits) - 12} 处")
    else:
        print(f"  ✓ {path.name}")
    return bad


def main() -> int:
    args = sys.argv[1:] or DEFAULT
    files = [ROOT / a for a in args]
    bad = 0

    print("[1–2] 口语化句式与记法禁则")
    for f in files:
        if not f.exists():
            print(f"  ✗ 缺失 {f}")
            bad += 1
            continue
        bad += check(f)

    print("[3] 因变量四类构念齐备（研究目标页）")
    for f in files:
        if not f.exists():
            continue
        t = f.read_text(encoding="utf-8")
        if not in_scope(t):
            print(f"  － {f.name} 不适用（无研究目标页）")
            continue
        lack = [c for c in DV_CONSTRUCTS if c not in t]
        if lack:
            print(f"  ✗ {f.name} 缺构念 {lack}")
            bad += 1
        else:
            print(f"  ✓ {f.name} 四类构念齐备")

    print("[4] 编号成套")
    for f in files:
        if not f.exists():
            continue
        t = f.read_text(encoding="utf-8")
        if not in_scope(t):
            print(f"  － {f.name} 不适用（无研究目标页）")
            continue
        lack = [i for i in ("RQ1", "RQ2", "RQ3") if i not in t]
        lack += [i for i in ("O1", "O2", "O3", "O4") if i not in t]
        if lack:
            print(f"  ✗ {f.name} 缺编号 {lack}")
            bad += 1
        else:
            print(f"  ✓ {f.name} RQ1–RQ3 与 O1–O4 齐全")

    print("\n" + ("✓ 全部校验通过" if bad == 0 else f"✗ {bad} 处不通过"))
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
