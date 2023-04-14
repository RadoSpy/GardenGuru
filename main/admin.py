from django.contrib import admin
from .models import ProductCategory, ProductList, ProductCategoryGroup, ProductCategoryFeature, ProductListSubCategory
from .models import NavCat, NavSubCat, Article, ArticleTag

# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(ProductList)
admin.site.register(ProductCategoryGroup)
admin.site.register(ProductCategoryFeature)
admin.site.register(ProductListSubCategory)
admin.site.register(NavCat)
admin.site.register(NavSubCat)
admin.site.register(Article)
admin.site.register(ArticleTag)