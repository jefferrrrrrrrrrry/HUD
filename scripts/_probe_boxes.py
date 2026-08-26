#!/usr/bin/env python3
"""量出指定页每个 .box 的 scrollHeight 与可用高度，定位真正超高的那一栏。"""
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / sys.argv[1]
PAGES = [int(x) for x in sys.argv[2:]] or [1]

PROBE = """
() => {
  const el = document.querySelector('.slide.on');
  const body = el.querySelector('.body');
  const out = [];
  el.querySelectorAll('.box, table, .ok, .warn, .note, .def').forEach(n => {
    out.push({
      cls: (n.className || n.tagName).slice(0, 22),
      h: n.getBoundingClientRect().height,
      sh: n.scrollHeight, ch: n.clientHeight,
      head: (n.querySelector('h3') || n).innerText.split('\\n')[0].slice(0, 18)
    });
  });
  return {bodyH: body.clientHeight, bodySH: body.scrollHeight, items: out};
}
"""


async def main() -> None:
    async with async_playwright() as pw:
        br = await pw.chromium.launch()
        pg = await br.new_page(viewport={"width": 1330, "height": 748})
        await pg.goto(HTML.as_uri())
        await pg.wait_for_timeout(600)
        for k in PAGES:
            await pg.evaluate(f"show({k - 1})")
            await pg.wait_for_timeout(200)
            r = await pg.evaluate(PROBE)
            print(f"\n== p{k:02d}  body {r['bodyH']} / scroll {r['bodySH']}")
            for it in r["items"]:
                over = it["sh"] - it["ch"]
                flag = "⚠" if over > 2 else " "
                print(f" {flag} {it['cls']:<24} h={it['h']:7.1f} sh={it['sh']:>5} ch={it['ch']:>5}  {it['head']}")
        await br.close()


asyncio.run(main())
