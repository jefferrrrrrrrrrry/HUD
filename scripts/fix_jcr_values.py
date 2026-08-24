#!/usr/bin/env python3
"""按 WoS 官方数据更正 7 处期刊分区/影响因子，并同步三处下游正文提及。

起因：scripts/verify_jcr_if.py 逐刊比对 wos-journal.info（WoS/JCR 数据镜像）后发现，
VENUE 表里 20 个带数值 IF 的期刊中有 7 个与官方数据不符，其中两个**分区**也错：
  Applied Ergonomics  Q1 → Q2（百分位 70.4%，未过 75 分位线）
  IET ITS             Q2 → Q3（百分位 49.6%，未过 50 分位线）
其余五处是 IF 数值偏差（含 Human Factors 3.4 → 3.6，该值被综述、幻灯片、
框架文档三处正文直接引用，故一并改）。

分区判定：JCR 以 JIF 百分位 75 / 50 / 25 为 Q1 / Q2 / Q3 / Q4 界。
"""
from __future__ import annotations

import collections
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# venue 键 -> (旧 JCR 串, 新 JCR 串, WoS 实测)
FIXES: list[tuple[str, str, str, dict]] = [
    ("Applied Ergonomics",
     "Q1 (IF 3.8) (人因工程权威期刊)",
     "Q2 (IF 3.5) (人因工程权威期刊；百分位 70.4%，未过 Q1 线)",
     {"jif": 3.5, "jif5": 4.2, "pct": "70.4%", "q": "Q2", "index": "SCIE"}),
    ("International Journal of Human-Computer Interaction",
     "Q1 (IF 4.9) (HCI 重要期刊)",
     "Q1 (IF 6.1) (HCI 重要期刊；百分位 91.7%)",
     {"jif": 6.1, "jif5": 7.0, "pct": "91.7%", "q": "Q1", "index": "SCIE"}),
    ("International Journal of Human–Computer Interaction",
     "Q1 (IF 4.9) (HCI 重要期刊)",
     "Q1 (IF 6.1) (HCI 重要期刊；百分位 91.7%)",
     {"jif": 6.1, "jif5": 7.0, "pct": "91.7%", "q": "Q1", "index": "SCIE"}),
    ("IEEE Transactions on Intelligent Transportation Systems",
     "Q1 (IF 7.9) / CCF B (智能交通顶刊)",
     "Q1 (IF 9.1) / CCF B (智能交通顶刊；百分位 95.9%)",
     {"jif": 9.1, "jif5": 10.4, "pct": "95.9%", "q": "Q1", "index": "SCIE"}),
    ("IET Intelligent Transport Systems",
     "Q2 (IF 2.5) (智能交通期刊)",
     "Q3 (IF 2.7) (智能交通期刊；百分位 49.6%，未过 Q2 线)",
     {"jif": 2.7, "jif5": 3.1, "pct": "49.6%", "q": "Q3", "index": "SCIE"}),
    ("Journal of the Society for Information Display",
     "Q3 (IF 2.2) (显示技术专刊)",
     "Q3 (IF 2.0) (显示技术专刊；百分位 44.2%)",
     {"jif": 2.0, "jif5": 2.1, "pct": "44.2%", "q": "Q3", "index": "SCIE"}),
    ("IEEE Transactions on Visualization and Computer Graphics",
     "Q1 (IF 6.5) / CCF A (可视化和计算机图形学顶刊)",
     "Q1 (IF 6.8) / CCF A (可视化和计算机图形学顶刊；百分位 92.2%)",
     {"jif": 6.8, "jif5": 6.8, "pct": "92.2%", "q": "Q1", "index": "SCIE"}),
]

# FALLBACK（按 idx）里的期刊同样要改
FALLBACK_FIXES = [
    (82,
     "Q1 (IF 3.4) (人因工程顶刊；同研究另有 Univ. of Iowa 学位论文版，不重复计数)",
     "Q1 (IF 3.6) (人因工程顶刊，百分位 86%；同研究另有 Univ. of Iowa 学位论文版，不重复计数)",
     {"jif": 3.6, "jif5": 5.5, "pct": "86%", "q": "Q1", "index": "SCIE"}),
]

