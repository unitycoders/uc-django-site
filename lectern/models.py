from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey('Category')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    abstract = models.TextField(blank=True, null=True)
    body = models.TextField()

    def get_absolute_url(self):
            from django.core.urlresolvers import reverse
            return reverse('lectern:detail', kwargs={'slug':self.slug, 'category':self.category.slug})

    def __unicode__(self):
        return self.title

class RelatedLink(models.Model):
    title = models.CharField(max_length=80)
    url = models.URLField()
    article = models.ForeignKey(Article)

class Category(models.Model):
    title = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25, unique=True)
    abstract = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title
