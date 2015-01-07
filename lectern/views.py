from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from models import Article
from forms import ArticleForm

class ArticleListView(ListView):
	model = Article

class ArticleDetailView(DetailView):
	model = Article

class ArticleCreate(CreateView):
    model = Article
    form_class = ArticleForm

class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm

# REST api views
from rest_framework import viewsets
from lectern.serializers import ArticleSerializer
class ArticleViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows articles to be viewed or edited.
	"""
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
