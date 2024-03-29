# Generated by Django 2.2.15 on 2021-06-01 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0019_auto_20210322_1339'),
        ('articles', '0005_articles_article_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='which_mobile',
            field=models.ManyToManyField(blank=True, null=True, to='mobiles.MobileVariant'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='article_type',
            field=models.CharField(blank=True, choices=[('news', 'NEWS'), ('howto', 'HOW TO'), ('reviews', 'REVIEWS'), ('article', 'ARTICLE'), ('weekly news', 'WEEKLY NEWS')], default='news', max_length=50, null=True),
        ),
    ]
