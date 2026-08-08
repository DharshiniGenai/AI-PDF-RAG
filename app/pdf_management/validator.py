from fastapi import UploadFile, HTTPException

ALLOWED_EXTENTION = [".pdf"]
MAX_FILE_SIZE = 10* 1024 *1024

async def validate_pdf(file: UploadFile):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="only PDF file are allowed"
        )
    
    if file.content_type!="application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Invalid PDF file"
        )
    contents = await file.read()

    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File exceeds maximum size"
        )
    await file.seek(0)

    return True