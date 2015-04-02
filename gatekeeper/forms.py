from django import forms
from django.contrib.auth.forms import AuthenticationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *

class UCLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UCLoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password',
            Submit('submit','Sign in'),
        )
	self.helper.html5_required = True

class RegisterForm(forms.Form):
	username = forms.CharField(label='username', max_length=100)
	password = forms.CharField(label='password', widget=forms.PasswordInput, max_length=100)
	key = forms.CharField(label="invite key", max_length=50)

	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			'username',
			'password',
			'key',
			Submit('submit','Register'),
		)
		self.helper.html5_required = True
