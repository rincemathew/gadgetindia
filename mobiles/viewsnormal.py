import json

from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from django.db.models import Max

from mobiles.models import MobileName, MobileVariant


def home_view(request):
    budget_mobiles = MobileVariant.objects.filter(Q(mobileGeneral__price__gte=9000) & Q(mobileGeneral__price__lte=11500)).order_by("-mobileGeneral__release_date")
    latest_mobiles = MobileName.objects.all().annotate(latest=Max('mobile_Variant__mobileGeneral__release_date')).order_by("-latest")[:10]
    # latest = MobileVariant.objects.all().order_by("-mobileGeneral__release_date")
    return render(request, "index.html", {'latest_mobiles': latest_mobiles, 'budget_mobiles': budget_mobiles, })


def search_query(request):
    if request.method == 'POST':
        query = json.loads(request.body).get('searchText')
        # query = request.GET.get("q", "real")
        queryset_list = MobileName.objects.filter(Q(mobile_name__icontains=query) | Q(brandName__brand_name__icontains=query)).distinct()
        data = queryset_list.values()
        return JsonResponse(list(data), safe=False)


# def latestMobile(request):
#     queryset_list = MobileName.objects.filter(Q(mobile_name__icontains=query) | Q(brandName__brand_name__icontains=query)).distinct()
#     return render(request, "mobiledetails.html", {'queryset_list': queryset_list, })