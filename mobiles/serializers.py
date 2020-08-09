from rest_framework import serializers
from .models import BrandName


class SearchResults(serializers.ModelSerializer):
    class Meta:
        model = BrandName
        fields = ['brand_name',]
