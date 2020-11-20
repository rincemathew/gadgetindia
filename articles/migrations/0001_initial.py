# Generated by Django 2.2.15 on 2020-11-20 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_name', models.CharField(max_length=500)),
                ('released_or_not', models.BooleanField(default=False)),
                ('release_date', models.DateField()),
                ('type', models.CharField(choices=[('static', 'STATIC'), ('dynamic', 'DYNAMIC')], default='dynamic', max_length=50)),
                ('article_type', models.CharField(choices=[('news', 'NEWS'), ('howto', 'HOW TO'), ('reviews', 'REVIEWS'), ('article', 'ARTICLE')], default='news', max_length=50)),
                ('article_thumbnail', models.ImageField(blank=True, null=True, upload_to='article-thumbnail/')),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_images', models.ImageField(blank=True, null=True, upload_to='article-images/')),
                ('articles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Articles')),
            ],
        ),
    ]