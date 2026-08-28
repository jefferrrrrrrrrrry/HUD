#!/usr/bin/env python3
"""第二轮审核用检查器：引注可追溯性、口播语速、备答覆盖。

用法：
    python3 scripts/audit_round2.py

检查项：
  [F] 引注可追溯：deck／讲稿中的「作者 等（年份）」是否能在文献综合表或 summaries 中查到
  [G] 配额可行性：各页「只说一句 ÷ 配额」≤ 320 字/分钟；并报告逐字稿与配额之比
  [H] 备答覆盖：讲述页是否有备答；★核心页必须有备答
  [I] 逐字稿单页字数上限 1300 字（超出者宜拆页；备查页豁免）
"""
from __future__ import annotations

import html as htmlmod
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DECK_TALK = [
    ("研究汇报_2026_08.html", "研究汇报_2026_08_讲稿.md"),
    ("文献综述_幻灯片.html", "文献综述_幻灯片_讲稿.md"),
    ("盲区框架/研究汇报_双情境框架.html", "盲区框架/研究汇报_双情境框架_讲稿.md"),
    ("盲区框架/开题报告_双情境框架.html", "盲区框架/开题报告_双情境框架_讲稿.md"),
    ("盲区框架/文献综述_盲区情境.html", "盲区框架/文献综述_盲区情境_讲稿.md"),
]

LIB = ["HUD_AR-HUD_行人预警_文献综合表.md", "ar-hud参考文献列表.md",
       "thesis/第2章_文献综述_v2.md", "盲区框架/盲区证据台账.md"]

CITE = re.compile(r"([A-Z][A-Za-z\u00C0-\u024F\-]{1,20}|[\u4e00-\u9fa5]{1,4})\s*"
                  r"(?:与|and|&)?\s*(?:等|等人)?\s*[（(](\d{4})[a-z]?[）)]")


def visible(s: str) -> str:
    return htmlmod.unescape(re.sub(r"<[^>]+>", " ", s))


def load_lib() -> str:
    buf = []
    for f in LIB:
        p = ROOT / f
        if p.exists():
            buf.append(p.read_text(encoding="utf-8"))
    for p in (ROOT / "summaries").glob("*.md"):
        buf.append(p.name)
    return "\n".join(buf)


def audit_cites(lib: str) -> int:
    print("[F] 引注可追溯")
    bad = 0
    for deck, talk in DECK_TALK:
        miss = {}
        for f in (deck, talk):
            p = ROOT / f
            txt = visible(p.read_text(encoding="utf-8")) if f.endswith("html") \
                else p.read_text(encoding="utf-8")
            for m in CITE.finditer(txt):
                name, yr = m.group(1), m.group(2)
                if name in ("WHO", "GB", "ISO", "SAE", "NHTSA", "IIHS", "Euro"):
                    continue
                if name in lib and yr in lib:
                    ctx = [i for i in range(len(lib)) if lib.startswith(name, i)]
                    ok = any(yr in lib[i:i + 220] for i in ctx[:80])
                    if ok:
                        continue
                miss[f"{name}（{yr}）"] = f
        if miss:
            print(f"  ⚠ {Path(deck).name}：{len(miss)} 处引注未在文献库直接匹配")
            for k in list(miss)[:8]:
                print(f"      {k}")
        else:
            print(f"  ✓ {Path(deck).name} 引注均可追溯")
    return bad


def talk_pages(talk: Path) -> list[tuple[str, str]]:
    parts = re.split(r"^## (p\d+)[　 ]", talk.read_text(encoding="utf-8"), flags=re.M)
    return [(parts[i], parts[i + 1]) for i in range(1, len(parts), 2)]


def audit_rate() -> int:
    """两轨制计时下的可行性检查：

    ⏱ 为讲述配额，逐字稿不用于全文朗读。故检查两项：
      ① 每页「只说一句」须能在配额内讲完（≤ 320 字/分）——硬性；
      ② 报告逐字稿总时长与配额之比——信息性，供决定是否拆页。
    """
    print("[G] 配额可行性（只说一句 ≤ 320 字/分为硬性；逐字倍率为信息项）")
    bad = 0
    for _, talk in DECK_TALK:
        p = ROOT / talk
        over, quota, verb = [], 0, 0
        for pid, body in talk_pages(p):
            m = re.search(r"\*\*⏱ (\d+):(\d{2})\*\*", body)
            sec = int(m.group(1)) * 60 + int(m.group(2)) if m else 0
            quota += sec
            if "不讲，备查" in body:
                continue
            seg = re.search(r"\*\*讲稿：\*\*(.*?)(?:\*\*只说一句|\*\*备答|$)", body, re.S)
            if seg:
                verb += len(re.sub(r"[\s*`>|#—－-]", "", seg.group(1)))
            one = re.search(r"\*\*只说一句：\*\*(.*?)(?:\n\n|\*\*备答)", body, re.S)
            if not one or not sec:
                continue
            n = len(re.sub(r"[\s*`>|#—－-]", "", one.group(1)))
            rate = n * 60 / sec
            if rate > 320:
                over.append(f"{pid} 只说一句 {n} 字 / {sec} 秒 = {rate:.0f} 字/分")
        ratio = (verb / 245) / (quota / 60) if quota else 0
        if over:
            print(f"  ✗ {p.name}：{len(over)} 页的压缩版讲不完")
            for o in over[:8]:
                print("      ", o)
            bad += len(over)
        else:
            print(f"  ✓ {p.name} 压缩版全页可行　逐字 {verb / 245:.0f} 分 / 配额 "
                  f"{quota // 60} 分 = {ratio:.1f}×")
    return bad


def audit_qa() -> int:
    print("[H] 备答覆盖")
    bad = 0
    for _, talk in DECK_TALK:
        p = ROOT / talk
        pages = talk_pages(p)
        no_qa, star_no_qa = [], []
        for pid, body in pages:
            if "不讲，备查" in body or pid == "p01":
                continue
            if "**备答：**" not in body:
                no_qa.append(pid)
                if "★" in body:
                    star_no_qa.append(pid)
        if star_no_qa:
            print(f"  ✗ {p.name} ★核心页缺备答：{star_no_qa}")
            bad += len(star_no_qa)
        cov = 1 - len(no_qa) / max(1, len(pages))
        print(f"  {'✓' if cov >= 0.5 else '⚠'} {p.name} 备答覆盖 {cov:.0%}"
              f"（缺 {len(no_qa)} 页）")
    return bad


def audit_len() -> int:
    print("[I] 逐字稿单页字数（上限 1300 字，超出者宜拆页；备查页豁免）")
    bad = 0
    for _, talk in DECK_TALK:
        p = ROOT / talk
        over = []
        for pid, body in talk_pages(p):
            if "不讲，备查" in body:
                continue
            seg = re.search(r"\*\*讲稿：\*\*(.*?)(?:\*\*只说一句|\*\*备答|$)", body, re.S)
            if not seg:
                continue
            n = len(re.sub(r"[\s*`>|#—－-]", "", seg.group(1)))
            if n > 1300:
                over.append(f"{pid} {n} 字")
        if over:
            print(f"  ⚠ {p.name}：{len(over)} 页超长")
            for o in over[:8]:
                print("      ", o)
        else:
            print(f"  ✓ {p.name} 全页不超长")
    return bad


def main() -> int:
    lib = load_lib()
    bad = audit_cites(lib) + audit_rate() + audit_qa() + audit_len()
    print("\n" + ("✓ 第二轮机检通过" if bad == 0 else f"✗ {bad} 处须修"))
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
