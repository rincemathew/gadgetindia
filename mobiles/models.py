from django.db import models


class BrandName(models.Model):
    brand_name = models.CharField(max_length=30, unique=True)
    brand_logo = models.ImageField(upload_to='brand-logo/', blank=True, null=True)

    def __str__(self):
        return self.brand_name


class MobileName(models.Model):
    brandName = models.ForeignKey(BrandName, on_delete=models.CASCADE, related_name='mobiles_name')
    mobile_name = models.CharField(max_length=50)
    mobile_image = models.ImageField(upload_to='mobile_image/')

    def __str__(self):
        return self.mobile_name


class MobileGeneral(models.Model):
    OS_CHOICES = (
        ('ANDROID', 'Android'),
        ('IOS', 'ios'),
    )
    release_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    os = models.CharField(max_length=1, choices=OS_CHOICES)
    os_version = models.CharField(max_length=10, null=True, blank=True)
    UI_version = models.CharField(max_length=50, null=True, blank=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    is_available = models.BooleanField(max_length=None, default=True)
    dimensions = models.CharField(max_length=50)
    weight = models.FloatField()
    slots = models.CharField(max_length=200, default='Dual SIM(2) + Dedicated Memory Card Slot')


class MobilePerformance(models.Model):
    ram = models.PositiveIntegerField()
    processor = models.CharField(max_length=50)
    processor_company = models.CharField(max_length=50)
    clock_speed = models.FloatField()


class MobileStorage(models.Model):
    device_storage = models.PositiveIntegerField()
    expandable_memory = models.BooleanField(default=True)
    expandable_memory_capacity = models.IntegerField(blank=True, null=True)
    OTG_support = models.BooleanField(blank=True, null=True, default=True)


class MobileCamera(models.Model):
    primary_camera = models.IntegerField()
    primary_camera_str = models.CharField(max_length=501)
    primary_camera_features = models.CharField(max_length=500)
    secondary_camera = models.IntegerField()
    secondary_camera_str = models.CharField(max_length=50)
    secondary_camera_features = models.CharField(max_length=500)


class MobileBattery(models.Model):
    BATTERY_TYPE_CHOICES = (
        ('LI-ION', 'Li-ion'),
        ('LI-POLY', 'Li-poly'),
    )
    battery_capacity = models.IntegerField()
    battery_type = models.CharField(max_length=1, choices=BATTERY_TYPE_CHOICES, blank=True, null=True)
    fast_charger = models.BooleanField(default=True, blank=True, null=True)
    fast_charging = models.CharField(max_length=200, blank=True, null=True)
    replaceable = models.BooleanField(default=False, blank=True, null=True)
    talk_time = models.FloatField(blank=True, null=True)


class MobileDisplay(models.Model):
    screen_size = models.FloatField()
    resolution = models.CharField(max_length=50)
    resolution_type = models.CharField(max_length=50, blank=True, null=True)
    GPU = models.CharField(max_length=50, blank=True, null=True)
    display_type = models.CharField(max_length=100)
    display_features = models.CharField(max_length=300, blank=True, null=True)


class MobileConnectivityDetails(models.Model):
    SIM_TYPE = (
        ('NANO', 'Nano'),
        ('MICRO', 'Micro'),
        ('STANDARD', 'Standard'),
    )
    sim_type = models.CharField(max_length=1, choices=SIM_TYPE, default='NANO')
    five_g = models.BooleanField(default=False)
    four_g = models.BooleanField(default=True)
    three_g = models.BooleanField(default=True)
    two_g = models.BooleanField(default=True)
    SAR_value = models.CharField(max_length=100, blank=True, null=True)
    wi_fi = models.CharField(max_length=100, blank=True, null=True)
    bluetooth = models.CharField(max_length=100, blank=True, null=True, default='v5.0')
    GPS = models.BooleanField(default=True)


class MobileSensor(models.Model):
    FINGER_CHOICES = (
        ('SIDE', 'Side'),
        ('REAR', 'REAR'),
        ('FRONTSIDE', 'Front Side'),
        ('ONSCREEN', 'Onscreen'),
    )
    fingerprint_sensor = models.BooleanField(default=True)
    fingerprint_position = models.CharField(max_length=1, choices=FINGER_CHOICES, blank=True, null=True)
    other_sensor = models.CharField(max_length=300)


class OtherFeature(models.Model):
    other_Feature = models.CharField(max_length=500, blank=True, null=True)
    in_the_box = models.CharField(max_length=300, blank=True, null=True)
    warranty = models.CharField(max_length=300, blank=True, null=True)


class VariantImage(models.Model):
    variant_image = models.ImageField(upload_to='variant_image/')


class PriceURL(models.Model):
    flipkart_URL = models.URLField(max_length=200, blank=True, null=True)
    amazon_URL = models.URLField(max_length=200, blank=True, null=True)
    tata_cliq_URL = models.URLField(max_length=200, blank=True, null=True)
    reliance_digital_URL = models.URLField(max_length=200, blank=True, null=True)


class OnlinePrice(models.Model):
    flipkart = models.PositiveIntegerField(blank=True, null=True)
    amazon = models.PositiveIntegerField(blank=True, null=True)
    tata_cliq = models.PositiveIntegerField(blank=True, null=True)
    reliance_digital = models.PositiveIntegerField(blank=True, null=True)
    priceURL = models.OneToOneField(PriceURL, on_delete=models.CASCADE)


class VariantColor(models.Model):
    mobile_color = models.CharField(max_length=50)
    price_variant = models.OneToOneField(OnlinePrice, on_delete=models.CASCADE)


class MobileVariant(models.Model):
    mobileNames = models.ForeignKey(MobileName, on_delete=models.CASCADE, related_name='mobileName')
    mobile_variants = models.CharField(max_length=20)
    image_credit = models.URLField(max_length=200)

    variantImage = models.ForeignKey(VariantImage, on_delete=models.CASCADE)
    variantColor = models.ForeignKey(VariantColor, on_delete=models.CASCADE)
    mobileGeneral = models.OneToOneField(MobileGeneral, on_delete=models.CASCADE)
    mobilePerformance = models.OneToOneField(MobilePerformance, on_delete=models.CASCADE)
    mobileStorage = models.OneToOneField(MobileStorage, on_delete=models.CASCADE)
    mobileCamera = models.OneToOneField(MobileCamera, on_delete=models.CASCADE)
    mobileBattery = models.OneToOneField(MobileBattery, on_delete=models.CASCADE)
    mobileDisplay = models.OneToOneField(MobileDisplay, on_delete=models.CASCADE)
    mobileSensor = models.OneToOneField(MobileSensor, on_delete=models.CASCADE)
    otherFeature = models.OneToOneField(OtherFeature, on_delete=models.CASCADE)


class MobileConnectivity(models.Model):
    mobileVariant = models.ForeignKey(MobileVariant, on_delete=models.CASCADE)
    SIM_CHOICES = (
        ('SIM 1', 'SIM 1'),
        ('SIM 2', 'SIM 2'),
        ('SIM 3', 'SIM 3'),
    )
    sim_name = models.CharField(max_length=1, choices=SIM_CHOICES)
    audio_jack = models.CharField(max_length=30, default='3.5 mm')
    USB_type_c = models.BooleanField(blank=True, null=True, default=True)
    mobileConnectivity = models.OneToOneField(MobileConnectivityDetails, on_delete=models.CASCADE)



