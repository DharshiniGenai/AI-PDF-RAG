import re

from app.pdf_processing.extract_text import extract_text

def clean_text(file_path: str):

    pages = extract_text(file_path)

    cleaned_pages=[]

    for page in pages:

        text=page["text"]

        text=re.sub(r"[\t]+"," ", text)

        text = re.sub(r"\n+", "\n", text)

        text = text.strip()

        cleaned_pages.append(
            {
                "page": page["page"],
                "text": text
            }
        )


    return cleaned_pages


    

        

