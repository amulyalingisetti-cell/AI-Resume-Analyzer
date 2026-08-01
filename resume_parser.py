import pdfplumber
import docx2txt

def extract_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    return text

def extract_docx(file):
    text = docx2txt.process(file)
    return text if text else ""