# Generated by Django 3.2.18 on 2023-04-14 16:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategoryFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FeatureName', models.CharField(max_length=200)),
                ('FeatureDesc', models.CharField(blank=True, max_length=1000)),
                ('FeatureLastUpdated', models.DateTimeField(default=django.utils.timezone.now)),
                ('ProductCategoryName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productcategory')),
            ],
        ),
    ]
