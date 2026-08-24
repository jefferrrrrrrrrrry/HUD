#!/usr/bin/env python3
"""用 scripts/apa_refs.json 重建《研究框架》§15.2 的本库文献表。

问题
  §15.2 原有 42 条中，**19 条的作者列表是占位值**，从未经 Crossref 核验。例如：
    Cangut, B., & Alver, Y.        实为 Cangut, S. H., & Alver, Y.
    Kang, N., Sakamoto, K., & Kubo, N.   实为 Kang, H., Han, K., & Lee, J.
    Li, Y., Wang, C., & Zhang, H.  实为 Li, J., Wang, C., & Chen, M.
    Shen, Y., Zhang, L., & Chen, K.      实为 Shen, C., Qin, H., Li, S., …
    Suzuki, K., Nakano, K., & Yamada, K. 实为 Suzuki, S., Raksincharoensak, P., …
    Wei, L., Chen, X., & Sun, Y.   实为 Wei, C., Jin, Y., Fu, Y., …
    Zhu, Y., Wang, T., & Li, M.   实为 Zhu, Q., Li, J., & Liu, Y.
  另有 3 条缺同作者同年后缀（#7/#40 → 2024a/b，#52 → 2025a）。

  逐条手改风险高且不可复现，故改为**从权威源整表重建**：apa_refs.json 的 102 条
  已全部经 Crossref API 核验 DOI、年份、卷期页码与作者。

  §15.1（理论与方法学文献，如 Lee 1976、Posner 1980、Wickens 2002）不在本库
  102 篇内，不由本脚本管理，保持原样。

被本框架实际引用的条目才列入，避免把 §15.2 变成整库清单；引用检测方式为在
文档 §1–§14 正文中搜索该条的 in-text 形式。
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "AR-HUD行人碰撞预警_毕业论文研究框架.md"
REFS = ROOT / "scripts" / "apa_refs.json"

HEAD = "### 15.2 本库文献（按第一作者姓氏字母序）"
NOTE = (
    "> 本表由 `scripts/rebuild_framework_refs.py` 从 `scripts/apa_refs.json` 自动生成，"
    "**请勿手改**；如需修订请改权威源后重跑该脚本。\n"
    "> 全部条目已经 Crossref API 核验 DOI、年份、卷期页码与作者列表。"
    "同作者同年者加 a/b 后缀。完整 102 条见"
    "《HUD_AR-HUD_行人预警_文献综合表.csv》的「★APA条目」列。\n"
)


def intext_keys(e: dict) -> list[str]:
    """生成该条目在正文中可能的引注写法，用于判断是否被引用。"""
    m = re.match(r"^(.+?) \(", e["apa"])
    first = m.group(1).split(",")[0].strip().lstrip("*") if m else ""
    yr = re.search(r"\((\d{4})[a-z]?\)", e["apa"])
    y = yr.group(1) if yr else ""
    out = [e["intext"], e["intext"].strip("()")]
    if first and y:
        out += [f"{first} et al. ({y}", f"{first} et al., {y}",
                f"{first} ({y}", f"{first}, {y}",
                f"{first}等（{y}", f"{first} 等（{y}"]
    return [x for x in out if x]


def main() -> None:
    s = DOC.read_text("utf-8")
    apa = json.loads(REFS.read_text("utf-8"))

    i = s.index(HEAD)
    j = s.find("\n## ", i)
    tail = s[j:] if j > 0 else ""
    body = s[:i]                      # §1–§15.1，用于检测引用

    used, unused = [], []
    for k, e in apa.items():
        if any(t in body for t in intext_keys(e)):
            used.append((k, e))
        else:
            unused.append(k)

    used.sort(key=lambda kv: (kv[1]["sort_key"][0], str(kv[1]["sort_key"][1])))
    lines = [HEAD, "", NOTE]
    for k, e in used:
        note = f"　<sub>［#{k}"
        if e.get("note"):
            note += "；" + e["note"].strip().split("　")[0][:60]
        note += "］</sub>"
        lines.append(f"{e['apa']}{note}\n")

    new = "\n".join(lines).rstrip() + "\n" + tail
    DOC.write_text(body + new, encoding="utf-8")

    print(f"§15.2 重建：{len(used)} 条被引用，{len(unused)} 条未在本文档引用")
    # 自检：不得残留已知的占位作者名
    s2 = DOC.read_text("utf-8")
    stale = ["Cangut, B.", "Kang, N., Sakamoto", "Li, Y., Wang, C., & Zhang, H",
             "Shen, Y., Zhang, L.", "Suzuki, K., Nakano", "Wei, L., Chen, X.",
             "Zhu, Y., Wang, T.", "Zhang, Z., Wang, Q.", "Wang, X., Liu, Y., & Zhao",
             "Lopez, C., Martinez", "Bao, W. Y.", "Amini, R. E., Katrakazas"]
    left = [x for x in stale if x in s2]
    assert not left, f"§15.2 仍有占位作者名：{left}"
    print("自检通过：无占位作者名残留")


if __name__ == "__main__":
    main()
