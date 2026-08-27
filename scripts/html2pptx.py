#!/usr/bin/env python3
"""HTML 幻灯片 → 可编辑 PPTX 转换器（通用，面向本库四种 deck 的结构）。

规则：
  · 16:9（1280×720 版心等比），每页一张幻灯片；元素全部为可编辑文本框/表格，不做图片化。
  · 按内容流式布局：header（面包屑）→ 内容块 → 页码；内容块间自动避让。
  · 支持：h1.crumb / h2 / h3 / p / ul.li / table / .def / .note / .warn / .ok / .box.g/.r/.a
    / .cols2/.cols3 / .p4 参数页四行 / .cover 封面。
  · 所有 div 嵌套按深度感知拆分，不做正则贪婪假设。
"""
from __future__ import annotations

import html as H
import math
import re
import sys
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.util import Emu, Pt

ROOT = Path(__file__).resolve().parents[1]

BLUE = RGBColor(0x44, 0x72, 0xC4)
BLUE_D = RGBColor(0x2F, 0x52, 0x8F)
BLUE_L = RGBColor(0xD9, 0xE2, 0xF3)
RED = RGBColor(0xC0, 0x00, 0x00)
GREEN = RGBColor(0x3E, 0x7D, 0x3E)
AMBER = RGBColor(0xE0, 0xA1, 0x00)
GREY = RGBColor(0x8C, 0x8C, 0x8C)
INK = RGBColor(0x1A, 0x1A, 0x1A)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
BG_SUB = RGBColor(0xFA, 0xFB, 0xFD)
LINE_G = RGBColor(0xD6, 0xD6, 0xD6)

FONT = "微软雅黑"
MATH = "Cambria Math"

SLIDE_W, SLIDE_H = 1280, 720
MARGIN = 46
HEAD_H = 66
BOTTOM = 40

LH = {11.5: 1.9, 12: 1.9, 13: 1.85, 13.5: 1.82, 14: 1.8, 14.5: 1.78,
      15: 1.75, 15.5: 1.72, 16: 1.7, 16.5: 1.68, 17: 1.65, 18: 1.6}


def lh(sz: float) -> float:
    return LH.get(round(sz * 2) / 2, LH.get(int(sz), 1.7))


TAG_OP = re.compile(r"<(div|p|ul|ol|li|h1|h2|h3|h4|table|thead|tbody|tr|td|th|b|em|span|br|figure|figcaption)\b")
TAG_RE = re.compile(r"</(div|p|ul|ol|li|h1|h2|h3|h4|table|thead|tbody|tr|td|th|b|em|span|br|figure|figcaption)>")


def split_top(html: str) -> list[str]:
    """按顶层元素切分（div/table/figure/p/ul）。嵌套不破。"""
    out, buf, depth = [], [], 0
    i = 0
    n = len(html)
    while i < n:
        if html[i] == "<":
            m = TAG_OP.match(html, i)
            m2 = TAG_RE.match(html, i)
            if m:
                tag = m.group(1)
                end = html.find(">", i)
                if end == -1:
                    buf.append(html[i:]); break
                tok = html[i:end + 1]
                if tag not in ("br",):
                    if depth == 0 and buf and not "".join(buf).strip():
                        buf = []
                    depth += 1
                buf.append(tok)
                i = end + 1
                continue
            if m2:
                tag = m2.group(1)
                depth -= 1
                buf.append("</" + tag + ">")
                i = m2.end()
                continue
            # 其他标签（注释等）
            end = html.find(">", i)
            if end == -1:
                buf.append(html[i:]); break
            tok = html[i:end + 1]
            if tok.lstrip().lower().startswith("<!--"):
                i = end + 1
                continue
            buf.append(tok)
            i = end + 1
            continue
        buf.append(html[i])
        i += 1
        if depth == 0 and buf and buf[-1] == ">" :
            pass
    # 由于 div 自嵌套，用另一方案：栈式
    return out


BLOCK_TAGS = {"div", "table", "figure", "p", "ul", "ol"}


