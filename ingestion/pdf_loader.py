from pypdf import PdfReader
import os
from ingestion.ocr_loader import extract_text_from_image
from pdf2image import convert_from_path

def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    # Step 1: Try normal text extraction
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    # Step 2: If no text → use OCR
    if not text.strip():
        images = convert_from_path(file_path)

        for i, img in enumerate(images):   # ✅ FIXED
            img_path = f"temp_page_{i}.png"

            img.save(img_path)             # ✅ inside loop
            text += extract_text_from_image(img_path)

            os.remove(img_path)            # ✅ cleanup

    return text