"""对 Crossref 原始记录做人工核实后的修正。每条修正都注明核实来源。"""
import json
import pathlib

P = pathlib.Path('scripts/apa_crossref_raw.json')
raw = json.loads(P.read_text())

# ── 1. Crossref 把中文作者的 given/family 颠倒（README 的作者标注与本修正一致）
SWAP = {
    '33': '姓氏应为 Cheng/Zhong/Ye/Tian，Crossref 记录颠倒',
    '67': '姓氏应为 Cheng/Zhong/Tian，Crossref 记录颠倒',
    '71': '姓氏应为 Zhang/Li/Yan/Xue，Crossref 记录颠倒',
}
for k, why in SWAP.items():
    au = raw[k].get('cr_authors') or []
    raw[k]['cr_authors'] = [{'given': a.get('family'), 'family': a.get('given')} for a in au]
    raw[k]['fix_note'] = why

# ── 2. Crossref 期刊名中的 HTML 实体
for k, v in raw.items():
    c = v.get('cr_container')
    if c and '&amp;' in c:
        v['cr_container'] = c.replace('&amp;', '&')

# ── 3. 两篇法国博士论文：Crossref 的 publisher 是书目机构 ABES，非授予机构。
#     经 theses.fr API 用 NNT 核实真实授予机构与答辩日期。
raw['81'].update({
    'cr_publisher': 'Université de Technologie de Compiègne',
    'cr_year': 2016,
    'fix_note': "theses.fr NNT 2016COMP2280；答辩 2016-06-27；École doctorale Sciences pour l'ingénieur (Compiègne)；"
                "实验室 Heudiasyc UMR-7253；导师 Frémont & Thouvenin。Crossref 原记 publisher='ABES'（书目机构）已更正",
})
raw['84'].update({
    'cr_publisher': 'Aix-Marseille Université',
    'cr_year': 2020,
    'fix_note': "theses.fr NNT 2020AIXM0610；答辩 **2020-12-18**（Crossref 记 2022 为登记年，非答辩年）；"
                "École Doctorale Sciences du mouvement humain (Marseille)；LMA UMR 7031 + Université Gustave Eiffel；"
                "导师 Serre。**本库多处此前写作『Char 2022』，应统一改为 2020**",
})

# ── 4. SAE 标准与技术论文的团体作者，用于 in-text 引注
raw['101']['corporate_author'] = 'SAE International'
raw['101']['fix_note'] = 'SAE J2400_200308；团体作者，in-text 作 (SAE International, 2003)'

P.write_text(json.dumps(raw, ensure_ascii=False, indent=1))
print('patched:', sorted(set(list(SWAP) + ['55', '62', '73', '81', '84', '101']), key=int))

# ── 5. Crossref 把部分作者的完整姓名塞进 family 字段（given 为空）。
#     依据 papers_metadata.json 的 authors 与论文原文署名切分为 given/family。
NAME_SPLIT = {
    '2':  [('Minh Tien', 'Phan'), ('Indira', 'Thouvenin'), ('Vincent', 'Frémont')],
    '5':  [('Changrak', 'Yoon'), ('Kyongho', 'Kim'), ('Hye Sun', 'Park'), ('Min Woo', 'Park'), ('Soon Ki', 'Jung')],
    '28': [('A.', 'Doshi'), ('Shinko Yuanhsien', 'Cheng'), ('M. M.', 'Trivedi')],
    '72': [('Yuan-Lin', 'Chen'), ('Kun-Yuan', 'Shen'), ('Shun-Chung', 'Wang')],
}
raw2 = json.loads(P.read_text())
for k, pairs in NAME_SPLIT.items():
    raw2[k]['cr_authors'] = [{'given': g, 'family': f} for g, f in pairs]
    prev = raw2[k].get('fix_note')
    note = 'Crossref 将完整姓名置于 family 字段，已按论文署名切分 given/family'
    raw2[k]['fix_note'] = (prev + '；' + note) if prev else note
# #101 的作者列表为 [{None,None}]，清空以走团体作者分支
raw2['101']['cr_authors'] = []
P.write_text(json.dumps(raw2, ensure_ascii=False, indent=1))
print('name-split patched:', sorted(NAME_SPLIT, key=int), '+ 101 cleared')
