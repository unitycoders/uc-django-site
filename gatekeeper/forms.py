from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.core.mail import send_mail

from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *

from gatekeeper.models import Invite

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

class RegisterForm(UserCreationForm):
	key = forms.CharField(label="invite key", max_length=50)

	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_class = 'form-horizonal'
		self.helper.label_class = 'col-xs-4'
		self.helper.field_class = 'col-xs-8'
		self.helper.layout = Layout(
			'username',
			'password1',
			'password2',
			'key',
			Submit('submit','Register'),
		)
		self.helper.html5_required = True

	def clean_key(self):
		try:
			form_key = self.cleaned_data['key']
			invite = Invite.objects.get(key=form_key)
			return form_key
		except Invite.DoesNotExist:
			raise forms.ValidationError('Invalid invite key', code='invalid')
