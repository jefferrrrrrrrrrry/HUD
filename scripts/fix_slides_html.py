#!/usr/bin/env python3
"""对《文献综述_幻灯片.html》做三处修订并渲染截图验收。

修订
  1. 调页序：把「研究假设（2.5.3）」提到「研究框架图（2.5.4）」之前
  2. 补 @media print，使浏览器「打印为 PDF」时一页一张 1280×720 横向幻灯片
  3. 末尾追加一页「参考文献（本讲稿主引 24 篇）」

幂等：已改过的项跳过。
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "文献综述_幻灯片.html"

PRINT_CSS = """
/* 打印为 PDF：一页一张幻灯片，横向 1280×720 */
@page{size:1280px 720px;margin:0}
@media print{
  body{background:#fff;display:block;overflow:visible}
  #stage{width:auto;height:auto;display:block}
  #nav,#hud,#hint{display:none!important}
  .slide{position:static!important;display:flex!important;transform:none!important;
    box-shadow:none;page-break-after:always;break-after:page;margin:0}
  .slide:last-child{page-break-after:auto;break-after:auto}
}
"""

# 主引文献：取综述中作为参数锚点或冲突裁定依据的条目
KEY_REFS = [102, 71, 44, 8, 69, 99, 100, 87, 86, 1, 54, 62, 78, 58, 12, 53,
            52, 48, 60, 43, 65, 59, 97, 84]


def reorder(s: str) -> str:
    """把「31 假设」整块移到「30 研究框架图」之前。"""
    if s.index("<!-- 31 假设 -->") < s.index("<!-- 30 研究框架图 -->"):
        print("SKIP 页序（已调整）")
        return s
    pat = r"(<!-- 30 研究框架图 -->.*?</section>\s*)(<!-- 31 假设 -->.*?</section>\s*)"
    m = re.search(pat, s, re.S)
    assert m, "未匹配到第 30/31 页整块"
    s = s[:m.start()] + m.group(2) + m.group(1) + s[m.end():]
    # 注释里的序号一并互换，便于后续维护对读
    s = s.replace("<!-- 31 假设 -->", "<!-- 30 假设 -->", 1)
    s = s.replace("<!-- 30 研究框架图 -->", "<!-- 31 研究框架图 -->", 1)
    print("OK   页序：假设(2.5.3) 前移至 研究框架图(2.5.4) 之前")
    return s


def add_print_css(s: str) -> str:
    if "@media print" in s:
        print("SKIP 打印样式（已存在）")
        return s
    s = s.replace("</style>", PRINT_CSS + "</style>", 1)
    print("OK   已补 @media print")
    return s


def add_refs_page(s: str) -> str:
    if "id=\"refs\"" in s:
        print("SKIP 参考文献页（已存在）")
        return s
    apa = json.loads((ROOT / "scripts" / "apa_refs.json").read_text("utf-8"))
    items = sorted(({"k": k, **apa[str(k)]} for k in KEY_REFS),
                   key=lambda d: (d["sort_key"][0], d["sort_key"][1]))
    li = "\n".join(
        f'  <li>{r["apa"].replace("*", "")}</li>' for r in items)
    page = f"""
<!-- 34 参考文献 -->
<section class="slide" id="refs">
<h1 class="crumb">文献综述<em>参考文献：本讲稿主引 {len(items)} 篇</em><span class="tag">2.6</span></h1>
<div class="body">
<p class="cite">APA 第 7 版。完整 102 条见《第2章_文献综述_v2.md》文末参考文献表与
《HUD_AR-HUD_行人预警_文献综合表.csv》的「★APA条目」列。</p>
<ol class="refs">
{li}
</ol>
</div>
<div class="pg">34 / 34</div>
</section>
"""
    css = """
.refs{margin-left:18px;columns:2;column-gap:24px;font-size:9.3px;line-height:1.44}
.refs li{font-size:9.3px;line-height:1.44;margin-bottom:4px;break-inside:avoid;color:#333}
"""
    s = s.replace("</style>", css + "</style>", 1)
    anchor = "</section>\n\n</div>\n\n<div id=\"nav\">"
    assert anchor in s, "未找到 #stage 结束标记"
    s = s.replace(anchor, "</section>\n" + page + "\n</div>\n\n<div id=\"nav\">", 1)
    print(f"OK   已追加参考文献页（{len(items)} 条）")
    return s


def main() -> None:
    s = HTML.read_text("utf-8")
    s = reorder(s)
    s = add_print_css(s)
    s = add_refs_page(s)
    HTML.write_text(s, "utf-8")
    n = len(re.findall(r"<section\b", s))
    print(f"\n共 {n} 页 -> {HTML.name}")


if __name__ == "__main__":
    main()
