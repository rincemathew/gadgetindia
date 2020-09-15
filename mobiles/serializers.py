from rest_framework import serializers
from .models import BrandName, MobileName


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandName
        fields = ['brand_name', ]


class NameSerializer(serializers.ModelSerializer):
    brandName = BrandSerializer()

    class Meta:
        model = MobileName
        fields = ['id', 'mobile_name', 'test_bool', 'test_int', 'brandName']


class SearchResults(serializers.ModelSerializer):
    mobiles_name = NameSerializer(many=True)

    class Meta:
        model = BrandName
        fields = ['brand_name', 'mobiles_name']
