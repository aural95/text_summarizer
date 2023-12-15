from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

nltk.download('punkt')
nltk.download('stopwords')

class TextSummarizer(View):
    def preprocess_text(self, text):
        stop_words = set(stopwords.words('english'))
        words = word_tokenize(text.lower())
        filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
        return filtered_words

    def generate_summary(self, text, num_sentences=3):
        sentences = sent_tokenize(text)
        words = self.preprocess_text(text)
        freq_dist = FreqDist(words)
        key_sentences = sorted(sentences, key=lambda sentence: sum(freq_dist[word] for word in word_tokenize(sentence.lower())), reverse=True)[:num_sentences]
        summary = ' '.join(key_sentences)
        return summary

    def get(self, request):
        return render(request, 'textsummarizer/index.html')

    def post(self, request):
        input_text = request.POST.get('input_text', '')
        summary = self.generate_summary(input_text)
        return render(request, 'textsummarizer/index.html', {'input_text': input_text, 'summary': summary})