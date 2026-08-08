import os

from dotenv import load_dotenv
from groq import Groq

from app.vector_db.client import qdrant
from app.vector_db.embeddings import encoder
from app.vector_db.collections import COLLECTION_NAME

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_answer(question, chunks):

    context = "\n\n".join(
        chunk.payload["text"]
        for chunk in chunks
    )

    system_prompt = """
You are an AI assistant.

Answer ONLY from the provided context.

Do not make up information.

If the answer is not available in the context, reply:

I do not know based on the uploaded documents.
"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        temperature=0,

        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": f"""
Context:

{context}

Question:

{question}
"""
            }
        ]
    )

    return response.choices[0].message.content


def search_documents(question):

    query_vector = encoder.encode(
        question,
        normalize_embeddings=True
    ).tolist()

    results = qdrant.query_points(

        collection_name=COLLECTION_NAME,

        query=query_vector,

        limit=5,

        with_payload=True

    ).points

    answer = generate_answer(
        question,
        results
    )

    return {
        "question": question,
        "answer": answer,
        "sources": [
            {
                "page": r.payload["page"],
                "sequence": r.payload["sequence"]
            }
            for r in results
        ]
    }