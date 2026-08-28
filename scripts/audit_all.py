#!/usr/bin/env python3
"""交付物全量审计：跨文档术语、数值、编号与页面结构的一致性扫描。

用法：
    python3 scripts/audit_all.py            # 全量
    python3 scripts/audit_all.py <file>...  # 指定文件

审计项：
  [A] 旧术语与记法残留
  [B] deck 页面结构：标题唯一、tag 齐备、页码连续
  [C] deck 与讲稿的数值一致性（deck 内数值须在讲稿可查）
  [D] 关键数值跨文档一致（同一量不得写成不同值）
  [E] 编号成套（RQ／O／G／H／P′／BD／BG）
"""
from __future__ import annotations

import html as htmlmod
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DECK_TALK = [
    ("研究汇报_2026_08.html", "研究汇报_2026_08_讲稿.md"),
    ("文献综述_幻灯片.html", "文献综述_幻灯片_讲稿.md"),
    ("盲区框架/研究汇报_双情境框架.html", "盲区框架/研究汇报_双情境框架_讲稿.md"),
    ("盲区框架/开题报告_双情境框架.html", "盲区框架/开题报告_双情境框架_讲稿.md"),
    ("盲区框架/文献综述_盲区情境.html", "盲区框架/文献综述_盲区情境_讲稿.md"),
]

DOCS = [
    "AR-HUD行人碰撞预警_毕业论文研究框架.md",
    "thesis/第1章_研究背景及意义.md",
    "thesis/第2章_文献综述_v2.md",
    "thesis/第3章_研究内容与预期目标.md",
    "盲区框架/双情境研究框架.md",
    "盲区框架/盲区证据台账.md",
    "盲区框架/thesis/第1章_研究背景及意义.md",
    "盲区框架/thesis/第3章_研究内容与预期目标.md",
    "盲区框架/thesis/盲区情境专题文献综述.md",
    "盲区框架/实验1_双情境零点同批标定_文献与设计依据.md",
    "盲区框架/实验4_盲区时间参数与可靠性_文献与设计依据.md",
    "盲区框架/实验5_盲区锚定策略与遮挡几何_文献与设计依据.md",
]

# [A] 旧术语与记法：正则 → 应改为
LEGACY = {
    r"风险加工(?!链|过程)": "题目与构念一律用「情境意识」",
    r"\bT-SA\b": "无文献出处；用「情境意识·感知层」+ 指标 t₀",
    r"基准时间节点": "BTN 为制动威胁数（无量纲比值），非时间节点",
    r"\u0307": "组合上点缺字形；一律写 dθ/dt",
    r"形态四家族": "应作「四类图形形态」",
    r"红利": "应作「增益」",
    r"闪烁可缓解无意视盲": "转述失真；原文为动效无显著影响、仅闪烁缩短反应时",
    r"(?<![无不])(?:有|无)效(?![性度果应载荷])(?=[。，、）]|$)": "须给出效应方向与量",
}
EXEMPT_LINE = ("禁则", "禁用", "应作", "不得写成", "转述失真", "已更正", "缺字形",
               "改为", "不渲染", "非时间节点", "属误", "口径", "朴素假设",
               "不可读作", "不得读作", "而非「", "无对应测量构念", "不可合称")

# [D] 关键数值：描述 → (正则, 期望字面)
ANCHORS = {
    "油门松开提前量": r"36\.29",
    "首次制动提前量": r"39\.10",
    "峰值减速度降幅": r"3\.45",
    "最小冲突距离增加": r"9\.41",
    "遮挡场景最低时间预算": r"1\.66",
    "交叉口遮挡视觉需求": r"6\.07",
    "跟随目标锁定首次注视": r"617",
    "屏幕固定首次注视": r"2563",
    "道路锁定首次注视": r"2730",
    "自主松油门基线": r"0\.72",
    "工程可达骚扰占比": r"13\.74",
    "峰值减速度上升": r"34\.46",
    "共形箭头注视时长": r"3\.33",
}
# 与锚点配对的错值（出现即为不一致）
WRONG = {
    r"36\.2(?!9)": "36.29",
    r"39\.1(?![0-9])": "39.10",
    r"2000\s*ms 分心": None,
}


