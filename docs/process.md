# Process

This file will serve as documentation for [process.py](../process.py)

    import pdf2image
    import process

    pages = pdf2image.convert_from_path(
        pdf_path = '../path/to/file.pdf',
        dpi=200,
        size=(1654,2340))

### extract_from(pdf_pages)

Transform a PDF into readable python friendly strings. This function returns an array whereas each item represents one page of a PDF document.

- **limit**: The number of pages that you want to read. This value starts from 0, this means limit=2 returns an array of length 3
- **pdf_pages**: This parameter takes an array of pdf pages. You can use pdf2image as described in the example above.

_Example_

    process.save_as_images(pdf_pages = pages, limit= 1)

    output<array>:
    ["this is the text of page 1", "this is the text of page 2"]
