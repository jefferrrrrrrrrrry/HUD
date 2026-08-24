#!/usr/bin/env python3
"""Generate the new structured comprehensive table from agent outputs.

Schema:
- 时间维度: T_onset / T_duration / T_graded / T_L1_to_L2_interval / T_L2_to_L3_interval
- 空间-平面: S_planar_color / S_planar_dynamics / S_planar_shape
- 空间-立体: S_3d_layout / S_3d_fov / S_3d_relpos

Each cell with source provenance (原文/abstract_only/未报告).
"""
import json
import pathlib
import csv
from typing import Any, Dict, List

ROOT = pathlib.Path("/home/gezhuocheng/HUD")
OUTDIR = ROOT
GROUPS_DIR = ROOT / "agent_outputs"

# Load metadata for citation/journal/jcr info
with open(ROOT / "papers_metadata.json") as f:
    meta_list = json.load(f)
meta_by_idx = {p["idx"]: p for p in meta_list}

with open(ROOT / "jcr_quartile_data.json") as f:
    jcr = json.load(f)

# Load the existing comprehensive table (for fallback citation/scenario)
with open(ROOT / "temporal_spatial_params.json") as f:
    existing = json.load(f)
existing_by_idx = {p["idx"]: p for p in existing}

# Load all agent outputs
all_data: Dict[int, Dict[str, Any]] = {}
for grp in sorted(GROUPS_DIR.glob("group*.json")):
    with open(grp) as f:
        items = json.load(f)
    for item in items:
        idx = item["idx"]
        all_data[idx] = item

print(f"Loaded {len(all_data)} entries from agent outputs")

# Sanity check - all 39?
missing = sorted(set(range(1, 40)) - set(all_data.keys()))
if missing:
    print(f"MISSING: {missing}")

# Build display rows
def fmt_cell(val: Any) -> str:
    """Format a value/source dict to a display string."""
    if isinstance(val, dict):
        v = val.get("value", "未报告")
        s = val.get("source", "")
        if s:
            return f"{v}  [来源:{s}]"
        return v
    if val is None:
        return "未报告"
    return str(val)

def get_authors_year(idx):
    if idx in meta_by_idx:
        m = meta_by_idx[idx]
        if "authors" in m:
            authors = m["authors"]
            if len(authors) == 1:
                a = authors[0]
            elif len(authors) == 2:
                a = f"{authors[0]} & {authors[1]}"
            else:
                a = f"{authors[0]} et al."
            return f"{a} ({m.get('year','')})"
        else:
            return f"{m.get('title','')[:40]}... ({m.get('year','')})"
    return "?"

# Header definition
HEADERS = [
    "idx", "数据源",
    "作者(年份)", "标题", "DOI/ID", "Venue", "JCR分区",
    "场景简述",
    # 时间维度
    "T1_出现时机", "T2_持续时长", "T3_是否分级", "T4_L1→L2间隔", "T5_L2→L3间隔",
    # 空间-平面
    "S1_色彩", "S2_动效", "S3_形状",
    # 空间-立体
    "S4_空间分布", "S5_视野FOV", "S6_相对位置",
    "关键发现",
    "待审查项"
]

