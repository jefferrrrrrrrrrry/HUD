#!/usr/bin/env python3
"""重建研究汇报讲稿：第 1 章 14 讲述页 + 第 2 章 10 备查页。"""
import re
from pathlib import Path

P = Path("研究汇报_2026_08_讲稿.md")
s = P.read_text(encoding="utf-8")
# 结构保持：标题行、讲稿、只说一句、计时，与现有格式一致
head = s.split("## p01")[0]
print(f"头部 {len(head)} 字，开头：{head.splitlines()[0][:60]}")
print(f"旧页数：{len(re.findall(r'^## p', s, re.M))}")
print("--- 旧 p01 示例 ---")
print(s[s.index("## p01"):s.index("## p02")][:700])
