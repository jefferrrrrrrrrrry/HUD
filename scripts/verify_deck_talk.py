#!/usr/bin/env python3
"""通用校验器：任意幻灯片 HTML 与其配套 md 讲稿的逐页对齐。

用法：
    python3 scripts/verify_deck_talk.py <deck.html> <talk.md>

校验项：
  [1] 页数一致
  [2] 逐页标题一致（deck 取 h1.crumb 内 <em> 文本；封面页取「封面」）
  [3] 每页三块齐全：讲稿 / 只说一句 /（封面页豁免「只说一句」）
  [4] 计时标记齐全，并汇总总时长
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def deck_titles(html: str) -> list[str]:
    secs = re.findall(r'<section class="slide.*?</section>', html, re.S)
    out = []
    for s in secs:
        m = re.search(r'<h1 class="crumb">.*?<em>(.*?)</em>', s, re.S)
        if m:
            t = re.sub(r"<[^>]+>", "", m.group(1))
        else:
            t = "封面"
        out.append(re.sub(r"\s+", " ", t).strip())
    return out


def talk_pages(md: str) -> list[tuple[str, str]]:
    """返回 [(标题, 正文)]，按 '## pNN　标题' 切分。"""
    parts = re.split(r"^## p(\d+)[　 ]*(.*)$", md, flags=re.M)
    out = []
    for i in range(1, len(parts), 3):
        out.append((re.sub(r"\s+", " ", parts[i + 1]).strip(), parts[i + 2]))
    return out


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    deck = ROOT / sys.argv[1]
    talk = ROOT / sys.argv[2]
    dt = deck_titles(deck.read_text(encoding="utf-8"))
    tp = talk_pages(talk.read_text(encoding="utf-8"))
    bad = 0

    print(f"[1] 页数　deck {len(dt)} 页　讲稿 {len(tp)} 页", end="　")
    if len(dt) != len(tp):
        print("✗ 不一致")
        bad += 1
    else:
        print("✓")

    print("[2] 逐页标题")
    for i, (d, (t, _)) in enumerate(zip(dt, tp), 1):
        if d != t:
            print(f"  ✗ p{i:02d}  deck「{d}」　讲稿「{t}」")
            bad += 1
    if not bad:
        print(f"  ✓ {min(len(dt), len(tp))} 页标题逐字一致")

    print("[3] 每页分块")
    miss = []
    for i, (t, body) in enumerate(tp, 1):
        need = ["**讲稿：**"] if i == 1 else ["**讲稿：**", "**只说一句：**"]
        lack = [k for k in need if k not in body]
        if lack:
            miss.append(f"p{i:02d} 缺 {lack}")
    if miss:
        for m in miss:
            print("  ✗", m)
        bad += len(miss)
    else:
        print("  ✓ 分块齐全")

    print("[4] 计时")
    tot = 0
    notime = []
    for i, (t, body) in enumerate(tp, 1):
        m = re.search(r"\*\*⏱ (\d+):(\d{2})\*\*", body)
        if not m:
            notime.append(i)
            continue
        tot += int(m.group(1)) * 60 + int(m.group(2))
    if notime:
        print("  ✗ 缺计时页：", notime)
        bad += 1
    else:
        print(f"  ✓ 全部 {len(tp)} 页有计时；合计 {tot // 60} 分 {tot % 60} 秒")

    print("\n" + ("✓ 全部校验通过" if bad == 0 else f"✗ {bad} 处不通过"))
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