def top_blocks(html: str) -> list[str]:
    """栈式取顶层块（div/table/figure/p/ul）。其余标签作为内容留存。"""
    out, stack, buf = [], [], []
    i, n = 0, len(html)
    while i < n:
        ch = html[i]
        if ch != "<":
            buf.append(ch)
            i += 1
            continue
        m2 = TAG_RE.match(html, i)
        if m2:
            tag = m2.group(1)
            buf.append("</" + tag + ">")
            if stack and stack[-1] == tag:
                stack.pop()
                if not stack:
                    out.append("".join(buf)); buf = []
            i = m2.end()
            continue
        m = TAG_OP.match(html, i)
        end = html.find(">", i)
        if end == -1:
            buf.append(html[i:])
            break
        tok = html[i:end + 1]
        if tok.lstrip().startswith("<!") or tag_is_void(tok):
            buf.append(tok)
        else:
            tag = m.group(1) if m else "?"
            buf.append(tok)
            if tag in BLOCK_TAGS:
                stack.append(tag)
        i = end + 1
    if buf and "".join(buf).strip():
        out.append("".join(buf))
    return out


def tag_is_void(tok: str) -> bool:
    t = re.match(r"<(\w+)", tok)
    return bool(t) and t.group(1) in ("br", "img", "hr", "meta", "input")


def text_of(node: str) -> str:
    s = re.sub(r"<[^>]+>", "", node)
    return re.sub(r"\s+", " ", H.unescape(s)).strip()


def para_metrics(lvl: int, size: float):
    return (0.05 + lvl * 0.42, 0.36)


def estimate_height(card, width: float) -> float:
    total = 0.0
    for lvl, t, sz, bold, role in card.paras:
        if not t:
            total += sz * 0.45
            continue
        indent, hang = para_metrics(lvl, sz)
        usable = width - indent - hang
        cpl = max(1, int(usable / (sz * 0.5)))
        t2 = ("• " + t) if role == "bullet" else t
        n_lines = max(1, math.ceil(len(t2) / cpl))
        total += n_lines * sz * lh(sz) / 2 + sz * 0.22
    return total + card.pad * 2 + 6


class Card:
    def __init__(self, kind="box", pad=12):
        self.kind = kind
        self.pad = pad
        self.paras: list[tuple[int, str, float, bool, str]] = []
        self.cols: list[Card] = []

    def add(self, lvl, text, size, bold=False, role="p"):
        self.paras.append((lvl, text, size, bold, role))


def add_rich(card: Card, html: str) -> None:
    """把块内内容解析为段落。html 为不含外层 div 的 inner。"""
    for m in re.finditer(r"<h3[^>]*>(.*?)</h3>", html, re.S):
        card.add(0, text_of(m.group(1)), 15, True, "h3")
    for m in re.finditer(r"<p[^>]*>(.*?)</p>", html, re.S):
        t = text_of(m.group(1))
        if t:
            card.add(0, t, 14, False, "p")
    for m in re.finditer(r"<li[^>]*>(.*?)</li>", html, re.S):
        t = text_of(m.group(1))
        if t:
            card.add(0, t, 13.5, False, "bullet")
    # 剩余裸文本与 <br>
    stripped = re.sub(r"<h3[^>]*>.*?</h3>|<p[^>]*>.*?</p>|<li[^>]*>.*?</li>", "", html, flags=re.S)
    bare = text_of(re.sub(r"<br\s*/?>", " ", stripped))
    if bare:
        card.add(0, bare, 14, False, "p")


def classify(blk: str):
    blk = blk.strip()
    if blk.startswith("<div"):
        cm = re.match(r'<div class="([^"]*)"', blk)
        cls = cm.group(1) if cm else ""
        inner = blk[cm.end():]
        inner = re.sub(r"</div>\s*$", "", inner, flags=re.S)
        if cls in ("def", "note", "warn", "ok"):
            card = Card(cls)
            add_rich(card, inner)
            return cls, card
        if cls.startswith("cols"):
            card = Card("cols")
            for cm2 in re.finditer(r'<div class="box(?: [^"]*)?">', inner):
                pass
            sub = re.findall(r'<div class="box(?: [^"]*)?">.*?</div>', inner, re.S)
            card.cols = []
            for s2 in sub:
                c2 = Card("box")
                s3 = re.sub(r"^<div class=\"box(?: [^\"]*)?\">", "", s2)
                s3 = re.sub(r"</div>$", "", s3)
                add_rich(c2, s3)
                card.cols.append(c2)
            if not card.cols:
                card.cols = [Card("box")]
            return "cols", card
        if cls == "p4":
            card = Card("p4")
            starts = [m.start() for m in re.finditer(r'<div class="row">', blk)]
            for a, b in zip(starts, starts[1:] + [len(blk)]):
                chunk = blk[a:b]
                lb = re.search(r'<div class="lb[^"]*">(.*?)</div>', chunk, re.S)
                tx = re.search(r'<div class="tx">(.*?)</div>', chunk, re.S)
                if lb and tx:
                    card.add(0, "▍" + text_of(lb.group(1)) + "　" + text_of(tx.group(1)), 16, True, "p")
            return "p4", card
        if cls.startswith("box"):
            card = Card("box")
            add_rich(card, inner)
            return "box", card
    if blk.startswith("<table"):
        card = Card("table")
        card.table_html = blk.strip()
        return "table", card
    if blk.startswith("<p"):
        card = Card("box")
        add_rich(card, blk)
        return "box", card
    return None


