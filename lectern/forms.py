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
                    Tab('article', InlineField('title'), InlineField('body'), Div(Div(Field('category'),css_class='col-xs-6'), css_class='row')),
                    Tab('metadata', Fieldset('Advanced', PrependedText('slug', 'http://unitycoders.co.uk/articles/mycategory/'), css_id='advanced', css_class='collapse'), 'abstract'),
                ),
                ButtonHolder(Submit('submit', 'Submit'))
        )
        self.helper.html5_required = True

    class Meta:
        model = Article
	fields = ('title', 'body', 'category', 'slug', 'abstract')
        widgets = {
                'abstract': forms.Textarea(attrs={'rows':4}),
        }
