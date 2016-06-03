from django import forms
from .models import Articles

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'article_text', 'current', 'authors']
