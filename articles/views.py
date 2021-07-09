import random

from django.db.models import Q, Max
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from mobiles.models import MobileName
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

def dynamic_article_amp(request, articlename):
    dynamic_articles = Articles.objects.filter(Q(released_or_not=True) & Q(type='dynamic') & Q(article_name_url=articlename))
    related_articles_view = Articles.objects.filter(Q(released_or_not=True) & Q(type='dynamic') & ~Q(article_name_url=articlename)).order_by("-release_date", "-release_time")[:10]
    related_articles = random.sample(list(related_articles_view), 3)
    rea_mobiles_list = MobileName.objects.filter(
        Q(mobile_Variant__mobileGeneral__status='Available') & Q(mobile_Variant__mobileGeneral__is_available=True) & Q(
            phone_type='SMARTPHONE')).annotate(latest=Max('mobile_Variant__mobileGeneral__release_date')).order_by(
        "-latest")[:20]
    rea_mobiles = random.sample(list(rea_mobiles_list), 5)
    return render(request, "articles/dynamicarticleamp.html", {'dynamic_articles': dynamic_articles, 'related_articles':related_articles, 'rea_mobiles':rea_mobiles, })


def dynamic_article(request, articlename):
    dynamic_articles = Articles.objects.filter(Q(released_or_not=True) & Q(type='dynamic') & Q(article_name_url=articlename))
    related_articles_view = Articles.objects.filter(Q(released_or_not=True) & Q(type='dynamic') & ~Q(article_name_url=articlename)).order_by("-release_date", "-release_time")[:10]
    related_articles = random.sample(list(related_articles_view), 3)
    rea_mobiles_list = MobileName.objects.filter(Q(mobile_Variant__mobileGeneral__status='Available') & Q(mobile_Variant__mobileGeneral__is_available=True) & Q(phone_type='SMARTPHONE')).annotate(latest=Max('mobile_Variant__mobileGeneral__release_date')).order_by("-latest")[:20]
    rea_mobiles = random.sample(list(rea_mobiles_list), 5)
    return render(request, "articles/dynamicarticle.html", {'dynamic_articles': dynamic_articles, 'related_articles':related_articles ,'rea_mobiles': rea_mobiles, })


def article_home_view(request):
    articles_list = Articles.objects.filter(Q(released_or_not=True) & Q(type='dynamic')).order_by("-release_date")[:5]
    reviews = Articles.objects.filter(Q(released_or_not=True) & Q(type='dynamic') & Q(article_type='reviews')).order_by("-release_date", "-release_time")[:10]
    news = Articles.objects.filter(Q(released_or_not=True) & Q(type='dynamic') & Q(article_type='news')).order_by("-release_date", "-release_time")[:10]
    howto = Articles.objects.filter(Q(released_or_not=True) & Q(type='dynamic') & Q(article_type='howto')).order_by("-release_date", "-release_time")[:10]
    return render(request, "articles/articlehomeview.html", {'articles_list': articles_list, 'howto': howto, 'news': news, 'reviews': reviews, })


def rss_feed(request):
    articles_list = Articles.objects.filter(Q(released_or_not=True) & Q(type='dynamic')).order_by("-release_date", "-release_time")
    return render(request, "articles/rssfeed.xml", {'articles_list': articles_list, }, content_type='text/xml')


def feed_rss(request):
    articles_list = Articles.objects.filter(Q(released_or_not=True) & Q(type='dynamic')).order_by("-release_date", "-release_time")
    return render(request, "articles/feedrss.xml", {'articles_list': articles_list, }, content_type='application/rss+xml; charset=utf-8')

