# Generated by Django 2.2.15 on 2020-09-24 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0009_auto_20200923_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilecamera',
            name='primary_camera_features',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='mobilestorage',
            name='sim_slot_type',
            field=models.CharField(choices=[('Dedicated Slot', 'DEDICATED SLOT'), ('Hybrid Slot', 'HYBRID SLOT')], default='Dedicated Slot', max_length=50),
        ),
    ]