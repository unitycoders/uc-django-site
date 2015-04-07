from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from gatekeeper.forms import RegisterForm
from gatekeeper.models import Invite, Member

# Create your views here.
class RegisterView(FormView):
	form_class = RegisterForm
	template_name = "gatekeeper/register.html"

	def form_valid(self, form):
		# TODO mark the invite as used
		print(form.cleaned_data['key'])
		invite = Invite.objects.get(key=form.cleaned_data['key'])

		user = User.objects.create_user(form.cleaned_data['username'], invite.email, form.cleaned_data['password1'])
		user.save()
		return super(RegisterView, self).form_valid(form)

class UserList(ListView):
	model = Member

class UserProfile(DetailView):
	model = Member
	slug_field = 'username'
