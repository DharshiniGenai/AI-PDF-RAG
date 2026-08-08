
# 🤖 AI PDF Chat — RAG-Based Document Question Answering

🚀 **Built from scratch using Python, FastAPI, Qdrant, Sentence Transformers, and Groq LLM**

A production-inspired Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions about their content.

Instead of sending the entire document directly to the LLM, the application processes PDFs into smaller chunks, converts them into vector embeddings, stores them in Qdrant Vector Database, retrieves the most relevant chunks for a user's question, and then uses a Groq-hosted LLM to generate an answer based on the retrieved context.

The project was implemented **from scratch** to understand the complete RAG pipeline, from PDF ingestion and text processing to vector search and LLM-based answer generation.

---

# 📖 Project Overview

The application provides a complete workflow for interacting with PDF documents using Retrieval-Augmented Generation.

The system performs the following operations:

* Upload PDF documents
* Extract text from PDFs
* Clean extracted text
* Split documents into smaller chunks
* Generate vector embeddings
* Store embeddings in Qdrant
* Perform semantic similarity search
* Retrieve the most relevant document chunks
* Generate answers using a Groq LLM
* Manage uploaded PDF documents
* Retrieve PDF metadata and details
* Delete PDF documents
* Download PDF documents

The main goal of the project is to demonstrate how a modern RAG-based AI application works internally rather than relying on a simple LLM prompt.

---

# ⚙️ How the RAG System Works

The complete RAG architecture follows this workflow:

