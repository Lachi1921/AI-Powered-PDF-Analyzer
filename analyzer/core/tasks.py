from celery import shared_task

from core.models import PdfDocument
from tutor_app import settings
from huggingface_hub import InferenceClient
import json

client = InferenceClient(api_key=settings.HF_ACCESS_TOKEN)

@shared_task(bind=True, name="tasks.process_pdf", retry_backoff=True, max_retries=3)
def process_pdf(self, pdf_id):
    pdf_document = PdfDocument.objects.get(id=pdf_id)
    pdf_text = pdf_document.raw_text

    summary_prompt = f"""
    
    1. Summarize the extracted PDF text accurately and concisely while maintaining the main points, topic, context, and original meaning.
    2. Generate up to 10 unique questions, relevant questions based on the extracted PDF text. Avoid duplicates or repetitive wording.

    Output Requirements:
        - Return valid JSON only.
        - Do not include markdown, explanations, comments, or extra text.
        - Maintain semantic accuracy and avoid hallucinations.

        JSON schema:
        {{
        "summary": string,
        "questions": string[]
        }}


        Text to analyze:
        {pdf_text}
    
    """
    
    process_pdf = client.chat.completions.create(
        model = "deepseek-ai/DeepSeek-V4-Pro",
        messages=[{
                "role": "user",
                "content": summary_prompt
        }],
        temperature=0
        )
    
    content = process_pdf.choices[0].message.content
    parsed = json.loads(content)

    pdf_document.summary = parsed["summary"]
    pdf_document.questions = parsed["questions"]
    pdf_document.status = "PROCESSED"
    pdf_document.save()

    return pdf_document.id
