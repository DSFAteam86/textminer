import pandas as pd
import pytesseract as pt
import pdf2image


def extract_from(pdf_pages, limit):
    pages = []
    index = 0
    while index <= limit:
        content = pt.image_to_string(pdf_pages[index], lang='spa')
        pages.append(content)
        index = index + 1
    return pages
