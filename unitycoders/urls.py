from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework import routers

from lectern.rest_views import ArticleViewSet

from unitycoders import views

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^articles/', include('lectern.urls', namespace='articles', app_name="lectern")),
    url(r'^accounts/', include('gatekeeper.urls', namespace='accounts', app_name='gatekeeper')),

    # Django contrib
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),

    # REST API stuff
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
