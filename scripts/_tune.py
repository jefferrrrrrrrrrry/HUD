#!/usr/bin/env python3
"""讲述页排版宽松化：加 .lo 修饰类，参数页四行等高分布，消除版心下方大片留白。"""
import re
from pathlib import Path

P = Path("研究汇报_2026_08.html")
s = P.read_text(encoding="utf-8")

s = s.replace("技术可行不等同于人因有效。", "技术可行不等同于人因收益。")

CSS = """/* 讲述页宽松排版：内容少的页面放大字号与行距，填满版心 */
.slide.lo li{font-size:15.6px;line-height:2.04;margin-bottom:9px}
.slide.lo .box{padding:15px 18px}
.slide.lo .box h3{font-size:16px;margin-bottom:11px;padding-bottom:8px}
.slide.lo .def{font-size:15.6px;line-height:1.82;padding:13px 17px}
.slide.lo .warn,.slide.lo .ok,.slide.lo .note{font-size:14.4px;line-height:1.8;padding:12px 16px}
.slide.lo p{font-size:15.2px;line-height:1.92}
.slide.lo p.small{font-size:14.6px;line-height:1.88}
.slide.lo table{font-size:14px}
.slide.lo th{padding:9px 11px;font-size:14px}
.slide.lo td{padding:10px 11px}
.slide.lo table.mini{font-size:12.6px}
.slide.lo table.mini td{padding:6px 8px}
.slide.lo table.mini th{padding:7px 8px;font-size:12.6px}
.slide.lo .cite{font-size:13px}
/* 参数页：四行等高分布 */
.p4 .row{flex:1 1 0;align-items:center}
.p4 .tx{font-size:16.4px;line-height:1.8}
"""
s = s.replace('.m{font-family:', CSS + '.m{font-family:')

secs = list(re.finditer(r'<section class="slide(?P<cls>[^"]*)"', s))
assert len(secs) == 24, len(secs)
# 讲述页 p02–p14 加 .lo（p01 为封面，p15 起为备查页）
for m in reversed(secs[1:14]):
    s = s[:m.start()] + f'<section class="slide lo{m.group("cls")}"' + s[m.end():]

P.write_text(s, encoding="utf-8")
print("✓ 已加 .lo 至 p02–p14，并修正一处效应表述")
