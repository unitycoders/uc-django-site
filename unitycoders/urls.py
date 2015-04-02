from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework import routers

from lectern.views import ArticleViewSet
from unitycoders.forms import UCLoginForm

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'unitycoders.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name="unitycoders/index.html"), name='home'),
    url(r'^articles/', include('lectern.urls', namespace='articles', app_name="lectern")),
    url(r'^admin/', include(admin.site.urls)),

    # User login stuff
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html', 'authentication_form':UCLoginForm}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),

    # REST API stuff
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
