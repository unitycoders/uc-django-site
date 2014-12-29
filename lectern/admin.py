from django.contrib import admin
from models import Article, RelatedLink

# Register your models here.
class RelatedLinkInline(admin.TabularInline):
	model = RelatedLink

class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	inlines = [
		RelatedLinkInline
	]
admin.site.register(Article, ArticleAdmin)
