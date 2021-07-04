from django.contrib import admin
from . import models


admin.site.register(models.WearDimensions)
admin.site.register(models.WearConnectivity)
admin.site.register(models.WearDisplay)
admin.site.register(models.WearOnlinePrice)
admin.site.register(models.WearBrandName)


class WearVariantInline(admin.StackedInline):
    model = models.WearVariantImage


@admin.register(models.WearModelName)
class WearModelNameAdmin(admin.ModelAdmin):
    list_display = ['wear_name', 'wearBrandName', 'wear_price']
    inlines = [WearVariantInline]
