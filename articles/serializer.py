from rest_framework import serializers
from . import models


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Articles
        fields = ['id', 'article_name', 'article_name_url', 'release_date', 'type', 'article_type', 'article_thumbnail', ]


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Articles
        fields = '__all__'


