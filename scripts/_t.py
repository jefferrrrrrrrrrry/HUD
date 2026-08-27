from pathlib import Path

TITLE = [
    "thesis/_parts/talk_p01_12.md",
    "文献综述_幻灯片_讲稿.md",
    "文献综述_幻灯片.html",
    "研究汇报_2026_08_讲稿.md",
    "AR-HUD行人碰撞预警_毕业论文研究框架.md",
    "研究汇报_2026_08.html",
    "时间元素设计参数_专题分析.md",
]
OLD = "风险加工与避险绩效"
NEW = "情境意识与避险绩效"

for rel in TITLE:
    p = Path(rel)
    s = p.read_text(encoding="utf-8")
    n = s.count(OLD)
    if n:
        p.write_text(s.replace(OLD, NEW), encoding="utf-8")
    print(f"  {'✓' if n else '·'} {rel:46s} {n} 处")

p = Path("AR-HUD行人碰撞预警_毕业论文研究框架.md")
s = p.read_text(encoding="utf-8")
o = "对驾驶员风险加工各阶段的作用路径"
assert s.count(o) == 1
p.write_text(s.replace(o, "对驾驶员情境意识各层级的作用路径"), encoding="utf-8")
print("  ✓ 框架 §摘要「风险加工各阶段」→「情境意识各层级」")
print("\n保留（理论概念名，非题目）：优化方案「四阶段风险加工链」、框架 §3.3、plot_ar_hud_thesis_framework.py")
