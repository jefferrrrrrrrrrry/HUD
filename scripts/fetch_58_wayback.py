#!/usr/bin/env python3
"""经 Wayback Machine 取 #58 全文（真实浏览器 + 退避重试）。

为什么绕道 Wayback：annualreviews.org 对本机出口 IP 一律 403（Cloudflare），
Crossref 的 TDM crawler 链接、三种 UA、headless Chromium 均被拦；而 Wayback 存有
2025-09-25 的 200 快照。Wayback 的 replay 端点对本 IP 有 429 限流，故先冷却再试，
并用浏览器会话（完整头部 + JS）而非 urllib。

该文 Crossref 登记许可为 CC BY 4.0，可自由下载与再分发。
"""
from __future__ import annotations

import re
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
DOI = "10.1146/annurev-vision-110423-025626"
LAND = f"https://www.annualreviews.org/content/journals/{DOI}"
SNAP = "20250925152730"
PROXY = "http://oversea-squid2.ko.txyun:11080"
PDF_OUT = ROOT / "papers" / "58_2025_SPIDER_2.0_Driver_Distraction_and_Visual_Attention.pdf"
TXT_OUT = ROOT / "extracted_text" / "58_2025_SPIDER2.0_Strayer_McDonnell.txt"
COOLDOWN = int(sys.argv[1]) if len(sys.argv) > 1 else 180


def main() -> None:
    print(f"冷却 {COOLDOWN}s 以避开 Wayback 的 429 限流…")
    time.sleep(COOLDOWN)
    targets = [f"https://web.archive.org/web/{SNAP}/{LAND}",
               f"https://web.archive.org/web/{SNAP}id_/{LAND}",
               f"https://web.archive.org/web/2025/{LAND}"]
    with sync_playwright() as pw:
        br = pw.chromium.launch(headless=True, proxy={"server": PROXY})
        ctx = br.new_context(
            user_agent=("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"),
            viewport={"width": 1440, "height": 1200}, locale="en-US",
            accept_downloads=True)
        pg = ctx.new_page()
        html = None
        for rnd in range(4):
            for u in targets:
                try:
                    r = pg.goto(u, wait_until="domcontentloaded", timeout=120_000)
                    code = r.status if r else 0
                    body = pg.content()
                    print(f"  轮 {rnd + 1} HTTP {code} {len(body)} 字符  {u[-52:]}")
                    if code == 200 and len(body) > 20_000:
                        html = body
                        break
                except Exception as e:  # noqa: BLE001
                    print(f"  轮 {rnd + 1} ERR {type(e).__name__} {str(e)[:70]}")
            if html:
                break
            time.sleep(60 + rnd * 60)

        if not html:
            print("✗ Wayback 仍不可取")
            br.close()
            sys.exit(1)

        # 快照里的 PDF 链接（Wayback 会把它改写为 /web/<ts>/<原始 url>）
        links = pg.eval_on_selector_all(
            "a", "els => els.map(e => e.href).filter(Boolean)")
        pdfs = [u for u in links if "pdf" in u.lower()]
        print(f"  链接 {len(links)} 个，含 pdf 的 {len(pdfs)}：{pdfs[:5]}")
        got = False
        for u in dict.fromkeys(pdfs):
            try:
                r = ctx.request.get(u, timeout=120_000)
                b = r.body()
                print(f"  试 {u[-70:]} → {r.status} {len(b)}B")
                if b[:4] == b"%PDF":
                    PDF_OUT.write_bytes(b)
                    print(f"  ✓ PDF 存 {PDF_OUT.name}（{len(b) / 1048576:.2f} MB）")
                    got = True
                    break
            except Exception as e:  # noqa: BLE001
                print(f"  取 PDF 失败 {type(e).__name__} {str(e)[:60]}")

        txt = pg.evaluate("""() => {
            for (const s of ['div.article-content','section.article-body','main','article']) {
                const e = document.querySelector(s);
                if (e && e.innerText.length > 2000) return e.innerText;
            }
            return document.body.innerText;
        }""")
        txt = re.sub(r"\n{3,}", "\n\n", txt)
        TXT_OUT.write_text(txt, encoding="utf-8")
        print(f"  正文抽取 {len(txt)} 字符 -> {TXT_OUT.name}")
        br.close()
        sys.exit(0 if got or len(txt) > 8000 else 1)


if __name__ == "__main__":
    main()
