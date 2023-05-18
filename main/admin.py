from django.contrib import admin

from .models import ProductCategoryGroup, ProductCategory, ProductListSubCategory, ProductList, ProductCategoryFeature, ProductCategoryMasterGroup, ProductCategoryText
from .models import NavCat, NavSubCat, ArticleTag, Article
# Register your models here.


admin.site.register(ProductCategoryFeature)

admin.site.register(NavCat)
admin.site.register(NavSubCat)
admin.site.register(Article)
admin.site.register(ArticleTag)
admin.site.register(ProductCategory)
admin.site.register(ProductCategoryGroup)
admin.site.register(ProductCategoryMasterGroup)
admin.site.register(ProductList)
admin.site.register(ProductListSubCategory)
admin.site.register(ProductCategoryText)
