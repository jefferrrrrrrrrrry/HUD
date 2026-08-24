#!/usr/bin/env python3
"""把 102 篇文献合并为 24 列的《HUD_AR-HUD_行人预警_文献综合表.csv》。

数据来源
  - 第 1–39 行的 12 个内容列：沿用旧 CSV（人工核校过，不动）
  - 第 40–102 行的 12 个内容列：scripts/_csv_batch_*.json（四批 agent 精读提取）
  - 元数据 5 列（作者/团队/年份/来源/JCR）：papers_metadata.json + apa_refs.json + JCR 表
  - 新增 5 列：scripts/_csv_newcols.json

输出同时写 csv / tsv / md 三份。
"""
from __future__ import annotations

import csv
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
S = ROOT / "scripts"

OLD_CSV = ROOT / "HUD_AR-HUD_行人预警_文献综合表.csv"
OUT_CSV = ROOT / "HUD_AR-HUD_行人预警_文献综合表.csv"
OUT_TSV = ROOT / "HUD_AR-HUD_行人预警_文献综合表.tsv"
OUT_MD = ROOT / "HUD_AR-HUD_行人预警_文献综合表.md"

CONTENT_COLS = ["场景", "色彩显示", "位置", "形状", "动静态", "预警信息出现时间",
                "预警信息持续时间", "预警信息是否有分级", "实验任务", "自变量",
                "因变量", "结果"]
NEW_COLS = ["★资料来源", "★证据强度", "★APA引注", "★APA条目", "★所属实验"]
HEADER = (["序号", "文献"] + CONTENT_COLS
          + ["作者", "团队/单位", "发表年份", "期刊/来源", "JCR分区"] + NEW_COLS)

