# Generated by Django 2.2.15 on 2020-11-20 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='article_name',
            field=models.CharField(max_length=254, unique=True),
        ),
    ]
