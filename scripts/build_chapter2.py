#!/usr/bin/env python3
"""拼接第 2 章文献综述各分节，并追加 APA 7th 参考文献表。

分节文件位于 thesis/_parts/，按 ORDER 顺序拼接到 thesis/第2章_文献综述_v2.md 之后。
参考文献表分两部分：理论与方法学文献（人工核验，硬编码于本脚本）+ 本库 102 篇
（读 scripts/apa_refs.json，按 sort_key 排序）。
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "thesis" / "第2章_文献综述_v2.md"
PARTS = ROOT / "thesis" / "_parts"
ORDER = ["sec2_1.md", "sec2_2a.md", "sec2_2b.md", "sec2_3.md", "sec2_4.md", "sec2_5_6.md"]

THEORY = """Bliss, J. P., & Acton, S. A. (2003). Alarm mistrust in automobiles: How collision alarm reliability affects driving. *Applied Ergonomics, 34*(6), 499–509. https://doi.org/10.1016/j.apergo.2003.07.003

Bliss, J. P., Gilson, R. D., & Deaton, J. E. (1995). Human probability matching behaviour in response to alarms of varying reliability. *Ergonomics, 38*(11), 2300–2312. https://doi.org/10.1080/00140139508925269

Dixon, S. R., Wickens, C. D., & McCarley, J. S. (2007). On the independence of compliance and reliance: Are automation false alarms worse than misses? *Human Factors, 49*(4), 564–572. https://doi.org/10.1518/001872007X215656

Endsley, M. R. (1995). Toward a theory of situation awareness in dynamic systems. *Human Factors, 37*(1), 32–64. https://doi.org/10.1518/001872095779049543

Green, D. M., & Swets, J. A. (1966). *Signal detection theory and psychophysics*. Wiley.

Holmqvist, K., Nyström, M., Andersson, R., Dewhurst, R., Jarodzka, H., & van de Weijer, J. (2011). *Eye tracking: A comprehensive guide to methods and measures*. Oxford University Press.

Jian, J.-Y., Bisantz, A. M., & Drury, C. G. (2000). Foundations for an empirically determined scale of trust in automated systems. *International Journal of Cognitive Ergonomics, 4*(1), 53–71. https://doi.org/10.1207/S15327566IJCE0401_04

Lee, D. N. (1976). A theory of visual control of braking based on information about time-to-collision. *Perception, 5*(4), 437–459. https://doi.org/10.1068/p050437

Norman, D. A. (1988). *The psychology of everyday things*. Basic Books.

Posner, M. I. (1980). Orienting of attention. *Quarterly Journal of Experimental Psychology, 32*(1), 3–25. https://doi.org/10.1080/00335558008248231

Rasmussen, J. (1983). Skills, rules, and knowledge; signals, signs, and symbols, and other distinctions in human performance models. *IEEE Transactions on Systems, Man, and Cybernetics, SMC-13*(3), 257–266. https://doi.org/10.1109/TSMC.1983.6313160

Sokolov, E. N. (1963). *Perception and the conditioned reflex*. Pergamon Press.

Straughn, S. M., Gray, R., & Tan, H. Z. (2009). To go or not to go: Stimulus-response compatibility for tactile and auditory pedestrian collision warnings. *IEEE Transactions on Haptics, 2*(2), 111–117. https://doi.org/10.1109/TOH.2009.15

Strayer, D. L., & Fisher, D. L. (2016). SPIDER: A framework for understanding driver distraction. *Human Factors, 58*(1), 5–12. https://doi.org/10.1177/0018720815619074

Theeuwes, J. (1992). Perceptual selectivity for color and form. *Perception & Psychophysics, 51*(6), 599–606. https://doi.org/10.3758/BF03211656

Vicente, K. J., & Rasmussen, J. (1992). Ecological interface design: Theoretical foundations. *IEEE Transactions on Systems, Man, and Cybernetics, 22*(4), 589–606. https://doi.org/10.1109/21.156574

Wickens, C. D. (2002). Multiple resources and performance prediction. *Theoretical Issues in Ergonomics Science, 3*(2), 159–177. https://doi.org/10.1080/14639220210123806

Yantis, S., & Hillstrom, A. P. (1994). Stimulus-driven attentional capture: Evidence from equiluminant visual objects. *Journal of Experimental Psychology: Human Perception and Performance, 20*(1), 95–107. https://doi.org/10.1037/0096-1523.20.1.95
"""

HEAD = """
---

## 参考文献

> **生成与核验说明**：本表分两部分。§A 为理论与方法学文献，逐条人工核验一手题录。§B 为本库 102 篇文献，由 `scripts/apa_refs.json` 生成，逐条经 Crossref（按 DOI）、theses.fr（按 NNT）、arXiv API 核验，人工修正 15 处出版商记录错误——中文作者 given/family 颠倒 3 条、完整姓名误置于 family 字段 4 条、期刊名 HTML 实体 3 条、学位论文授予机构 2 条、团体作者 1 条、arXiv 预印本被误匹配 3 条（另有 6 条因同一第一作者同年发表而加 a/b 后缀）。逐条预览见 `scripts/apa_refs_preview.md`。
>
> **两点使用提示**：（1）文章标题的大小写按出版商记录**原样转录**，未做 sentence-case 自动转换，以避免误伤专有名词与缩略语；若学校格式要求 sentence case，须人工逐条调整。（2）§B 按第一作者姓氏字母序排列，序号为本课题文献库内部编号（`#N`），便于回溯到 `summaries/` 的精读笔记，正式定稿时应删除该编号。

### A　理论与方法学文献

"""


def main() -> None:
    body = ""
    for name in ORDER:
        p = PARTS / name
        assert p.exists(), f"缺少分节文件 {p}"
        body += p.read_text(encoding="utf-8")

    body += HEAD + THEORY

    refs = json.loads((ROOT / "scripts" / "apa_refs.json").read_text(encoding="utf-8"))
    items = sorted(refs.items(), key=lambda kv: (str(kv[1]["sort_key"][0]).lower(), kv[1]["sort_key"][1]))
    body += "\n### B　本库文献（102 篇，按第一作者姓氏字母序）\n\n"
    for idx, e in items:
        body += f"[#{idx}] {e['apa']}\n\n"

    MAIN.write_text(body, encoding="utf-8")

    n_ch = len(re.findall(r"[\u4e00-\u9fff]", body))
    print(f"写入 {MAIN}")
    n_tbl = sum(1 for ln in body.splitlines() if set(ln.strip()) <= set("|-: ") and "---" in ln)
    print(f"  总字符 {len(body):,} | 汉字 {n_ch:,} | 表格 {n_tbl} 张 | 分节 {len(ORDER)}")
    print(f"  参考文献 A {THEORY.count('https://') + 3} 条（含 3 条无 DOI 专著）| B {len(items)} 条")


if __name__ == "__main__":
    main()
