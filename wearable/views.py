import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render

from wearable.models import WearModelName


def wear_home_view(request):
    wear_wear_list_a = WearModelName.objects.filter(Q(wear_availability=True) & Q(wear_status='Available')).order_by("-wear_release_date")
    page = request.GET.get('page', 1)

    paginator = Paginator(wear_wear_list_a, 8)
    try:
        wear_wear_list = paginator.page(page)
    except PageNotAnInteger:
        wear_wear_list = paginator.page(1)
    except EmptyPage:
        wear_wear_list = paginator.page(paginator.num_pages)
    return render(request, "wearables/wearhomeview.html", {'wear_wear_list': wear_wear_list, })


def wear_detailed_view(request, wear_brand_url, wear_url):
    wear_wear_list = WearModelName.objects.filter(Q(wear_availability=True) & Q(wearBrandName__wear_brand_name_url=wear_brand_url) & Q(wear_name_url=wear_url))
    option_list = WearModelName.objects.filter(Q(wear_availability=True) & ~Q(wear_name_url=wear_url)).order_by("-wear_release_date")[:20]
    option_random = random.sample(list(option_list), 2)
    return render(request, "wearables/wear_detailed_view.html", {'wear_wear_list': wear_wear_list, 'option_random': option_random})


def wear_detailed_view_amp(request, wear_brand_url, wear_url):
    wear_wear_list = WearModelName.objects.filter(Q(wear_availability=True) & Q(wearBrandName__wear_brand_name_url=wear_brand_url) & Q(wear_name_url=wear_url))
    option_list = WearModelName.objects.filter(Q(wear_availability=True) & ~Q(wear_name_url=wear_url)).order_by("-wear_release_date")[:20]
    option_random = random.sample(list(option_list), 2)
    return render(request, "wearables/wear_detailed_viewamp.html", {'wear_wear_list': wear_wear_list, 'option_random': option_random})