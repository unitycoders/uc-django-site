from django.conf.urls import patterns, url
from views import ArticleListView, ArticleDetailView, ArticleCreate, ArticleUpdate

urlpatterns = patterns('',
    url(r'^$', ArticleListView.as_view(), name="index"),
    url(r'^\+add$', ArticleCreate.as_view(), name="add"),
    url(r'^(?P<slug>[a-z0-9_-]+)/$', ArticleDetailView.as_view(), name="detail"),
    url(r'^(?P<slug>[a-z0-9_-]+)/\+edit$', ArticleUpdate.as_view(), name="edit"),
)
