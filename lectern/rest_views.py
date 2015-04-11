from django.views.decorators.csrf import csrf_exempt

from rest_framework import status, viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from lectern.models import Article
from lectern.serializers import MarkdownSerializer, ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows articles to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @list_route(methods=['GET','POST'])
    def preview(self, request, *args, **kwargs):
	serializer = MarkdownSerializer(data=request.data)
	if serializer.is_valid():
		return Response(serializer.data)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