# ── venue 归一化：原始 venue 片段 -> (期刊/来源简称, JCR分区串) ───────────────
# 简称不含年份，年份在生成时拼接。JCR 数据来源见 jcr_quartile_data.json 的 _meta。
VENUE = {
    # 期刊
    "Accident Analysis": ("AAP", "Q1 (IF 7.4) (交通安全领域权威期刊)"),
    "Transportation Research Part F": ("TR Part F", "Q1 (IF 5.0) (交通心理学与行为权威期刊)"),
    "Traffic Injury Prevention": ("Traffic Inj Prev", "Q3 (IF 2.1) (交通伤害预防专刊)"),
    "Applied Ergonomics": ("Applied Ergonomics", "Q2 (IF 3.5) (人因工程权威期刊；百分位 70.4%，未过 Q1 线)"),
    "International Journal of Human-Computer Studies": ("IJHCS", "Q1 (IF 6.0) (HCI 重要期刊)"),
    "International Journal of Human-Computer Interaction": ("IJHCI", "Q1 (IF 6.1) (HCI 重要期刊；百分位 91.7%)"),
    "International Journal of Human–Computer Interaction": ("IJHCI", "Q1 (IF 6.1) (HCI 重要期刊；百分位 91.7%)"),
    "IEEE Transactions on Intelligent Transportation Systems": (
        "IEEE T-ITS", "Q1 (IF 9.1) / CCF B (智能交通顶刊；百分位 95.9%)"),
    "IET Intelligent Transport Systems": ("IET ITS", "Q3 (IF 2.7) (智能交通期刊；百分位 49.6%，未过 Q2 线)"),
    "PLoS ONE": ("PLoS ONE", "Q2 (IF 2.8) (综合性开放获取期刊)"),
    "Annual Review of Vision Science": ("Annu Rev Vis Sci", "Q1 (IF 6.5) (视觉科学年度综述)"),
    "Journal of the Society for Information Display": (
        "J SID", "Q3 (IF 2.0) (显示技术专刊；百分位 44.2%)"),
    "Journal of Traffic and Transportation Engineering": (
        "JTTE (Engl. Ed.)", "Q1 (IF 9.6) (长安大学主办，交通工程)"),
    # 以下三刊的 IF 于本轮补核（来源见 jcr_quartile_data.json 的 _verified_2026 段）
    "Annals of the New York Academy of Sciences": (
        "Ann NY Acad Sci", "Q1 (IF 4.5) (SCIE，Multidisciplinary Sciences 百分位 82.9%)"),
    "Transportation Research Interdisciplinary Perspectives": (
        "TRIP", "Q2 (IF 4.8) (ESCI，Transportation 类百分位 71.2%，全开放获取)"),
    "PRESENCE": ("PRESENCE (MIT Press)", "未收录JCR (IF -) (MIT Press，VR/AR 老牌期刊)"),
    "IEEE Access": ("IEEE Access", "Q2 (IF 4.2)"),
    "Sustainability": ("Sustainability (MDPI)", "Q2 (IF 4.1)"),
    "International Journal of Vehicle Design": (
        "Int J Vehicle Design", "Q4 (IF 0.7) (Inderscience；官网公示 Clarivate 2025 JIF 0.7、JCI 0.15)"),
    "Korean Journal of Industrial and Organizational Psychology": (
        "Korean J Ind Organ Psychol", "未收录JCR (IF -) (韩国 KCI 收录期刊)"),
    "Advances in Psychology": ("心理学进展", "未收录JCR (IF -) (中文期刊，汉斯出版社)"),
    "IEEE Transactions on Visualization and Computer Graphics": (
        "TVCG", "Q1 (IF 6.8) / CCF A (可视化和计算机图形学顶刊；百分位 92.2%)"),
    # 会议 / 论文集 / 其他
    "Proceedings of the 7th International Conference on Automotive User Interfaces": (
        "AutomotiveUI", "会议 (IF -) (ACM 车载交互旗舰会议)"),
    "IEEE International Conference on Robotics and Automation": (
        "ICRA", "会议 (IF -) / CCF B (机器人领域顶级会议)"),
    "IEEE Intelligent Vehicles Symposium": ("IEEE IV", "会议 (IF -) (智能车辆重要会议)"),
    "Conference on Intelligent Transportation Systems": (
        "ITSC", "会议 (IF -) / CCF C (ITSC 国际智能交通会议)"),
    "CAA International Conference on Vehicular Control and Intelligence": (
        "CVCI", "会议 (IF -) (中国自动化学会车辆控制与智能会议)"),
    "Conference on Traffic Engineering and Transportation System": (
        "ICTETS", "会议论文集 (IF -) (SPIE 出版)"),
    "Conference on Transportation Information and Safety": (
        "ICTIS", "会议 (IF -) (交通信息与安全国际会议)"),
    "Conference on Industrial Electronics and Applications": (
        "ICIEA", "会议 (IF -) (IEEE 工业电子与应用会议)"),
    "Vehicular Electronics and Safety": ("ICVES", "会议 (IF -) (IEEE 车辆电子与安全会议)"),
    "Asia-Pacific Services Computing Conference": (
        "IEEE APSCC", "会议 (IF -) (亚太服务计算会议)"),
    "International Conference on Road and Rail Infrastructure": (
        "CETRA", "会议论文集 (IF -) (公路与铁路基础设施国际会议)"),
    "CICTP": ("CICTP", "会议论文集 (IF -) (ASCE 出版，中国交通运输研究会议)"),
    "International Symposium on Computer, Consumer and Control": (
        "IS3C", "会议 (IF -) (IEEE 计算机、消费电子与控制会议)"),
    "AHFE International": ("AHFE", "会议论文集 (IF -) (AHFE 国际人因会议)"),
    "Procedia Manufacturing": ("Procedia Manufacturing", "会议论文集 (IF -) (Elsevier，已停刊)"),
    "Lecture Notes in Computer Science": ("Springer LNCS", "会议论文集 (IF -) (Springer LNCS)"),
    "Implementation and Integration of Information Systems": (
        "图书章节 (IGI Global)", "图书章节 (IF -) (非期刊)"),
    "arXiv preprint": ("arXiv 预印本", "预印本 (IF -) (未经同行评议)"),
    "SAE Technical Paper": ("SAE Technical Paper", "技术论文 (IF -) (SAE 技术论文，非 JCR 期刊)"),
    "PsycEXTRA": ("PsycEXTRA (APA)", "灰色文献 (IF -) (APA PsycEXTRA 收录报告)"),
}

