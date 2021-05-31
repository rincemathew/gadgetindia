from django.db.models import Q
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from . import models
from . import serializer
from rest_framework.pagination import LimitOffsetPagination
from articles.models import Articles


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


# pure django

def dynamic_article(request, articlename):
    dynamic_articles = Articles.objects.filter(Q(released_or_not=True) & Q(type='dynamic') & Q(article_name_url=articlename))
    return render(request, "articles/dynamicarticle.html", {'dynamic_articles': dynamic_articles, })


def article_home_view(request):
    articles_list = Articles.objects.filter(Q(released_or_not=True) & Q(type='dynamic')).order_by("-release_date")[:5]
    reviews = Articles.objects.filter(Q(released_or_not=True) & Q(type='dynamic') & Q(article_type='reviews')).order_by("-release_date")[:10]
    news = Articles.objects.filter(Q(released_or_not=True) & Q(type='dynamic') & Q(article_type='news')).order_by("-release_date")[:10]
    howto = Articles.objects.filter(Q(released_or_not=True) & Q(type='dynamic') & Q(article_type='howto')).order_by("-release_date")[:10]
    return render(request, "articles/articlehomeview.html", {'articles_list': articles_list, 'howto': howto, 'news': news, 'reviews': reviews, })


# def article_list_view(request):
#     articles_list = Articles.objects.filter(Q(released_or_not=True) & Q(type='dynamic')).order_by("-release_date")[:10]
#     return render(request, "articlelistview.html", {'articles_list': articles_list, })