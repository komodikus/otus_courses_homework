import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site_with_courses.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
app = Celery('profile_user')

app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'send-mail-each-two-hours': {
        'task': 'lesson.tasks.send_mail_lesson',
        'schedule': crontab(hour=2),
    },
}