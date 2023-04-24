from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from main.models import Article
from main.models import ProductCategory

class ArticleSitemap(Sitemap):
	def items(self):
		return Article.objects.all()

class ProductCategorySitemap(Sitemap):

	def items(self):
		return ProductCategory.objects.all()

class StaticViewSitemap(Sitemap):

	def items(self):
		return ['sitemap']

	def location(self, item):
		return reverse(item)