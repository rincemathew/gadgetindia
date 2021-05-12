# Generated by Django 2.2.15 on 2020-12-15 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0015_auto_20201215_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilecamera',
            name='primary_camera_features',
            field=models.CharField(max_length=1200),
        ),
        migrations.AlterField(
            model_name='mobilecamera',
            name='secondary_camera_features',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='mobileconnectivity',
            name='audio_jack',
            field=models.CharField(blank=True, default='3.5 mm', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='mobileconnectivitydetails',
            name='sim_type',
            field=models.CharField(choices=[('NANO', 'Nano'), ('MICRO', 'Micro'), ('STANDARD', 'Standard'), ('eSIM', 'eSIM')], default='NANO', max_length=20),
        ),
        migrations.AlterField(
            model_name='mobilestorage',
            name='sim_slot_type',
            field=models.CharField(blank=True, choices=[('Dedicated Slot', 'DEDICATED SLOT'), ('Hybrid Slot', 'HYBRID SLOT')], default='Dedicated Slot', max_length=50, null=True),
        ),
    ]