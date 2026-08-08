import os 
from fastapi import HTTPException
from fastapi.responses import FileResponse

UPLOAD_FOLDER = "app/Uploads"

def download_pdf(file_name: str):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file_name
    )

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="PDF not found"
        )
    
    return FileResponse(
        path=file_path,
        media_type="application/pdf",
        filename=file_name
    )