from django.db import models
from martor.models import MartorField
import datetime



# Create your models here.

class ArticleModel(models.Model):
    THEMES_NAMES = (
        ('work', 'Работка'),
        ('projects', 'Мои проекты'),
        ('travels', 'Путешествия'),
        ('mind', 'Мысли о всяком'),
    )
    theme = models.CharField(max_length=20, choices=THEMES_NAMES)

    title = models.fields.CharField(max_length=40)
    sub_title = models.fields.CharField(max_length=80, blank=True)
    text_article = MartorField()
    publication_date = models.fields.DateField()
    description = models.CharField(verbose_name='Description', max_length=200, blank=True)
    # tags =
    slug = models.SlugField(verbose_name='URL', max_length=50, unique=True, )
    image = models.ImageField(verbose_name='Image', upload_to='images/%Y/%m/%d', blank=True)

    @classmethod
    def get_all_themes(cls):
        return [i[1] for i in cls.THEMES_NAMES]

    # @classmethod
    # def get_paginator_curent_page(cls, request):
    #     all_articles = cls.objects.all()
    #     current_page = Paginator(all_articles, 2)
    #     page = request.GET.get('page')
    #     try:
    #         # Если существует, то выбираем эту страницу
    #         current_page = current_page.page(page)
    #     except PageNotAnInteger:
    #         current_page = current_page.page(1)
    #     except EmptyPage:
    #         current_page = current_page.page(current_page.num_pages)
    #     return current_page

    # TODO: Сделать автора форейнкей, сделать коментарии, возможность их оставлять, увеличить Desc, Paginator
    def __str__(self):
        return self.title
