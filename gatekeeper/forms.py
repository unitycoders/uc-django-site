from django import forms
from django.contrib.auth.forms import AuthenticationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *

class UCLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UCLoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            'username',
            'password',
            Submit('submit','Sign in'),
        )
	self.helper.html5_required = True
