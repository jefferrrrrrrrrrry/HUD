#!/usr/bin/env python3
"""Extract text from newly downloaded PDFs."""
import os
import pathlib
import fitz  # PyMuPDF

PAPERS = pathlib.Path("/home/gezhuocheng/HUD/papers")
TEXTS = pathlib.Path("/home/gezhuocheng/HUD/extracted_text")

extracted = 0
failed = []

for pdf_path in sorted(PAPERS.glob("*.pdf")):
    base = pdf_path.stem
    out_txt = TEXTS / f"{base}.txt"
    if out_txt.exists() and out_txt.stat().st_size > 1000:
        continue
    print(f"Extracting: {base}")
    try:
        doc = fitz.open(str(pdf_path))
        text_parts = []
        for page_num, page in enumerate(doc, 1):
            text_parts.append(f"--- Page {page_num} ---\n{page.get_text()}")
        doc.close()
        full_text = "\n".join(text_parts)
        out_txt.write_text(full_text, encoding="utf-8")
        print(f"  -> {len(full_text)} chars, {page_num} pages")
        extracted += 1
    except Exception as e:
        print(f"  ERROR: {e}")
        failed.append((base, str(e)))

print(f"\nExtracted: {extracted}")
print(f"Failed: {len(failed)}")
for b, e in failed:
    print(f"  {b}: {e}")
