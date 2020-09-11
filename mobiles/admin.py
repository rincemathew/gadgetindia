from django.contrib import admin
from .models import BrandName, MobileName, MobileVariants, MobileStorage

admin.site.register(BrandName)
admin.site.register(MobileName)
admin.site.register(MobileVariants)
admin.site.register(MobileStorage)
