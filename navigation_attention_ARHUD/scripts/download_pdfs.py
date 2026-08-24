#!/usr/bin/env python3
"""Batch download PDFs for navigation_attention_ARHUD project via Sci-Hub mirrors."""
import json
import os
import re
import time
import subprocess
import pathlib

ROOT = pathlib.Path("/home/gezhuocheng/moe/HUD/navigation_attention_ARHUD")
PAPERS_DIR = ROOT / "papers"
META_FILE = ROOT / "metadata_filtered.json"
LOG_FILE = ROOT / "download_log.json"

PROXY = "http://oversea-squid2.ko.txyun:11080"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

MIRRORS = [
    "sci-hub.ren",
    "www.tesble.com",
    "sci-hub.ru",
    "sci-hub.st",
    "sci-hub.box",
]

def safe_filename(idx, year, title):
    title_clean = re.sub(r"[^\w\s-]", "", title).strip()
    title_clean = re.sub(r"\s+", "_", title_clean)[:100]
    return f"{idx:02d}_{year}_{title_clean}.pdf"

def curl(url, output=None, follow=True, ua=UA, referer=None, timeout=30):
    cmd = ["curl", "-sk", "--connect-timeout", "10", "--max-time", str(timeout),
           "-A", ua,
           "-x", PROXY]
    if follow:
        cmd.append("-L")
    if referer:
        cmd += ["-H", f"Referer: {referer}"]
    if output:
        cmd += ["-o", output]
    cmd.append(url)
    return subprocess.run(cmd, capture_output=True, text=False)

def fetch_text(url, referer=None, timeout=25):
    r = curl(url, referer=referer, timeout=timeout)
    if r.returncode != 0:
        return None, r.returncode
    try:
        return r.stdout.decode("utf-8", errors="ignore"), 0
    except Exception:
        return r.stdout.decode("latin-1", errors="ignore"), 0

def find_pdf_url(html, mirror):
    if not html:
        return None
    patterns = [
        r'src="(//[^"]+\.pdf[^"]*)"',
        r'src="(https?://[^"]+\.pdf[^"]*)"',
        r"location\.href='(https?:\\?/\\?/[^']+\.pdf[^']*)'",
        r'embed[^>]+src="([^"]+\.pdf[^"]*)"',
        r'iframe[^>]+src="([^"]+\.pdf[^"]*)"',
    ]
    for pat in patterns:
        m = re.search(pat, html, re.IGNORECASE)
        if m:
            url = m.group(1).replace("\\/", "/")
            if url.startswith("//"):
                url = "https:" + url
            return url
    if "ddos-guard" in html.lower() or "challenge" in html.lower():
        return "DDOS_BLOCKED"
    return None

def download_pdf_url(pdf_url, output_path, referer):
    r = curl(pdf_url, output=output_path, referer=referer, timeout=60)
    if r.returncode != 0:
        return False, f"curl rc={r.returncode}"
    if not os.path.exists(output_path) or os.path.getsize(output_path) < 5000:
        return False, "file too small"
    with open(output_path, "rb") as f:
        sig = f.read(8)
    if not sig.startswith(b"%PDF"):
        os.remove(output_path)
        return False, f"not pdf: {sig[:8]!r}"
    return True, f"OK ({os.path.getsize(output_path)} bytes)"

def try_mirror(doi, mirror):
    url = f"https://{mirror}/{doi}"
    html, _ = fetch_text(url)
    if not html:
        return None, "fetch fail"
    pdf_url = find_pdf_url(html, mirror)
    if pdf_url == "DDOS_BLOCKED":
        return None, "ddos blocked"
    if not pdf_url:
        if "article not found" in html.lower():
            return None, "article not found"
        return None, "no pdf url"
    return pdf_url, "ok"

def main():
    with open(META_FILE) as f:
        data = json.load(f)
    records = data['records']
    print(f"待下载: {len(records)} 篇")
    PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    
    log = {}
    if LOG_FILE.exists():
        with open(LOG_FILE) as f:
            log = json.load(f)
    
    succ_count = 0
    fail_count = 0
    for idx, p in enumerate(records, 1):
        doi = p.get('doi', '')
        if not doi:
            log[str(idx)] = {"success": False, "doi": "", "reason": "no DOI"}
            fail_count += 1
            continue
        # 已下载?
        if str(idx) in log and log[str(idx)].get("success"):
            succ_count += 1
            continue
        
        fname = safe_filename(idx, p.get('year', ''), p.get('title', ''))
        out = PAPERS_DIR / fname
        if out.exists() and out.stat().st_size > 50000:
            log[str(idx)] = {"success": True, "doi": doi, "file": fname, "via": "existing"}
            succ_count += 1
            continue
        
        print(f"\n[{idx:02d}/{len(records)}] DOI={doi[:60]}")
        print(f"   Title: {p['title'][:80]}")
        success = False
        attempts = []
        for mirror in MIRRORS:
            pdf_url, err = try_mirror(doi, mirror)
            attempts.append({"mirror": mirror, "err": err})
            if not pdf_url:
                continue
            ok, msg = download_pdf_url(pdf_url, str(out), referer=f"https://{mirror}/")
            attempts[-1]["dl"] = msg
            if ok:
                print(f"  ✓ {mirror} → {msg}")
                log[str(idx)] = {"success": True, "doi": doi, "file": fname, "via": mirror, "pdf_url": pdf_url}
                success = True
                succ_count += 1
                break
        
        if not success:
            print(f"  ✗ All mirrors failed")
            log[str(idx)] = {"success": False, "doi": doi, "attempts": attempts, "title": p['title']}
            fail_count += 1
        
        # 每5篇保存一次log
        if idx % 5 == 0:
            with open(LOG_FILE, "w") as f:
                json.dump(log, f, indent=2, ensure_ascii=False)
        time.sleep(0.5)
    
    with open(LOG_FILE, "w") as f:
        json.dump(log, f, indent=2, ensure_ascii=False)
    
    print(f"\n=== Summary ===")
    print(f"成功: {succ_count}/{len(records)}")
    print(f"失败: {fail_count}/{len(records)}")

if __name__ == "__main__":
    main()
