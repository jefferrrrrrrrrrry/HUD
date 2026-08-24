#!/usr/bin/env python3
"""Multi-source PDF downloader for the new AR-HUD reference list.

Order of attempts:
  1. Unpaywall / OpenAlex / Semantic Scholar OA pdf links
  2. Publisher heuristics (MDPI, IEEE stamp, Springer, ACM, SPIE, Wiley pdfdirect)
  3. Sci-Hub mirrors (sci-hub.ren, tesble.com) via oversea proxy
"""
import json
import os
import pathlib
import re
import subprocess
import sys
import time
import urllib.parse

ROOT = pathlib.Path("/home/gezhuocheng/HUD")
PAPERS = ROOT / "papers"
RESOLVED = ROOT / "scripts" / "new_refs_resolved.json"
LOG = ROOT / "scripts" / "new_download_log.json"

PROXY = "http://oversea-squid2.ko.txyun:11080"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
MIRRORS = ["sci-hub.ren", "www.tesble.com", "sci-hub.usualwant.com", "wellesu.com",
           "sci-hub.et-fine.com", "sci-hub.mksa.top", "sci-hub.box"]
MIN_SIZE = 30 * 1024


def curl(url, out=None, referer=None, proxy=False, timeout=300, head=False, plain=False):
    cmd = ["curl", "-skL", "--connect-timeout", "15", "--max-time", str(timeout)]
    if not plain:
        cmd += ["-A", UA,
                "-H", "Accept: text/html,application/xhtml+xml,application/pdf,*/*"]
    if proxy:
        cmd += ["-x", PROXY]
    if referer:
        cmd += ["-H", f"Referer: {referer}"]
    if head:
        cmd.append("-I")
    if out:
        cmd += ["-o", str(out)]
    cmd.append(url)
    return subprocess.run(cmd, capture_output=True)


def fetch_text(url, proxy=False, referer=None, timeout=60, plain=False):
    r = curl(url, referer=referer, proxy=proxy, timeout=timeout, plain=plain)
    if r.returncode != 0:
        return ""
    return r.stdout.decode("utf-8", errors="ignore")


def is_pdf(path):
    p = pathlib.Path(path)
    if not p.exists() or p.stat().st_size < MIN_SIZE:
        return False
    with open(p, "rb") as f:
        head = f.read(1024)
    return head[:5] == b"%PDF-" or b"%PDF-" in head


def try_pdf(url, dest, referer=None, proxy=False):
    tmp = str(dest) + ".part"
    attempts = [(proxy, False)] if proxy else [(False, False), (True, False),
                                               (False, True), (True, True)]
    for use_proxy, plain in attempts:
        r = curl(url, out=tmp, referer=referer, proxy=use_proxy, plain=plain)
        if is_pdf(tmp):
            os.replace(tmp, dest)
            tag = ("proxy" if use_proxy else "direct") + ("/plain" if plain else "")
            return True, f"{tag} {url[:90]}"
    if os.path.exists(tmp):
        os.remove(tmp)
    return False, ""


def openalex_links(doi):
    txt = fetch_text(f"https://api.openalex.org/works/doi:{urllib.parse.quote(doi)}")
    urls = []
    try:
        d = json.loads(txt)
    except Exception:
        return urls
    for loc in (d.get("locations") or []):
        for k in ("pdf_url", "landing_page_url"):
            u = loc.get(k)
            if u:
                urls.append(u)
    return urls


def s2_links(doi):
    txt = fetch_text(
        "https://api.semanticscholar.org/graph/v1/paper/DOI:"
        f"{urllib.parse.quote(doi)}?fields=openAccessPdf,externalIds,title")
    try:
        d = json.loads(txt)
    except Exception:
        return []
    out = []
    oa = d.get("openAccessPdf") or {}
    if oa.get("url"):
        out.append(oa["url"])
    return out


def publisher_links(doi, landing=""):
    d = doi.lower()
    out = []
    if d.startswith("10.3390/"):
        slug = d.split("/", 1)[1]
        out.append(f"https://www.mdpi.com/{slug}/pdf")
    if d.startswith("10.1109/"):
        m = re.search(r"\.(\d{7,8})$", d)
        if m:
            arn = m.group(1)
            out.append(f"https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber={arn}")
    if d.startswith("10.1007/"):
        out.append(f"https://link.springer.com/content/pdf/{doi}.pdf")
    if d.startswith("10.1145/"):
        out.append(f"https://dl.acm.org/doi/pdf/{doi}")
    if d.startswith("10.1002/"):
        out.append(f"https://onlinelibrary.wiley.com/doi/pdfdirect/{doi}")
    if d.startswith("10.1080/"):
        out.append(f"https://www.tandfonline.com/doi/epdf/{doi}")
    if d.startswith("10.1117/"):
        out.append(f"https://www.spiedigitallibrary.org/conference-proceedings-of-spie/"
                   f"article-pdf/doi/{doi}")
    if landing and landing.endswith(".pdf"):
        out.append(landing)
    return out


