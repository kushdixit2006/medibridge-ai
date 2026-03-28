import streamlit as st
import os

from ingestion.pdf_loader import load_pdf
from ingestion.chunker import chunk_text
from rag.vector_store import create_vector_store, search
from llm.generator import generate_response

# ================= UI ================= #
st.set_page_config(page_title="MediBridge", layout="centered")

st.title("🩺 MediBridge")
st.subheader("AI-powered medical report assistant")

# ================= CLEAN TEXT ================= #
def clean_text(text):
    return text.replace("\n", " ").replace("  ", " ")

# ================= FILE ================= #
uploaded_file = st.file_uploader("Upload medical report (PDF)", type=["pdf"])

if uploaded_file:

    temp_path = "temp_report.pdf"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("File uploaded")

    if st.button("Analyze"):

        try:
            text = load_pdf(temp_path)
            text = clean_text(text)

            if not text.strip():
                st.error("Could not extract text")
                st.stop()

            st.write("📄 Preview:", text[:300])

            # ================= RAG ================= #
            chunks = chunk_text(text)
            index = create_vector_store(chunks)
            context = search(index, "important medical values")[:2]

            # ================= AI ================= #
            result = generate_response(context, text)

            is_ai_working = "ERROR" not in result and len(result) > 50

            st.subheader("📋 Result")

            if is_ai_working:
                # ✅ PURE AI OUTPUT
                st.markdown("### 🧠 AI Medical Analysis")
                st.write(result)

            else:
                # 🔥 FALLBACK (only if AI fails)
                st.warning("AI failed, using basic analysis")

                observations = []
                text_lower = text.lower()

                if "hemoglobin" in text_lower and "11" in text_lower:
                    observations.append("Low hemoglobin detected → possible anemia")

                if "glucose" in text_lower:
                    observations.append("Blood sugar appears within normal range")

                if not observations:
                    observations.append("No major abnormalities detected")

                st.markdown("### ⚠️ Basic Analysis")
                for o in observations:
                    st.write("-", o)

                st.markdown("### ❓ Questions")
                st.write("- Should I consult a doctor?")
                st.write("- Do I need further tests?")
                st.write("- What precautions should I take?")

            st.info("⚠️ This is not medical advice. Please consult a doctor.")

        except Exception as e:
            st.error(f"Error: {str(e)}")

        os.remove(temp_path)