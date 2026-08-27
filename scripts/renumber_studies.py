#!/usr/bin/env python3
"""全库实验与研究编号重编：实验 0–4 → 1–5；主线 研究零/一/二 → 研究一/二/三。

用法：
    python3 scripts/renumber_studies.py --dry     # 仅报告
    python3 scripts/renumber_studies.py --apply   # 落盘

规则：
  1) 「实验」后紧跟的数字表达式（含 0-4 及其区间／枚举写法）整体上移一位。
     覆盖 实验 0 / 实验0 / 实验 1–4 / 实验 0／1／2 / 实验 1、2 / 实验 2 至 4 等。
  2) 主线文件：研究零→研究一，研究一→研究二，研究二→研究三（降序替换）。
     盲区框架文件**不做研究号平移**——其「研究一＝非盲区、研究二＝盲区」为情境标签而非序号。
  3) 「五个实验」「五实验」等总数表述不变（总数仍为 5）。
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MAIN = [
    "研究汇报_2026_08.html",
    "研究汇报_2026_08_讲稿.md",
    "文献综述_幻灯片.html",
    "文献综述_幻灯片_讲稿.md",
    "thesis/第2章_文献综述_v2.md",
    "AR-HUD行人碰撞预警_毕业论文研究框架.md",
    "scripts/plot_research_framework_3col.py",
]
BLIND = [
    "盲区框架/README.md",
    "盲区框架/双情境研究框架.md",
    "盲区框架/盲区证据台账.md",
    "盲区框架/研究汇报_双情境框架.html",
    "盲区框架/研究汇报_双情境框架_讲稿.md",
    "盲区框架/开题报告_双情境框架.html",
    "盲区框架/开题报告_双情境框架_讲稿.md",
    "盲区框架/thesis/盲区情境专题文献综述.md",
]

# 「实验」+ 数字表达式（数字之间可夹分隔符）
EXP = re.compile(r"(实验\s*)(\d(?:\s*[–\-—、，,/／和与至到及]\s*\d)*)")
DIGIT = re.compile(r"\d")


def bump(m: re.Match) -> str:
    head, body = m.group(1), m.group(2)
    return head + DIGIT.sub(lambda d: str(int(d.group(0)) + 1), body)


def process(path: Path, shift_study: bool) -> tuple[str, int, int]:
    s = path.read_text(encoding="utf-8")
    s2, n_exp = EXP.subn(bump, s)
    n_std = 0
    if shift_study:
        for a, b in (("二", "\u3007三"), ("一", "\u3007二"), ("零", "\u3007一")):
            # 负向断言排除「研究一律／一致／一般／一样」等非序号用法
            pat = re.compile("研究" + a + r"(?![律致般样些直贯])")
            s2, k = pat.subn("研究" + b, s2)
            n_std += k
        s2 = s2.replace("研究\u3007", "研究")
    return s2, n_exp, n_std


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "--dry"
    apply = mode == "--apply"
    total_e = total_s = 0
    for rel, shift in [(f, True) for f in MAIN] + [(f, False) for f in BLIND]:
        p = ROOT / rel
        if not p.exists():
            print(f"  ✗ 缺失 {rel}")
            continue
        new, ne, ns = process(p, shift)
        total_e += ne
        total_s += ns
        tag = "研究号平移" if shift else "仅实验号"
        print(f"  {'✓' if apply else '·'} {rel:44s} 实验 {ne:3d}  研究 {ns:3d}  [{tag}]")
        if apply and new != p.read_text(encoding="utf-8"):
            p.write_text(new, encoding="utf-8")
    print(f"\n合计：实验号 {total_e} 处，研究号 {total_s} 处"
          f"{'（已落盘）' if apply else '（未落盘，加 --apply 执行）'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
