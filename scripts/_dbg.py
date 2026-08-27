import sys, re, pathlib
sys.path.insert(0, 'scripts')
import html2pptx
html = pathlib.Path('研究汇报_2026_08.html').read_text(encoding='utf-8')
secs = re.findall(r'<section class="slide.*?</section>', html, re.S)
sec = secs[2]
bm = re.search(r'<div class="body">(.*)', sec, re.S)
body = bm.group(1)
body = re.sub(r'</div>\s*<div class="pg"></div>.*$', '', body, flags=re.S)
blocks = html2pptx.top_blocks(body)
blk = blocks[1].strip()
i = blk.index('<div class="row">')
print(repr(blk[i:i+430]))
print('---- tx 后的第一个 </div>:')
j = blk.index('<div class="tx">')
seg = blk[j:]
k = seg.index('</div>')
print(repr(seg[k-60:k+100]))
