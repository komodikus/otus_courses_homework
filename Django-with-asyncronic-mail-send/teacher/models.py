from django.db import models


# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=600)

    def __str__(self):
        return "Имя: {}".format(self.name)

    class Meta:
        verbose_name = "Преподователь"
        verbose_name_plural = "Преподователи"
