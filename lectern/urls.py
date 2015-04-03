from django.conf.urls import patterns, url
from views import ArticleListView, ArticleRawView, ArticleDetailView, ArticleCreate, ArticleUpdate, RequestListView, RequestDetailView, RequestCreate

urlpatterns = patterns('',
    url(r'^$', ArticleListView.as_view(), name="index"),
    url(r'^(?P<slug>[a-z0-9_-]+)/$', ArticleListView.as_view(), name="category"),
    url(r'^\+add$', ArticleCreate.as_view(), name="add"),
    url(r'^\+requests/$', RequestListView.as_view(), name="request-list"),
    url(r'^\+requests/(?P<pk>[0-9]+)/$', RequestDetailView.as_view(), name="request-detail"),
    url(r'^\+requests/\+add$', RequestCreate.as_view(), name="request"),
    url(r'^(?P<category>[a-z0-0_-]+)/(?P<slug>[a-z0-9_-]+)/$', ArticleDetailView.as_view(), name="detail"),
    url(r'^(?P<category>[a-z0-9_-]+)/(?P<slug>[a-z0-9_-]+)/\+edit$', ArticleUpdate.as_view(), name="edit"),
    url(r'^(?P<category>[a-z0-9_-]+)/(?P<slug>[a-z0-9_-]+)/\+raw$', ArticleRawView.as_view(), name="edit"),
)
