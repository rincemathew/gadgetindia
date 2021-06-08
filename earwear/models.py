from django.db import models


class EarOnlinePrice(models.Model):
    ear_flipkart = models.PositiveIntegerField(blank=True, null=True)
    ear_flipkart_URL = models.URLField(max_length=200, blank=True, null=True)
    ear_amazon = models.PositiveIntegerField(blank=True, null=True)
    ear_amazon_URL = models.URLField(max_length=200, blank=True, null=True)
    ear_tata_cliq = models.PositiveIntegerField(blank=True, null=True)
    ear_tata_cliq_URL = models.URLField(max_length=200, blank=True, null=True)
    ear_reliance_digital = models.PositiveIntegerField(blank=True, null=True)
    ear_reliance_digital_URL = models.URLField(max_length=200, blank=True, null=True)
    ear_mi_store = models.PositiveIntegerField(blank=True, null=True)
    ear_mi_store_URL = models.URLField(max_length=200, blank=True, null=True)
    ear_samsung = models.PositiveIntegerField(blank=True, null=True)
    ear_samsung_URL = models.URLField(max_length=200, blank=True, null=True)
    ear_vivo = models.PositiveIntegerField(blank=True, null=True)
    ear_vivo_URL = models.URLField(max_length=200, blank=True, null=True)
    ear_realme = models.PositiveIntegerField(blank=True, null=True)
    ear_realme_URL = models.URLField(max_length=200, blank=True, null=True)
    ear_oppo = models.PositiveIntegerField(blank=True, null=True)
    ear_oppo_URL = models.URLField(max_length=200, blank=True, null=True)


class EarBrandName(models.Model):
    ear_brand_name = models.CharField(max_length=50)
    ear_brand_name_url = models.SlugField(max_length=50)

    def __str__(self):
        return self.ear_brand_name


class EarModelName(models.Model):
    STATUS = (
        ('Upcoming', 'Upcoming'),
        ('Available', 'Available'),
        ('not available', 'not-available'),
        ('Rumored', 'Rumored'),
    )
    EAR_TYPE = (
        ('Pure Wireless', 'pure-wireless'),
        ('In Ear Wireless', 'in-ear-wireless'),
        ('On Ear Wireless', 'on-ear-wireless'),
        ('In Ear Wired', 'in-ear-wired'),
        ('On Ear Wired', 'on-ear-wired'),
    )
    earBrandName = models.ForeignKey(EarBrandName, on_delete=models.CASCADE, )
    ear_name = models.CharField(max_length=50)
    ear_price = models.PositiveIntegerField(blank=True, null=True)
    ear_name_url = models.SlugField(max_length=50)
    ear_picture = models.ImageField(upload_to='ear_picture/')
    ear_picture_credit = models.URLField(max_length=200)
    ear_release_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    ear_availability = models.BooleanField(default=True)
    ear_status = models.CharField(max_length=15, choices=STATUS, default='Available')
    ear_type = models.CharField(max_length=20, choices=EAR_TYPE, )
    ear_mic = models.BooleanField(default=True)
    ear_mic_features = models.CharField(max_length=500, default='Active noise cancellation', blank=True, null=True)
    ear_battery = models.PositiveIntegerField(blank=True, null=True)
    ear_battery_feature = models.CharField(max_length=1000, default='Charging time:2, Play Time:15 hours, standby Time:100hours', blank=True, null=True)
    ear_battery_connectivity = models.CharField(max_length=500, default='Bluetooth v5.0, USB Type-C', blank=True, null=True)
    ear_waterproof = models.CharField(max_length=100, default='Yes, IPX7', blank=True, null=True)
    ear_colors = models.CharField(max_length=100, blank=True, null=True)
    ear_other_features = models.CharField(max_length=1200, default='Bluetooth Range:10m', blank=True, null=True)
    inside_package = models.CharField(max_length=500, blank=True, null=True)
    ear_price_variant = models.OneToOneField(EarOnlinePrice, on_delete=models.CASCADE)

    def __str__(self):
        return self.ear_name


class EarVariantImage(models.Model):
    earImage = models.ForeignKey(EarModelName, on_delete=models.CASCADE, blank=True, null=True, related_name='ear_Image')
    ear_image = models.ImageField(upload_to='ear_image/')
