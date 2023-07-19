import fitz  # PyMuPDF

def convert_pdf_to_images(pdf_filename, zoom):

    pdf_document = fitz.open(pdf_filename)

    # Save each page as an image
    image_paths = []
    for i in range(pdf_document.page_count):
        page = pdf_document.load_page(i)
        image = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
        image_path = f"CV.png"  # Save as PNG format
        image.save(image_path)
        image_paths.append(image_path)

    # Close the PDF document
    pdf_document.close()

    return image_paths

# Usage example (assuming 'example.pdf' is the PDF file in the same folder)
pdf_filename = 'cv-aaron.pdf'
converted_images = convert_pdf_to_images(pdf_filename, zoom=5)
print("Images converted successfully:", converted_images)
