# Generated by Django 2.2.15 on 2020-11-20 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0011_auto_20200924_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilegeneral',
            name='dimensions',
            field=models.CharField(default='77 mm x 77 mm x  77 mm', max_length=50),
        ),
        migrations.AlterField(
            model_name='mobilevariant',
            name='mobile_variants',
            field=models.CharField(default='1 GB RAM, 16 GB Storage', max_length=50),
        ),
    ]
