from django.urls import path
from . import views

urlpatterns = [
    path('', views.ear_home_view),
    path('<slug:ear_brand_url>/<slug:ear_url>/', views.ear_detailed_view),
    path('<slug:ear_brand_url>/<slug:ear_url>/amp', views.ear_detailed_view_amp),
]

