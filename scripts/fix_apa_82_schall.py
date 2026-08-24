#!/usr/bin/env python3
"""把 #82 Schall 的题录从学位论文版改为期刊版。

依据
  `summaries/82_2013_Schall_AR提示与老年驾驶员危险感知.md` 的表头明确记载：
  **本地全文对应的是期刊版** —— Human Factors, 55(3), 643–658,
  DOI 10.1177/0018720812462029（7 位作者）；manifest 中登记的是同名学位论文
  DOI 10.17077/etd.tbjq72y2（单作者）。两者是同一研究的两个版本。

  既然精读与全部引用的数值（视角 0.7°→16.7°、更新距离 43.75 m、显示时长
  11–13 s、触发距离 350 m、反应时收益 0.35 s）都出自期刊版全文，题录就应
  当是期刊版。已用 Crossref API 核验期刊版的题名、卷期页码与 7 位作者。
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REFS = ROOT / "scripts" / "apa_refs.json"

NEW = {
    "apa": "Schall, M. C., Rusch, M. L., Lee, J. D., Dawson, J. D., Thomas, G., "
           "Aksan, N., & Rizzo, M. (2013). Augmented Reality Cues and Elderly "
           "Driver Hazard Perception. *Human Factors: The Journal of the Human "
           "Factors and Ergonomics Society*, *55*(3), 643–658. "
           "https://doi.org/10.1177/0018720812462029",
    "intext": "(Schall et al., 2013)",
    "sort_key": ["schall", 2013],
    "type": "journal-article",
    "note": "同一研究另有学位论文版（Schall, M. C., 2013, The University of Iowa, "
            "DOI 10.17077/etd.tbjq72y2，单作者）。本研究精读与引用的全部数值均出自"
            "**期刊版全文**，故题录取期刊版；两版不得并列计为两项独立证据。",
}


def main() -> None:
    d = json.loads(REFS.read_text("utf-8"))
    old = d["82"]
    if old["apa"] == NEW["apa"]:
        print("SKIP #82（已是期刊版）")
        return
    print("旧:", old["apa"][:110])
    print("新:", NEW["apa"][:110])
    assert old["sort_key"][1] == 0, f"意外的 sort_key：{old['sort_key']}"
    d["82"] = NEW
    REFS.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("\nOK #82 已改为期刊版（Human Factors 55(3), 643–658），"
            "并在 note 中记录学位论文版以防重复计数")


if __name__ == "__main__":
    main()
