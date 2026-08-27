#!/usr/bin/env python3
"""第二阶段全库重编号：把首轮未覆盖的附属材料由旧编号（实验 0–4）改为现行编号（实验 1–5）。

用法：
    python3 scripts/renumber_phase2.py --dry     # 仅报告
    python3 scripts/renumber_phase2.py --apply   # 落盘（含 git mv 改名）

三种处理模式：
  WHOLE    ——全文件重编号。文件内「实验」后的数字整体上移一位（含 `实验N_描述.md`
            这类文件名字符串，故文件名引用随之自动更新）。
  LASTCOL  ——仅末列重编号。用于 `HUD_AR-HUD_行人预警_文献综合表.{md,csv,tsv}`：
            正文列描述的是**被综述论文自身的实验**（如 Gray 2014 的实验 1／实验 2），
            不得改写；只有末列「★所属实验」指本课题实验。
  TARGETED ——仅定向重编号。用于 `summaries/*.md`：其中「实验 N」多指原文自身的实验，
            只改写带本课题标记的「本课题实验 N」「对应实验 N」，另更新旧文件名引用。

不处理（并在报告中列出理由）：
  · 优化方案_…md、PPT_开题报告_大纲.md ——已声明保留旧编号／属更早的三实验方案；
  · 参考模板_…周颖2024.md、navigation_attention_ARHUD/** ——他人论文与另一课题；
  · weekly_reports*/**、REVIEW_REPORT.md 等 ——带日期的历史快照，重编号即改写记录；
  · scripts/fix_*_2026_08.py、build_pptx.py 等一次性历史脚本；
  · _bak_rename_terms/、_deprecated_summaries_dup/ ——备份目录。
"""
from __future__ import annotations

import csv
import io
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# ── 改名（须降序执行，避免与既有文件同名）
RENAME = [
    ("实验4_风险演化动态_文献与设计依据.md", "实验5_风险演化动态_文献与设计依据.md"),
    ("实验3_空间参照系与锁定策略_文献与设计依据.md", "实验4_空间参照系与锁定策略_文献与设计依据.md"),
    ("实验2_分层预警升级规则_文献与设计依据.md", "实验3_分层预警升级规则_文献与设计依据.md"),
    ("实验1_单层时间参数筛选_文献与设计依据.md", "实验2_单层时间参数筛选_文献与设计依据.md"),
    ("实验0_自发察觉基线标定_文献与设计依据.md", "实验1_自发察觉基线标定_文献与设计依据.md"),
]

WHOLE = [
    "README.md",
    "最终交付清单.md",
    "AR-HUD行人碰撞预警_毕业论文大纲与危险判定文献综述.md",
    "时间元素设计参数_专题分析.md",
    "空间元素设计参数_专题分析.md",
] + [new for _, new in RENAME] + [
    f"thesis/_parts/{n}" for n in (
        "add_2_1_7.md", "add_2_2_6.md", "add_2_2_8.md", "add_2_3_9.md", "add_2_4_10.md",
        "sec2_1.md", "sec2_2a.md", "sec2_2b.md", "sec2_3.md", "sec2_4.md", "sec2_5_6.md",
        "talk_p01_12.md", "talk_p13_34.md",
    )
]

LASTCOL_MD = "HUD_AR-HUD_行人预警_文献综合表.md"
LASTCOL_SEP = [("HUD_AR-HUD_行人预警_文献综合表.csv", ","),
               ("HUD_AR-HUD_行人预警_文献综合表.tsv", "\t")]

EXP = re.compile(r"(实验\s*)(\d(?:\s*[–\-—、，,/／和与至到及]\s*\d)*)")
TARGET = re.compile(r"((?:本课题实验|对应实验)\s*)(\d(?:\s*[–\-—、，,/／和与至到及]\s*\d)*)")
DIGIT = re.compile(r"\d")


def bump(m: re.Match) -> str:
    return m.group(1) + DIGIT.sub(lambda d: str(int(d.group(0)) + 1), m.group(2))


def bump_filenames(s: str) -> tuple[str, int]:
    """更新旧文件名引用（降序，避免连环撞名）。"""
    n = 0
    for old, new in RENAME:
        stem_old, stem_new = old[:-3], new[:-3]
        n += s.count(stem_old)
        s = s.replace(stem_old, stem_new)
    return s, n


def main() -> int:
    apply = (sys.argv[1] if len(sys.argv) > 1 else "--dry") == "--apply"
    tot = 0

    print("── [1] 改名（git mv）")
    for old, new in RENAME:
        p = ROOT / old
        if not p.exists():
            print(f"  · 跳过（已改名或缺失）{old}")
            continue
        print(f"  {'✓' if apply else '·'} {old}  →  {new}")
        if apply:
            subprocess.run(["git", "mv", old, new], cwd=ROOT, check=True)

    print("\n── [2] WHOLE：全文件重编号")
    for rel in WHOLE:
        p = ROOT / rel
        if not p.exists():
            print(f"  ✗ 缺失 {rel}")
            continue
        s = p.read_text(encoding="utf-8")
        s2, n = EXP.subn(bump, s)
        tot += n
        print(f"  {'✓' if apply else '·'} {rel:52s} 实验号 {n:4d}")
        if apply and s2 != s:
            p.write_text(s2, encoding="utf-8")

    print("\n── [3] LASTCOL：仅末列「★所属实验」重编号")
    p = ROOT / LASTCOL_MD
    out, n = [], 0
    for ln in p.read_text(encoding="utf-8").splitlines(keepends=True):
        if "|" in ln and EXP.search(ln):
            cells = ln.split("|")
            # 末列＝倒数第二个片段（行尾以 | 结束）
            idx = len(cells) - 2
            cells[idx], k = EXP.subn(bump, cells[idx])
            n += k
            ln = "|".join(cells)
        out.append(ln)
    tot += n
    print(f"  {'✓' if apply else '·'} {LASTCOL_MD:52s} 实验号 {n:4d}（正文列未动）")
    if apply:
        p.write_text("".join(out), encoding="utf-8")

    for rel, sep in LASTCOL_SEP:
        p = ROOT / rel
        with p.open(newline="", encoding="utf-8") as fh:
            rows = list(csv.reader(fh, delimiter=sep))
        n = 0
        for r in rows[1:]:
            if r:
                r[-1], k = EXP.subn(bump, r[-1])
                n += k
        tot += n
        print(f"  {'✓' if apply else '·'} {rel:52s} 实验号 {n:4d}（末列 ★所属实验）")
        if apply:
            buf = io.StringIO()
            csv.writer(buf, delimiter=sep, lineterminator="\n").writerows(rows)
            p.write_text(buf.getvalue(), encoding="utf-8")

    print("\n── [4] TARGETED：summaries 仅改「本课题实验 N」「对应实验 N」与文件名引用")
    n_mark = n_file = n_files = 0
    for p in sorted((ROOT / "summaries").glob("*.md")):
        s = p.read_text(encoding="utf-8")
        s2, a = TARGET.subn(bump, s)
        s2, b = bump_filenames(s2)
        if a or b:
            n_mark += a
            n_file += b
            n_files += 1
            if apply:
                p.write_text(s2, encoding="utf-8")
    tot += n_mark
    print(f"  {'✓' if apply else '·'} summaries/*.md　涉及 {n_files} 份：本课题标记 {n_mark} 处、文件名引用 {n_file} 处")

    print(f"\n合计实验号改写 {tot} 处{'（已落盘）' if apply else '（未落盘，加 --apply 执行）'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