def draw_card(sl, card: Card, x: float, y: float, w: float, h: float) -> None:
    acc = None
    if card.kind in ("def", "note", "warn", "ok"):
        bgc = {"def": BLUE_L, "note": RGBColor(0xFF, 0xF8, 0xE5),
               "warn": RGBColor(0xFD, 0xF2, 0xF2), "ok": RGBColor(0xF2, 0xF9, 0xF2)}[card.kind]
        acc = {"def": BLUE, "note": AMBER, "warn": RED, "ok": GREEN}[card.kind]
        shp = sl.shapes.add_shape(MSO_SHAPE.RECTANGLE, Emu(int(x * 12700)), Emu(int(y * 12700)),
                                  Emu(int(w * 12700)), Emu(int((h + 6) * 12700)))
        shp.fill.solid(); shp.fill.fore_color.rgb = bgc
        shp.line.color.rgb = acc; shp.line.width = Pt(1.4)
        shp.shadow.inherit = False
        bar = sl.shapes.add_shape(MSO_SHAPE.RECTANGLE, Emu(int(x * 12700)), Emu(int(y * 12700)),
                                  Emu(int(5 * 12700)), Emu(int((h + 6) * 12700)))
        bar.fill.solid(); bar.fill.fore_color.rgb = acc; bar.line.fill.background()
        bar.shadow.inherit = False
        x += 16; w -= 26
    elif card.kind == "box":
        shp = sl.shapes.add_shape(MSO_SHAPE.RECTANGLE, Emu(int(x * 12700)), Emu(int(y * 12700)),
                                  Emu(int(w * 12700)), Emu(int((h + 6) * 12700)))
        shp.fill.solid(); shp.fill.fore_color.rgb = WHITE
        shp.line.color.rgb = LINE_G; shp.line.width = Pt(1.2)
        shp.shadow.inherit = False
        x += 16; w -= 30

    box = sl.shapes.add_textbox(Emu(int(x * 12700)), Emu(int(y * 12700)),
                                Emu(int(w * 12700)), Emu(int(h * 12700)))
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = Emu(0); tf.margin_right = Emu(0)
    tf.margin_top = Emu(0); tf.margin_bottom = Emu(0)
    first = True
    for lvl, t, sz, bold, role in card.paras:
        if not t:
            p = tf.paragraphs[0] if first else tf.add_paragraph()
            p.space_after = Pt(2)
            first = False
            continue
        col = BLUE_D if role == "h3" else INK
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        p.space_after = Pt(5)
        p.line_spacing = lh(sz)
        if role == "bullet":
            pPr = p._p.get_or_add_pPr()
            pPr.set("marL", str(int(0.42 * 12700)))
            pPr.set("indent", str(int(-0.36 * 12700)))
            r = p.add_run(); r.text = "•  " + t
        else:
            r = p.add_run(); r.text = t
        r.font.size = Pt(sz); r.font.bold = bold; r.font.color.rgb = col; r.font.name = FONT
        first = False


def add_text(sl, x, y, w, h, text, sz, bold, color, align=PP_ALIGN.LEFT, font=FONT):
    box = sl.shapes.add_textbox(Emu(int(x * 12700)), Emu(int(y * 12700)),
                                Emu(int(w * 12700)), Emu(int(h * 12700)))
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = Emu(0); tf.margin_right = Emu(0)
    tf.margin_top = Emu(0); tf.margin_bottom = Emu(0)
    p = tf.paragraphs[0]
    p.alignment = align
    p.line_spacing = 1.25
    r = p.add_run(); r.text = text
    r.font.size = Pt(sz); r.font.bold = bold; r.font.color.rgb = color; r.font.name = font
    return box


