#!/usr/bin/env python3
"""Merge the 62 newly added references into papers_metadata.json."""
import json
import pathlib
import shutil

ROOT = pathlib.Path("/home/gezhuocheng/HUD")
META = ROOT / "papers_metadata.json"


def main():
    meta = json.load(open(META))
    manifest = json.load(open(ROOT / "scripts" / "new_papers_manifest.json"))
    have = {p.get("doi", "").lower() for p in meta if p.get("doi")}
    have_idx = {p["idx"] for p in meta}

    added = 0
    for r in manifest:
        if r["idx"] in have_idx:
            continue
        doi = (r.get("doi") or "").lower()
        if doi and doi in have:
            continue
        meta.append({
            "idx": r["idx"],
            "doi": doi,
            "title": r["title"],
            "year": r["year"],
            "authors": r.get("authors") or [],
            "venue": r.get("venue") or "",
            "is_oa": bool(r["has_pdf"]),
            "pdf_url": "",
            "landing": f"https://doi.org/{doi}" if doi else "",
            "abstract": r.get("abstract", ""),
            "local_pdf": r.get("pdf", ""),
            "local_text": r.get("text", ""),
            "has_fulltext": bool(r["has_pdf"]),
            "cited_by": r.get("cited_by"),
            "source_list": r["list"],
            "ref_key": r["key"],
        })
        added += 1

    meta.sort(key=lambda p: p["idx"])
    shutil.copy(META, str(META) + ".bak")
    json.dump(meta, open(META, "w"), ensure_ascii=False, indent=2)
    print(f"papers_metadata.json: +{added} -> {len(meta)} entries (backup .bak)")

    # consolidated download log
    log = {}
    for p in ("new_download_log.json", "list2_download_log.json"):
        log.update(json.load(open(ROOT / "scripts" / p)))
    json.dump(log, open(ROOT / "download_log_2026-08.json", "w"),
              ensure_ascii=False, indent=2)
    ok = sum(1 for v in log.values() if v["status"] == "ok")
    print(f"download_log_2026-08.json: {ok}/{len(log)} ok")


if __name__ == "__main__":
    main()
