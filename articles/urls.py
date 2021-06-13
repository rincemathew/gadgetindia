from django.urls import path
from . import views

urlpatterns = [
    path('listarticles/', views.ArticleListView.as_view()),  #rest api
    path('article/', views.ArticleView.as_view()),  #rest api
    path('rssfeed/', views.rss_feed),
    path('feedrss/', views.feed_rss),
    path('', views.article_home_view),
    path('<slug:articlename>/', views.dynamic_article),
    path('<slug:articlename>/amp', views.dynamic_article_amp),
]

