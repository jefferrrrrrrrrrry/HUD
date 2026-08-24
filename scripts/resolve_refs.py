#!/usr/bin/env python3
"""Verify DOIs via Crossref + query Unpaywall for OA PDF links."""
import json
import pathlib
import subprocess
import sys
import time
import urllib.parse

sys.path.insert(0, "/home/gezhuocheng/HUD/scripts")
from reflist_new import REFS

ROOT = pathlib.Path("/home/gezhuocheng/HUD")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
EMAIL = "research@example.org"


def get(url, timeout=30):
    cmd = ["curl", "-skL", "--connect-timeout", "12", "--max-time", str(timeout), "-A", UA, url]
    r = subprocess.run(cmd, capture_output=True)
    return r.stdout.decode("utf-8", errors="ignore")


def crossref(doi):
    txt = get(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}")
    try:
        return json.loads(txt)["message"]
    except Exception:
        return None


def crossref_search(title):
    q = urllib.parse.quote(title[:150])
    txt = get(f"https://api.crossref.org/works?query.bibliographic={q}&rows=3")
    try:
        return json.loads(txt)["message"]["items"]
    except Exception:
        return []


def unpaywall(doi):
    txt = get(f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={EMAIL}")
    try:
        return json.loads(txt)
    except Exception:
        return None


def main():
    meta = json.load(open(ROOT / "papers_metadata.json"))
    have_dois = {p.get("doi", "").lower() for p in meta}
    out = []
    for r in REFS:
        if r["doi"].lower() in have_dois:
            continue
        rec = dict(r)
        cr = crossref(r["doi"])
        if cr is None:
            items = crossref_search(r["title"])
            if items:
                cr = items[0]
                rec["doi_fixed"] = cr.get("DOI")
        if cr:
            rec["cr_title"] = (cr.get("title") or [""])[0]
            rec["cr_year"] = (cr.get("issued", {}).get("date-parts", [[None]])[0][0])
            rec["cr_venue"] = (cr.get("container-title") or [""])[0]
            rec["cr_type"] = cr.get("type")
            rec["cr_authors"] = [
                f"{a.get('given','')} {a.get('family','')}".strip() for a in cr.get("author", [])
            ]
            rec["cr_doi"] = cr.get("DOI")
            rec["cited_by"] = cr.get("is-referenced-by-count")
            rec["abstract"] = cr.get("abstract", "")
        doi_use = rec.get("cr_doi") or r["doi"]
        up = unpaywall(doi_use)
        if up:
            rec["is_oa"] = up.get("is_oa")
            loc = up.get("best_oa_location") or {}
            rec["oa_pdf"] = loc.get("url_for_pdf") or ""
            rec["oa_landing"] = loc.get("url") or ""
            rec["oa_all"] = [
                l.get("url_for_pdf") for l in (up.get("oa_locations") or []) if l.get("url_for_pdf")
            ]
        out.append(rec)
        status = "OA" if rec.get("is_oa") else "--"
        crok = "cr:ok" if rec.get("cr_title") else "cr:MISS"
        print(f"{rec['key']:18s} {crok:8s} {status} {rec.get('oa_pdf','')[:80]}")
        time.sleep(0.4)

    with open(ROOT / "scripts" / "new_refs_resolved.json", "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"\nwrote {len(out)} records")


if __name__ == "__main__":
    main()
