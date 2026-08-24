#!/usr/bin/env python3
"""Resolve + download PDFs for list 2 (风险时机判断 论文清单).

Handles arXiv, HAL / institutional theses, MDPI, PLoS, SAE, IGI, IEEE, SSRN.
Falls back to Sci-Hub mirrors, then records abstract-only metadata.
"""
import json
import os
import pathlib
import re
import subprocess
import sys
import time
import urllib.parse

sys.path.insert(0, "/home/gezhuocheng/HUD/scripts")
from reflist2 import REFS2, SKIP_KEYS
from download_new import (curl, fetch_text, is_pdf, try_pdf, scrape_pdf_urls,
                          scihub, openalex_links, s2_links, publisher_links,
                          safe_name, PAPERS)

ROOT = pathlib.Path("/home/gezhuocheng/HUD")
RESOLVED = ROOT / "scripts" / "list2_resolved.json"
LOG = ROOT / "scripts" / "list2_download_log.json"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
START_IDX = 70


def crossref(doi):
    txt = fetch_text(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}")
    try:
        return json.loads(txt)["message"]
    except Exception:
        return None


def crossref_search(title):
    q = urllib.parse.quote(title[:150])
    txt = fetch_text(f"https://api.crossref.org/works?query.bibliographic={q}&rows=3")
    try:
        return json.loads(txt)["message"]["items"]
    except Exception:
        return []


def arxiv_meta(aid):
    txt = fetch_text(f"http://export.arxiv.org/api/query?id_list={aid}")
    d = {}
    m = re.search(r"<title>(.*?)</title>", txt, re.S)
    ts = re.findall(r"<title>(.*?)</title>", txt, re.S)
    if len(ts) > 1:
        d["title"] = re.sub(r"\s+", " ", ts[1]).strip()
    m = re.search(r"<summary>(.*?)</summary>", txt, re.S)
    if m:
        d["abstract"] = re.sub(r"\s+", " ", m.group(1)).strip()
    d["authors"] = re.findall(r"<name>(.*?)</name>", txt)
    m = re.search(r"<published>(\d{4})", txt)
    if m:
        d["year"] = int(m.group(1))
    return d


def extra_candidates(r):
    out = []
    if r.get("arxiv"):
        a = r["arxiv"]
        out.append(f"https://arxiv.org/pdf/{a}")
        out.append(f"https://arxiv.org/pdf/{a}v1")
    d = (r.get("doi") or "").lower()
    if d.startswith("10.1371/"):
        out.append("https://journals.plos.org/plosone/article/file?id="
                   f"{r['doi']}&type=printable")
    if d.startswith("10.12677/"):
        out.append(f"https://www.hanspub.org/journal/PaperDownload.aspx?DOI={r['doi']}")
    if d.startswith("10.54941/"):
        out.append(f"https://openaccess.cms-conferences.org/publications/book/"
                   f"978-1-958651-70-2/article/{r['doi']}")
    if d.startswith("10.17077/"):
        out.append("https://iro.uiowa.edu/view/delivery/01IOWA_INST/"
                   "12730425100002771/13730424830002771")
    if r.get("url"):
        out.append(r["url"])
    return out


def hal_pdf(landing):
    """HAL theses: landing/document is the PDF."""
    if "hal.science" in landing or "theses.hal" in landing:
        return [landing.rstrip("/") + "/document", landing.rstrip("/") + "/file/index.pdf"]
    return []


def main():
    only = sys.argv[1:] or None
    log = json.load(open(LOG)) if LOG.exists() else {}
    resolved = json.load(open(RESOLVED)) if RESOLVED.exists() else {}

    targets = [r for r in REFS2 if r["key"] not in SKIP_KEYS]
    for i, r in enumerate(targets):
        idx = START_IDX + i
        key = r["key"]
        if only and key not in only:
            continue
        rec = dict(r, idx=idx)
        if key in resolved:
            rec.update({k: v for k, v in resolved[key].items() if k not in rec or not rec[k]})
        doi = r.get("doi") or ""

        if not rec.get("cr_title"):
            cr = crossref(doi) if doi else None
            if cr is None and not r.get("arxiv"):
                items = crossref_search(r["title"])
                if items:
                    cr = items[0]
            if cr:
                rec["cr_title"] = (cr.get("title") or [""])[0]
                rec["cr_doi"] = cr.get("DOI")
                rec["cr_year"] = cr.get("issued", {}).get("date-parts", [[None]])[0][0]
                rec["cr_venue"] = (cr.get("container-title") or [""])[0]
                rec["cr_authors"] = [f"{a.get('given','')} {a.get('family','')}".strip()
                                     for a in cr.get("author", [])]
                rec["cited_by"] = cr.get("is-referenced-by-count")
                rec["abstract"] = re.sub(r"<[^>]+>", " ", cr.get("abstract", "") or "")
            if r.get("arxiv"):
                am = arxiv_meta(r["arxiv"])
                rec.setdefault("cr_title", am.get("title"))
                rec["abstract"] = rec.get("abstract") or am.get("abstract", "")
                rec["cr_year"] = rec.get("cr_year") or am.get("year")
                rec["cr_authors"] = rec.get("cr_authors") or am.get("authors")
                rec["cr_venue"] = rec.get("cr_venue") or "arXiv preprint"

        title = rec.get("cr_title") or r["title"]
        year = rec.get("cr_year") or r["year"]
        dest = PAPERS / safe_name(idx, year, title)
        rec["filename"] = dest.name
        resolved[key] = rec

        if dest.exists() and is_pdf(dest):
            log[key] = {"idx": idx, "doi": doi, "file": dest.name, "status": "ok",
                        "src": log.get(key, {}).get("src", "already")}
            print(f"[{idx}] {key}: already present")
            continue

        cands = extra_candidates(r)
        cands += hal_pdf(r.get("url", ""))
        if doi:
            cands += publisher_links(doi)
            cands += s2_links(doi)
            cands += openalex_links(doi)
        seen, ordered = set(), []
        for u in cands:
            if u and u not in seen:
                seen.add(u)
                ordered.append(u)

        got, how = False, ""
        for u in ordered:
            got, how = try_pdf(u, dest)
            if got:
                break
        if not got:
            for u in ordered:
                if u.lower().endswith(".pdf"):
                    continue
                html = fetch_text(u, timeout=45) or fetch_text(u, proxy=True, timeout=45)
                if not html:
                    continue
                for pu in scrape_pdf_urls(html, u)[:6]:
                    got, how = try_pdf(pu, dest)
                    if got:
                        break
                if got:
                    break
        if not got and doi:
            got, how = scihub(doi, dest)

        log[key] = {"idx": idx, "doi": doi, "file": dest.name,
                    "status": "ok" if got else "fail", "src": how}
        print(f"[{idx}] {key}: {'OK  ' + how[:70] if got else 'FAIL'}")
        json.dump(log, open(LOG, "w"), ensure_ascii=False, indent=2)
        json.dump(resolved, open(RESOLVED, "w"), ensure_ascii=False, indent=2)

    json.dump(log, open(LOG, "w"), ensure_ascii=False, indent=2)
    json.dump(resolved, open(RESOLVED, "w"), ensure_ascii=False, indent=2)
    ok = sum(1 for v in log.values() if v["status"] == "ok")
    print(f"\ndone: {ok}/{len(log)} ok")


if __name__ == "__main__":
    main()
