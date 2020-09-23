# Generated by Django 2.2.15 on 2020-09-23 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0007_auto_20200919_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobileconnectivitydetails',
            name='hybrid_slot',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mobilestorage',
            name='battery_type',
            field=models.CharField(choices=[('Dedicated Slot', 'DEDICATED SLOT'), ('Hybrid Slot', 'HTBRID SLOT')], default='Dedicated Slot', max_length=50),
        ),
        migrations.AlterField(
            model_name='variantcolor',
            name='variantColor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variant_Color', to='mobiles.MobileVariant'),
        ),
        migrations.AlterField(
            model_name='variantimage',
            name='variantImage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variant_Image', to='mobiles.MobileVariant'),
        ),
    ]
