#!/usr/bin/env python3
"""用 Playwright 逐页截图《文献综述_幻灯片.html》并检测内容溢出。

溢出判据：幻灯片内 .body 的 scrollHeight > clientHeight（正文超出可视区）
或任一子元素右/下边界越出 1280×720 版心。
输出 figures/slides_shots/p01.png … 与一份 overflow 报告。
"""
from __future__ import annotations

import asyncio
import json
from pathlib import Path

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "文献综述_幻灯片.html"
OUT = ROOT / "figures" / "slides_shots"

PROBE = """
() => {
  const el = document.querySelector('.slide.on');
  const b = el.querySelector('.body') || el;
  const r = el.getBoundingClientRect();
  let worst = 0, who = '';
  el.querySelectorAll('*').forEach(n => {
    const q = n.getBoundingClientRect();
    const d = Math.max(q.bottom - r.bottom, q.right - r.right);
    if (d > worst) { worst = d; who = n.tagName + '.' + (n.className || ''); }
  });
  return {
    idx: [...document.querySelectorAll('.slide')].indexOf(el) + 1,
    scrollH: b.scrollHeight, clientH: b.clientHeight,
    overflowPx: Math.round(worst), who: who.slice(0, 46),
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
    (ROOT / "figures" / "slides_overflow.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\n溢出页 {len(bad)} / {len(report)}")
    for r in bad:
        print(f"  p{r['idx']:02d} +{r['over']}px  {r['who']}")


if __name__ == "__main__":
    asyncio.run(main())
