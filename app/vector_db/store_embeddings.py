from qdrant_client import models

from app.vector_db.client import qdrant
from app.vector_db.collections import COLLECTION_NAME
from app.vector_db.embeddings import encoder


def store_embeddings(processed_chunks):

    points = []

    for chunk in processed_chunks:

        vector = encoder.encode(
            chunk["text"],
            normalize_embeddings=True
        ).tolist()

        points.append(
            models.PointStruct(
                id=chunk["chunk_id"],
                vector=vector,
                payload={
                    "document_id": chunk["document_id"],
                    "page": chunk["page"],
                    "sequence": chunk["sequence"],
                    "text": chunk["text"]
                }
            )
        )

    if points:

        qdrant.upsert(
            collection_name=COLLECTION_NAME,
            points=points
        )

    print(f"{len(points)} chunks stored in Qdrant.")