from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Store chunks
stored_chunks = []


def create_vector_store(chunks):
    global stored_chunks

    if not chunks:
        raise ValueError("No chunks found. Check PDF extraction.")

    embeddings = model.encode(chunks)

    if len(embeddings.shape) == 1:
        raise ValueError("Embeddings shape error. Possibly empty or invalid input.")

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    stored_chunks = chunks

    return index


def search(index, query, k=3):
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, k)

    results = []
    for i in indices[0]:
        if i < len(stored_chunks):
            results.append(stored_chunks[i])

    return results


if __name__ == "__main__":
    from ingestion.pdf_loader import load_pdf
    from ingestion.chunker import chunk_text


    file_path = "/Users/kushdixit/Desktop/medibridge/data/sample_report.pdf"

    text = load_pdf(file_path)
    chunks = chunk_text(text)

    index = create_vector_store(chunks)

    query = "high blood sugar meaning"
    results = search(index, query)

    print("\n---------- SEARCH RESULTS ---------\n")
    for r in results:
        print(r)
        print("---------")