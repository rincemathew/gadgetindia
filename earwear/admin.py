from django.contrib import admin
from . import models

admin.site.register(models.EarBrandName)
admin.site.register(models.EarOnlinePrice)


class VariantPriceInline(admin.StackedInline):
    model = models.EarOnlinePrice


class VariantImageInline(admin.StackedInline):
    model = models.EarVariantImage


# Register your models here.
@admin.register(models.EarModelName)
class EarModelNameAdmin(admin.ModelAdmin):
    list_display = ['ear_name', 'earBrandName', 'ear_price']
    inlines = [VariantImageInline]
