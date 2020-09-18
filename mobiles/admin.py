from django.contrib import admin
from . import models

admin.site.register(models.BrandName)
admin.site.register(models.MobileName)


class VariantImageInline(admin.StackedInline):
    model = models.VariantImage
    # extra = 15  # If you have a fixed number number of answers, set it here.


class VariantColorInline(admin.StackedInline):
    model = models.VariantColor


@admin.register(models.MobileVariant)
class MobileVariantAdmin(admin.ModelAdmin):
    list_display = ['mobile_variants', 'mobileNames', 'brand_name_value']
    inlines = [VariantImageInline, VariantColorInline]

    def brand_name_value(self, obj):
        return obj.mobileNames.brandName
    brand_name_value.admin_order_field = 'mobileNames'  # Allows column order sorting
    brand_name_value.short_description = 'brandName'  # Renames column head


class MobileConnectivityDetailsInline(admin.StackedInline):
    model = models.MobileConnectivityDetails


@admin.register(models.MobileConnectivity)
class MobileVariantAdmin(admin.ModelAdmin):
    inlines = [MobileConnectivityDetailsInline]


admin.site.register(models.MobileGeneral)
admin.site.register(models.MobilePerformance)
admin.site.register(models.MobileStorage)
admin.site.register(models.MobileCamera)
admin.site.register(models.MobileBattery)
admin.site.register(models.MobileDisplay)
admin.site.register(models.MobileConnectivityDetails)
admin.site.register(models.MobileSensor)
admin.site.register(models.OtherFeature)
admin.site.register(models.VariantImage)
admin.site.register(models.OnlinePrice)
admin.site.register(models.VariantColor)
