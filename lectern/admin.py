from django.contrib import admin
from models import Article, RelatedLink, Category

# Register your models here.
class RelatedLinkInline(admin.TabularInline):
	model = RelatedLink
	extra = 1

class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	search_fields = ['title']
	list_display = ['title', 'slug', 'category']
	list_filter = ['created', 'modified']
	inlines = [
		RelatedLinkInline
	]
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
