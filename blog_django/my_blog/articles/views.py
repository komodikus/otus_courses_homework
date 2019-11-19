from django.shortcuts import render
from django.views import View
from articles.models import ArticleModel


# Create your views here.

class ArticleView(View):

    def get(self, request, **kwargs):
        my_article = ArticleModel.objects.get(slug=kwargs["slug"])
        return render(request, "articles/articles.html", context={"article": my_article,
                                                                  "title": my_article.title})


class IndexView(View):

    def get(self, request):
        template_name = "my_blog/index.html"
        last_four_articles = ArticleModel.objects.order_by('-publication_date')[1:6]
        last_article = ArticleModel.objects.latest('publication_date')

        return render(request, template_name,
                      context={'title': 'Main page', 'last_four_articles': last_four_articles, 'last_article': last_article})


class CategoryView(View):

    def get(self, request, **kwargs):
        template_name = "articles/category.html"
        my_art = ArticleModel.objects.filter(theme=kwargs["name_category"])
        return render(request, template_name, context={"articles":my_art})
