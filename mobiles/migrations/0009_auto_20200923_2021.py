# Generated by Django 2.2.15 on 2020-09-23 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0008_auto_20200923_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mobilestorage',
            old_name='battery_type',
            new_name='sim_slot_type',
        ),
    ]
