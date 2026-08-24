#!/usr/bin/env python3
"""Batch fetch papers via Jina AI Reader (r.jina.ai) - bypasses Akamai/Cloudflare for many sites."""
import json
import os
import re
import time
import urllib.parse
import subprocess
import pathlib

ROOT = pathlib.Path("/home/gezhuocheng/HUD")
TEXT_DIR = ROOT / "extracted_text"
LOG_FILE = ROOT / "jina_log.json"

PROXY = "http://oversea-squid2.ko.txyun:11080"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

def safe_name(idx, year, title):
    title_clean = re.sub(r"[^\w\s-]", "", title).strip()
    title_clean = re.sub(r"\s+", "_", title_clean)[:80]
    return f"{idx:02d}_{year}_{title_clean}"

def jina_fetch(url, timeout=60):
    """Fetch URL via Jina Reader. Returns (markdown_text, status)."""
    jina_url = f"https://r.jina.ai/{url}"
    cmd = ["curl", "-sk", "--connect-timeout", "15", "--max-time", str(timeout),
           "-A", UA, "-x", PROXY, "-L", jina_url]
    r = subprocess.run(cmd, capture_output=True)
    if r.returncode != 0:
        return None, f"curl rc={r.returncode}"
    try:
        text = r.stdout.decode("utf-8", errors="ignore")
    except Exception:
        text = r.stdout.decode("latin-1", errors="ignore")
    if len(text) < 500:
        return None, f"too small ({len(text)} bytes)"
    if "Title:" not in text and "# " not in text and "Markdown Content" not in text:
        return None, "no markdown content"
    return text, "ok"

def main():
    with open(ROOT / "papers_metadata.json") as f:
        meta = json.load(f)

    # Still missing from sci-hub
    still_missing = [7, 8, 9, 12, 19, 23, 24, 27, 31, 32, 36]
    targets = [p for p in meta if p["idx"] in still_missing]

    log = {}
    if LOG_FILE.exists():
        with open(LOG_FILE) as f:
            log = json.load(f)

    for p in targets:
        idx = p["idx"]
        if str(idx) in log and log[str(idx)].get("success"):
            print(f"[{idx:02d}] already done")
            continue
        # Pick best URL: prefer alt_oa_urls then pdf_url
        candidates = []
        for k in ("alt_oa_urls", "all_oa_pdf_urls"):
            for u in p.get(k, []):
                if u: candidates.append(u)
        if p.get("pdf_url"):
            candidates.append(p["pdf_url"])
        # Always include landing
        candidates.append(p["landing"])
        # Add abstract page for MDPI (in case PDF link fails)
        for u in candidates[:]:
            if "/pdf" in u and "mdpi.com" in u:
                candidates.append(u.split("/pdf")[0])
        candidates = list(dict.fromkeys(candidates))  # dedupe preserving order

        out_name = safe_name(idx, p["year"], p["title"])
        out_md = TEXT_DIR / f"{out_name}.md"
        out_txt = TEXT_DIR / f"{out_name}.txt"

        print(f"\n[{idx:02d}] {p['title'][:70]}")
        print(f"  candidates: {len(candidates)}")
        success = False
        attempts = []
        for url in candidates:
            print(f"  Trying: {url[:90]}")
            text, status = jina_fetch(url)
            attempts.append({"url": url, "status": status, "size": len(text) if text else 0})
            if text:
                # Save as markdown
                out_md.write_text(text, encoding="utf-8")
                # Also write txt for compatibility
                out_txt.write_text(text, encoding="utf-8")
                size = len(text)
                print(f"  ✓ Saved {size} chars to {out_name}.md")
                log[str(idx)] = {
                    "success": True,
                    "doi": p["doi"],
                    "url": url,
                    "size": size,
                    "via": "jina"
                }
                success = True
                break
            else:
                print(f"  ✗ {status}")
            time.sleep(1)
        if not success:
            log[str(idx)] = {"success": False, "doi": p["doi"], "attempts": attempts}
        with open(LOG_FILE, "w") as f:
            json.dump(log, f, indent=2, ensure_ascii=False)
        time.sleep(2)

    print("\n=== Summary ===")
    succ = sum(1 for v in log.values() if v.get("success"))
    print(f"Success: {succ} / {len(targets)}")

if __name__ == "__main__":
    main()
