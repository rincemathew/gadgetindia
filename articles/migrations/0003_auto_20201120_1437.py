# Generated by Django 2.2.15 on 2020-11-20 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20201120_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='article_type',
            field=models.CharField(blank=True, choices=[('news', 'NEWS'), ('howto', 'HOW TO'), ('reviews', 'REVIEWS'), ('article', 'ARTICLE')], default='news', max_length=50, null=True),
        ),
    ]
