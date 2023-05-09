# Generated by Django 3.2.18 on 2023-05-09 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articletag',
            name='NavSubCatName',
        ),
        migrations.RemoveField(
            model_name='navsubcat',
            name='NavCatName',
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='ProductCategoryGroupName',
        ),
        migrations.RemoveField(
            model_name='productcategoryfeature',
            name='ProductCategoryName',
        ),
        migrations.RemoveField(
            model_name='productlist',
            name='ProductCategoryName',
        ),
        migrations.RemoveField(
            model_name='productlist',
            name='ProductListSubCategory',
        ),
        migrations.RemoveField(
            model_name='productlistsubcategory',
            name='ProductCategoryName',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='ArticleTag',
        ),
        migrations.DeleteModel(
            name='NavSubCat',
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
        migrations.DeleteModel(
            name='ProductCategoryFeature',
        ),
        migrations.DeleteModel(
            name='ProductList',
        ),
        migrations.DeleteModel(
            name='ProductListSubCategory',
        ),
    ]
