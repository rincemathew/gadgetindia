from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import BrandName, MobileName
from .serializers import SearchResults, NameSerializer


class SearchView(ListAPIView):
    queryset = MobileName.objects.all()
    serializer_class = NameSerializer
    # filter_backends = (SearchFilter, DjangoFilterBackend)
    # search_fields = ('mobile_name', 'brandName__brand_name')
    # filter_fields = \
    #     {
    #         'id': [], 'mobile_name': ['exact'],
    #         'test_bool': ['exact'], 'test_int': ['gte', 'lte', 'exact'], 'brandName__brand_name': ['exact'],
    #     }

# class SearchView(ListAPIView):
#     queryset = BrandName.objects.all()
#     serializer_class = NameSerializer
#     filter_backends = (SearchFilter,)
#     search_fields = ('brand_name', 'mobiles_name__mobile_name')
