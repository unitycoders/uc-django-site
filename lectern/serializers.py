from models import Article
from rest_framework import serializers

from markdown_deux import markdown

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'slug', 'created', 'modified', 'abstract', 'body')


class MarkdownSerializer(serializers.Serializer):
	body = serializers.CharField(style={'base_template': 'textarea.html'})

	def to_representation(selfi, obj):
		data = markdown(obj['body'])
		return {
			'markdown': markdown(obj['body']),
			'metadata': data.metadata,
		}
		
