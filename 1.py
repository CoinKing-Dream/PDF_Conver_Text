import PyPDF2

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file.
    
    Returns:
        str: Extracted text from the PDF file.
    """
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for page_number in range(num_pages):
            page = reader.getPage(page_number)
            text += page.extractText()
    return text

pdf_path = "1.pdf"  # Replace with the path to your PDF file
print(extract_text_from_pdf(pdf_path))