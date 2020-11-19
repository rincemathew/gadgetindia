from rest_framework import serializers
from . import models


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BrandName
        fields = ['brand_name', ]


class MobileNameSerializer(serializers.ModelSerializer):
    brandName = BrandSerializer(many=False)

    class Meta:
        model = models.MobileName
        fields = ['mobile_name', 'mobile_image', 'phone_type', 'brandName', ]


class MobileGeneralSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = models.MobileGeneral
        fields = ['release_date', 'os', 'price']


class MobilePerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MobilePerformance
        fields = ['ram', 'processor', ]


class MobileStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MobileStorage
        fields = ['device_storage', ]


class MobileCameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MobileCamera
        fields = ['primary_camera', 'secondary_camera', ]


class MobileBatterySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MobileBattery
        fields = ['battery_capacity', ]


class MobileDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MobileDisplay
        fields = ['screen_size', 'resolution', ]


class MobileConnectivityDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MobileConnectivityDetails
        fields = ['sim_name', 'five_g', 'four_g', 'VoLTE', 'three_g', 'two_g', ]


class MobileConnectivitySerializer(serializers.ModelSerializer):
    mobile_connectivity_details = MobileConnectivityDetailsSerializer(many=True)

    class Meta:
        model = models.MobileConnectivity
        fields = ['USB_type_c', 'mobile_connectivity_details', ]


class MobileSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MobileSensor
        fields = ['fingerprint_sensor', ]


class OtherFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OtherFeature
        fields = ['other_Feature', ]


class OnlinePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OnlinePrice
        fields = ['flipkart', ]


class VariantColorSerializer(serializers.ModelSerializer):
    price_variant = OnlinePriceSerializer(many=False)

    class Meta:
        model = models.VariantColor
        fields = ['mobile_color', 'price_variant', ]


class MobileResults(serializers.ModelSerializer):
    mobileNames = MobileNameSerializer(many=False)
    mobileGeneral = MobileGeneralSerializerAll(many=False)
    mobilePerformance = MobilePerformanceSerializer(many=False)
    mobileStorage = MobileStorageSerializer(many=False)
    mobileCamera = MobileCameraSerializer(many=False)
    mobileBattery = MobileBatterySerializer(many=False)
    mobileDisplay = MobileDisplaySerializer(many=False)
    mobileConnectivity = MobileConnectivitySerializer(many=False)
    mobileSensor = MobileSensorSerializer(many=False)
    otherFeature = OtherFeatureSerializer(many=False)
    variant_Color = VariantColorSerializer(many=True)

    class Meta:
        model = models.MobileVariant
        fields = ['mobile_variants', 'mobileNames', 'mobileGeneral', 'mobilePerformance',
                  'mobileStorage', 'mobileCamera', 'mobileBattery', 'mobileDisplay',
                  'mobileConnectivity', 'mobileSensor', 'otherFeature', 'variant_Color', ]
