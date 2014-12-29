from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'unitycoders.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^lectern/', include('lectern.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # REST API stuff
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
