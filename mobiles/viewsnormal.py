import json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from django.db.models import Max

from mobiles.models import MobileName, MobileVariant, BrandName
from articles.models import Articles
from . import listcontent


def home_view(request):
    budget_mobiles = MobileVariant.objects.filter(Q(mobileGeneral__price__gte=9000) & Q(mobileGeneral__price__lte=11500) & Q(mobileGeneral__status='Available') & Q(mobileGeneral__is_available=True) & Q(mobileNames__phone_type='SMARTPHONE')).order_by("-mobileGeneral__release_date")[:10]
    latest_mobiles = MobileName.objects.filter(Q(mobile_Variant__mobileGeneral__status='Available') & Q(mobile_Variant__mobileGeneral__is_available=True) & Q(phone_type='SMARTPHONE')).annotate(latest=Max('mobile_Variant__mobileGeneral__release_date')).order_by("-latest")[:10]
    articles_list = Articles.objects.filter(Q(released_or_not=True) & Q(type='dynamic')).order_by("-release_date")[:10]
    return render(request, "index.html", {'latest_mobiles': latest_mobiles, 'budget_mobiles': budget_mobiles,
                                          'articles_list': articles_list, })


def compare_view(request):
    budget_mobiles = MobileVariant.objects.filter(Q(mobileGeneral__price__gte=9000) & Q(mobileGeneral__price__lte=11500) & Q(mobileGeneral__status='Available') & Q(mobileGeneral__is_available=True) & Q(mobileNames__phone_type='SMARTPHONE')).order_by("-mobileGeneral__release_date")[:10]
    return render(request, "compare-phone.html", )


def search_query(request):
    if request.method == 'POST':
        query = json.loads(request.body).get('searchText')
        queryset_list = MobileVariant.objects.filter(Q(mobileNames__mobile_name__icontains=query) | Q(mobileNames__brandName__brand_name__icontains=query)).distinct()
        data = queryset_list.values('mobile_variants', 'mobile_variants_url', 'mobileNames__brandName__brand_name', 'mobileNames__brandName__brand_name_url', 'mobileNames__mobile_name', 'mobileNames__mobile_name_url', 'mobileNames__mobile_image', 'mobileGeneral__price')
        return JsonResponse(list(data), safe=False)


def mobiles_details(request, brand_url, mobile_url):
    variant = request.GET.get('variant', '')
    mobile_details = MobileVariant.objects.filter(Q(mobileNames__brandName__brand_name_url=brand_url) & Q(mobileNames__mobile_name_url=mobile_url))
    if mobile_details:
        return render(request, "mobiledetails.html", {'mobile_details': mobile_details, 'variant': variant })
    else:
        return render(request, "404.html", )


def mobiles_list(request, listmobile):
    static_a = ["aboutus", "contactus", "sitemap", "privacypolicy", "termsandconditions"]
    other_urls = ["latest-phones", "budget-phones", "smartphones", "tablets"]
    if listmobile in static_a:
        static_articles = Articles.objects.filter(
            Q(released_or_not=True) & Q(article_name_url=listmobile))
        return render(request, "articles/staticarticles.html", {'static_articles': static_articles, })
    elif listmobile in [li['name'] for li in listcontent.brand_name_values]:
        dic_of_list = next(item for item in listcontent.brand_name_values if item["name"] == listmobile)
        heading = dic_of_list['heading']
        title = dic_of_list['title']
        description = dic_of_list['description']
        mobile_list_a = MobileVariant.objects.filter(Q(mobileNames__brandName__brand_name_url=listmobile) & Q(mobileGeneral__is_available=True)).order_by("-mobileGeneral__release_date")
        page = request.GET.get('page', 1)

        paginator = Paginator(mobile_list_a, 10)
        try:
            mobile_list = paginator.page(page)
        except PageNotAnInteger:
            mobile_list = paginator.page(1)
        except EmptyPage:
            mobile_list = paginator.page(paginator.num_pages)
        return render(request, "mobilelist.html", {'mobile_list': mobile_list, 'heading': heading, 'title': title, 'description': description, })
    elif listmobile in other_urls:
        dic_of_list = next(item for item in listcontent.other_list_items if item["name"] == listmobile)
        heading = dic_of_list['heading']
        title = dic_of_list['title']
        description = dic_of_list['description']
        search_content = dic_of_list['filter_set']
        mobile_list_a = MobileVariant.objects.filter(**search_content).order_by("-mobileGeneral__release_date")
        page = request.GET.get('page', 1)

        paginator = Paginator(mobile_list_a, 10)
        try:
            mobile_list = paginator.page(page)
        except PageNotAnInteger:
            mobile_list = paginator.page(1)
        except EmptyPage:
            mobile_list = paginator.page(paginator.num_pages)
        return render(request, "mobilelist.html", {'mobile_list': mobile_list, 'heading': heading, 'title': title, 'description': description, })
    else:
        return render(request, "404.html", )