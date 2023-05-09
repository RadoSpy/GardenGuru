# Generated by Django 3.2.18 on 2023-05-09 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_navsubcat'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ArticleTagName', models.CharField(max_length=200)),
                ('LastUpdated', models.DateTimeField(auto_now_add=True)),
                ('NavSubCatName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.navsubcat')),
            ],
        ),
    ]
