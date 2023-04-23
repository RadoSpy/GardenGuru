'''from django.contrib.sitemaps import Sitemap
from main.models import Article
from main.models import ProductCategory

class ArticleSitemap(Sitemap):

	def items(self):
		return Article.objects.all()

class ProductCategorySitemap(Sitemap):

	def items(self):
		return ProductCategory.objects.all()'''