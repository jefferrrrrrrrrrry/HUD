#!/usr/bin/env python3
"""把新增小节插入第 2 章的分节文件，并顺延受影响的小节编号。

只改 thesis/_parts/ 下的分节文件，随后由 build_chapter2.py 重新拼接。
幂等：若目标文件中已存在插入锚点标记，则跳过。
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "thesis" / "_parts"

# (目标文件, 插入内容文件, 插入位置锚点, 该文件内需重编号的替换对)
JOBS = [
    (
        "sec2_1.md", "add_2_1_7.md", "### 2.1.7 §2.1 小结",
        [("### 2.1.7 §2.1 小结", "### 2.1.8 §2.1 小结")],
    ),
    (
        "sec2_2b.md", "add_2_2_6.md", "### 2.2.7 驾驶员反应时的分解与运动学下界",
        [],
    ),
    (
        "sec2_2b.md", "add_2_2_8.md", "### 2.2.8 §2.2 小结",
        [("### 2.2.8 §2.2 小结", "### 2.2.9 §2.2 小结")],
    ),
    (
        "sec2_3.md", "add_2_3_9.md", "### 2.3.9 无意视盲与注意隧道：AR-HUD 的副作用侧",
        [
            ("### 2.3.9 无意视盲与注意隧道：AR-HUD 的副作用侧",
             "### 2.3.10 无意视盲与注意隧道：AR-HUD 的副作用侧"),
            ("### 2.3.10 眼动指标的判定门槛：从单调假设到区间判定",
             "### 2.3.11 眼动指标的判定门槛：从单调假设到区间判定"),
            ("### 2.3.11 §2.3 小结", "### 2.3.12 §2.3 小结"),
        ],
    ),
    (
        "sec2_4.md", "add_2_4_10.md", "### 2.4.10 §2.4 小结：冲突如何转化为设计",
        [("### 2.4.10 §2.4 小结：冲突如何转化为设计",
          "### 2.4.11 §2.4 小结：冲突如何转化为设计")],
    ),
]

# 跨文件的交叉引用同步（章内引用了被重编号的小节）
XREFS = [
    ("sec2_3.md", "§2.3.10 的区间判定", "§2.3.11 的区间判定"),
    ("sec2_1.md", "§2.1.5 第 5 条", "§2.1.5 第 5 条"),
]


def main() -> None:
    for target, addfile, anchor, renumbers in JOBS:
        t = P / target
        s = t.read_text(encoding="utf-8")
        add = (P / addfile).read_text(encoding="utf-8")
        tag = f"<!-- inserted:{addfile} -->"
        if tag in s:
            print(f"SKIP {target} <- {addfile}（已插入）")
            continue
        # 先重编号（避免锚点被改掉后找不到）
        assert anchor in s, f"{target} 中找不到锚点：{anchor}"
        i = s.index(anchor)
        head, tail = s[:i], s[i:]
        for old, new in renumbers:
            assert old in tail, f"{target} 中找不到待重编号标题：{old}"
            tail = tail.replace(old, new, 1)
        s = head + tag + "\n" + add.rstrip() + "\n\n" + tail
        t.write_text(s, encoding="utf-8")
        print(f"OK   {target} <- {addfile}（插入 {len(add):,} 字符，重编号 {len(renumbers)} 处）")

    for target, old, new in XREFS:
        if old == new:
            continue
        t = P / target
        s = t.read_text(encoding="utf-8")
        if old in s:
            t.write_text(s.replace(old, new), encoding="utf-8")
            print(f"XREF {target}: {old} -> {new}")


if __name__ == "__main__":
    main()
