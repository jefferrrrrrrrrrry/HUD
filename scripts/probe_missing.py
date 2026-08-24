#!/usr/bin/env python3
"""List every known location for the still-missing papers."""
import json
import pathlib
import subprocess
import urllib.parse

ROOT = pathlib.Path("/home/gezhuocheng/HUD")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")


def get(url, timeout=40):
    r = subprocess.run(["curl", "-skL", "--connect-timeout", "12", "--max-time", str(timeout),
                        "-A", UA, url], capture_output=True)
    return r.stdout.decode("utf-8", "ignore")


log = json.load(open(ROOT / "scripts" / "new_download_log.json"))
recs = {r["key"]: r for r in json.load(open(ROOT / "scripts" / "new_refs_resolved.json"))}
fails = [k for k, v in log.items() if v["status"] != "ok"]

out = {}
for k in fails:
    doi = log[k]["doi"]
    info = {"doi": doi, "locs": []}
    up = get(f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email=research@example.org")
    try:
        u = json.loads(up)
        for loc in (u.get("oa_locations") or []):
            info["locs"].append({"src": "upw", "host": loc.get("host_type"),
                                 "pdf": loc.get("url_for_pdf"), "land": loc.get("url")})
        info["journal_is_oa"] = u.get("journal_is_oa")
        info["oa_status"] = u.get("oa_status")
    except Exception:
        pass
    oa = get(f"https://api.openalex.org/works/doi:{urllib.parse.quote(doi)}")
    try:
        d = json.loads(oa)
        for loc in (d.get("locations") or []):
            info["locs"].append({"src": "oax", "pdf": loc.get("pdf_url"),
                                 "land": loc.get("landing_page_url"),
                                 "ver": loc.get("version")})
        pl = d.get("primary_location") or {}
        info["pii_or_id"] = pl.get("landing_page_url")
    except Exception:
        pass
    out[k] = info
    print(f"--- {k} [{info.get('oa_status')}] journal_oa={info.get('journal_is_oa')}")
    for l in info["locs"]:
        print("    ", l)

json.dump(out, open(ROOT / "scripts" / "missing_locations.json", "w"),
          ensure_ascii=False, indent=2)
