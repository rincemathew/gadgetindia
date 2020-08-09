from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from .models import BrandName
from .serializers import SearchResults


class SearchView(ListAPIView):
    queryset = BrandName.objects.all()
    serializer_class = SearchResults
    filter_backends = (SearchFilter,)
    search_fields = ('brand_name', )
