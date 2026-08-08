from qdrant_client import models

from app.vector_db.client import qdrant
from app.vector_db.embeddings import encoder

COLLECTION_NAME = "pdf_documents"


def create_collection():

    if qdrant.collection_exists(COLLECTION_NAME):
        return

    qdrant.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(
            size=encoder.get_sentence_embedding_dimension(),
            distance=models.Distance.COSINE,
        ),
    )

    print("Qdrant Collection Created")