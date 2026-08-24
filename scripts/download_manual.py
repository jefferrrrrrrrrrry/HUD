#!/usr/bin/env python3
"""Second pass: download the still-missing papers from manually located URLs."""
import json
import pathlib
import sys

sys.path.insert(0, "/home/gezhuocheng/HUD/scripts")
from download_new import try_pdf, fetch_text, scrape_pdf_urls, is_pdf, PAPERS

ROOT = pathlib.Path("/home/gezhuocheng/HUD")

MANUAL = {
    # list 2
    "phan_thesis": [
        "https://theses.hal.science/tel-01508528/file/These_UTC_Minh_Tien_Phan.pdf",
        "https://theses.hal.science/tel-01508528/document",
    ],
    "char_thesis": [
        "https://amu.hal.science/tel-03058542/document",
        "https://amu.hal.science/tel-03058542/file/Thesismanuscrit-Francois-CHAR-Version-n2.pdf",
    ],
    "schall_thesis": [
        "https://stacks.cdc.gov/view/cdc/222159/cdc_222159_DS1.pdf",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC3875361/pdf/nihms-419504.pdf",
        "https://europepmc.org/api/fulltextRepo?pprId=PMC3875361&type=FILE&fileName=EMS55621-pdf.pdf",
    ],
    "bao2024crowd": [
        "https://pdf.hanspub.org/ap2024148_271134899.pdf",
    ],
    "cangut2026intent": [
        "https://cetra.grad.hr/archive/cetra2026papers/1849.pdf",
    ],
    "takada_decel": [
        "https://scispace.com/pdf/effectiveness-of-forward-obstacles-collision-warning-system-4zqs85zlcu.pdf",
    ],
    "kang2016ttc": [
        "https://koreascience.kr/article/JAKO201634574282667.pdf",
        "https://journal.ksiop.or.kr/index.php/KJIOP/article/view/99",
        "https://koreascience.kr/article/JAKO201634574282667.page",
    ],
    "attc2025": [
        "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6351998",
    ],
    "joo2024rate": [
        "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4927850",
    ],
    "sun2023rl": ["https://ascelibrary.org/doi/pdf/10.1061/9780784484869.024"],
    "zhangy2023path": [],
    "miyoshi2005sae": [],
    "saej2400": [],
    "abe2004": [],
    "chang2013bus": [],
    # list 1 leftovers worth another try
    "park2013eff": [
        "https://ksp.etri.re.kr/ksp/article/read?id=12463",
        "https://link.springer.com/content/pdf/10.1007/978-3-642-39238-2_43.pdf",
    ],
    "cheng2023trip": [
        "https://www.sciencedirect.com/science/article/pii/S2590198223000143/pdfft",
        "https://doaj.org/article/7d4a377b3cad4121bdd718191f7948aa",
    ],
    "zhu2025sal": [
        "https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=11079581",
    ],
}


def main():
    logs = {
        "1": ROOT / "scripts" / "new_download_log.json",
        "2": ROOT / "scripts" / "list2_download_log.json",
    }
    data = {k: json.load(open(p)) for k, p in logs.items()}
    only = sys.argv[1:] or None

    for which, log in data.items():
        for key, entry in log.items():
            if entry["status"] == "ok":
                continue
            if only and key not in only:
                continue
            urls = MANUAL.get(key) or []
            if not urls:
                continue
            dest = PAPERS / entry["file"]
            got, how = False, ""
            for u in urls:
                if u.lower().endswith(".pdf") or "pdfft" in u or "stamp" in u:
                    got, how = try_pdf(u, dest)
                    if got:
                        break
                html = fetch_text(u, timeout=60) or fetch_text(u, proxy=True, timeout=60)
                if html:
                    for pu in scrape_pdf_urls(html, u)[:8]:
                        got, how = try_pdf(pu, dest, referer=u)
                        if got:
                            break
                if got:
                    break
            if got:
                entry["status"] = "ok"
                entry["src"] = "manual " + how
            print(f"[{which}] {key}: {'OK  ' + how[:80] if got else 'still FAIL'}")
        json.dump(log, open(logs[which], "w"), ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
