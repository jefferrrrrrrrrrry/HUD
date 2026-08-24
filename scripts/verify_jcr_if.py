#!/usr/bin/env python3
"""核验 build_master_csv.py 的 VENUE 表里每个「Q? (IF x.x)」是否与 WoS 官方数据一致。

数据源：wos-journal.info（Web of Science / JCR 数据镜像，按 ISSN 与刊名检索）。
判定：JCR 以 JIF 百分位 75 / 50 / 25 为 Q1 / Q2 / Q3 / Q4 的分界。
输出：逐刊对照，末尾汇总不一致者；本脚本只报告，不自动改写 VENUE。
"""
from __future__ import annotations

import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_master_csv import FALLBACK, VENUE  # noqa: E402

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}
CACHE = ROOT / "scripts" / "_wos_journal_cache.json"
SNAP = ROOT / "scripts" / "_jcr_verified.json"   # 离线快照，供 verify_deliverables 复用


def norm(s: str) -> str:
    s = html.unescape(s).lower()
    s = s.replace("&", " and ").replace("–", "-").replace("—", "-").replace("‐", "-")
    s = re.sub(r"\b(the|of|for)\b", " ", s)
    return re.sub(r"[^a-z0-9]+", "", s)


def get(url: str, cache: dict) -> str:
    if url in cache:
        return cache[url]
    for attempt in range(3):
        try:
            b = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=45)
            t = b.read().decode("utf-8", "replace")
            cache[url] = t
            time.sleep(0.7)
            return t
        except Exception as e:  # noqa: BLE001
            if attempt == 2:
                cache[url] = ""
                print(f"     ! 取页失败 {type(e).__name__} {str(e)[:60]}")
                return ""
            time.sleep(2)
    return ""


FIELDS = {
    "abbr": r"Abbreviation:\s*([^:]+?)\s+ISSN:",
    "issn": r"\bISSN:\s*([\dXx-]+)",
    "category": r"Category:\s*(.+?)\s+WoS Core Citation Indexes:",
    "index": r"WoS Core Citation Indexes:\s*(\S+)",
    "jif": r"Journal Impact Factor \(JIF\):\s*([\d.]+|N/A)",
    "jif5": r"5-year Impact Factor:\s*([\d.]+|N/A)",
    "best": r"Best ranking:\s*(.+?)\s+║",
    "pct": r"Percentage rank:\s*([\d.]+)%",
}


def parse(page: str) -> dict | None:
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", page, flags=re.S)
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))
    if "Abbreviation:" not in t:
        return None
    title = re.search(r"WoS Journal Info » (.+?) Abbreviation:", t)
    out = {"title": (title.group(1).strip() if title else "")}
    for k, pat in FIELDS.items():
        m = re.search(pat, t)
        out[k] = m.group(1).strip() if m else None
    return out


def quartile(pct: str | None) -> str | None:
    if not pct:
        return None
    p = float(pct)
    return "Q1" if p >= 75 else "Q2" if p >= 50 else "Q3" if p >= 25 else "Q4"


def main() -> None:
    cache = json.loads(CACHE.read_text("utf-8")) if CACHE.exists() else {}
    pool = dict(VENUE)
    for _idx, (short, jcr) in FALLBACK.items():
        if re.match(r"Q[1-4] \(IF [\d.]+\)", jcr):
            pool[short] = (short, jcr)          # 键即刊名，如 "Human Factors"
    targets, seen = {}, set()
    for k, v in pool.items():
        if not re.match(r"Q[1-4] \(IF [\d.]+\)", v[1]):
            continue
        if norm(k) in seen:                      # 破折号变体键指向同一刊，只核一次
            continue
        seen.add(norm(k))
        targets[k] = v
    print(f"待核 {len(targets)} 刊（VENUE 表中带数值 IF 且标了分区者）\n")
    bad, unknown, snap = [], [], {}
    for name, (short, jcr) in targets.items():
        rec_q = jcr[:2]
        rec_if = float(re.search(r"IF ([\d.]+)", jcr).group(1))
        # 镜像站检索对破折号敏感：两种写法都试，合并候选
        ids: list[str] = []
        for query in dict.fromkeys([name, re.sub(r"[-–—‐]", " ", name)]):
            s = get("https://wos-journal.info/?jsearch=" + urllib.parse.quote(query), cache)
            ids += [x for x in re.findall(r"/journalid/(\d+)", s) if x not in ids]
        ids = ids[:8]
        hit = None
        for jid in ids:
            info = parse(get(f"https://wos-journal.info/journalid/{jid}", cache))
            if info and (norm(name) in norm(info["title"])
                         or norm(info["title"]) in norm(name)):
                hit = info
                break
        if hit is None:
            print(f"?  {short:24s} 记 {rec_q} IF {rec_if} —— 检索未命中同名刊（候选 {ids}）")
            unknown.append(short)
            continue
        wq, wif = quartile(hit["pct"]), hit["jif"]
        snap[name] = {"short": short, "wos_title": hit["title"], "index": hit["index"],
                      "category": hit["best"], "percentile": hit["pct"],
                      "jif": wif, "jif_5y": hit["jif5"], "quartile": wq,
                      "recorded": jcr}
        ok_if = wif not in (None, "N/A") and abs(float(wif) - rec_if) <= 0.15
        ok_q = wq is None or wq == rec_q
        flag = "✓" if (ok_if and ok_q) else "✗"
        print(f"{flag}  {short:24s} 记 {rec_q} IF {rec_if:<5} | WoS {wq or '?'} "
              f"JIF {wif} 5y {hit['jif5']} 百分位 {hit['pct']}% | {hit['best']} ({hit['index']})")
        if flag == "✗":
            bad.append((short, rec_q, rec_if, wq, wif, hit["best"], hit["pct"],
                        hit["title"], hit["jif5"]))
    CACHE.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")
    SNAP.write_text(json.dumps(
        {"_source": "wos-journal.info（Web of Science / JCR 数据镜像）",
         "_rule": "JCR 以 JIF 百分位 75 / 50 / 25 为 Q1 / Q2 / Q3 / Q4 界",
         "_note": "由 scripts/verify_jcr_if.py 生成；verify_deliverables.py 据此离线复核",
         "venues": snap}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\n快照已写入 {SNAP.name}（{len(snap)} 刊）")

    print("\n" + "=" * 62)
    if bad:
        print(f"✗ {len(bad)} 刊与 WoS 不一致，须改 build_master_csv.py 的 VENUE：")
        for short, rq, ri, wq, wif, cat, pct, title, jif5 in bad:
            print(f"   {short}: 记 {rq} IF {ri} → 应为 {wq} IF {wif}"
                  f"（5y {jif5}，{cat}，百分位 {pct}%）\n      匹配到：{title}")
    else:
        print("✓ 全部带数值 IF 的期刊与 WoS 一致")
    if unknown:
        print(f"⚠ {len(unknown)} 刊未在镜像站命中，须人工核：{unknown}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
