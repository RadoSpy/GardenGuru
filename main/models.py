from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.db.models import Count
# Create your models here.


class ProductCategoryGroup(models.Model):
	ProductCategoryGroupName = models.CharField(max_length=200)
	ProductCategoryGroupimg = models.CharField(max_length=200)
	ProductCategoryLastUpdated = models.DateTimeField(default=timezone.now)
	bolDisplay = models.IntegerField(default=1)

	def __str__(self):
		return self.ProductCategoryGroupName

class ProductCategory(models.Model):
	ProductCategoryName = models.CharField(max_length=200)
	ProductCategoryGroupName = models.ForeignKey(ProductCategoryGroup, on_delete=models.CASCADE)
	ProductCategoryDesc1 = models.CharField(max_length=1000)
	ProductCategoryDesc2 = models.CharField(max_length=1000)
	ProductCategoryDesc3 = models.CharField(max_length=1000)
	ProductCategoryFeatures = models.CharField(max_length=1000)
	ProductCategoryAddInfo = models.CharField(max_length=1000, blank=True)
	ProductCategoryimg = models.CharField(max_length=400)
	ProductCategoryLastUpdated = models.DateTimeField(default=timezone.now)
	bolDisplay = models.IntegerField(default=1)


	def __str__(self):
		return self.ProductCategoryName

	'''
	To add, enter following into shell:
	from main.models import ProductCategory, ProductList, ProductCategoryGroup
	catname = 'Pressure Washers'
	catname2 = catname.replace(' ','')
	p= ProductCategoryGroup.objects.get(ProductCategoryGroupName = 'Outdoor Power Tools')
	p.productcategory_set.create(ProductCategoryName=catname,
						ProductCategoryGroupName=p.ProductCategoryGroupName,
						ProductCategoryDesc1='What are they + SEO keywords',
						ProductCategoryDesc2='Additional notes',
						ProductCategoryDesc3='How we test, how we score and what we look for',
						ProductCategoryFeatures='Feature 1;Feature 2;Feature 3',
						ProductCategoryAddInfo='Any other considerations',
						ProductCategoryimg='assets/img/productcategories/' + catname2 + '.jpg',
						)
	p.save()

	'''


class ProductListSubCategory(models.Model):
	SubCategoryName = models.CharField(max_length=400)
	ProductCategoryName = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, default=22)
	ProductListSubCategoryLastUpdated = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.SubCategoryName



class ProductList(models.Model):
	ProductName = models.CharField(max_length=200)
	ProductCategoryName = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
	ProductBrand = models.CharField(max_length=200)
	ProductCost = models.FloatField()
	AmazonLink = models.CharField(max_length=1000,default='')
	AmazonStar = models.FloatField(default=0, blank=True)
	Productimg = models.CharField(max_length=400, blank=True)
	ProductDesc = models.CharField(max_length=1000, default='', blank=True)
	ProductScoreSummary = models.CharField(max_length=1000, blank=True)
	ProductListSubCategory = models.ForeignKey(ProductListSubCategory, on_delete=models.CASCADE, default=1)
	ProductLastUpdated = models.DateTimeField(default=timezone.now)
	bolDisplay = models.IntegerField(default=1)

	def __str__(self):
		return self.ProductName

	def ProductScores(self):
		return [i.split(':') for i in self.ProductScoreSummary.split(';')]

	def AmazonStarRating(self):
		if self.AmazonStar>=4.5:
			return 'Amazing'
		elif self.AmazonStar>=4.0:
			return 'Great'
		else:
			return 'Good'




	'''
	from main.models import ProductList, ProductCategories
	p = ProductCategories.objects.get(ProductCategoryName = 'Propagators')
	p.productlist_set.create(ProductName='test1',
							ProductCategoryName=p.ProductCategoryName,
							ProductBrand='Brand Test 1',
							ProductCost='10.99',
							Productimg='assets/img/portfolio/Propagators.jpg',
							ProductScore='58',
							ProductScoreSummary='Feature 1: 100; Feature 2: 30, Feature 3: 50, Feature 4:20',
							ProductPros='Pro1 test; Pro2 test; Pro3 test',
							ProductCons='Con1 test; Con2 test; Con3 test',
							bolDisplay=1)

	'''

class ProductCategoryFeature(models.Model):
	FeatureName = models.CharField(max_length=200)
	FeatureDesc = models.CharField(max_length=1000, blank=True)
	FeatureLastUpdated = models.DateTimeField(default=timezone.now)
	ProductCategoryName = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

	def __str__(self):
		return self.FeatureName

class NavCat(models.Model):
	NavCatName = models.CharField(max_length=200)
	LastUpdated = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.NavCatName

class NavSubCat(models.Model):
	NavSubCatName = models.CharField(max_length=200)
	LastUpdated = models.DateTimeField(auto_now_add=True)
	NavCatName = models.ForeignKey(NavCat, on_delete=models.CASCADE)
	ArticleCategoryimg = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.NavSubCatName



class ArticleTag(models.Model):
	ArticleTagName = models.CharField(max_length=200)
	NavSubCatName = models.ForeignKey(NavSubCat, on_delete=models.CASCADE)
	LastUpdated = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.ArticleTagName


class Article(models.Model):
	ArticleName = models.CharField(max_length=200)
	Articleimg = models.CharField(max_length=200, blank=True, null=True)
	ArticleTagName = models.ForeignKey(ArticleTag, on_delete=models.CASCADE, blank=True, null=True)
	NavSubCatName = models.ForeignKey(NavSubCat, on_delete=models.CASCADE)

	ArticleBody = RichTextField(blank=True, null=True)

	LastUpdated = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.ArticleName

	def ArticlesCount(self):
		self.annotate(num_articles=Count("id"))


