# Generated by Django 2.2.15 on 2020-09-16 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0003_auto_20200916_2027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mobilevariant',
            old_name='mobileVariant',
            new_name='mobileConnectivity',
        ),
    ]