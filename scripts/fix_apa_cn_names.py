#!/usr/bin/env python3
"""修正 apa_refs.json 中 Crossref 姓名颠倒的三条（#33/#67/#71），并处理同作者同年碰撞的 a/b 后缀。

背景：Crossref 对部分中文作者把「名」记入 family、「姓」记入 given，导致 APA 条目与
正文引注全部使用了「名」。此前仅在 note 字段留了说明，未实际改写 apa 与 intext。
"""
import json
import re
from collections import defaultdict
from pathlib import Path

P = Path(__file__).resolve().parent / "apa_refs.json"
d = json.loads(P.read_text(encoding="utf-8"))

FIX = {
    "33": dict(
        authors="Cheng, Y. N., Zhong, X., Ye, M., & Tian, L. W.",
        old="Yunuo, C., Xia, Z., Min, Y., & Liwei, T.",
        intext="(Cheng et al., 2022)",
        sort_key=["cheng", 2022],
        note="Crossref 将「名」记入 family 字段，已按论文署名 Cheng Yunuo / Zhong Xia / Ye Min / Tian Liwei 复原姓氏",
    ),
    "67": dict(
        authors="Cheng, Y. N., Zhong, X., & Tian, L. W.",
        old="Yunuo, C., Xia, Z., & Liwei, T.",
        intext="(Cheng et al., 2023b)",
        sort_key=["cheng", 2023.2],
        note="Crossref 姓名颠倒已复原；与 #45 同作者同年（疑似一稿两投），按 APA 7th 加 a/b 后缀，本条为 2023b",
    ),
    "71": dict(
        authors="Zhang, Y. T., Li, X. M., Yan, X. D., & Xue, Q. W.",
        old="Yuting, Z., Xiaomeng, L., Xuedong, Y., & Qingwan, X.",
        intext="(Zhang et al., 2015)",
        sort_key=["zhang", 2015],
        note="Crossref 姓名颠倒已复原（张钰婷 / 李晓萌 / 严学栋 / 薛清婉）",
    ),
    "45": dict(
        authors=None,
        old=None,
        intext="(Cheng et al., 2023a)",
        sort_key=["cheng", 2023.1],
        note="与 #67 同作者同年（疑似同一数据两次发表），按 APA 7th 加 a/b 后缀，本条为 2023a",
    ),
}

for k, f in FIX.items():
    e = d[k]
    if f["old"]:
        assert f["old"] in e["apa"], f"#{k} 未匹配到旧作者串"
        e["apa"] = e["apa"].replace(f["old"], f["authors"], 1)
    if k in ("67", "45"):
        yr = "2023a" if k == "45" else "2023b"
        e["apa"] = re.sub(r"\((2023)\)\.", f"({yr}).", e["apa"], count=1)
    e["intext"] = f["intext"]
    e["sort_key"] = f["sort_key"]
    e["note"] = f["note"]
    print(f'#{k} -> {e["intext"]}')
    print("     ", e["apa"][:150])

# 复查是否仍有同姓同年碰撞未加后缀
buck = defaultdict(list)
for k, e in d.items():
    buck[e["intext"]].append(k)
dup = {a: b for a, b in buck.items() if len(b) > 1}
print("\n仍存在的相同 intext（需人工判断是否同一文献族）:")
for a, b in sorted(dup.items()):
    print("  ", a, "->", b)

P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("\nsaved", P)
