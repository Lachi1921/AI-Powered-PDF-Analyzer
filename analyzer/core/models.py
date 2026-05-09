from django.db import models

# Create your models here.


class PdfDocument(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/')
    raw_text = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    questions = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, default="pending")
    
    uploaded_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return f"PdfDocument(id={self.id}, status={self.status})"