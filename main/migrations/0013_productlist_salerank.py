# Generated by Django 3.2.18 on 2023-05-18 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_article_productcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlist',
            name='SaleRank',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
