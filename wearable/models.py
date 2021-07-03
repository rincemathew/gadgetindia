from django.db import models


class WearOnlinePrice(models.Model):
    wear_flipkart = models.PositiveIntegerField(blank=True, null=True)
    wear_flipkart_URL = models.URLField(max_length=200, blank=True, null=True)
    wear_amazon = models.PositiveIntegerField(blank=True, null=True)
    wear_amazon_URL = models.URLField(max_length=200, blank=True, null=True)
    wear_tata_cliq = models.PositiveIntegerField(blank=True, null=True)
    wear_tata_cliq_URL = models.URLField(max_length=200, blank=True, null=True)
    wear_reliance_digital = models.PositiveIntegerField(blank=True, null=True)
    wear_reliance_digital_URL = models.URLField(max_length=200, blank=True, null=True)
    wear_mi_store = models.PositiveIntegerField(blank=True, null=True)
    wear_mi_store_URL = models.URLField(max_length=200, blank=True, null=True)
    wear_samsung = models.PositiveIntegerField(blank=True, null=True)
    wear_samsung_URL = models.URLField(max_length=200, blank=True, null=True)
    wear_vivo = models.PositiveIntegerField(blank=True, null=True)
    wear_vivo_URL = models.URLField(max_length=200, blank=True, null=True)
    wear_realme = models.PositiveIntegerField(blank=True, null=True)
    wear_realme_URL = models.URLField(max_length=200, blank=True, null=True)
    wear_oppo = models.PositiveIntegerField(blank=True, null=True)
    wear_oppo_URL = models.URLField(max_length=200, blank=True, null=True)


class WearBrandName(models.Model):
    wear_brand_name = models.CharField(max_length=50)
    wear_brand_name_url = models.SlugField(max_length=50)

    def __str__(self):
        return self.wear_brand_name


class WearDimensions(models.Model):
    wear_dimensions = models.CharField(blank=True, null=True, max_length=50, default='77 mm x 77 mm x  77 mm')
    wear_weight = models.FloatField(blank=True, null=True)


class WearConnectivity(models.Model):
    wear_callfunction = models.CharField(blank=True, null=True, max_length=500, default='No,')
    wear_bluetooth = models.CharField(blank=True, null=True, max_length=50, default='Yes, Version:5.1')
    wear_wifi = models.CharField(blank=True, null=True, max_length=50, default='No,')
    wear_GPS = models.CharField(blank=True, null=True, max_length=50, default='Yes,')


class WearDisplay(models.Model):
    wear_resolutions = models.CharField(blank=True, null=True, max_length=50, default='320 x 320 Pixels')
    wear_size = models.FloatField(blank=True, null=True)
    wear_type = models.CharField(blank=True, null=True, max_length=50, default='LCD')
    wear_size = models.CharField(blank=True, null=True, max_length=800, default='HD Display')


class WearModelName(models.Model):
    STATUS = (
        ('Upcoming', 'Upcoming'),
        ('Available', 'Available'),
        ('not available', 'not-available'),
        ('Rumored', 'Rumored'),
    )
    WEAR_TYPE = (
        ('Band', 'band'),
        ('Watch', 'watch'),
    )
    wearBrandName = models.ForeignKey(WearBrandName, on_delete=models.CASCADE, )
    wear_name = models.CharField(max_length=50)
    wear_name_url = models.SlugField(max_length=50)
    wear_price = models.PositiveIntegerField(blank=True, null=True)
    wear_picture = models.ImageField(upload_to='wear_picture/')
    wear_picture_credit = models.URLField(max_length=200)
    wear_release_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    wear_availability = models.BooleanField(default=True)
    wear_status = models.CharField(max_length=15, choices=STATUS, default='Available')
    wear_type = models.CharField(max_length=20, choices=WEAR_TYPE, )
    ideal_for = models.CharField(max_length=200, blank=True, null=True, default='Unisex')
    wear_touch = models.BooleanField(default=True)
    wear_os = models.CharField(max_length=100, blank=True, null=True, default='RTOS')
    wear_functions = models.CharField(max_length=800, blank=True, null=True, default='Activity Tracking,Sleep Tracking, Heart rate Tracking')
    wear_compatible_device = models.CharField(max_length=200, blank=True, null=True, default='Phones with Android 5.0 and Above or IOS 10 and Above')
    wear_sensors = models.CharField(max_length=200, blank=True, null=True, default='3-Axis Accelerometer, Barometer, Gyroscope, Ambient Light Sensor, PPG Heart Rate Sensor, Geomagnetic Sensor, Compass')
    wear_battery = models.PositiveIntegerField(blank=True, null=True)
    wear_battery_feature = models.CharField(max_length=1000, default='Charging time:120 minutes, Battery Life:10 days, Battery Type: Lithiun Polymer', blank=True, null=True)
    wear_battery_connectivity = models.CharField(max_length=500, default='Bluetooth v5.1, USB Type-C, GPS', blank=True, null=True)
    wear_water_resistant = models.CharField(max_length=100, default='Yes, upto 50 m', blank=True, null=True)
    wear_colors = models.CharField(max_length=100, blank=True, null=True, default='Dial Color:Black & Strap Color:Blue')
    wear_other_features = models.CharField(max_length=1200, default='3 Color Variants and 4 Color Strap Options, Built-in GPS & Glonass', blank=True, null=True)
    inside_package = models.CharField(max_length=500, blank=True, null=True)
    wearDimensions = models.OneToOneField(WearDimensions, on_delete=models.CASCADE, blank=True, null=True)
    wearConnectivity = models.OneToOneField(WearConnectivity, on_delete=models.CASCADE, blank=True, null=True)
    wearDisplay = models.OneToOneField(WearDisplay, on_delete=models.CASCADE, blank=True, null=True)
    wear_price_variant = models.OneToOneField(WearOnlinePrice, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.ear_name


class WearVariantImage(models.Model):
    wearImage = models.ForeignKey(WearModelName, on_delete=models.CASCADE, blank=True, null=True, related_name='wear_Image')
    wear_image = models.ImageField(upload_to='wear_image/')
