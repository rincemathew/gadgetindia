from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from . import models
from . import serializers


class SearchResultView(ListAPIView):
    queryset = models.MobileVariant.objects.all()
    serializer_class = serializers.SearchResults
    filter_backends = (SearchFilter,)
    # search_fields = ('mobile_name', 'brandName__brand_name')


# class MobileResultsView(ListAPIView):
#     queryset = models.MobileName.objects.all()
#     serializer_class = serializers.MobileResults
#     filter_backends = (SearchFilter, DjangoFilterBackend)
#     search_fields = ('mobile_name', 'brandName__brand_name')
#     filter_fields = \
#         {
#             'id': [], 'mobile_name': ['exact'],
#             'test_bool': ['exact'], 'test_int': ['gte', 'lte', 'exact'], 'brandName__brand_name': ['exact'],
#         }


class MobileDetailedResultsView(ListAPIView):
    queryset = models.MobileVariant.objects.all()
    serializer_class = serializers.MobileDetailedResults
    # filter_backends = (SearchFilter, DjangoFilterBackend)
    # search_fields = ('mobile_name', 'brandName__brand_name')
    # filter_fields = \
    #     {
    #         'mobile_name': ['exact'],
    #         'test_bool': ['exact'], 'test_int': ['gte', 'lte', 'exact'],
    #         'brandName__brand_name': ['exact'],
    #     }


# class Test(ListAPIView):
#     queryset = models.MobileVariant.objects.all()
#     serializer_class = serializers.MobileVariantSerializer
