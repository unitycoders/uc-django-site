from django import forms
from allauth.account.forms import LoginForm as AALoginForm
from allauth.account.forms import SignupForm as AASignupForm

from lectern.models import Article

from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *

class LoginForm(AALoginForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
		Field('login'),
		'password',
		'remember',
                ButtonHolder(Submit('loginBtn', 'Login', css_class='btn btn-primary btn-block'))
        )
        self.helper.html5_required = True

    class Meta:
	fields = ('login', 'password', 'remember')

class RegisterForm(AASignupForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
		'username',
		'email',
		'password1',
		'password2',
                ButtonHolder(Submit('signup', 'Sign up', css_class='btn btn-primary btn-block'))
        )
        self.helper.html5_required = True

    class Meta:
	fields = ('username', 'email', 'password1', 'password2')
