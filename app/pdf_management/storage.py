import os
import shutil
import uuid
from fastapi import UploadFile

UPLOAD_FOLDER = "app/Uploads"

os.makedirs(UPLOAD_FOLDER,exist_ok=True)

async def save_pdf(file:UploadFile):

    unique_name = f"{uuid.uuid4()}.pdf"

    file_path = os.path.join(
        UPLOAD_FOLDER,
        unique_name
    )

    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

        return {
            "file_name":unique_name,
            "path":file_path
        }
