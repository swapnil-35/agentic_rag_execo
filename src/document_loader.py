import pypdf

def load_pdf_text(pdf_path: str) -> str:
    with open(pdf_path, 'rb') as file:
        reader = pypdf.PdfReader(file)
        text = ""

        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

    return text