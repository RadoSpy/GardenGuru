from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('index.html', views.index, name='index'),
	path('productcategory/<int:id>', views.productcategory, name='product category'),
	path('articlecategory/<int:id>', views.articlecategory, name='article category'),
	path('article/<int:id>', views.article, name='article'),
	path('allarticles', views.allarticles, name='all articles'),
	path('allproductcats', views.allproductcats, name='all product cats'),
]