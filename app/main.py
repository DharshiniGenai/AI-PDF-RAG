from fastapi import FastAPI
from app.pdf_management.router import router as pdf_management_router

app = FastAPI(
    title="RAG Engine",
    description="Decoupled backend API architecture using Groq LPU Framework & Qdrant persistent storage indices.",
    version="1.0.0"
)

app.include_router(pdf_management_router)

@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "service": "enterprise-rag-core"
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )

  