from ingestion.pdf_loader import load_pdf
from ingestion.chunker import chunk_text
from rag.vector_store import create_vector_store, search
from llm.generator import generate_response

file_path = "/Users/kushdixit/Desktop/medibridge/data/sample_report.pdf"

text = load_pdf(file_path)
chunks = chunk_text(text)

index = create_vector_store(chunks)
context = search(index, "important values")
context = context[:2]   # 🔥 limit context
final_output = generate_response(context, text)

print("\n========== FINAL OUTPUT ==========\n")
print(final_output)