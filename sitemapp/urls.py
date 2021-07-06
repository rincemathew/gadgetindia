from django.urls import path

from . import views

urlpatterns = [
    path('article-how.xml', views.how_article),
    path('sitemap-articles.xml', views.news_article),
    path('sitemap-common-urls.xml', views.common),
    path('sitemap-mobile-list21.xml', views.mobiles),
    path('sitemap-common-urls2.xml', views.common_two),
    path('earwear-list.xml', views.earwear),
    path('wearable-list.xml', views.wearables),
   ]



