#!/usr/bin/env python3
"""Harvest richest available abstract/metadata for papers whose PDF could not be fetched.

Sources: Semantic Scholar -> Europe PMC -> OpenAlex inverted index -> DOAJ -> Crossref
"""
import json
import pathlib
import re
import subprocess
import time
import urllib.parse

ROOT = pathlib.Path("/home/gezhuocheng/HUD")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")


def get(url, timeout=45):
    r = subprocess.run(["curl", "-skL", "--connect-timeout", "12", "--max-time", str(timeout),
                        "-A", UA, url], capture_output=True)
    return r.stdout.decode("utf-8", "ignore")


def strip_tags(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    return re.sub(r"\s+", " ", s).strip()


def s2(doi):
    txt = get("https://api.semanticscholar.org/graph/v1/paper/DOI:"
              f"{urllib.parse.quote(doi)}?fields=abstract,tldr,title,venue,year,"
              "authors,citationCount,referenceCount,fieldsOfStudy,publicationTypes")
    try:
        return json.loads(txt)
    except Exception:
        return {}


def epmc(doi):
    txt = get("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query="
              f"DOI:%22{urllib.parse.quote(doi)}%22&resultType=core&format=json")
    try:
        res = json.loads(txt)["resultList"]["result"]
        return res[0] if res else {}
    except Exception:
        return {}


def openalex_abs(doi):
    txt = get(f"https://api.openalex.org/works/doi:{urllib.parse.quote(doi)}")
    try:
        d = json.loads(txt)
    except Exception:
        return "", {}
    inv = d.get("abstract_inverted_index")
    abs_txt = ""
    if inv:
        pos = {}
        for w, idxs in inv.items():
            for i in idxs:
                pos[i] = w
        abs_txt = " ".join(pos[k] for k in sorted(pos))
    extra = {
        "cited_by_count": d.get("cited_by_count"),
        "concepts": [c["display_name"] for c in (d.get("concepts") or [])[:8]],
        "topics": [t["display_name"] for t in (d.get("topics") or [])[:5]],
        "referenced_works_count": len(d.get("referenced_works") or []),
    }
    return abs_txt, extra


def doaj_abs(doi):
    txt = get("https://doaj.org/api/search/articles/doi:"
              f"{urllib.parse.quote(doi)}")
    try:
        res = json.loads(txt).get("results") or []
        if res:
            return res[0]["bibjson"].get("abstract", "")
    except Exception:
        pass
    return ""


def main():
    log = json.load(open(ROOT / "scripts" / "new_download_log.json"))
    recs = {r["key"]: r for r in json.load(open(ROOT / "scripts" / "new_refs_resolved.json"))}
    out = {}
    for k, v in log.items():
        if v["status"] == "ok":
            continue
        doi = v["doi"]
        rec = {"key": k, "doi": doi, "idx": v["idx"],
               "title": recs[k].get("cr_title") or recs[k]["title"],
               "year": recs[k].get("cr_year"), "venue": recs[k].get("cr_venue"),
               "authors": recs[k].get("cr_authors"),
               "cited_by": recs[k].get("cited_by")}
        cands = {}
        cands["crossref"] = strip_tags(recs[k].get("abstract"))
        d = s2(doi)
        cands["s2"] = d.get("abstract") or ""
        rec["tldr"] = ((d.get("tldr") or {}).get("text") or "")
        rec["s2_citations"] = d.get("citationCount")
        e = epmc(doi)
        cands["epmc"] = e.get("abstractText") or ""
        rec["pmid"] = e.get("pmid")
        rec["keywords"] = e.get("keywordList", {}).get("keyword") if e else None
        oa_abs, extra = openalex_abs(doi)
        cands["openalex"] = oa_abs
        rec.update(extra)
        cands["doaj"] = doaj_abs(doi)
        best_src = max(cands, key=lambda s: len(strip_tags(cands[s])))
        rec["abstract"] = strip_tags(cands[best_src])
        rec["abstract_source"] = best_src if rec["abstract"] else "none"
        rec["abstract_all"] = {s: strip_tags(t) for s, t in cands.items() if t}
        out[k] = rec
        print(f"{k:16s} {rec['abstract_source']:9s} len={len(rec['abstract']):5d} "
              f"cit={rec.get('cited_by_count')} pmid={rec.get('pmid')}")
        time.sleep(0.5)
    json.dump(out, open(ROOT / "scripts" / "missing_abstracts.json", "w"),
              ensure_ascii=False, indent=2)
    print(f"\nwrote {len(out)}")


if __name__ == "__main__":
    main()
