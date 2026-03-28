import ollama

def generate_response(context, report_text):

    prompt = f"""
You are an expert medical assistant.

Analyze the medical report like a doctor.

Tasks:
- Identify abnormal values
- Compare with normal ranges
- Use symptoms if present
- Explain clearly in simple language

STRICT FORMAT:

Explanation:
...

Observations:
- ...

Risk:
Low / Moderate / High

Questions:
1.
2.
3.

Next Steps:
- ...

Report:
{report_text}
"""

    try:
        response = ollama.chat(
            model="mistral",
            messages=[{"role": "user", "content": prompt}]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"ERROR: {str(e)}"