def draw_table(sl, html: str, x: float, y: float, w: float) -> float:
    """绘制原生 pptx 表格，返回高度。"""
    rows = re.findall(r"<tr[^>]*>(.*?)</tr>", html, re.S)
    if not rows:
        return 0
    cols_n = 0
    for r in rows:
        cols_n = max(cols_n, len(re.findall(r"<t[dh][^>]*>", r)))
    if not cols_n:
        return 0
    n_rows = len(rows)
    graph = sl.shapes.add_table(n_rows, cols_n, Emu(int(x * 12700)), Emu(int(y * 12700)),
                                Emu(int(w * 12700)), Emu(int(40 * n_rows * 12700)))
    tb = graph.table
    row_h = 40
    for ri, r in enumerate(rows):
        cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", r, re.S)
        for ci in range(cols_n):
            cell = tb.cell(ri, ci)
            if ci < len(cells):
                txt = text_of(re.sub(r"<br\s*/?>", "\n", cells[ci]))
            else:
                txt = ""
            head = "<th" in (re.search(r"<(t[dh])[^>]*>", r).group(1) if re.search(r"<(t[dh])[^>]*>", r) else "td") == "th"
            head = ci == 0 and "<th" in r[:r.find(">") + 1] or (re.search(r"<th", r[:r.find(">") + 1]) is not None)
            tf = cell.text_frame
            tf.word_wrap = True
            tf.margin_left = Emu(int(6 * 12700)); tf.margin_right = Emu(int(6 * 12700))
            tf.margin_top = Emu(int(3 * 12700)); tf.margin_bottom = Emu(int(3 * 12700))
            p = tf.paragraphs[0]
            p.line_spacing = 1.15
            lines = txt.split("\n")
            hdr = re.match(r"<tr>\s*<th", html) and ri == 0
            if hdr or (ri == 0 and "<th" in rows[0]):
                hdr = True
            hmm = re.match(r"<tr[^>]*>", r)
            hdr = bool(re.search(r"^\s*<th", r))
            for li, ln2 in enumerate(lines):
                pp = p if li == 0 else tf.add_paragraph()
                pp.line_spacing = 1.15
                rr = pp.add_run(); rr.text = ln2
                rr.font.size = Pt(12 if not hdr else 12.5)
                rr.font.bold = bool(hdr)
                rr.font.name = FONT
                rr.font.color.rgb = WHITE if hdr else INK
            cell.fill.solid()
            cell.fill.fore_color.rgb = BLUE if hdr else WHITE
            if not hdr and ri % 2 == 0:
                cell.fill.fore_color.rgb = BG_SUB
        tb.rows[ri].height = Emu(int(row_h * 12700))
    return row_h * n_rows


def fit_scale(card: Card, width: float, avail: float) -> float:
    """若卡片估计高度超过可用高度，返回需缩小的字号比例。"""
    h0 = estimate_height(card, width)
    if h0 <= avail:
        return 1.0
    best = 0.6
    for k in range(60, 101):
        f = k / 100.0
        card2 = Card(card.kind, card.pad)
        card2.paras = [(lvl, t, sz * f, b, r) for lvl, t, sz, b, r in card.paras]
        if estimate_height(card2, width) <= avail:
            best = f
            break
    return best


