from django.db import models
from django.contrib import admin
from django.forms import TextInput,Textarea
from martor.widgets import AdminMartorWidget

from articles.models import ArticleModel


@admin.register(ArticleModel)
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ["title", "publication_date", "description"]

    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