# Crossref 把部分中文姓名的姓/名颠倒或未转写，此处按 apa_refs.json 的判定改正
AUTHOR_FIX = {
    79: ["鲍威宇 (Weiyu Bao)"],
    # #82 的 papers_metadata 登记的是学位论文版（单作者），题录已改期刊版（7 位作者）
    82: ["Mark C. Schall", "Michelle L. Rusch", "John D. Lee", "Jeffrey D. Dawson",
         "Geb Thomas", "Nazan Aksan", "Matthew Rizzo"],
}

# 6 篇 venue 缺失者：由 apa_refs.json 的 type 与条目文本判定

FALLBACK = {
    81: ("博士论文 (UTC)", "学位论文 (IF -) (Université de Technologie de Compiègne，Heudiasyc UMR-7253)"),
    # #82 题录已由 fix_apa_82_schall.py 改为期刊版（精读全文即期刊版），来源列同步
    82: ("Human Factors", "Q1 (IF 3.6) (人因工程顶刊，百分位 86%；同研究另有 Univ. of Iowa 学位论文版，不重复计数)"),
    84: ("博士论文 (Aix-Marseille Univ.)", "学位论文 (IF -) (Aix-Marseille Université，NNT 2020AIXM0610)"),
    94: ("SSRN 预印本", "预印本 (IF -) (SSRN，未经同行评议)"),
    95: ("SAE Technical Paper", "技术论文 (IF -) (SAE 技术论文，非 JCR 期刊)"),
    101: ("SAE J2400 标准", "标准 (IF -) (SAE 推荐规范，非 JCR 期刊)"),
}

# 批次提取后由后续核查得到更强结论的字段，在此覆盖（附裁定依据，勿删）。
# 不透明度记法裁定过程见 scripts/resolve_opacity_conflict.py 的模块 docstring。
OVERRIDES: dict[int, dict[str, str]] = {
    48: {"色彩显示":
         "本篇核心变量：色彩透明度 4 水平——T1 / T0.75 / T0.5 / T0.35（摘要明确给出取值）。"
         "T 值方向已裁定为 alpha（不透明度）：Ye 与 Yin（2025, Electronics 14(23):4768，"
         "本库 #09）方法节写 “The color transparency of the graphics was set to 0.75, "
         "which offers advantages in visibility and search response [22,23]”，其 [23] 即本篇"
         "——一个“提升 visibility”的 0.75 在物理上只能是不透明度，不可能是“75% 透明”。"
         "故 T1 = 完全不透明、T0.35 = 最透明；本篇最优区间换算为不透明度 0.5–0.75，"
         "与 Li 等（2025a）的 ≥ 0.6 一致。⚠ 裁定属间接证据（依据引用者转述而非本篇原文的"
         "参数定义），仍待原文确认。色相、RGB/HEX/CIE 坐标、颜色名称摘要均未报告。"},
}


def clean(s: str) -> str:
    """去 HTML 实体、压缩空白、统一破折号。"""
    if s is None:
        return ""
    s = html.unescape(str(s))
    s = s.replace("\u2010", "-").replace("\u00ad", "")
    return re.sub(r"\s+", " ", s).strip()


def venue_of(idx: int, raw: str) -> tuple[str, str]:
    if not raw:
        assert idx in FALLBACK, f"#{idx} venue 缺失且无 fallback"
        return FALLBACK[idx]
    raw = clean(raw)
    # 长匹配优先，避免 "International Journal of Human-Computer Studies" 被短键截获
    for key in sorted(VENUE, key=len, reverse=True):
        if key.lower() in raw.lower():
            return VENUE[key]
    raise SystemExit(f"#{idx} 未登记的 venue：{raw!r}")


def year_of(idx: int, apa: dict, meta_year) -> str:
    """年份以 apa_refs.json 为准（已 Crossref 核验，含 #84=2020、#78=2019 等更正）。"""
    m = re.search(r"\((\d{4})[a-z]?\)", apa.get("apa", ""))
    if m:
        return m.group(1)
    sk = apa.get("sort_key") or [None, 0]
    if isinstance(sk[1], (int, float)) and sk[1] > 1900:
        return str(int(sk[1]))
    return str(meta_year or "")


