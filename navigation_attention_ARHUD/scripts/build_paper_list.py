"""生成文献清单 CSV/MD"""
import json
import csv
import re

INPUT = "/home/gezhuocheng/moe/HUD/navigation_attention_ARHUD/metadata_filtered.json"
OUT_CSV = "/home/gezhuocheng/moe/HUD/navigation_attention_ARHUD/02_文献清单.csv"
OUT_MD = "/home/gezhuocheng/moe/HUD/navigation_attention_ARHUD/02_文献清单.md"

with open(INPUT) as f:
    data = json.load(f)
records = data['records']

# CSV
with open(OUT_CSV, 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['idx', 'year', 'first_author', 'all_authors', 'title', 'venue',
                'doi', 'cited_by', 'group', 'topic', '相关性评分', '匹配关键词', 'abstract'])
    for i, r in enumerate(records, 1):
        w.writerow([
            i,
            r.get('year', ''),
            r['authors'][0] if r.get('authors') else '',
            '; '.join(r.get('authors', [])[:4]),
            r.get('title', ''),
            r.get('venue', ''),
            r.get('doi', ''),
            r.get('cited_by_count', 0),
            r.get('group', ''),
            r.get('topic', ''),
            f"{r.get('_score', 0):.1f}",
            r.get('_matched', ''),
            (r.get('abstract', '') or '')[:300],
        ])

# Markdown
with open(OUT_MD, 'w', encoding='utf-8') as f:
    f.write(f"# 文献清单（共 {len(records)} 篇）\n\n")
    f.write(f"> 来源：OpenAlex 514 条原始记录 → 271 条相关 → 排序后 Top-{len(records)}\n")
    f.write(f"> 排除：主课题已收录 37 篇 + 明显无关主题（医学/航空/农业等）\n\n")
    f.write("| idx | 年份 | 第一作者 | 标题 | 期刊/会议 | DOI | 引用 | 相关性 | 主题组 |\n")
    f.write("|-----|------|---------|------|-----------|-----|------|--------|--------|\n")
    for i, r in enumerate(records, 1):
        first_au = r['authors'][0] if r.get('authors') else 'N/A'
        title = (r.get('title') or '')[:80]
        venue = (r.get('venue') or '')[:40]
        doi = r.get('doi', '')
        f.write(f"| {i} | {r.get('year','')} | {first_au} | {title} | {venue} | {doi} | "
                f"{r.get('cited_by_count', 0)} | {r.get('_score', 0):.1f} | "
                f"{r.get('group', '')[:30]} |\n")
    f.write(f"\n\n## 各主题组分布\n\n")
    from collections import Counter
    groups = Counter()
    for r in records:
        g = r.get('group', '').split('+')[0]
        groups[g] += 1
    for g, n in groups.most_common():
        f.write(f"- **{g}**: {n} 篇\n")
    f.write(f"\n## 引用数 Top-10\n\n")
    top_cited = sorted(records, key=lambda r: -r.get('cited_by_count', 0))[:10]
    for r in top_cited:
        first_au = r['authors'][0] if r.get('authors') else 'N/A'
        f.write(f"- [{r.get('cited_by_count', 0):>4}] {r.get('year', '')} {first_au}: {r.get('title', '')[:80]}\n")
    f.write(f"\n## 期刊/会议分布\n\n")
    venues = Counter()
    for r in records:
        v = r.get('venue', '')[:40] or 'N/A'
        venues[v] += 1
    for v, n in venues.most_common(15):
        f.write(f"- {v}: {n}\n")

print(f"CSV: {OUT_CSV}")
print(f"MD:  {OUT_MD}")
