import os
import fitz  # PyMuPDF
import json
import re
from collections import Counter

INPUT_DIR = '/app/input'
OUTPUT_DIR = '/app/output'

HEADING_LEVELS = ['H1', 'H2', 'H3']

# Heuristic: font size, boldness, position, numbering, all-caps

def extract_title(doc):
    # Try metadata first
    title = doc.metadata.get('title')
    if title and title.strip():
        return title.strip()
    # Else, use largest text on first page
    page = doc[0]
    blocks = page.get_text('dict')['blocks']
    candidates = []
    for b in blocks:
        if 'lines' in b:
            for l in b['lines']:
                for s in l['spans']:
                    candidates.append((s['size'], s['text']))
    if candidates:
        # Largest font size, non-empty, not just numbers
        candidates = [c for c in candidates if c[1].strip() and not c[1].strip().isdigit()]
        if candidates:
            return max(candidates, key=lambda x: x[0])[1].strip()
    return "Untitled Document"

def detect_headings(doc):
    headings = []
    font_stats = Counter()
    # First, collect font sizes and styles for all text
    for page_num, page in enumerate(doc, 1):
        blocks = page.get_text('dict')['blocks']
        for b in blocks:
            if 'lines' in b:
                for l in b['lines']:
                    for s in l['spans']:
                        font_stats[(s['size'], s['font'], s.get('flags', 0))] += 1
    # Find the most common font size (body text)
    if not font_stats:
        return headings
    most_common_size = font_stats.most_common(1)[0][0][0]
    # Heuristic: headings are larger, bold, or all-caps, or numbered
    for page_num, page in enumerate(doc, 1):
        blocks = page.get_text('dict')['blocks']
        for b in blocks:
            if 'lines' in b:
                for l in b['lines']:
                    for s in l['spans']:
                        text = s['text'].strip()
                        if not text or len(text) < 3:
                            continue
                        size = s['size']
                        font = s['font']
                        flags = s.get('flags', 0)
                        is_bold = 'Bold' in font or (flags & 2)
                        is_caps = text.isupper() and len(text) > 4
                        is_numbered = bool(re.match(r'^(\d+\.|[A-Z]\.|[IVXLC]+\.|[a-z]\.)', text))
                        # Heading level by size difference
                        if size > most_common_size:
                            if size > most_common_size + 5:
                                level = 'H1'
                            elif size > most_common_size + 2:
                                level = 'H2'
                            else:
                                level = 'H3'
                        elif is_bold or is_caps or is_numbered:
                            level = 'H3'
                        else:
                            continue
                        # Avoid duplicates, skip body text
                        if len(text.split()) > 30:
                            continue
                        headings.append({
                            'level': level,
                            'text': text,
                            'page': page_num
                        })
    # Remove duplicates (same text, same page, same level)
    seen = set()
    unique_headings = []
    for h in headings:
        key = (h['level'], h['text'], h['page'])
        if key not in seen:
            unique_headings.append(h)
            seen.add(key)
    return unique_headings

def process_pdf(pdf_path, output_path):
    doc = fitz.open(pdf_path)
    title = extract_title(doc)
    outline = detect_headings(doc)
    result = {
        'title': title,
        'outline': outline
    }
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    doc.close()

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(INPUT_DIR, filename)
            output_filename = os.path.splitext(filename)[0] + '.json'
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            try:
                process_pdf(pdf_path, output_path)
                print(f"Processed {filename} -> {output_filename}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

if __name__ == '__main__':
    main() 