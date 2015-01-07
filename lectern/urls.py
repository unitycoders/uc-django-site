from django.conf.urls import patterns, url
from views import ArticleListView, ArticleDetailView

urlpatterns = patterns('',
    url(r'^$', ArticleListView.as_view(), name="index"),
    url(r'^(?P<slug>[a-z0-9_-]+)/$', ArticleDetailView.as_view(), name="detail"),
)
