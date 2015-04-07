from django.conf.urls import patterns, url
from views import ArticleListView, ArticleRawView, ArticleDetailView, ArticleCreate, ArticleUpdate

urlpatterns = patterns('',
    url(r'^$', ArticleListView.as_view(), name="index"),
    url(r'^(?P<slug>[a-z0-9_-]+)/$', ArticleListView.as_view(), name="category"),
    url(r'^\+add$', ArticleCreate.as_view(), name="add"),
    url(r'^(?P<category>[a-z0-0_-]+)/(?P<slug>[a-z0-9_-]+)/$', ArticleDetailView.as_view(), name="detail"),
    url(r'^(?P<category>[a-z0-9_-]+)/(?P<slug>[a-z0-9_-]+)/\+edit$', ArticleUpdate.as_view(), name="edit"),
    url(r'^(?P<category>[a-z0-9_-]+)/(?P<slug>[a-z0-9_-]+)/\+raw$', ArticleRawView.as_view(), name="raw"),
)
