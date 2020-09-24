from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from . import models
from . import serializers, serializerone
from rest_framework.pagination import LimitOffsetPagination


class ProductPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class SearchResultView(ListAPIView):
    queryset = models.MobileVariant.objects.all()
    serializer_class = serializers.SearchResults
    filter_backends = (SearchFilter,)
    search_fields = ('mobileNames__mobile_name', 'mobileNames__brandName__brand_name')


class MobileResultsView(ListAPIView):
    queryset = models.MobileVariant.objects.all()
    serializer_class = serializerone.MobileResults
    filter_backends = (DjangoFilterBackend, )
    pagination_class = ProductPagination
    filter_fields = \
        {
            'mobileNames__brandName__brand_name': ['exact'],
            'mobileNames__phone_type': ['exact'],
            'mobileGeneral__price': ['gte', 'lte', 'exact'],
            'mobileStorage__device_storage': ['gte', 'lte', 'exact'],
            'mobilePerformance__ram': ['gte', 'lte', 'exact'],
            'mobileGeneral__release_date': ['gte', 'lte', 'exact', 'range'],
            # "2020-09-30T12:00:00+05:30"
        }


class MobileDetailedResultsView(ListAPIView):
    queryset = models.MobileVariant.objects.all()
    serializer_class = serializers.MobileDetailedResults
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('mobileNames__mobile_name', 'mobileNames__brandName__brand_name')
    filter_fields = \
        {
            'mobileNames__mobile_name': ['exact'],
            'mobileNames__brandName__brand_name': ['exact'],
            'mobile_variants': ['exact'], 'mobileNames__phone_type': ['exact'],
        }


# class Test(ListAPIView):
#     queryset = models.MobileVariant.objects.all()
#     serializer_class = serializers.MobileVariantSerializer
