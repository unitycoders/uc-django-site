from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from lectern.views import ArticleViewSet
from unitycoders.views import HomeView

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^articles/', include('lectern.urls', namespace='articles', app_name="lectern")),
    url(r'^admin/', include(admin.site.urls)),

    # REST API stuff
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
