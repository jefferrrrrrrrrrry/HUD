import re
from pathlib import Path

TALKS = ["研究汇报_2026_08_讲稿.md", "文献综述_幻灯片_讲稿.md",
         "盲区框架/研究汇报_双情境框架_讲稿.md",
         "盲区框架/开题报告_双情境框架_讲稿.md",
         "盲区框架/文献综述_盲区情境_讲稿.md"]
RATE = 245


def clean(t):
    return len(re.sub(r"[\s*`>|#—－\-]", "", t))


for f in TALKS:
    s = Path(f).read_text(encoding="utf-8")
    parts = re.split(r"^## (p\d+)[　 ]", s, flags=re.M)
    pages = [(parts[i], parts[i + 1]) for i in range(1, len(parts), 2)]
    quota = 0
    verbatim = 0
    one_over = []
    ref_pages = 0
    for pid, body in pages:
        m = re.search(r"\*\*⏱ (\d+):(\d{2})\*\*", body)
        sec = int(m.group(1)) * 60 + int(m.group(2)) if m else 0
        quota += sec
        seg = re.search(r"\*\*讲稿：\*\*(.*?)(?:\*\*只说一句|\*\*备答|$)", body, re.S)
        n = clean(seg.group(1)) if seg else 0
        if "不讲，备查" in body:
            ref_pages += 1
            continue
        verbatim += n
        one = re.search(r"\*\*只说一句：\*\*(.*?)(?:\n\n|\*\*备答)", body, re.S)
        m1 = clean(one.group(1)) if one else 0
        if sec and m1 * 60 / sec > 320:
            one_over.append(f"{pid} 只说一句 {m1} 字 / {sec} 秒 = {m1 * 60 / sec:.0f} 字/分")
    print(f"== {f}")
    print(f"   页数 {len(pages)}（备查 {ref_pages}）　配额合计 {quota // 60}:{quota % 60:02d}"
          f"　逐字稿 {verbatim} 字 ≈ {verbatim / RATE:.0f} 分（{RATE} 字/分）")
    if one_over:
        print(f"   ✗ 只说一句超配额 {len(one_over)} 页")
        for o in one_over[:12]:
            print("     ", o)
    else:
        print("   ✓ 每页「只说一句」均可在配额内讲完")
