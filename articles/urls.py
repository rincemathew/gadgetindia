from django.urls import path
from . import views

urlpatterns = [
    path('listarticles/', views.ArticleListView.as_view()),  #rest api
    path('article/', views.ArticleView.as_view()),  #rest api
    path('', views.article_home_view),
    path('<slug:articlename>/', views.dynamic_article),
]