PDF_PATTERNS = [
    r'src\s*=\s*["\']([^"\']+\.pdf[^"\']*)["\']',
    r'href\s*=\s*["\']([^"\']*(?:download|pdf)[^"\']*\.pdf[^"\']*)["\']',
    r'citation_pdf_url"\s+content="([^"]+)"',
    r'location\.href\s*=\s*["\']([^"\']+\.pdf[^"\']*)["\']',
    r'<embed[^>]+src="([^"]+)"',
    r'<iframe[^>]+src="([^"]+)"',
]


def scrape_pdf_urls(html, base):
    found = []
    for pat in PDF_PATTERNS:
        for m in re.findall(pat, html, re.I):
            u = m.replace("&amp;", "&").strip()
            if u.startswith("//"):
                u = "https:" + u
            elif u.startswith("/"):
                pr = urllib.parse.urlparse(base)
                u = f"{pr.scheme}://{pr.netloc}{u}"
            elif not u.startswith("http"):
                u = urllib.parse.urljoin(base, u)
            if u not in found:
                found.append(u)
    return found


def scihub(doi, dest):
    for direct in (f"https://sci.bban.top/pdf/{doi}.pdf",
                   f"https://zero.sci-hub.se/pdf/{doi}.pdf"):
        ok, how = try_pdf(direct, dest, proxy=True)
        if ok:
            return True, f"bban {how}"
    for mirror in MIRRORS:
        base = f"https://{mirror}"
        url = f"{base}/{doi}"
        html = fetch_text(url, proxy=True, timeout=60)
        if not html or len(html) < 200:
            continue
        for u in scrape_pdf_urls(html, base):
            ok, how = try_pdf(u, dest, referer=url, proxy=True)
            if ok:
                return True, f"scihub[{mirror}] {how}"
    return False, ""


def safe_name(idx, year, title):
    t = re.sub(r"[^\w\s-]", "", title).strip()
    t = re.sub(r"\s+", "_", t)[:80]
    return f"{idx:02d}_{year}_{t}.pdf"


def main():
    recs = json.load(open(RESOLVED))
    log = json.load(open(LOG)) if LOG.exists() else {}
    start_idx = 41
    only = sys.argv[1:] or None

    for i, r in enumerate(recs):
        idx = start_idx + i
        key = r["key"]
        if only and key not in only:
            continue
        doi = r.get("cr_doi") or r["doi"]
        title = r.get("cr_title") or r["title"]
        year = r.get("cr_year") or r["year"]
        dest = PAPERS / safe_name(idx, year, title)
        r["idx"] = idx
        r["filename"] = dest.name
        if dest.exists() and is_pdf(dest):
            print(f"[{idx}] {key}: already present")
            log[key] = {"idx": idx, "file": dest.name, "status": "ok", "src": log.get(key, {}).get("src", "pre-existing")}
            continue

        cands = []
        cands += [u for u in [r.get("oa_pdf")] if u]
        cands += r.get("oa_all") or []
        cands += publisher_links(doi, r.get("oa_landing", ""))
        cands += s2_links(doi)
        cands += openalex_links(doi)

        seen, ordered = set(), []
        for u in cands:
            if u and u not in seen:
                seen.add(u)
                ordered.append(u)

        got, how = False, ""
        for u in ordered:
            if u.lower().endswith(".pdf") or "/pdf" in u.lower() or "stamp" in u.lower():
                got, how = try_pdf(u, dest, referer=r.get("oa_landing") or None)
                if got:
                    break
        if not got:
            for u in ordered:
                if u.lower().endswith(".pdf"):
                    continue
                html = fetch_text(u, timeout=45)
                if not html:
                    html = fetch_text(u, proxy=True, timeout=45)
                if not html:
                    continue
                for pu in scrape_pdf_urls(html, u)[:6]:
                    got, how = try_pdf(pu, dest, referer=u)
                    if got:
                        break
                if got:
                    break
        if not got:
            got, how = scihub(doi, dest)

        log[key] = {"idx": idx, "doi": doi, "file": dest.name,
                    "status": "ok" if got else "fail", "src": how}
        print(f"[{idx}] {key}: {'OK  ' + how[:70] if got else 'FAIL'}")
        with open(LOG, "w") as f:
            json.dump(log, f, ensure_ascii=False, indent=2)

    with open(RESOLVED, "w") as f:
        json.dump(recs, f, ensure_ascii=False, indent=2)
    ok = sum(1 for v in log.values() if v["status"] == "ok")
    print(f"\ndone: {ok}/{len(log)} ok")


if __name__ == "__main__":
    main()