# 下游正文里被直接引用的 Human Factors 影响因子
TEXT_FIXES = [
    ("thesis/_parts/sec2_1.md",
     "*Human Factors* 为 SAGE 出版、JCR Q1、影响因子 3.4，",
     "*Human Factors* 为 SAGE 出版、JCR Q1、影响因子 3.6，"),
    ("文献综述_幻灯片.html",
     "（*Human Factors*，JCR Q1，IF 3.4；",
     "（*Human Factors*，JCR Q1，IF 3.6；"),
    ("AR-HUD行人碰撞预警_毕业论文研究框架.md",
     "*Human Factors*（SAGE，JCR Q1，IF 3.4，人因工程领域旗舰刊）",
     "*Human Factors*（SAGE，JCR Q1，IF 3.6，人因工程领域旗舰刊）"),
]

SRC = "wos-journal.info（Web of Science / JCR 数据镜像），2026-08 核验"


def patch_builder() -> int:
    p = ROOT / "scripts" / "build_master_csv.py"
    s = p.read_text("utf-8")
    n = 0
    for key, old, new, _ in FIXES:
        if f'"{new}"' in s:
            print(f"SKIP {key[:44]}（已改）")
            continue
        assert f'"{old}"' in s, f"未找到旧值：{key} -> {old}"
        s = s.replace(f'"{old}"', f'"{new}"')
        n += 1
        print(f"OK   {key[:52]:52s} {old[:12]} -> {new[:12]}")
    for idx, old, new, _ in FALLBACK_FIXES:
        if f'"{new}"' in s:
            print(f"SKIP FALLBACK #{idx}（已改）")
            continue
        assert f'"{old}"' in s, f"未找到 FALLBACK #{idx} 旧值"
        s = s.replace(f'"{old}"', f'"{new}"')
        n += 1
        print(f"OK   FALLBACK #{idx} Human Factors IF 3.4 -> 3.6")
    p.write_text(s, encoding="utf-8")
    return n


def patch_texts() -> int:
    n = 0
    for rel, old, new in TEXT_FIXES:
        p = ROOT / rel
        s = p.read_text("utf-8")
        if new in s:
            print(f"SKIP {rel}（已改）")
            continue
        assert old in s, f"未找到：{rel} -> {old[:40]}"
        p.write_text(s.replace(old, new), encoding="utf-8")
        n += 1
        print(f"OK   {rel}")
    return n


def patch_jcr_json() -> None:
    p = ROOT / "jcr_quartile_data.json"
    d = json.loads(p.read_text("utf-8"), object_pairs_hook=collections.OrderedDict)
    recs = {}
    for key, old, new, w in FIXES + [(f"Human Factors", o, nw, w2)
                                    for _i, o, nw, w2 in FALLBACK_FIXES]:
        if key.endswith("Interaction") and "–" in key:      # 破折号变体不重复登记
            continue
        recs[key] = {
            "jcr": w["q"], "if": w["jif"], "if_5y": w["jif5"],
            "percentile": w["pct"], "index": w["index"],
            "note": f"本轮据 WoS 更正：旧记 {re.match(r'Q[1-4] \(IF [\d.]+\)', old).group(0)}",
            "source": SRC,
        }
    d["venues"].update(recs)
    d.setdefault("_verified_2026", {})["据 WoS 更正的条目"] = {
        k: f"{v['note']} → {v['jcr']} (IF {v['if']})" for k, v in recs.items()}
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK   jcr_quartile_data.json 登记 {len(recs)} 条更正")


def main() -> None:
    a = patch_builder()
    b = patch_texts()
    patch_jcr_json()
    print(f"\n共改 {a} 处构建表 + {b} 处正文。"
          f"\n后续：重跑 build_master_csv.py（先从 /tmp/backup_master_39.csv 复原）、"
          "build_chapter2.py 链、shoot_slides.py，再跑 verify_jcr_if.py 复核")


if __name__ == "__main__":
    main()
