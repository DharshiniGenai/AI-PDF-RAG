from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.pdf_processing.clean_text import clean_text

text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)


def chunk_text(file_path: str):
    pages =clean_text(file_path)
    chunks=[]
    chunk_id=1
    for page in pages:
        split_chunks=text_splitter.split_text(page["text"])
        for sequence, chunk in enumerate(split_chunks, start=1):
            chunks.append(
                {
                    "chunk_id": chunk_id,
                    "page": page["page"],
                    "sequence": sequence,
                    "text": chunk
                }

            )

            chunk_id +=1
    return chunks



        

        