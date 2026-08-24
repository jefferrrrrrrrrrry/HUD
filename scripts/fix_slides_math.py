#!/usr/bin/env python3
"""修《文献综述_幻灯片.html》两处渲染缺陷。

1. 裸 LaTeX：正文有 60 处 `$...$`，浏览器不渲染，截图确认显示为字面量
   （如「$t_0$ 分布」「$PRT_{p95}$」）。此处不引 KaTeX（要联网，破坏单文件
   离线可用），改为就地转成原生 HTML 上下标 + Unicode 数学符号。
   排版约定：单个拉丁字母与希腊字母作变量 → 斜体；数字、运算符、下标词、
   2 个以上字母的大写缩写（PRT/BTN/PPV/SPIDER）与函数名 → 正体。
2. 页码：`.pg` 原为硬编码，第 30/31 页换序后错位（显示 31、30），末页写成
   「34 / 34」。改为清空 DOM 值、由 JS 按实际下标写入。

幂等：`data-math-fixed` 标记存在则跳过第 1 项。
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "文献综述_幻灯片.html"

SYM = {
    r"\dot\theta": "θ\u0307", r"\Delta": "Δ", r"\approx": "≈", r"\leq": "≤",
    r"\geq": "≥", r"\cdot": "·", r"\sum": "Σ", r"\times": "×",
    r"\theta": "θ", r"\tau": "τ", r"\delta": "δ", r"\pi": "π",
    r"\min": "min", r"\max": "max",
}
FUNCS = ("min", "max", "log", "exp", "sin", "cos")
# 正体字符集：数字、标点、运算符。&lt; / &gt; 先用哨兵占位，避免破坏 HTML 实体。
UPRIGHT = set("0123456789.,≈≤≥·Σ×√=+-−±/*()[]|%'\" \u0001\u0002")

MATH_CSS = """
/* 行内数学：原生上下标 + Unicode，不依赖 KaTeX，保证单文件离线可用 */
.m{font-family:"Cambria Math","Latin Modern Math","Times New Roman",serif;font-style:italic}
.m sub,.m sup{font-style:normal;font-size:.7em;line-height:0}
.m .up{font-style:normal}
"""

PG_JS = """
  slides.forEach((el,k)=>{const p=el.querySelector('.pg');
    if(p)p.textContent=(k+1)+' / '+slides.length;});
"""


def _sqrt(s: str) -> str:
    """把 \\sqrt{...} 换成 √(...)，支持嵌套花括号。"""
    while (k := s.find("\\sqrt{")) != -1:
        i, depth = k + 6, 1
        while i < len(s) and depth:
            depth += {"{": 1, "}": -1}.get(s[i], 0)
            i += 1
        assert depth == 0, f"\\sqrt 花括号不配对：{s!r}"
        s = s[:k] + "√(" + s[k + 6:i - 1] + ")" + s[i:]
    return s


def to_html(expr: str) -> str:
    """把一段 $...$ 的内容转成 <span class="m">…</span>。

    实现要点：先把 HTML 实体换成哨兵，再逐字符切分成「正体段 / 斜体段 /
    上下标」，**最后一次性**拼接并还原实体——绝不在已生成的 HTML 串上做
    运算符替换（那会把刚插入的 </sub> 里的 `/` 再次改写）。
    """
    s = expr.replace("&lt;", "\u0001").replace("&gt;", "\u0002")
    s = _sqrt(s)
    for k in sorted(SYM, key=len, reverse=True):
        s = s.replace(k, SYM[k])
    # LaTeX 里 `\Delta t` 的空格只是命令分隔符，渲染时应贴紧作 Δt
    s = re.sub(r"([ΔΣθτδπ\u0307]) +(?=[A-Za-z])", r"\1", s)
    assert "\\" not in s, f"未登记的 LaTeX 命令：{expr!r}"

    out: list[str] = []
    i, n = 0, len(s)
    while i < n:
        c = s[i]
        if c in "_^":                                   # 上下标
            tag = "sub" if c == "_" else "sup"
            i += 1
            if i < n and s[i] == "{":
                j = s.index("}", i)
                body, i = s[i + 1:j], j + 1
            else:
                body, i = s[i], i + 1
            out.append(f"<{tag}>{body}</{tag}>")
        elif c in UPRIGHT:                              # 数字与运算符成组
            j = i
            while j < n and s[j] in UPRIGHT:
                j += 1
            out.append(f'<span class="up">{s[i:j]}</span>')
            i = j
        else:                                           # 变量名
            j = i
            while j < n and s[j] not in UPRIGHT and s[j] not in "_^":
                j += 1
            run = s[i:j]
            up = (len(run) > 1 and run.isupper()) or run.lower() in FUNCS
            out.append(f'<span class="up">{run}</span>' if up else run)
            i = j
    body = "".join(out).replace("\u0001", "&lt;").replace("\u0002", "&gt;")
    return f'<span class="m">{body}</span>'


def main() -> None:
    s = HTML.read_text("utf-8")

    if "data-math-fixed" in s:
        print("SKIP 数学转写（已处理）")
    else:
        # 只在 <script> 之前替换：JS 模板字面量 `${s}` 不是数学
        cut = s.rindex("<script>")
        head, tail = s[:cut], s[cut:]
        assert head.count("$") % 2 == 0, f"$ 数量为奇数（{head.count('$')}）"
        seen: set[str] = set()

        def rep(m: re.Match) -> str:
            seen.add(m.group(1))
            return to_html(m.group(1))

        head, cnt = re.subn(r"\$([^$\n]{1,80})\$", rep, head)
        assert "$" not in head, \
            f"仍有残留 $（表达式超长？）：{re.findall(r'.{30}[$].{30}', head)[:3]}"
        # 自检：不得出现被二次改写的标签
        for bad in ("</span>\"up\"", "</sub>=", "</sup>≥", "<sub>=</sub>"):
            assert bad not in head, f"标签被二次改写：{bad}"
        head = head.replace("</style>", MATH_CSS + "</style>", 1)
        head = head.replace("<body>", '<body data-math-fixed="1">', 1)
        s = head + tail
        print(f"OK   数学转写 {cnt} 处（{len(seen)} 个不同表达式）")

    hard = re.findall(r'<div class="pg">[^<]+</div>', s)
    s = re.sub(r'<div class="pg">[^<]*</div>', '<div class="pg"></div>', s)
    if PG_JS.strip() not in s:
        assert "function show(n){" in s, "未找到 show() 函数"
        s = s.replace("function show(n){", "function show(n){" + PG_JS, 1)
        print(f"OK   页码改为 JS 生成（清掉 {len(hard)} 处硬编码）")
    else:
        print("SKIP 页码（已由 JS 生成）")

    HTML.write_text(s, "utf-8")
    print(f"\n{HTML.name} 已更新，共 {len(re.findall(r'<section', s))} 页")


if __name__ == "__main__":
    main()
