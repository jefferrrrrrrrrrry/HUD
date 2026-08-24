"""由 Crossref/arXiv 核实结果生成 APA 7th 参考文献条目。

输入：scripts/apa_crossref_raw.json + papers_metadata.json
输出：scripts/apa_refs.json（idx -> {apa, intext, sort_key}）与 scripts/apa_refs_preview.md
"""
import json
import pathlib
import re

raw = json.loads(pathlib.Path('scripts/apa_crossref_raw.json').read_text())
meta = {str(p['idx']): p for p in json.loads(pathlib.Path('papers_metadata.json').read_text())}

# 中文姓名（本库有两条中文一作），APA 7th 对中文作者按姓全拼 + 名首字母处理
CJK_OVERRIDE = {
    '09': [('Ye', 'M. H.')],       # 叶明慧
    '79': [('Bao', 'W. Y.')],      # 鲍威宇
}


def initials(given):
    if not given:
        return ''
    parts = re.split(r'[\s\-]+', given.strip())
    out = []
    for p in parts:
        p = p.strip('.')
        if not p:
            continue
        if len(p) == 1 or p.isupper():
            out.append(p[0].upper() + '.')
        else:
            out.append(p[0].upper() + '.')
    return ' '.join(out)


def fmt_authors(authors, idx=None):
    if idx in CJK_OVERRIDE:
        items = [f'{fam}, {ini}' for fam, ini in CJK_OVERRIDE[idx]]
    else:
        items = []
        for a in authors or []:
            fam = (a.get('family') or '').strip()
            giv = initials(a.get('given'))
            if not fam and not giv:
                continue
            items.append(f'{fam}, {giv}'.strip().rstrip(','))
    if not items:
        return None
    if len(items) == 1:
        return items[0]
    if len(items) <= 20:
        return ', '.join(items[:-1]) + ', & ' + items[-1]
    # APA 7th：>20 位作者，列前 19 位 + ... + 最后一位
    return ', '.join(items[:19]) + ', . . . ' + items[-1]


def pages(v):
    p = v.get('cr_page')
    if p:
        return p.replace('-', '\u2013')
    art = v.get('cr_article_number')
    return str(art) if art else None


def doi_url(v):
    d = v.get('cr_doi')
    if d:
        return 'https://doi.org/' + d
    return v.get('cr_url')


def build(idx, v):
    m = meta[idx]
    au = fmt_authors(v.get('cr_authors'), idx)
    yr = v.get('cr_year') or m.get('year')
    title = (v.get('cr_title') or m.get('title') or '').strip()
    t = v.get('cr_type') or 'journal-article'
    cont = v.get('cr_container')
    vol, iss, pg = v.get('cr_volume'), v.get('cr_issue'), pages(v)
    pub = v.get('cr_publisher')
    url = doi_url(v)

    if au is None:
        head = f'{title}.'
        au_part = None
    else:
        au_part = au

    def tail(s):
        return (s + ' ' + url) if url else s

    if t == 'journal-article':
        seg = f'*{cont}*' if cont else ''
        if vol:
            seg += f', *{vol}*'
            if iss:
                seg += f'({iss})'
        if pg:
            seg += f', {pg}'
        if au_part:
            return tail(f'{au_part} ({yr}). {title}. {seg}.'.replace(' .', '.'))
        return tail(f'{title}. ({yr}). {seg}.')

    if t == 'proceedings-article':
        inpart = f'In *{cont}*' if cont else 'In *Proceedings*'
        if pg:
            inpart += f' (pp. {pg})'
        seg = inpart + ('. ' + pub if pub else '')
        return tail(f'{au_part} ({yr}). {title}. {seg}.')

    if t == 'book-chapter':
        inpart = f'In *{cont}*' if cont else ''
        if pg:
            inpart += f' (pp. {pg})'
        seg = inpart + ('. ' + pub if pub else '')
        return tail(f'{au_part} ({yr}). {title}. {seg}.')

    if t == 'dissertation':
        inst = pub or 'Institution not reported'
        kind = 'Doctoral dissertation'
        return tail(f'{au_part} ({yr}). *{title}* [{kind}, {inst}].')

    if t in ('standard',):
        org = pub or 'Standards body not reported'
        return tail(f'{org}. ({yr}). *{title}*.')

    if t in ('report',):
        org = pub or 'Publisher not reported'
        if au_part:
            return tail(f'{au_part} ({yr}). *{title}* [Technical paper]. {org}.')
        return tail(f'{org}. ({yr}). *{title}* [Technical paper].')

    if t in ('preprint', 'posted-content'):
        host = pub if pub in ('arXiv',) else (pub or 'Preprint server')
        if host == 'arXiv':
            return tail(f'{au_part} ({yr}). *{title}* [Preprint]. arXiv.')
        return tail(f'{au_part} ({yr}). *{title}* [Preprint]. {host}.')

    if t == 'dataset':
        return tail(f'{au_part} ({yr}). *{title}* [Conference paper record]. {pub or ""}.'.replace('  ', ' '))

    seg = f'*{cont}*' if cont else (pub or '')
    return tail(f'{au_part} ({yr}). {title}. {seg}.')


def intext(idx, v):
    if idx in CJK_OVERRIDE:
        fams = [f for f, _ in CJK_OVERRIDE[idx]]
    else:
        fams = [(a.get('family') or '').strip() for a in (v.get('cr_authors') or []) if a.get('family')]
    yr = v.get('cr_year') or meta[idx].get('year')
    if not fams:
        corp = v.get('corporate_author') or v.get('cr_publisher')
        return f'({corp}, {yr})' if corp else f'(无作者记录, {yr})'
    if len(fams) == 1:
        return f'({fams[0]}, {yr})'
    if len(fams) == 2:
        return f'({fams[0]} & {fams[1]}, {yr})'
    return f'({fams[0]} et al., {yr})'


out = {}
for idx in sorted(raw, key=int):
    v = raw[idx]
    if v.get('err'):
        out[idx] = {'apa': None, 'err': v['err']}
        continue
    apa = re.sub(r'\s+', ' ', build(idx, v)).replace(' ,', ',').replace('..', '.').strip()
    fams = [f for f, _ in CJK_OVERRIDE[idx]] if idx in CJK_OVERRIDE else \
        [(a.get('family') or '') for a in (v.get('cr_authors') or [])]
    out[idx] = {
        'apa': apa,
        'intext': intext(idx, v),
        'sort_key': ((fams[0] if fams else 'zzz').lower(), v.get('cr_year') or 0),
        'type': v.get('cr_type'),
        'note': v.get('note') or v.get('fix_note'),
    }

pathlib.Path('scripts/apa_refs.json').write_text(json.dumps(out, ensure_ascii=False, indent=1))

lines = ['# APA 7th 参考文献条目（由 Crossref/arXiv 核实结果自动生成）', '',
         '> 生成脚本：`scripts/build_apa_refs.py`；原始核实数据：`scripts/apa_crossref_raw.json`。',
         '> 标题大小写按出版商记录原样转录，未做 sentence-case 自动转换（避免误伤专有名词）。', '']
for idx in sorted(out, key=int):
    r = out[idx]
    if not r.get('apa'):
        lines.append(f'- **#{idx}** ⚠ {r.get("err")}')
    else:
        lines.append(f'- **#{idx}** `{r["intext"]}` — {r["apa"]}' + (f'  ⟨{r["note"]}⟩' if r.get('note') else ''))
pathlib.Path('scripts/apa_refs_preview.md').write_text('\n'.join(lines))
print('generated', len(out))
