#!/usr/bin/env python3
"""Convert 音乐流派对驾驶行为影响的多维分析0520.pdf into readable Markdown.

- Tables are detected with PyMuPDF's table finder and rendered as Markdown tables;
  their bounding boxes are excluded from the running text.
- Headings are inferred from font size + numbering patterns.
- Figures are exported to figures/template_thesis/ and referenced inline.
"""
import pathlib
import re
import statistics

import pymupdf

ROOT = pathlib.Path("/home/gezhuocheng/HUD")
SRC = ROOT / "音乐流派对驾驶行为影响的多维分析0520.pdf"
OUT = ROOT / "参考模板_音乐流派对驾驶行为影响的多维分析_周颖2024.md"
IMG_DIR = ROOT / "figures" / "template_thesis"

HEAD_PAT = re.compile(
    r"^\s*(?:"
    r"第\s*[0-9一二三四五六七八九十]+\s*章"
    r"|摘\s*要|Abstract|目\s*录|图\s*目\s*录|表\s*目\s*录|参考文献|致\s*谢|附\s*录"
    r"|\d{1,2}(?:\.\d{1,2}){1,3}\s*[^\d\s].{0,60}"
    r")\s*$"
)
BAD_HEAD = re.compile(r"[，。；、：？！]|^\d+\s*[)）]|^\(|^（|等,|等，")
NUMERIC_ONLY = re.compile(r"^[\d\s.,*\-+()\[\]%<>=~／/、·　]+$")


def in_any(bbox, rects, pad=2):
    x0, y0, x1, y1 = bbox
    for r in rects:
        if x0 >= r[0] - pad and x1 <= r[2] + pad and y0 >= r[1] - pad and y1 <= r[3] + pad:
            return True
        cy = (y0 + y1) / 2
        if r[1] - pad <= cy <= r[3] + pad and x0 >= r[0] - 20 and x1 <= r[2] + 20:
            return True
    return False


def md_table(rows):
    cleaned = []
    for r in rows:
        cells = []
        for c in r:
            c = (c or "").replace("\n", " ").replace("|", "\\|")
            c = re.sub(r"[.．·]{3,}", " ", c)
            cells.append(re.sub(r"\s+", " ", c).strip())
        if any(cells):
            cleaned.append(cells)
    if len(cleaned) < 3:
        return ""
    w = max(len(r) for r in cleaned)
    if w < 2:
        return ""
    flat = " ".join(" ".join(r) for r in cleaned)
    nums = re.findall(r"\d+\.\d+|\b\d{1,4}\b", flat)
    if len(nums) < 4:
        return ""
    letters = len(re.findall(r"[A-Za-z]", flat))
    if letters > 60 and len(nums) < 8:
        return ""
    cleaned = [r + [""] * (w - len(r)) for r in cleaned]
    head = cleaned[0]
    if not any(head):
        head = [f"列{i + 1}" for i in range(w)]
        cleaned = cleaned[1:]
    else:
        cleaned = cleaned[1:]
    out = ["| " + " | ".join(head) + " |",
           "|" + "|".join(["---"] * w) + "|"]
    for r in cleaned:
        out.append("| " + " | ".join(r) + " |")
    return "\n".join(out)


