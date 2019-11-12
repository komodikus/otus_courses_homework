from django.core.mail import send_mail
from profile_user.celery import app
from lesson.models import Lesson
import datetime


@app.task
def send_mail_lesson():
    latest_lesson = Lesson.objects.latest()
    latest_date = latest_lesson.lesson_date
    now = datetime.date.today()
    remaining_hours = latest_date - now
    studients = latest_lesson.course.studients.all()
    if remaining_hours < datetime.timedelta(hours=2):
        for studient in studients:
            send_mail(
                'Soon ur lesson is start',
                'through 2 hours your lesson is start: '
                'http://localhost:8000/lesson/'.format(latest_lesson.id),
                'from@otuscourses.dev',
                [studient.email],
                fail_silently=False, )