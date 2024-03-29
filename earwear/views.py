import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render

from earwear.models import EarModelName


def ear_home_view(request):
    ear_wear_list_a = EarModelName.objects.filter(Q(ear_availability=True) & Q(ear_status='Available')).order_by("-ear_release_date")
    page = request.GET.get('page', 1)

    paginator = Paginator(ear_wear_list_a, 8)
    try:
        ear_wear_list = paginator.page(page)
    except PageNotAnInteger:
        ear_wear_list = paginator.page(1)
    except EmptyPage:
        ear_wear_list = paginator.page(paginator.num_pages)
    return render(request, "earwear/earwear_home.html", {'ear_wear_list': ear_wear_list, })


def ear_detailed_view(request, ear_brand_url, ear_url):
    ear_wear_list = EarModelName.objects.filter(Q(ear_availability=True) & Q(earBrandName__ear_brand_name_url=ear_brand_url) & Q(ear_name_url=ear_url))
    option_list = EarModelName.objects.filter(Q(ear_availability=True) & ~Q(ear_name_url=ear_url)).order_by("-ear_release_date")[:20]
    option_random = random.sample(list(option_list), 6)
    print(ear_wear_list)
    return render(request, "earwear/earwear_detailed_view.html", {'ear_wear_list': ear_wear_list, 'option_random':option_random})


def ear_detailed_view_amp(request, ear_brand_url, ear_url):
    ear_wear_list = EarModelName.objects.filter(Q(ear_availability=True) & Q(earBrandName__ear_brand_name_url=ear_brand_url) & Q(ear_name_url=ear_url))
    option_list = EarModelName.objects.filter(Q(ear_availability=True) & ~Q(ear_name_url=ear_url)).order_by("-ear_release_date")[:20]
    option_random = random.sample(list(option_list), 6)
    print(ear_wear_list)
    return render(request, "earwear/earwear_detailed_viewamp.html", {'ear_wear_list': ear_wear_list, 'option_random':option_random})