from django.shortcuts import render
from django.http import HttpResponse

from .models import ProductCategory, ProductList, ProductCategoryGroup, ProductCategoryMasterGroup, ProductCategoryFeature, ProductListSubCategory
from .models import NavSubCat, Article
from .models import ProductCategoryText

import datetime
# Create your views here.


ProductCategoryMasterGroups = ProductCategoryMasterGroup.objects.all().order_by('ProductCategoryMasterGroupName')
ProductCategoryGroups = ProductCategoryGroup.objects.all().filter(bolDisplay=1).order_by('ProductCategoryGroupName')

ProductCategories = ProductCategory.objects.filter(bolDisplay=1).order_by('ProductCategoryName')
#ProductCategoriesToDisplay = [obj.id for obj in ProductCategories if obj.ProductCategoryGroupName.bolDisplay == 1]
#ProductCategories = ProductCategories.filter(id__in=ProductCategoriesToDisplay)
ProductCategories = ProductCategories.filter(ProductCategoryGroupName__bolDisplay=1)

NavSubCats = NavSubCat.objects.filter(id__in=[3,4,5]).order_by('NavSubCatName')
Articles = Article.objects.all().order_by('-LastUpdated')

'''
def index(response):
	return render(response, 'main/index.html',{})

def productcategory(response,id):
	return render(response, 'main/productcategory.html',{})

def articlecategory(response,id):
	return render(response, 'main/articlecategory.html',{})

def article(response, id):
	return render(response, 'main/article.html',{})

def allarticles(response, id):
	return render(response, 'main/article.html',{})

def allproductcats(response, id):
	return render(response, 'main/article.html',{})

def sitemap(response, id):
	return render(response, 'main/article.html',{})

'''



def index(response):
	return render(response, 'main/index.html', {'ProductCategoryMasterGroups':ProductCategoryMasterGroups,
												'ProductCategories':ProductCategories,
												'ProductCategoryGroups':ProductCategoryGroups,
												'Year':datetime.datetime.now().year,
												'ProductLists':ProductList.objects.filter(bolDisplay=1).count(),
												'NavSubCats':NavSubCats,
												'Articles':Articles,
												

												})

def productcategory(response,id):
	pc = ProductCategory.objects.get(id=id)
	ProductLists = ProductList.objects.filter(ProductCategoryName=id)
	features = ProductCategoryFeature.objects.filter(ProductCategoryName=id)

	ProductLists = ProductLists.filter(bolDisplay=1)
	ProductLists = ProductLists.order_by('-AmazonStar','SaleRank')

	#ProductsNotSetCount = ProductLists.filter(ProductListSubCategory=1).count()
	ProductsNotSetCount = ProductLists.filter(ProductListSubCategory=1).count()

	ProductListSubCategories = ProductListSubCategory.objects.filter(ProductCategoryName=id)

	pct = ProductCategoryText.objects.filter(ProductCategory=id)

	return render(response, 'main/productcategory.html', {
												'ProductCategoryMasterGroups':ProductCategoryMasterGroups,
												'ProductCategories':ProductCategories,
												'ProductCategoryGroups':ProductCategoryGroups,
												'pc':pc,
												'Year':datetime.datetime.now().year,
												'ProductLists':ProductLists,
												'features':features,
												'ProductListSubCategories':ProductListSubCategories,
												'ProductsNotSetCount':ProductsNotSetCount,
												'NavSubCats':NavSubCats,
												'Articles':Articles,
												'pct':pct,
												})

def articlecategory(response,id):
	ac = NavSubCat.objects.get(id=id)

	return render(response, 'main/articlecategory.html', {
												'ProductCategoryMasterGroups':ProductCategoryMasterGroups,
												'ProductCategories':ProductCategories,
												'ProductCategoryGroups':ProductCategoryGroups,
												'Year':datetime.datetime.now().year,
												#'ProductLists':ProductList.objects.all().filter(bolDisplay=1),
												'NavSubCats':NavSubCats,
												'Articles':Articles,
												'ac':ac,
												})


def article(response, id):
	a = Article.objects.get(id=id)
	return render(response, 'main/article.html', {
												'ProductCategoryMasterGroups':ProductCategoryMasterGroups,
												'ProductCategories':ProductCategories,
												'ProductCategoryGroups':ProductCategoryGroups,
												'Year':datetime.datetime.now().year,
												#'ProductLists':ProductList.objects.all().filter(bolDisplay=1),
												'NavSubCats':NavSubCats,
												'Articles':Articles,
												'a':a,
												})
											
def allarticles(response):
	return render(response, 'main/allarticles.html', {
													'ProductCategoryMasterGroups':ProductCategoryMasterGroups,
													'ProductCategories':ProductCategories,
													'ProductCategoryGroups':ProductCategoryGroups,
													'Year':datetime.datetime.now().year,
													'NavSubCats':NavSubCats,
													'Articles':Articles,
													})

def allproductcats(response):
	return render(response, 'main/allproductcats.html', {
														'ProductCategoryMasterGroups':ProductCategoryMasterGroups,
														'ProductCategories':ProductCategories,
														'ProductCategoryGroups':ProductCategoryGroups,
														'Year':datetime.datetime.now().year,
														'NavSubCats':NavSubCats,
														'Articles':Articles,
														})

def sitemap(response):
	return render(response, 'main/sitemap.html', {
													'ProductCategoryMasterGroups':ProductCategoryMasterGroups,
													'ProductCategories':ProductCategories,
													'ProductCategoryGroups':ProductCategoryGroups,
													'Year':datetime.datetime.now().year,
													'NavSubCats':NavSubCats,
													'Articles':Articles,
													})
