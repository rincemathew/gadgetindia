# Generated by Django 2.2.15 on 2021-01-12 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0016_auto_20201215_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobilevariant',
            name='mobile_url_themes_name',
            field=models.CharField(default='brand+name+variant', max_length=50),
        ),
        migrations.AlterField(
            model_name='brandname',
            name='brand_name_url',
            field=models.CharField(default='company', max_length=30),
        ),
    ]