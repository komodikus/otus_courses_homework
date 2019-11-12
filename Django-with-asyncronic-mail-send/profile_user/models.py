from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import signals
import uuid
from profile_user.tasks import send_verification_email



class Profile(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='persons', blank=True, verbose_name='Фото пользователя')
    url_to_vk = models.CharField(blank=True, max_length=50)
    url_to_git = models.CharField(blank=True, max_length=50)
    email = models.EmailField('email', unique=True, blank=False, null=False)
    is_verified = models.BooleanField('verified', default=False)
    verification_uuid = models.UUIDField('Unique Verification UUID', default=uuid.uuid4)


    def __str__(self):
        return self.username


def user_post_save(sender, instance, signal, *args, **kwargs):
    if not instance.is_verified:
        send_verification_email.delay(instance.pk)


signals.post_save.connect(user_post_save, sender=Profile)
