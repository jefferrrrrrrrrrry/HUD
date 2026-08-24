import json, time, urllib.request, urllib.parse, pathlib

UA = {'User-Agent': 'HUD-thesis-refs/1.0 (mailto:res@example.org)'}

def cr_by_doi(doi):
    u = 'https://api.crossref.org/works/' + urllib.parse.quote(doi, safe='')
    try:
        return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=45))['message']
    except Exception as e:
        return {'_err': str(e)}

def cr_by_title(title, year=None):
    q = {'query.bibliographic': title, 'rows': 3}
    u = 'https://api.crossref.org/works?' + urllib.parse.urlencode(q)
    try:
        items = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=45))['message']['items']
    except Exception as e:
        return {'_err': str(e)}
    tl = title.lower()[:60]
    for it in items:
        t = (it.get('title') or [''])[0].lower()
        if t[:60] == tl or tl in t or t[:40] in tl:
            return it
    return items[0] if items else {'_err': 'no match'}

meta = json.load(open('papers_metadata.json'))
out = {}
for p in meta:
    idx = p['idx']
    doi = p.get('doi')
    d = cr_by_doi(doi) if doi else cr_by_title(p.get('title',''), p.get('year'))
    if '_err' in d and doi:
        d = cr_by_title(p.get('title',''), p.get('year'))
    rec = {'idx': idx}
    if '_err' in d:
        rec['err'] = d['_err']
    else:
        iss = (d.get('issued') or {}).get('date-parts') or [[None]]
        rec.update({
            'cr_doi': d.get('DOI'),
            'cr_title': (d.get('title') or [None])[0],
            'cr_container': (d.get('container-title') or [None])[0],
            'cr_short_container': (d.get('short-container-title') or [None])[0],
            'cr_volume': d.get('volume'),
            'cr_issue': d.get('issue'),
            'cr_page': d.get('page'),
            'cr_article_number': d.get('article-number'),
            'cr_year': iss[0][0] if iss and iss[0] else None,
            'cr_type': d.get('type'),
            'cr_publisher': d.get('publisher'),
            'cr_event': (d.get('event') or {}).get('name'),
            'cr_authors': [{'given': a.get('given'), 'family': a.get('family')} for a in (d.get('author') or [])],
            'cr_editors': [{'given': a.get('given'), 'family': a.get('family')} for a in (d.get('editor') or [])],
            'cr_isbn': d.get('ISBN'),
            'cr_cites': d.get('is-referenced-by-count'),
        })
    out[str(idx)] = rec
    print(idx, rec.get('cr_container') or rec.get('err'), '| v', rec.get('cr_volume'), 'i', rec.get('cr_issue'), 'p', rec.get('cr_page'), flush=True)
    time.sleep(0.35)

pathlib.Path('scripts/apa_crossref_raw.json').write_text(json.dumps(out, ensure_ascii=False, indent=1))
print('DONE', len(out))
