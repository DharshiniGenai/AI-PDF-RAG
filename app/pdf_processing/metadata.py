import uuid
from app.pdf_processing.chunk_text import chunk_text

def store_metadata(file_path: str, document_id: str):

    chunks =chunk_text(file_path)

    processed_chunks =[]

    for chunk in chunks:

        processed_chunks.append(
            {
                "document_id": document_id,
                "chunk_id": str(uuid.uuid4()),
                "page": chunk["page"],
                "sequence": chunk["sequence"],
                "text": chunk["text"]
            }
        )
    return processed_chunks


