from django.urls import path
from . import views


urlpatterns = [
    path('', views.wear_home_view),
    path('<slug:wear_brand_url>/<slug:wear_url>/', views.wear_detailed_view),
]