def main():
    doc = pymupdf.open(SRC)
    IMG_DIR.mkdir(parents=True, exist_ok=True)

    sizes = []
    for pno in range(doc.page_count):
        for b in doc[pno].get_text("dict")["blocks"]:
            if b.get("type") != 0:
                continue
            for ln in b["lines"]:
                for s in ln["spans"]:
                    if s["text"].strip():
                        sizes.append(s["size"])
    body = statistics.median(sizes)

    md = [
        "# 音乐流派对驾驶行为影响的多维分析：个人偏好与音乐元素的影响",
        "",
        "> **文档性质**：参考模板（硕士学位论文全文转录，供本课题各交付文档参照写作体例）  ",
        "> **作者**：周颖　**指导教师**：葛燕 副研究员（中国科学院心理研究所）  ",
        "> **学位/专业**：理学硕士 / 应用心理学　**培养单位**：中国科学院心理研究所　"
        "**完成时间**：2024 年 6 月  ",
        "> **原始文件**：`音乐流派对驾驶行为影响的多维分析0520.pdf`（146 页）  ",
        "> **参照要点**：章节层级（研究背景→文献综述→问题提出→研究内容与预期目标→"
        "分实验章→总讨论→结论）、每个实验章内固定的「研究目的 / 实验设计 / 被试 / 实验材料 / "
        "实验流程 / 实验结果 / 小结与讨论」六段式、统计量的报告格式（F、p、η²、95% CI）、"
        "图表编号（图4-1、表4-7）与三线表风格。",
        "",
        "---",
        "",
    ]

    fig_count = tbl_count = 0
    for pno in range(doc.page_count):
        page = doc[pno]
        md.append(f"\n<!-- ===== 原文 第 {pno + 1} 页 ===== -->\n")

        table_rects, table_md = [], []
        page_text = page.get_text()
        is_toc = bool(re.search(r"[.．·]{6,}", page_text))
        if not is_toc:
            for strat in ("lines", "text"):
                try:
                    tabs = page.find_tables(strategy=strat).tables
                except Exception:
                    tabs = []
                if tabs:
                    for t in tabs:
                        m = md_table(t.extract())
                        if m and m.count("\n") >= 2:
                            table_rects.append(tuple(t.bbox))
                            table_md.append(m)
                    if table_md:
                        break

        for i, info in enumerate(page.get_images(full=True)):
            try:
                pix = pymupdf.Pixmap(doc, info[0])
                if pix.width < 140 or pix.height < 140:
                    continue
                if pix.n - pix.alpha >= 4:
                    pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
                name = f"p{pno + 1:03d}_{i}.png"
                pix.save(IMG_DIR / name)
                fig_count += 1
                md.append(f"![原文第{pno + 1}页图{i + 1}](figures/template_thesis/{name})\n")
            except Exception:
                pass

        buf = []

        def flush():
            if buf:
                md.append(" ".join(buf).strip())
                md.append("")
                buf.clear()

        for b in page.get_text("dict")["blocks"]:
            if b.get("type") != 0:
                continue
            for ln in b["lines"]:
                t = "".join(s["text"] for s in ln["spans"]).strip()
                if not t:
                    continue
                if in_any(ln["bbox"], table_rects):
                    continue
                if re.fullmatch(r"[-–—\s]*\d{1,3}[-–—\s]*", t):
                    continue
                sp = [s for s in ln["spans"] if s["text"].strip()]
                size = max(s["size"] for s in sp)
                bold = any("Bold" in s["font"] or "bold" in s["font"] for s in sp)
                head_like = bool(HEAD_PAT.match(t)) and not BAD_HEAD.search(t)
                numericish = bool(NUMERIC_ONLY.match(t))
                level = None
                if numericish or len(t) > 80:
                    pass
                elif size >= body * 1.45 and not BAD_HEAD.search(t):
                    level = 2
                elif head_like and re.match(r"^\s*第", t):
                    level = 2
                elif head_like and re.match(r"^\s*\d{1,2}\.\d{1,2}\s*\S+$", t):
                    level = 3
                elif head_like:
                    level = 4
                elif size >= body * 1.18 and bold and len(t) < 40 and not BAD_HEAD.search(t):
                    level = 3
                if level:
                    flush()
                    md.append(f"{'#' * level} {t}")
                    md.append("")
                else:
                    buf.append(t)
        flush()

        for m in table_md:
            tbl_count += 1
            md.append(m)
            md.append("")

    text = "\n".join(md)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUT.name}: {len(text)} chars, {fig_count} figures, {tbl_count} tables")


if __name__ == "__main__":
    main()
