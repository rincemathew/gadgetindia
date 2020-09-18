from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.SearchResultView.as_view()),
    # path('test/', views.Test.as_view()),
    path('mobiles/', views.MobileDetailedResultsView.as_view()),
]

