from django.db import models


class BrandName(models.Model):
    brand_name = models.CharField(max_length=30, unique=True)
    brand_logo = models.ImageField(upload_to='brand-logo/', blank=True, null=True)

    def __str__(self):
        return self.brand_name


class MobileName(models.Model):
    brandName = models.ForeignKey(BrandName, on_delete=models.CASCADE, related_name='mobiles_name')
    mobile_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.mobile_name


# class MobileGeneral(models.Model):
#     OS_CHOICES = (
#         ('ANDROID', 'Android'),
#         ('IOS', 'ios'),
#     )
#     release_date = models.DateTimeField(blank=True, null=True)
#     os = models.CharField(max_length=1, choices=OS_CHOICES)
#     os_version = models.CharField(max_length=10, null=True, blank=True)
#     price = models.IntegerField(blank=True, null=True)
#     is_available = models.BooleanField(max_length=None, default=True)
#
#
# class MobilePerformance(models.Model):
#     ram = models.IntegerField()
#     processor = models.CharField()
#     processor_company = models.CharField()


class MobileStorage(models.Model):
    device_storage = models.IntegerField()
    expandable_memory = models.BooleanField(default=True)
    expandable_memory_capacity = models.IntegerField()
    OTG_support = models.BooleanField()


# class MobileCamera(models.Model):
#     primary_camera = models.IntegerField()
#
#
# class MobileBattery(models.Model):
#     battery_capacity = models.IntegerField()
#
#
# class MobileSensors(models.Model):
#     fingerprint_sensor = models.BooleanField(default=True)


class MobileVariants(models.Model):
    mobileNames = models.ForeignKey(MobileName, on_delete=models.CASCADE, related_name='mobileName')
    mobile_variants = models.CharField(max_length=20)

    mobileStorage = models.OneToOneField(MobileStorage, on_delete=models.CASCADE)
    # launch_date = models.DateTimeField(auto_now=False, auto_now_add=False)




