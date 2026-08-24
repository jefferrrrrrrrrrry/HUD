"""
对 metadata_raw.json 进行筛选与排名
策略：
1. 排除已经在主课题40篇中的（按DOI去重）
2. 按相关性评分（含title/abstract关键词匹配 + 引用数）排序
3. 输出 top-80 候选清单
"""
import json
import re
import os

INPUT = "/home/gezhuocheng/moe/HUD/navigation_attention_ARHUD/metadata_raw.json"
MAIN_PROJECT_META = "/home/gezhuocheng/moe/HUD/papers_metadata.json"
OUTPUT = "/home/gezhuocheng/moe/HUD/navigation_attention_ARHUD/metadata_filtered.json"

# 主题相关关键词（含权重）
HIGH_PRIORITY_TERMS = {
    # AR-HUD 导航
    'AR-HUD': 5, 'augmented reality': 4, 'head-up display': 4, 'HUD': 3,
    'navigation': 4, 'wayfinding': 3, 'conformal': 4,
    # 注意捕获
    'attentional capture': 5, 'visual salience': 4, 'salience': 3,
    'bottom-up attention': 4, 'stimulus-driven': 4, 'abrupt onset': 3,
    # 信号抑制
    'signal suppression': 5, 'distractor suppression': 5, 'attentional suppression': 4,
    'feature suppression': 4, 'salience reduction': 4,
    # 非注意盲视
    'inattentional blindness': 5, 'attentional tunneling': 5, 'attention tunneling': 5,
    'change blindness': 4, 'attention competition': 4,
    # 透明度/亮度
    'transparency': 3, 'opacity': 3, 'luminance': 3, 'alpha blending': 3,
    # 应用领域
    'driving': 3, 'driver': 3, 'pedestrian': 3, 'collision warning': 4,
    'in-vehicle': 3, 'vehicle display': 3, 'ADAS': 3,
    # 方法
    'eye tracking': 2, 'driving simulator': 2, 'cognitive load': 2,
}

# 排除明显无关
EXCLUDE_TERMS = [
    'aircraft', 'aviation', 'pilot', 'aerial vehicle', 'drone', 'UAV',
    'cancer', 'medical imaging', 'tumor', 'patient',
    'molecular', 'gene', 'protein', 'cell',
    'climate', 'weather forecast', 'earthquake',
    'agriculture', 'farming', 'crop',
    'astronomy', 'galaxy', 'planet',
    'mining', 'geology', 'mineral',
    'finance', 'stock market', 'banking',
    'sports', 'athletic', 'gym',
    'children\'s book', 'preschool',
]

# 主课题40篇
def load_main_dois():
    if not os.path.exists(MAIN_PROJECT_META):
        return set()
    with open(MAIN_PROJECT_META) as f:
        data = json.load(f)
    dois = set()
    if isinstance(data, list):
        for entry in data:
            doi = (entry.get('doi') or '').lower().replace('https://doi.org/', '')
            if doi:
                dois.add(doi)
    elif isinstance(data, dict):
        for entry in data.values() if isinstance(data, dict) else []:
            if isinstance(entry, dict):
                doi = (entry.get('doi') or '').lower().replace('https://doi.org/', '')
                if doi:
                    dois.add(doi)
    return dois


def score_record(rec, exclude_dois):
    """对单条记录评分"""
    title = (rec.get('title') or '').lower()
    abstract = (rec.get('abstract') or '').lower()
    venue = (rec.get('venue') or '').lower()
    text = title + ' ' + abstract
    
    # 已排除的DOI
    doi = (rec.get('doi') or '').lower()
    if doi and doi in exclude_dois:
        return -1, 'EXCLUDED_MAIN_PROJECT'
    
    # 排除关键词
    for term in EXCLUDE_TERMS:
        if term in text:
            return -1, f'EXCLUDED_BY_TERM:{term}'
    
    # 标题/摘要为空
    if not title or len(title) < 10:
        return -1, 'NO_TITLE'
    if not abstract or len(abstract) < 50:
        # 没有 abstract，但是 title 非常匹配可保留
        title_score = sum(w for term, w in HIGH_PRIORITY_TERMS.items() if term in title)
        if title_score < 5:
            return -1, 'NO_ABSTRACT_LOW_TITLE'
    
    # 评分
    score = 0
    matched = []
    for term, weight in HIGH_PRIORITY_TERMS.items():
        if term in title:
            score += weight * 2  # title 权重双倍
            matched.append(f'T:{term}')
        elif term in abstract:
            score += weight
            matched.append(f'A:{term}')
    
    # 引用加成（log scale）
    cited = rec.get('cited_by_count', 0) or 0
    if cited > 0:
        import math
        score += min(math.log10(cited + 1) * 2, 8)
    
    # venue 质量加成
    high_venue_keywords = [
        'human factors', 'cognition', 'psychology', 'attention',
        'human-computer interaction', 'transportation research',
        'accident analysis', 'applied ergonomics',
        'IEEE', 'ACM', 'CHI', 'HFES',
        'augmented reality', 'virtual reality', 'displays'
    ]
    for v in high_venue_keywords:
        if v in venue:
            score += 1
            break
    
    # 类型加成
    rtype = (rec.get('type') or '').lower()
    if rtype in ('article', 'journal-article'):
        score += 2
    elif rtype in ('proceedings-article', 'paper-conference', 'conference'):
        score += 1
    
    return score, ','.join(matched[:8])


def main():
    with open(INPUT) as f:
        data = json.load(f)
    records = data['records']
    print(f"原始记录: {len(records)}")
    
    exclude_dois = load_main_dois()
    print(f"主课题40篇 DOI 待排除: {len(exclude_dois)}")
    
    scored = []
    excluded_stats = {}
    for rec in records:
        score, reason = score_record(rec, exclude_dois)
        if score < 0:
            excluded_stats[reason] = excluded_stats.get(reason, 0) + 1
            continue
        rec['_score'] = score
        rec['_matched'] = reason
        scored.append(rec)
    
    print(f"\n排除统计:")
    for k, v in sorted(excluded_stats.items(), key=lambda x: -x[1])[:10]:
        print(f"  {k}: {v}")
    
    # 按评分排序
    scored.sort(key=lambda r: -r['_score'])
    print(f"\n保留 {len(scored)} 条相关记录")
    
    # 取 top-80
    top = scored[:80]
    print(f"\nTop-80 评分分布:")
    print(f"  最高: {top[0]['_score']:.1f}")
    print(f"  Top-10 中位数: {sorted([r['_score'] for r in top[:10]])[5]:.1f}")
    print(f"  第80名: {top[-1]['_score']:.1f}")
    
    # 输出
    output = {
        'meta': {
            'original_count': len(records),
            'main_project_dois_excluded': len(exclude_dois),
            'after_filter': len(scored),
            'top_n': len(top),
            'score_range': [top[-1]['_score'], top[0]['_score']],
        },
        'records': top,
    }
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"\n输出: {OUTPUT}")
    
    # 打印 top-20 预览
    print("\n=== Top-20 预览 ===")
    for i, rec in enumerate(top[:20], 1):
        title = rec['title'][:80]
        authors = ', '.join(rec['authors'][:2])
        print(f"  {i:>2}. [{rec['_score']:>5.1f}] {rec['year']} {authors} | {title}")


if __name__ == '__main__':
    main()
