from django import forms
from lectern.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        widgets = {
                'abstract': forms.Textarea(attrs={'rows':4}),
        }
