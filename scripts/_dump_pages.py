#!/usr/bin/env python3
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
s = (ROOT / "文献综述_幻灯片.html").read_text(encoding="utf-8")
secs = re.findall(r'<section class="slide.*?</section>', s, re.S)
pages = [int(x) for x in sys.argv[1:]] or [8]
for p in pages:
    t = re.sub(r"\n\s*\n", "\n", secs[p - 1])
    print(f"\n\n=========== PAGE {p} ===========")
    print(t)
