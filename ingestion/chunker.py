def chunk_text(text, chunk_size=300, overlap=50):
    if not text or not text.strip():
        return []

    # 🔥 Clean text
    text = text.replace("\n", " ").strip()

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        # ✅ only keep meaningful chunks
        if len(chunk.split()) > 5:
            chunks.append(chunk.strip())

        start += chunk_size - overlap

    return list(set(chunks))[:10]   # 🔥 remove duplicates + limit


if __name__ == "__main__":
    from pdf_loader import load_pdf

    file_path = "/Users/kushdixit/Desktop/medibridge/data/sample_report.pdf"
    
    text = load_pdf(file_path)
    chunks = chunk_text(text)

    print("----- CHUNKS -----\n")

    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}:\n{chunk}\n")