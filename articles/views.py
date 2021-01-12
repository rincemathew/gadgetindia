from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from . import models
from . import serializer
from rest_framework.pagination import LimitOffsetPagination


class ProductPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class ArticleView(ListAPIView):
    queryset = models.Articles.objects.all()
    serializer_class = serializer.ArticleSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('id', 'article_name')
    filter_fields = \
        {
            'article_name': ['exact'],
            'article_name_url': ['exact'],
            'id': ['exact'],
        }


class ArticleListView(ListAPIView):
    queryset = models.Articles.objects.order_by('-release_date').filter(released_or_not=True,type='dynamic')
    serializer_class = serializer.ArticleListSerializer
    filter_backends = (DjangoFilterBackend, )
    pagination_class = ProductPagination
    filter_fields = \
        {
            # 'type': ['exact'],
            'article_type': ['exact'],
            'article_name_url': ['exact'],
        }

