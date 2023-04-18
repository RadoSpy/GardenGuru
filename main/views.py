from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductCategory, ProductList, ProductCategoryGroup, ProductCategoryFeature, ProductListSubCategory
from .models import NavSubCat, Article
import datetime
# Create your views here.



ProductCategoryGroups = ProductCategoryGroup.objects.all().filter(bolDisplay=1).order_by('ProductCategoryGroupName')

ProductCategories = ProductCategory.objects.all().filter(bolDisplay=1).order_by('ProductCategoryName')
ProductCategoriesToDisplay = [obj.id for obj in ProductCategories if obj.ProductCategoryGroupName.bolDisplay == 1]
ProductCategories = ProductCategories.filter(id__in=ProductCategoriesToDisplay)





'''
def index(response):
	return render(response, 'main/index.html',{})

def productcategory(response,id):
	return render(response, 'main/productcategory.html',{})

def articlecategory(response,id):
	return render(response, 'main/articlecategory.html',{})

def article(response, id):
	return render(response, 'main/article.html',{})
'''



def index(response):
	return render(response, 'main/index.html', {'ProductCategories':ProductCategories,
												'ProductCategoryGroups':ProductCategoryGroups,
												'Year':datetime.datetime.now().year,
												'ProductLists':ProductList.objects.all().filter(bolDisplay=1),
												'NavSubCats':NavSubCat.objects.filter(id__in=[3,4,5]).order_by('NavSubCatName'),
												'Articles':Article.objects.all(),
												

												})

def productcategory(response,id):
	pc = ProductCategory.objects.get(id=id)
	features = ProductCategoryFeature.objects.all().filter(ProductCategoryName=pc.id)
	ProductLists = ProductList.objects.all().filter(bolDisplay=1)
	ProductsToDisplay = [obj.id for obj in ProductLists if obj.ProductCategoryName.bolDisplay == 1]
	ProductLists = ProductLists.filter(id__in=ProductsToDisplay)
	ProductLists = ProductLists.filter(ProductCategoryName=pc.id).order_by('-AmazonStar')
	ProductsNotSetCount = ProductLists.filter(ProductListSubCategory=1).count()

	ProductListSubCategories = ProductListSubCategory.objects.all().filter(ProductCategoryName=pc.id)

	return render(response, 'main/productcategory.html', {'ProductCategories':ProductCategories,
												'ProductCategoryGroups':ProductCategoryGroups,
												'pc':pc,
												'Year':datetime.datetime.now().year,
												'ProductLists':ProductLists,
												'features':features,
												'ProductListSubCategories':ProductListSubCategories,
												'ProductsNotSetCount':ProductsNotSetCount,
												'NavSubCats':NavSubCat.objects.filter(id__in=[3,4,5]).order_by('NavSubCatName'),
												'Articles':Article.objects.all(),
												})

def articlecategory(response,id):
	ac = NavSubCat.objects.get(id=id)

	return render(response, 'main/articlecategory.html', {'ProductCategories':ProductCategories,
												'ProductCategoryGroups':ProductCategoryGroups,
												'Year':datetime.datetime.now().year,
												#'ProductLists':ProductList.objects.all().filter(bolDisplay=1),
												'NavSubCats':NavSubCat.objects.filter(id__in=[3,4,5]).order_by('NavSubCatName'),
												'Articles':Article.objects.all().order_by('-LastUpdated'),
												'ac':ac,
												})


def article(response, id):
	a = Article.objects.get(id=id)
	return render(response, 'main/article.html', {'ProductCategories':ProductCategories,
												'ProductCategoryGroups':ProductCategoryGroups,
												'Year':datetime.datetime.now().year,
												#'ProductLists':ProductList.objects.all().filter(bolDisplay=1),
												'NavSubCats':NavSubCat.objects.filter(id__in=[3,4,5]).order_by('NavSubCatName'),
												'Articles':Article.objects.all(),
												'a':a,
												})
											
def allarticles(response):
	return render(response, 'main/allarticles.html', {'ProductCategories':ProductCategories,
													'ProductCategoryGroups':ProductCategoryGroups,
													'Year':datetime.datetime.now().year,
													'NavSubCats':NavSubCat.objects.filter(id__in=[3,4,5]).order_by('NavSubCatName'),
													'Articles':Article.objects.all().order_by('-LastUpdated'),
													})

def allproductcats(response):
	return render(response, 'main/allproductcats.html', {'ProductCategories':ProductCategories,
														'ProductCategoryGroups':ProductCategoryGroups,
														'Year':datetime.datetime.now().year,
														'NavSubCats':NavSubCat.objects.filter(id__in=[3,4,5]).order_by('NavSubCatName'),
														'Articles':Article.objects.all().order_by('-LastUpdated'),
														})
