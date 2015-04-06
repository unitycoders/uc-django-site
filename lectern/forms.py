from django import forms
from lectern.models import Article

from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *

class ArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                TabHolder(
                    Tab('article', InlineField('title'), InlineField('body')),
                    Tab('metadata', Fieldset('Advanced', 'slug', css_id='advanced', css_class='collapse'), 'category', 'abstract'),
                ),
                ButtonHolder(Submit('submit', 'Submit', css_class='button white'))
        )
        self.helper.html5_required = True

    class Meta:
        model = Article
        widgets = {
                'abstract': forms.Textarea(attrs={'rows':4}),
        }
