# Generated by Django 2.2.14 on 2020-08-16 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0002_auto_20200801_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandname',
            name='brand_logo',
            field=models.ImageField(blank=True, null=True, upload_to='brand-logo/'),
        ),
    ]