from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt

from . import views, viewsnormal

urlpatterns = [
    path('', viewsnormal.home_view),
    path('search_query', csrf_exempt(viewsnormal.search_query), name='search_query'),
    # path('paragraph/', viewsnormal.search_query, name='paragraph'),
    path('search/', views.SearchResultView.as_view()),   #rest api
    path('mobiles/', views.MobileResultsView.as_view()),  #rest api
    path('mobile/', views.MobileDetailedResultsView.as_view()),  #rest api
    path('compare-phone/', viewsnormal.compare_view),
    path('<slug:brand_url>/<slug:mobile_url>/', viewsnormal.mobiles_details),
    # re_path(r'^(?P<brand_url>[\w-]+)/(?P<mobile_url>[\w-]+)/$', viewsnormal.mobiles_details),
    path('<slug:listmobile>/', viewsnormal.mobiles_list),
]

