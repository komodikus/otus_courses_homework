from django.db import models
from django.contrib.auth.models import AbstractUser



class Profile(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='persons', blank=True, verbose_name='Фото пользователя')
    url_to_vk = models.CharField(blank=True, max_length=50)
    url_to_git = models.CharField(blank=True, max_length=50)
    def __str__(self):
        return self.username


