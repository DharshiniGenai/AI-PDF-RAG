from qdrant_client import QdrantClient

# Connect to a local Qdrant server running on Docker or local machine
qdrant = QdrantClient(url="http://localhost:6333")