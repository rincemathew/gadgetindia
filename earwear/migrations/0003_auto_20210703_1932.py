# Generated by Django 2.2.15 on 2021-07-03 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('earwear', '0002_auto_20210606_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='earmodelname',
            name='ear_price_variant',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='earwear.EarOnlinePrice'),
        ),
    ]
