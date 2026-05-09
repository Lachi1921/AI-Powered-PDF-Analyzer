from django.urls import path
from core.views import PdfSummirizerView

urlpatterns = [
    path('pdf-summarize/', PdfSummirizerView.as_view()),
]