def build_slide(prs, sec: str, idx: int, total: int) -> None:
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    bg = sl.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Emu(int(SLIDE_W * 12700)), Emu(int(SLIDE_H * 12700)))
    bg.fill.solid(); bg.fill.fore_color.rgb = WHITE
    bg.line.fill.background(); bg.shadow.inherit = False

    if sec.startswith('<section class="slide cover'):
        h1m = re.search(r"<h1>(.*?)</h1>", sec, re.S)
        h1 = re.sub(r"\s+", " ", text_of(h1m.group(1))) if h1m else ""
        add_text(sl, MARGIN + 60, 120, SLIDE_W - 2 * (MARGIN + 60), 240, h1, 34, True, BLUE_D,
                 align=PP_ALIGN.CENTER)
        ym = 400
        qm = re.search(r'<div class="q">(.*?)</div>', sec, re.S)
        if qm:
            add_text(sl, MARGIN + 60, ym, SLIDE_W - 2 * (MARGIN + 60), 150, text_of(qm.group(1)),
                     16, True, BLUE_D)
            ym += 180
        rm = re.search(r'<div class="rq">(.*?)</div>', sec, re.S)
        if rm:
            lines = split_top(rm.group(1))
            n = len(lines)
            for j, ln in enumerate(lines):
                t = text_of(ln)
                if not t:
                    continue
                t = re.sub(r"^(RQ[123])\s*", r"\1　", t)
                if not t.startswith("RQ"):
                    t = "　" + t
                add_text(sl, MARGIN + 60, ym + j * 34, SLIDE_W - 2 * (MARGIN + 60), 32, t, 13.5, False, INK)
        add_text(sl, SLIDE_W - MARGIN - 80, SLIDE_H - 30, 80, 22, f"{idx} / {total}", 11, False, GREY,
                 align=PP_ALIGN.RIGHT)
        return

    crumb = re.search(r'<h1 class="crumb">(.*?)</h1>', sec, re.S)
    kind, title, tag = "", "", ""
    if crumb:
        c = crumb.group(1)
        km = re.search(r"<em>(.*?)</em>", c, re.S)
        tm = re.search(r'<span class="tag">(.*?)</span>', c, re.S)
        title = text_of(km.group(1)) if km else ""
        pre = c[:km.start()] if km else c
        kind = text_of(pre)
        if tm:
            tag = text_of(tm.group(1))
    add_text(sl, MARGIN, 16, SLIDE_W - 2 * MARGIN, 44, (kind + "　" if kind else "") + title, 20, True, INK)
    ln = sl.shapes.add_shape(MSO_SHAPE.RECTANGLE, Emu(int(MARGIN * 12700)), Emu(int(60 * 12700)),
                             Emu(int((SLIDE_W - 2 * MARGIN) * 12700)), Emu(int(2.5 * 12700)))
    ln.fill.solid(); ln.fill.fore_color.rgb = BLUE; ln.line.fill.background(); ln.shadow.inherit = False
    if tag:
        w = min(260, 46 + len(tag) * 15)
        bg2 = sl.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                  Emu(int((SLIDE_W - MARGIN - w) * 12700)), Emu(int(16 * 12700)),
                                  Emu(int(w * 12700)), Emu(int(30 * 12700)))
        bg2.fill.solid(); bg2.fill.fore_color.rgb = BLUE
        bg2.line.fill.background()
        bg2.adjustments[0] = 0.5
        tfc = bg2.text_frame
        tfc.word_wrap = False
        tfc.margin_left = Emu(0); tfc.margin_right = Emu(0)
        p = tfc.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = tag
        r.font.size = Pt(11.5); r.font.color.rgb = WHITE; r.font.name = FONT

    body = sec
    bm = re.search(r'<div class="body">(.*)', sec, re.S)
    if bm:
        body = bm.group(1)
        body = re.sub(r"</div>\s*<div class=\"pg\"></div>.*$", "", body, flags=re.S)

    top = HEAD_H + 8
    avail_h = SLIDE_H - top - BOTTOM
    cur = top
    for blk in top_blocks(body):
        if not blk.strip():
            continue
        c = classify(blk)
        if c is None:
            continue
        kind_c, card = c
        w = SLIDE_W - 2 * MARGIN
        if kind_c == "table":
            h = draw_table(sl, card.table_html, MARGIN, cur, w)
            cur += h + 12
            continue
        if kind_c == "cols":
            n = max(1, len(card.cols))
            inner_w = (w - 18 * (n - 1)) / n
            used = 0
            for k, cc in enumerate(card.cols):
                avail = max(60, avail_h - (cur - top))
                hh = estimate_height(cc, inner_w)
                if hh > avail:
                    f = fit_scale(cc, inner_w, avail)
                    cc.paras = [(lvl, t, sz * f, b, r) for lvl, t, sz, b, r in cc.paras]
                    hh = estimate_height(cc, inner_w)
                draw_card(sl, cc, MARGIN + k * (inner_w + 18), cur, inner_w, hh)
                used = max(used, hh)
            cur += used + 12
            continue
        avail = max(60, avail_h - (cur - top))
        h = estimate_height(card, w)
        if h > avail:
            f = fit_scale(card, w, avail)
            card.paras = [(lvl, t, sz * f, b, r) for lvl, t, sz, b, r in card.paras]
            h = estimate_height(card, w)
        draw_card(sl, card, MARGIN, cur, w, h)
        cur += h + 12

    add_text(sl, SLIDE_W - MARGIN - 80, SLIDE_H - 30, 80, 22, f"{idx} / {total}", 11, False, GREY,
             align=PP_ALIGN.RIGHT)


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    deck = ROOT / sys.argv[1]
    out = ROOT / sys.argv[2]
    html = deck.read_text(encoding="utf-8")
    secs = re.findall(r'<section class="slide.*?</section>', html, re.S)
    prs = Presentation()
    prs.slide_width = Emu(int(SLIDE_W * 12700))
    prs.slide_height = Emu(int(SLIDE_H * 12700))
    for i, s in enumerate(secs, 1):
        build_slide(prs, s, i, len(secs))
    out.parent.mkdir(parents=True, exist_ok=True)
    prs.save(out)
    print(f"✓ {out}：{len(secs)} 页")
    return 0


if __name__ == "__main__":
    sys.exit(main())
