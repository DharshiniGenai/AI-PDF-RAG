import os
from fastapi import HTTPException
from app.pdf_management.metadata import extract_metadata

UPLOAD_FOLDER = "app/Uploads"

def get_pdf_details(file_name:str):
    file_path = os.path.join(
        UPLOAD_FOLDER,
        file_name
    )

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="PDF not found"
        )
    
    metadata = extract_metadata(file_path)

    return {
        "file_name": file_name,
        "file_path": file_path,
        "processing_status": "Completed",
        "metadata": metadata
    }