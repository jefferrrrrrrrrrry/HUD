#!/usr/bin/env python3
"""用 Playwright 逐页截图《文献综述_幻灯片.html》并检测内容溢出。

溢出判据：幻灯片内 .body 的 scrollHeight > clientHeight（正文超出可视区）
或任一子元素右/下边界越出 1280×720 版心。
输出 figures/slides_shots/p01.png … 与一份 overflow 报告。
"""
from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "文献综述_幻灯片.html")
OUT = ROOT / "figures" / (sys.argv[2] if len(sys.argv) > 2 else "slides_shots")

PROBE = """
() => {
  const el = document.querySelector('.slide.on');
  const b = el.querySelector('.body') || el;
  let worst = 0, who = '';
  const bump = (d, n, tag) => {
    if (d > worst) { worst = d; who = tag + ' ' + n.tagName + '.' + (n.className || ''); }
  };
  // ① 版心：任何元素不得越出 1280×720
  const rs = el.getBoundingClientRect();
  el.querySelectorAll('*').forEach(n => {
    const q = n.getBoundingClientRect();
    if (q.width < 1 && q.height < 1) return;
    bump(Math.max(q.bottom - rs.bottom, q.right - rs.right), n, 'slide');
  });
  // ② 容器：子孙不得越出各自的布局容器（网格/弹性子项越界会被静默裁掉或互相压盖）
  el.querySelectorAll('.body, .cols2, .cols3, .cols4, .box, figure, .vs').forEach(c => {
    const rc = c.getBoundingClientRect();
    c.querySelectorAll('*').forEach(n => {
      const q = n.getBoundingClientRect();
      if (q.width < 1 && q.height < 1) return;
      if (getComputedStyle(n).position === 'absolute') return;
      bump(Math.max(q.bottom - rc.bottom, q.right - rc.right), n, 'in-' + (c.className || c.tagName));
    });
  });
  return {
    idx: [...document.querySelectorAll('.slide')].indexOf(el) + 1,
    scrollH: b.scrollHeight, clientH: b.clientHeight,
    overflowPx: Math.round(worst), who: who.slice(0, 58),
    title: (el.querySelector('h1') || {}).innerText || ''
  };
}
"""


async def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    report = []
    async with async_playwright() as pw:
        br = await pw.chromium.launch(args=["--font-render-hinting=none"])
        pg = await br.new_page(viewport={"width": 1330, "height": 748},
                               device_scale_factor=2)
        await pg.goto(HTML.as_uri())
        await pg.wait_for_timeout(700)
        n = await pg.evaluate("document.querySelectorAll('.slide').length")
        print(f"共 {n} 页")
        for k in range(1, n + 1):
            await pg.evaluate(f"show({k - 1})")
            await pg.wait_for_timeout(230)
            info = await pg.evaluate(PROBE)
            el = await pg.query_selector(".slide.on")
            await el.screenshot(path=str(OUT / f"p{k:02d}.png"))
            over = max(info["scrollH"] - info["clientH"], info["overflowPx"])
            flag = "⚠" if over > 2 else " "
            report.append({**info, "over": over})
            t = info["title"].replace("\n", " ")[:48]
            print(f"{flag} p{k:02d}  溢出 {over:>4} px  {t}")
        await br.close()
    bad = [r for r in report if r["over"] > 2]
    (ROOT / "figures" / f"{OUT.name}_overflow.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\n溢出页 {len(bad)} / {len(report)}")
    for r in bad:
        print(f"  p{r['idx']:02d} +{r['over']}px  {r['who']}")


if __name__ == "__main__":
    asyncio.run(main())
