from fastapi import APIRouter,UploadFile,File
from app.pdf_management.validator import validate_pdf
from app.pdf_management.storage import save_pdf
from app.pdf_management.metadata import extract_metadata
import os
from app.pdf_management.delete import delete_pdf
from app.pdf_management.download import download_pdf
from app.pdf_management.details import get_pdf_details
from app.pdf_processing.process_pdf import process_pdf
import uuid
from app.vector_db.collections import create_collection
from app.vector_db.store_embeddings import store_embeddings
from app.models.query import QueryRequest
from app.vector_db.search import search_documents

UPLOAD_FOLDER = "app/Uploads"

router=APIRouter(
    prefix="/pdf",
    tags=["PDF Management"]
)

@router.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):
    await validate_pdf(file)

    saved = await save_pdf(file)

    metadata = extract_metadata(saved["path"])

    document_id = str(uuid.uuid4())

    create_collection()

    processed_chunks = process_pdf(
        saved["path"],
        document_id
    )

    store_embeddings(processed_chunks)

    return {
        "message": "PDF uploaded successfully",
        "file": saved,
        "metadata": metadata,
        "document_id": document_id,
        "total_chunks": len(processed_chunks)
    }


@router.get("/list")
def list_pdfs():
    pdfs =[]

    if os.path.exists(UPLOAD_FOLDER):
        for file in os.listdir(UPLOAD_FOLDER):
            if file.endswith(".pdf"):
                file_path = os.path.join(UPLOAD_FOLDER, file)


                pdfs.append({
                    "file_name": file,
                    "file_size": os.path.getsize(file_path)
                })

    return {
            "total_files": len(pdfs),   
            "files": pdfs
            }

@router.delete("/delete/{file_name}")
def delete_pdf(file_name: str):

    return delete_pdf(file_name)

@router.get("/download/{file_name}")
def download(file_name: str):

    return download_pdf(file_name)

@router.get("/details/{file_name}")
def pdf_details(file_name: str):
    return get_pdf_details(file_name)

@router.post("/query")
def query_pdf(request: QueryRequest):

    return search_documents(
        request.question
    )


            
