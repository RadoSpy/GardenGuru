# Generated by Django 3.2.18 on 2023-04-11 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20230412_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletag',
            name='NavSubCatName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.navsubcat'),
        ),
    ]
