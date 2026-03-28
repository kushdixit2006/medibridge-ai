# 🩺 MediBridge AI

An AI-powered medical report assistant that converts complex medical reports into simple, understandable insights using a locally deployed LLM.

---

## 🚀 Overview

MediBridge helps users understand their medical reports without needing medical expertise.
It uses **AI reasoning (Mistral LLM)** to analyze reports and generate clear explanations, observations, risk levels, and questions for doctors.

---

## ✨ Features

* 📄 Upload medical reports (PDF)
* 🔍 OCR support for scanned reports
* 🧠 AI-driven analysis (no hardcoded rules)
* ⚠️ Detects abnormal values
* 💬 Generates meaningful questions for doctors
* 🧾 Suggests next steps
* 🔒 Runs locally → privacy-friendly

---

## 🧠 How It Works

```text
PDF Report
   ↓
Text Extraction (OCR if needed)
   ↓
Chunking + Vector Search (RAG)
   ↓
Mistral LLM (Reasoning)
   ↓
Structured Medical Explanation
```

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** (UI)
* **Ollama + Mistral** (Local LLM)
* **FAISS** (Vector database)
* **Sentence Transformers** (Embeddings)
* **EasyOCR** (Text extraction)

---

## ⚙️ Installation

```bash
git clone https://github.com/kushdixit2006/medibridge-ai.git
cd medibridge-ai
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
ollama serve
streamlit run ui.py
```

---

---

## 💡 Key Highlights

* ✅ Fully AI-driven (no hardcoded rules)
* ✅ Handles real-world messy medical reports
* ✅ Uses local LLM → no API dependency
* ✅ Privacy-focused (data stays on device)
* ✅ Combines OCR + RAG + LLM

---

## 🧪 Example Use Case

**Input:** Medical report PDF
**Output:**

* Explanation in simple language
* Important observations
* Risk level (Low / Moderate / High)
* Questions to ask a doctor
* Suggested next steps

---

## ⚠️ Disclaimer

This project is for educational purposes only.
It does **not** provide medical advice. Always consult a qualified healthcare professional.

---

## 👨‍💻 Author

**Kush Dixit**
GitHub: https://github.com/kushdixit2006

---

## ⭐ If you like this project



