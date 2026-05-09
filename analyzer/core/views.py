from rest_framework import generics
from core.models import PdfDocument
from core.serializers import PdfDocumentSerializer
# Create your views here.


class PdfSummirizerView(generics.ListCreateAPIView):
    serializer_class = PdfDocumentSerializer
    queryset = PdfDocument.objects.all()