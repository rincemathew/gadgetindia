import json

from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from django.db.models import Max

from mobiles.models import MobileName, MobileVariant, BrandName
from articles.models import Articles


def home_view(request):
    budget_mobiles = MobileVariant.objects.filter(Q(mobileGeneral__price__gte=9000) & Q(mobileGeneral__price__lte=11500)).order_by("-mobileGeneral__release_date")[:10]
    latest_mobiles = MobileName.objects.all().annotate(latest=Max('mobile_Variant__mobileGeneral__release_date')).order_by("-latest")[:10]
    articles_list = Articles.objects.filter(Q(released_or_not=True) & Q(type='dynamic')).order_by("-release_date")[:10]
    return render(request, "index.html", {'latest_mobiles': latest_mobiles, 'budget_mobiles': budget_mobiles,
                                          'articles_list': articles_list, })


def search_query(request):
    if request.method == 'POST':
        query = json.loads(request.body).get('searchText')
        queryset_list = MobileVariant.objects.filter(Q(mobileNames__mobile_name__icontains=query) | Q(mobileNames__brandName__brand_name__icontains=query)).distinct()
        data = queryset_list.values('mobile_variants', 'mobile_variants_url', 'mobileNames__brandName__brand_name', 'mobileNames__brandName__brand_name_url', 'mobileNames__mobile_name', 'mobileNames__mobile_name_url', 'mobileNames__mobile_image', 'mobileGeneral__price')
        return JsonResponse(list(data), safe=False)


# mobiledetailes.html
def mobiles_details(request, brand_url, mobile_url):
    variant = request.GET.get('variant', '')
    variant_unslugified = variant.replace('-', ' ')
    print(variant_unslugified)
    # queryset_list = MobileName.objects.filter(Q(mobile_name__icontains=query) | Q(brandName__brand_name__icontains=query)).distinct()
    mobile_details = MobileVariant.objects.filter(Q(mobileNames__brandName__brand_name_url=brand_url) & Q(mobileNames__mobile_name_url=mobile_url))
    return render(request, "mobiledetails.html", {'mobile_details': mobile_details, 'variant': variant })


# mobilelist.html
def mobiles_list(request, listmobile):
    static_a = ["aboutus", "contactus", "sitemap", "privacypolicy", "termsandconditions"]
    if listmobile in static_a:
        static_articles = Articles.objects.filter(
            Q(released_or_not=True) & Q(article_name_url=listmobile))
        return render(request, "articles/staticarticles.html", {'static_articles': static_articles, })
    else:
        mobile_list = MobileVariant.objects.filter(mobileNames__brandName__brand_name_url=listmobile)
        return render(request, "mobilelist.html", {'mobile_list': mobile_list, })