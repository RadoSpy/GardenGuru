from django.contrib import admin
from .models import ProductCategoryGroup 
''', ProductCategory, ProductList, ProductListSubCategory, ProductCategoryFeature
from .models import NavCat, NavSubCat, Article, ArticleTag
'''
# Register your models here.


#admin.site.register(ProductCategoryFeature)

#admin.site.register(NavCat)
#admin.site.register(NavSubCat)
#admin.site.register(Article)
#admin.site.register(ArticleTag)

#admin.site.register(ProductCategory)
admin.site.register(ProductCategoryGroup)
#admin.site.register(ProductList)
#admin.site.register(ProductListSubCategory)