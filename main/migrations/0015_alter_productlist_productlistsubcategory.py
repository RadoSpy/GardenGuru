# Generated by Django 3.2.18 on 2023-05-19 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_productlist_productlistsubcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlist',
            name='ProductListSubCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.productlistsubcategory'),
        ),
    ]
