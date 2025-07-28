from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar
from collections import defaultdict, Counter
import os

def extract_font_sizes_and_text(path):
    font_data = []
    for page_num, page_layout in enumerate(extract_pages(path), 1):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    line_text = text_line.get_text().strip()
                    if not line_text:
                        continue
                    sizes = [char.size for char in text_line if isinstance(char, LTChar)]
                    avg_size = sum(sizes)/len(sizes) if sizes else 0
                    font_data.append((avg_size, line_text, page_num))
    return font_data

def classify_headings(font_data):
    sizes = [round(item[0]) for item in font_data if item[0] > 0]
    common_sizes = sorted(set(Counter(sizes).most_common()), reverse=True)
    size_map = {}

    if not common_sizes:
        return [], ""

    sorted_sizes = sorted(set(sizes), reverse=True)

    size_map[sorted_sizes[0]] = "Title"
    if len(sorted_sizes) > 1:
        size_map[sorted_sizes[1]] = "H1"
    if len(sorted_sizes) > 2:
        size_map[sorted_sizes[2]] = "H2"
    if len(sorted_sizes) > 3:
        size_map[sorted_sizes[3]] = "H3"

    outline = []
    title = ""

    for size, text, page in font_data:
        label = size_map.get(round(size), None)
        if label == "Title" and not title:
            title = text
        elif label in {"H1", "H2", "H3"}:
            outline.append({
                "level": label,
                "text": text,
                "page": page
            })

    return outline, title

def extract_headings(pdf_path):
    font_data = extract_font_sizes_and_text(pdf_path)
    outline, title = classify_headings(font_data)
    return {
        "title": title,
        "outline": outline
    }
