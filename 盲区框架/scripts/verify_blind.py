#!/usr/bin/env python3
"""盲区框架交付物一致性校验器。

用法：
    python3 盲区框架/scripts/verify_blind.py

校验项：
  [1] 文件齐备
  [2] 关键数值跨文件一致（同一数字在各文件中不得写成不同值）
  [3] 术语与记法统一（禁用词、旧提法）
  [4] 相对路径引用可解析
  [5] 六条边界（BD-1..6）与六条预测（P1'..P6')、七项空白（BG1..7）编号齐全
  [6] 两套 deck 与讲稿对齐（转调 verify_deck_talk）
  [7] 两套 deck 零溢出报告存在且无溢出页
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BD = ROOT / "盲区框架"

LEDGER = BD / "盲区证据台账.md"
FRAME = BD / "双情境研究框架.md"
DECK = BD / "研究汇报_双情境框架.html"
TALK = BD / "研究汇报_双情境框架_讲稿.md"
REVIEW = BD / "thesis" / "盲区情境专题文献综述.md"
PROP = BD / "开题报告_双情境框架.html"
PTALK = BD / "开题报告_双情境框架_讲稿.md"
README = BD / "README.md"

FILES = [LEDGER, FRAME, DECK, TALK, REVIEW, PROP, PTALK, README]

# (deck, talk, 溢出报告) 三元组
PAIRS = [
    (DECK, TALK, "figures/blind_shots_overflow.json"),
    (PROP, PTALK, "figures/proposal_shots_overflow.json"),
]

# 关键数值：出现即必须与此处一致（正则 → 说明）
ANCHORS = {
    r"36\.29": "油门松开提前量（m）",
    r"39\.10": "首次制动提前量（m）",
    r"3\.45": "最大减速度绝对值降低（m/s²）",
    r"9\.41": "最小冲突距离增加（m）",
    r"1\.66": "遮挡场景最低时间预算（s）",
    r"6\.07": "交叉口遮挡视觉预警需求（s）",
    r"6\.28": "交叉口遮挡语音预警需求（s）",
    r"85\.02": "意图预测查准率（%）",
    r"84\.13": "意图预测查全率（%）",
    r"84\.57": "意图预测 F1（%）",
    r"66\.10": "老年驾驶员检出率基线（%）",
    r"91\.13": "老年驾驶员检出率提升后（%）",
    r"0\.72": "自主松油门基线（s）",
    r"13\.74": "工程可达骚扰报警占比（%）",
    r"617": "跟随目标锁定首次注视（ms）",
    r"2563": "屏幕固定首次注视（ms）",
    r"2730": "道路锁定首次注视（ms）",
}

# 禁用表述：键为正则，值为应改成的说明
FORBIDDEN = {
    r"形态四家族": "应作「四类图形形态」",
    r"红利": "应作「增益」",
    r"要决定的量": "应作「待确定的参数」",
    r"本研究的动作": "应作「本研究的处理」",
    r"闪烁可缓解无意视盲": "转述失真；原文为「动效对无意视盲无显著影响，仅闪烁缩短反应时」",
    r"θ̇": "组合上点在多数字体缺字形；HTML 用 dθ/dt，Markdown 用 \\dot{\\theta}",
}

# 必须成套出现的编号
SETS = {
    "边界 BD": ([f"BD-{i}" for i in range(1, 7)], [FRAME, DECK, REVIEW, PROP]),
    "预测 P′": ([f"P{i}′" for i in range(1, 7)], [FRAME, DECK, TALK, REVIEW, PROP, PTALK]),
    "空白 BG": ([f"BG{i}" for i in range(1, 8)], [REVIEW]),
    "假设 H′": ([f"H{i}′" for i in range(1, 6)], [FRAME, REVIEW]),
}


def main() -> int:
    bad = 0

    print("[1] 文件齐备")
    for f in FILES:
        ok = f.exists() and f.stat().st_size > 0
        print(f"  {'✓' if ok else '✗'} {f.relative_to(ROOT)}"
              f"{'' if ok else '  缺失或为空'}")
        if not ok:
            bad += 1
    if bad:
        print("\n✗ 文件缺失，后续校验中止")
        return 1

    text = {f: f.read_text(encoding="utf-8") for f in FILES}

    print("[2] 关键数值跨文件一致")
    miss = []
    for pat, desc in ANCHORS.items():
        hit = [f.name for f in FILES if re.search(pat, text[f])]
        if not hit:
            miss.append(f"{desc}（{pat}）未在任何文件中出现")
    if miss:
        for m in miss:
            print("  ⚠", m)
    print(f"  ✓ {len(ANCHORS) - len(miss)} / {len(ANCHORS)} 项锚点在交付物中可查")

    print("[3] 术语与记法统一")
    # 若该行同时含「转述失真」「已更正」「应作」等纠错语，视为正当的反面引用
    EXEMPT = ("转述失真", "已更正", "应作", "不得写成", "属误",
              "禁用", "禁则", "不渲染")
    hits = []
    for pat, why in FORBIDDEN.items():
        for f in FILES:
            n = 0
            for line in text[f].splitlines():
                if re.search(pat, line) and not any(e in line for e in EXEMPT):
                    n += len(re.findall(pat, line))
            if n:
                hits.append(f"{f.name} 出现 {n} 次「{pat}」——{why}")
    if hits:
        for h in hits:
            print("  ✗", h)
        bad += len(hits)
    else:
        print("  ✓ 无禁用表述")

    print("[4] 相对路径引用可解析")
    broken = []
    for f in FILES:
        for m in re.finditer(r"`((?:\.\./)+[^`]+\.(?:md|html|json|png))`", text[f]):
            tgt = (f.parent / m.group(1)).resolve()
            if not tgt.exists():
                broken.append(f"{f.name} → {m.group(1)}")
    if broken:
        for b in sorted(set(broken)):
            print("  ✗", b)
        bad += len(set(broken))
    else:
        print("  ✓ 全部可解析")

    print("[5] 编号成套")
    for name, (ids, files) in SETS.items():
        lack = []
        for i in ids:
            if not any(i in text[f] for f in files):
                lack.append(i)
        if lack:
            print(f"  ✗ {name} 缺 {lack}")
            bad += 1
        else:
            print(f"  ✓ {name} 齐全（{len(ids)} 条）")

    print("[6] deck 与讲稿对齐")
    for deck, talk, _ in PAIRS:
        print(f"  · {deck.name}")
        r = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "verify_deck_talk.py"),
             str(deck.relative_to(ROOT)), str(talk.relative_to(ROOT))],
            capture_output=True, text=True, cwd=ROOT)
        for line in r.stdout.strip().splitlines():
            if line.strip().startswith(("✓", "✗", "[")):
                print("     ", line.strip())
        if r.returncode != 0:
            bad += 1

    print("[7] deck 溢出报告")
    for deck, _, relrep in PAIRS:
        rep = ROOT / relrep
        if not rep.exists():
            print(f"  ⚠ 未找到 {relrep}；请先跑 shoot_slides.py")
            continue
        d = json.loads(rep.read_text(encoding="utf-8"))
        over = [x for x in d if max(x["scrollH"] - x["clientH"], x["overflowPx"]) > 2]
        thin = [x["idx"] for x in d
                if x["idx"] > 1 and x["clientH"]
                and x["scrollH"] / x["clientH"] < 0.88]
        n_deck = len(re.findall(r'<section class="slide', text[deck]))
        print(f"  {'✓' if not over else '✗'} {deck.name}：{len(d)} 页，溢出 {len(over)} 页"
              f"（deck 内 section 数 {n_deck}）")
        if over:
            bad += len(over)
            for x in over:
                print(f"    p{x['idx']:02d} +{max(x['scrollH'] - x['clientH'], x['overflowPx'])}px  {x['who']}")
        if len(d) != n_deck:
            print(f"    ✗ 报告页数与 deck section 数不符")
            bad += 1
        print(f"  {'✓' if not thin else '⚠'} {deck.name}：版心填充不足页：{thin or '无'}")

    print("\n" + ("✓ 全部校验通过" if bad == 0 else f"✗ {bad} 处不通过"))
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
