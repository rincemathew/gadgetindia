from datetime import date

from django.db.models import Q, Max
from django.shortcuts import render

from articles.models import Articles
from earwear.models import EarModelName
from mobiles.models import MobileName
from sitemapp.models import TimeFields
from wearable.models import WearModelName


def how_article(request):
    articles_list = Articles.objects.filter(Q(released_or_not=True) & Q(type='dynamic') & Q(article_type='howto') | Q(article_type='article')).order_by("-release_date", "-release_time")
    time_value = TimeFields.objects.all()
    return render(request, "sitemaps/article-how.xml", {'articles_list': articles_list, 'time_value': time_value }, content_type='application/xml; charset=utf-8')


def news_article(request):
    articles_list = Articles.objects.filter(Q(released_or_not=True) & Q(type='dynamic') & Q(article_type='news') | Q(article_type='reviews') | Q(article_type='weekly news')).order_by("-release_date", "-release_time")
    time_value = TimeFields.objects.all()
    return render(request, "sitemaps/article-how.xml", {'articles_list': articles_list, 'time_value': time_value }, content_type='application/xml; charset=utf-8')


def earwear(request):
    earwear_list = EarModelName.objects.filter(Q(ear_availability=True) & Q(ear_status='Available') | Q(ear_status='Upcoming')).order_by("-ear_release_date")
    time_value = TimeFields.objects.all()
    return render(request, "sitemaps/earwear-list.xml", {'earwear_list': earwear_list, 'time_value': time_value }, content_type='application/xml; charset=utf-8')


def wearables(request):
    wearable_list = WearModelName.objects.filter(Q(wear_availability=True) & Q(wear_status='Available') | Q(wear_status='Upcoming')).order_by("-wear_release_date")
    time_value = TimeFields.objects.all()
    return render(request, "sitemaps/wearable-list.xml", {'wearable_list': wearable_list, 'time_value': time_value }, content_type='application/xml; charset=utf-8')


def mobiles(request):
    mobiles_list = MobileName.objects.filter(Q(mobile_Variant__mobileGeneral__status='Available') | Q(mobile_Variant__mobileGeneral__status='Rumored') | Q(mobile_Variant__mobileGeneral__status='Upcoming') & Q(mobile_Variant__mobileGeneral__is_available=True) & Q(phone_type='SMARTPHONE')).annotate(latest=Max('mobile_Variant__mobileGeneral__release_date')).order_by("-latest")
    time_value = TimeFields.objects.all()
    return render(request, "sitemaps/sitemap-mobile-list21.xml", {'mobiles_list': mobiles_list, 'time_value': time_value }, content_type='application/xml; charset=utf-8')


def common(request):
    time_value = date.today()
    return render(request, "sitemaps/sitemap-common-urls.xml", {'time_value': time_value, }, content_type='application/xml; charset=utf-8')


def common_two(request):
    time_value = date.today()
    return render(request, "sitemaps/sitemap-common-urls2.xml", {'time_value': time_value, }, content_type='application/xml; charset=utf-8')