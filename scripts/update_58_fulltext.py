#!/usr/bin/env python3
"""#58（SPIDER 2.0）由「仅摘要」升级为「全文精读」后的下游同步。

改动
  1. papers_metadata.json：登记本地 PDF／全文、has_fulltext、is_oa、license、卷期页、PMID
  2. scripts/_csv_newcols.json：资料来源 仅摘要 → 全文精读
  3. scripts/_csv_batch_57_72.json：12 个内容列按全文重写（原为摘要口径）
幂等：已改则跳过。
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PDF = "papers/58_SPIDER 2.0- Driver Distraction and Visual Attention.pdf"
TXT = "extracted_text/58_2025_SPIDER2.0_Strayer_McDonnell.txt"

CONTENT = {
    "场景": (
        "无实验场景。本篇为受邀叙述性综述（PubMed 出版类型 Review，无 PRISMA、无元分析、"
        "118 篇参考文献），不含模拟器、实车、视频或算法仿真；无道路类型、无车速、无行人冲突形式。"
        "全文与本课题场景相关的唯一表述在 Scanning 一节：威胁常首先出现在周边视野，"
        "原文举例即「一名分心的行人正在横穿」，多任务造成的隧道视野降低了及时发现这类威胁的可能。"),
    "色彩显示": (
        "论文未涉及任何显示设计参数。全文检索「head-up display」出现 0 次；"
        "唯一一次提及 AR 显示在 FUTURE ISSUES 第 4 条，把「增强现实仪表（augmented reality "
        "dashboards）」与语音助手、信息娱乐系统并列为**待研究的新型分心源**。"),
    "位置": (
        "论文未涉及呈现位置或空间参照系。可迁移的是一条否定性约束："
        "无意视盲可发生于「直接位于视线之内」的信息（look-but-failed-to-see），"
        "故「把图形放到视线中央即可保证被感知」不成立；且原文指出即使不含视觉成分的次任务"
        "也使注视向场景中心集中，AR 图形长期占据中心区可能与该趋势叠加。"),
    "形状": "论文未涉及图形形态（无箭头/框/条等形状讨论）。",
    "动静态": "论文未涉及动效、闪烁频率或占空比。",
    "预警信息出现时间": (
        "本篇不给任何 TTC/提前量阈值。可用于时序设计的唯一数值是恢复动态："
        "次任务结束后分心影响仍持续 30 s 以上（转述 Strayer et al. 2022b），"
        "据此本课题把同一被试相邻危险事件的间隔定为 ≥ 60 s。"
        "此外须注意记法冲突：本篇 Figure 2 的 t0 = 次任务开始时刻，"
        "与本课题 t0 = 驾驶员自发察觉时刻含义不同。"),
    "预警信息持续时间": "论文未报告任何预警持续时长或撤销策略。",
    "预警信息是否有分级": (
        "论文不涉及预警分级。但其阶段划分为分级设计提供了归属依据："
        "低行动要求的提示作用于 Scanning/Predicting，高行动要求的报警作用于 "
        "Decision-making/Executing，二者最优提前量不可互相迁移。"),
    "实验任务": (
        "无被试实验。全文的实质贡献之一是系统化了四类测量方法及其边界（pp. 524–526）："
        "① 视觉遮挡（产出最小安全离路视线时间，须与绩效评估配对，仅限模拟器/封闭道路）；"
        "② 探测响应任务 DRT（ISO 17488:2016，刺激间隔 3–5 s，LED 变体测视觉注意，"
        "但不能捕获离路视线时长、未必与实际瞥视时刻对齐）；"
        "③ 眼动（注视率、扫视、瞥视编码、眨眼、注视分散度）；"
        "④ EEG（α 8–12 Hz 与视觉注意反向；P300 幅值随次任务需求升高而下降）。"),
    "自变量": (
        "不适用（无被试实验）。框架层的自变量类比是「是否从事与驾驶无关的次任务」"
        "及其心理需求与时间需求（原文：任务越长、越难，SA 损害越大）。"),
    "因变量": (
        "不适用（无实测指标）。全文给出的阶段代理量为：Scanning—注视中心化与注视分散度、"
        "隧道视野；Predicting—预期性注视（anticipatory glances）；"
        "Identification—识别记忆与 LBFTS/无意视盲率；Decision-making—间隙接受与安全边际"
        "（标准协议为 ISO 26022 换道任务）；Executing—反应时及其分布偏斜。"),
    "结果": (
        "① 五阶段 SPIDER 依赖有限注意容量，是建立与维持情境意识的必要过程；"
        "Figure 1 中只有 S、P、I 与 SA 之间是双向箭头，D 与 ER 是 SA 的下游，"
        "故把五阶段画成单向串行链属误读。② Endsley 层级映射（原文明确）："
        "Scanning↔层级 1（感知）、Identification↔层级 2（理解）、Predicting↔层级 3（预测）。"
        "③ 本篇最关键的量化命题：任一 SPIDER 过程的成功完成概率下降 5%，"
        "即可使相对碰撞风险翻倍（转述 Fisher & Strayer 2014）——即 SPIDER 是"
        "**成功概率模型而非耗时预算模型**，全文不含任何阶段耗时值。"
        "④ 恢复动态（Figure 2，以信息论为基础）：t0 次任务开始 → t1 结束 → t2 恢复完成，"
        "分心影响在任务结束后仍持续 30 s 以上。⑤ 差错占比（NMVCCS，Singh 2015）："
        "人因差错占碰撞 94%，其中识别类 41%、决策类 33%、操作类 11%、非操作类 7%、其他 8%"
        "——识别类是操作类的近 4 倍，支持把干预点放在 S/I 阶段。"
        "⑥ 其他转述数值：通话使已注视物体的再认记忆下降约 50%（Strayer et al. 2003）；"
        "次任务使反应时分布右偏、慢反应尾部被格外拉长（Ratcliff & Strayer 2014）。"),
}


def main() -> None:
    n = 0

    # 1) papers_metadata.json
    p = ROOT / "papers_metadata.json"
    meta = json.loads(p.read_text("utf-8"))
    for rec in meta:
        if rec.get("idx") != 58:
            continue
        if rec.get("has_fulltext") and rec.get("local_pdf"):
            print("SKIP papers_metadata（已登记）")
            break
        rec.update({
            "local_pdf": str(ROOT / PDF),
            "local_text": str(ROOT / TXT),
            "has_fulltext": True,
            "has_pdf": True,
            "is_oa": True,
            "oa_status": "hybrid",
            "license": "cc-by",
            "pmid": "40216457",
            "volume": "11", "issue": "1", "pages": "521-540",
            "text_chars": len((ROOT / TXT).read_text("utf-8")),
            "fulltext_note": ("CC BY 4.0；出版商站点对本机出口 IP 一律 403（Cloudflare），"
                              "PDF 由用户经机构网络下载后置入 papers/。"),
        })
        p.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        n += 1
        print("OK   papers_metadata.json #58 已登记全文")
        break

    # 2) _csv_newcols.json
    p = ROOT / "scripts" / "_csv_newcols.json"
    nc = json.loads(p.read_text("utf-8"))
    if nc["58"]["资料来源"] == "全文精读":
        print("SKIP _csv_newcols（已改）")
    else:
        nc["58"]["资料来源"] = "全文精读"
        p.write_text(json.dumps(nc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        n += 1
        print("OK   _csv_newcols.json #58 资料来源 → 全文精读")

    # 3) _csv_batch_57_72.json 的 12 个内容列
    p = ROOT / "scripts" / "_csv_batch_57_72.json"
    b = json.loads(p.read_text("utf-8"))
    if "成功概率模型" in b["58"]["结果"]:
        print("SKIP _csv_batch_57_72（已改）")
    else:
        b["58"].update(CONTENT)
        b["58"]["证据强度"] = "弱"          # 设计参数层仍无数值，故不上调
        p.write_text(json.dumps(b, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        n += 1
        print("OK   _csv_batch_57_72.json #58 十二个内容列已按全文重写")

    print(f"\n共改 {n} 处；后续：cp /tmp/backup_master_39.csv 后重跑 build_master_csv.py")


if __name__ == "__main__":
    main()
