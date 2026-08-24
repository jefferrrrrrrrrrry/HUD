#!/usr/bin/env python3
"""交付前一致性总校验：CSV / 综述正文 / 幻灯片 / 讲稿 / 框架文档五份产物。

校验项
  1. CSV：102 行 × 24 列、序号连续、无空单元、★APA 两列与 apa_refs.json 一致
  2. 综述正文：汉字数落在 3.5–4.5 万区间；表号 2-1..2-18 连续无重复；图号 2-1..2-5
  3. 幻灯片：34 页、无裸 $ 数学、图片路径存在、无硬编码页码
  4. 讲稿：页数与幻灯片一致、每页四块齐全
  5. 框架文档：§15.2 与 apa_refs.json 一致，无占位作者名、无失效 DOI
  6. 跨文件：不得残留已修正的旧写法（旧 APA 缩写、Bliss 30%、27.3 m 反向表述）
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
fail: list[str] = []


def ck(cond: bool, msg: str) -> None:
    print(("  ✓ " if cond else "  ✗ ") + msg)
    if not cond:
        fail.append(msg)


apa = json.loads((ROOT / "scripts" / "apa_refs.json").read_text("utf-8"))

print("[1] 文献综合表 CSV")
rows = list(csv.reader((ROOT / "HUD_AR-HUD_行人预警_文献综合表.csv")
                       .open(encoding="utf-8-sig")))
hdr, data = rows[0], rows[1:]
ck(len(data) == 102, f"102 行（实为 {len(data)}）")
ck(len(hdr) == 24 and {len(r) for r in data} == {24}, "全部 24 列")
ck([r[0] for r in data] == [str(i) for i in range(1, 103)], "序号 1–102 连续")
ck(not [1 for r in data for c in r if not c.strip()], "无空单元")
bad = [r[0] for r in data if r[21] != apa[r[0]]["intext"] or r[22] != apa[r[0]]["apa"]]
ck(not bad, f"★APA 两列与权威源一致（不符：{bad}）")
ck(len({r[1] for r in data}) == 102, "文献标题无重复")

print("\n[2] 综述正文")
t = (ROOT / "thesis" / "第2章_文献综述_v2.md").read_text("utf-8")
n = len(re.findall(r"[\u4e00-\u9fff]", t))
ck(35000 <= n <= 45000, f"汉字数 {n:,} 落在 3.5–4.5 万")
tb = sorted({int(x) for x in re.findall(r"表 2-(\d+)　", t)})
ck(tb == list(range(1, 19)), f"表号 2-1..2-18 连续（实为 {tb}）")
fg = sorted({int(x) for x in re.findall(r"图 2-(\d+)　", t)})
ck(fg == list(range(1, 6)), f"图号 2-1..2-5 连续（实为 {fg}）")

print("\n[3] 幻灯片 HTML")
h = (ROOT / "文献综述_幻灯片.html").read_text("utf-8")
ck(len(re.findall(r"<section\b", h)) == 34, "34 页")
ck("$" not in h[:h.rindex("<script>")], "正文无裸 LaTeX 定界符")
imgs = re.findall(r'<img[^>]+src="([^"]+)"', h)
ck(all((ROOT / u).exists() for u in imgs), f"{len(imgs)} 张配图路径均存在")
ck(not re.search(r'<div class="pg">[^<\s]', h), "页码由 JS 生成（无硬编码）")
ck("@media print" in h, "含打印样式（可导出 PDF）")

print("\n[4] 讲稿")
k = (ROOT / "文献综述_幻灯片_讲稿.md").read_text("utf-8")
pgs = re.findall(r"^## p(\d+)　", k, re.M)
ck([int(x) for x in pgs] == list(range(1, 35)), f"34 页与幻灯片对齐（实为 {len(pgs)}）")
miss = [f"p{m.group(1)}"
        for m in re.finditer(r"^## p(\d+)　.*?$(.*?)(?=^## |\Z)", k, re.M | re.S)
        if not all(b in m.group(2) for b in ("**⏱", "**讲稿：**", "**备答：**"))]
ck(not miss, f"每页三块必备齐全（缺：{miss}）")

print("\n[5] 框架文档 §15.2")
f = (ROOT / "AR-HUD行人碰撞预警_毕业论文研究框架.md").read_text("utf-8")
sec = f[f.index("### 15.2"):]
ent = re.findall(r"］</sub>", sec)
ck(len(ent) >= 40, f"§15.2 有 {len(ent)} 条自动生成条目")
idxs = re.findall(r"［#(\d+)", sec)
mism = [i for i in idxs if apa[i]["apa"] not in sec]
ck(not mism, f"每条与权威源逐字一致（不符：{mism}）")
ck("10.1145/2687923" not in f, "已移除误标 DOI 10.1145/2687923（实为 ColorBless）")
ck("ICIEA.2013.6566503" not in f, "已移除误标 DOI ICIEA.2013.6566503（实为血糖监测论文）")

print("\n[6] 跨文件：已修正写法不得残留")
# 前缀「而非」「不是」「应为」等否定语境属正当引用（讲稿备答里说明修了什么），
# 故用负向前查排除；只抓真正作为**正文主张**出现的旧写法。
STALE = {
    "旧 APA 缩写 Zhang, Y. T.": r"(?<!而非 )(?<!不是 )(?<!应为 )Zhang, Y\. T\.",
    "旧 APA 缩写 Cheng, Y. N.": r"(?<!而非 )(?<!不是 )Cheng, Y\. N\.",
    "旧 APA 缩写 Bao, W. Y.": r"(?<!而非 )(?<!不是 )Bao, W\. Y\.",
    # 只在「同一行内无撤回标注」时算残留：小结表的"原表述 | 修正后"两栏
    # 天然会提到旧写法，那是正当的，不能算残留。
    "未溯源的 Bliss 30% 门限（作为依据使用）":
        r"Bliss（2003）元分析给出 30%(?![^\n]*(?:已撤回|未能溯源|不得))",
    "#12 制动距离反向表述": r"远大于基线64\.5",
}
targets = ["thesis/第2章_文献综述_v2.md", "文献综述_幻灯片.html",
           "文献综述_幻灯片_讲稿.md", "AR-HUD行人碰撞预警_毕业论文研究框架.md",
           "时间元素设计参数_专题分析.md", "HUD_AR-HUD_行人预警_文献综合表.csv"]
for label, pat in STALE.items():
    hit = [p for p in targets
           if re.search(pat, (ROOT / p).read_text("utf-8"))]
    ck(not hit, f"{label} —— 残留于 {hit}" if hit else label)

print("\n[7] 冲突六裁定的跨文件一致性")
ch2 = t
slides = h
talk = k
ck("功能上是 alpha" in ch2, "综述 §2.3.5 载有记法裁定")
ck("均**支持情境意识" in ch2 and "并非推荐 20%" in ch2,
   "综述已更正 #53 的读法（20% 非推荐值）")
ck("四源收敛" in slides or "四源收敛 <b>0.6–0.75</b>" in slides, "幻灯片 p20 已同步裁定")
ck("本轮已裁定" in slides, "幻灯片 p27 已标注冲突六已裁定")
ck("T 值方向已裁定为 alpha" in (ROOT / "HUD_AR-HUD_行人预警_文献综合表.csv").read_text("utf-8"),
   "CSV #48 色彩显示列载有裁定依据")
ck("裁定" in talk and "Hussain" in talk, "讲稿已同步裁定与检索漏检")
# 裁定必须同时保留其证据等级限定，不得被读成已由原文确认
for name, txt in (("综述", ch2), ("CSV", (ROOT / "HUD_AR-HUD_行人预警_文献综合表.csv").read_text("utf-8"))):
    ck(("间接" in txt), f"{name} 保留了「间接证据」限定（未夸大为原文确认）")

print("\n[8] 期刊分区与影响因子（离线比对 WoS 快照）")
snap_p = ROOT / "scripts" / "_jcr_verified.json"
ck(snap_p.exists(), "存在 WoS 核验快照 scripts/_jcr_verified.json")
if snap_p.exists():
    snap = json.loads(snap_p.read_text("utf-8"))["venues"]
    mism = []
    for name, w in snap.items():
        m = re.match(r"(Q[1-4]) \(IF ([\d.]+)\)", w["recorded"])
        if not m or w["jif"] in (None, "N/A"):
            mism.append(name)
            continue
        if m.group(1) != w["quartile"] or abs(float(m.group(2)) - float(w["jif"])) > 0.15:
            mism.append(f'{w["short"]}(记 {m.group(0)} vs WoS {w["quartile"]} IF {w["jif"]})')
    ck(not mism, f"{len(snap)} 刊分区/IF 与 WoS 一致（不符：{mism}）")
    # CSV 里不得再出现「有分区却无 IF」的占位
    csv_txt = (ROOT / "HUD_AR-HUD_行人预警_文献综合表.csv").read_text("utf-8")
    ck(not re.search(r"Q[1-4] \(IF -\)", csv_txt), "CSV 无「Q? (IF -)」占位")
    ck("IF 未核验" not in csv_txt, "CSV 无「IF 未核验」标注")
    # 两处曾误标的分区不得回退
    ck("Q2 (IF 3.5)" in csv_txt, "Applied Ergonomics 已更正为 Q2（曾误记 Q1）")
    ck("Q3 (IF 2.7)" in csv_txt, "IET ITS 已更正为 Q3（曾误记 Q2）")
    for label, path in (("综述", "thesis/第2章_文献综述_v2.md"),
                        ("幻灯片", "文献综述_幻灯片.html"),
                        ("框架文档", "AR-HUD行人碰撞预警_毕业论文研究框架.md")):
        s_ = (ROOT / path).read_text("utf-8")
        ck("IF 3.4" not in s_ and "影响因子 3.4" not in s_,
           f"{label} 的 Human Factors 影响因子已改为 3.6")

print("\n[9] 构建产物不得有重复段落（插入型脚本非幂等的典型症状）")
INTENDED_DUP = {"⚠ 归因更正（2026-08）"}          # 同一勘误在两节各挂一次，属有意重复
for label, path in (("综述", "thesis/第2章_文献综述_v2.md"),
                    ("讲稿", "文献综述_幻灯片_讲稿.md"),
                    ("框架文档", "AR-HUD行人碰撞预警_毕业论文研究框架.md"),
                    ("时间专题", "时间元素设计参数_专题分析.md"),
                    ("空间专题", "空间元素设计参数_专题分析.md")):
    txt = (ROOT / path).read_text("utf-8")
    paras = [x.strip() for x in re.split(r"\n\s*\n", txt) if len(x.strip()) >= 80]
    dup = [p for p, n in __import__("collections").Counter(paras).items()
           if n > 1 and not any(w in p for w in INTENDED_DUP)]
    ck(not dup, f"{label} 无重复段落"
       + (f"（重复 {len(dup)} 组，首条：{dup[0][:40]}…）" if dup else ""))

print("\n[10] Markdown 表格列数须与表头一致（多写一个 | 会整列错位）")


def _cells(line: str) -> int:
    s = line.strip().strip("|")
    return len(re.split(r"(?<!\\)\|", s))


for label, path in (("综述", "thesis/第2章_文献综述_v2.md"),
                    ("框架文档", "AR-HUD行人碰撞预警_毕业论文研究框架.md"),
                    ("讲稿", "文献综述_幻灯片_讲稿.md"),
                    ("时间专题", "时间元素设计参数_专题分析.md"),
                    ("空间专题", "空间元素设计参数_专题分析.md"),
                    ("综合表 MD", "HUD_AR-HUD_行人预警_文献综合表.md")):
    lines = (ROOT / path).read_text("utf-8").split("\n")
    bad, ntab, ncol = [], 0, None
    for i, ln in enumerate(lines):
        if not ln.strip().startswith("|"):
            ncol = None
            continue
        sep = re.compile(r"^\|[\s:|-]+\|$")
        if ncol is None:
            if i + 1 < len(lines) and sep.match(lines[i + 1].strip()):
                ncol, ntab = _cells(ln), ntab + 1
            continue
        if sep.match(ln.strip()):
            continue
        if _cells(ln) != ncol:
            bad.append(f"行 {i + 1}（{_cells(ln)}≠{ncol}）")
    ck(not bad, f"{label} {ntab} 张表列数齐整"
       + (f"（错位：{bad[:4]}）" if bad else ""))

print("\n" + "=" * 62)
if fail:
    print(f"✗ {len(fail)} 项未通过：")
    for x in fail:
        print("   -", x)
    sys.exit(1)
print("✓ 全部校验通过")


