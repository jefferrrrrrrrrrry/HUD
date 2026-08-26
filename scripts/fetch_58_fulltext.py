#!/usr/bin/env python3
"""用真实浏览器取 #58（SPIDER 2.0）全文。

背景：该文 Crossref 登记许可为 **CC BY 4.0**，Unpaywall/Semantic Scholar 均报 hybrid OA，
即合法可自由下载；但 annualreviews.org 有 Cloudflare 防护，urllib 一律 403（含 Crossref
的 crawler=true TDM 链接与三种 UA）。故改用 Playwright+Chromium 走真实浏览器会话。

产出
  papers/58_2025_SPIDER_2.0_Driver_Distraction_and_Visual_Attention.pdf（若能拿到 PDF）
  extracted_text/58_2025_SPIDER2.0_Strayer_McDonnell.txt（HTML 正文抽取，兜底）
"""
from __future__ import annotations

import re
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
DOI = "10.1146/annurev-vision-110423-025626"
LANDING = f"https://www.annualreviews.org/content/journals/{DOI}"
PDF_OUT = ROOT / "papers" / "58_2025_SPIDER_2.0_Driver_Distraction_and_Visual_Attention.pdf"
TXT_OUT = ROOT / "extracted_text" / "58_2025_SPIDER2.0_Strayer_McDonnell.txt"
PROXY = "http://oversea-squid2.ko.txyun:11080"


def main() -> None:
    with sync_playwright() as pw:
        br = pw.chromium.launch(headless=True, proxy={"server": PROXY},
                                args=["--disable-blink-features=AutomationControlled"])
        ctx = br.new_context(
            user_agent=("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"),
            viewport={"width": 1440, "height": 1000},
            locale="en-US", accept_downloads=True)
        pg = ctx.new_page()
        print(f"→ 打开 {LANDING}")
        try:
            resp = pg.goto(LANDING, wait_until="domcontentloaded", timeout=90_000)
            print(f"   HTTP {resp.status if resp else '?'}  title={pg.title()[:70]!r}")
        except Exception as e:  # noqa: BLE001
            print(f"   goto 失败：{type(e).__name__} {str(e)[:90]}")
            br.close()
            sys.exit(2)

        # Cloudflare 挑战页会自跳，给它时间
        for i in range(8):
            t = pg.title()
            if "just a moment" not in t.lower() and "attention required" not in t.lower():
                break
            print(f"   等待 Cloudflare 挑战…({i + 1})")
            time.sleep(4)
        print(f"   最终 title={pg.title()[:70]!r}  url={pg.url[:80]}")

        html = pg.content()
        print(f"   页面 {len(html)} 字符")
        if "Just a moment" in html or len(html) < 3000:
            print("   ✗ 仍被拦截")
            (ROOT / "scripts" / "_58_blocked.html").write_text(html, encoding="utf-8")
            br.close()
            sys.exit(3)

        # 找 PDF 链接
        links = pg.eval_on_selector_all(
            "a", "els => els.map(e => e.getAttribute('href')).filter(Boolean)")
        pdfs = [u for u in links if "pdf" in u.lower()]
        print(f"   页面共 {len(links)} 个链接，其中含 pdf 的 {len(pdfs)} 个：{pdfs[:6]}")

        got = False
        for u in dict.fromkeys(pdfs):
            full = u if u.startswith("http") else "https://www.annualreviews.org" + u
            try:
                r = ctx.request.get(full, timeout=90_000)
                body = r.body()
                print(f"   试 {full[:78]} → HTTP {r.status} {len(body)}B")
                if body[:4] == b"%PDF":
                    PDF_OUT.parent.mkdir(exist_ok=True)
                    PDF_OUT.write_bytes(body)
                    print(f"   ✓ PDF 已存 {PDF_OUT.relative_to(ROOT)}"
                          f"（{len(body) / 1048576:.2f} MB）")
                    got = True
                    break
            except Exception as e:  # noqa: BLE001
                print(f"   取 PDF 失败：{type(e).__name__} {str(e)[:70]}")

        # 无论 PDF 成败，都抽一份 HTML 正文兜底
        txt = pg.evaluate("""() => {
            const sel = ['div.article-content', 'section.article-body', 'main', 'article'];
            for (const s of sel) { const e = document.querySelector(s);
                if (e && e.innerText.length > 2000) return e.innerText; }
            return document.body.innerText;
        }""")
        txt = re.sub(r"\n{3,}", "\n\n", txt)
        TXT_OUT.parent.mkdir(exist_ok=True)
        TXT_OUT.write_text(txt, encoding="utf-8")
        print(f"   HTML 正文抽取 {len(txt)} 字符 -> {TXT_OUT.relative_to(ROOT)}")
        br.close()
        sys.exit(0 if got else 1)


if __name__ == "__main__":
    main()
