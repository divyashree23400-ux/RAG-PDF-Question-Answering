
from sentence_transformers import SentenceTransformer
import chromadb

embedder = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("syllabus")

def retrieve(query, k=3):
    query_vec = embedder.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_vec,
        n_results=k,
    )

    return results["documents"][0]


question = "How many credits is the DevOps Automation course?"
top_chunks = retrieve(question)

for i, chunk in enumerate(top_chunks):
    print(f"--- Match {i+1} ---\n{chunk[:150]}...")
