from django.db import models


class BrandName(models.Model):
    brand_name = models.CharField(max_length=30, unique=True)
    brand_logo = models.ImageField(upload_to='brand-logo/', blank=True, null=True)
    image_credits = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.brand_name


class MobileName(models.Model):
    brandName = models.ForeignKey(BrandName, on_delete=models.CASCADE, related_name='brandName')
    mobile_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.mobile_name


class MobileDetails(models.Model):
    mobileNames = models.ForeignKey(MobileName, on_delete=models.CASCADE, related_name='mobileName')

    mobile_spec = models.CharField(max_length=30)
    is_available = models.BooleanField(max_length=None, default=True)
    launch_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    ram = models.IntegerField()
    battery = models.IntegerField()
    price = models.IntegerField(blank=True, null=True)