rows = []
for idx in sorted(all_data.keys()):
    item = all_data[idx]
    m = meta_by_idx.get(idx, {})
    
    # Get DOI or arxiv_id
    doi_or_id = m.get("doi") or m.get("arxiv_id") or ""
    venue = m.get("venue") or ""
    jcr_q = jcr.get(venue, {}).get("quartile", "—") if venue else "—"
    
    # Title
    title = m.get("title", "")
    
    # Format data_source with marker
    src = item.get("data_source", "?")
    src_display = {
        "pdf_full": "✓ 全文(PDF)",
        "jina_full": "◐ Jina全文",
        "pdf_full_chinese_companion": "◑ 中文姊妹篇PDF",
        "abstract_only": "★【仅摘要】",
    }.get(src, src)
    
    row = [
        idx,
        src_display,
        get_authors_year(idx),
        title,
        doi_or_id,
        venue,
        jcr_q,
        item.get("scenario_brief", ""),
        # 时间维度
        fmt_cell(item.get("T_onset")),
        fmt_cell(item.get("T_duration")),
        item.get("T_graded", "未报告"),
        item.get("T_L1_to_L2_interval", "未报告"),
        item.get("T_L2_to_L3_interval", "未报告"),
        # 空间-平面
        fmt_cell(item.get("S_planar_color")),
        fmt_cell(item.get("S_planar_dynamics")),
        fmt_cell(item.get("S_planar_shape")),
        # 空间-立体
        fmt_cell(item.get("S_3d_layout")),
        fmt_cell(item.get("S_3d_fov")),
        item.get("S_3d_relpos", "未报告"),
        item.get("key_findings_oneline", ""),
        item.get("needs_review", "")
    ]
    rows.append(row)

# Write CSV
csv_path = OUTDIR / "HUD_AR-HUD_行人预警_时空设计_新表.csv"
with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(HEADERS)
    w.writerows(rows)
print(f"Wrote CSV: {csv_path}")

# Write TSV
tsv_path = OUTDIR / "HUD_AR-HUD_行人预警_时空设计_新表.tsv"
with open(tsv_path, "w", encoding="utf-8") as f:
    f.write("\t".join(HEADERS) + "\n")
    for r in rows:
        f.write("\t".join(str(c).replace("\n"," ").replace("\t"," ") for c in r) + "\n")
print(f"Wrote TSV: {tsv_path}")

# Write Markdown table
md_path = OUTDIR / "HUD_AR-HUD_行人预警_时空设计_新表.md"
with open(md_path, "w", encoding="utf-8") as f:
    f.write("# HUD/AR-HUD 行人碰撞预警 — 时空设计元素综合表\n\n")
    f.write("## 字段定义\n\n")
    f.write("**时间维度（Temporal）**\n")
    f.write("- T1 出现时机：警示首次出现的TTC时间或距离阈值\n")
    f.write("- T2 持续时长：警示在屏幕上保持的时长\n")
    f.write("- T3 是否分级：是否多级警告\n")
    f.write("- T4/T5 分级间隔：相邻级别的TTC间隔\n\n")
    f.write("**空间-平面维度（Spatial-Planar）**\n")
    f.write("- S1 色彩：颜色及RGB等参数\n")
    f.write("- S2 动效：动态/静态及具体动效\n")
    f.write("- S3 形状：图标几何形状\n\n")
    f.write("**空间-立体维度（Spatial-3D）**\n")
    f.write("- S4 空间分布：垂直面/水平面/混合/屏幕固定\n")
    f.write("- S5 视野FOV：HUD虚像视场角\n")
    f.write("- S6 相对位置：屏幕固定/行人锁定/路面锁定/世界锁定\n\n")
    f.write("**数据源标记**\n")
    f.write("- `✓ 全文(PDF)`：通过PDF原文提取（含sci-hub/IEEE/Cambridge等）\n")
    f.write("- `◐ Jina全文`：通过Jina Reader获取的Markdown全文（MDPI论文）\n")
    f.write("- `◑ 中文姊妹篇PDF`：英文版被锁但同一研究组的中文版可获取（如paper #12）\n")
    f.write("- `★【仅摘要】`：仅从abstract提取（Tandfonline锁文，**待补齐PDF**）\n\n")
    f.write("---\n\n")
    
    f.write("## 综合表格\n\n")
    # Write header
    f.write("| " + " | ".join(HEADERS) + " |\n")
    f.write("|" + "|".join(["---"] * len(HEADERS)) + "|\n")
    for r in rows:
        # Replace pipes within cells & truncate very long cells
        row_cells = []
        for c in r:
            s = str(c)
            s = s.replace("|", "\\|").replace("\n", "<br>")
            row_cells.append(s)
        f.write("| " + " | ".join(row_cells) + " |\n")
    
    # Append needs review summary
    f.write("\n---\n\n")
    f.write("## 待补齐清单（Needs Review）\n\n")
    f.write("以下论文的部分关键字段未在原文中明确报告，建议在后续整理时进一步核查：\n\n")
    
    abstract_only_idx = [idx for idx, item in all_data.items() if item.get("data_source") == "abstract_only"]
    if abstract_only_idx:
        f.write(f"### 仅摘要论文（必须补齐PDF全文）\n\n")
        for idx in sorted(abstract_only_idx):
            m = meta_by_idx.get(idx, {})
            f.write(f"- **#{idx:02d}** [{get_authors_year(idx)}] {m.get('title', '?')[:80]}\n")
            f.write(f"  - DOI: {m.get('doi', '?')}\n")
            f.write(f"  - 提示: Tandfonline 全文付费墙，需通过机构订阅、ResearchGate请求或科研通互助下载\n\n")
    
    f.write(f"### 部分字段缺失论文\n\n")
    for idx, item in sorted(all_data.items()):
        nr = item.get("needs_review", "OK")
        if nr and nr != "OK" and item.get("data_source") != "abstract_only":
            f.write(f"- **#{idx:02d}** [{get_authors_year(idx)}]: {nr}\n")

