from django.urls import path
from . import views

'''from main.sitemaps import ArticleSitemap,ProductCategorySitemap, StaticViewSitemap
from django.contrib.sitemaps.views import sitemap 
'''
'''
sitemaps = {
	'Sitemap_Articles':ArticleSitemap,
	'Sitemap_ProductCategories':ProductCategorySitemap,
	'Sitemap_static':StaticViewSitemap,
}
'''

urlpatterns = [
	path('', views.index, name='index'),
	#path('index.html', views.index, name='index'),
	#path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'), 
	#path('productcategory/<int:id>', views.productcategory, name='product category'),
	#path('articlecategory/<int:id>', views.articlecategory, name='article category'), 
	#path('article/<int:id>', views.article, name='article'),
	#path('allarticles', views.allarticles, name='all articles'),
	#path('allproductcats', views.allproductcats, name='all product cats'),
	#path('sitemap', views.sitemap, name='sitemap'),
]