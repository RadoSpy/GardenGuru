# Generated by Django 3.2.18 on 2023-05-09 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_productlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavSubCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NavSubCatName', models.CharField(max_length=200)),
                ('LastUpdated', models.DateTimeField(auto_now_add=True)),
                ('ArticleCategoryimg', models.CharField(blank=True, max_length=200, null=True)),
                ('NavCatName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.navcat')),
            ],
        ),
    ]
