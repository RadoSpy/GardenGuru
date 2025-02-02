# Generated by Django 3.2.18 on 2023-05-09 18:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_productcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductListSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubCategoryName', models.CharField(max_length=400)),
                ('ProductListSubCategoryLastUpdated', models.DateTimeField(default=django.utils.timezone.now)),
                ('ProductCategoryName', models.ForeignKey(default=22, on_delete=django.db.models.deletion.CASCADE, to='main.productcategory')),
            ],
        ),
    ]
