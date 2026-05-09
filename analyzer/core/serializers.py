from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.tasks import process_pdf
from core.models import PdfDocument

import fitz



class PdfDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PdfDocument
        fields = [
            "id",
            "uploaded_at",
            "pdf_file",
            "summary",
            "questions",
            "status",
            "raw_text",
        ]
        read_only_fields = ["id", "uploaded_at", "summary", "questions", "status", "raw_text"]

    def create(self, validated_data):

        pdf_file = validated_data["pdf_file"]
        text_content = ""

        try:
            with fitz.open(stream=pdf_file.read()) as pdf_document:
                for page in pdf_document:
                    text_content += page.get_text("text")
                    text_content += "\n\n-------------------\n\n"

        except Exception as e:
            raise ValidationError(f"Error reading PDF file: {e}")



        pdf_document = PdfDocument.objects.create(
            pdf_file=pdf_file,
            raw_text=text_content,
            status="PENDING",
        )
        process_pdf.delay(pdf_document.id)

        return pdf_document