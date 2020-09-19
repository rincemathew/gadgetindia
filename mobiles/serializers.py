from rest_framework import serializers
from . import models


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BrandName
        fields = ['brand_name', 'brand_logo' ]


class MobileNameSerializer(serializers.ModelSerializer):
    brandName = BrandSerializer(many=False)

    class Meta:
        model = models.MobileName
        fields = ['mobile_name', 'mobile_image', 'phone_type', 'brandName', ]


class MobileGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MobileGeneral
        fields = ['price', ]


class SearchResults(serializers.ModelSerializer):
    mobileNames = MobileNameSerializer(many=False)
    mobileGeneral = MobileGeneralSerializer(many=False)

    class Meta:
        model = models.MobileVariant
        fields = ['mobile_variants', 'mobileNames', 'mobileGeneral']


# class MobileResults(serializers.ModelSerializer):
#     brandName = BrandSerializer(many=False)
#
#     class Meta:
#         model = models.MobileName
#         fields = ['mobile_name', 'mobile_image', 'brandName', ]


class MobileGeneralSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = models.MobileGeneral
        fields = '__all__'


class MobilePerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MobilePerformance
        fields = '__all__'


class MobileStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MobileStorage
        fields = '__all__'


class MobileCameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MobileCamera
        fields = '__all__'


class MobileBatterySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MobileBattery
        fields = '__all__'


class MobileDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MobileDisplay
        fields = '__all__'


class MobileConnectivityDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MobileConnectivityDetails
        fields = ['sim_name', 'sim_type', 'five_g', 'four_g', 'VoLTE', 'three_g', 'two_g', ]


class MobileConnectivitySerializer(serializers.ModelSerializer):
    mobile_connectivity_details = MobileConnectivityDetailsSerializer(many=True)

    class Meta:
        model = models.MobileConnectivity
        fields = ['SAR_value', 'wi_fi', 'bluetooth', 'GPS',
                  'audio_jack', 'USB_type_c', 'mobile_connectivity_details']


class MobileSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MobileSensor
        fields = '__all__'


class OtherFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OtherFeature
        fields = '__all__'


class OnlinePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OnlinePrice
        fields = '__all__'


class VariantColorSerializer(serializers.ModelSerializer):
    price_variant = OnlinePriceSerializer(many=False)

    class Meta:
        model = models.VariantColor
        fields = ['mobile_color', 'price_variant', ]


class VariantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VariantImage
        fields = ['variant_image']


class MobileDetailedResults(serializers.ModelSerializer):
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
    variant_Image = VariantImageSerializer(many=True)

    class Meta:
        model = models.MobileVariant
        fields = ['mobile_variants', 'mobileNames', 'mobileGeneral', 'mobilePerformance',
                  'mobileStorage', 'mobileCamera', 'mobileBattery', 'mobileDisplay',
                  'mobileConnectivity', 'mobileSensor', 'otherFeature', 'variant_Color', 'variant_Image' ]