```text
🤖 AI PDF Chat — RAG-Based Document Question Answering

🚀 Built from scratch using Python, FastAPI, Qdrant, Sentence Transformers, and Groq LLM

A production-inspired Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions about their content.

Instead of sending the entire document directly to the LLM, the application processes PDFs into smaller chunks, converts them into vector embeddings, stores them in Qdrant Vector Database, retrieves the most relevant chunks for a user's question, and then uses a Groq-hosted LLM to generate an answer based on the retrieved context.

This project was built from scratch to understand the complete RAG pipeline, from PDF ingestion and text processing to vector search and LLM-based answer generation.

📖 Project Overview

The application provides a complete workflow for interacting with PDF documents using Retrieval-Augmented Generation.

The system performs the following operations:

Upload PDF documents
Extract text from PDFs
Clean extracted text
Split documents into smaller chunks
Generate vector embeddings
Store embeddings in Qdrant
Perform semantic similarity search
Retrieve the most relevant document chunks
Generate answers using a Groq LLM
Retrieve PDF metadata and details
Download PDF documents
Delete PDF documents

The main goal of this project is to understand how a RAG system works internally rather than treating RAG as a black-box technology.

⚙️ How the RAG System Works

The complete RAG pipeline follows this architecture:

                    PDF Upload
                        │
                        ▼
                  FastAPI API
                        │
                        ▼
                PDF Text Extraction
                        │
                        ▼
                  Text Cleaning
                        │
                        ▼
                    Chunking
                 500 characters
                  50 overlap
                        │
                        ▼
               Sentence Transformer
              all-MiniLM-L6-v2
                        │
                        ▼
                 Vector Embeddings
                        │
                        ▼
                    Qdrant
                Vector Database
                        │
                        │
                User asks question
                        │
                        ▼
              Question Embedding
                        │
                        ▼
              Qdrant Similarity Search
                        │
                        ▼
              Top 5 Relevant Chunks
                        │
                        ▼
                Context Construction
                        │
                        ▼
                  Groq LLM
             Llama 3.3 70B Versatile
                        │
                        ▼
                  Final Answer

This architecture separates document processing, vector storage, retrieval, and answer generation into independent components.

🔄 RAG Pipeline

The application follows two major stages.

1️⃣ Document Ingestion

When a PDF is uploaded, it goes through the following pipeline:

PDF
 ↓
Read PDF
 ↓
Extract Text
 ↓
Clean Text
 ↓
Split into Chunks
 ↓
Generate Embeddings
 ↓
Store in Qdrant

Each document chunk is converted into a numerical vector representation using:

all-MiniLM-L6-v2

The generated vectors are stored in Qdrant along with the corresponding document text and metadata.

2️⃣ Question Answering

When the user asks a question:

User Question
      ↓
Generate Question Embedding
      ↓
Qdrant Similarity Search
      ↓
Retrieve Top 5 Relevant Chunks
      ↓
Build Context
      ↓
Send Context + Question to LLM
      ↓
Generate Answer

The retrieved chunks are provided to the LLM as context so that the generated response is grounded in the uploaded documents.

If the required information is not available in the retrieved context, the system is instructed to avoid inventing information.

🧠 Key Concepts Used
📌 Retrieval-Augmented Generation

Retrieval-Augmented Generation combines information retrieval with Large Language Model generation.

Instead of asking the LLM to answer using only its pretrained knowledge, the application first retrieves relevant information from the user's documents.

User Question
      ↓
Retrieve Relevant Information
      ↓
Build Context
      ↓
LLM
      ↓
Grounded Answer

This approach helps provide answers based on the uploaded documents.

📌 PDF Processing

The PDF processing pipeline is divided into separate modules:

pdf_processing/
│
├── read_pdf.py
├── extract_text.py
├── clean_text.py
├── chunk_text.py
├── process_pdf.py
└── metadata.py

Each module is responsible for a specific processing stage.

The overall workflow is:

PDF
 ↓
Read
 ↓
Extract Text
 ↓
Clean Text
 ↓
Chunk Text
 ↓
Generate Embeddings

This modular structure makes the processing pipeline easier to understand, maintain, and extend.

📌 Text Chunking

The project uses:

RecursiveCharacterTextSplitter

with:

chunk_size = 500 characters
chunk_overlap = 50 characters

Chunking is necessary because sending an entire document directly to an LLM is inefficient and can exceed context limits.

The overlap helps preserve contextual information between neighboring chunks.

Example:

Chunk 1
────────────────────
A B C D E F G H
        │
        ▼
Chunk 2
        D E F G H I J K

The overlapping portion helps reduce the chance of losing important information at chunk boundaries.

📌 Embeddings

The project uses the Sentence Transformers model:

all-MiniLM-L6-v2

The model converts text into numerical vector representations.

For example:

"What is BERT?"
       ↓
Sentence Transformer
       ↓
Embedding Vector
       ↓
Qdrant

The same embedding model is used for both:

Document chunks
User questions

This allows the application to compare the semantic similarity between the question and stored document chunks.

📌 Qdrant Vector Database

Qdrant is used as the vector database for storing and searching document embeddings.

The application stores:

Vector
+
Document Text
+
Metadata

When a user asks a question:

User Question
      ↓
Question Embedding
      ↓
Qdrant Similarity Search
      ↓
Relevant Document Chunks

The application retrieves the top 5 relevant chunks and passes them to the LLM as context.

📌 Semantic Similarity Search

The system does not rely only on exact keyword matching.

Instead, the question is converted into an embedding and compared against document embeddings.

User Question
      ↓
Embedding
      ↓
Vector Similarity
      ↓
Most Relevant Chunks

This allows the application to retrieve conceptually related information even when the exact wording of the question does not appear in the document.

📌 Groq LLM

The retrieved document context is passed to a Groq-hosted LLM for answer generation.

Current model:

llama-3.3-70b-versatile

The generation pipeline follows:

Retrieved Chunks
       +
User Question
       ↓
Groq LLM
       ↓
Final Answer

The generation instructions are designed to:

Answer using the provided document context
Avoid unsupported information
Avoid unnecessarily inventing answers
Respond appropriately when the required information is not available
📄 PDF Management

The project also includes a dedicated PDF management module.

pdf_management/
│
├── delete.py
├── details.py
├── download.py
├── metadata.py
├── router.py
├── storage.py
└── validator.py

This separates document management operations from the core RAG processing pipeline.

The application supports:

PDF upload
PDF deletion
PDF details
PDF metadata handling
PDF download
File validation
PDF storage management
✨ Features
✅ Upload PDF documents
✅ Extract text from PDF files
✅ Clean extracted text
✅ Split documents into smaller chunks
✅ Generate semantic embeddings
✅ Store embeddings in Qdrant
✅ Perform vector similarity search
✅ Retrieve top 5 relevant document chunks
✅ Generate context-aware answers using Groq LLM
✅ PDF metadata extraction
✅ PDF details retrieval
✅ PDF download
✅ PDF deletion
✅ File validation
✅ FastAPI REST APIs
✅ Swagger UI documentation
✅ Modular project architecture
✅ Local Qdrant vector storage
✅ RAG-based question answering
🧰 Technologies Used
Backend
Python
FastAPI
Uvicorn
PDF Processing
PyMuPDF
Vector Database
Qdrant
Embeddings
Sentence Transformers
all-MiniLM-L6-v2
LLM
Groq
Llama 3.3 70B Versatile
Text Processing
LangChain Text Splitters
RecursiveCharacterTextSplitter
Data Validation
Pydantic
Environment Management
python-dotenv
📁 Project Structure
AI-PDF-RAG/
│
├── app/
│   │
│   ├── main.py
│   │
│   ├── models/
│   │   └── query.py
│   │
│   ├── pdf_management/
│   │   ├── delete.py
│   │   ├── details.py
│   │   ├── download.py
│   │   ├── metadata.py
│   │   ├── router.py
│   │   ├── storage.py
│   │   └── validator.py
│   │
│   ├── pdf_processing/
│   │   ├── read_pdf.py
│   │   ├── extract_text.py
│   │   ├── clean_text.py
│   │   ├── chunk_text.py
│   │   ├── process_pdf.py
│   │   └── metadata.py
│   │
│   ├── vector_db/
│   │   ├── client.py
│   │   ├── collections.py
│   │   ├── embeddings.py
│   │   ├── search.py
│   │   └── store_embeddings.py
│   │
│   ├── papers/
│   │   ├── BERT.pdf
│   │   ├── RAG.pdf
│   │   └── sample.pdf
│   │
│   ├── Uploads/
│   │
│   └── vector_store/
│
├── README.md
└── requirements.txt

The project follows a modular architecture where PDF processing, vector database operations, document management, and API logic are separated into dedicated modules.

🔗 End-to-End Architecture
                    ┌─────────────────┐
                    │      User       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    FastAPI      │
                    │      API        │
                    └────────┬────────┘
                             │
             ┌───────────────┴────────────────┐
             │                                │
             ▼                                ▼
      PDF Upload                         User Query
             │                                │
             ▼                                ▼
      PDF Processing                 Question Embedding
             │                                │
      ┌──────┴──────┐                         ▼
      │             │                    Qdrant Search
      ▼             ▼                         │
   Extract       Chunk                       ▼
    Text          Text                  Top 5 Chunks
      │             │                         │
      └──────┬──────┘                         │
             ▼                                │
        Embeddings                            │
             │                                │
             ▼                                │
          Qdrant ◄────────────────────────────┘
             │
             ▼
        Retrieved Context
             │
             ▼
          Groq LLM
             │
             ▼
       Generated Answer
📸 API Endpoints

The application exposes REST APIs through FastAPI.

Method	Endpoint	Description
POST	/pdf/upload	Upload and process a PDF
GET	/pdf/list	List uploaded PDFs
GET	/pdf/download/{filename}	Download a PDF
GET	/pdf/details/{filename}	Retrieve PDF details
DELETE	/pdf/delete/{filename}	Delete a PDF
POST	/query	Ask a question using the RAG pipeline

The exact endpoint paths may vary depending on the current router configuration in the project.

📚 Vector Database Workflow

The vector database workflow is:

PDF Chunk
    ↓
Generate Embedding
    ↓
Create Vector Point
    ↓
Store in Qdrant
    ↓
User Question
    ↓
Generate Question Embedding
    ↓
Similarity Search
    ↓
Retrieve Relevant Chunks

Qdrant acts as the retrieval layer between the document processing pipeline and the LLM.

🧪 Example RAG Flow

User asks:

What is BERT?

The system performs:

"What is BERT?"
        ↓
Sentence Transformer
        ↓
Question Embedding
        ↓
Qdrant
        ↓
Top 5 Relevant Chunks
        ↓
Context Construction
        ↓
Groq LLM
        ↓
Generated Answer

Example response:

BERT is conceptually simple and empirically powerful.

The answer is generated using information retrieved from the uploaded document.

📖 API Documentation

FastAPI automatically provides interactive API documentation through Swagger UI.

After starting the application:

http://127.0.0.1:8000/docs

The Swagger interface can be used to:

Upload PDF documents
Test PDF management APIs
Send questions
Test the RAG pipeline
Inspect API responses
▶️ How to Run
1️⃣ Clone the repository
git clone <repository-url>
cd AI-PDF-RAG
2️⃣ Create a virtual environment
python -m venv venv

Activate it on Windows:

venv\Scripts\activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Configure environment variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key
5️⃣ Start the application
uvicorn app.main:app --reload
6️⃣ Open Swagger UI
http://127.0.0.1:8000/docs
🧠 Key Concepts Learned

This project provided hands-on understanding of:

Retrieval-Augmented Generation
Vector embeddings
Semantic search
Vector databases
Qdrant
Sentence Transformers
PDF text extraction
Text cleaning
Document chunking
Chunk overlap
Context retrieval
LLM prompt construction
Grounded generation
Hallucination reduction
FastAPI REST APIs
Modular backend architecture
Metadata management
Document lifecycle management
🎯 Learning Outcomes

By building this project from scratch, I gained practical understanding of how a RAG application works internally.

The complete pipeline can be summarized as:

Document
   ↓
Text
   ↓
Chunks
   ↓
Embeddings
   ↓
Vector Database
   ↓
Similarity Search
   ↓
Relevant Context
   ↓
LLM
   ↓
Answer

Rather than treating RAG as a black-box framework, this project focuses on implementing and understanding each individual stage of the pipeline.

🔮 Future Improvements

The application can be further extended with:

Agentic AI integration
LangChain tool calling
Keycloak authentication
Role-Based Access Control
MinIO object storage
Redis caching
Conversation history
Multi-document filtering
Document-level access control
Streaming LLM responses
Reranking retrieved chunks
Hybrid search
Citation generation
Docker deployment
Cloud deployment
Monitoring and logging
Production database integration
🚨 Important Notes

This project is production-inspired and built for learning purposes.

The current implementation focuses primarily on understanding the core RAG architecture and backend integration.

It should not be considered a fully production-ready enterprise RAG platform without additional security, authentication, monitoring, scalability, testing, and deployment considerations.

👨‍💻 Conclusion

This project demonstrates how a modern RAG application can process PDF documents, generate embeddings, store them in a vector database, retrieve relevant information using semantic search, and use an LLM to generate grounded answers.

By implementing the pipeline from scratch, the project provided practical experience with:

RAG architecture
PDF processing
Embeddings
Vector databases
Semantic retrieval
LLM integration
FastAPI backend development
Modular application architecture

The project focuses on understanding what happens inside a RAG system, rather than simply using a pre-built RAG framework.

👨‍💻 Author

Dharshini A.

B.Sc. Computer Science Graduate | Aspiring Generative AI Developer

This project was built from scratch to gain hands-on experience with Retrieval-Augmented Generation, vector databases, semantic search, LLM integration, PDF processing, and backend API development using FastAPI.
```
