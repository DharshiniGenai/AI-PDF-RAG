import pymupdf
import os
from datetime import datetime

def extract_metadata (file_path:str):

    document = pymupdf.open(file_path)
    metadata = document.metadata
    page_count = document.page_count
    file_size = os.path.getsize(file_path)
    document.close()

    return{
        "title": metadata.get("title"),
        "author": metadata.get("author"),
        "creator": metadata.get("creator"),
        "creation_date": metadata.get("creationDate"),
        "page_count": page_count,
        "file_size": file_size,
        "uploaded_at": datetime.now().isoformat()
    }