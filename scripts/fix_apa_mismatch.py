import json
import pathlib

RAW = pathlib.Path('scripts/apa_crossref_raw.json')
raw = json.loads(RAW.read_text())

# 三条 arXiv 预印本被 Crossref 模糊匹配到无关记录，按 arXiv API 核实结果覆盖
FIX = {
    '38': dict(cr_doi=None, cr_title='A Real-Time Predictive Pedestrian Collision Warning Service for Cooperative Intelligent Transportation Systems',
               cr_container=None, cr_volume=None, cr_issue=None, cr_page=None, cr_year=2022, cr_type='preprint',
               cr_publisher='arXiv', cr_url='https://arxiv.org/abs/2009.10868',
               cr_authors=[{'given': 'Ue-Hwan', 'family': 'Kim'}, {'given': 'Dongho', 'family': 'Ka'},
                           {'given': 'Hwasoo', 'family': 'Yeo'}, {'given': 'Jong-Hwan', 'family': 'Kim'}],
               note='arXiv:2009.10868v4；首次投递 2020-09-23，v4 更新 2022-02-22'),
    '83': dict(cr_doi=None, cr_title='Head-up Displays (HUD) in driving',
               cr_container=None, cr_volume=None, cr_issue=None, cr_page=None, cr_year=2018, cr_type='preprint',
               cr_publisher='arXiv', cr_url='https://arxiv.org/abs/1803.08383',
               cr_authors=[{'given': 'Marcos', 'family': 'Maroto'}, {'given': 'Enrique', 'family': 'Caño'},
                           {'given': 'Pavel', 'family': 'González'}, {'given': 'Diego', 'family': 'Villegas'}],
               note='arXiv:1803.08383v1'),
    '89': dict(cr_doi=None, cr_title='Early warning of pedestrians and cyclists',
               cr_container=None, cr_volume=None, cr_issue=None, cr_page=None, cr_year=2021, cr_type='preprint',
               cr_publisher='arXiv', cr_url='https://arxiv.org/abs/2107.05186',
               cr_authors=[{'given': 'Joerg Christian', 'family': 'Wolf'}],
               note='arXiv:2107.05186v1'),
}

for k, v in FIX.items():
    raw[k] = {'idx': int(k), **v}

RAW.write_text(json.dumps(raw, ensure_ascii=False, indent=1))
print('fixed', list(FIX))
