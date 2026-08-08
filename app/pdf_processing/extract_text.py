from app.pdf_processing.read_pdf import read_pdf

def extract_text(file_path: str):

    pages = read_pdf(file_path)

    extracted_pages =[]

    for page in pages:
        extracted_pages.append(
            {
            "page": page["page"],
            "text": page["text"]
            }

        )

    return extracted_pages



        
  