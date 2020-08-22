# Generated by Django 2.2.14 on 2020-08-01 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandname',
            name='brand_logo',
            field=models.ImageField(blank=True, null=True, upload_to='folder_brand_logo/'),
        ),
        migrations.AddField(
            model_name='brandname',
            name='image_credits',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='brandname',
            name='brand_name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='mobilename',
            name='mobile_name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]