from django.urls import path
from .views import TextSummarizer

urlpatterns = [
    path('', TextSummarizer.as_view(), name='text_summarizer'),
]