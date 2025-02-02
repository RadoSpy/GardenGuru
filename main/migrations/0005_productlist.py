# Generated by Django 3.2.18 on 2023-05-09 18:10

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_productlistsubcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=200)),
                ('ProductBrand', models.CharField(max_length=200)),
                ('ProductCost', models.FloatField()),
                ('AmazonLink', models.CharField(default='', max_length=1000)),
                ('AmazonStar', models.FloatField(blank=True, default=0)),
                ('Productimg', models.CharField(blank=True, max_length=400)),
                ('ProductDesc', models.CharField(blank=True, default='', max_length=1000)),
                ('ProductScoreSummary', models.CharField(blank=True, max_length=1000)),
                ('ProductLastUpdated', models.DateTimeField(default=django.utils.timezone.now)),
                ('bolDisplay', models.IntegerField(default=1)),
                ('ProductBody', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('ProductCategoryName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productcategory')),
                ('ProductListSubCategory', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.productlistsubcategory')),
            ],
        ),
    ]
