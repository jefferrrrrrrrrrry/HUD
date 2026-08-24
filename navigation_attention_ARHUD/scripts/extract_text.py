"""提取已下载PDF的文本 + 用Jina补全失败的"""
import os
import re
import json
import subprocess
import time
import urllib.parse
import urllib.request
import pathlib

ROOT = pathlib.Path("/home/gezhuocheng/moe/HUD/navigation_attention_ARHUD")
PAPERS = ROOT / "papers"
EXTRACTED = ROOT / "extracted_text"
LOG = ROOT / "download_log.json"
META = ROOT / "metadata_filtered.json"

EXTRACTED.mkdir(parents=True, exist_ok=True)

PROXY = "http://oversea-squid2.ko.txyun:11080"

def extract_pdf_text(pdf_path, txt_path):
    """用 PyMuPDF 提取"""
    try:
        import fitz
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text() + "\n\n"
        doc.close()
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(text)
        return len(text)
    except Exception as e:
        print(f"  提取失败: {e}")
        return 0

def fetch_jina(url, timeout=60):
    """通过 Jina r.jina.ai 获取页面纯文本"""
    jina_url = f"https://r.jina.ai/{url}"
    try:
        proxy_handler = urllib.request.ProxyHandler({"http": PROXY, "https": PROXY})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [
            ('User-Agent', 'Mozilla/5.0'),
            ('Accept', 'text/plain'),
        ]
        with opener.open(jina_url, timeout=timeout) as resp:
            return resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"    Jina失败: {e}")
        return None

def safe_filename_txt(idx, year, title):
    title_clean = re.sub(r"[^\w\s-]", "", title).strip()
    title_clean = re.sub(r"\s+", "_", title_clean)[:100]
    return f"{idx:02d}_{year}_{title_clean}.txt"


def main():
    with open(META) as f:
        records = json.load(f)['records']
    with open(LOG) as f:
        dl_log = json.load(f)
    
    extract_count = 0
    jina_count = 0
    skip_count = 0
    
    for i, p in enumerate(records, 1):
        idx_str = str(i)
        title = p.get('title', '')
        year = p.get('year', '')
        doi = p.get('doi', '')
        out_txt = EXTRACTED / safe_filename_txt(i, year, title)
        
        if out_txt.exists() and out_txt.stat().st_size > 1000:
            skip_count += 1
            continue
        
        # 路径1: 用已下载的PDF
        if dl_log.get(idx_str, {}).get('success') and dl_log[idx_str].get('via') != 'jina':
            fname = dl_log[idx_str]['file']
            pdf_path = PAPERS / fname
            if pdf_path.exists() and pdf_path.stat().st_size > 50000:
                size = extract_pdf_text(str(pdf_path), str(out_txt))
                if size > 1000:
                    print(f"[{i:02d}] PDF提取 → {size} 字符")
                    extract_count += 1
                    continue
        
        # 路径2: Jina 抓取摘要级
        if doi:
            doi_url = f"https://doi.org/{doi}"
            print(f"[{i:02d}] Jina尝试: {doi_url}")
            content = fetch_jina(doi_url)
            if content and len(content) > 500:
                with open(out_txt, 'w', encoding='utf-8') as f:
                    f.write(f"# 来源: Jina @ {doi_url}\n\n{content}")
                print(f"     ✓ {len(content)} 字符")
                jina_count += 1
                # 更新log
                if idx_str not in dl_log:
                    dl_log[idx_str] = {}
                dl_log[idx_str]['jina_text'] = True
                dl_log[idx_str]['jina_size'] = len(content)
                time.sleep(2)
                continue
            else:
                print(f"     ✗ 内容过短或失败")
        
        # 路径3: 仅写元数据兜底
        with open(out_txt, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            f.write(f"作者: {', '.join(p.get('authors', []))}\n")
            f.write(f"年份: {year}\n")
            f.write(f"期刊: {p.get('venue', '')}\n")
            f.write(f"DOI: {doi}\n")
            f.write(f"引用数: {p.get('cited_by_count', 0)}\n\n")
            f.write(f"## Abstract\n\n{p.get('abstract', '')}\n")
        print(f"[{i:02d}] 仅元数据 → {len(p.get('abstract', ''))} 字符")
    
    with open(LOG, 'w', encoding='utf-8') as f:
        json.dump(dl_log, f, ensure_ascii=False, indent=2)
    
    print(f"\n=== Summary ===")
    print(f"  PDF提取: {extract_count}")
    print(f"  Jina补全: {jina_count}")
    print(f"  已跳过: {skip_count}")
    print(f"  总文件: {len(list(EXTRACTED.iterdir()))}")


if __name__ == '__main__':
    main()
