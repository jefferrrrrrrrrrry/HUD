#!/usr/bin/env python3
"""Build a manifest of all newly added papers: idx, key, title, files, status."""
import json
import pathlib
import re

ROOT = pathlib.Path("/home/gezhuocheng/HUD")
PAPERS = ROOT / "papers"
TEXTS = ROOT / "extracted_text"
SUMM = ROOT / "summaries"


def load(p):
    return json.load(open(ROOT / "scripts" / p)) if (ROOT / "scripts" / p).exists() else {}


def main():
    l1_log = load("new_download_log.json")
    l2_log = load("list2_download_log.json")
    l1_res = {r["key"]: r for r in load("new_refs_resolved.json")}
    l2_res = load("list2_resolved.json")
    l1_abs = load("missing_abstracts.json")
    l2_abs = load("list2_missing_abstracts.json")

    rows = []
    for log, res, absd, src in ((l1_log, l1_res, l1_abs, "list1"),
                                (l2_log, l2_res, l2_abs, "list2")):
        for key, v in log.items():
            r = res.get(key, {})
            a = absd.get(key, {})
            pdf = PAPERS / v["file"]
            txt = TEXTS / (pathlib.Path(v["file"]).stem + ".txt")
            rows.append({
                "idx": v["idx"], "key": key, "list": src,
                "doi": v.get("doi") or r.get("doi") or "",
                "title": r.get("cr_title") or r.get("title") or a.get("title"),
                "year": r.get("cr_year") or r.get("year") or a.get("year"),
                "venue": r.get("cr_venue") or a.get("venue") or "",
                "authors": r.get("cr_authors") or r.get("authors") or a.get("authors"),
                "cited_by": r.get("cited_by") or a.get("cited_by")
                            or a.get("cited_by_count"),
                "pdf": str(pdf) if pdf.exists() else "",
                "text": str(txt) if txt.exists() else "",
                "text_chars": txt.stat().st_size if txt.exists() else 0,
                "has_pdf": v["status"] == "ok",
                "abstract": a.get("abstract", "") or re.sub(r"<[^>]+>", " ",
                                                            r.get("abstract", "") or ""),
                "abstract_source": a.get("abstract_source", "crossref"),
            })
    rows.sort(key=lambda x: x["idx"])
    json.dump(rows, open(ROOT / "scripts" / "new_papers_manifest.json", "w"),
              ensure_ascii=False, indent=2)
    okp = sum(1 for r in rows if r["has_pdf"])
    print(f"manifest: {len(rows)} entries, {okp} with PDF, {len(rows)-okp} abstract-only")
    for r in rows:
        flag = "PDF " if r["has_pdf"] else "ABS "
        print(f"  {r['idx']:3d} {flag}{r['key']:20s} {(r['title'] or '')[:62]}")


if __name__ == "__main__":
    main()