def main() -> None:
    meta = {p["idx"]: p for p in json.loads((ROOT / "papers_metadata.json").read_text("utf-8"))}
    apa = json.loads((S / "apa_refs.json").read_text("utf-8"))
    newc = json.loads((S / "_csv_newcols.json").read_text("utf-8"))
    batch: dict[int, dict] = {}
    for f in ("_csv_batch_41_56", "_csv_batch_57_72", "_csv_batch_73_88", "_csv_batch_89_102"):
        for k, v in json.loads((S / f"{f}.json").read_text("utf-8")).items():
            batch[int(k)] = v

    old = list(csv.reader(OLD_CSV.open(encoding="utf-8-sig")))
    assert old[0][:19] == HEADER[:19], f"旧表表头不符：{old[0][:19]}"
    old_rows = {int(r[0]): r for r in old[1:] if r and r[0].strip().isdigit()}

    rows, warn, apa_fix = [], [], []
    for i in range(1, 103):
        nc, a = newc[str(i)], apa[str(i)]
        # ★APA 两列一律以 apa_refs.json 为准：_csv_newcols.json 生成于同作者同年
        # 后缀（2016a/b、2024a/b、2025a/b）与中文姓名更正之前，有 10 条已过期。
        if nc["APA引注"] != a["intext"]:
            apa_fix.append(f"#{i} {nc['APA引注']} -> {a['intext']}")
        five = [nc["资料来源"], nc["证据强度"], a["intext"], a["apa"], nc["所属实验"]]
        if i in old_rows and i <= 39:
            r = old_rows[i][:19]
            r += [""] * (19 - len(r))
            rows.append(r + five)
            continue

        p = meta[i]
        b = batch.get(i)
        if b is None:
            raise SystemExit(f"#{i} 缺少内容字段（batch JSON 未覆盖）")
        content = []
        for c in CONTENT_COLS:
            v = clean(OVERRIDES.get(i, {}).get(c) or b.get(c, ""))
            if not v:
                v = "摘要未报告" if nc["资料来源"] == "仅摘要" else "论文未明确报告"
                warn.append(f"#{i} {c} 为空，已按资料来源填占位")
            content.append(v)
        au = AUTHOR_FIX.get(i) or [clean(x) for x in (p.get("authors") or []) if clean(x)]
        short, jcr = venue_of(i, p.get("venue") or "")
        yr = year_of(i, a, p.get("year"))
        rows.append([str(i), clean(p["title"])] + content
                    + [", ".join(au[:3]) or "（团体作者）",
                       au[0] if au else "SAE International", yr,
                       f"{short} {yr}", jcr] + five)

    # ── 写出 ──────────────────────────────────────────────────────────────
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(HEADER)
        w.writerows(rows)
    with OUT_TSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(HEADER)
        w.writerows([[c.replace("\t", " ") for c in r] for r in rows])

    def esc(s: str) -> str:
        return s.replace("|", "\\|").replace("\n", "<br>")

    md = ["# AR-HUD 行人碰撞预警文献综合表（102 篇 × 24 列）", "",
          f"共 {len(rows)} 篇。第 20–24 列（★）为本轮新增：资料来源、证据强度、"
          "APA 引注、APA 条目、所属实验。", "",
          "| " + " | ".join(HEADER) + " |",
          "|" + "|".join(["---"] * len(HEADER)) + "|"]
    md += ["| " + " | ".join(esc(c) for c in r) + " |" for r in rows]
    OUT_MD.write_text("\n".join(md) + "\n", encoding="utf-8")

    # ── 自检 ──────────────────────────────────────────────────────────────
    assert len(rows) == 102, len(rows)
    bad = [r[0] for r in rows if len(r) != 24]
    assert not bad, f"列数不为 24 的行：{bad}"
    assert [r[0] for r in rows] == [str(i) for i in range(1, 103)], "序号不连续"
    empty = [(r[0], HEADER[j]) for r in rows for j in range(len(r)) if not r[j].strip()]
    print(f"OK  {len(rows)} 行 × {len(HEADER)} 列 -> {OUT_CSV.name} / .tsv / .md")
    if apa_fix:
        print(f"已按 apa_refs.json 更正 APA 引注 {len(apa_fix)} 条：")
        for x in apa_fix:
            print("  ", x)
    if empty:
        print(f"⚠ 空单元 {len(empty)} 处：{empty[:12]}")
    for w_ in warn[:20]:
        print("  ", w_)
    if len(warn) > 20:
        print(f"   …另有 {len(warn) - 20} 条")


if __name__ == "__main__":
    main()
