#!/usr/bin/env python3
"""把本轮两项核查结果写进框架文档：§14.9 增列第 7 条勘误，§14.10 更新不透明度行。

§14.9 第 7 条：期刊分区与影响因子的 7 处更正（含 2 处分区错判）。
§14.10 第 1 行：不透明度记法已由引用链间接裁定，待核性质从「不可用」降为「待原文确认」。
幂等：已含标记则跳过。
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "AR-HUD行人碰撞预警_毕业论文研究框架.md"

ERRATA_7 = (
    "| **7** | **期刊分区与影响因子**：文献综合表 `JCR分区` 列有 **7 刊与 WoS 官方数据不符**，"
    "其中 **2 处分区判错**——*Applied Ergonomics* 记 Q1、实为 **Q2**（JIF 百分位 70.4%，未过 75 分位线）；"
    "*IET Intelligent Transport Systems* 记 Q2、实为 **Q3**（百分位 49.6%）；"
    "另 5 处为 IF 数值偏差：*Human Factors* 3.4→**3.6**、IEEE T-ITS 7.9→**9.1**、"
    "IJHCI 4.9→**6.1**、TVCG 6.5→**6.8**、*J SID* 2.2→**2.0**。"
    "此外 3 刊此前只填分区、IF 记作「未核验」 | "
    "逐刊比对 Web of Science / JCR 数据后更正（核验脚本 `scripts/verify_jcr_if.py`，"
    "离线快照 `scripts/_jcr_verified.json`，更正脚本 `scripts/fix_jcr_values.py`）；"
    "分区一律按 **JIF 百分位 75 / 50 / 25** 判定。3 刊补齐为 *Ann NY Acad Sci* **Q1 IF 4.5**"
    "（原记 Q2 亦错，百分位 82.9%）、TRIP **Q2 IF 4.8**（ESCI）、"
    "*Int J Vehicle Design* **Q4 IF 0.7**（出版商官网公示的 Clarivate 指标）。"
    "**未采用聚合站数值**——同一刊在 resurchify / research.com / journalseeker 上"
    "给出 2.6 / 3.8 / 4.55 / 4.87 / 5.69 五个互斥数字，均非 JCR 的 JIF。"
    "*Human Factors* 的 IF 被综述 §2.1、幻灯片与本文档 §14.1 三处正文直接引用，"
    "已同步改为 3.6 |"   # 表格只有 3 列，末段并入「更正」列，勿再拆单元格
)

OLD_1410 = (
    "| 不透明度记法（透明度 vs 不透明度）与 0.2／0.6 冲突 | "
    "Li et al. (2025)、Lopez et al. (2025)、Hou et al. (2024) 三篇均仅摘要，记法互不一致 | "
    "**实验 3 四个 AR 条件的视觉参数取值** |"
)

NEW_1410 = (
    "| 不透明度记法（透明度 vs 不透明度）与 0.2／0.6 冲突 | "
    "**已由引用链间接裁定**：Ye 与 Yin (2025) 在方法节把 Hou et al. (2024) 的 T 标尺"
    "当作「提升**可见性**的 0.75」使用，故 T 功能上是 alpha（不透明度），"
    "四源收敛于 **0.6–0.75**；Lopez et al. (2025) 原文为「20% 与 60% **均**支持情境意识」，"
    "**并未推荐 20%**，与 ≥ 0.6 不构成冲突。三篇仍仅摘要，"
    "**须由原文的参数定义作最终确认**（证据等级：间接） | "
    "实验 3 主条件定为 **0.6**（四源交集的保守下界）；0.2 档保留，"
    "但检验目的改为「遮挡收益是否超过可读性代价」 |"
)


def main() -> None:
    s = DOC.read_text("utf-8")
    n = 0

    if "| **7** | **期刊分区与影响因子**" in s:
        print("SKIP §14.9 第 7 条（已存在）")
    else:
        anchor = "\n### 14.10 仍需取得一手文献才能引用的清单"
        assert anchor in s, "找不到 §14.10 标题"
        head, tail = s.split(anchor, 1)
        # 表格末行后插入；末行是第 6 条
        assert head.rstrip().endswith("|"), "§14.9 表格末行异常"
        s = head.rstrip() + "\n" + ERRATA_7 + anchor + tail
        n += 1
        print("OK   §14.9 增列第 7 条（期刊分区与影响因子）")

    if NEW_1410.split(" | ")[1][:24] in s:
        print("SKIP §14.10 不透明度行（已更新）")
    else:
        assert OLD_1410 in s, "找不到 §14.10 不透明度行"
        s = s.replace(OLD_1410, NEW_1410, 1)
        n += 1
        print("OK   §14.10 不透明度行已更新为「已间接裁定」")

    DOC.write_text(s, encoding="utf-8")
    print(f"\n共改 {n} 处")


if __name__ == "__main__":
    main()
