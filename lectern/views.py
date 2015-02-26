from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from models import Article, Category, Request
from forms import ArticleForm

class ArticleListView(ListView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ArticleDetailView(DetailView):
    model = Article

class ArticleRawView(ArticleDetailView):
    """Like article detail view, only display raw markdown"""
    template_name = "lectern/article_raw.html"

    def render_to_response(self, context, **response_kwargs):
        response = super(ArticleRawView, self).render_to_response(context, **response_kwargs)
        response['content-type'] = 'text/plain'
        return response

class ArticleCreate(CreateView):
    model = Article
    form_class = ArticleForm

class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm

class RequestListView(ListView):
    model = Request

class RequestDetailView(DetailView):
    model = Request

class RequestCreate(CreateView):
    model = Request

# REST api views
from rest_framework import viewsets
from lectern.serializers import ArticleSerializer
class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows articles to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
