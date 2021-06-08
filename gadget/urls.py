"""gadget URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mobiles/', include('mobiles.urls')),
    path('articles/', include('articles.urls')),
    path('earwear/', include('earwear.urls')),
    path('', include('mobiles.urls')),
    path('sitemap.xml', TemplateView.as_view(template_name='sitemaps/sitemap.xml', content_type='text/xml')),
    path('sitemap-articles.xml', TemplateView.as_view(template_name='sitemaps/sitemap-articles.xml', content_type='text/xml')),
    path('sitemap-common-urls.xml', TemplateView.as_view(template_name='sitemaps/sitemap-common-urls.xml', content_type='text/xml')),
    path('sitemap-mobile-list21.xml', TemplateView.as_view(template_name='sitemaps/sitemap-mobile-list21.xml', content_type='text/xml')),
    path('article-how.xml', TemplateView.as_view(template_name='sitemaps/article-how.xml', content_type='text/xml')),
    path('sitemap-common-urls2.xml', TemplateView.as_view(template_name='sitemaps/sitemap-common-urls2.xml', content_type='text/xml')),
    path('earwear-list.xml', TemplateView.as_view(template_name='sitemaps/earwear-list.xml', content_type='text/xml')),
]
