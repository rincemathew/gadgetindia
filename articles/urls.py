from django.urls import path
from . import views

urlpatterns = [
    path('listarticles/', views.ArticleListView.as_view()),
    path('article/', views.ArticleView.as_view()),
]

