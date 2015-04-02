from django.conf.urls import patterns, url

from forms import UCLoginForm

urlpatterns = patterns('',
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html', 'authentication_form':UCLoginForm}),
	url(r'^logout/$', 'django.contrib.auth.views.logout'),
)
