from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.db.models import Count
# Create your models here.


class NavCat(models.Model):
	NavCatName = models.CharField(max_length=200)
	LastUpdated = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.NavCatName

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

	def get_absolute_url(self):
		return reverse('product category', args=[str(self.id)])


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




class NavSubCat(models.Model):
	NavSubCatName = models.CharField(max_length=200)
	LastUpdated = models.DateTimeField(auto_now_add=True)
	NavCatName = models.ForeignKey(NavCat, on_delete=models.CASCADE)
	ArticleCategoryimg = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.NavSubCatName	


'''

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

	def get_absolute_url(self):
		return reverse('article', args=[str(self.id)])



class ProductCategoryFeature(models.Model):
	FeatureName = models.CharField(max_length=200)
	FeatureDesc = models.CharField(max_length=1000, blank=True)
	FeatureLastUpdated = models.DateTimeField(default=timezone.now)
	ProductCategoryName = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

	def __str__(self):
		return self.FeatureName
'''
