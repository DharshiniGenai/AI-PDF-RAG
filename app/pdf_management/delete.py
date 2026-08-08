import os
from fastapi import HTTPException

UPLOAD_FOLDER = "app/Uploads"

def delete_pdf(file_name: str):
    file_path = os.path.join(
        UPLOAD_FOLDER,
        file_name

    )

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=400,
            detail="PDF not found"
        )
    
    os.remove(file_path)

    return{
        "message": "PDF deleted successfully",
        "file_name": file_name

    }