print(f"Wrote MD: {md_path}")

# Write source provenance summary
prov_path = OUTDIR / "数据源提供性_汇总.md"
with open(prov_path, "w", encoding="utf-8") as f:
    f.write("# 数据源提供性汇总\n\n")
    f.write("本次综述共39篇论文，下载/获取情况如下：\n\n")
    
    pdf_full = sorted([idx for idx, item in all_data.items() if item.get("data_source") == "pdf_full"])
    jina_full = sorted([idx for idx, item in all_data.items() if item.get("data_source") == "jina_full"])
    chinese_companion = sorted([idx for idx, item in all_data.items() if item.get("data_source") == "pdf_full_chinese_companion"])
    abstract_only = sorted([idx for idx, item in all_data.items() if item.get("data_source") == "abstract_only"])

    f.write(f"## PDF全文 ({len(pdf_full)} 篇)\n\n")
    for idx in pdf_full:
        m = meta_by_idx.get(idx, {})
        f.write(f"- #{idx:02d} {get_authors_year(idx)} — {m.get('title','')[:70]}\n")

    f.write(f"\n## Jina Reader全文 ({len(jina_full)} 篇)\n\n")
    for idx in jina_full:
        m = meta_by_idx.get(idx, {})
        f.write(f"- #{idx:02d} {get_authors_year(idx)} — {m.get('title','')[:70]}\n")

    f.write(f"\n## 中文姊妹篇PDF ({len(chinese_companion)} 篇)\n\n")
    for idx in chinese_companion:
        m = meta_by_idx.get(idx, {})
        f.write(f"- #{idx:02d} {get_authors_year(idx)} — {m.get('title','')[:70]}\n")
        f.write(f"  - 英文版DOI: `{m.get('doi','?')}` (Tandfonline锁)\n")
        f.write(f"  - 中文版DOI: `10.12141/j.issn.1000-565X.230096` 华南理工大学学报2024 (sciopen.com获取)\n")

    f.write(f"\n## 仅摘要 ({len(abstract_only)} 篇) ⚠ 待补齐\n\n")
    for idx in abstract_only:
        m = meta_by_idx.get(idx, {})
        f.write(f"- #{idx:02d} {get_authors_year(idx)} — {m.get('title','')[:70]}\n")
        f.write(f"  - DOI: `{m.get('doi','?')}`\n")
        f.write(f"  - Venue: {m.get('venue','')}\n")
print(f"Wrote provenance: {prov_path}")

print("\nDone.")
