from django.contrib import admin
from models import Article, RelatedLink

# Register your models here.
class RelatedLinkInline(admin.TabularInline):
	model = RelatedLink
	extra = 1

class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	search_fields = ['title']
	list_display = ['__unicode__', 'slug']
	list_filter = ['created', 'modified']
	inlines = [
		RelatedLinkInline
	]
admin.site.register(Article, ArticleAdmin)
