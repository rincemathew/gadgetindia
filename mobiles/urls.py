from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.SearchResultView.as_view()),
    path('mobiles/', views.MobileResultsView.as_view()),
    path('mobile/', views.MobileDetailedResultsView.as_view()),
]

