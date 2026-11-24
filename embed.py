
from load import chunks
from sentence_transformers import SentenceTransformer
import chromadb

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Create vector database
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("syllabus")

# Generate embeddings
embeddings = embedder.encode(chunks).tolist()

# Store chunks and embeddings
collection.add(
    documents=chunks,
    embeddings=embeddings,
    ids=[f"chunk-{i}" for i in range(len(chunks))]
)

print("Indexed all chunks into the vector store")
print("Total chunks stored:", collection.count())