def text_of(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def visible(sec: str) -> str:
    t = re.sub(r"<[^>]+>", "", sec)
    return htmlmod.unescape(t)


def audit_legacy(files: list[Path]) -> int:
    print("[A] 旧术语与记法残留")
    bad = 0
    for f in files:
        hits = []
        for n, line in enumerate(text_of(f).splitlines(), 1):
            if any(e in line for e in EXEMPT_LINE):
                continue
            for pat, why in LEGACY.items():
                for m in re.finditer(pat, line):
                    hits.append((n, m.group(0), why))
        if hits:
            bad += len(hits)
            print(f"  ✗ {f.name}　{len(hits)} 处")
            for n, g, why in hits[:6]:
                print(f"      L{n} 「{g}」→ {why}")
    if not bad:
        print("  ✓ 无残留")
    return bad


def audit_deck(deck: Path) -> int:
    s = text_of(deck)
    secs = re.findall(r'<section class="slide.*?</section>', s, re.S)
    bad = 0
    tits, tags, pgs = [], 0, []
    for sec in secs:
        m = re.search(r"<em>(.*?)</em>", sec, re.S)
        tits.append(re.sub(r"\s+", " ", visible(m.group(1))).strip() if m else "封面")
        if 'class="tag"' in sec:
            tags += 1
        mp = re.search(r'class="pg">\s*(\d+)\s*/\s*(\d+)', sec)
        if mp:
            pgs.append((int(mp.group(1)), int(mp.group(2))))
    dup = [t for t, c in Counter(tits).items() if c > 1 and t != "封面"]
    if dup:
        print(f"  ✗ {deck.name} 标题重复：{dup}")
        bad += len(dup)
    if tags < len(secs) - 1:
        print(f"  ⚠ {deck.name} tag 覆盖 {tags}/{len(secs) - 1} 讲述页")
    seq = [a for a, _ in pgs]
    if seq and seq != list(range(seq[0], seq[0] + len(seq))):
        print(f"  ✗ {deck.name} 页码不连续：{seq}")
        bad += 1
    tot = {b for _, b in pgs}
    if len(tot) > 1 or (tot and tot != {len(secs)}):
        print(f"  ✗ {deck.name} 页码分母 {tot}，section 数 {len(secs)}")
        bad += 1
    if not bad:
        print(f"  ✓ {deck.name}　{len(secs)} 页　标题唯一、页码连续")
    return bad


THIN = r"[\u2009\u202f\u00a0 ]"


def denum(t: str) -> str:
    """去掉数字之间的窄空格千分位，使 3 700 与 3700 可比。"""
    return re.sub(rf"(?<=\d){THIN}(?=\d)", "", t)


def audit_numbers(deck: Path, talk: Path) -> int:
    """deck 中出现的三位以上数值，应在讲稿中可查（否则口播与投影不一致）。"""
    ds = denum(text_of(deck))
    ts = denum(text_of(talk))
    secs = re.findall(r'<section class="slide.*?</section>', ds, re.S)
    lost = defaultdict(list)
    for i, sec in enumerate(secs, 1):
        vis = denum(visible(sec))
        for m in re.finditer(r"(?<![.\d])\d+\.\d{2}(?!\d)|(?<![.\d])\d{3,}(?!\d)", vis):
            v = m.group(0)
            if v in ("2026", "2025", "2024", "2023", "2022", "2021", "2020",
                     "2019", "2018", "2017", "2016", "2015", "2014", "2013",
                     "2012", "2010", "2009", "2007", "2006", "1995", "1976",
                     "1972", "1936"):
                continue
            if v not in ts:
                lost[i].append(v)
    if lost:
        n = sum(len(v) for v in lost.values())
        print(f"  ⚠ {deck.name} 有 {n} 个数值未在讲稿出现（{len(lost)} 页）")
        for i in sorted(lost)[:6]:
            print(f"      p{i:02d}: {sorted(set(lost[i]))[:8]}")
        return 0
    print(f"  ✓ {deck.name} deck 数值均可在讲稿查到")
    return 0


def audit_anchors(files: list[Path]) -> int:
    print("[D] 关键数值跨文档一致")
    bad = 0
    for desc, pat in ANCHORS.items():
        hit = [f.name for f in files if re.search(pat, text_of(f))]
        if not hit:
            print(f"  ⚠ {desc}（{pat}）未在任何交付物出现")
    for pat, right in WRONG.items():
        if right is None:
            continue
        for f in files:
            for n, line in enumerate(text_of(f).splitlines(), 1):
                if re.search(pat, line):
                    print(f"  ✗ {f.name} L{n} 出现疑似错值（应为 {right}）")
                    bad += 1
    if not bad:
        print("  ✓ 未见错值")
    return bad


def audit_sets(files: list[Path]) -> int:
    print("[E] 编号成套")
    txt = {f: text_of(f) for f in files}
    groups = {
        "RQ1–RQ3": [f"RQ{i}" for i in (1, 2, 3)],
        "O1–O4": [f"O{i}" for i in (1, 2, 3, 4)],
        "P1′–P6′": [f"P{i}′" for i in range(1, 7)],
        "BD-1–BD-6": [f"BD-{i}" for i in range(1, 7)],
        "BG1–BG7": [f"BG{i}" for i in range(1, 8)],
        "H1′–H5′": [f"H{i}′" for i in range(1, 6)],
    }
    bad = 0
    for name, ids in groups.items():
        lack = [i for i in ids if not any(i in t for t in txt.values())]
        if lack:
            print(f"  ✗ {name} 缺 {lack}")
            bad += 1
        else:
            print(f"  ✓ {name} 齐全")
    return bad


def main() -> int:
    args = sys.argv[1:]
    decks = [(ROOT / a, ROOT / b) for a, b in DECK_TALK]
    docs = [ROOT / d for d in DOCS if (ROOT / d).exists()]
    allf = [x for pair in decks for x in pair] + docs
    if args:
        allf = [ROOT / a for a in args]
    bad = audit_legacy(allf)

    print("[B] deck 页面结构")
    for d, _ in decks:
        bad += audit_deck(d)

    print("[C] deck 与讲稿数值一致")
    for d, t in decks:
        bad += audit_numbers(d, t)

    bad += audit_anchors(allf)
    bad += audit_sets(allf)
    print("\n" + ("✓ 审计通过" if bad == 0 else f"✗ {bad} 处待修"))
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
