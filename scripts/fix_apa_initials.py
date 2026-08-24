#!/usr/bin/env python3
"""修正 scripts/apa_refs.json 中中文作者名的首字母缩写。

问题（已用 Crossref API 逐条核验）
  APA 第 7 版：一个**连写**的拼音名（Yuting、Liwei、Yunuo、威宇）是**单个**
  given name，缩写只取一个首字母（Zhang, Y.）。原 build_apa_refs.py 把连写
  拼音按音节切分成两个缩写（Zhang, Y. T.），共 10 处错误。

  另一个后果：同一作者 Cheng Yunuo 在 #33/#67（Crossref 记 "Yunuo"）与
  #45（Crossref 记 "Yu-nuo"）之间形式不一致，会破坏参考文献表的字母序与
  同作者同年后缀（2023a/2023b）的配对。此处统一取单首字母形式。

  #79 的作者 Crossref 只给汉字（given='威宇', family='鲍'），转写为
  Bao, W.（威宇 = Weiyu，单个给定名）。

不改动的项
  #71 标题结尾 "distanc" 是 IEEE 官方记录中的**原始拼写错误**（Crossref
  已核验）。APA 要求照录出版物题名，故保留，仅在 note 中标注，以免被误认为
  本文转录失误。
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REFS = ROOT / "scripts" / "apa_refs.json"

# (idx, 错误形式, 正确形式)　—— 均以 Crossref 的 given 字段为准
FIXES = [
    (33, "Cheng, Y. N.", "Cheng, Y."),      # given='Yunuo'
    (33, "Tian, L. W.", "Tian, L."),        # given='Liwei'
    (45, "Cheng, Y. N.", "Cheng, Y."),      # given='Yu-nuo'，与 #33/#67 统一
    (45, "Tian, L. W.", "Tian, L."),        # given='Li-wei'
    (67, "Cheng, Y. N.", "Cheng, Y."),      # given='Yunuo'
    (67, "Tian, L. W.", "Tian, L."),        # given='Liwei'
    (71, "Zhang, Y. T.", "Zhang, Y."),      # given='Yuting'
    (71, "Li, X. M.", "Li, X."),            # given='Xiaomeng'
    (71, "Yan, X. D.", "Yan, X."),          # given='Xuedong'
    (71, "Xue, Q. W.", "Xue, Q."),          # given='Qingwan'
    (79, "Bao, W. Y.", "Bao, W."),          # given='威宇' = Weiyu
]

NOTES = {
    71: "题名结尾 \"distanc\" 为 IEEE 官方记录中的原始拼写错误（Crossref 已核验），"
        "按 APA 照录出版物题名的要求保留。",
    45: "与 #67 疑为一稿两投（同作者、同方法、同结论）；证据只计一次，优先采用 #45。",
}


def main() -> None:
    d = json.loads(REFS.read_text("utf-8"))
    n = 0
    for idx, old, new in FIXES:
        k = str(idx)
        e = d[k]
        if old not in e["apa"]:
            print(f"SKIP #{idx}: {old}（已修或不存在）")
            continue
        e["apa"] = e["apa"].replace(old, new)
        n += 1
        print(f"FIX  #{idx}: {old} -> {new}")

    for idx, note in NOTES.items():
        e = d[str(idx)]
        if note not in (e.get("note") or ""):
            e["note"] = ((e.get("note") or "") + "　" + note).strip()
            print(f"NOTE #{idx}")

    # 自检：不得再有「姓, X. Y.」形式对应单个连写拼音名的情形
    raw = json.loads((ROOT / "scripts" / "apa_crossref_raw.json").read_text("utf-8"))
    left = []
    for k, r in raw.items():
        for a in (r.get("cr_authors") or []):
            g, f = a.get("given") or "", a.get("family") or ""
            for sur, giv in ((g, f), (f, g)):
                if not re.fullmatch(r"[A-Z][a-z]{2,}", giv):
                    continue
                m = re.search(re.escape(sur) + r", ([A-Z])\. ([A-Z])\.", d[k]["apa"])
                if m and m.group(1) == giv[0]:
                    left.append(f"#{k} {sur}, {m.group(1)}. {m.group(2)}. (given={giv})")
    assert not left, f"仍有未修的双缩写：{left}"

    REFS.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"\n共修 {n} 处缩写，自检通过 -> {REFS.name}")


if __name__ == "__main__":
    main()
