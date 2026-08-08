from app.pdf_processing.read_pdf import read_pdf
from app.pdf_processing.extract_text import extract_text
from app.pdf_processing.clean_text import clean_text
from app.pdf_processing.chunk_text import chunk_text
from app.pdf_processing.metadata import store_metadata

def process_pdf(file_path: str, document_id: str):

    read_pdf(file_path)
    extract_text(file_path)
    clean_text(file_path)
    chunk_text(file_path)
    processed_data=store_metadata(file_path, document_id)

    return processed_data




    