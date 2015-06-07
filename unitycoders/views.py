from django.views.generic import TemplateView

from lectern.models import Article
import random

SITE_LINES = [
	"Battwa battwa battwa mushroom!",
	"Minecraft server is at minecraft.unitycoders.co.uk",
	"I should probably put something useful here...",
	"find us in #unity-coders on freenode"
]

class HomeView(TemplateView):
	template_name = "unitycoders/index.html"

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['articles'] = Article.objects.all()[:5]
		context['line'] = random.choice(SITE_LINES)
		return context
