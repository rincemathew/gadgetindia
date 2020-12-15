from django.db import models

# Create your models here.


class Articles(models.Model):
    TYPE = (
        ('static', 'STATIC'),
        ('dynamic', 'DYNAMIC'),
    )
    ARTICLE_TYPE = (
        ('news', 'NEWS'),
        ('howto', 'HOW TO'),
        ('reviews', 'REVIEWS'),
        ('article', 'ARTICLE'),
    )
    article_name = models.CharField(max_length=254, unique=True)
    article_name_url = models.CharField(max_length=254, )
    released_or_not = models.BooleanField(default=False, )
    release_date = models.DateField(auto_now=False, auto_now_add=False, )
    type = models.CharField(max_length=50, choices=TYPE, default='dynamic')
    article_type = models.CharField(max_length=50, choices=ARTICLE_TYPE, default='news', blank=True, null=True)
    article_thumbnail = models.ImageField(upload_to='article-thumbnail/', blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.article_name


class ArticleImages(models.Model):
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE, )
    article_images = models.ImageField(upload_to='article-images/', blank=True, null=True)
