#!/usr/bin/env python3
"""拼接讲稿分节文件为《文献综述_幻灯片_讲稿.md》，并校验与幻灯片逐页对齐。

校验项
  1. 讲稿的 p 编号必须 1..N 连续，且 N == 幻灯片 <section> 数
  2. 每页标题须与幻灯片该页 <h1> 的文本一致（去标签、去空白后包含关系）
  3. ⏱ 用时之和须等于声称的总时长
  4. 三档预案里点到的页号必须都存在
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTS = ROOT / "thesis" / "_parts"
HTML = ROOT / "文献综述_幻灯片.html"
OUT = ROOT / "文献综述_幻灯片_讲稿.md"
SRC = ["talk_p01_12.md", "talk_p13_34.md"]


def slide_titles() -> list[str]:
    s = HTML.read_text("utf-8")
    out = []
    for blk in re.findall(r"<section\b.*?</section>", s, re.S):
        m = re.search(r"<h1[^>]*>(.*?)</h1>", blk, re.S)
        t = re.sub(r"<[^>]+>", " ", m.group(1)) if m else "封面"
        out.append(re.sub(r"\s+", "", t))
    return out


def main() -> None:
    text = "\n".join((PARTS / f).read_text("utf-8").rstrip() for f in SRC) + "\n"
    OUT.write_text(text, encoding="utf-8")

    titles = slide_titles()
    heads = re.findall(r"^## p(\d+)　(.+)$", text, re.M)
    nums = [int(a) for a, _ in heads]

    assert nums == list(range(1, len(titles) + 1)), \
        f"页号不连续或数量不符：讲稿 {len(nums)} 页（{nums[:5]}…），幻灯片 {len(titles)} 页"

    # 标题对齐：取讲稿标题「：」后的核心词，须出现在幻灯片标题中。
    # 幻灯片标题含面包屑前缀（「文献综述」）与末尾章节号，故用包含关系而非相等。
    bad = []
    for (n, ht), st in zip(heads, titles):
        core = re.sub(r"[（(].*", "", ht).split("：")[-1]
        core = re.sub(r"[\s　]", "", core)[:6]
        if core and core not in st and "封面" not in ht:
            bad.append(f"p{n}: 讲稿「{ht}」 vs 幻灯片「{st}」")
    assert not bad, "标题不对齐：\n  " + "\n  ".join(bad)
    print(f"标题对齐 {len(heads)}/{len(titles)} 页 ✓")

    # 用时合计与三档预案
    per = {}
    for m in re.finditer(r"^## p(\d+)　.*?$(.*?)(?=^## |\Z)", text, re.M | re.S):
        t = re.search(r"\*\*⏱ (\d+):(\d\d)\*\*", m.group(2))
        per[int(m.group(1))] = int(t.group(1)) * 60 + int(t.group(2)) if t else 0
    assert len(per) == len(nums), f"有页缺 ⏱ 标记：{set(nums) - set(per)}"

    def fmt(sec: int) -> str:
        return f"{sec // 60} 分 {sec % 60:02d} 秒"

    SKIP = {3, 7, 12, 19, 20, 21, 27, 32}
    KEEP = [2, 6, 9, 11, 13, 14, 18, 23, 28, 29, 31, 33]
    full = sum(per.values())
    std = sum(v for k, v in per.items() if k not in SKIP)
    lite = sum(per[k] for k in KEEP)
    print(f"完整 {len(per)} 页 {fmt(full)}｜标准 {len(per) - len(SKIP)} 页 {fmt(std)}"
          f"｜精简 {len(KEEP)} 页 {fmt(lite)}")

    # 正文中声明的合计必须与实测一致，防止手改用时后说明失同步
    for label, sec in (("完整 34 页", full), ("标准档 26 页", std),
                       ("精简档 12 页", lite)):
        want = f"**{sec // 60}:{sec % 60:02d}**"
        assert want in text, f"附录 B 中「{label}」的合计与实测不符，应为 {want}"
    print("附录 B 合计与实测一致 ✓")

    # 每页四块齐全（p34 不作口播，无「只说一句」）
    miss = []
    for m in re.finditer(r"^## p(\d+)　.*?$(.*?)(?=^## |\Z)", text, re.M | re.S):
        n, body = int(m.group(1)), m.group(2)
        need = ["**⏱", "**讲稿：**", "**备答：**"]
        if n not in (34,):
            need.append("**只说一句：**")
        miss += [f"p{n} 缺 {b}" for b in need if b not in body]
    assert not miss, "分块缺失：" + "；".join(miss)
    stars = sorted(int(x) for x in re.findall(r"\| p(\d+) ★", text))
    assert f"★ 标记的 {len(stars)} 页" in text, \
        f"使用说明里的核心页数与附录 B 不符，附录 B 有 {len(stars)} 页"
    print(f"每页分块齐全 ✓　核心页 {len(stars)} 页与说明一致 ✓")

    # 预案页号存在性
    for m in re.finditer(r"跳过 ([p0-9、\u3001]+)", text):
        for p in re.findall(r"p(\d+)", m.group(1)):
            assert int(p) in nums, f"预案引用了不存在的页 p{p}"

    chars = len(re.findall(r"[\u4e00-\u9fff]", text))
    body = re.sub(r"\*\*只说一句：\*\*.*?(?=\n\*\*|\n---|\Z)", "", text, flags=re.S)
    body = re.sub(r"\*\*备答：\*\*.*?(?=\n---|\Z)", "", body, flags=re.S)
    spoken = len(re.findall(r"[\u4e00-\u9fff]", body))
    print(f"讲稿全文 {chars:,} 汉字（其中口播部分约 {spoken:,} 字）-> {OUT.name}")


if __name__ == "__main__":
    main()
