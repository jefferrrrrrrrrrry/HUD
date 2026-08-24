"""
OpenAlex 批量元数据爬取脚本
针对：navigation_attention_ARHUD 子项目

策略：6 个关键词组 × OpenAlex API
输出：metadata.json（含title/abstract/doi/year/venue/authors/cited_by_count）
"""

import json
import time
import urllib.parse
import urllib.request
import os

PROXY = os.environ.get('http_proxy', 'http://oversea-squid2.ko.txyun:11080')
HEADERS = {'User-Agent': 'Mozilla/5.0 (research bot; mailto:user@example.com)'}

# 6 个关键词组
QUERY_GROUPS = {
    "A_AR_HUD_navigation": [
        "AR-HUD navigation",
        "augmented reality head-up display navigation",
        "conformal navigation arrow driving",
        "wayfinding head-up display",
    ],
    "B_attentional_capture_driving": [
        "attentional capture driving HUD",
        "stimulus-driven attention vehicle display",
        "visual salience driving warning",
        "abrupt onset attention driving",
    ],
    "C_signal_suppression": [
        "signal suppression hypothesis driving",
        "distractor suppression visual search",
        "attentional suppression display",
        "feature suppression visual attention",
    ],
    "D_inattentional_blindness_AR": [
        "inattentional blindness driving HUD",
        "attentional tunneling head-up display",
        "change blindness augmented reality driving",
        "attention competition AR display",
    ],
    "E_transparency_luminance": [
        "transparency HUD warning",
        "opacity head-up display visibility",
        "luminance reduction in-vehicle display",
        "alpha blending AR driving",
    ],
    "F_traffic_density_complexity": [
        "traffic density AR-HUD warning",
        "scene complexity driving warning",
        "multi-target augmented reality driving",
        "visual clutter HUD warning",
    ],
}

OUTPUT_FILE = "/home/gezhuocheng/moe/HUD/navigation_attention_ARHUD/metadata_raw.json"


def search_openalex(query, per_page=25):
    """OpenAlex search API"""
    url = (
        f"https://api.openalex.org/works?"
        f"search={urllib.parse.quote(query)}"
        f"&per-page={per_page}"
        f"&filter=publication_year:2008-2025"
    )
    try:
        proxy_handler = urllib.request.ProxyHandler({"http": PROXY, "https": PROXY})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = list(HEADERS.items())
        with opener.open(url, timeout=30) as resp:
            data = json.loads(resp.read().decode('utf-8'))
        return data.get('results', [])
    except Exception as e:
        print(f"  ERROR: {e}")
        return []


def reconstruct_abstract(inverted_index):
    """OpenAlex 的 abstract 是 inverted index 格式，需要重建"""
    if not inverted_index:
        return ""
    word_positions = []
    for word, positions in inverted_index.items():
        for pos in positions:
            word_positions.append((pos, word))
    word_positions.sort()
    return " ".join(w for _, w in word_positions)


def normalize_record(rec, group_key):
    """提取关键字段，规范化"""
    abstract = reconstruct_abstract(rec.get('abstract_inverted_index', {}))
    authors = []
    for au in rec.get('authorships', []) or []:
        a = au.get('author', {}) or {}
        if a.get('display_name'):
            authors.append(a['display_name'])
    # 兼容新旧版API字段：primary_location.source 取代 host_venue
    venue = ''
    primary_loc = rec.get('primary_location') or {}
    src = primary_loc.get('source') or {}
    venue = src.get('display_name', '')
    if not venue:
        venue_obj = rec.get('host_venue', {}) or {}
        venue = venue_obj.get('display_name', '')

    return {
        'openalex_id': rec.get('id', ''),
        'doi': rec.get('doi', '').replace('https://doi.org/', '') if rec.get('doi') else '',
        'title': rec.get('title', ''),
        'abstract': abstract[:1500],
        'year': rec.get('publication_year'),
        'type': rec.get('type', ''),
        'authors': authors[:8],
        'venue': venue,
        'cited_by_count': rec.get('cited_by_count', 0),
        'topic': (rec.get('primary_topic') or {}).get('display_name', ''),
        'group': group_key,
    }


def main():
    all_records = {}  # 用 openalex_id 去重
    log = []
    
    for group_key, queries in QUERY_GROUPS.items():
        print(f"\n=== Group {group_key} ===")
        for query in queries:
            print(f"  搜索: {query}")
            results = search_openalex(query, per_page=25)
            print(f"    返回 {len(results)} 条")
            log.append({'group': group_key, 'query': query, 'hits': len(results)})
            for rec in results:
                norm = normalize_record(rec, group_key)
                if norm['openalex_id']:
                    if norm['openalex_id'] not in all_records:
                        all_records[norm['openalex_id']] = norm
                    else:
                        # 已存在 - 仅追加 group 来源
                        existing = all_records[norm['openalex_id']]
                        if norm['group'] not in existing['group']:
                            existing['group'] = existing['group'] + '+' + norm['group']
            time.sleep(1)  # API rate limit
    
    print(f"\n总计去重后 {len(all_records)} 条记录")
    
    # 输出
    output = {
        'meta': {
            'total': len(all_records),
            'log': log,
            'queries': QUERY_GROUPS,
        },
        'records': list(all_records.values())
    }
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"\n输出: {OUTPUT_FILE}")


if __name__ == '__main__':
    main()
