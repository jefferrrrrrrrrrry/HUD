import re, pathlib, sys
s = pathlib.Path("研究汇报_2026_08.html").read_text(encoding="utf-8")
secs = re.findall(r'<section class="slide.*?</section>', s, re.S)
for i in [int(x) - 1 for x in sys.argv[1:]]:
    t = re.sub(r"<[^>]+>", "｜", secs[i])
    t = re.sub(r"｜{2,}", "｜", t)
    t = re.sub(r"\s+", " ", t)
    print(f"══════ p{i+1}")
    print(t.strip())
    print()
