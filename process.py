import pandas as pd
import pytesseract as pt
import pdf2image


# take a pdf file an create an image for each page
def save_as_images(pdf_pages):
    for page in range(len(pdf_pages)):
        pdf_pages[page].save('images/img' + str(page) + '.jpg')

    print(pdf_pages)


# this function returns an array of strings
# whereas each string represents one page of a single document
def extract_from(pdf_pages, limit):
    pages = []
    index = 0
    while index <= limit:
        content = pt.image_to_string(pdf_pages[index], lang='spa')
        pages.append(content)
        index = index + 1
    return pages

